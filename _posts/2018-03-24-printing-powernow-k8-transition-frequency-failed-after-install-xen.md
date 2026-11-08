---
title: "Fix PowerNow-k8 Frequency Scaling Errors on Xen"
date: 2018-03-24 11:46:57 +0000
modified: 2026-04-12 16:11:29 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /printing-powernow-k8-transition-frequency-failed-after-install-xen/
---

After installing Xen on AMD systems, you may see continuous “powernow-k8 transition frequency failed” messages on the console. This happens because the `powernow_k8` driver (AMD CPU power management) is incompatible with Xen’s CPU handling and tries to manage frequencies that Xen controls.

## Quick Fix

The simplest solution is to unload the conflicting module:

``` bash
sudo rmmod powernow_k8
```

This stops the error messages immediately, but the change won’t persist after a reboot.

## Persistent Solution Using Kernel Parameters

The most reliable approach is to blacklist the module at boot time. Edit or create `/etc/modprobe.d/blacklist-powernow.conf`:

``` bash
sudo nano /etc/modprobe.d/blacklist-powernow.conf
```

Add this line:

    blacklist powernow_k8

Then rebuild your initramfs and reboot:

``` bash
sudo update-initramfs -u
sudo reboot
```

This prevents the module from loading at all, eliminating the error messages without needing startup scripts.

## Alternative: Using rc.local (Legacy Approach)

If you prefer to unload the module during boot rather than blacklist it, you can use `/etc/rc.local`. Note that `rc.local` is deprecated on systemd systems but still supported for backward compatibility.

Create or edit `/etc/rc.local`:

``` bash
sudo nano /etc/rc.local
```

Add this before the `exit 0` line:

``` bash
rmmod powernow_k8 2>/dev/null || true
```

The `2>/dev/null || true` ensures the script doesn’t fail if the module isn’t loaded. Make the file executable:

``` bash
sudo chmod +x /etc/rc.local
```

Enable the service on boot:

``` bash
sudo systemctl enable rc-local.service
```

## Modern Approach: Systemd Service

For a cleaner solution on modern systems, create a dedicated systemd service. Create `/etc/systemd/system/disable-powernow.service`:

``` ini
[Unit]
Description=Disable powernow_k8 module for Xen
After=network.target

[Service]
Type=oneshot
ExecStart=/sbin/rmmod powernow_k8
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable and start it:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable disable-powernow.service
sudo systemctl start disable-powernow.service
```

## Verification

Check that the module is no longer loaded:

``` bash
lsmod | grep powernow
```

No output means it’s successfully unloaded. Verify your Xen instance still manages CPU frequency correctly using `xl info` or your monitoring tools.

## Why This Happens

Xen controls CPU frequency scaling directly through ACPI cpufreq drivers. The legacy `powernow_k8` driver attempts to manage the same resources, causing conflicts. Newer AMD systems should use the `amd-pstate` driver instead, which is Xen-aware, but older systems need the module disabled entirely.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
