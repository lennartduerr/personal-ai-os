---
name: calendar-caldav
description: Read and create calendar events over CalDAV (Apple iCloud by default). Use for
  "what's on today", "am I free", scheduling events with reminders.
---

# calendar-caldav

Talks to a CalDAV server. Defaults to Apple iCloud but works with any CalDAV endpoint.

## Setup
- Credentials in `~/.hermes/.env`: `ICLOUD_USERNAME`, `ICLOUD_APP_PASSWORD`
  (an app-specific password from https://appleid.apple.com).
- See [docs/06](../../docs/06-calendar-tasks.md).

## Commands
```
caldav.py list-events [--days N]
caldav.py create-event --title T --start "YYYY-MM-DD HH:MM" --end "YYYY-MM-DD HH:MM" [--notes N] [--no-alarms]
```

Default alarms: 1 day before + 2 hours before (disable with `--no-alarms`).
