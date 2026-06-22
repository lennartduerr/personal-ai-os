# 08 — Web & internet access

> **Agent note:** This is what makes the agent useful for research. Tavily is the recommended
> search/extract backend; maps need no key; Apify is an optional YouTube fallback. You wire the
> config; the user just gets the keys.

By default an LLM can't browse. These give your agent eyes on the web.

## Web search & extraction — Tavily (recommended)

[Tavily](https://tavily.com) is an LLM-friendly search API with a free tier.

1. **User:** get a key at **https://tavily.com** → put `TAVILY_API_KEY=tvly-...` in `~/.hermes/.env`.
2. **You (agent):** enable it in `~/.hermes/config.yaml`:
   ```yaml
   web:
     search_backend: tavily
     extract_backend: tavily
   ```
3. Restart + test:
   ```bash
   sudo hermes gateway restart --system
   hermes -z "Search the web: what's new with <topic>? Give me 3 sources."
   ```

> Pair this with the notes skill ([09](09-notes-secondbrain.md)) for "research X and save it as a
> PDF/note" workflows.

## Maps & location — OpenStreetMap (no key)

Hermes ships a maps skill backed by OpenStreetMap — **no API key needed**. Make sure it's enabled
(it's a built-in productivity skill) and optionally set the user's home location in `SOUL.md` so
"how far is X from home?" works.

## YouTube transcripts — optional, with Apify fallback

A YouTube skill can pull transcripts (for "summarize this video"). Direct transcript fetching works
for many videos; for the rest, an [Apify](https://apify.com) actor is a reliable fallback.

1. **User (optional):** `APIFY_TOKEN=apify_api_...` in `~/.hermes/.env`.
2. **You (agent):** install the scaffold:
   ```bash
   cp -r skills/youtube ~/.hermes/custom-skills/youtube
   sudo hermes gateway restart --system
   ```

## Next step

[09-notes-secondbrain.md](09-notes-secondbrain.md).
