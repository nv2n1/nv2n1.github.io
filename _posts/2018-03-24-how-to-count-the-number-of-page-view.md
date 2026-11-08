---
title: "How to Count Page Views in Your Web Application"
date: 2018-03-24 08:18:51 +0000
modified: 2026-04-11 16:06:18 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-count-the-number-of-page-view/
---

Counting page views isn’t as simple as incrementing a counter. You need to handle edge cases: duplicate views from the same user, multiple users behind a single IP (corporate networks), and bots. Here’s how to build a robust system.

## The Problem with IP-Based Counting

Relying on IP addresses fails in several scenarios:

- Multiple users behind a corporate firewall or NAT share the same IP
- Mobile users switch between networks (WiFi to cellular)
- VPN users appear to come from the same exit node
- IPv6 rotation is common for ISPs

A session-based approach is more reliable.

## Session-Based Page View Counting

Use session IDs (typically stored in cookies or via URL parameters for tracking pixel endpoints) to identify unique viewers within a time window. Here’s a practical schema:

``` sql
CREATE TABLE page_views (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    page_id INT NOT NULL,
    session_id VARCHAR(255) NOT NULL,
    viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address INET,
    user_agent TEXT,
    INDEX (page_id, session_id, viewed_at),
    INDEX (viewed_at)
);

CREATE TABLE page_view_counts (
    page_id INT PRIMARY KEY,
    total_views BIGINT DEFAULT 0,
    unique_sessions_24h BIGINT DEFAULT 0,
    unique_sessions_30d BIGINT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

Sample data:

``` sql
INSERT INTO page_views (page_id, session_id, ip_address, user_agent) VALUES
(1, 'sess_abc123', '192.168.1.100', 'Mozilla/5.0...'),
(1, 'sess_xyz789', '192.168.1.100', 'Mozilla/5.0...'),
(1, 'sess_abc123', '192.168.1.100', 'Mozilla/5.0...'),
(2, 'sess_abc123', '192.168.2.50', 'Mozilla/5.0...');
```

## Deduplication Logic

When a page is viewed, execute this logic:

``` python
from datetime import datetime, timedelta
import hashlib
import secrets

def record_page_view(page_id, session_id, request_obj):
    """Record a page view with deduplication."""

    # If no session exists, create one
    if not session_id:
        session_id = f"sess_{secrets.token_hex(16)}"

    now = datetime.utcnow()
    thirty_mins_ago = now - timedelta(minutes=30)

    # Check if this session viewed this page in the last 30 minutes
    recent_view = db.query("""
        SELECT COUNT(*) as count FROM page_views
        WHERE page_id = %s 
        AND session_id = %s 
        AND viewed_at > %s
    """, (page_id, session_id, thirty_mins_ago))

    if recent_view[0]['count'] == 0:
        # Record this as a new view
        db.insert("""
            INSERT INTO page_views (page_id, session_id, ip_address, user_agent)
            VALUES (%s, %s, %s, %s)
        """, (page_id, session_id, request_obj.remote_addr, request_obj.user_agent))

        # Update counters
        db.execute("""
            UPDATE page_view_counts SET total_views = total_views + 1
            WHERE page_id = %s
        """, (page_id,))

    # Cleanup old entries (older than 24 hours for example)
    cleanup_threshold = now - timedelta(hours=24)
    db.execute("""
        DELETE FROM page_views
        WHERE page_id = %s AND viewed_at < %s
    """, (page_id, cleanup_threshold))
```

## Computing Aggregate Counts

Use materialized views or scheduled jobs to compute counts efficiently:

``` sql
-- Update unique session counts (run every 5-15 minutes)
UPDATE page_view_counts pvc
SET 
    unique_sessions_24h = (
        SELECT COUNT(DISTINCT session_id) FROM page_views
        WHERE page_id = pvc.page_id
        AND viewed_at > DATE_SUB(NOW(), INTERVAL 24 HOUR)
    ),
    unique_sessions_30d = (
        SELECT COUNT(DISTINCT session_id) FROM page_views
        WHERE page_id = pvc.page_id
        AND viewed_at > DATE_SUB(NOW(), INTERVAL 30 DAY)
    ),
    last_updated = NOW();
```

## For High-Traffic Sites

At scale, use Redis for real-time tracking:

``` python
import redis
import json

r = redis.Redis(host='localhost', db=0)

def record_page_view_redis(page_id, session_id):
    """Efficient deduplication using Redis."""

    now = int(datetime.utcnow().timestamp())
    window_key = f"page:{page_id}:views:30m"

    # Check if session viewed this page recently
    member = f"{session_id}:{now}"

    if r.zscore(window_key, session_id) is None:
        # New view within the window
        r.zadd(window_key, {session_id: now})
        r.zremrangebyscore(window_key, 0, now - 1800)  # Remove entries older than 30 mins

        # Increment counter in database asynchronously
        queue.enqueue('increment_view_count', page_id)

    return session_id
```

## Client-Side Implementation

For server-side tracking, set a session cookie on first visit:

``` javascript
// JavaScript tracking pixel / async call
function trackPageView(pageId) {
    let sessionId = getCookie('tracking_session');
    if (!sessionId) {
        sessionId = 'sess_' + generateUUID();
        setCookie('tracking_session', sessionId, 365); // 1 year
    }

    fetch('/api/track', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({page_id: pageId, session_id: sessionId})
    });
}
```

## Key Takeaways

- Session IDs beat IP addresses for accuracy
- Implement deduplication at the application layer
- Use a time window (30 minutes to 24 hours) to avoid counting repeated views
- For high traffic, offload counts to cache layers (Redis, memcached)
- Clean up old data regularly to manage database size
- Materialize aggregate counts separately from raw events

This approach scales from small sites to millions of daily views while maintaining accuracy across diverse network configurations.
