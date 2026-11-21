---
title: "Man Page Heading Cleanup Tracker"
url: "/man-heading-cleanup/"
description: "Tracks which man pages have had redundant leading subtitle heading removed"
---

# Man Page Heading Cleanup Tracker

This page tracks man pages cleaned up by removing a **redundant leading subtitle heading**. The page title and header block already identify the page, so a page should start with content text rather than a redundant subtitle.

## Cleanup Rule

Remove the **first h2 heading** of the body only when **both** hold:

1. Its text is one of (case-insensitive): `NAME`, `INTRO`, `INTRODUCTION`, `DESCRIPTION`, `SYNOPSIS`
2. The body does **not** already start with meaningful text before that heading — i.e. the heading is the very first content

**Pages whose body already begins with a text paragraph keep all their headings.** In those pages the leading paragraph *is* the subtitle (previously under a `NAME` heading, removed in pass 1), and the following `SYNOPSIS`/`DESCRIPTION`/… headings are informative section headers that must stay.

Non-exact variants (e.g. `DETAILED DESCRIPTION`, `SYNTAX`, `C SYNOPSIS`) are intentionally kept.

## Passes

| Pass | Date | Scope | Files changed | Script state |
|------|------|-------|---------------|--------------|
| 1 (#79) | 2026-11-21 | All files, one heading per file | 22,981 (mostly `</p>` cleanup + uppercase `NAME` removal) | Buggy: no `re.IGNORECASE` → missed mixed-case headings |
| 2 (this PR) | 2026-11-21 | Stragglers only | **240** | Fixed: case-insensitive match + "no text before heading" guard |

### Pass 2 details

Audit after pass 1 found 56,865 files in `man-src/`:

- **49,605** already start with text before their first h2 — compliant, left untouched
- **242** started directly with a target heading (true stragglers): 212 × `Name` (mixed case, missed by pass 1's regex bug), 29 × `SYNOPSIS`, 1 × `Introduction`
- **242 removed** — zero remain

Post-pass-2 verification: **0 stragglers remain**. The script is idempotent (a re-run changes 0 files).

## Cleaned Pages (samples)

| Man Page | Pass | Removed Heading | Notes |
|----------|------|-----------------|-------|
| [repo(1)](/docs/linux/man/1-repo/) | 1 | NAME | Sample 1 |
| [user_namespaces(7)](/docs/linux/man/7-user_namespaces/) | 1 | NAME | Sample 2 |
| [ocf_heartbeat_icp(7)](/docs/linux/man/7-ocf_heartbeat_icp/) | 1 | NAME | Sample 3 |
| [rmic-java-1(1)](/docs/linux/man/1-rmic-java-1/) | 2 | Name (mixed case) | Straggler from pass 1 regex bug |
| [unopkg(1)](/docs/linux/man/1-unopkg/) | 2 | Name (mixed case) | Straggler from pass 1 regex bug |

## Future Use

When re-building man pages, run the script before committing — it only touches files that violate the rule, and is safe to re-run at any time:

```bash
python3 scripts/fix-man-headings.py          # verbose
python3 scripts/fix-man-headings.py -q       # quiet (batch)
python3 scripts/fix-man-headings.py man-src/1/s/sort.md   # specific files
```
