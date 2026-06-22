<!--
Dashboard export — SCRIPT cron (no LLM). See docs/11-dashboard-vercel.md.

This cron runs the exporter script, not the agent. It stays SILENT on success and only pings you
on error, so it never spams the channel.

  hermes cron create --name "Dashboard export" --schedule "5 8,12,17 * * *" \
    --no-agent --script briefing_export.py --deliver telegram:<chat_id>

The script (dashboard/briefing_export.py.example → ~/.hermes/scripts/briefing_export.py):
  - gathers calendar (next ~2 days), open tasks, noteworthy mail (24h), LLM spend,
    and optionally `sbp status --json`
  - POSTs the JSON to DASHBOARD_INGEST_URL with a Bearer DASHBOARD_INGEST_SECRET
  - exits non-zero (and prints the error) only on failure → the cron then alerts you

No prompt is needed for a --no-agent script cron; this file documents the schedule + intent.
-->
