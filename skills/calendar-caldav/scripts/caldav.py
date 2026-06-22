#!/usr/bin/env python3
"""calendar-caldav — read/create calendar events over CalDAV (Apple iCloud by default).

SCAFFOLD: structure + CLI are complete; fill in the CalDAV calls where marked TODO.
Recommended library: `pip install caldav icalendar`.

Reads credentials from env:
  ICLOUD_USERNAME, ICLOUD_APP_PASSWORD
Optionally CALDAV_URL (defaults to the iCloud CalDAV discovery endpoint).
"""
import argparse
import os
import sys
from datetime import datetime, timedelta

ICLOUD_CALDAV_URL = "https://caldav.icloud.com/"


def _client():
    user = os.environ.get("ICLOUD_USERNAME")
    pw = os.environ.get("ICLOUD_APP_PASSWORD")
    url = os.environ.get("CALDAV_URL", ICLOUD_CALDAV_URL)
    if not user or not pw:
        sys.exit("Missing ICLOUD_USERNAME / ICLOUD_APP_PASSWORD in environment.")
    # TODO: return a connected client, e.g.:
    #   import caldav
    #   return caldav.DAVClient(url=url, username=user, password=pw)
    raise NotImplementedError("TODO: connect via the `caldav` library using url/user/pw above.")


def list_events(days: int):
    client = _client()
    start = datetime.now()
    end = start + timedelta(days=days)
    # TODO: iterate principal().calendars(), search(start=start, end=end, event=True),
    #       print title / start / end for each. Sort by start.
    raise NotImplementedError("TODO: fetch and print events between start and end.")


def create_event(title, start, end, notes, alarms):
    client = _client()
    # TODO: build an iCalendar VEVENT (use the `icalendar` package). If `alarms`, add VALARMs
    #       at -1 day and -2 hours. Save it to the target calendar via calendar.save_event(ics).
    raise NotImplementedError("TODO: create the VEVENT and save it.")


def main():
    p = argparse.ArgumentParser(description="CalDAV calendar skill")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list-events")
    pl.add_argument("--days", type=int, default=7)

    pc = sub.add_parser("create-event")
    pc.add_argument("--title", required=True)
    pc.add_argument("--start", required=True, help='"YYYY-MM-DD HH:MM"')
    pc.add_argument("--end", required=True, help='"YYYY-MM-DD HH:MM"')
    pc.add_argument("--notes", default="")
    pc.add_argument("--no-alarms", action="store_true")

    args = p.parse_args()
    if args.cmd == "list-events":
        list_events(args.days)
    elif args.cmd == "create-event":
        create_event(args.title, args.start, args.end, args.notes, not args.no_alarms)


if __name__ == "__main__":
    main()
