# 11 — Dashboard on Vercel (read-only)

> **Agent note:** Optional. A read-only web view of the briefing. The key design point: **no live
> LLM** — the VPS pushes a static JSON a few times a day, the site just renders it, so viewing it is
> free. Deployable starter: [../dashboard/](../dashboard/).
>
> ⚠️ **The dashboard is a starting template, not a finished product.** Ship the minimal version
> first, then offer to extend it for the user's needs (more blocks, charts, theming, a calendar
> view, better auth…). Build on it — don't treat it as fixed. See the "Ideas to extend it" section
> in [../dashboard/README.md](../dashboard/README.md).

## How it works

```
VPS (briefing_export.py)  ── once or a few times/day ──►  POST /api/ingest  (Bearer secret)
        gathers: calendar, tasks, mail (24h), LLM spend, optional sbp status
                                                          │
                                                          ▼
                                            Vercel Blob: briefing/latest.json (private)
                                                          │
                                                          ▼
                                        Dashboard page renders the JSON (0 LLM tokens)
```

- **Auth:** a simple password → signed HMAC cookie gates the page.
- **Ingest:** a Bearer secret protects the POST endpoint.
- **Storage:** Vercel Blob (private). No database needed.
- **Cost:** free tier; each pageview is static rendering, no model calls.

## Step 1 — Deploy the dashboard (Claude Code does almost all of it)

> **Agent note:** This is a "you do the work" phase. The user's only manual steps are creating a
> Vercel account and authenticating the CLI once. After that, **you** link the project, set env
> vars, connect storage, deploy, and hand back the URL. Don't make the user click through the
> dashboard UI for things the CLI can do.

**The user's only job (2 minutes):**
1. Create a free account at **https://vercel.com**.
2. Authenticate the CLI once — either `vercel login` (a browser click) **or** create a token at
   **Account → Settings → Tokens** and paste it so you can run fully non-interactively
   (`vercel --token <TOKEN>` / `export VERCEL_TOKEN=...`).

**What you (Claude Code) then do:**
```bash
cd dashboard
npm install
vercel link --yes                      # create/link the Vercel project
# generate secrets and push them as env vars (repeat for preview if you want previews):
printf '%s' "$(openssl rand -hex 32)" | vercel env add AUTH_SECRET production
printf '%s' "$(openssl rand -hex 32)" | vercel env add INGEST_SECRET production
printf '%s' "<password the user picked>" | vercel env add DASHBOARD_PASSWORD production
```

Connect Blob storage (gives you `BLOB_READ_WRITE_TOKEN`):
- Create/connect a **Blob store** for the project, then pull its token into the project env.
  Use the CLI if your version supports `vercel blob`/`vercel storage`; otherwise this is the **one**
  ~30-second click for the user in the Vercel dashboard (Storage → Blob → Connect). After it's
  connected, `vercel env pull` to confirm `BLOB_READ_WRITE_TOKEN` is present.

Deploy:
```bash
vercel --prod                          # build + deploy; capture the production URL
```

Then tell the user their dashboard URL. Env vars you set:

| Var | Meaning |
|-----|---------|
| `DASHBOARD_PASSWORD` | the login password for the page |
| `AUTH_SECRET` | random string used to sign the auth cookie |
| `INGEST_SECRET` | random string the VPS sends as a Bearer token |
| `BLOB_READ_WRITE_TOKEN` | from the connected Blob store |

## Step 2 — Wire the VPS exporter

Copy the exporter and point it at your deployment:

```bash
cp dashboard/briefing_export.py.example ~/.hermes/scripts/briefing_export.py
```

In `~/.hermes/.env`:
```bash
DASHBOARD_INGEST_URL=https://<your-dashboard>.vercel.app/api/ingest
DASHBOARD_INGEST_SECRET=<same value as INGEST_SECRET on Vercel>
```

Test the push, then schedule it (silent on success, alerts only on error):
```bash
python3 ~/.hermes/scripts/briefing_export.py        # one manual run
# schedule via the dashboard-export cron — see docs/10
```

## Step 3 — Link it from the briefing

Add a footer line to the morning briefing prompt:
```
📊 Dashboard: https://<your-dashboard>.vercel.app
```

## Next step

[12-self-improve.md](12-self-improve.md).
