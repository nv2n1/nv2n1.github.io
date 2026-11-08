---
title: "How to Concatenate Multiple Video Files on Linux"
date: 2018-03-24 08:20:32 +0000
modified: 2026-04-12 16:08:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-concatenate-multiple-video-file-together-on-linux/
---

When you need to combine multiple video files (like video1.mp4, video2.mp4, and video3.mp4) into a single output file, FFmpeg is the standard tool on Linux. It’s faster, more reliable, and better maintained than older tools like mencoder.

## Using FFmpeg with the Concat Demuxer

The most robust approach uses FFmpeg’s concat demuxer, which properly handles file sequences without re-encoding.

First, create a text file listing your videos (concat_list.txt):

    file 'video1.mp4'
    file 'video2.mp4'
    file 'video3.mp4'

Then concatenate with:

``` bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy output.mp4
```

The `-c copy` option copies streams without re-encoding, preserving quality and speed.

**Important notes:**

- The `-safe 0` flag is needed if your file paths contain special characters or are absolute paths
- All input files should ideally have the same codec, resolution, and frame rate. If they don’t, FFmpeg will likely fail or produce unexpected results
- Use quotes around filenames if they contain spaces

## Quick Concatenation with the Concat Protocol

For files with identical properties, you can use the concat protocol directly:

``` bash
ffmpeg -i "concat:video1.mp4|video2.mp4|video3.mp4" -c copy output.mp4
```

This is faster but less reliable if files have any property differences.

## Re-encoding When Necessary

If your source files have mismatched codecs or resolutions, you’ll need to re-encode:

``` bash
ffmpeg -f concat -i concat_list.txt -c:v libx264 -preset fast -crf 23 -c:a aac output.mp4
```

This example uses H.264 video and AAC audio with moderate quality. Adjust `-crf` (0-51, lower is better) and `-preset` (ultrafast to veryslow) based on your needs.

## Handling Different Container Formats

If you’re mixing formats (.avi, .mkv, .mp4), first convert them to a common format:

``` bash
ffmpeg -i video1.avi -c copy video1.mp4
ffmpeg -i video2.mkv -c copy video2.mp4
```

Then concatenate the converted files using the concat demuxer.

## Common Issues

**Audio sync problems:** Re-encoding both video and audio together usually resolves this:

``` bash
ffmpeg -f concat -i concat_list.txt -c:v libx264 -c:a aac output.mp4
```

**File path errors:** Use absolute paths or `-safe 0`:

``` bash
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy output.mp4
```

**Duration detection fails:** Some formats need explicit re-encoding rather than stream copying, especially for certain AVI or MKV files.

## Installation

FFmpeg is in all major Linux distributions:

``` bash
# Debian/Ubuntu
sudo apt install ffmpeg

# RHEL/CentOS/Fedora
sudo dnf install ffmpeg

# Arch
sudo pacman -S ffmpeg
```

For best results with modern codecs and hardware acceleration, ensure you have a recent FFmpeg build (4.4+).

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
