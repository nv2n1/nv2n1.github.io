---
title: "How to Change Systemd Targets on Fedora Linux"
date: 2013-07-12 16:32:32 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/changing-systemd-runlevel-on-fedora-linux/
---

Fedora switched to systemd for service management years ago, replacing the traditional `/etc/inittab` file with a target-based system. While `systemctl set-default` is the standard approach, understanding the manual method gives you insight into how systemd actually manages boot targets.

## Systemd Targets vs. Legacy Runlevels

Systemd uses **targets** instead of runlevels. The two primary targets you’ll work with are:

- `multi-user.target` — equivalent to runlevel 3 (multi-user, text mode, no GUI)
- `graphical.target` — equivalent to runlevel 5 (multi-user with graphical interface)

The system maintains a symlink at `/etc/systemd/system/default.target` that points to whichever target should load at boot.

## Manual Target Switching

To manually change the default boot target, create or update the symlink in `/etc/systemd/system/`:

``` bash
sudo ln -sf /usr/lib/systemd/system/multi-user.target /etc/systemd/system/default.target
```

The `-f` flag overwrites any existing symlink without requiring a separate `rm` command. Note that on modern Fedora/RHEL systems, the systemd unit files are typically in `/usr/lib/systemd/system/` rather than `/lib/systemd/system/` (though the latter may exist as a compatibility link).

To switch to graphical mode:

``` bash
sudo ln -sf /usr/lib/systemd/system/graphical.target /etc/systemd/system/default.target
```

Verify the change with:

``` bash
ls -l /etc/systemd/system/default.target
```

The symlink takes effect on the next boot. If you want to change targets immediately without rebooting, use:

``` bash
sudo systemctl isolate multi-user.target
sudo systemctl isolate graphical.target
```

The `isolate` command switches to the specified target and stops services not required by it.

## Checking Current Target

To see which target is currently set as default:

``` bash
systemctl get-default
```

To check the active target right now:

``` bash
systemctl list-units --type=target --active
```

## Practical Use Cases

**Disable GUI on a desktop system:** If you installed Fedora with GNOME but need headless operation or want to troubleshoot without the display manager running:

``` bash
sudo ln -sf /usr/lib/systemd/system/multi-user.target /etc/systemd/system/default.target
sudo reboot
```

**Emergency recovery:** If the graphical environment fails to start, drop to multi-user target to diagnose the issue:

``` bash
sudo systemctl isolate multi-user.target
```

**Server configuration:** Most Fedora/RHEL servers run in multi-user mode to avoid unnecessary resource consumption.

## Why Manual Symlinks Matter

While `systemctl set-default` is the recommended method for regular use, the manual symlink approach is useful when:

- Scripting automated deployments where you need explicit control
- Troubleshooting systemd issues
- Understanding how the boot system actually works
- Environments where systemctl might not be available

The symlink-based approach is also completely compatible with systemctl’s management tools — they both read and write the same default.target link.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
