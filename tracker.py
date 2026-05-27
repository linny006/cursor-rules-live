"""Update script for cursor-rules-live.

Runs on a cron via .github/workflows/update.yml every 15 minutes.
Fetches the upstream data, ALSO fetches actual .cursorrules content
per item (the value-add — readers can copy-paste), diffs against
data/items.json, rewrites the README between sentinel markers,
writes a new JSON snapshot, regenerates pSEO pages. The workflow
then commits any diff.
"""
from __future__ import annotations

import base64
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx


DATA_FILE = Path("data/items.json")
README_FILE = Path("README.md")
TABLE_START = "<!-- TRACKER_TABLE_START -->"
TABLE_END = "<!-- TRACKER_TABLE_END -->"
LAST_UPDATED_RE = re.compile(r"^> ⏰ Last updated: .+$", re.MULTILINE)
ITEMS_BADGE_RE = re.compile(r"badge/Tracked_Items-\d+-brightgreen")


GITHUB_QUERY = 'topic:cursor-rules sort:updated-desc'
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MAX_ITEMS = 50

# pSEO metadata
REPO_OWNER = "linny006"
REPO_SLUG = "cursor-rules-live"
REPO_TITLE = "Cursor Rules Live"
REPO_BASE_URL = f"https://{REPO_OWNER}.github.io/{REPO_SLUG}"
REPO_TOPIC = "cursor-rules"
REPO_NICHE = "ai-coding"


def _auth_headers() -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        h["Authorization"] = f"token {GITHUB_TOKEN}"
    return h


def fetch_cursorrules_content(full_name: str) -> dict:
    """Try to fetch the actual .cursorrules content from a tracked repo.

    Returns {"path": ..., "content": ..., "format": ...} or {} if not found.

    Tries (in priority order):
    1. /.cursorrules at repo root (classic format)
    2. /cursorrules.json at repo root
    3. /.cursor/rules/*.mdc — pick first .mdc file (new format)
    """
    base = f"https://api.github.com/repos/{full_name}/contents"

    try:
        r = httpx.get(f"{base}/.cursorrules", headers=_auth_headers(), timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data.get("encoding") == "base64":
                content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
                return {"path": ".cursorrules", "content": content[:8000], "format": "text"}
    except Exception:
        pass

    try:
        r = httpx.get(f"{base}/cursorrules.json", headers=_auth_headers(), timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data.get("encoding") == "base64":
                content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
                return {"path": "cursorrules.json", "content": content[:8000], "format": "json"}
    except Exception:
        pass

    try:
        r = httpx.get(f"{base}/.cursor/rules", headers=_auth_headers(), timeout=15)
        if r.status_code == 200:
            files = r.json()
            if isinstance(files, list):
                mdc = next((f for f in files if f.get("name", "").endswith(".mdc")), None)
                if mdc:
                    r2 = httpx.get(mdc["url"], headers=_auth_headers(), timeout=15)
                    if r2.status_code == 200:
                        data = r2.json()
                        if data.get("encoding") == "base64":
                            content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
                            return {
                                "path": f".cursor/rules/{mdc['name']}",
                                "content": content[:8000],
                                "format": "mdc",
                            }
    except Exception:
        pass

    return {}


def fetch_items() -> list[dict]:
    if not GITHUB_TOKEN:
        print("WARN: GITHUB_TOKEN not set; running with anonymous quota")

    url = "https://api.github.com/search/repositories"
    params = {"q": GITHUB_QUERY, "sort": "updated", "order": "desc", "per_page": MAX_ITEMS}
    resp = httpx.get(url, headers=_auth_headers(), params=params, timeout=30)
    resp.raise_for_status()

    # Cache cursorrules content from previous run, keyed by id+updated_at.
    # Skips re-fetching when the source repo hasn't changed since last tick —
    # critical for staying under GitHub Search rate limits (5000/hr per token,
    # we run every 15min so worst case 96*100=9600 calls/day without cache).
    cache: dict[str, tuple[str, dict]] = {}
    if DATA_FILE.exists():
        try:
            prev_items = json.loads(DATA_FILE.read_text())
            for p in prev_items:
                if p.get("cursorrules") and p.get("id"):
                    cache[p["id"]] = (p.get("updated_at", ""), p["cursorrules"])
        except Exception:
            pass

    out: list[dict] = []
    n_fetched = 0
    n_cached = 0
    for r in resp.json().get("items", [])[:MAX_ITEMS]:
        item = {
            "id": r["full_name"],
            "name": r["full_name"],
            "url": r["html_url"],
            "stars": r["stargazers_count"],
            "language": r.get("language") or "—",
            "description": (r.get("description") or "")[:120],
            "updated_at": r["pushed_at"],
        }
        prev_updated, prev_rules = cache.get(item["id"], ("", None))
        if prev_rules and prev_updated == item["updated_at"]:
            item["cursorrules"] = prev_rules
            n_cached += 1
        else:
            content = fetch_cursorrules_content(item["id"])
            if content:
                item["cursorrules"] = content
                n_fetched += 1
        out.append(item)

    n_with = sum(1 for x in out if x.get("cursorrules"))
    print(f"items={len(out)} with_rules={n_with} (fetched={n_fetched}, cached={n_cached})")
    return out


def load_previous() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        return []


def diff_counts(old: list[dict], new: list[dict]) -> tuple[int, int]:
    old_ids = {i["id"] for i in old}
    new_ids = {i["id"] for i in new}
    return len(new_ids - old_ids), len(old_ids - new_ids)


def render_table(items: list[dict]) -> str:
    if not items:
        return "_No items in the upstream feed right now. Next check in 15 minutes._"
    rows = ["| # | Name | ⭐ | Lang | Updated | Rules | Description |",
            "|---|------|---|------|---------|-------|-------------|"]
    for i, it in enumerate(items, 1):
        name = f"[{it['name']}]({it['url']})"
        desc = (it.get("description") or "").replace("|", "\\|")
        updated = it.get("updated_at", "")[:10]
        owner, _, repo = it["name"].partition("/")
        rules_link = (
            f"✅ [view](https://linny006.github.io/cursor-rules-live/r/{owner}/{repo}/)"
            if it.get("cursorrules") else "—"
        )
        rows.append(
            f"| {i} | {name} | {it.get('stars', 0)} | {it.get('language', '—')} | "
            f"{updated} | {rules_link} | {desc} |"
        )
    return "\n".join(rows)


def rewrite_readme(items: list[dict]) -> None:
    txt = README_FILE.read_text()

    table = render_table(items)
    section = f"{TABLE_START}\n{table}\n{TABLE_END}"
    pattern = re.compile(re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END), re.DOTALL)
    txt = pattern.sub(section, txt)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    txt = LAST_UPDATED_RE.sub(f"> ⏰ Last updated: {now}", txt)

    txt = ITEMS_BADGE_RE.sub(f"badge/Tracked_Items-{len(items)}-brightgreen", txt)

    README_FILE.write_text(txt)


def main() -> int:
    items = fetch_items()
    previous = load_previous()
    added, removed = diff_counts(previous, items)

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(items, indent=2, sort_keys=True))
    rewrite_readme(items)

    try:
        import pseo
        meta = {
            "title": REPO_TITLE,
            "base_url": REPO_BASE_URL,
            "topic": REPO_TOPIC,
            "niche_label": REPO_NICHE,
            "update_interval_minutes": 15,
        }
        n_pages = pseo.generate_pages(items, meta)
        print(f"pseo: {n_pages} pages written")
    except Exception as exc:
        print(f"pseo: skipped (error: {exc})")

    now_short = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    msg = f"feat: +{added} added, -{removed} removed ({now_short})"
    print(msg)

    gho = os.environ.get("GITHUB_OUTPUT")
    if gho:
        with open(gho, "a") as f:
            f.write(f"message={msg}\n")
            f.write(f"changed={'true' if (added or removed) else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
