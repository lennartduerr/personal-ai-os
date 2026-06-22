# 05 — Channels: pick one (Telegram or Slack)

> **Agent note:** Do this right after the LLM so the user gets a working chat loop early — it's the
> first "wow". **Have the user pick ONE channel to start** — Telegram or Slack. Running both is
> possible (one agent behind both), but one is the norm; they can add more later. More channels
> (WhatsApp Business, Discord, Signal…) are optional add-ons in [15-ideas.md](15-ideas.md). Tokens
> go in `~/.hermes/.env`, never in this repo.

The **gateway** connects chat platforms to the agent and detects which platforms to enable from the
tokens present in `.env`. Restart it after adding tokens:
`sudo hermes gateway restart --system`.

---

## Telegram (recommended, easiest)

1. In Telegram, open **[@BotFather](https://t.me/BotFather)** → `/newbot` → pick a name and a
   username ending in `bot`. Copy the **token**.
2. Find your **numeric chat id**: message **[@userinfobot](https://t.me/userinfobot)** (or similar)
   and copy the number.
3. In `~/.hermes/.env`:
   ```bash
   TELEGRAM_BOT_TOKEN=0000000000:AA...
   TELEGRAM_HOME_CHANNEL=<your_numeric_chat_id>
   TELEGRAM_HOME_CHANNEL_NAME=Me
   ```
4. Lock the bot to *you* in `~/.hermes/config.yaml`:
   ```yaml
   telegram:
     allowed_chats: [<your_numeric_chat_id>]
   ```
5. Restart the gateway and message your bot. If it ignores you, you may need to approve a pairing
   code once: `hermes pairing approve telegram <CODE>` (watch `journalctl -u hermes-gateway -f`).

**Nice-to-haves** (in `config.yaml`): render the agent's tables as monospace code blocks and hide
raw command breadcrumbs on Telegram:
```yaml
display:
  platforms:
    telegram:
      tool_progress: off
```

---

## Slack (optional)

1. Create an app at **[api.slack.com/apps](https://api.slack.com/apps)** → *From scratch*.
2. Enable **Socket Mode** (no public port needed — the bot connects out over WebSocket).
3. **OAuth & Permissions** → add bot scopes (e.g. `chat:write`, `im:history`, `im:write`), then
   *Install to Workspace* and copy the **Bot User OAuth Token** (`xoxb-…`).
4. **Basic Information** → *App-Level Tokens* → create one with `connections:write`; copy the
   **App Token** (`xapp-…`).
5. In `~/.hermes/.env`:
   ```bash
   SLACK_BOT_TOKEN=xoxb-...
   SLACK_APP_TOKEN=xapp-...
   SLACK_ALLOWED_USERS=<your_slack_user_id>
   ```
6. Restart the gateway and DM the bot. (Find your Slack user id in your profile → *Copy member ID*.)

---

## Verify

```bash
sudo hermes gateway restart --system
sudo hermes gateway status --system
# then message the bot from Telegram and/or Slack
```

If a channel stays silent, check `sudo journalctl -u hermes-gateway -f` for auth/pairing errors.

## Next step

Pick the skills the user wants: calendar & tasks ([06](06-calendar-tasks.md)), mail
([07](07-mail.md)), web ([08](08-web-internet.md)), notes/second brain ([09](09-notes-secondbrain.md)).
Then the headline **morning briefing** ([10](10-crons-briefing.md)).
