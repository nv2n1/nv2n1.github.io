---
title: "Man Page Heading Cleanup Tracker"
url: "/man-heading-cleanup/"
description: "Tracks which man pages have had redundant first h2 heading removed"
---

# Man Page Heading Cleanup Tracker

This page tracks man pages that have been cleaned up by removing the **first h2 heading** if it's one of: `NAME`, `INTRO`, `INTRODUCTION`, `DESCRIPTION`, or `SYNOPSIS`. The page title and header block already identify the page, making these first headings redundant.

## Cleanup Rules

Remove the **first h2 heading only** if it matches one of:
- `NAME`
- `INTRO`
- `INTRODUCTION`
- `DESCRIPTION`
- `SYNOPSIS`

All content paragraphs are preserved. Subsequent headings (even if they match) are not removed.

## Cleaned Pages

| Man Page | Section | Date Cleaned | Removed Heading | Notes |
|----------|---------|--------------|-----------------|-------|
| [repo(1)](/docs/linux/man/1-repo/) | 1 | 2024-11-21 | NAME | Sample 1 |
| [user_namespaces(7)](/docs/linux/man/7-user_namespaces/) | 7 | 2024-11-21 | NAME | Sample 2 |
| [ocf_heartbeat_icp(7)](/docs/linux/man/7-ocf_heartbeat_icp/) | 7 | 2024-11-21 | NAME | Sample 3 |

## Future Use

When re-building man pages, check this page to see which files have been cleaned. The cleanup script is at `scripts/fix-man-headings.py`.

Run the script on uncommitted man-src files to apply the same cleanup:
```bash
python3 scripts/fix-man-headings.py
```