# 04 — LLM: choose your model (DeepSeek recommended)

> **Agent note:** This is the user's decision — present the options, give the recommendation, then
> let them pick. The config shape is identical for any OpenAI-compatible provider, so swapping later
> is trivial (`base_url` / `model` / key). Never print the key.
> Template: [../templates/config.yaml.example](../templates/config.yaml.example).

## Pick your LLM (your call)

| Option | Best for | Notes |
|--------|----------|-------|
| **DeepSeek** ⭐ *recommended* | cheapest capable default | Two tiers (`pro` / `flash`), OpenAI-compatible. Key at **https://platform.deepseek.com** |
| **OpenRouter** | trying many models behind one key | One key, hundreds of models (Claude, Gemini, Llama, Qwen, DeepSeek, …). Easy A/B testing. Key at **https://openrouter.ai/keys** |
| **Qwen / other** | a specific model you like | Any OpenAI-compatible endpoint works — Qwen (Alibaba), Mistral, a local model via Ollama, etc. |

**Recommendation:** start with **DeepSeek** — it's the cheapest way to get a genuinely capable
agent, and you can switch any time by editing three lines of config. If you'd rather experiment
across models, use **OpenRouter** and try a few; you can always settle on one later. The rest of
this OS doesn't care which you choose.

> The choice isn't permanent. Because everything is OpenAI-compatible, moving from DeepSeek to
> OpenRouter to Qwen is just a `base_url` + `model` + key change in `config.yaml`. Pick something
> now, refine later.

---

## Why DeepSeek

It's **OpenAI-compatible and very cheap**, with two tiers:

| Model | Use | Relative cost |
|-------|-----|---------------|
| `deepseek-v4-pro` | default — complex reasoning, agentic tasks | baseline |
| `deepseek-v4-flash` | research, token-heavy/cheap tasks | ~3× cheaper |

You can switch tiers **per session** in chat with `/model flash` and `/model pro` (these are
aliases defined in `config.yaml`).

## Step 1 — Get a key

Create one at **https://platform.deepseek.com** → *API keys*, and put it in `~/.hermes/.env`:

```bash
DEEPSEEK_API_KEY=sk-deepseek-...
```

## Step 2 — Configure the model

In `~/.hermes/config.yaml` (see the template for the full file):

```yaml
model:
  provider: custom
  base_url: https://api.deepseek.com/v1
  model: deepseek-v4-pro
  api_key: ${DEEPSEEK_API_KEY}

# /model flash  and  /model pro
model_aliases:
  flash:
    provider: custom
    base_url: https://api.deepseek.com/v1
    model: deepseek-v4-flash
    api_key: ${DEEPSEEK_API_KEY}
  pro:
    provider: custom
    base_url: https://api.deepseek.com/v1
    model: deepseek-v4-pro
    api_key: ${DEEPSEEK_API_KEY}
```

## Alternative: OpenRouter (try many models behind one key)

If you'd rather experiment, point the model config at OpenRouter and swap `model` freely:

```yaml
model:
  provider: openrouter            # or: provider: custom, base_url: https://openrouter.ai/api/v1
  model: deepseek/deepseek-chat   # try: anthropic/claude-sonnet-4-6, google/gemini-2.5-flash,
                                  #      qwen/qwen-2.5-72b-instruct, meta-llama/llama-3.3-70b, …
  api_key: ${OPENROUTER_API_KEY}
```

Set up `model_aliases` for two or three favorites so you can `/model <name>` to compare them in
chat. Costs vary per model — OpenRouter shows per-model pricing on its site.

> Want a specific provider like **Qwen** directly (not via OpenRouter)? Use `provider: custom` with
> that provider's `base_url`, its `model` id, and its key. Same three lines.

## Step 3 — Vision (images), optional

DeepSeek doesn't take images directly, so route image inputs to a vision model via
[OpenRouter](https://openrouter.ai/keys):

```yaml
auxiliary:
  vision:
    provider: openrouter
    model: google/gemini-2.5-flash
    api_key: ${OPENROUTER_API_KEY}
image_input_mode: auto
```

> ⚠️ **Don't send confidential documents** (banking, legal) through cloud vision.

## Step 4 — Test

```bash
hermes -z "In one sentence, what can you do for me?"
/model flash    # then ask something cheap
/model pro      # back to the default
```

## Cost monitoring (recommended)

DeepSeek exposes a balance API. A small helper script can print your 24h spend + remaining
balance, which the **morning briefing** ([10-crons-briefing.md](10-crons-briefing.md)) includes so
you never get surprised by an empty balance. A starter lives at
[../skills/](../skills/) / scripts; wire it into the briefing prompt.

> Keep an eye on the balance early on — a chatty agent on `pro` can burn through a small top-up
> faster than you'd expect. Default token-heavy research tasks to `flash`.

## Next step

[05-channels.md](05-channels.md).
