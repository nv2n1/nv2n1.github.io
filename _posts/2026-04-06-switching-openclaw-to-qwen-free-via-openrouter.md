---
title: "Switching from OpenClaw to Qwen on OpenRouter"
date: 2026-04-06 08:30:29 +0000
author: "Eric Ma"
layout: post
categories: [ai-engineering]
canonical: /switching-openclaw-to-qwen-free-via-openrouter/
---

For months, I’ve been running OpenClaw — a personal AI assistant integrated with Telegram that monitors my crypto portfolio and handles daily tasks. Initially, I used Anthropic’s Claude Sonnet, but the recurring costs add up fast for a 24/7 agent.

OpenRouter’s free tier provides access to capable open-source models like Qwen and Llama at zero cost. Here’s how to migrate your instance without losing functionality or requiring infrastructure changes.

## Why switch to free models?

**Cost elimination**: Free tier removes ongoing expenses for always-on agents. Even modest usage adds up; switching saves hundreds monthly.

**Model flexibility**: OpenRouter’s provider abstraction means you can swap models instantly. If one model degrades or hits rate limits, failover happens seamlessly.

**Solid performance**: Qwen and Llama 3.3 70B handle tool use, JSON generation, and multi-step reasoning well enough for most agent tasks. They’re less “aligned” than commercial APIs, which sometimes means better performance on edge cases.

**No infrastructure lock-in**: Decoupling from a single provider reduces vendor risk. You control which model runs your agent.

## Self-configuring agents (recommended)

If your agent supports dynamic configuration, ask it directly:

    Switch to OpenRouter using this key: sk-or-v1-YOUR_KEY_HERE
    Use Qwen 3.6 Plus (free) as primary model and Llama 3.3 70B (free) as fallback.

The agent registers the API key, updates configuration files, and restarts itself. This takes seconds and requires no manual intervention.

## Manual configuration

If you need direct control or your agent doesn’t self-configure, edit the files directly.

**1. Add the OpenRouter API key** (~/.openclaw/agents/main/agent/auth-profiles.json):

``` json
{
  "profiles": {
    "openrouter:default": {
      "type": "token",
      "provider": "openrouter",
      "token": "sk-or-v1-YOUR_KEY_HERE"
    }
  }
}
```

**2. Update the model configuration** (~/.openclaw/openclaw.json):

``` json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "openrouter/qwen/qwen-plus:free",
        "fallbacks": ["openrouter/meta-llama/llama-3.3-70b-instruct:free"]
      }
    }
  }
}
```

Check OpenRouter’s API documentation for current free model identifiers, as these names change periodically.

**3. Restart the gateway**:

``` bash
openclaw gateway restart
```

Verify the restart completed successfully before testing.

## Testing the migration

After switching, validate that your agent’s core functions still work:

``` bash
# Check gateway logs for connection errors
openclaw logs gateway --tail 50

# Test a simple agent request
openclaw agent main --prompt "What's your current model and provider?"

# Verify tool execution (if applicable)
openclaw agent main --prompt "Fetch the current Bitcoin price"
```

Watch the logs for rate-limit errors or authentication failures. OpenRouter’s free tier has reasonable limits, but sustained high-volume requests may hit thresholds.

## Handling model-specific quirks

Open-source models behave differently than commercial APIs:

- **Less restrictive filtering**: Qwen and Llama don’t refuse requests as aggressively. This can be good for tool-heavy agents but means less safety guardrails.
- **Slightly slower inference**: Expect 20-30% longer response times compared to Claude Sonnet.
- **Different instruction sensitivity**: Some models require more explicit, detailed prompts. Test your agent’s prompts and refine if responses degrade.
- **Token counting**: Free models sometimes handle token limits differently. Monitor for unexpected truncation in long conversations.

## Sandboxing considerations

If your agent accesses sensitive files, logs, or credentials, ensure sandboxing is enabled. Open-source models are less “lobotomized” than commercial APIs, meaning they may follow instructions more literally — including potentially dangerous ones. Run agents in restricted environments when they have access to production systems.

## Fallback and rate limits

The configuration above sets Qwen as primary and Llama as fallback. If the primary model hits rate limits or errors, OpenRouter automatically tries the next in the list. This prevents agent downtime during provider issues.

For production agents, consider:

- Monitoring fallback activation (indicates primary model is struggling)
- Setting multiple fallbacks if you need high availability
- Rotating between free models based on time of day to spread load

## Long-term stability

OpenRouter’s free tier is sustainable because they’re operating on a large user base sharing compute resources. However, free access can be revoked if terms change. Keep your agent flexible enough to switch providers with minimal changes. Using abstraction layers (like OpenClaw’s provider system) makes this straightforward.

If OpenRouter’s free tier becomes unavailable, you can migrate to Ollama (self-hosted) or other free providers by updating just the authentication and model identifiers.
