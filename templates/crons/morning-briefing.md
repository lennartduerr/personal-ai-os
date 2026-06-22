<!--
Morning briefing — cron PROMPT template (the headline feature).
Feed this as the --prompt for the morning-briefing cron (see docs/10-crons-briefing.md):

  hermes cron create --name "Morning briefing" --schedule "0 8 * * *" \
    --prompt "$(cat templates/crons/morning-briefing.md)" \
    --deliver telegram:<chat_id> --deliver slack:<channel_id>

Everything below the marker is the actual prompt. Tweak the [bracketed] bits to taste.
-->
--- PROMPT ---

Put together my morning briefing for today. Keep it short, warm, and scannable — this goes to my
phone. Use my skills; don't ask me anything, just produce the briefing.

Include, in this order:

1. 📅 **Today's calendar** — today's events (and tomorrow's first event) from my calendar skill.
   If nothing today, say so in one line.
2. ✅ **Open to-dos** — open Google Tasks (status: needsAction). Group lightly if there are many;
   highlight anything overdue. [Limit to the top ~7 unless I have fewer.]
3. 📧 **Mail worth noticing** — noteworthy unread mail from the last 24h. Skip newsletters,
   promos, and automated notifications. One line each; if nothing notable, say "inbox quiet".
4. 💸 **LLM spend** — my DeepSeek 24h spend and remaining balance (so I don't run dry).
5. ✨ **One proactive suggestion** — [optional] one small thing I could do today that you can help
   with (research, a draft, scheduling).

Formatting:
- Tight and friendly. Tables/lists as monospace code blocks on Telegram.
- End with: 📊 Dashboard: <DASHBOARD_URL>   [remove this line if no dashboard]

[Optional add-ons you can enable:]
- Weather for <CITY> today.
- A short "focus for the day" line based on my calendar + to-dos.
