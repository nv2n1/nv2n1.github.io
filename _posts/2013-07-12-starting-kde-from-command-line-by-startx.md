---
title: "Starting KDE Desktop from the Command Line with startx"
date: 2013-07-12 16:32:11 +0000
layout: post
canonical: https://www.systutorials.com/starting-kde-from-command-line-by-startx/
---

If you prefer booting to a minimal environment and starting your desktop manually, you can configure `startx` to launch KDE Plasma instead of your default desktop environment.

### Understanding startx and Desktop Selection

The `startx` command reads configuration files to determine which desktop environment to start. On systemd-based distributions (Fedora, RHEL, Arch), the startup chain typically works through `~/.xinitrc` or system-wide xinit scripts that check environment variables to decide which desktop to load.

Rather than relying on a display manager like GDM or SDDM, you’re booting to runlevel 3 (multi-user, no GUI) and starting X manually. This gives you control over when and how the display server starts.

### Fedora and RHEL Approach

On Fedora and RHEL systems, the startup process checks `/etc/sysconfig/desktop` for the `DESKTOP` variable. If this file doesn’t exist, create it:

``` bash
sudo nano /etc/sysconfig/desktop
```

Add or modify the line to specify KDE:

    DESKTOP="KDE"

If you want to set a specific display manager (though this mainly matters when using a DM), you can also add:

    DISPLAYMANAGER="KDE"

After saving, run `startx` from a TTY and KDE Plasma should launch.

### User-Level Configuration with ~/.xinitrc

For more granular control, create or edit `~/.xinitrc` in your home directory:

``` bash
nano ~/.xinitrc
```

Add one of these lines at the end (before `exec` calls):

For KDE Plasma 5/6:

``` bash
exec startplasma-x11
```

For older KDE:

``` bash
exec startkde
```

A complete minimal `~/.xinitrc` might look like:

``` bash
#!/bin/bash

# Load system-wide X settings
if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
    [ -x "$f" ] && . "$f"
  done
fi

# Start KDE Plasma
exec startplasma-x11
```

Make it executable:

``` bash
chmod +x ~/.xinitrc
```

Now running `startx` will launch your KDE session.

### Arch Linux and Derivatives

On Arch, `startx` reads `~/.xinitrc` directly. Create the file as shown above with `exec startplasma-x11` and you’re set.

### Selecting Desktop Environment at Runtime

If you have multiple desktop environments installed and want to choose at runtime, modify `~/.xinitrc`:

``` bash
#!/bin/bash

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/?*.sh; do
    [ -x "$f" ] && . "$f"
  done
fi

case "${1}" in
  kde)
    exec startplasma-x11
    ;;
  gnome)
    exec gnome-session
    ;;
  xfce)
    exec startxfce4
    ;;
  *)
    exec startplasma-x11
    ;;
esac
```

Then start KDE with:

``` bash
startx -- kde
```

Or GNOME with:

``` bash
startx -- gnome
```

### Troubleshooting

If `startx` fails to launch KDE, check:

- The `startplasma-x11` binary exists: `which startplasma-x11`
- Your `~/.xinitrc` has proper permissions and syntax
- X server logs: `cat ~/.local/share/xorg/Xorg.0.log` or `/var/log/Xorg.0.log`
- Ensure KDE Plasma is actually installed: `pacman -Q plasma-desktop` (Arch) or `dnf list installed | grep plasma` (Fedora)

### Modern Considerations

If you’re using Wayland-based KDE sessions (Plasma 5.24+), use `startplasma-wayland` instead. Check available sessions in `/usr/share/xsessions/` to see what your system supports. For most current setups, `startplasma-x11` remains the standard X11 session starter.

## 2026 Best Practices and Advanced Techniques

For Starting KDE Desktop from the Command Line with startx, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
