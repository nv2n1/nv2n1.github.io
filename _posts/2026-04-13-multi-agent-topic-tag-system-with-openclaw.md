---
title: "Multi-Agent Topic/Tag System with OpenClaw"
date: 2026-04-13 15:15:13 +0000
author: "Eric Ma"
layout: post
categories: [ai-engineering]
canonical: /multi-agent-topic-tag-system-with-openclaw/
---

When running multiple OpenClaw agents on the same Telegram group, you can use Telegram’s topic feature to enable agent isolation. This guide explains the actual setup used for Eric’s OpenClaw group with multi-agent support.

### The Setup

The configuration uses Telegram topics to isolate different agents so they don’t interfere with each other. Each agent works in its own topic while sharing the same group. This prevents conflicts and enables parallel operation.

### Step-by-Step Configuration

#### Step 1: Create Telegram Supergroup

Start with a Telegram supergroup that supports topics:

1.  Convert your existing group to a supergroup (if not already)
2.  Enable topics in group settings
3.  Note the group ID for OpenClaw configuration

#### Step 2: Configure OpenClaw Telegram Plugin

Open OpenClaw gateway configuration and configure the Telegram plugin with the following settings:

- **Group ID:** Your Telegram supergroup ID (e.g., -1003985866461)
- **Privacy Settings:** Allow the OpenClaw Telegram bot to access the group

#### Step 3: Set Up Isolation with Topics

Configure topic-based isolation in OpenClaw configuration:

```wp-block-code
{
  "plugins": {
    "entries": {
      "telegram": {
        "dmPolicy": "pairing",
        "groupPolicy": "open",
        "topics": {
          "policy": "allowlist",
          "allowlist": ["general", "blog", "academy", "news", "analytics"]
        }
      }
    }
  }
}
```

Key settings explained:

- **dmPolicy: “pairing”** — New users must pair via QR code or invite link
- **groupPolicy: “open”** — The OpenClaw bot can join and work in the group
- **topics.policy: “allowlist”** — Only specified topics are allowed for agent operations
- **topics.allowlist** — Array of allowed topic names for your agents

#### Step 4: Create Topics in Telegram Group

Manually create the topics you specified in OpenClaw configuration:

1.  Open the Telegram group
2.  Create each topic: \#general, \#blog, \#academy, \#news, \#analytics
3.  Ensure topic names exactly match the allowlist in your configuration

#### Step 5: Assign Agents to Topics

Each OpenClaw agent is configured to work in a specific topic. This is done in the agent’s configuration:

- **\#general** — General conversations and coordination
- **\#blog** — Blog post creation and updates
- **\#academy** — Academy and hub management tasks
- **\#news** — News articles and announcements
- **\#analytics** — Statistics, reporting, and monitoring

When an agent sends a message to its assigned topic, it only responds to messages in that topic. Messages from other topics are ignored by default.

### Benefits of This Setup

- **Isolation:** Each agent operates in its own topic without interference from others
- **Parallel Operation:** Multiple agents can work simultaneously on different tasks
- **Clear Boundaries:** Messages and commands are scoped to specific topics
- **Easy Management:** Topic-based filtering makes it easy to see what each agent is doing

### How It Works in Practice

Here is the actual use case from Eric’s OpenClaw group:

1.  **Content Writing:** Blog post extensions happen in \#blog topic
2.  **Academy Management:** Updates to academies and hubs happen in \#academy topic
3.  **Analytics:** Statistics and reporting happen in \#analytics topic
4.  **Coordination:** General conversation and instructions happen in \#general topic
5.  **News:** News articles and announcements happen in \#news topic

This setup enables 24/7 operation with multiple specialized agents working in parallel without conflicts.

### Configuration Notes

Important notes for successful implementation:

- **Topic Names:** Must exactly match between Telegram and OpenClaw configuration
- **Supergroup Requirement:** Topics are only available in supergroups (not regular groups)
- **Bot Permissions:** The Telegram bot must have permissions to create and post in topics
- **Case Sensitivity:** Topic names in allowlist should match topic creation exactly

### Conclusion

Using Telegram topics with OpenClaw provides a simple yet powerful way to isolate multiple agents in a single group. Each agent works in its own topic while benefiting from shared infrastructure. This setup scales well and is easy to maintain.
