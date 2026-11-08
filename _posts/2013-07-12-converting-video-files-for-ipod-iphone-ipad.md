---
title: "Convert Video Files for iPhone, iPad, and iPod"
date: 2013-07-12 16:32:27 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/converting-video-files-for-ipod-iphone-ipad/
---

Modern iOS devices handle a wider range of video formats natively, but if you’re working with legacy formats or need specific encoding for compatibility, conversion is straightforward with ffmpeg. This guide covers converting common video formats (.wmv, .mpg, .mkv, .webm, etc.) to .mp4 format suitable for Apple devices.

## Installing ffmpeg

On most modern Linux distributions, ffmpeg is available in the default repositories:

**Debian/Ubuntu:**

``` bash
apt install ffmpeg
```

**RHEL/CentOS/Fedora:**

``` bash
dnf install ffmpeg
```

**Arch:**

``` bash
pacman -S ffmpeg
```

Verify installation with `ffmpeg -version`.

## Basic Video Conversion

The simplest ffmpeg command converts any input format to .mp4:

``` bash
ffmpeg -i input.wmv output.mp4
```

ffmpeg automatically detects the input format and determines output format from the filename extension. You can convert to .mov as well:

``` bash
ffmpeg -i input.wmv output.mov
```

## Optimizing for Apple Devices

If you need to optimize file size or ensure compatibility with specific Apple devices, adjust the resolution and bitrate. Modern iPhones support up to 4K video, but older devices have lower limits. Example optimizations:

**For iPad (1080p target):**

``` bash
ffmpeg -i input.wmv -s 1920x1080 -b:v 2500k output.mp4
```

**For iPhone (720p target):**

``` bash
ffmpeg -i input.wmv -s 1280x720 -b:v 1500k output.mp4
```

**For older/smaller screens (480p target):**

``` bash
ffmpeg -i input.wmv -s 854x480 -b:v 1000k output.mp4
```

The `-s` flag sets frame size (width×height), and `-b:v` sets video bitrate. Higher bitrates improve quality but increase file size. Typical bitrates range from 500k (low quality) to 5000k (high quality).

## Handling Audio

Ensure audio is properly encoded. If you encounter audio sync issues, specify the audio codec explicitly:

``` bash
ffmpeg -i input.wmv -s 1280x720 -b:v 1500k -c:a aac -b:a 128k output.mp4
```

Use `-c:a aac` for AAC audio (widely compatible) or `-c:a libmp3lame` for MP3 (older devices). The `-b:a` flag controls audio bitrate; 128k is standard for most cases.

## Batch Conversion Script

For converting multiple files, create a reusable script:

``` bash
#!/bin/bash
# convert_video.sh - Convert video files to MP4 with specified resolution

if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <input_file> <output_file>"
    exit 1
fi

INPUT="$1"
OUTPUT="$2"
RESOLUTION="${3:-1280x720}"
BITRATE="${4:-1500k}"

ffmpeg -i "$INPUT" -s "$RESOLUTION" -b:v "$BITRATE" -c:a aac -b:a 128k "$OUTPUT"
```

Usage:

``` bash
chmod +x convert_video.sh
./convert_video.sh input.wmv output.mp4
./convert_video.sh input.mkv output.mp4 854x480 1000k
```

## Advanced Options

For better quality at smaller file sizes, use H.264 encoding explicitly with quality presets:

``` bash
ffmpeg -i input.wmv -c:v libx264 -preset slow -crf 23 -s 1280x720 -c:a aac output.mp4
```

- `-preset slow` uses slower encoding for better compression (options: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow)
- `-crf 23` sets quality (0-51, lower is better; 18-28 is typical)

For faster encoding at the cost of file size:

``` bash
ffmpeg -i input.wmv -c:v libx264 -preset fast -crf 28 -s 1280x720 -c:a aac output.mp4
```

## Hardware Acceleration

On systems with capable GPUs, enable hardware encoding for faster conversion:

``` bash
ffmpeg -i input.wmv -c:v h264_nvenc -b:v 1500k -s 1280x720 output.mp4
```

(NVIDIA GPUs; check `ffmpeg -codecs` for available hardware encoders on your system)

## Checking Conversion Progress

By default, ffmpeg shows conversion progress. For long files, you can estimate completion time from the output. To suppress unnecessary output, add `-loglevel warning`:

``` bash
ffmpeg -loglevel warning -i input.wmv -s 1280x720 -b:v 1500k output.mp4
```

Use `-progress pipe:1` to pipe progress to another script for automated monitoring in batch jobs.
