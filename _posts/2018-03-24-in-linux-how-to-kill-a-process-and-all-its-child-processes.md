---
title: "Terminating a Bash Script and Its Child Processes in Linux"
date: 2018-03-24 11:53:20 +0000
layout: post
canonical: https://www.systutorials.com/in-linux-how-to-kill-a-process-and-all-its-child-processes/
---

When a Bash script spawns child processes—say script A starts B, which starts C, which runs rsync—you need a way to terminate the entire process tree cleanly. Simply killing the parent leaves orphaned children running in the background.

The most reliable approach uses session IDs (SID). By default, child processes inherit the same session ID as the parent script. You can leverage this to identify and terminate the entire process group at once.

## Finding All Child Processes by Session ID

First, determine what processes belong to your script’s session:

``` bash
ps -s $$ -o pid=
```

This returns all process IDs in the session where `$$` is your script’s process ID. The `-s` flag filters by session ID, and `-o pid=` outputs only the PID column without the header.

You can also use `pgrp` to see the process group, or combine with other columns for more detail:

``` bash
ps -s $$ -o pid,ppid,cmd
```

## Killing the Entire Process Tree

To terminate all processes in the session (the script and all children):

``` bash
kill $(ps -s $$ -o pid=)
```

This expands to a list of PIDs and sends SIGTERM to each. If processes don’t respond to SIGTERM after a reasonable wait, force them:

``` bash
kill -9 $(ps -s $$ -o pid=)
```

## Practical Example in a Script

``` bash
#!/bin/bash

cleanup() {
    echo "Terminating all child processes..."
    kill $(ps -s $$ -o pid=) 2>/dev/null
}

trap cleanup EXIT INT TERM

# Start background jobs
long_running_command &
another_process &

# Do work
sleep 100
```

When the script exits or receives SIGINT/SIGTERM, the trap calls `cleanup()`, which terminates everything in the session. The `2>/dev/null` suppresses error messages if no child processes exist.

## Alternative Approaches

**Using process groups (recommended for modern scripts):**

Instead of relying on session IDs, explicitly manage process groups:

``` bash
#!/bin/bash

# Start processes in a subshell as a new process group
{
    command1 &
    command2 &
    wait
} &

PID=$!

# Later, kill the entire group
kill -TERM -$PID  # Negative PID targets the process group
```

**Using `pkill` with parent process:**

``` bash
pkill -P $$ -TERM
```

This kills direct children only (not grandchildren). For full tree termination, repeat or use a loop:

``` bash
while pgrep -P $$ > /dev/null; do
    pkill -P $$
    sleep 0.1
done
```

**Using `killall` (less reliable, matches by name):**

``` bash
killall rsync
```

This is dangerous because it kills all processes with that name system-wide, not just children of your script.

## Important Considerations

- **Signal handling**: SIGTERM (`kill -TERM`) allows processes to clean up. SIGKILL (`kill -9`) forces immediate termination but risks data loss.
- **Orphaned processes**: If a child forks before you kill the parent, grandchildren may become orphaned and attach to init/systemd. The session ID approach avoids this.
- **Shell vs. subshells**: Session IDs work across shell boundaries, making them more reliable than process group IDs for complex script hierarchies.
- **Timing**: Kill sends signals but doesn’t wait. Add a brief sleep before escalating to SIGKILL if needed:

``` bash
kill $(ps -s $$ -o pid=)
sleep 2
kill -9 $(ps -s $$ -o pid=) 2>/dev/null
```

For production scripts managing long-running processes, combine session-based killing with explicit traps and logging to ensure clean shutdown.
