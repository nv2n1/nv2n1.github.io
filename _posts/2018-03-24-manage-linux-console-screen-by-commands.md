---
title: "Controlling Linux Console Blanking and Power Settings"
date: 2018-03-24 11:42:51 +0000
layout: post
canonical: https://www.systutorials.com/manage-linux-console-screen-by-commands/
---

Managing display power and screen blanking on Linux systems is essential for reducing power consumption on servers, headless machines, and workstations. Two primary tools handle this: `setterm` for software-based blanking and `vbetool` for hardware power management via VESA DPMS.

## Screen Blanking with setterm

The `setterm` command controls when and how the console screen blanks during periods of inactivity. This works on virtual consoles (TTY devices), not on graphical displays.

### Setting blanking timeout

``` bash
setterm -blank 10
```

This blanks the screen after 10 minutes of inactivity. The interval accepts values from 0 to 60 minutes. A value of 0 disables blanking entirely.

``` bash
setterm -blank force
```

The `force` option keeps the screen blank even when keys are pressed, useful for preventing accidental input wake-ups.

### Unblanking the screen

``` bash
setterm -blank poke
```

The `poke` option unblank the screen immediately, restoring display output.

### Checking blank status

``` bash
setterm -blank
```

Running without arguments returns the current blanking state, showing which virtual terminal is blanked or zero if none are blanked.

## Hardware Power Management with vbetool

For systems supporting VESA DPMS (Display Power Management Signaling), `vbetool` provides direct control over monitor power states through VESA 0x4f10 extensions.

### Turning off monitor power

``` bash
vbetool dpms off
```

This powers down the monitor completely, consuming minimal energy.

### DPMS states

`vbetool` accepts these power states:

- **on** — Display fully powered and active
- **standby** — Low power, quick resume (~1-2 seconds)
- **suspend** — Deeper sleep state, slower resume (~3-10 seconds)
- **reduced** — Minimal power reduction, display remains responsive
- **off** — Complete power down

Example setting monitor to standby:

``` bash
vbetool dpms standby
```

## Practical combined approach

For integrated power management on servers, combine both tools:

``` bash
# Blank console after 5 minutes of inactivity
setterm -blank 5

# Power down monitor after 10 minutes (requires periodic script)
```

Note: `vbetool` requires root privileges and works primarily on systems with legacy BIOS. Modern systems using UEFI may need alternative approaches like `xset` (for X11) or `brightnessctl` for backlight control.

## Checking tool availability

Verify `setterm` is available (usually pre-installed):

``` bash
which setterm
```

Check if `vbetool` is installed:

``` bash
which vbetool
```

If missing, install via your package manager:

``` bash
# Debian/Ubuntu
sudo apt install vbetool

# RHEL/CentOS/Fedora
sudo dnf install vbetool
```

## Persistent configuration

To apply settings across reboots, add commands to system initialization scripts or systemd units. For virtual consoles, modify `/etc/default/grub` or add settings to `.bashrc` for user-specific configurations.

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
