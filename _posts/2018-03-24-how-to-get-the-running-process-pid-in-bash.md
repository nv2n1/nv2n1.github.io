---
title: "Getting a Process PID in Bash"
date: 2018-03-24 11:52:47 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-get-the-running-process-pid-in-bash/
---

Every shell script runs as a process with a unique ID (PID). You need this ID for process management, logging, temporary file naming, and cleanup operations.

## The \$\$ variable

The special variable `$$` expands to the PID of the current shell process:

``` bash
echo $$
```

This returns a single integer — the PID of your current Bash instance. Use it in scripts to identify which process is running:

``` bash
#!/bin/bash
LOGFILE="/var/log/myscript_$$.log"
echo "Script started with PID $$" | tee "$LOGFILE"
```

## The \$! variable for background processes

When you launch a command in the background, `$!` gives you the PID of that last backgrounded process:

``` bash
long_running_job &
BG_PID=$!
echo "Started background job with PID $BG_PID"
```

This is critical for managing child processes. You can wait for it to complete:

``` bash
sleep 300 &
BG_PID=$!
wait $BG_PID
echo "Background job $BG_PID finished"
```

## Practical use cases

**Temporary files with PID naming:**

``` bash
TMPDIR="/tmp/myapp_$$"
mkdir -p "$TMPDIR"
trap "rm -rf $TMPDIR" EXIT
```

This ensures each script instance gets its own isolated temporary directory that cleans up automatically when the script exits.

**Process tracking and cleanup:**

``` bash
#!/bin/bash
PID_FILE="/var/run/myservice_$$.pid"
echo $$ > "$PID_FILE"

# Your service runs here
sleep 1000 &
SERVICE_PID=$!

# Cleanup on exit
trap "kill $SERVICE_PID 2>/dev/null; rm -f $PID_FILE" EXIT INT TERM
wait $SERVICE_PID
```

**Logging with context:**

``` bash
declare -A pids
for item in "${items[@]}"; do
    process_item "$item" &
    pids["$item"]=$!
done

for item in "${!pids[@]}"; do
    if wait "${pids[$item]}" 2>/dev/null; then
        echo "✓ $item completed"
    else
        echo "✗ $item failed"
    fi
done
```

## Related process variables

- `$PPID` — the parent process ID (the PID of the shell that launched your script)
- `$BASHPID` — the PID of the current Bash shell (differs from `$$` in subshells)

In subshells, `$$` may return the parent’s PID, but `$BASHPID` always gives the actual subshell’s PID:

``` bash
bash -c 'echo "PID: $$, BASHPID: $BASHPID"'
# Output: PID: 12345, BASHPID: 12345 (in this case, same)

(echo "Subshell PID: $$, BASHPID: $BASHPID")
# $$ shows parent, $BASHPID shows actual subshell PID
```

## Important notes

- PIDs are only guaranteed unique at any given moment, not across system lifetime
- For daemonized processes, always use PID files in `/var/run` or `/run` (not `/tmp`, which gets cleaned)
- When backgrounding multiple processes in a loop, save each `$!` immediately before launching the next one
- Always include proper signal handlers (`trap`) when managing child processes to ensure cleanup on script exit or interruption

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
