---
title: "Setting MATE as Your Default Desktop Environment on Fedora"
date: 2013-07-12 16:32:32 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/setting-mate-as-default-desktop-environment-for-startx-on-fedora/
---

The `startx` command launches an X session without a display manager, reading configuration from `$HOME/.xinitrc`. By default, this file doesn’t exist—startx falls back to system defaults that typically only recognize GNOME or KDE. If you’ve installed MATE and want to use it with `startx`, you need to create a user-level configuration.

## Understanding startx Initialization

When you run `startx`, it sources the startup script chain in this order:

1.  `$HOME/.xinitrc` (user configuration)
2.  `/etc/X11/xinit/xinitrc` (system fallback)
3.  Desktop session managers referenced within those files

The startx script explicitly checks for a user-level xinitrc first. If it exists, startx uses that instead of searching for detected sessions in `/usr/share/xsessions/`.

## Creating Your .xinitrc for MATE

Create `$HOME/.xinitrc` with the following content:

``` bash
exec mate-session
```

Set proper permissions:

``` bash
chmod +x $HOME/.xinitrc
```

That’s sufficient. When you run `startx`, it will execute `mate-session`, which handles all window manager and session initialization.

## Booting to Virtual Console

If you’re running Fedora without a display manager:

``` bash
systemctl set-default multi-user.target
systemctl reboot
```

Log in at the console and run:

``` bash
startx
```

MATE should start. If it doesn’t, verify the session is installed:

``` bash
which mate-session
```

Should output `/usr/bin/mate-session` or similar.

## Advanced Configuration

For more control, source system defaults before launching the session:

``` bash
# $HOME/.xinitrc
[ -f /etc/X11/xinit/xinitrc.d/00-xhost ] && source /etc/X11/xinit/xinitrc.d/00-xhost
[ -f /etc/X11/xinit/xinitrc.d/50-systemd-user ] && source /etc/X11/xinit/xinitrc.d/50-systemd-user

exec mate-session
```

This ensures systemd user session integration and proper X11 access control.

## Using systemd-user with startx

Modern Fedora integrates systemd user sessions with X11. Ensure the socket is available:

``` bash
systemctl --user status podman.socket
```

If you need specific environment variables or services, add them before the exec:

``` bash
export QT_QPA_PLATFORMTHEME=mate
export GTK_MODULES=canberra-gtk-module

exec mate-session
```

## Switching Back to a Display Manager

If you later want to use SDDM or GDM instead:

``` bash
systemctl set-default graphical.target
systemctl reboot
```

The display manager will auto-select available sessions from `/usr/share/xsessions/`. MATE should appear in the session menu if installed properly.

## Troubleshooting

**Session won’t start:** Check `/var/log/Xorg.0.log` for errors:

``` bash
tail -n 50 /var/log/Xorg.0.log
```

**Wrong session launching:** Remove `$HOME/.xinitrc` if you want to fall back to system detection, or double-check the executable name:

``` bash
dpkg -L mate-session 2>/dev/null || rpm -ql mate-session
```

**Keyboard/mouse not working:** Add explicit device initialization:

``` bash
exec mate-session
```

If that fails, add `dbus-launch` before mate-session:

``` bash
exec dbus-launch --exit-with-session mate-session
```

The dbus session daemon is critical for modern desktop environments and should launch automatically, but explicit invocation resolves edge cases on minimal installs.

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
