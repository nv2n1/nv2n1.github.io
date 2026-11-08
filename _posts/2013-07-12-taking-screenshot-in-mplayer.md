---
title: "Taking Screenshots in MPlayer"
date: 2013-07-12 16:32:22 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/taking-screenshot-in-mplayer/
---

MPlayer reached end-of-life years ago. Its active fork, **mpv**, maintains all screenshot functionality with identical or simpler syntax. This guide covers mpv, which handles both single captures and burst sequences.

## Enable Screenshot Support

Screenshot support is built into mpv by default — no filter loading required. However, you can customize behavior by adding configuration to `~/.config/mpv/mpv.conf`:

``` ini
screenshot-format=png
screenshot-png-compression=9
screenshot-directory=~/Pictures/mpv-screenshots
```

## Take a Single Screenshot

Press `s` during playback to capture a frame. The screenshot saves immediately to your current working directory as `mpv-shot0001.png` (or your configured directory).

To take a screenshot without playing:

``` bash
mpv --no-audio --frames=1 --screenshot video.mp4
```

This extracts frame 1 and saves it.

## Capture at Specific Timestamps

Capture frames at exact times using `--screenshot-template`:

``` bash
mpv --no-audio video.mp4 --screenshot-template='frame-%02n' --ss 00:01:30 --frames=1
```

This grabs one frame at 1m 30s and names it `frame-01.png`.

## Take Continuous Screenshots

Press `S` during playback to start burst capture. Press `S` again to stop. mpv names them sequentially: `mpv-shot0001.png`, `mpv-shot0002.png`, etc.

**Warning:** This generates many files quickly. A 10-second burst at 30fps creates 300 images. Always monitor disk space and stop manually.

## Batch Extract Frames

To extract every Nth frame from a video:

``` bash
mpv --no-audio video.mp4 --screenshot-template='frame-%04n' --fps=5
```

This extracts 5 frames per second (one every 0.2 seconds) and saves them as `frame-0001.png`, `frame-0002.png`, etc.

For extracting all frames:

``` bash
mpv --no-audio video.mp4 --fps=30
```

This extracts every frame at the video’s native framerate.

## Configure Output Format

mpv supports PNG (default), WebP, and JPEG. Configure in `mpv.conf`:

``` ini
screenshot-format=webp
screenshot-webp-lossless=yes
```

Or pass options directly:

``` bash
mpv video.mp4 --screenshot-format=jpg --screenshot-jpeg-quality=90
```

## Customize Filenames

The `--screenshot-template` option controls naming. Available tokens:

- `%n` — sequence number (zero-padded)
- `%f` — current filename (without extension)
- `%wH`, `%wM`, `%wS` — hours, minutes, seconds into video
- `%{now}` — current system time

Example:

``` bash
mpv video.mp4 --screenshot-template='%f-%wH-%wM-%wS'
```

This produces names like `video-00-01-30.png` for a frame at 1m 30s.

## Save Screenshots to a Specific Directory

Create the directory first, then configure:

``` bash
mkdir -p ~/Videos/mpv-shots
mpv video.mp4 --screenshot-directory=~/Videos/mpv-shots
```

Or add to `mpv.conf`:

``` ini
screenshot-directory=~/Videos/mpv-shots
```

## Performance Considerations

- **PNG compression** (`screenshot-png-compression=0-9`) defaults to 9 but slows capture. Set to 6 for speed: `screenshot-png-compression=6`
- **WebP** is faster and smaller than PNG. For burst captures, use: `screenshot-format=webp`
- **JPEG** is fastest but lossy. For thumbnails: `screenshot-format=jpg` with `screenshot-jpeg-quality=85`

## View Recent Screenshots

After capturing, quickly view them:

``` bash
feh ~/Videos/mpv-shots/ &
```

Or open the directory in your file manager:

``` bash
xdg-open ~/Videos/mpv-shots/
```

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
