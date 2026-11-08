---
title: "Installing FFmpeg on Linux Mint"
date: 2018-03-24 11:42:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-ffmpeg-on-linux-mint-17-qiana/
---

FFmpeg is essential for video and audio processing on Linux. Installation methods vary depending on your Linux Mint version and whether you want the stable release or cutting-edge builds.

## Installing FFmpeg from Official Repositories

The simplest approach is to use your distribution’s package manager. FFmpeg is now included in the official repositories for all modern Linux Mint versions:

``` bash
sudo apt update
sudo apt install ffmpeg
```

This installs a pre-built binary that’s stable and tested by your distribution maintainers. Check the installed version:

``` bash
ffmpeg -version
```

## Installing Latest FFmpeg from PPA

If you need a more recent version than what’s in the official repositories, use the FFmpeg maintainers’ PPA:

``` bash
sudo add-apt-repository ppa:savoury1/ffmpeg6
sudo apt update
sudo apt install ffmpeg
```

The `savoury1/ffmpeg6` PPA is actively maintained and provides newer builds than the default repositories while remaining compatible with your system. Replace `ffmpeg6` with newer versions as they become available (check the PPA page for current options).

## Compiling from Source

For maximum control or if you need specific codecs and libraries, compile FFmpeg directly:

``` bash
sudo apt install build-essential git yasm
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
cd ffmpeg
./configure --enable-gpl --enable-libx264 --enable-libx265 --enable-libvpx --enable-libopus
make -j$(nproc)
sudo make install
```

This enables common codecs (H.264, H.265, VP8/VP9, Opus). Add additional options for other codecs:

- `--enable-libmp3lame` for MP3 encoding
- `--enable-libfreetype` for subtitle handling
- `--enable-cuda` for NVIDIA hardware acceleration (requires CUDA toolkit)
- `--enable-nvenc` for NVIDIA hardware encoding

After compilation, verify the installation:

``` bash
ffmpeg -codecs | grep encoder
```

## Common FFmpeg Tasks

Once installed, here are practical examples:

**Convert video format:**

``` bash
ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4
```

**Extract audio:**

``` bash
ffmpeg -i video.mp4 -q:a 0 -map a audio.mp3
```

**Resize video:**

``` bash
ffmpeg -i input.mp4 -vf scale=1280:720 output.mp4
```

**Batch convert with hardware acceleration:**

``` bash
for file in *.mp4; do
  ffmpeg -hwaccel cuda -i "$file" -c:v hevc_nvenc -c:a aac "${file%.mp4}_converted.mp4"
done
```

## Troubleshooting

**Codec not available:** Run `ffmpeg -codecs` to list installed codecs. If missing, recompile with the appropriate `--enable-lib*` flags.

**Permission denied on `/usr/local/bin/ffmpeg`:** After `make install`, ensure the binary has proper permissions:

``` bash
sudo chmod +x /usr/local/bin/ffmpeg
```

**Out of memory during compilation:** Reduce parallel jobs:

``` bash
make -j2
```

## Why Repository Packages Change

Ubuntu and Linux Mint sometimes swap between FFmpeg and Libav based on maintenance resources and stability considerations. Modern distributions have standardized on FFmpeg due to its broader codec support and active development. The official repositories are now the recommended source for most users.

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
