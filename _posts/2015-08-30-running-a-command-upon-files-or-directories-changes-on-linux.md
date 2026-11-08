---
title: "Monitor File Changes and Trigger Commands with inotifywait"
date: 2015-08-30 04:30:05 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/running-a-command-upon-files-or-directories-changes-on-linux/
---

Watching for filesystem changes and triggering actions is essential for development workflows—recompiling after source edits, restarting services when configs update, or running tests during coding. Linux’s inotify subsystem provides kernel-level file monitoring, and `inotifywait` makes it accessible from the command line.

## Installation

Install inotify-tools on your system:

**Fedora/RHEL/CentOS:**

``` bash
sudo dnf install inotify-tools
```

**Debian/Ubuntu:**

``` bash
sudo apt install inotify-tools
```

**Alpine:**

``` bash
apk add inotify-tools
```

## Basic Usage

The simplest approach is a shell loop that watches files and runs a command when changes occur:

``` bash
#!/bin/bash
COMMAND="$1"
shift
FILES="$@"

while true; do
  inotifywait -q -r -e modify,create,delete "$FILES"
  echo "Changes detected, running: $COMMAND"
  eval "$COMMAND"
  echo "Command completed"
done
```

Save as `watch-and-run.sh`, make it executable, then use it:

``` bash
chmod +x watch-and-run.sh

# Rebuild on C file changes
./watch-and-run.sh "make" src/*.c include/*.h Makefile

# Restart a service on config changes
./watch-and-run.sh "systemctl restart myservice" /etc/myapp/config.conf

# Run tests on Python file changes
./watch-and-run.sh "pytest" tests/ src/
```

## Preventing Overlapping Executions

If your command is slow and files change frequently, overlapping executions can cause problems. Add a lock mechanism to skip triggers while the command is still running:

``` bash
#!/bin/bash
COMMAND="$1"
shift
FILES="$@"
LOCKFILE="/tmp/watcher-lock-$$"

while true; do
  inotifywait -q -r -e modify,create,delete "$FILES"

  if [ -f "$LOCKFILE" ]; then
    echo "Command still running, skipping trigger"
    continue
  fi

  touch "$LOCKFILE"
  echo "Changes detected, running: $COMMAND"
  eval "$COMMAND"
  rm "$LOCKFILE"
  echo "Command completed"
done
```

This prevents resource contention and ensures each execution completes before the next triggers.

## Event Types and Filtering

`inotifywait` supports several event types. Choose what you actually need to monitor:

``` bash
# Only monitor file modifications (not creates/deletes)
inotifywait -e modify -r /path/to/watch

# Watch for close after write (better for buffered file operations)
inotifywait -e close_write -r /path/to/watch

# Exclude temporary files and version control
inotifywait -e modify --exclude '(\.git|\.swp|__pycache__|\.tmp)' -r /path/to/watch

# Watch multiple event types
inotifywait -e modify,create,delete -r /path/to/watch

# Exit after first event (don't loop)
inotifywait -e modify --format '%w' /path/to/watch
```

Using `close_write` is safer than `modify` for real-world scenarios, since editors buffer writes and you want to trigger only when files are truly written to disk.

## Real-World Examples

**Auto-rebuild and test on code changes:**

``` bash
#!/bin/bash
while true; do
  inotifywait -q -e close_write src/ tests/
  cargo build && cargo test
done
```

**Regenerate documentation on edits:**

``` bash
#!/bin/bash
while true; do
  inotifywait -q -e close_write docs/
  pandoc docs/*.md -o docs/output.html
done
```

**Validate and reload configuration:**

``` bash
#!/bin/bash
CONF="/etc/myapp/config.yaml"
while true; do
  inotifywait -q -e close_write "$CONF"
  if yamllint "$CONF"; then
    systemctl reload myapp
  else
    echo "Validation failed, not reloading"
  fi
done
```

**Auto-restart development server:**

``` bash
#!/bin/bash
PORT=8000
PIDFILE="/tmp/dev-server.pid"

restart_server() {
  if [ -f "$PIDFILE" ]; then
    kill $(cat "$PIDFILE") 2>/dev/null
    sleep 1
  fi
  python3 -m uvicorn app:app --port $PORT &
  echo $! > "$PIDFILE"
}

restart_server

while true; do
  inotifywait -q -e close_write -r app/ --exclude '(__pycache__|\.pyc|\.egg-info)'
  echo "Changes detected, restarting..."
  restart_server
done
```

## Running as a systemd Service

For persistent monitoring, run the watcher as a systemd service:

``` ini
# /etc/systemd/system/myapp-watcher.service
[Unit]
Description=Watch and rebuild MyApp
After=network.target

[Service]
Type=simple
User=appuser
WorkingDirectory=/home/appuser/myapp
ExecStart=/home/appuser/myapp/watch-and-run.sh "make" src/
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start it:

``` bash
sudo systemctl enable myapp-watcher
sudo systemctl start myapp-watcher
sudo systemctl status myapp-watcher
```

View logs with `journalctl -u myapp-watcher -f`.

## Performance Tuning

**Recursive watching depth:** Use `-r` sparingly on large directory trees. Specify exact paths when possible:

``` bash
# Good: narrow scope
inotifywait -e close_write src/ tests/ docs/

# Avoid: too broad on large codebases
inotifywait -e close_write -r /home/user/
```

**System limits:** Check your inotify watch limit:

``` bash
cat /proc/sys/fs/inotify/max_user_watches
```

If monitoring many files, increase it:

``` bash
echo 524288 | sudo tee /proc/sys/fs/inotify/max_user_watches
```

Make it persistent in `/etc/sysctl.d/99-inotify.conf`:

    fs.inotify.max_user_watches=524288

**Bulk operations:** Rapid successive changes (like git checkouts or build output) can queue multiple executions. The locking pattern shown earlier handles this, or use the `--format` option to batch output:

``` bash
inotifywait -q -r -e close_write --format '%w' /path | while read file; do
  # Process batched changes here
done
```

## Alternatives

For complex scenarios, consider these specialized tools:

- **entr** — Simpler syntax, better for one-off automation
- **watchexec** — Rust-based, built-in debouncing and process management
- **nodemon** — Originally for Node.js but works for any language, includes file exclusion patterns
- **systemd path units** — Native integration without external tools

These handle rapid successive changes and edge cases more elegantly, though `inotifywait` is sufficient for most use cases and requires no additional dependencies beyond inotify-tools.
