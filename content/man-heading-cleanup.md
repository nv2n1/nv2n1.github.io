---
title: "Man Page Heading Cleanup Tracker"
url: "/man-heading-cleanup/"
description: "Tracks which man pages have had redundant NAME/SYNOPSIS/DESCRIPTION headings removed"
---

# Man Page Heading Cleanup Tracker

This page tracks man pages that have been cleaned up by removing redundant `<h2 class="name">NAME</h2>`, `<h2>SYNOPSIS</h2>`, and `<h2>DESCRIPTION</h2>` headings. The page title and header block already identify the page, making these headings redundant.

## Cleanup Rules

Remove the **first occurrence** of each of these headings (keep all content paragraphs):
- `<h2 class="name">NAME</h2>`
- `<h2>SYNOPSIS</h2>`
- `<h2>DESCRIPTION</h2>`

## Cleaned Pages

| Man Page | Section | Date Cleaned | Notes |
|----------|---------|--------------|-------|
| [repo(1)](/docs/linux/man/1-repo/) | 1 | 2024-11-21 | Sample 1 |
| [user_namespaces(7)](/docs/linux/man/7-user_namespaces/) | 7 | 2024-11-21 | Sample 2 |
| [ocf_heartbeat_icp(7)](/docs/linux/man/7-ocf_heartbeat_icp/) | 7 | 2024-11-21 | Sample 3 |

## Future Use

When re-building man pages, check this page to see which files have been cleaned. The cleanup script is at `scripts/fix-man-headings.py`.

Run the script on uncommitted man-src files to apply the same cleanup:
```bash
python3 scripts/fix-man-headings.py
```