---
title: "Fix \u201csulogin: can not open password database\u201d on Linux"
date: 2018-03-24 11:49:47 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/linux-boots-failed-with-sulogin-can-not-open-password-database-while-the-etc-passwd-and-etc-shadow-files-look-fine/
---

When Linux fails to boot with the error message “sulogin: can not open password database” despite `/etc/passwd` and `/etc/shadow` appearing intact, SELinux is often the culprit. The files exist and have correct content, but SELinux context labels are missing or corrupted, preventing the login process from reading them.

## Diagnose the Problem

Boot into the initramfs emergency shell to confirm the issue. The error typically occurs during the early boot phase when systemd tries to spawn the sulogin session. You’ll see the error repeatedly without getting a login prompt.

## Solution: Boot into Read-Write Mode and Fix SELinux

**Step 1: Reboot with read-write root and shell access**

Reboot your system and interrupt the GRUB menu (press `e` on the boot entry). Find the `linux` line and append:

    rw init=/bin/bash

This boots directly to a bash shell with a read-write root filesystem, bypassing normal SELinux policy enforcement.

**Step 2: Disable SELinux temporarily**

Once at the shell prompt, run:

``` bash
setenforce 0
```

This sets SELinux to permissive mode, allowing the system to boot normally.

**Step 3: Reboot normally**

``` bash
reboot
```

If the system boots successfully, the issue is confirmed as SELinux context corruption.

## Permanent Fix: Restore SELinux Contexts

Once logged in normally, restore the correct SELinux contexts on authentication files:

``` bash
sudo restorecon -v /etc/passwd /etc/shadow /etc/group /etc/gshadow
```

For a more thorough fix across the entire system:

``` bash
sudo restorecon -Rv /etc
```

If you need to relabel the entire filesystem:

``` bash
sudo touch /.autorelabel
sudo reboot
```

This creates a flag that triggers a full SELinux relabel on the next boot. On modern systems, this can take 10-30 minutes depending on disk size.

## Verify SELinux is Enforcing Again

After the system boots and relabels (if you used `.autorelabel`), confirm SELinux is back in enforcing mode:

``` bash
getenforce
```

Should return `Enforcing`. If you manually set it to permissive, re-enable it:

``` bash
sudo setenforce 1
```

## Check for Filesystem Issues

If relabeling doesn’t resolve the problem, verify the filesystem itself:

``` bash
sudo fsck -n /
```

(The `-n` flag does a read-only check without modifications. Remove `-n` to actually repair if needed, but only on unmounted filesystems.)

## Prevention

SELinux context corruption often occurs from:

- Incomplete package updates
- Filesystem errors during shutdown
- Direct file modifications that bypass SELinux context tools
- Disk failures

Keep your system updated and always use proper shutdown procedures:

``` bash
sudo dnf update -y
sudo systemctl reboot
```

Avoid force-killing the system or hard power cycles when possible.

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
