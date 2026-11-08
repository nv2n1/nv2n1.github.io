---
title: "Speeding Up journalctl: Performance Tips and Filtering Strategies"
date: 2018-03-24 11:49:37 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-make-journalctl-faster/
---

When you run `journalctl` without options on a system with years of log history, it can take seconds or even minutes to parse everything. The slowness comes from journalctl loading and deserializing potentially gigabytes of journal data. The solution is targeted querying — you almost never need the entire journal, so restrict what journalctl reads from disk.

## Limit output with -n (most recent entries)

The simplest optimization is showing only recent logs:

``` bash
journalctl -n 100
```

This shows the last 100 journal entries and exits immediately. For a quick log check, this is often all you need. You can adjust the number up or down based on context.

To follow logs in real-time (like `tail -f`):

``` bash
journalctl -f
```

This is useful for monitoring services or troubleshooting live issues without scanning the entire journal.

## Filter by boot session

Since boot cycles are discrete units, querying a specific boot is much faster than searching the full journal:

``` bash
journalctl -b
```

Shows logs from the current boot only. To see logs from previous boots:

``` bash
journalctl -b -1
journalctl -b -2
```

The `-1` is the previous boot, `-2` is two boots ago, and so on. List all available boots with:

``` bash
journalctl --list-boots
```

## Filter by time range

For a specific time window, use `--since` and `--until`:

``` bash
journalctl --since "2025-01-15 10:00:00" --until "2025-01-15 12:00:00"
journalctl --since "1 hour ago"
journalctl --since "today"
```

These are much faster than scanning the entire journal.

## Filter by unit or service

If you’re troubleshooting a specific service, query only that unit’s logs:

``` bash
journalctl -u nginx.service
journalctl -u ssh.service -n 50
```

Combine with other filters for even faster results:

``` bash
journalctl -u postgresql.service --since "1 hour ago"
```

## Filter by priority level

Reduce noise by showing only important messages:

``` bash
journalctl -p err
journalctl -p warning
```

Priority levels: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`. Show errors and above:

``` bash
journalctl -p err..emerg
```

## Combine multiple filters

Stack filters for surgical precision:

``` bash
journalctl -u nginx.service -p err --since "today" -n 50
```

This shows the last 50 error-level messages from nginx since midnight — nearly instant, even on large journals.

## Use grep for pattern matching

For pattern-based filtering on the output (not the journal itself), pipe to grep:

``` bash
journalctl -u mysql.service | grep -i "connection"
```

Note: This still reads the full unit’s logs, so it’s not as fast as other filters, but it’s useful when you need pattern matching.

## Check journal size

If journalctl remains slow despite filtering, your journal may have grown too large. Check its size:

``` bash
journalctl --disk-usage
```

You can rotate and limit journal size in `/etc/systemd/journald.conf`:

``` ini
SystemMaxUse=500M
RuntimeMaxUse=100M
MaxRetentionDays=30
```

Then restart journald:

``` bash
sudo systemctl restart systemd-journald
```

This prevents unbounded growth and keeps queries snappy.

## Practical workflow

In day-to-day use, combine filtering strategies:

- **Quick health check:** `journalctl -b -p err` — errors from current boot
- **Service troubleshooting:** `journalctl -u service-name --since "10 minutes ago" -f` — follow a service’s recent logs
- **Overnight incident review:** `journalctl -b -1 -p warning..emerg` — warnings and errors from the previous boot
- **Authentication issues:** `journalctl -u ssh.service -p err -n 20` — recent SSH errors

The key is always asking “do I actually need to read this data?” before letting journalctl scan the journal. With targeted queries, journalctl becomes a fast, indispensable tool.
