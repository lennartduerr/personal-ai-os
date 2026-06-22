# 07 — Email (read + relay send)

> **Agent note:** Mail is **read-mostly by default** — the agent reads and tidies, but must never
> send, click links, or delete on its own initiative. Sending is a separate, deliberate step and
> commonly hits a provider IP block (see below). Scaffold/notes:
> [../skills/mail-himalaya/](../skills/mail-himalaya/).

We use **[himalaya](https://github.com/pimalaya/himalaya)**, a small IMAP/SMTP CLI, so the agent
can list, read, and move mail.

## Step 1 — Install himalaya

```bash
# See the himalaya repo for the current install method; e.g.:
cargo install himalaya            # or download a release binary
himalaya --version
```

## Step 2 — Read access (IMAP)

1. **User:** create an **app/mail password** for IMAP at your provider (most require this for
   third-party clients).
2. Store it in a locked-down file (not env):
   ```bash
   printf '%s' 'YOUR_IMAP_APP_PASSWORD' > ~/.hermes/.mail_pass
   chmod 600 ~/.hermes/.mail_pass
   ```
3. **You (agent):** configure `~/.config/himalaya/config.toml`. Example for an IMAP host (adjust
   server/folders to the provider; e.g. T-Online uses an `INBOX.`-prefixed folder layout):
   ```toml
   [accounts.main]
   default = true
   email = "you@example.com"
   backend = "imap"
   imap.host = "imap.example.com"
   imap.port = 993
   imap.login = "you@example.com"
   imap.auth.type = "password"
   imap.auth.cmd = "cat ~/.hermes/.mail_pass"
   folder.alias.sent = "Sent"
   ```
4. Test:
   ```bash
   himalaya envelope list -a main
   himalaya message read <id> -a main
   himalaya message move <id> Archive -a main
   ```

## Step 3 — Sending (optional) — beware the host IP block

⚠️ **Common gotcha:** many mail providers (e.g. Telekom/T-Online) **block outbound SMTP from
data-center IPs**, so sending directly from your VPS fails (`421 ... blocked`). The fix is a
**relay** like **[Brevo](https://www.brevo.com)** (free tier):

1. **User:** sign up at Brevo, verify your *from* address, get SMTP relay credentials, and add the
   VPS public IP under **Security → Authorized IPs**.
2. Store the relay password:
   ```bash
   printf '%s' 'YOUR_BREVO_SMTP_KEY' > ~/.hermes/.brevo_pass
   chmod 600 ~/.hermes/.brevo_pass
   ```
3. **You (agent):** point himalaya's SMTP at the relay:
   ```toml
   smtp.host = "smtp-relay.brevo.com"
   smtp.port = 587
   smtp.login = "your-brevo-login@smtp-brevo.com"
   smtp.auth.type = "password"
   smtp.auth.cmd = "cat ~/.hermes/.brevo_pass"
   ```

> If you skip the relay, keep the agent in read-only mail mode and have it deliver "email reports"
> to you over Telegram/Slack instead of sending real mail.

## Safety rules (mirror these into SOUL.md)

- ✅ Read, search, move/tidy mail.
- ❌ Never send without an explicit instruction. ❌ Never click links. ❌ Never unsubscribe/delete
  on the agent's own initiative. ❌ Never run cloud vision on confidential attachments.

## Next step

[08-web-internet.md](08-web-internet.md).
