# 14 — Security & secrets

> **Agent note:** Run this as a final review pass after the chosen phases, and keep these rules in
> mind throughout. This is also what makes the OS safe to *share* — the agent has real access to the
> user's accounts, so the guardrails are not optional.

## Secrets: where they live, how they're protected

| Secret | Location | Protection |
|--------|----------|------------|
| API keys, tokens | `~/.hermes/.env` | `chmod 600`, git-ignored, never printed |
| Mail / relay passwords | `~/.hermes/*.pass` | `chmod 600` |
| OAuth / app credentials | `*credentials*.json`, `*_token.json` | `chmod 600`, git-ignored |
| GitHub token (if used) | `~/.config/gh/hosts.yml` | `chmod 600` |

Rules:
- **Never** print, echo, log, or commit any of the above.
- The self-improve loop ([12](12-self-improve.md)) is blocked from these by the permission deny-list
  ([../templates/claude-settings.json.example](../templates/claude-settings.json.example)).
- Keep a `.gitignore` in `~/.hermes/` excluding `.env`, `*.pass`, `*credentials*.json`, `sessions/`, `logs/`.

## Operational guardrails (mirror into SOUL.md)

- **Mail:** read/tidy only. Never send unprompted, never click links, never unsubscribe/delete on
  the agent's own initiative.
- **Cloud vision:** never on confidential documents (banking, legal, ID).
- **Server changes:** back up first (`cp f f.bak.$(date +%s)`), keep changes small, test
  (`hermes -z`, relevant tests), then `sudo hermes gateway restart --system` and verify.
- **Cron approvals:** `approvals.cron_mode: deny` blocks dangerous commands in scheduled runs.
- **VPS = source of truth:** never edit a synced local copy that will be overwritten.

## VPS hygiene

- Root SSH disabled, password auth off, key-only login.
- `ufw` allows only SSH; `fail2ban` running.
- Keep packages updated: `sudo apt update && sudo apt upgrade`.
- Reboot test occasionally to confirm the gateway comes back (`systemctl is-enabled hermes-gateway`).

## Before you share *your* setup

If you fork/adapt this repo, **never commit your real values**. Run a quick leak scan before any
push:

```bash
grep -rEn 'sk-|xoxb-|xapp-|tvly-|apify_api_|1//|BEGIN .*PRIVATE KEY|@.*\.(com|de)|[0-9]{1,3}(\.[0-9]{1,3}){3}' . \
  --exclude-dir=node_modules --exclude-dir=.git
```
Anything that looks real (a key, an IP, an email, a chat id) must become a placeholder.

## Done

That's the full OS. See [99-use-cases.md](99-use-cases.md) for ideas on what to do with it.
