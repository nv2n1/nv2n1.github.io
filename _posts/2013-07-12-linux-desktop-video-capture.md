---
title: "Capturing Desktop Video on Linux with ffmpeg"
date: 2013-07-12 16:32:02 +0000
modified: 2026-04-12 05:27:33 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /linux-desktop-video-capture/
---

ffmpeg is the de facto tool for desktop recording on Linux. It can capture your X11 or Wayland display and encode directly to MP4, WebM, or other formats without requiring intermediate files.

## Basic X11 Screen Capture

For X11-based desktops (KDE Plasma, XFCE, i3, etc.), use the `x11grab` input device:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 -c:v libx264 -preset fast -crf 23 output.mp4
```

Breaking down the options:

- `-f x11grab` — Input format for X11 display capture
- `-s 1920x1080` — Output resolution (adjust to your display size; check with `xrandr`)
- `-r 30` — Frames per second (24, 30, or 60 are typical)
- `-i :0.0+0,0` — Display and offset (`:0.0` is usually your main display; `+0,0` is the top-left corner)
- `-c:v libx264` — Video codec (H.264 for broad compatibility)
- `-preset fast` — Encoding speed/quality tradeoff (ultrafast, superfast, fast, medium, slow, slower)
- `-crf 23` — Quality level (0–51; lower is better; 23 is default)

## Finding Your Display and Resolution

First, determine your actual display size and number:

``` bash
xrandr | grep connected
```

This shows connected displays and their resolutions. If you have multiple displays and want to capture only one:

``` bash
ffmpeg -f x11grab -s 2560x1440 -r 30 -i :0.0+1920,0 output.mp4
```

The `+1920,0` offset captures a display starting 1920 pixels to the right—useful for multi-monitor setups.

## Including Audio

Capture system audio along with video using PulseAudio:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 \
  -f pulse -i default -c:v libx264 -preset fast -c:a aac output.mp4
```

For PipeWire (now standard on most distributions), the audio device is similar but may be labeled differently. Check available sources:

``` bash
pactl list sources | grep -A2 "Name:"
```

## Wayland Desktop Capture

X11 grab doesn’t work on Wayland. Use `pipewire` instead:

``` bash
ffmpeg -f pipewire -i - -c:v libx264 -preset fast output.mp4
```

Or capture a specific window via PipeWire’s screencast protocol. Most modern desktop environments (GNOME 42+, KDE Plasma 5.27+) support this natively through `xdg-desktop-portal-*` implementations.

## Reducing CPU Usage

Real-time desktop recording is CPU-intensive. Optimize for lower overhead:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 \
  -c:v libx264 -preset ultrafast -crf 28 -thread_queue_size 512 output.mp4
```

Use `ultrafast` preset for live streaming or when CPU is constrained. If you’re willing to spend more time encoding, switch to `libx265` (H.265/HEVC) with lower bitrate:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 \
  -c:v libx265 -preset fast -crf 28 output.mp4
```

## Recording a Specific Window

To capture a single window instead of the entire desktop, first get its window ID:

``` bash
xdotool search --name "Firefox"
```

Then use that window’s geometry:

``` bash
WINDOW_ID=$(xdotool search --name "Firefox" | head -1)
xdotool getwindowgeometry "$WINDOW_ID"
```

Capture it directly using the coordinates returned:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+100,100 output.mp4
```

## Common Issues

**“Permission denied” or “Cannot connect to display”:** Set the correct DISPLAY variable:

``` bash
export DISPLAY=:0
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 output.mp4
```

**High CPU usage:** Reduce frame rate (`-r 24` instead of 30), use `ultrafast` preset, or increase `-crf` value (lower quality = faster encoding).

**Audio out of sync:** Add audio sync options:

``` bash
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 \
  -f pulse -i default -c:v libx264 -c:a aac -async 1 output.mp4
```

**No audio recorded:** Verify PulseAudio/PipeWire is running and check `pactl list sources` or `wpctl status` for available devices.

## Output Formats

For different use cases:

``` bash
# MP4 (broad compatibility)
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 -c:v libx264 output.mp4

# WebM (web streaming)
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 -c:v libvpx-vp9 output.webm

# QuickTime (macOS-friendly)
ffmpeg -f x11grab -s 1920x1080 -r 30 -i :0.0+0,0 -c:v libx264 output.mov
```

Consult the ffmpeg documentation (`man ffmpeg` or `ffmpeg -h full`) for additional encoding options and codecs.
