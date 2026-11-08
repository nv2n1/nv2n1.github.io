---
title: "Remap Space Bar to Ctrl with Tap-for-Space on Linux"
date: 2018-03-24 08:22:11 +0000
modified: 2026-04-11 16:02:59 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-turn-the-space-bar-to-another-ctrl-key/
---

Remapping space to Ctrl while preserving space on tap is useful for modal editors and power users. The challenge: distinguish between a held key (Ctrl) and a quick tap (space). Kernel-level remapping can’t do this, so you need userspace solutions.

## Quick Comparison of Methods

| Tool | Best For | Pros | Cons |
|----|----|----|----|
| keyd | Simplicity, both X11 and Wayland | Single config file, works everywhere | Less mature than xcape |
| xcape | X11-only setups, fine-grained control | Stable, widely tested | X11 only |
| interception-tools | Wayland, complex key combos | Robust, scriptable | Steeper learning curve |

## Using keyd (Recommended for 2026)

keyd is the simplest modern approach and works on both X11 and Wayland.

Install:

``` bash
sudo apt install keyd  # Debian/Ubuntu
sudo dnf install keyd  # Fedora
sudo pacman -S keyd    # Arch
```

Edit `/etc/keyd/default.conf`:

``` ini
[ids]
*

[main]
space = oneshot(ctrl)
```

The `oneshot` layer means: hold space for Ctrl, tap space for space. Adjust timing with:

``` ini
[main]
space = oneshot(ctrl, timeout=200)
```

Enable and start:

``` bash
sudo systemctl enable --now keyd
```

Verify it works by opening a text editor and testing both hold (Ctrl+C should work) and tap (space should insert a space).

## Using xcape (X11-only, stable alternative)

If you’re stuck on X11 and need battle-tested stability, xcape works well.

First, remap space to Ctrl at the XKB level. Create or edit `~/.config/xkb/symbols/custom`:

    default partial alphanumeric_keys modifier_keys
    xkb_symbols "custom" {
        include "pc(pc105)"
        key <SPCE> { [ Control_L, Control_L ] };
    };

Load it:

``` bash
setxkbmap -I$HOME/.config/xkb -symbols "pc+us+custom"
```

Install xcape:

``` bash
sudo apt install xcape  # Debian/Ubuntu
sudo dnf install xcape  # Fedora
```

Run xcape:

``` bash
xcape -e 'Control_L=space'
```

For persistence, add to `~/.xinitrc`:

``` bash
xcape -e 'Control_L=space' &
```

Or create a systemd user service at `~/.config/systemd/user/xcape.service`:

``` ini
[Unit]
Description=xcape - Tap space for space, hold for Ctrl
After=graphical-session-pre.target
PartOf=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/xcape -e 'Control_L=space'
Restart=on-failure
RestartSec=2

[Install]
WantedBy=graphical-session.target
```

Enable it:

``` bash
systemctl --user daemon-reload
systemctl --user enable --now xcape
```

Adjust timeout if space feels laggy:

``` bash
xcape -t 150 -e 'Control_L=space'  # 150ms tap threshold
```

## Using interception-tools (Wayland-native)

For Wayland sessions or when you need advanced key filtering:

Install:

``` bash
sudo apt install interception-tools  # Debian/Ubuntu
sudo dnf install interception-tools  # Fedora
```

Create `/etc/interception/udevmon.yaml`:

``` yaml
- JOB: "intercept -g $DEVNODE | space2ctrl | uinput -d $DEVNODE"
  DEVICE:
    EVENTS:
      EV_KEY: [KEY_SPACE]
```

Enable:

``` bash
sudo systemctl enable --now udevmon
```

Check status:

``` bash
sudo systemctl status udevmon
journalctl -u udevmon -f
```

## Testing Your Setup

Verify the mapping with `evtest` (shows raw events):

``` bash
sudo evtest
```

Or on X11 with `xev`:

``` bash
xev
```

Hold space—should show Ctrl. Tap space quickly—should show space character. If it feels off, adjust timeout settings in your config.

## Common Issues

**Rapid typing registers as Ctrl instead of space**
Increase the timeout: `space = oneshot(ctrl, timeout=250)` in keyd, or `xcape -t 150` for xcape.

**Nothing happens after enabling the service**
Check logs: `journalctl --user -u xcape -f` for xcape, or `journalctl -u udevmon -f` for interception-tools. Ensure systemd service has proper paths.

**Works in some apps but not others**
Some applications bypass normal key handling (games, some terminals). Test with a simple text editor first. For games, you may need separate profiles or disable the mapping temporarily.

**Wayland session not working with xcape**
xcape only works on X11. Switch to keyd or interception-tools for Wayland, or set `QT_QPA_PLATFORM=xcb` as a workaround (not reliable long-term).

**Small delay before space is recognized**
This is normal—the system waits for the timeout before deciding “tap” vs “hold.” Reduce timeout if acceptable (trade-off: faster Ctrl, slower space).
