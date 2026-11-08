---
title: "Libvirt Crash After Upgrading to Version 2.5.0"
date: 2018-03-24 11:51:39 +0000
author: "Weiwei Jia"
layout: post
canonical: https://www.systutorials.com/libvirt-crash-when-upgrade-from-version-1-2-2-to-version-2-5-0/
---

When upgrading libvirt from an older version (like 1.2.2) to 2.5.0 or later, you may encounter a socket connection error when trying to create VMs:

    ERROR    Failed to connect socket to '/var/run/libvirt/virtlogd-sock': No such file or directory
    Domain installation does not appear to have been successful.

This happens because libvirt 2.5.0 introduced the `virtlogd` daemon for centralized VM logging, but it doesn’t start automatically after a fresh installation or upgrade.

## Root Cause

The `virtlogd` service manages logging for all libvirt domains. When you restart `libvirtd` after upgrading, the main daemon starts but `virtlogd` doesn’t launch automatically, leaving the socket missing.

## Solution

Start `virtlogd` manually:

``` bash
/usr/sbin/virtlogd
```

For persistent startup, run it as a daemon:

``` bash
virtlogd -d
```

However, relying on manual startup isn’t ideal. Use your system’s service manager instead.

## Permanent Fix with systemd

On modern systems using systemd, enable `virtlogd` to start automatically:

``` bash
sudo systemctl enable virtlogd
sudo systemctl start virtlogd
sudo systemctl restart libvirtd
```

Verify both services are running:

``` bash
sudo systemctl status virtlogd
sudo systemctl status libvirtd
```

## For Older Init Systems

If you’re using sysvinit (less common in 2026, but still relevant for older deployments), create an init script or add `virtlogd` to your startup sequence before `libvirtd`:

``` bash
/usr/sbin/virtlogd -d
service libvirt-bin restart
```

## Avoiding This on Fresh Installations

When building from source, the modern way is to use systemd units:

``` bash
./configure --prefix=/usr --with-systemd-units
make
sudo make install
sudo systemctl daemon-reload
sudo systemctl enable virtlogd libvirtd
sudo systemctl start virtlogd libvirtd
```

This ensures proper dependency ordering — `libvirtd` will wait for `virtlogd` to be ready before initializing.

## Debugging Connection Issues

If you still see connection errors after starting `virtlogd`, check:

``` bash
# Verify the socket exists
ls -la /var/run/libvirt/virtlogd-sock

# Check libvirtd logs
journalctl -xe -u libvirtd

# Verify virtlogd is listening
ps aux | grep virtlogd
```

If the socket still doesn’t exist, `virtlogd` may be failing to start. Check its logs:

``` bash
journalctl -xe -u virtlogd
```

Common causes include permission issues or a corrupted libvirt installation. In those cases, reinstalling from your package manager is faster than troubleshooting the source build.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
