---
title: "Debugging LightDM Login Failures in Ubuntu"
date: 2018-03-24 11:46:48 +0000
modified: 2026-04-12 16:06:37 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /i-cannot-login-ubuntu-precise-desktop/
---

If you’re stuck at the Ubuntu login screen with errors like “Could not write bytes: Broken Pipe” or “Check Battery State,” the display manager is likely corrupted or misconfigured. This typically indicates a problem with LightDM, Ubuntu’s default display manager since 12.04.

## Understanding the Problem

LightDM (the lightweight X display manager) manages your login session and desktop startup. When it fails, you get stuck before reaching your desktop environment. Common causes include:

- Corrupted LightDM configuration files
- Permissions issues in `/var/lib/lightdm/`
- Driver conflicts or X server problems
- Failed package upgrades

The “Broken Pipe” error usually means the display manager can’t communicate with the X server or your session environment.

## Quick Diagnostics

Before replacing LightDM, check the logs:

``` bash
sudo tail -100 /var/log/lightdm/lightdm.log
sudo tail -100 /var/log/lightdm/x-0-greeter.log
```

These files often reveal the exact failure point.

## Solution 1: Reset LightDM Configuration (Try This First)

``` bash
sudo systemctl stop lightdm
sudo rm -rf ~/.cache/lightdm/
sudo rm -rf ~/.Xauthority
sudo systemctl start lightdm
```

If you can’t access a TTY, boot into recovery mode (hold Shift during startup, select “Drop to root shell prompt”).

## Solution 2: Reinstall LightDM

A clean reinstall often fixes corrupted installations:

``` bash
sudo apt-get remove lightdm
sudo apt-get install lightdm lightdm-gtk-greeter
sudo dpkg-reconfigure lightdm
```

Then reboot.

## Solution 3: Switch to GDM

If LightDM remains broken, GDM (GNOME Display Manager) is a stable alternative. From a TTY or recovery shell:

``` bash
sudo apt-get install gdm3
sudo dpkg-reconfigure gdm3
```

When prompted, select GDM as your default display manager. GDM is heavier than LightDM but more robust for troubleshooting.

For Wayland-based desktops (GNOME 3.20+), GDM also handles Wayland sessions better than LightDM.

## Accessing a TTY if Login Fails Completely

If the graphical login loop prevents any access:

1.  Press `Ctrl+Alt+F2` (or `Ctrl+Alt+F3` through `F6`)
2.  Log in with your username and password
3.  Run the commands above

## Prevention

To avoid future display manager issues:

- Keep your system updated: `sudo apt-get update && sudo apt-get upgrade`
- Don’t forcefully kill the display manager—use `systemctl stop`
- Monitor disk space; a full `/var` partition breaks session creation
- Keep `.config/` and `.local/share/` permissions correct: `chmod 700 ~/{.config,.local}`

## Checking Your Current Display Manager

``` bash
cat /etc/X11/default-display-manager
```

Or on systemd systems:

``` bash
systemctl status display-manager
```

Most modern Ubuntu installs use GDM by default now, though LightDM remains an option for lighter desktop environments like Lubuntu and Xubuntu.

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
