# 10 — Crons & the morning briefing ⭐

> **Agent note:** This is one of the most-loved features of the whole OS — treat it as a headline
> deliverable, not an afterthought. As soon as the user has a channel ([05](05-channels.md)) plus at
> least one data skill (calendar/tasks/mail), proactively offer to set up the morning briefing.
> Ready-made prompts live in [../templates/crons/](../templates/crons/).

Hermes has a built-in **cron** scheduler: it runs a prompt (or a script) on a schedule and delivers
the result to your channels. The flagship cron is the **morning briefing**.

## Cron basics

```bash
hermes cron list [--json]
hermes cron run <job-id>                       # run now (great for testing)
hermes cron create --name "..." --schedule "0 8 * * *" --prompt "..." --deliver telegram:<chat_id>
hermes cron edit <job-id> --prompt "..."
hermes cron delete <job-id>
```

- Schedules are standard cron expressions; set your timezone in `config.yaml` (`timezone: Europe/Berlin`).
- Deliver to one or more targets, e.g. `--deliver telegram:<chat_id>` and/or `--deliver slack:<channel_id>`.
- **Approvals for crons:** set `approvals.cron_mode: deny` in `config.yaml` so scheduled runs can
  use safe skills (read calendar/mail) but are blocked from dangerous commands (`rm`, `sudo`, `git`)
  without you in the loop.

---

## The morning briefing

A single daily message that tells you what matters: today's calendar, open to-dos, unread mail
worth noticing, and your LLM spend/balance.

### Step 1 — Create it

Use the ready-made prompt in [../templates/crons/morning-briefing.md](../templates/crons/morning-briefing.md).
Create the cron (adjust targets):

```bash
hermes cron create \
  --name "Morning briefing" \
  --schedule "0 8 * * *" \
  --prompt "$(cat templates/crons/morning-briefing.md)" \
  --deliver telegram:<your_chat_id> \
  --deliver slack:<your_channel_id>
```

The prompt tells the agent to:
1. List today's (and tomorrow's) calendar events (calendar skill).
2. List open to-dos (`status: needsAction`) from Google Tasks.
3. Summarize noteworthy unread mail from the last 24h (and ignore newsletters/promos).
4. Report LLM spend + remaining balance.
5. Format it tightly for chat (short, scannable; tables as monospace on Telegram), ending with a
   link to the dashboard if enabled.

### Step 2 — Test it immediately

```bash
hermes cron list                # find the job id
hermes cron run <job-id>        # runs now and delivers to your channel
```

Iterate on the prompt until the briefing reads the way you like:

```bash
hermes cron edit <job-id> --prompt "$(cat templates/crons/morning-briefing.md)"
```

> Make it *yours*: tone, what to include/exclude, how aggressive the mail filtering is, whether to
> add weather, a quote, or a "one proactive suggestion" line. The template has comments showing
> where to tweak.

---

## Other useful crons

| Cron | Schedule (example) | What it does | Template |
|------|--------------------|--------------|----------|
| **Dashboard export** | `5 8,12,17 * * *` | pushes briefing JSON to the Vercel dashboard (script, not agent) | [../templates/crons/dashboard-export.md](../templates/crons/dashboard-export.md) |
| **End-of-day wrap** *(optional)* | `0 21 * * *` | what got done + tomorrow's first event | write your own prompt |

The dashboard-export cron runs a script (no LLM), stays silent on success, and only pings you on
error — so it never spams the channel. See [11-dashboard-vercel.md](11-dashboard-vercel.md).

```bash
# Example: a script-based, error-only cron
hermes cron create --name "Dashboard export" --schedule "5 8,12,17 * * *" \
  --no-agent --script briefing_export.py --deliver telegram:<your_chat_id>
```

## Verify

```bash
hermes cron list
hermes cron run <morning-briefing-id>   # you should get the briefing in chat within seconds
```

## Next step

[11-dashboard-vercel.md](11-dashboard-vercel.md).
