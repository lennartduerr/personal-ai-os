#!/usr/bin/env python3
"""tasks-google — to-dos/reminders via Google Tasks.

SCAFFOLD: CLI is complete; fill in the API calls where marked TODO.
Uses the Google Tasks REST API. You can use `google-api-python-client` + `google-auth`, or plain
HTTPS with a refreshed access token.

Reads from env:
  GOOGLE_TASKS_CLIENT_ID, GOOGLE_TASKS_CLIENT_SECRET, GOOGLE_TASKS_REFRESH_TOKEN
(or the fallback file ~/.hermes/google_tasks_token.json, chmod 600)
"""
import argparse
import os
import sys

TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://tasks.googleapis.com/tasks/v1"


def _access_token():
    cid = os.environ.get("GOOGLE_TASKS_CLIENT_ID")
    secret = os.environ.get("GOOGLE_TASKS_CLIENT_SECRET")
    refresh = os.environ.get("GOOGLE_TASKS_REFRESH_TOKEN")
    if not (cid and secret and refresh):
        sys.exit("Missing GOOGLE_TASKS_CLIENT_ID/SECRET/REFRESH_TOKEN (or token file).")
    # TODO: POST to TOKEN_URL with grant_type=refresh_token to get a fresh access_token.
    raise NotImplementedError("TODO: exchange the refresh token for an access token.")


def _default_list_id(token):
    # TODO: GET {API}/users/@me/lists  → return the first list id (usually '@default').
    raise NotImplementedError("TODO: fetch the default task list id.")


def list_tasks(list_id):
    token = _access_token()
    list_id = list_id or _default_list_id(token)
    # TODO: GET {API}/lists/{list_id}/tasks?showCompleted=false
    #       print title / due / id for tasks with status == 'needsAction'.
    raise NotImplementedError("TODO: list open tasks.")


def create_task(title, due, notes):
    token = _access_token()
    # TODO: POST {API}/lists/@default/tasks  body {title, notes, due (RFC3339)}.
    raise NotImplementedError("TODO: create a task.")


def complete_task(task_id):
    token = _access_token()
    # TODO: PATCH the task to status='completed'.
    raise NotImplementedError("TODO: complete a task.")


def delete_task(task_id):
    token = _access_token()
    # TODO: DELETE {API}/lists/@default/tasks/{task_id}.
    raise NotImplementedError("TODO: delete a task.")


def list_lists():
    token = _access_token()
    # TODO: GET {API}/users/@me/lists  → print title / id.
    raise NotImplementedError("TODO: list task lists.")


def main():
    p = argparse.ArgumentParser(description="Google Tasks skill")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list-tasks")
    pl.add_argument("--list-id", default=None)

    pc = sub.add_parser("create-task")
    pc.add_argument("--title", required=True)
    pc.add_argument("--due", default=None, help="YYYY-MM-DD")
    pc.add_argument("--notes", default="")

    pcomp = sub.add_parser("complete-task")
    pcomp.add_argument("--id", required=True)

    pdel = sub.add_parser("delete-task")
    pdel.add_argument("--id", required=True)

    sub.add_parser("list-lists")

    args = p.parse_args()
    if args.cmd == "list-tasks":
        list_tasks(args.list_id)
    elif args.cmd == "create-task":
        create_task(args.title, args.due, args.notes)
    elif args.cmd == "complete-task":
        complete_task(args.id)
    elif args.cmd == "delete-task":
        delete_task(args.id)
    elif args.cmd == "list-lists":
        list_lists()


if __name__ == "__main__":
    main()
