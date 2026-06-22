---
name: youtube
description: Fetch a YouTube video's transcript so the agent can summarize it. Direct fetch first,
  with an optional Apify fallback for videos without easy captions.
---

# youtube

Pulls transcripts for "summarize this video" workflows.

## Setup
- `pip install youtube-transcript-api` for the direct path.
- Optional fallback: `APIFY_TOKEN` in `~/.hermes/.env` (a YouTube transcript/scraper actor).
- See [docs/08](../../docs/08-web-internet.md).

## Commands
```
youtube.py transcript --url URL        # prints the transcript text (direct, then Apify fallback)
```
