---
title: "Switching Display Managers on Fedora Linux"
date: 2018-03-24 11:47:31 +0000
layout: post
canonical: https://www.systutorials.com/how-to-change-the-display-manager-on-fedora-linux/
---

The default display manager on Fedora is GNOME Display Manager (GDM). If you want to switch to another display manager like KDE Plasma (SDDM), LightDM, or another option, you need a reliable method that won’t break your system.

## Using system-switch-displaymanager

The most straightforward approach is the `system-switch-displaymanager` utility, which handles the systemd configuration for you.

First, install the tool along with the package for your target display manager. For example, to switch to KDE Plasma:

``` bash
sudo dnf install system-switch-displaymanager sddm
```

Or for LightDM:

``` bash
sudo dnf install system-switch-displaymanager lightdm
```

Then run the switch command:

``` bash
sudo system-switch-displaymanager
```

This will present an interactive menu showing available display managers. Select your choice and confirm. The tool updates the necessary systemd symlinks automatically.

After switching, log out completely (or restart for safety) to load the new display manager. You don’t need to restart the X server — just exit your current session.

## Manual method: Using systemd

If `system-switch-displaymanager` isn’t available or you prefer manual control, you can manage the display manager through systemd directly.

First, check what’s currently active:

``` bash
sudo systemctl status display-manager.service
```

To see available display manager services:

``` bash
ls /etc/systemd/system/display-manager.service*
systemctl list-unit-files | grep -E '(gdm|sddm|lightdm|lxdm)'
```

To switch manually, create a symlink pointing to your chosen display manager’s service:

``` bash
sudo systemctl disable gdm.service
sudo systemctl enable sddm.service
sudo systemctl set-default graphical.target
```

Then restart the display manager or reboot:

``` bash
sudo systemctl restart display-manager.service
```

Or for a full reboot:

``` bash
sudo systemctl reboot
```

## Common display managers available on Fedora

- **SDDM** (KDE Plasma) — lightweight, modern, highly configurable
- **LightDM** — minimal, compositable, used by XFCE and LXDE
- **GDM** (GNOME) — feature-rich, wayland-native, default on Fedora
- **LXDM** — very lightweight, good for older hardware

## Troubleshooting

If you break something during the switch, boot into a TTY (Ctrl+Alt+F2) and reinstall or reconfigure manually:

``` bash
sudo dnf install gdm
sudo systemctl enable gdm.service
sudo systemctl set-default graphical.target
sudo reboot
```

To verify which display manager service file is active:

``` bash
ls -l /etc/systemd/system/display-manager.service
```

This shows the symlink target and confirms what’s configured.

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

For Switching Display Managers on Fedora Linux, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
