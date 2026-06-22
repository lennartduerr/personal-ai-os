---
name: tasks-google
description: Manage to-dos / reminders via Google Tasks. Use for "look at my to-dos", "remind me
  to...", "what's overdue". Open tasks have status needsAction.
---

# tasks-google

Google Tasks as the to-do/reminder backend (decoupled from OS updates — see docs/06 for why not
Apple Reminders).

## Setup
- OAuth client from Google Cloud (Tasks API enabled, consent screen in **Production**).
- `~/.hermes/.env`: `GOOGLE_TASKS_CLIENT_ID`, `GOOGLE_TASKS_CLIENT_SECRET`, `GOOGLE_TASKS_REFRESH_TOKEN`.
- Token fallback file: `~/.hermes/google_tasks_token.json` (chmod 600).
- See [docs/06](../../docs/06-calendar-tasks.md).

## Commands
```
google_tasks.py list-tasks [--list-id ID]      # open tasks (status: needsAction)
google_tasks.py create-task --title T [--due YYYY-MM-DD] [--notes N]
google_tasks.py complete-task --id TASK_ID
google_tasks.py delete-task --id TASK_ID
google_tasks.py list-lists
```
