---
title: "Boot Linux to Console Mode with systemd"
date: 2018-03-24 11:47:26 +0000
layout: post
canonical: https://www.systutorials.com/how-to-configure-systemd-to-boot-linux-to-console-mode-runlevel-3/
---

systemd uses *targets* instead of the old sysvinit runlevels. Runlevel 3 (console mode) maps to `multi-user.target`. Here’s how to boot directly to console on Fedora, RHEL, Debian, Ubuntu, and other systemd-based distributions.

## Switch to Console Mode Immediately

To switch from graphical mode to console without rebooting:

``` bash
sudo systemctl isolate multi-user.target
```

This immediately stops the display manager and any graphical services, leaving you with a text console.

## Boot to Console Mode by Default

To make console mode the default boot target, set it as the default:

``` bash
sudo systemctl set-default multi-user.target
```

Verify the change:

``` bash
systemctl get-default
```

This command outputs `multi-user.target` if configured correctly.

To revert to graphical mode:

``` bash
sudo systemctl set-default graphical.target
```

## Boot to Console Mode Once (Without Making It Permanent)

If you only want to boot to console this time, add a kernel argument at boot. Interrupt GRUB, press `e` to edit the boot entry, and add `systemd.unit=multi-user.target` to the kernel line. Press Ctrl+X to boot.

For a permanent kernel argument, edit `/etc/default/grub`:

``` bash
sudo nano /etc/default/grub
```

Add to the `GRUB_CMDLINE_LINUX` line:

    GRUB_CMDLINE_LINUX="... systemd.unit=multi-user.target"

Then rebuild GRUB:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg  # RHEL/Fedora/CentOS
# or
sudo update-grub  # Debian/Ubuntu
```

## Disable the Display Manager Service

If you’ve set the default to `multi-user.target` but graphical mode still loads, the display manager service may be enabled independently. Check and disable it:

``` bash
systemctl list-unit-files | grep -E 'gdm|lightdm|sddm|lxdm'
```

Common display managers include:

- `gdm.service` (GNOME)
- `lightdm.service` (lightweight systems)
- `sddm.service` (KDE Plasma)
- `lxdm.service` (LXDE)

Disable the active one:

``` bash
sudo systemctl disable gdm.service
sudo systemctl disable sddm.service
sudo systemctl disable lightdm.service
```

You only need to disable whichever display manager your distribution actually uses. Running all three is harmless if only one is installed.

## Verify Your Configuration

After making changes, check what will load at boot:

``` bash
systemctl list-dependencies multi-user.target
```

This shows all units pulled in by the console target. Services like SSH, networking, and system daemons should appear here.

To see what’s currently running:

``` bash
systemctl list-units --type=service --state=running
```

## Return to Graphical Mode

If you need graphical mode again:

``` bash
sudo systemctl set-default graphical.target
sudo systemctl enable gdm.service  # or sddm, lightdm, etc.
sudo reboot
```

Console mode is useful for servers, headless systems, or when troubleshooting graphical issues. The `multi-user.target` boots faster, uses fewer resources, and keeps the system focused on services rather than a desktop environment.

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
