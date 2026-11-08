---
title: "Centering MPlayer and mpv Windows on Linux"
date: 2018-03-24 08:22:36 +0000
modified: 2026-04-12 16:04:30 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-force-mplayer-to-start-a-video-at-the-center-of-the-screen/
---

MPlayer is largely obsolete, but if you’re maintaining legacy systems, you’ll need to know how to position windows. For new work, use **mpv** (MPlayer’s maintained fork) instead.

## Centering with MPlayer

Add this to `~/.mplayer/config`:

    geometry=50%:50%

This centers the window by setting both X and Y to 50% of screen dimensions.

Override at runtime:

``` bash
mplayer -geometry 50%:50% video.mp4
```

## Geometry syntax reference

The format is `X:Y`. Values can be:

- **Absolute pixels**: `geometry=1920:1080` (top-left corner position)
- **Screen percentages**: `geometry=50%:50%` (center)
- **Mixed**: `geometry=50%:100` (50% horizontal, 100px down)
- **Negative offsets**: `geometry=-10:50%` (10px from right edge, 50% down)

Examples:

    geometry=100:100          # 100px from top-left
    geometry=25%:75%          # 25% from left, 75% from top
    geometry=-50:-50          # 50px from bottom-right corner
    geometry=1280:0           # 1280px from left, at top

## Using mpv (recommended)

If you’re choosing a player, use **mpv**:

``` bash
mpv --geometry=50%:50% video.mp4
```

Or with pixel coordinates:

``` bash
mpv --geometry=1920x1080+100+100 video.mp4
```

mpv’s geometry syntax is X×Y±X±Y (width×height+X+Y offset).

For window positioning without explicit dimensions:

``` bash
mpv --geometry=50%:50% --force-window=immediate video.mp4
```

The `--force-window` flag ensures a window opens even for audio files, making geometry settings reliable.

## Window manager conflicts

Modern desktop environments may ignore geometry hints. Troubleshooting:

**Check if fullscreen is interfering:**

``` bash
mplayer --no-fs -geometry 50%:50% video.mp4
mpv --fs=no --geometry=50%:50% video.mp4
```

**Use xdotool for post-launch positioning:**

``` bash
mplayer video.mp4 &
sleep 1
xdotool search --name mplayer windowmove --window %@ 50% 50%
```

**On GNOME/KDE with tiling:**

Your window manager may enforce tiling rules. Check preferences or use floating window mode:

- GNOME: Super+Y toggles window management
- KDE: Right-click title bar → More Actions → Keep Above Others
- i3/sway: Use `floating enable` in config

**On Wayland:**

Geometry hints don’t work reliably—Wayland doesn’t expose the coordinate system to applications. Use your compositor’s window management instead, or switch to X11.

## Config file locations

MPlayer checks these in order:

    ~/.mplayer/config                    # Traditional
    ~/.config/mplayer/config             # XDG standard
    /etc/mplayer/mplayer.conf            # System-wide

Find which config files are loaded:

``` bash
mplayer -v 2>&1 | grep -i config
```

Edit the first one that exists, or create one in `~/.mplayer/` for compatibility.

## Quick reference

| Task                    | Command                                       |
|-------------------------|-----------------------------------------------|
| Center window (MPlayer) | `mplayer -geometry 50%:50% video.mp4`         |
| Center window (mpv)     | `mpv --geometry=50%:50% video.mp4`            |
| Absolute position       | `mpv --geometry=1920x1080+200+100 video.mp4`  |
| Disable fullscreen      | `mplayer --no-fs -geometry 50%:50% video.mp4` |
| Check active config     | `mplayer -v 2>&1 \| grep config`              |

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
