---
title: "Switching Linux Systemd Boot Targets"
date: 2016-09-17 02:15:12 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /change-systemd-boot-target-linux/
---

Systemd replaced traditional init on most modern Linux distributions, shifting terminology from “runlevels” to “targets.” If you’re migrating from older systems, here’s the mapping:

| Runlevel | Systemd Target      | Purpose             |
|----------|---------------------|---------------------|
| 0        | `poweroff.target`   | Shutdown            |
| 1        | `rescue.target`     | Single-user mode    |
| 2, 3, 4  | `multi-user.target` | Multi-user, no GUI  |
| 5        | `graphical.target`  | Multi-user with GUI |
| 6        | `reboot.target`     | Reboot              |

The two targets you’ll use most are `multi-user.target` (CLI only) and `graphical.target` (desktop environment).

## Checking the Current Target

View your default boot target:

``` bash
systemctl get-default
```

List all currently active targets:

``` bash
systemctl list-units --type target
```

See all targets installed on your system:

``` bash
systemctl list-unit-files --type target
```

## Switching Target Immediately

Use `isolate` to switch the active target without rebooting:

``` bash
sudo systemctl isolate multi-user.target
```

Or to switch to graphical mode:

``` bash
sudo systemctl isolate graphical.target
```

The `isolate` command starts the target and its dependencies while stopping conflicting units—equivalent to the legacy `init 3` or `init 5` commands.

**Important caveat:** `isolate` may interrupt active services. In production environments, plan for potential downtime. Switching from graphical to multi-user will terminate your display manager and X11/Wayland session, killing any unsaved work in running applications. Use this primarily for troubleshooting or scheduled maintenance windows.

## Setting the Default Boot Target

Permanently change what target loads on boot:

``` bash
sudo systemctl set-default multi-user.target
```

Or for graphical mode:

``` bash
sudo systemctl set-default graphical.target
```

Verify the change:

``` bash
systemctl get-default
```

This creates or updates a symlink at `/etc/systemd/system/default.target`. Run it once—systemd handles all necessary setup. The `enable` command isn’t needed for targets.

## Rescue and Emergency Targets

### Rescue Mode

Boot into a minimal environment for troubleshooting:

``` bash
sudo systemctl isolate rescue.target
```

Rescue mode requires the root password and disables most non-critical services. Use it for:

- System repairs without full multi-user mode
- Filesystem checks and repairs
- Emergency configuration changes

To boot into rescue on the next restart:

``` bash
sudo systemctl set-default rescue.target
sudo reboot
```

After repairs, restore your normal target:

``` bash
sudo systemctl set-default graphical.target
sudo systemctl isolate graphical.target
```

### Emergency Mode

For severe troubleshooting when rescue mode isn’t sufficient:

``` bash
sudo systemctl isolate emergency.target
```

Emergency mode provides only the root filesystem—mounted read-only—with virtually no services running. The root password is required. Use this only when:

- `rescue.target` won’t boot
- You need maximum isolation to diagnose filesystem or boot issues
- You can’t mount additional filesystems

After emergency repairs, reboot cleanly:

``` bash
sudo systemctl reboot
```

Don’t isolate back to graphical mode after emergency repairs; a clean reboot ensures filesystem checks run properly.

## Understanding the Default Target Symlink

Systemd manages the default target via a symlink. View it with:

``` bash
ls -l /etc/systemd/system/default.target
```

This symlink points to a file in `/usr/lib/systemd/system/`. Never manually edit this symlink—always use `systemctl set-default`. This command is idempotent, integrates with systemd’s management layer, and prevents configuration errors.

## Common Workflows

### Disable GUI for Lower Resource Usage

``` bash
sudo systemctl set-default multi-user.target
sudo systemctl isolate multi-user.target
```

### Re-enable GUI

``` bash
sudo systemctl set-default graphical.target
sudo systemctl start graphical.target
```

Here, `start` launches the graphical target without stopping multi-user services—usually sufficient. Use `isolate` only if you encounter conflicts between targets.

### Check What Loads at Boot Without Rebooting

``` bash
systemctl list-unit-files | grep enabled
systemctl list-dependencies graphical.target
```

The first command shows all enabled services. The second displays the full dependency chain for your default target, confirming what will start on boot.

### View All Unit Dependencies for a Target

``` bash
systemctl list-dependencies --all multi-user.target
```

This recursively shows every service, socket, and timer that a target depends on, useful for understanding what runs when you boot into a given mode.

## Troubleshooting

If you accidentally set the wrong default target and can’t reach the GUI:

1.  Boot the system (you’ll land at a CLI login)
2.  Log in as root or a sudoer
3.  Run `sudo systemctl set-default graphical.target`
4.  Reboot

If the system won’t boot to rescue mode, interrupt the boot process at the GRUB menu (hold Shift during boot on many systems) and append `systemd.unit=rescue.target` to the kernel command line. This forces the kernel to boot into rescue mode for one boot cycle.
