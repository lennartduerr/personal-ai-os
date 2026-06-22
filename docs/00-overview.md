# 00 — Overview & architecture

> **Agent note:** Read this first so you can explain the whole system to the user before you
> start. Then ask the discovery questions in [CLAUDE.md](../CLAUDE.md) §2. Nothing here is
> installed automatically — every phase is opt-in.

## What this is

`personal-ai-os` turns a small Linux VPS into a 24/7 personal assistant you chat with from your
phone. The core is the **Hermes agent** (from [NousResearch](https://github.com/NousResearch)):
an LLM-driven agent with a *skill* system, a *gateway* that connects chat platforms, and a *cron*
system for scheduled tasks. Around that core we add cheap LLM access, productivity skills, a daily
briefing, an optional second brain, a dashboard, and a self-improvement loop.

## The mental model: an "AI OS"

Think of it like an operating system for your digital life:

- **Kernel** → the Hermes agent + its gateway (always running as a `systemd` service).
- **Shell** → your chat apps (Telegram, Slack). You talk; it acts.
- **Drivers** → *skills*: calendar, tasks, mail, web, notes. Each is a small folder with a
  script the agent calls.
- **Scheduler** → *crons*: the morning briefing and the dashboard export.
- **Storage / memory** → notes + the [Second Brain Pipeline](https://github.com/lennartduerr/second-brain-pipeline)
  (documents compiled into a queryable Markdown knowledge base).
- **Display** → an optional read-only web dashboard on Vercel.
- **Package manager / self-update** → the self-improvement loop: the agent asks Claude Code on the
  VPS to build new skills and ships them after your review.

## Architecture

```
   Telegram ─┐
             ├──► Hermes Gateway (systemd) ──► Hermes Agent ──► LLM (DeepSeek; vision→OpenRouter)
   Slack  ───┘                                     │
                                                    │ calls skills:
            ┌───────────────┬───────────────┬─────────────┬───────────────┐
            ▼               ▼               ▼             ▼               ▼
        calendar         tasks            mail          web            notes
       (CalDAV)      (Google Tasks)   (himalaya +     (Tavily)       (md/pdf/…)
                                       Brevo relay)                       │
                                                                          ▼
                                                            Second Brain Pipeline (sbp ingest)
                                                                          │
   crons (scheduler):                                                     ▼
     • morning briefing  ──► Telegram/Slack                       brain/ (queryable knowledge)
     • dashboard export  ──► Vercel  ──►  read-only Dashboard (https://…vercel.app)
```

## Where things live (on the VPS)

The Hermes install lives under `~/.hermes/` for a non-root user (we use `hermes` in the docs):

```
~/.hermes/
├── hermes-agent/        # the agent source (git install)
├── config.yaml          # main config (model, aliases, skills, approvals)
├── .env                 # secrets (chmod 600, never committed)
├── SOUL.md              # persona + rules + personal facts
├── CLAUDE.md            # guardrails for the on-VPS self-improve loop
├── custom-skills/       # your skills (registered via skills.external_dirs)
├── hermes-notes/        # documents the agent creates / reads
├── scripts/             # helpers (cost check, briefing export, …)
└── cron/ sessions/ logs/
```

Templates for all of these are in [`../templates/`](../templates/); skill scaffolds in
[`../skills/`](../skills/).

## Cost mindset

This is built to be **cheap**: a ~€5–6/mo VPS, a cheap LLM (DeepSeek, with an even cheaper
`flash` tier), free tiers for web/dashboard/relay. The dashboard does **no live LLM calls** — the
VPS pushes a static JSON once or a few times a day, so viewing it is free. See
[01-prerequisites.md](01-prerequisites.md) for the full cost/keys table.

## Next step

Go to [01-prerequisites.md](01-prerequisites.md) to line up accounts and keys for the pieces the
user chose. Then [02-vps-setup.md](02-vps-setup.md).
