# 🛰️ personal-ai-os

> **Hand this repo to Claude Code, and it will guide you through building your own 24/7 personal AI operating system.**
> A self-hosted personal agent — built on the **[Hermes](https://github.com/nousresearch/hermes-agent)**
> agent — that lives on a tiny VPS and chats with you in the app *you* choose: Telegram, Slack, or
> another channel (WhatsApp, Discord, Signal …). It reads your calendar and email, runs your morning
> briefing, builds its own skills, and turns your documents into a queryable second brain.

`personal-ai-os` is **not** a single app you install. It's a **guided blueprint**: a set of
chronological playbooks plus generalized templates that a coding agent (Claude Code) reads and
then **walks you through, step by step**, asking what you actually want at every stage. At the
end you own a setup like the one this repo was distilled from — running on hardware you control,
for a few euros a month.

```
                 YOU  ──(Telegram / Slack / WhatsApp / …)──►  HERMES AGENT
                                                                  │
                                                  runs 24/7 on your own VPS
                                                                  │
        ┌───────────────────┬───────────────────┼───────────────────┐
        ▼                   ▼                   ▼                   ▼
       LLM                SKILLS             CRON JOBS          SELF-IMPROVE
   DeepSeek (cheap)    calendar · tasks    morning briefing    Claude Code
   or any model via    mail · web ·        + dashboard         rewrites &
   OpenRouter          notes · maps        export              builds skills
                                                  │
                                                  ▼
                              Telegram / Slack   +   Dashboard (Vercel, free)


   ╭──────────────────────────────────────────────────────────────────────────╮
   │   ★  SECOND BRAIN PIPELINE   ──►   your own "LLM WIKI"   (separate repo)   │
   ╰──────────────────────────────────────────────────────────────────────────╯
        your documents & notes                            the agent can now
        (PDF · Word · email · md)                         answer from its wiki
                  │                                                 ▲
                  ▼                                                 │
        Parse ─► Extract ─► Compile ─► Lint  ─────►   brain/  ──────┘
                                                  a queryable Markdown knowledge
                                                  base — no RAG, no chunking,
                                                  no vector DB
```

<sub>The **Second Brain Pipeline** is its own branch and a **separate project with its own repo** —
it compiles your documents into an **"LLM Wiki"** (`brain/`), a plain-Markdown knowledge base the
agent reads directly. Everything else runs on one small VPS.</sub>

---

## ✨ What you get

- **A personal agent on your own VPS** — built on the open-source **[Hermes agent](https://github.com/nousresearch/hermes-agent)** (by NousResearch): an LLM-driven assistant with a *skill* system, a *gateway* that connects chat platforms, and a *cron* scheduler. It runs 24/7 as a `systemd` service; the box costs ~€5–6/mo.
- **Chat in the app you pick** — Telegram or Slack out of the box; WhatsApp Business, Discord, Signal and more as optional add-ons. **Choose one to start.**
- **A cheap, capable brain (the LLM)** — [DeepSeek](https://platform.deepseek.com) by default: a `pro` tier and a ~3× cheaper `flash` tier you switch per message, with images routed to a vision model. Want to shop around? Point it at [OpenRouter](https://openrouter.ai) to A/B different models and **calculate which is most worth it** for your usage.
- **Real productivity skills** — calendar, to-dos/reminders, email triage, web research with sources, YouTube transcripts, maps.
- **A daily morning briefing** — calendar + tasks + unread mail + LLM spend, pushed to your chat every morning.
- **A second brain — your own "LLM Wiki"** — powered by a **whole separate project with its own repo: the [Second Brain Pipeline](https://github.com/lennartduerr/second-brain-pipeline)**. Drop any document (PDF, Word, email…) and it's compiled into a clean, queryable Markdown knowledge base your agent reads like a wiki — **no RAG, no chunking, no vector DB**.
- **A read-only web dashboard** — your briefing at a glance, hosted free on Vercel. You just make a Vercel account; **Claude Code deploys and hosts it for you** (no live LLM cost).
- **A self-improvement loop** — ask the agent to "build me a new skill" and it delegates to Claude Code on the VPS, shows you the diff, and ships it after your OK.

Everything is **opt-in**. You pick the pieces you want; the rest is skipped. (Advanced users can
also wire in workflow automation — see [docs/13](docs/13-n8n-orchestration.md) — but most people won't need it.)

---

## 🚀 Quickstart (the 3-step install)

> 💡 **Just installing once?** Clone it (step 1 below) — that's all you need. **Want to keep and
> customize your own version** (your `SOUL.md`, your skills, your dashboard tweaks)? Click
> **"Use this template"** on the [GitHub repo](https://github.com/lennartduerr/personal-ai-os) to
> create a fresh repo in *your* account. Either way, then point Claude Code at the files.

1. **Clone this repo** (skip if you used "Use this template")
   ```bash
   git clone https://github.com/lennartduerr/personal-ai-os.git
   cd personal-ai-os
   ```
2. **Open it with [Claude Code](https://claude.com/claude-code)** (or another capable coding agent) and say:
   > "Read CLAUDE.md and set up my personal AI OS with me."
3. **Answer its questions.** Claude Code reads [CLAUDE.md](CLAUDE.md), asks what you want
   (which channels, which skills, do you have a VPS yet, your budget…), drafts a tailored plan,
   and then installs each piece **with your confirmation** — nothing happens automatically.

Prefer to do it by hand? Every step is also a human-readable playbook under [`docs/`](docs/),
in install order starting at [docs/00-overview.md](docs/00-overview.md).

---

## 🧭 The install path

Each phase is its own playbook and is **optional** — Claude Code asks before doing any of it.

| # | Phase | Playbook |
|---|-------|----------|
| 00 | Overview & architecture | [docs/00-overview.md](docs/00-overview.md) |
| 01 | Prerequisites & API keys (with costs) | [docs/01-prerequisites.md](docs/01-prerequisites.md) |
| 02 | VPS setup (Hetzner example) | [docs/02-vps-setup.md](docs/02-vps-setup.md) |
| 03 | Install the Hermes agent | [docs/03-install-hermes.md](docs/03-install-hermes.md) |
| 04 | LLM: DeepSeek (+ vision) | [docs/04-llm-deepseek.md](docs/04-llm-deepseek.md) |
| 05 | Channels: Telegram & Slack | [docs/05-channels.md](docs/05-channels.md) |
| 06 | Calendar & tasks | [docs/06-calendar-tasks.md](docs/06-calendar-tasks.md) |
| 07 | Email (read + relay send) | [docs/07-mail.md](docs/07-mail.md) |
| 08 | Web & internet access | [docs/08-web-internet.md](docs/08-web-internet.md) |
| 09 | Notes & Second Brain Pipeline | [docs/09-notes-secondbrain.md](docs/09-notes-secondbrain.md) |
| 10 | Crons & morning briefing | [docs/10-crons-briefing.md](docs/10-crons-briefing.md) |
| 11 | Dashboard on Vercel | [docs/11-dashboard-vercel.md](docs/11-dashboard-vercel.md) |
| 12 | Self-improvement via Claude Code | [docs/12-self-improve.md](docs/12-self-improve.md) |
| 13 | Workflow automation — *advanced, optional* | [docs/13-n8n-orchestration.md](docs/13-n8n-orchestration.md) |
| 14 | Security & secrets | [docs/14-security.md](docs/14-security.md) |
| 15 | Ideas & extensions (WhatsApp, voice, …) | [docs/15-ideas.md](docs/15-ideas.md) |
| 99 | Use cases / playbooks | [docs/99-use-cases.md](docs/99-use-cases.md) |

Reusable building blocks live in [`templates/`](templates/), [`skills/`](skills/), and
[`dashboard/`](dashboard/).

---

## 🧠 The Second Brain Pipeline

A first-class, optional part of this OS. The
[Second Brain Pipeline](https://github.com/lennartduerr/second-brain-pipeline) ingests any
document and compiles it into a clean Markdown knowledge base — **no RAG, no chunking, no vector
DB**. The whole brain fits in a modern context window, so your agent navigates an *index* instead
of doing similarity search.

```
Input files → Parse → Extract → Compile → Lint → brain/ (Markdown your agent can read)
```

It plugs straight into this OS: the agent's `notes/` documents flow into `sbp ingest`, and the
resulting brain becomes knowledge the agent can answer from. See
[docs/09-notes-secondbrain.md](docs/09-notes-secondbrain.md).

---

## 💸 Rough monthly cost

| Item | Cost | Notes |
|------|------|-------|
| VPS (Hetzner CPX22, 2 vCPU / 4 GB) | ~€5–6/mo | Any small Linux VPS works |
| DeepSeek LLM | pay-as-you-go, cents/day | `flash` tier ~3× cheaper than `pro` |
| OpenRouter (vision) | pay-as-you-go | Only for image inputs |
| Tavily / Apify | free tiers | Web search / YouTube fallback |
| Vercel (dashboard) | free | Read-only, no live LLM cost |
| Brevo (mail relay) | free tier | Only if your host's IP is blocked for SMTP |
| Claude Code (self-improve) | your existing plan | Optional |

A realistic always-on personal agent lands in the **single-digit euros per month** range.

---

## 🔒 Safety & disclaimer

- This repo ships **only placeholders** — no real keys, IDs, IPs, or personal data. You bring your own.
- The agent is configured **read-mostly** by default: it reads mail/calendar, but never sends mail,
  clicks links, or makes irreversible changes without asking. See [docs/14-security.md](docs/14-security.md).
- You are responsible for your own VPS, accounts, and data. Review every step before running it.
- Built and shared by an enthusiast, not a vendor. Provided as-is under the MIT License.

---

## 🏷️ Topics

`ai-operating-system` · `personal-agent` · `hermes` · `claude-code` · `second-brain` ·
`deepseek` · `telegram-bot` · `slack-bot` · `self-hosted` · `ai-agent` · `vercel`

## 📄 License

[MIT](LICENSE) — do whatever you want, no warranty.
