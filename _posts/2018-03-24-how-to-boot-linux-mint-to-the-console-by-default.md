---
title: "Boot Linux Mint into Console Mode by Default"
date: 2018-03-24 11:42:44 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-boot-linux-mint-to-the-console-by-default/
---

Linux Mint defaults to graphical mode, but you can boot directly to the console if you prefer a text-only environment or need to troubleshoot display issues. There are two main approaches: using GRUB parameters or disabling the display manager entirely.

## Method 1: Add the `text` kernel parameter (GRUB)

This is the quickest approach and keeps your display manager installed, so you can still switch to graphical mode later if needed.

Edit the GRUB configuration:

``` bash
sudo nano /etc/default/grub
```

Find the line starting with `GRUB_CMDLINE_LINUX_DEFAULT` and add `text` to it:

``` bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash text"
```

Save the file (Ctrl+O, Enter, Ctrl+X in nano), then regenerate the GRUB configuration:

``` bash
sudo update-grub
```

Reboot to test:

``` bash
sudo reboot
```

This method works on all recent Linux Mint releases. If you want to return to graphical mode later, just remove `text` from the GRUB line and update GRUB again.

## Method 2: Disable the display manager (persistent)

If you want to completely remove graphical login, disable the display manager. Linux Mint typically uses LightDM (or MDM on older versions).

First, check which display manager is running:

``` bash
cat /etc/X11/default-display-manager
```

For LightDM (modern Mint versions):

``` bash
sudo systemctl disable lightdm
sudo systemctl mask lightdm
```

For older Mint versions using MDM:

``` bash
sudo apt remove mint-mdm mdm mint-mdm-themes
```

Optional cleanup (not required, but removes unused files):

``` bash
sudo apt remove lightdm lightdm-gtk-greeter
sudo rm -rf /var/cache/lightdm
```

Reboot:

``` bash
sudo reboot
```

## Switching back to graphical mode

**If you used Method 1:** Simply remove `text` from your GRUB configuration and run `sudo update-grub`.

**If you used Method 2:** Reinstall and re-enable the display manager:

``` bash
sudo apt install lightdm lightdm-gtk-greeter
sudo systemctl enable lightdm
sudo systemctl unmask lightdm
sudo reboot
```

## Accessing the graphical desktop from console mode

If you boot to console but want to start a graphical session temporarily:

``` bash
startx
```

You can also start a specific desktop environment if multiple are installed:

``` bash
DISPLAY=:0 cinnamon &
```

## Systemd target vs runlevel

Modern Linux (including recent Mint releases) uses `systemd` targets instead of runlevels. Console mode corresponds to `multi-user.target` rather than the older “runlevel 3” concept. You can also switch targets on the fly:

``` bash
sudo systemctl isolate multi-user.target    # Switch to console
sudo systemctl isolate graphical.target     # Switch to graphical mode
```

To set the default boot target:

``` bash
sudo systemctl set-default multi-user.target
sudo systemctl set-default graphical.target  # To revert
```

Method 1 (GRUB parameter) is usually preferred because it’s reversible and doesn’t require reinstalling packages.

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
