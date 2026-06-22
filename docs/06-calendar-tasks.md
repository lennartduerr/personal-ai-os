# 06 — Calendar & tasks

> **Agent note:** Two independent skills — offer them separately. Calendar via CalDAV (Apple
> iCloud example), to-dos via Google Tasks. You install/register the skills and wire the scripts;
> the user only creates the app-specific password / OAuth client and pastes the secrets. Scaffolds:
> [../skills/calendar-caldav/](../skills/calendar-caldav/) and [../skills/tasks-google/](../skills/tasks-google/).

## Calendar — Apple iCloud via CalDAV

Reads and creates calendar events (with reminders/alarms). Works with any CalDAV server; Apple
iCloud is the example.

1. **User:** create an **app-specific password** at **https://appleid.apple.com** → *Sign-In and
   Security* → *App-Specific Passwords*.
2. Put credentials in `~/.hermes/.env`:
   ```bash
   ICLOUD_USERNAME=you@example.com
   ICLOUD_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
   ```
3. **You (agent):** copy the scaffold into custom-skills and register it:
   ```bash
   cp -r skills/calendar-caldav ~/.hermes/custom-skills/calendar
   ```
   Ensure `config.yaml` has:
   ```yaml
   skills:
     external_dirs: [/home/hermes/.hermes/custom-skills]
   ```
4. Restart + test:
   ```bash
   sudo hermes gateway restart --system
   ~/.hermes/custom-skills/calendar/scripts/caldav.py list-events --days 7
   ```

Typical commands: `list-events [--days N]`, `create-event --title --start --end [--notes] [--no-alarms]`.

---

## Tasks / reminders — Google Tasks

Used for to-dos, reminders, "remind me to…". **Why Google Tasks and not Apple Reminders?** Apple's
"upgraded" Reminders are no longer readable over CalDAV (a hard Apple limitation, not a bug), so
to-dos move to Google Tasks, which is decoupled from OS updates. (The calendar stays on iCloud.)

1. **User:** in **[Google Cloud Console](https://console.cloud.google.com)**:
   - Create a project, enable the **Google Tasks API**.
   - Configure the **OAuth consent screen** and **publish it to "Production"** (so the refresh
     token doesn't expire after 7 days).
   - Create an **OAuth client ID** (Desktop app) and download the client JSON.
2. **You (agent):** run the one-time OAuth flow (the user clicks consent + pastes the code), then
   store the refresh token in `~/.hermes/.env`:
   ```bash
   GOOGLE_TASKS_CLIENT_ID=...apps.googleusercontent.com
   GOOGLE_TASKS_CLIENT_SECRET=...
   GOOGLE_TASKS_REFRESH_TOKEN=1//...
   ```
   (A token fallback file `~/.hermes/google_tasks_token.json` is also fine — chmod 600.)
3. Install + register the skill:
   ```bash
   cp -r skills/tasks-google ~/.hermes/custom-skills/google-tasks
   sudo hermes gateway restart --system
   ```
4. Test:
   ```bash
   ~/.hermes/custom-skills/google-tasks/scripts/google_tasks.py list-tasks
   ```

Typical commands: `list-tasks`, `create-task --title --due [--notes]`, `complete-task --id`,
`delete-task --id`, `list-lists`. Open to-dos have `status: needsAction`.

> **Handy workflow to teach the agent (put it in SOUL.md):** when the user says "look at my
> to-dos", list open Google Tasks, categorize them, and offer to act on the ones it can help with.

## Next step

[07-mail.md](07-mail.md) or jump to the [morning briefing](10-crons-briefing.md), which pulls
calendar + tasks together.
