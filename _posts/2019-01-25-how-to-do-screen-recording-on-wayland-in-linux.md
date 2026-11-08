---
title: "Screen Recording on Wayland: GNOME, OBS, and Kooha"
date: 2019-01-25 08:06:32 +0000
layout: post
canonical: https://www.systutorials.com/how-to-do-screen-recording-on-wayland-in-linux/
---

Wayland screen recording has matured significantly. Here are the tools that actually work well in 2026, with their tradeoffs and setup.

## GNOME Built-in Screen Recording

GNOME 40+ includes integrated screen recording on Wayland. Press `Ctrl+Alt+Shift+R` to start. A red dot appears in the top-right corner. Press the same shortcut again or click the indicator to stop.

Recordings save as WebM in `~/Videos/` by default.

### Extending Recording Duration

The default 30-second limit is usually too short. Increase it:

``` bash
gsettings set org.gnome.settings-daemon.plugins.media-keys max-screencast-length 600
```

Replace `600` with your desired duration in seconds. For a 10-minute recording, use `600`.

Check the current setting:

``` bash
gsettings get org.gnome.settings-daemon.plugins.media-keys max-screencast-length
```

Reset to default:

``` bash
gsettings reset org.gnome.settings-daemon.plugins.media-keys max-screencast-length
```

### Converting Output Format

Recordings come out as WebM. If you need MP4 or another format, convert with ffmpeg:

``` bash
ffmpeg -i input.webm -c:v libx264 -crf 23 -c:a aac output.mp4
```

This is good enough for quick demos and documentation. Skip it if you need fine-grained control over quality, bitrate, or multiple audio sources.

## OBS Studio

OBS 29+ has solid Wayland support and is the right choice for streaming, multi-source recordings, or custom encoding.

Install it:

``` bash
# Debian/Ubuntu
sudo apt install obs-studio

# Fedora
sudo dnf install obs-studio

# Arch
sudo pacman -S obs-studio
```

Launch and add a screen source. OBS supports:

- Multiple audio tracks
- Custom bitrate and codec selection
- Direct streaming to Twitch, YouTube, or RTMP servers
- Scene switching and transitions
- Advanced filters and effects

### Basic OBS Wayland Setup

When you launch OBS on Wayland for the first time, it may prompt for screen access permissions. Grant them. Then:

1.  Click the `+` button under Sources
2.  Select “Screen Capture (PipeWire)”
3.  Choose your monitor
4.  Adjust resolution and bitrate in Settings \> Output

For CPU-efficient recording on older hardware, use the VP9 codec with quality `crf 32`. For streaming, use H.264 with bitrate 4000–6000 Kbps depending on your upload speed.

## Kooha

Kooha is a lightweight GTK app built specifically for Wayland. It handles basic recording without the complexity of OBS.

Features:

- Simple GUI with sensible defaults
- MP4 and WebM output
- Frame rate and resolution control
- Optional audio capture from microphone or system

Install via Flathub:

``` bash
flatpak install flathub io.github.seadve.Kooha
```

Or from distro repositories:

``` bash
# Ubuntu 24.04+
sudo apt install kooha

# Fedora 40+
sudo dnf install kooha

# Arch
sudo pacman -S kooha
```

Kooha is faster to set up than OBS and uses less CPU. Useful for quick recordings when you don’t need streaming or advanced editing.

## Programmatic Recording with GNOME’s Screencast API

For automation or scripts, trigger GNOME’s recorder via D-Bus:

``` bash
dbus-send --session \
  --dest=org.gnome.Shell \
  --object-path=/org/gnome/Shell/Extensions/ScreenshotUI \
  org.gnome.Shell.Extensions.ScreenshotUI.Screencast
```

This starts recording without opening a GUI window. Useful in CI/CD pipelines or unattended recording workflows. Stop it by pressing `Ctrl+Alt+Shift+R` or send another D-Bus call.

## Wayland-Specific Gotchas

**PipeWire for Audio**

Modern recorders use PipeWire instead of PulseAudio for audio capture. If audio doesn’t record, check that PipeWire is running:

``` bash
pactl info | grep "Server Name"
```

Output should include “PipeWire”. If it shows PulseAudio, your distro hasn’t migrated yet. Check your distro’s documentation for enabling PipeWire.

**Multi-Monitor Recording**

Wayland doesn’t expose monitors via simple X11-style APIs. Most tools capture only the focused monitor. To record a different display:

- OBS: Add multiple screen sources, one per monitor
- GNOME built-in: Move the window to the target monitor before recording
- Kooha: Select the target display in settings before starting

Recording a specific window (not the whole screen) works well with GNOME built-in and OBS. Kooha is primarily for full-screen capture.

**Permissions**

GNOME handles permissions automatically. Flatpak apps (including Kooha) may prompt for screen casting permissions on first use—grant them.

## Choosing the Right Tool

| Tool | CPU Overhead | Best For | Setup Time |
|----|----|----|----|
| GNOME Built-in | Minimal | Quick clips, demos | 10 seconds |
| OBS | Moderate | Streaming, multi-source, complex encoding | 5 minutes |
| Kooha | Minimal | Lightweight standalone app, MP4 export | 1 minute |

Use GNOME built-in for quick clips and demos. Use OBS if you’re streaming or need fine-grained control over quality and encoding. Use Kooha if you want a lightweight app with MP4 output out of the box.
