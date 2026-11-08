---
title: "Disable Auto-Mounting in Linux Mint Cinnamon"
date: 2018-03-24 11:44:26 +0000
layout: post
canonical: https://www.systutorials.com/how-to-disable-auto-mounting-on-linux-mint-cinnamon/
---

Linux Mint’s Cinnamon desktop automatically mounts removable media like USB drives and external hard drives by default. If you prefer manual control over when and how storage devices are mounted, you can disable this behavior through Nemo, the Cinnamon file manager.

## Disable Auto-Mounting via Nemo Preferences

The simplest approach is to configure Nemo’s mounting behavior directly:

1.  Open **Nemo** (the file manager)
2.  Click **Edit** in the menu bar
3.  Select **Preferences**
4.  Navigate to the **Behavior** tab
5.  Look for the **“Automatically mount removable media”** option and uncheck it
6.  Also uncheck **“Automatically open a folder when media is inserted”** if you want to prevent automatic folder windows from opening
7.  Close the preferences window

After this change, USB drives and other removable media will no longer mount automatically when connected. You’ll need to right-click the device in Nemo’s sidebar and select **“Mount”** when you want to access it.

## Alternative: Disable via systemd and udisks

For a system-wide approach that affects all applications (not just Nemo), you can configure udisks2, which handles device mounting at the system level:

Edit or create `/etc/udisks2/udisks2.conf`:

``` ini
[defaults]
# Set to true to disable auto-mounting
NoUserInteraction=false
AutoMount=false
```

After editing, restart the udisks2 daemon:

``` bash
sudo systemctl restart udisks2
```

This method persists across desktop environment changes and affects mounting behavior system-wide.

## Verify the Changes

To confirm auto-mounting is disabled, connect a USB drive and verify it doesn’t appear in Nemo’s sidebar or doesn’t automatically mount. You can check mount status manually:

``` bash
lsblk
```

This command shows all block devices and their mount points. If your USB drive appears in the list but has no mount point, auto-mounting is successfully disabled.

## Re-enable Auto-Mounting

To restore the default behavior, simply reverse these steps:

- In Nemo: Edit → Preferences → Behavior → check “Automatically mount removable media” again
- Via systemd: Set `AutoMount=true` in `/etc/udisks2/udisks2.conf` and restart udisks2

Note that if you’re using other file managers like Nautilus (GNOME Files) or Dolphin (KDE), they have their own auto-mount settings in their respective preferences dialogs.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Disable Auto-Mounting in Linux Mint Cinnamon, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
