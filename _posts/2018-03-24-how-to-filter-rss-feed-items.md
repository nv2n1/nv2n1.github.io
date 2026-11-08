---
title: "Filter RSS Feeds by Keywords and Custom Rules"
date: 2018-03-24 11:45:01 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-filter-rss-feed-items/
---

Filtering RSS feeds lets you reduce noise and focus on content that actually matters. Whether you want to exclude posts mentioning certain topics or only see items matching specific keywords, there are several practical approaches depending on your setup.

## Using dedicated feed filtering services

**Feed43** (<a href="https://www.feed43.com/" rel="nofollow noopener" target="_blank">https://www.feed43.com/</a>) is one of the most reliable web-based tools for filtering and transforming RSS feeds. It lets you:

- Extract content from web pages and convert them to RSS
- Filter feeds by keywords (include or exclude)
- Extract specific fields and restructure the output
- Combine multiple feeds with rules applied

Create a new feed, paste your source RSS URL, and set up rules like “keep only items containing: python” or “exclude items with: deprecated”.

**Feedburner alternatives** like **Zapier** (<a href="https://zapier.com/" rel="nofollow noopener" target="_blank">https://zapier.com/</a>) can route RSS items to various actions based on conditions. You create a “Zap” that triggers when new feed items arrive, then apply filters:

- Contains specific keywords
- Doesn’t contain keywords
- Matches patterns or tags
- Published by specific authors

## Filtering with command-line tools

For more control, especially if you’re processing feeds regularly, use command-line utilities:

**Using `xmllint` and `grep`:**

``` bash
curl -s https://example.com/feed.xml | \
  xmllint --xpath "//item[contains(title, 'keyword')]" - | \
  xmllint --format -
```

**Using Python with `feedparser`:**

``` python
import feedparser

feed = feedparser.parse('https://example.com/feed.xml')

filtered = [
    entry for entry in feed.entries
    if 'keyword' in entry.title.lower() and 
       'exclude_word' not in entry.title.lower()
]

for entry in filtered:
    print(f"{entry.title}\n{entry.link}\n")
```

Install feedparser: `pip install feedparser`

**Using `jq` for JSON feeds:**

``` bash
curl -s https://api.example.com/feed.json | \
  jq '.items[] | select(.title | contains("keyword"))'
```

## Self-hosted solutions

**Miniflux** (<a href="https://miniflux.app/" rel="nofollow noopener" target="_blank">https://miniflux.app/</a>) is a lightweight, self-hosted feed reader that supports keyword filtering and has integrations with services like Pocket. It offers:

- Built-in filtering rules per subscription
- Full-text search across all articles
- Custom entry template filtering
- API for automation

**FreshRSS** (<a href="https://www.freshrss.org/" rel="nofollow noopener" target="_blank">https://www.freshrss.org/</a>) provides similar functionality with more granular control:

- Per-feed keyword filtering
- Rules engine for automatic categorization
- Support for feed transformations
- Simplistic to complex rule structures

## Building your own filter

For maximum flexibility, create a simple systemd timer that processes feeds hourly:

``` python
#!/usr/bin/env python3
import feedparser
import json
from datetime import datetime

RULES = {
    'include': ['golang', 'rust', 'linux'],
    'exclude': ['windows', 'deprecated']
}

def filter_feed(feed_url, rules):
    feed = feedparser.parse(feed_url)
    filtered = []

    for entry in feed.entries:
        text = (entry.get('title', '') + ' ' + 
                entry.get('summary', '')).lower()

        # Check include rules (OR logic)
        if rules['include'] and not any(
            word in text for word in rules['include']
        ):
            continue

        # Check exclude rules
        if any(word in text for word in rules['exclude']):
            continue

        filtered.append(entry)

    return filtered
```

Save as `feed_filter.py`, make it executable, and call it from a cron job or systemd timer to generate a filtered RSS feed on a schedule.

## Choosing the right approach

- **Web-based tools**: Best for quick setup, no technical overhead
- **Command-line tools**: Ideal for one-off filtering or scripting into automation
- **Self-hosted readers**: Good for long-term, private feed management with complex rules
- **Custom scripts**: Necessary when you need specific logic or multiple filtering stages

Most feeds benefit from a combination: use your reader’s built-in filters for common keywords, and supplementary tools like Feed43 for edge cases where feeds lack proper categorization.
