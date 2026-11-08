---
title: "Disabling systemd Core Dumps on Linux"
date: 2018-03-24 11:46:14 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-disable-the-coredump-function-of-systemd-on-linux/
---

\[md\]\
Systemd’s coredump handler captures process crash dumps by default, which can consume significant disk space on development or test systems. Here’s how to disable or control coredump storage.

\## Quick Solution

Edit `/etc/systemd/coredump.conf` and set:

```wp-block-code
[Coredump]
Storage=none
```

Then reload the systemd daemon:

```wp-block-code
systemctl daemon-reload
```

This prevents coredumps from being stored permanently while still logging crash events.

\## Understanding Storage Options

The `Storage=` directive in `coredump.conf` controls where crashes are saved:

– `none` — Logs crashes but discards dumps immediately\
– `external` — Stores dumps in `/var/lib/systemd/coredump/` (default)\
– `journal` — Stores dumps in the systemd journal with rotation\
– `both` — Stores in both external storage and journal

Other useful directives:

– `Compress=yes` — Compress stored coredumps (default on most distributions)\
– `ProcessSizeMax=2G` — Maximum size of core dumps to process\
– `MaxUse=` — Maximum disk space for stored dumps\
– `KeepFree=` — Minimum free disk space to maintain

\## Common Scenarios

\*\*Development machine with limited disk space:\*\*

```wp-block-code
Storage=none
```

\*\*Keep crash logs but limit disk usage:\*\*

```wp-block-code
Storage=journal
MaxUse=500M
```

\*\*Production system needing crash analysis:\*\*

```wp-block-code
Storage=external
MaxUse=2G
Compress=yes
```

\## Verify the Configuration

Check your current settings:

```wp-block-code
cat /etc/systemd/coredump.conf | grep -E '^[^#]'
```

List existing coredumps:

```wp-block-code
coredumpctl list
```

Show details of the most recent crash:

```wp-block-code
coredumpctl info
```

Extract a specific coredump for debugging:

```wp-block-code
coredumpctl dump PID -o core.dump
```

\## Clearing Existing Coredumps

If you’ve disabled storage but have accumulated dumps:

```wp-block-code
# Remove all stored coredumps
coredumpctl empty-journal

# Or manually clean the directory
sudo rm -rf /var/lib/systemd/coredump/*
sudo systemctl restart systemd-coredump.socket
```

Check how much space coredumps are using:

```wp-block-code
du -sh /var/lib/systemd/coredump/
journalctl --disk-usage | grep coredump
```

\## System-Wide vs Per-Service Control

You can also limit coredumps per service using systemd unit files. Add to the service file or a drop-in override:

```wp-block-code
[Service]
LimitCORE=0
```

This overrides global settings for that specific service. To apply without editing the unit file directly:

```wp-block-code
sudo systemctl edit servicename
```

Then add:

```wp-block-code
[Service]
LimitCORE=0
```

For containers, use `--ulimit core=0` with podman or docker to disable coredumps inside the container.

\## Kernel-Level Core Dump Control

In addition to systemd’s configuration, the kernel has its own core dump settings:

```wp-block-code
# Check current kernel setting
cat /proc/sys/kernel/core_pattern

# Disable core dumps entirely at kernel level
sudo sysctl -w kernel.core_pattern=|/bin/false

# Make it persistent
echo "kernel.core_pattern=|/bin/false" | sudo tee -a /etc/sysctl.d/99-no-coredump.conf
```

When systemd-coredump is active, `core_pattern` is typically set to pipe dumps to `/usr/lib/systemd/systemd-coredump`.

\## Analyzing Coredumps When You Need Them

If you keep coredump storage enabled for debugging, here’s how to work with them:

\*\*Debug a crash with GDB:\*\*

```wp-block-code
# Find the crashed process
coredumpctl list | tail -5

# Open in GDB with the binary
coredumpctl debug PID

# Or extract and debug manually
coredumpctl dump PID -o /tmp/core
gdb /path/to/binary /tmp/core
```

\*\*Get a backtrace from a coredump:\*\*

```wp-block-code
coredumpctl gdb PID -ex "bt full" -ex "quit"
```

\*\*Check what signal caused the crash:\*\*

```wp-block-code
coredumpctl info PID | grep -i signal
```

\## Verify Changes Take Effect

After modifying coredump.conf, reload the daemon and test:

```wp-block-code
systemctl daemon-reload
systemctl restart systemd-coredump.socket
```

Trigger a test crash (on a non-production system):

```wp-block-code
bash -c '$(dd if=/dev/zero bs=1 count=1)'
```

Check if the crash was logged:

```wp-block-code
journalctl -xe | grep -i coredump
```

With `Storage=none`, you should see the crash logged but no dump file created in `/var/lib/systemd/coredump/`.
