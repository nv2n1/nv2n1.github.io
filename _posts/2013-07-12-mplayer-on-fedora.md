---
title: "How to Install MPlayer and MEncoder on Fedora"
date: 2013-07-12 16:32:01 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /mplayer-on-fedora/
---

MPlayer and MEncoder are no longer actively maintained, but they’re still available through RPM Fusion if you need them for legacy content or specific workflows. Most users should consider modern alternatives like `mpv` (MPlayer’s successor) or `ffmpeg` for transcoding, but this guide covers the traditional setup.

### Enable RPM Fusion Repository

RPM Fusion hosts packages Fedora doesn’t include in its official repositories. Add both free and nonfree repos:

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

### Install MPlayer and MEncoder

Once RPM Fusion is enabled:

``` bash
sudo dnf install mplayer mencoder
```

Verify the installation:

``` bash
mplayer --version
mencoder -version
```

### Codec Support

Modern Fedora includes most codecs through FFmpeg dependencies, so manual codec installation is rarely necessary. If you encounter unsupported formats, first try upgrading your codec libraries:

``` bash
sudo dnf install ffmpeg
```

### Playing RMVB and Legacy Formats

RMVB files may require additional libraries. Install compatible C++ runtime libraries:

``` bash
sudo dnf install libstdc++ libstdc++-devel
```

Test playback with verbose output to diagnose issues:

``` bash
mplayer -v file.rmvb
```

### Common MPlayer Usage

Play a file with subtitles:

``` bash
mplayer -sub subtitle.srt video.mkv
```

Seek to a specific time (in seconds):

``` bash
mplayer -ss 120 video.mp4
```

Loop playback:

``` bash
mplayer -loop 0 file.mp3
```

### MEncoder for Transcoding

MEncoder is useful for batch conversions, though `ffmpeg` is generally preferred for new scripts. Convert AVI to MP4:

``` bash
mencoder input.avi -o output.mp4 -ovc lavc -lavcopts vcodec=mpeg4 -oac lavc -lavcopts acodec=aac
```

Extract audio from video:

``` bash
mencoder input.mkv -ovc copy -oac copy -of rawaudio -o audio.aac
```

Resize video during encoding:

``` bash
mencoder input.avi -o output.avi -vf scale=1280:720 -ovc lavc -oac copy
```

### Modern Alternatives

For new projects, consider these maintained tools:

- **mpv**: Modern MPlayer fork with better hardware acceleration and subtitle handling
- **ffmpeg**: Industry standard for encoding, decoding, and format conversion
- **HandBrake**: GUI-based video transcoder

Install mpv as an alternative:

``` bash
sudo dnf install mpv
```

### Troubleshooting

If MPlayer crashes or won’t play certain files:

1.  Check available codecs: `mplayer -ac help` and `mplayer -vc help`
2.  Try forcing a specific codec: `mplayer -ac mad file.mp3`
3.  Enable verbose logging: `mplayer -v file.mkv 2>&1 | tee debug.log`
4.  Consult `man mplayer` and `man mencoder` for full option documentation

## Troubleshooting Common Issues

If you encounter problems during installation, check these common solutions:

- Ensure your system packages are up to date before installing new software
- Check for conflicting packages that might prevent installation
- Verify network connectivity if downloading packages from external repositories
- Review system logs in /var/log/ for detailed error messages

## Verification Steps

After installation, verify everything is working correctly by checking the installed version and running basic functionality tests. Most command-line tools respond to the –version or -v flag to display their version information.

## Keeping Your Installation Updated

Regularly update your system to receive security patches and bug fixes. On Fedora, use dnf update. On Ubuntu and Debian, use apt update followed by apt upgrade. For software installed via language-specific package managers like pip, npm, or gem, check their respective update commands.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
