# dashboard/ — read-only briefing dashboard (Next.js + Vercel)

A tiny web view of your daily briefing. **No live LLM** — your VPS pushes a JSON a few times a day,
the page renders it, so viewing it is free. Password-gated with a signed cookie. See
[../docs/11-dashboard-vercel.md](../docs/11-dashboard-vercel.md).

> ⚠️ **This is a starting template, not a finished product.** It's deliberately minimal so Claude
> Code (and you) can build on it for your own needs — add blocks, charts, themes, a calendar view,
> mobile polish, stronger auth, whatever you want. Treat the code below as a foundation to extend,
> not a fixed app. See **"Ideas to extend it"** at the bottom.

## Stack

- Next.js 16 (App Router, TypeScript), React 19
- `@vercel/blob` for storage (no database)
- A minimal HMAC-cookie password gate (no external auth dependency)

## Deploy

```bash
cd dashboard
npm install
npx vercel            # link/create the project (first run)
npx vercel --prod     # deploy to production
```

Create a **Blob store** in the Vercel project (Storage → Blob) — this auto-adds
`BLOB_READ_WRITE_TOKEN`. Then set env vars (Production + Preview):

| Var | Meaning |
|-----|---------|
| `DASHBOARD_PASSWORD` | the login password |
| `AUTH_SECRET` | random string used to sign the session cookie |
| `INGEST_SECRET` | random string the VPS sends as a Bearer token |
| `BLOB_READ_WRITE_TOKEN` | added automatically with the Blob store |

Generate randoms with `openssl rand -hex 32`.

## Wire the VPS exporter

Copy `briefing_export.py.example` to `~/.hermes/scripts/briefing_export.py`, set
`DASHBOARD_INGEST_URL` and `DASHBOARD_INGEST_SECRET` in `~/.hermes/.env`, fill in the `# TODO`
gather functions, and schedule it (see [../templates/crons/dashboard-export.md](../templates/crons/dashboard-export.md)).

```bash
python3 ~/.hermes/scripts/briefing_export.py   # one manual run to test
```

## How it fits together

```
VPS briefing_export.py ──POST /api/ingest (Bearer)──► Blob: briefing/latest.json ──► page renders it
```

## Privacy note

The briefing blob is written with `access: "public"` at a stable path for simplicity; the **page**
is password-gated, but the raw JSON URL is reachable if guessed. For a fully private setup, switch
the Blob store to private and read it via a token-authorized download in `lib/data.ts` /
`app/api/ingest/route.ts`. For a single-user dashboard the password gate is usually enough.

## Local dev

```bash
npm install
npm run dev    # http://localhost:3000  (set the env vars in a .env.local first)
```

## Ideas to extend it

This template is meant to grow. Easy next steps (great to hand to Claude Code):
- **More blocks** — weather, a week calendar view, n8n status, Second Brain stats, habit tracker.
- **Charts** — LLM spend over time, task completion trends.
- **Theming** — light/dark toggle, your own colors, your logo.
- **Better auth** — swap the simple cookie gate for a real provider (e.g. Auth.js / Clerk) if you
  share it with others.
- **Editable, not just read-only** — e.g. tick off a to-do from the dashboard (would call back to the VPS).
- **Push instead of pull** — real-time updates via webhooks/streaming instead of scheduled JSON pushes.

Add a new block by extending the `Briefing` type in [`lib/data.ts`](lib/data.ts), emitting the data
in `briefing_export.py`, and adding a `<Card>` in [`components/blocks.tsx`](components/blocks.tsx).
