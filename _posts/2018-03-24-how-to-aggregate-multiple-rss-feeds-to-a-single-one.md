---
title: "Self-Hosted RSS Feed Aggregators: Build Your Own"
date: 2018-03-24 08:22:50 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-aggregate-multiple-rss-feeds-to-a-single-one/
---

Aggregating multiple RSS feeds into a single source is essential for monitoring diverse content — whether tracking news, blogs, project updates, or monitoring systems. Here are the practical approaches with working examples for 2026.

## Self-Hosted Feed Readers

**Miniflux** is the modern standard for self-hosted feed aggregation. Written in Go, it’s lightweight, actively maintained, and provides a clean web interface plus REST API for programmatic access.

Deploy with Docker:

``` bash
docker run -d \
  --name miniflux \
  -p 8080:8080 \
  -e DATABASE_URL="postgres://user:pass@db:5432/miniflux" \
  -e ADMIN_USERNAME="admin" \
  -e ADMIN_PASSWORD="password" \
  miniflux/miniflux:latest
```

Initialize the database:

``` bash
docker exec miniflux /miniflux -migrate
```

Then access the web interface at `http://localhost:8080`. Import your feeds via OPML file or add them individually through the UI. Miniflux handles subscription management, deduplication, and filtering natively.

**Newsboat** is a terminal-based alternative if you prefer command-line tools. It aggregates feeds locally without requiring infrastructure:

Configure `~/.newsboat/urls`:

    http://example.com/feed1.xml
    http://example.com/feed2.xml
    https://another-site.com/rss

Then run:

``` bash
newsboat
```

Export aggregated results to OPML:

``` bash
newsboat -e > all_feeds.opml
```

## Python-Based Aggregation

For generating a combined RSS feed output, use `feedparser` and `rfeed`:

``` bash
pip install feedparser rfeed
```

Create an aggregator script:

``` python
#!/usr/bin/env python3
from rfeed import Feed, Item
import feedparser
from datetime import datetime

feed_urls = [
    'http://example.com/feed1.xml',
    'http://example.com/feed2.xml',
    'http://example.com/feed3.xml'
]

# Create output feed
aggregated = Feed(
    title="Aggregated Feed",
    link="http://localhost",
    description="Multiple feeds combined",
    language="en"
)

all_entries = []

# Parse all feeds
for feed_url in feed_urls:
    try:
        parsed = feedparser.parse(feed_url)
        for entry in parsed.entries:
            all_entries.append({
                'title': entry.get('title', 'Untitled'),
                'link': entry.get('link', ''),
                'description': entry.get('summary', entry.get('description', '')),
                'published': entry.get('published', ''),
                'author': entry.get('author', ''),
                'source': parsed.feed.get('title', 'Unknown')
            })
    except Exception as e:
        print(f"Error parsing {feed_url}: {e}")

# Sort by publication date (newest first)
all_entries.sort(key=lambda x: x['published'], reverse=True)

# Add to output feed
for entry in all_entries:
    aggregated.add_item(Item(
        title=f"[{entry['source']}] {entry['title']}",
        link=entry['link'],
        description=entry['description'],
        pubDate=entry['published'],
        author=entry['author']
    ))

# Output as RSS
print(aggregated.rss())
```

Run it and pipe to a file:

``` bash
python3 aggregate_feeds.py > combined.rss
```

For regular updates, schedule it with cron:

``` bash
*/30 * * * * /home/user/aggregate_feeds.py > /var/www/html/combined.rss
```

## Advanced Filtering and Processing

Add filtering to the Python script to skip duplicate titles or old entries:

``` python
import hashlib
from datetime import datetime, timedelta

seen_titles = set()
cutoff_date = datetime.now() - timedelta(days=30)

for entry in all_entries:
    # Skip duplicates
    title_hash = hashlib.md5(entry['title'].encode()).hexdigest()
    if title_hash in seen_titles:
        continue

    # Skip entries older than 30 days
    try:
        pub_date = datetime.strptime(entry['published'], '%a, %d %b %Y %H:%M:%S %Z')
        if pub_date < cutoff_date:
            continue
    except:
        pass

    seen_titles.add(title_hash)
    aggregated.add_item(Item(...))
```

## Online Alternatives

**RSS Bridge** generates RSS feeds from sites without native feed support, and you can aggregate those outputs afterward. Self-host or use public instances.

**Inoreader** is a commercial service with advanced aggregation, filtering, search, and team collaboration. No self-hosting required.

FeedBurner is no longer recommended — it’s in maintenance mode with minimal support.

## Choosing Your Approach

- **Personal use with privacy**: Miniflux self-hosted or Newsboat
- **Generating a combined feed file**: Python script with feedparser + rfeed
- **Team/enterprise with features**: Miniflux self-hosted or Inoreader
- **Monitoring systems for alerts**: Python script with conditional email/webhook triggers

For most technical teams, Miniflux strikes the right balance between simplicity, control, and functionality. For one-off aggregation or custom integrations, the Python approach gives you maximum flexibility to process, filter, and transform feeds however you need.
