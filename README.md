<!--
SEO: cursor rules live
-->

<div align="center">

# Cursor Rules Live

Live index of cursor-rules files from GitHub, updated every 15 minutes

[![Stars](https://img.shields.io/github/stars/linny006/cursor-rules-live?style=for-the-badge&logo=github)](https://github.com/linny006/cursor-rules-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/cursor-rules-live?style=for-the-badge)](https://github.com/linny006/cursor-rules-live/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-13-brightgreen?style=for-the-badge)](#)
[![Updated](https://img.shields.io/badge/Updates-every_15min-blue?style=for-the-badge)](#)

**⭐ Star this repo to bookmark — fresh data every 15 minutes**

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

</div>

## 🚀 Install in 1 command

```bash
npx github:linny006/cursor-rules-picker
```

Detects your tech stack, ranks compatible rules from the live index below, installs the one you pick. [See cursor-rules-picker →](https://github.com/linny006/cursor-rules-picker)

---


---

## 💡 What is this?

Automatically discovers and indexes .cursorrules and cursorrules.json files across public GitHub repositories every 15 minutes. Surfaces what real teams are using today, with metadata like language, stars, and last-updated timestamps. Outputs a searchable JSON feed and static site for browsing the freshest AI coding rules in the wild.

This list is **auto-updated every 15 minutes** by a GitHub Actions cron.
Each commit reflects a real change in the upstream data source — new items added,
expired items removed — so you can rely on what you see being current.

---

## 📋 Current Items

> ⏰ Last updated: 2026-10-27 10:15 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Rules | Description |
|---|------|---|------|---------|-------|-------------|
| 1 | [fri3ndslab/my-human-has-adhd](https://github.com/fri3ndslab/my-human-has-adhd) | 0 | — | 2026-10-27 | — | An 18-line rules file for Claude Code, Codex and Cursor. Drop an idea mid-task and the agent parks it in PARK.md with th |
| 2 | [Aaditya1273/Agent.md](https://github.com/Aaditya1273/Agent.md) | 11 | — | 2026-10-27 | — | Your AI coding agent follows these files blindly, before it reads a line of your code. |
| 3 | [MnemeHQ/mneme](https://github.com/MnemeHQ/mneme) | 29 | Python | 2026-10-27 | — | Architectural drift prevention for the agentic AI SDLC. |
| 4 | [roedyrustam/vibes-plug](https://github.com/roedyrustam/vibes-plug) | 115 | JavaScript | 2026-10-26 | ✅ [view](https://linny006.github.io/cursor-rules-live/r/roedyrustam/vibes-plug/) | 🌊 Universal AI Agent Swarm & MCP Plugin with 176 specialized skills and 8 autonomous subagents for Antigravity, Claude C |
| 5 | [rover-001/checkmate](https://github.com/rover-001/checkmate) | 9 | JavaScript | 2026-10-26 | — | Goal-driven mode for AI coding agents. Reach the user's win condition in the fewest moves. |
| 6 | [vorlaxen-labs/agent-skills](https://github.com/vorlaxen-labs/agent-skills) | 7 | TypeScript | 2026-10-26 | — | Agent skills CLI: init AGENTS.md, install SKILL.md from any GitHub repo for Cursor, Claude Code, Copilot, Windsurf, Code |
| 7 | [vibestackdev/vibe-stack](https://github.com/vibestackdev/vibe-stack) | 8 | TypeScript | 2026-10-26 | ✅ [view](https://linny006.github.io/cursor-rules-live/r/vibestackdev/vibe-stack/) | 29 .mdc architecture rules that prevent AI coding assistants from hallucinating insecure auth, deprecated imports, and b |
| 8 | [nsozturk/open-agent-db](https://github.com/nsozturk/open-agent-db) | 1 | Python | 2026-10-26 | — | The universal open database and semantic vector search engine for AI Agent Skills, MCP Servers, Project Directives, and  |
| 9 | [orbitalsonic/AndroidPilot](https://github.com/orbitalsonic/AndroidPilot) | 1 | Kotlin | 2026-10-26 | ✅ [view](https://linny006.github.io/cursor-rules-live/r/orbitalsonic/AndroidPilot/) | Production-ready Android Engineering Rules for Cursor and other AI coding assistants. Build consistent, scalable, and ma |
| 10 | [atlaso-labs/cursor](https://github.com/atlaso-labs/cursor) | 0 | TypeScript | 2026-10-26 | — | Persistent memory for Cursor: automatic capture as you work, recall through a generated rules file, the same memory in C |
| 11 | [wangqiqi/cursor-ai](https://github.com/wangqiqi/cursor-ai) | 4 | Shell | 2026-10-26 | — | 无关用户， 无关系统， 无关项目，开箱复制即用！ code faster, code better;  |
| 12 | [scoyoc5/unity-ai-agent-rules](https://github.com/scoyoc5/unity-ai-agent-rules) | 6 | — | 2026-10-25 | ✅ [view](https://linny006.github.io/cursor-rules-live/r/scoyoc5/unity-ai-agent-rules/) | Free Cursor rules + AGENTS.md that stop AI (Cursor, Claude Code, ChatGPT) from writing broken Unity C#: missing usings,  |
| 13 | [danielvm-git/bigpowers](https://github.com/danielvm-git/bigpowers) | 280 | Shell | 2026-10-25 | ✅ [view](https://linny006.github.io/cursor-rules-live/r/danielvm-git/bigpowers/) | Agent skills synthesizing years of software engineering discipline into a prescriptive methodology for solo developers |
<!-- TRACKER_TABLE_END -->

---

## 🔍 How it works

Every 15 minutes, a GitHub Action runs `tracker.py`. That script:

1. Fetches the latest state from `GitHub Search API`.
2. Diffs against `data/items.json` (the previous snapshot).
3. Rewrites the table above between the `<!-- TRACKER_TABLE_* -->` markers.
4. Commits `feat: +N added, -M removed (timestamp)` if anything changed.

No external services. No paid APIs. Just a public data source and a free GitHub Action.

---

## 🤝 Contributing

See `CONTRIBUTING.md` — usually you don't need to: the tracker keeps itself current.
If you spot a data-source bug or want to suggest a new column for the table, open
an issue.

---

## 🔗 Related live trackers

If you find this useful, you might also like these other auto-updated
trackers from the same maintainer — same mechanism, different upstream:

- [trending-claude-skills](https://github.com/linny006/trending-claude-skills) — What's shipping in Claude Skills this week (`topic:claude-skills`)
- [mcp-servers-live](https://github.com/linny006/mcp-servers-live) — Live index of newest MCP servers (`topic:mcp-server`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [skills-tracker](https://github.com/linny006/skills-tracker) — Tracking new GitHub 'skills' repos (`topic:agent-skills`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.
