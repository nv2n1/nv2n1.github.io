---
title: "Essential MPlayer and Mencoder Commands"
date: 2013-07-12 16:32:08 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/useful-mplayermencoder-commands/
---

MPlayer and mencoder are obsolete. FFmpeg and mpv (the actively maintained fork of MPlayer) are the standard tools for video manipulation on Linux systems today. While some MPlayer syntax still works in mpv, FFmpeg is more performant, better documented, and handles modern codecs reliably.

This guide covers practical tasks using FFmpeg and mpv, with mpv commands included where appropriate.

## Extract Audio to WAV

Extract audio and convert to PCM/WAV format:

``` bash
ffmpeg -i video.avi -acodec pcm_s16le -ar 44100 audio.wav
```

For MP3 output:

``` bash
ffmpeg -i video.avi -acodec libmp3lame -q:a 2 audio.mp3
```

The `-q:a` flag controls quality (0-9, lower is better). Use `-q:a 2` for high quality.

## Create Video from Image Sequences

Preview JPEG sequence at 15fps:

``` bash
mpv "mf://*.jpg" --mf-fps=15
```

Create video from JPEG files:

``` bash
ffmpeg -framerate 15 -pattern_type glob -i "*.jpg" -c:v libx264 -pix_fmt yuv420p output.mp4
```

For higher quality or specific bitrate control:

``` bash
ffmpeg -framerate 15 -pattern_type glob -i "*.jpg" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p output.mp4
```

The `-crf` value ranges from 0-51 (lower = better quality). Use 18-28 for typical content.

## Extract Video Segment

Cut video from 6 seconds to 206 seconds (200 seconds duration):

``` bash
ffmpeg -i big-file.avi -ss 6 -t 200 -c:v copy -c:a copy output.avi
```

Use `-t` for duration (in seconds) rather than `-endpos`. For frame-accurate cutting without re-encoding:

``` bash
ffmpeg -i input.mp4 -ss 6 -t 200 -c copy output.mp4
```

## Transcode to H.264/H.265

Transcode to modern H.264 with reasonable quality:

``` bash
ffmpeg -i source.avi -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k output.mp4
```

For H.265 (hevc) with better compression:

``` bash
ffmpeg -i source.avi -c:v libx265 -preset medium -crf 23 -c:a aac -b:a 128k output.mp4
```

For specific bitrate control instead of CRF:

``` bash
ffmpeg -i source.avi -c:v libx264 -b:v 1000k -c:a aac -b:a 128k output.mp4
```

## Get Video Information

Inspect video properties:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name -of default=noprint_wrappers=1:nokey=1:noprint_sections=1 video.avi
```

For human-readable output:

``` bash
ffmpeg -i video.avi 2>&1 | grep -E "Duration|Stream"
```

Or use mpv to display detailed information:

``` bash
mpv --term-playing-msg='${duration}' video.avi
```

## Stream Audio Over SSH

Play audio from remote server:

``` bash
ssh user@example.com "cat audio.mp3" | mpv --cache=yes -
```

Or directly:

``` bash
mpv sftp://user@example.com/path/to/audio.mp3
```

## Stream from HTTP/FTP

Play files directly from remote sources:

``` bash
mpv http://example.com/file.mp4
mpv ftp://user:pass@example.com/file.mp4
```

FFmpeg can read from remote sources similarly:

``` bash
ffmpeg -i http://example.com/video.mp4 -c copy output.mp4
```

## Record Streaming Content

Download/record streaming media:

``` bash
ffmpeg -i rtsp://example.com/file -c copy -bsf:a aac_adtstoasc output.mp4
```

For RTMP streams:

``` bash
ffmpeg -rtmp_live live -i "rtmp://example.com/stream" -c copy output.mp4
```

## Batch Processing

Process multiple files with a loop:

``` bash
for file in *.avi; do
  ffmpeg -i "$file" -c:v libx264 -crf 23 -c:a aac "${file%.avi}.mp4"
done
```

Or with GNU Parallel for faster processing:

``` bash
find . -name "*.avi" | parallel ffmpeg -i {} -c:v libx264 -crf 23 -c:a aac {.}.mp4
```

## Common Codec Reference

- **H.264**: `libx264` – widely compatible, good compression
- **H.265/HEVC**: `libx265` – better compression, less compatible
- **VP9**: `libvpx-vp9` – open source, YouTube compatible
- **Audio AAC**: `aac` – widely supported
- **Audio Opus**: `libopus` – modern, efficient

For production work, prefer H.264 with AAC audio in MP4 container for maximum compatibility.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Essential MPlayer and Mencoder Commands with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Essential MPlayer and Mencoder Commands. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
