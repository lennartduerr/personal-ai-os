#!/usr/bin/env bash
# One-way mirror: VPS notes -> local folder (e.g. inside iCloud Drive).
# The VPS is the source of truth; this only ever pulls. See docs/09-notes-secondbrain.md.
#
# Setup:
#   1) Edit the three variables below.
#   2) chmod +x icloud-sync.sh ; run it once to test.
#   3) Schedule it (macOS launchd plist in this folder, or cron on Linux).
set -euo pipefail

# --- EDIT THESE ---------------------------------------------------------------
SSH_HOST="personal-ai-os"                       # your ~/.ssh/config alias (or user@ip)
REMOTE_DIR="/home/hermes/.hermes/hermes-notes/" # trailing slash matters
LOCAL_DIR="$HOME/Documents/personal-ai-os-notes/" # e.g. a folder inside iCloud Drive
# -----------------------------------------------------------------------------

mkdir -p "$LOCAL_DIR"
LOG="$HOME/.personal-ai-os-sync/sync.log"
mkdir -p "$(dirname "$LOG")"

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] syncing $SSH_HOST:$REMOTE_DIR -> $LOCAL_DIR"
  rsync -az --delete -e ssh "$SSH_HOST:$REMOTE_DIR" "$LOCAL_DIR"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] done"
} >> "$LOG" 2>&1

# keep the log small
tail -n 200 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
