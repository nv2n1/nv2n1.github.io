---
title: "Enable rpcbind.service to Auto-Start with systemd"
date: 2018-03-24 11:50:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-the-rpcbind-service-auto-start-in-systemd-on-linux/
---

The standard `systemctl enable` command should work for rpcbind.service, but if you’re seeing it fail to start after reboot, there are several approaches to troubleshoot and fix the issue.

## Check the Current State

First, verify the actual status:

``` bash
systemctl status rpcbind.service
systemctl is-enabled rpcbind.service
```

If `is-enabled` returns `disabled`, the service wasn’t properly enabled. Check for any error messages in the status output.

## Enable the Service

The standard way to enable autostart is:

``` bash
systemctl enable rpcbind.service
```

This creates a symbolic link in `/etc/systemd/system/multi-user.target.wants/` pointing to the unit file. After enabling, verify it worked:

``` bash
systemctl start rpcbind.service
systemctl status rpcbind.service
```

## Force Dependencies with add-wants

If `systemctl enable` doesn’t work or the service has dependency issues, you can explicitly add it as a “wanted” dependency to multi-user.target:

``` bash
systemctl add-wants multi-user.target rpcbind.service
```

This is more forceful than `enable` — it creates the symlink even if the unit file has conditions or other restrictions that might prevent normal enablement. Check what was created:

``` bash
ls -la /etc/systemd/system/multi-user.target.wants/ | grep rpcbind
```

## Common Reasons rpcbind Fails to Start

Even with enablement, rpcbind may not start on boot due to:

- **Conditional activation**: Check the unit file for `ConditionVirtualization`, `ConditionFileExists`, or similar directives that might prevent startup.

``` bash
systemctl cat rpcbind.service | grep -i condition
```

- **Missing dependencies**: rpcbind requires specific kernel modules or network interfaces. Verify prerequisites are available:

``` bash
modprobe sunrpc
```

- **Socket activation**: Some systems use socket-based activation instead. Check:

``` bash
systemctl list-unit-files | grep rpcbind
```

If you see `rpcbind.socket`, the service activates on-demand rather than at boot.

## Reload and Verify

After making changes, reload the systemd daemon:

``` bash
systemctl daemon-reload
systemctl enable rpcbind.service
systemctl start rpcbind.service
```

Check the journal for detailed error messages:

``` bash
journalctl -u rpcbind.service -n 50
```

## Persistent Configuration

To ensure the setting survives package updates, create a drop-in override:

``` bash
systemctl edit rpcbind.service
```

Add this to prevent conditional execution:

``` ini
[Unit]
ConditionVirtualization=

[Service]
Type=simple
```

Save and exit — the file is written to `/etc/systemd/system/rpcbind.service.d/override.conf`. Reload and test:

``` bash
systemctl daemon-reload
systemctl enable rpcbind.service
systemctl start rpcbind.service
```

Use `systemctl add-wants` only as a last resort when `enable` genuinely fails. In most cases, investigating why the service has blocking conditions or dependencies is the proper fix.

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
