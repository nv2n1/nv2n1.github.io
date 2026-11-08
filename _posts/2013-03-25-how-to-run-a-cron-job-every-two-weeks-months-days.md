---
title: "How to Schedule Cron Jobs at Custom Intervals"
date: 2013-03-25 13:06:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-run-a-cron-job-every-two-weeks-months-days/
---

Crontab controls what runs and when. Each crontab entry has this format:

    .---------------- minute (0-59)
    |  .------------- hour (0-23)
    |  |  .---------- day of month (1-31)
    |  |  |  .------- month (1-12) OR jan,feb,mar,apr ...
    |  |  |  |  .---- day of week (0-6) (Sunday=0 or 7) OR sun,mon,tue ...
    |  |  |  |  |
    *  *  *  *  *  command to be executed

To edit your user’s crontab:

``` bash
crontab -e
```

By default, cron uses `/bin/sh`. Override it by adding this at the top of your crontab file:

    SHELL=/bin/bash

Check `crontab(5)` and `cron(8)` man pages for full details. For complex scheduling needs, consider `systemd` timers as an alternative.

## Method 1: Step Values

Crontab supports step syntax with `/`. The expression `1-9/2` equals `1,3,5,7,9`.

For jobs every two months at 1:00 AM on the 1st:

    0 1 1 */2 * /path/to/command

For jobs every two days at 1:00 AM:

    0 1 */2 * * /path/to/command

**Important caveat**: This isn’t always “exactly” every N time units. `*/2` on day-of-month means “every other day that exists in the month,” and `*/2` on month means “every other month in the year.” If you need precise intervals (e.g., exactly 48 hours), use Method 2 or 3.

## Method 2: Conditional Test in the Command

Since cron executes shell code, you can run a job frequently and guard the actual command with a test condition.

For a job every 2 days (exactly 172,800 seconds), at 1:00 AM daily:

    0 1 * * * [ $((($(date +%s) / 86400) % 2)) -eq 0 ] && /path/to/command

This calculates days since Unix epoch (1970-01-01 00:00:00 UTC), divides by 2, and only runs when the remainder is 0.

For a job every 5 months starting from March 2016, at 1:00 AM:

    0 1 1 * * [ $((($(date +%Y) - 2016) * 12 + $(date +%m) - 3) % 5)) -eq 0 ] && /path/to/command

This calculates months elapsed since March 2016 and runs only when divisible by 5.

For a job every 2 weeks at 2:00 AM on Tuesday:

    0 2 * * 2 [ $((($(date +%s) / 604800) % 2)) -eq 0 ] && /path/to/command

Where 604800 = seconds in a week.

## Method 3: State File Tracking

Create a wrapper script that uses a marker file on disk to track whether the job ran on its last invocation.

Example script at `/home/share/bin/backup-job`:

``` bash
#!/bin/bash

mark_file="$HOME/.backup-job-marker"

if [ -e "$mark_file" ]; then
    rm -f "$mark_file"
    # Run the actual job
    /path/to/backup/command
else
    touch "$mark_file"
    exit 0
fi
```

First run: marker doesn’t exist, so it’s created and the script exits.\
Second run: marker exists, so it’s removed and the command runs.\
Third run: repeats cycle.

If this script runs weekly via cron, the job executes every two weeks.

Add to crontab:

    0 2 * * 2 /home/share/bin/backup-job

This runs your backup at 2:00 AM every other Tuesday.

You can extend this approach with timestamps or other state:

``` bash
#!/bin/bash

mark_file="$HOME/.job-marker"
days_between=14

if [ -e "$mark_file" ]; then
    last_run=$(stat -c %Y "$mark_file")
    now=$(date +%s)
    if [ $(((now - last_run) / 86400)) -ge "$days_between" ]; then
        /path/to/command
        touch "$mark_file"
    fi
else
    touch "$mark_file"
fi
```

This ensures the command runs at most once per 14-day window.

## Comparison

| Method | Pros | Cons |
|----|----|----|
| Step values | Simple, readable | Not exact time intervals |
| Conditional test | Precise intervals, inline | Complex syntax, harder to debug |
| State file | Flexible, handles edge cases | Requires script file, disk I/O |

Choose based on your accuracy requirements and complexity tolerance. For production backup jobs or critical infrastructure work, Method 2 or 3 offers better guarantees.
