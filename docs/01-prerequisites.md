# 01 — Prerequisites & API keys

> **Agent note:** Only line up keys for the components the user actually chose. Don't make them
> create accounts for skills they're skipping. Keys go into `~/.hermes/.env` on the VPS (see
> [.env.example](../.env.example)) — never into this repo.

## Accounts / keys by component

| Component | What you need | Where | Cost |
|-----------|---------------|-------|------|
| **VPS** | A small Linux server (2 vCPU / 4 GB is plenty) | [Hetzner](https://www.hetzner.com/cloud) (example) | ~€5–6/mo |
| **LLM** | `DEEPSEEK_API_KEY` | [platform.deepseek.com](https://platform.deepseek.com) | pay-as-you-go, cents/day |
| **Vision** (optional) | `OPENROUTER_API_KEY` | [openrouter.ai](https://openrouter.ai/keys) | pay-as-you-go, only for images |
| **Telegram** | Bot token + your chat id | [@BotFather](https://t.me/BotFather) | free |
| **Slack** (optional) | Bot + app token (Socket Mode) | [api.slack.com/apps](https://api.slack.com/apps) | free |
| **Calendar** (optional) | Apple ID + app-specific password | [appleid.apple.com](https://appleid.apple.com) | free |
| **Tasks** (optional) | Google OAuth client + refresh token | [Google Cloud Console](https://console.cloud.google.com) | free |
| **Mail read** (optional) | IMAP app password for your provider | your mail provider | free |
| **Mail send** (optional) | SMTP relay creds (if host IP is blocked) | [Brevo](https://www.brevo.com) | free tier |
| **Web search** (optional) | `TAVILY_API_KEY` | [tavily.com](https://tavily.com) | free tier |
| **YouTube fallback** (optional) | `APIFY_TOKEN` | [apify.com](https://apify.com) | free tier |
| **Self-improve** (optional) | `CLAUDE_CODE_OAUTH_TOKEN` | `claude setup-token` | your Claude plan |
| **Dashboard** (optional) | Vercel account | [vercel.com](https://vercel.com) | free |

## Local machine (for optional bits)

- An **SSH key** to reach the VPS (`ssh-keygen -t ed25519 -C "personal-ai-os"`).
- Optionally **Node.js** if you'll deploy the dashboard from your machine, and **rsync** if you'll
  mirror notes locally (macOS/Linux ship with it).

## A note on the LLM choice

DeepSeek is the documented default because it's **OpenAI-compatible and very cheap**, with two
tiers: `deepseek-v4-pro` (default) and `deepseek-v4-flash` (~3× cheaper) you can switch per message
with `/model flash` and `/model pro`. Any OpenAI-compatible provider works — if the user prefers
something else, keep the same config shape and just swap `base_url` / `model` / key. See
[04-llm-deepseek.md](04-llm-deepseek.md).

## Next step

[02-vps-setup.md](02-vps-setup.md).
