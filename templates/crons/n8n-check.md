<!--
n8n health check — cron PROMPT template (see docs/13-n8n-orchestration.md).
  hermes cron create --name "n8n check" --schedule "30 8 * * *" \
    --prompt "$(cat templates/crons/n8n-check.md)" --deliver telegram:<chat_id>
-->
--- PROMPT ---

Check my n8n instance (via n8n-MCP or the n8n REST API) and give me a one-glance health report for the last 24h:

- ✅ Workflows that ran successfully (count).
- ❌ Any failed/errored executions — name the workflow and the error, briefly.
- ⏸️ Any workflows that didn't run but were expected to (if detectable).

Keep it to a few lines. If everything is healthy, just say "n8n healthy — N runs, 0 errors."
Don't change anything; this is read-only monitoring.
