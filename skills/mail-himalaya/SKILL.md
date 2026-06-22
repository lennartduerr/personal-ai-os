---
name: mail-himalaya
description: Read, search, and tidy email via the himalaya CLI. READ-MOSTLY — never send without an
  explicit instruction, never click links, never delete/unsubscribe on your own.
---

# mail-himalaya

A thin wrapper around [himalaya](https://github.com/pimalaya/himalaya) so the agent can work with
mail. Sending (optional) goes through an SMTP relay like Brevo because many providers block
data-center IPs — see [docs/07](../../docs/07-mail.md).

## Setup
- Install himalaya; configure `~/.config/himalaya/config.toml`.
- IMAP password in `~/.hermes/.mail_pass` (chmod 600); optional relay password in `~/.hermes/.brevo_pass`.

## Commands (delegate to himalaya)
```
mail.py list [--account A] [--folder F]
mail.py read --id ID [--account A]
mail.py move --id ID --to FOLDER [--account A]
```

## Hard rules
- ✅ read / search / move-tidy   ❌ send unprompted   ❌ click links   ❌ delete/unsubscribe on own initiative
