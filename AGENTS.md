# AGENTS.md

This repository is a **guided installer** for a self-hosted personal AI operating system.

👉 **The full instructions for agents live in [CLAUDE.md](CLAUDE.md). Read that first.**

Short version for any coding agent (Claude Code, Cursor, etc.):

1. This is a menu, not a bundle — **install only what the user explicitly asks for**.
2. Ask discovery questions, draft a tailored plan, then execute one phase at a time **with confirmation**.
3. Follow the playbooks in [`docs/`](docs/) in install order; reuse [`templates/`](templates/),
   [`skills/`](skills/), and [`dashboard/`](dashboard/).
4. Never print or commit secrets. Back up before changing server files. Restart the gateway after changes.

Human readers: start at the [README](README.md) or [docs/00-overview.md](docs/00-overview.md).
