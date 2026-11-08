---
title: "Parse RSS Feeds and Display as HTML in PHP"
date: 2015-03-08 08:02:12 +0000
layout: post
canonical: https://www.systutorials.com/a-php-function-for-fetching-rss-feed-and-outputing-feed-items-as-html/
---

Displaying RSS feed items on a webpage is a practical way to aggregate external content. Here’s a production-ready approach using PHP’s SimpleXML to fetch, cache, and render feeds as HTML.

## Basic Implementation

This function handles RSS parsing with built-in caching, error handling, and output escaping:

``` php
<?php
function output_rss_feed($feed_url, $item_count = 10, $show_description = true, $show_pubdate = true, $description_length = 200, $cache_hours = 1) {
    $cache_file = sys_get_temp_dir() . '/rss_cache_' . md5($feed_url) . '.xml';
    $use_cache = false;

    // Check cache validity
    if (file_exists($cache_file) && time() - filemtime($cache_file) < ($cache_hours * 3600)) {
        $feed_content = file_get_contents($cache_file);
        $use_cache = true;
    } else {
        // Fetch fresh feed with timeout protection
        $context = stream_context_create([
            'http' => [
                'timeout' => 10,
                'user_agent' => 'PHP RSS Parser/1.0'
            ]
        ]);

        $feed_content = @file_get_contents($feed_url, false, $context);

        if (!$feed_content) {
            echo '<div class="feed-error">Unable to fetch RSS feed</div>';
            return;
        }

        // Save to cache
        file_put_contents($cache_file, $feed_content);
    }

    // Parse XML
    try {
        $rss = simplexml_load_string($feed_content);
        if (!$rss) {
            echo '<div class="feed-error">Invalid RSS feed format</div>';
            return;
        }
    } catch (Exception $e) {
        echo '<div class="feed-error">Error parsing RSS feed: ' . htmlspecialchars($e->getMessage()) . '</div>';
        return;
    }

    // Output feed items
    echo '<div class="feed-lists">';

    $count = 0;
    foreach ($rss->channel->item as $item) {
        if ($count >= $item_count) break;

        $title = htmlspecialchars((string)($item->title ?? 'Untitled'));
        $link = htmlspecialchars((string)($item->link ?? '#'));

        // Try multiple description fields for compatibility
        $description = (string)($item->description ?? $item->{'content:encoded'} ?? '');
        $description = htmlspecialchars(strip_tags($description));

        // Truncate description if needed
        if (strlen($description) > $description_length) {
            $description = substr($description, 0, $description_length) . '...';
        }

        $pubdate = '';
        if ($show_pubdate && isset($item->pubDate)) {
            try {
                $pubdate = date('M d, Y', strtotime((string)$item->pubDate));
            } catch (Exception $e) {
                $pubdate = '';
            }
        }

        echo '<div class="feed-item">';
        echo '<h3><a href="' . $link . '">' . $title . '</a></h3>';

        if ($show_pubdate && !empty($pubdate)) {
            echo '<span class="feed-item-date">' . $pubdate . '</span>';
        }

        if ($show_description && !empty($description)) {
            echo '<div class="feed-description">' . $description . '</div>';
        }

        echo '</div>';
        $count++;
    }

    echo '</div>';
}
?>
```

## Usage

Call the function with your feed URL:

``` php
<?php
output_rss_feed('https://example.com/feed.xml', 10, true, true, 200, 2);
?>
```

**Parameters:**

- `$feed_url` – URL to the RSS feed
- `$item_count` – Number of items to display (default: 10)
- `$show_description` – Include item descriptions (default: true)
- `$show_pubdate` – Include publication dates (default: true)
- `$description_length` – Character limit for descriptions (default: 200)
- `$cache_hours` – Cache duration in hours (default: 1)

## Handling Different Feed Formats

Some feeds use non-standard tags for content. Extend the function to handle Atom feeds and content:encoded tags:

``` php
<?php
function get_feed_content($item) {
    // Try standard RSS description first
    if (isset($item->description) && (string)$item->description !== '') {
        return (string)$item->description;
    }

    // Try content:encoded (common in WordPress feeds)
    if (isset($item->{'content:encoded'}) && (string)$item->{'content:encoded'} !== '') {
        return (string)$item->{'content:encoded'};
    }

    // Try Atom summary
    if (isset($item->summary) && (string)$item->summary !== '') {
        return (string)$item->summary;
    }

    return '';
}
?>
```

## Caching Strategy

The function caches feeds in the system temp directory using an MD5 hash of the URL as the filename. Adjust `$cache_hours` based on feed update frequency:

- **Hourly feeds:** `cache_hours = 1`
- **Slow-moving feeds:** `cache_hours = 6` or higher
- **Real-time critical feeds:** `cache_hours = 0.25` (15 minutes)

To clear cache manually:

``` php
<?php
$cache_file = sys_get_temp_dir() . '/rss_cache_' . md5($feed_url) . '.xml';
if (file_exists($cache_file)) {
    unlink($cache_file);
}
?>
```

## Styling

Add CSS to style feed output:

``` css
.feed-lists {
    list-style: none;
    padding: 0;
    margin: 0;
}

.feed-item {
    margin-bottom: 20px;
    padding: 15px;
    border-bottom: 1px solid #ddd;
}

.feed-item h3 {
    margin-top: 0;
    margin-bottom: 8px;
}

.feed-item h3 a {
    color: #0066cc;
    text-decoration: none;
}

.feed-item h3 a:hover {
    text-decoration: underline;
}

.feed-item-date {
    display: block;
    font-size: 0.85em;
    color: #666;
    margin-bottom: 10px;
}

.feed-description {
    padding-left: 10px;
    margin-left: 10px;
    border-left: 2px solid #eee;
    color: #444;
    line-height: 1.5;
}

.feed-error {
    padding: 10px;
    background-color: #fee;
    color: #c00;
    border: 1px solid #fcc;
    border-radius: 3px;
}
```

## Security and Performance Considerations

**Output escaping:** Always use `htmlspecialchars()` on user-controlled or external data to prevent XSS attacks. The function escapes all title, link, and description content.

**Timeout protection:** Set realistic timeouts to prevent hanging requests. A 10-second timeout is reasonable for most scenarios; adjust down for time-critical applications.

**Feed validation:** Some feeds have malformed XML or missing standard tags. The error handling gracefully falls back to empty values rather than breaking.

**User-Agent header:** Add a descriptive User-Agent string when fetching feeds. Some feed hosts reject requests without one.

**Alternative libraries:** For complex feed scenarios (Atom 1.0, media RSS, podcasts), consider `FeedIo` or `Zend Feed` packages from Composer:

``` bash
composer require debril/feed-io
```

These libraries handle edge cases and namespace variations better than SimpleXML alone, though SimpleXML works fine for standard RSS 2.0 and basic Atom feeds.
