# cursor-rules-live

> Índice ao vivo de arquivos cursor-rules do GitHub, atualizado a cada 15 minutos

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · **Português**

[![Stars](https://img.shields.io/github/stars/linny006/cursor-rules-live?style=for-the-badge&logo=github)](https://github.com/linny006/cursor-rules-live/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006/cursor-rules-live?style=for-the-badge)](https://github.com/linny006/cursor-rules-live/commits)

---

Descobre e indexa automaticamente arquivos `.cursorrules` e `cursorrules.json` em repositórios públicos do GitHub a cada 15 minutos. Mostra o que times reais estão usando hoje, com metadados como linguagem, stars e timestamps de última atualização. Gera um feed JSON pesquisável e um site estático para explorar as regras de codificação com IA mais recentes.

Esta lista é **atualizada automaticamente a cada 15 minutos** por um cron do GitHub Actions. Cada commit reflete uma mudança real na fonte de dados upstream — novos itens adicionados, itens expirados removidos — então você pode confiar que o que vê está sempre atualizado.

---

A cada 15 minutos, uma GitHub Action executa o `tracker.py`. Esse script:

1. Busca o estado mais recente da `GitHub Search API`.
2. Faz diff contra `data/items.json` (o snapshot anterior).
3. Reescreve a tabela entre os marcadores `<!-- TRACKER_TABLE_* -->`.
4. Faz commit de `feat: +N added, -M removed (timestamp)` se algo mudou.

Sem serviços externos. Sem APIs pagas. Só uma fonte de dados pública e uma GitHub Action gratuita.

---

## 📋 Live data

Os dados ao vivo estão no README em inglês

---

## 🔗 Related live trackers

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
