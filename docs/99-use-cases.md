# 99 — Use cases & playbooks

> What you can actually *do* once the OS is running. Each is written as: **you say** → **the agent
> does**. Many combine skills — that's the point. Use these as inspiration and as test cases.

## 🌅 Daily rhythm

- **Morning briefing** *(cron)* → every morning: today's calendar + open to-dos + noteworthy mail +
  LLM spend, in one tight message. *(see [10](10-crons-briefing.md))*
- **"What's on today?"** → lists today's events and the next deadlines.
- **"End-of-day wrap"** *(cron, optional)* → what got done (completed tasks), what's still open,
  tomorrow's first event.

## ✅ Tasks & reminders

- **"Look at my to-dos."** → lists open Google Tasks, **categorizes** them, and offers to help with
  the ones it can (research, drafting, scheduling). Leaves personal ones to you.
- **"Remind me to call the landlord on Friday."** → creates a task with a due date.
- **"What's overdue?"** → filters `needsAction` tasks past due.
- **Proactive nudge:** sees a to-do like "research X" → offers to do the research now.

## 📅 Calendar

- **"Am I free Thursday afternoon?"** → checks events and answers.
- **"Schedule dentist next Tuesday 10–11, remind me a day before."** → creates the event with alarms.
- **"What's my week look like?"** → a compact week overview.

## 📧 Email

- **"Anything important in my inbox?"** → summarizes noteworthy unread mail from the last 24h,
  skipping newsletters/promos.
- **"Tidy my inbox."** → moves newsletters/promos to a folder (never deletes).
- **"Draft a reply to <person> saying I'll be late."** → drafts it for you to send (never sends
  unprompted).
- **Email-report mode:** if SMTP is blocked, get "email reports" delivered to Telegram/Slack instead.

## 🔎 Research & web

- **"Research <topic> and give me 5 sources."** → Tavily search + synthesis with links.
- **"Research <topic> and save it as a PDF."** → research → `notes new --format pdf`.
- **"Summarize this YouTube video: <url>."** → transcript → summary → optional note.
- **"Compare <A> vs <B> for my use case."** → multi-source comparison.
- **"How far is <place> from home, and how long by transit?"** → maps (OSM), uses your home in SOUL.md.

## 🧠 Second brain

- **"Add this PDF to my second brain."** → `sbp ingest` → it becomes queryable knowledge.
- **"What do my documents say about <X>?"** → answers from `brain/index.md` + knowledge pages
  (no RAG needed).
- **Auto-ingest:** drop files in a watched folder → `sbp watch` ingests them automatically.
- **"Any contradictions in my notes about <project>?"** → `sbp lint` surfaces gaps/conflicts.

## 📝 Documents & notes

- **"Write up a report/analysis/list on <topic>."** → creates a doc (md/docx/pdf) under a topic folder.
- **"Append these points to the <project> doc."** → updates an existing note.
- **Local mirror:** documents show up in your Files/iCloud via the one-way sync.

## 🤖 Self-improvement

- **"Build me a skill that does <X>."** → delegates to Claude Code on the VPS, shows you the diff,
  ships after your OK. *(see [12](12-self-improve.md))*
- **"This briefing is too long — make it shorter."** → edits the cron prompt.
- **"Add a weather line to my morning briefing."** → updates the briefing prompt (and adds a weather
  fetch if needed).

## 🔁 Automation & pipelines

- **Ingest-and-notify** → drop a file → `sbp ingest` (or `sbp watch`) → agent summary → chat.
- **Scheduled digest** → a recurring, script-driven analysis delivered to chat (e.g. a weekday
  "what changed in <area>" summary).
- *(Advanced, optional)* hook the agent into an existing **n8n** automation setup — most users can
  ignore this. See [13](13-n8n-orchestration.md).

## 📊 Dashboard

- **At-a-glance view** → calendar + tasks + mail + LLM spend on a web page, free to view.
- **Second-brain status block** → `sbp status` surfaced on the dashboard.

## 💬 Multi-channel & lifestyle

- **One agent, two apps** → talk to the same agent from Telegram and Slack.
- **Travel helper** → "plan a 3-day itinerary for <city>", save as PDF, ingest into the brain.
- **Meeting prep** → "summarize what I know about <company> before my 3pm" (brain + web).
- **Spend awareness** → "how much LLM did I burn this week?" from the cost tracker.

---

> Test a few of these right after install — they double as smoke tests and they're the fastest way
> to fall in love with the setup.
