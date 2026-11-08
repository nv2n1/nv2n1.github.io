---
title: "Loop Videos in Fullscreen with mpv on Linux"
date: 2018-03-24 11:49:37 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-play-video-in-full-screen-and-keep-it-looping-with-mplayer/
---

mpv is a powerful media player for Linux that supports looping videos with minimal configuration. Here’s how to loop videos in fullscreen mode using mpv.

## Loop a Single Video

The simplest way — use the `--loop` flag:

```wp-block-code
mpv --fullscreen --loop video.mp4
```

`--loop` replays the video infinitely. To loop a specific number of times:

```wp-block-code
# Loop 5 times
mpv --fullscreen --loop=5 video.mp4
```

## Loop a Playlist

```wp-block-code
# Loop all videos in a directory
mpv --fullscreen --loop-playlist ~/Videos/*.mp4

# Loop playlist infinitely
mpv --fullscreen --loop-playlist=inf ~/Videos/*.mp4

# Shuffle and loop
mpv --fullscreen --loop-playlist --shuffle ~/Music/*.flac
```

## Loop a Portion of a Video (A-B Loop)

During playback, set A-B loop points to repeat a section:

1.  Press **l** at the start point (sets point A)
2.  Press **l** again at the end point (sets point B)
3.  The section between A and B loops continuously
4.  Press **l** a third time to disable A-B loop

## Configuration File

Set default looping behavior in mpv’s config file:

```wp-block-code
# ~/.config/mpv/mpv.conf
# Default to fullscreen and loop
fullscreen=yes
loop-playlist=inf

# Always loop the current file
loop-file=inf

# Useful quality-of-life settings
keep-open=yes           # Don't close after playback ends
save-position-on-quit=yes  # Remember where you stopped
```

## Keyboard Shortcuts for Looping

During playback, these shortcuts control looping:

- **l** — Set/clear A-B loop points
- **Shift+l** — Toggle infinite file loop
- **Shift+L** — Toggle playlist loop
- **LEFT/RIGHT** — Seek 5 seconds
- **UP/DOWN** — Seek 60 seconds
- **f** — Toggle fullscreen
- **ESC** — Exit fullscreen
- **q** — Quit

## Loop with Audio Visualization

For audio files, add visualizations while looping:

```wp-block-code
# Audio with visualizer
mpv --fullscreen --loop --audio-visualizer=avdebug ~/Music/song.flac
```

## Loop for Digital Signage or Kiosks

For unattended displays, configure mpv for reliable looping:

```wp-block-code
mpv --fullscreen \
    --loop-playlist=inf \
    --no-osd-bar \
    --no-stop-screensaver \
    --profile=pseudo-gui \
    --force-window \
    playlist.m3u
```

Create the playlist file:

```wp-block-code
# playlist.m3u
video1.mp4
video2.mp4
video3.mp4
```

For truly unattended operation, wrap it in a script that restarts mpv if it crashes:

```wp-block-code
#!/bin/bash
while true; do
    mpv --fullscreen --loop-playlist=inf --no-osd-bar playlist.m3u
    sleep 2
done
```

## GPU-Accelerated Video Looping

For smooth 4K looping, ensure hardware decoding is active:

```wp-block-code
mpv --fullscreen --loop --hwdec=auto 4kvideo.mp4
```

Check if hardware decoding is working:

```wp-block-code
mpv --fullscreen --loop --hwdec=auto --msg-level=all=info 4kvideo.mp4 2>&1 | grep hwdec
```

## Streaming Video Loops

mpv can loop network streams as well:

```wp-block-code
# Loop a live stream
mpv --fullscreen --loop https://stream.example.com/live.m3u8

# Loop a YouTube video (requires yt-dlp)
mpv --fullscreen --loop "https://youtube.com/watch?v=VIDEO_ID"
```

Install yt-dlp for YouTube and other streaming platform support:

```wp-block-code
pip install yt-dlp
# Or
sudo dnf install yt-dlp    # Fedora
sudo apt install yt-dlp    # Ubuntu
```

## mpv Configuration for Ambient Displays

For always-on ambient displays or art installations:

```wp-block-code
# ~/.config/mpv/mpv.conf for ambient display
fullscreen=yes
loop-playlist=inf
no-osd-bar=yes
no-input-default-bindings=yes
input-vo-keyboard=no
profile=gpu-hq
dither-depth=auto
gpu-api=vulkan
```

This configuration maximizes video quality while disabling all keyboard input to prevent accidental interruption.

## mpv Scripting for Advanced Loop Control

mpv supports Lua scripts for custom behavior. Create a script that loops specific files differently:

```wp-block-code
-- ~/.config/mpv/scripts/smart-loop.lua
-- Auto-loop short clips, play once for long videos
mp.register_event("file-loaded", function()
    local duration = mp.get_property_number("duration")
    if duration and duration < 60 then
        mp.set_property("loop-file", "inf")
        mp.msg.info("Short clip detected, enabling loop")
    end
end)
```

Save as `~/.config/mpv/scripts/smart-loop.lua` and mpv loads it automatically on startup.
