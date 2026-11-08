---
title: "Mastering pkill and pgrep for Process Management"
date: 2013-07-12 16:32:20 +0000
modified: 2026-04-12 04:41:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /pkill-and-pgrep-process-management-commands/
---

`pgrep` and `pkill` are essential tools for finding and signaling processes by name and attributes. They’re far more precise than grepping `ps` output and should be your go-to for process management scripts and one-liners.

## pgrep: Find Process IDs

`pgrep` searches running processes and outputs matching PIDs. All selection criteria must match unless you use alternatives (comma-separated values act as OR).

``` bash
pgrep -u root sshd        # sshd processes owned by root
pgrep -u root,daemon      # processes owned by root OR daemon
pgrep -f "python main.py" # match full command line
pgrep -x nginx            # exact process name match only
```

## pkill: Signal Processes

`pkill` sends a signal (default SIGTERM) to matching processes instead of listing them:

``` bash
pkill -HUP syslogd           # send SIGHUP to syslogd
pkill -9 firefox             # SIGKILL unresponsive processes
pkill -TERM -u username      # terminate all processes by user
pkill -f "node.*worker"      # signal by command line pattern
```

## Common Options

**Selection criteria:**

- `-u euid` – match by effective user ID (name or number)
- `-U uid` – match by real user ID
- `-g pgrp` – match by process group ID
- `-G gid` – match by group ID (name or number)
- `-P ppid` – match by parent process ID
- `-t term` – match by controlling terminal (e.g., `pts/0`)
- `-s sid` – match by session ID

**Matching:**

- `-f` – match against full command line, not just process name. Crucial for scripts with generic names
- `-x` – exact match only (no substring matching)
- `-v` – invert match (exclude matching processes)

**Process selection:**

- `-n` – select only the newest matching process
- `-o` – select only the oldest matching process
- `-l` – list process names alongside PIDs (pgrep only)
- `-d delimiter` – change output delimiter (pgrep only)

**Signals (pkill):**

- Use numeric (`-9`) or symbolic (`-KILL`) form
- Common: TERM (15, graceful), KILL (9, force), HUP (1, reload config)

## Practical Examples

**Reload a service without finding the PID manually:**

``` bash
pkill -HUP nginx          # nginx rereads config
pkill -TERM -u appuser    # stop all processes for a user
```

**Combine with other tools:**

``` bash
# Get detailed info on matching processes
ps -fp $(pgrep -d, -x python3)

# Count matching processes
pgrep -c redis

# Kill all zombies from a parent
pkill -P 1234 -9
```

**Match by command line:**

``` bash
# Kill specific Python script (not all Python processes)
pkill -f "celery worker"

# Only exact full command match
pkill -fx "/usr/bin/python3 /opt/app/main.py"
```

**Age-based selection:**

``` bash
pgrep -n -u postgres    # newest postgres process
pgrep -o java           # oldest Java process
```

## Important Behavior

- `pgrep` and `pkill` never match themselves
- Process names are limited to 15 characters in `/proc/[pid]/stat` — use `-f` to match against the full `/proc/[pid]/cmdline`
- Extended Regular Expressions are supported in patterns
- Exit status: 0 if matches found, 1 if no matches, 2 for syntax error, 3 for fatal error

## Avoid Common Mistakes

**Don’t use bare process names with common tools:**

``` bash
# BAD: might match unexpected processes
pkill java

# GOOD: be specific with full command matching
pkill -f "java.*myapp.jar"
```

**Verify matches before signaling:**

``` bash
# Preview what you're about to kill
pgrep -f "nginx master"

# Then signal it
pkill -f "nginx master"
```

**Combine criteria carefully:**

``` bash
# This finds processes owned by root AND in session 1234
pgrep -u root -s 1234

# Comma-separated values create OR logic
pgrep -u root,daemon   # owned by root OR daemon
```

## Related Commands

- `ps(1)` – detailed process listing
- `kill(1)` – signal a process by PID
- `killall(1)` – similar to pkill but doesn’t support regex
- `systemctl(1)` – preferred for managing services on systemd systems

`pgrep` and `pkill` outperform grepping `ps` output because they’re atomic operations that avoid race conditions and handle edge cases properly. Use them consistently in scripts rather than shell pipelines for robustness.
