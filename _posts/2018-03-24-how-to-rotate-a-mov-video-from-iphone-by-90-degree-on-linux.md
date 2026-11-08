---
title: "How to Rotate iPhone MOV Videos with FFmpeg on Linux"
date: 2018-03-24 11:42:35 +0000
layout: post
canonical: https://www.systutorials.com/how-to-rotate-a-mov-video-from-iphone-by-90-degree-on-linux/
---

iPhone videos often have rotation metadata embedded in the file rather than actual video frame rotation. This causes playback issues on Linux systems that don’t properly read the metadata. You’ll need to either apply the rotation during playback or permanently rotate the video frames.

## Understanding iPhone Video Rotation

iPhones store rotation information in the video container’s metadata using the `rotate` tag. Linux players sometimes ignore this metadata, making videos appear sideways. You have two options: rotate on playback or re-encode with rotation applied to the frames themselves.

## Option 1: Rotate During Playback

Most modern Linux video players can handle rotation metadata correctly, but if yours doesn’t, you can use FFmpeg with a filter.

Play with ffplay (part of FFmpeg):

``` bash
ffplay -vf "rotate=90*PI/180" video.mov
```

Or use VLC with a command-line filter:

``` bash
vlc --video-filter=rotate{angle=90} video.mov
```

For mpv (recommended for its reliability):

``` bash
mpv --vf=rotate=90 video.mov
```

Note: The rotation value depends on your video’s orientation. Use 90 for 90° clockwise, 180 for upside-down, 270 for 90° counter-clockwise.

## Option 2: Permanently Rotate and Save

This re-encodes the video with rotation applied to the actual frames. The video will display correctly on any player, but this takes longer and reduces quality slightly due to re-encoding.

Rotate 90° clockwise:

``` bash
ffmpeg -i video.mov -vf "rotate=90*PI/180" -c:a copy output.mov
```

Rotate 90° counter-clockwise:

``` bash
ffmpeg -i video.mov -vf "rotate=270*PI/180" -c:a copy output.mov
```

Rotate 180°:

``` bash
ffmpeg -i video.mov -vf "rotate=180*PI/180" -c:a copy output.mov
```

The `-c:a copy` flag preserves the audio without re-encoding, saving time and quality.

## Option 3: Fix Rotation Metadata (No Re-encoding)

If the rotation metadata is just wrong, fix it without re-encoding the video:

``` bash
ffmpeg -i video.mov -c copy -metadata:s:v:0 rotate=90 output.mov
```

This is the fastest option and preserves video quality. Players that respect rotation metadata will now display it correctly.

## Batch Rotating Multiple Videos

To rotate all MOV files in a directory:

``` bash
for file in *.mov; do
  ffmpeg -i "$file" -vf "rotate=90*PI/180" -c:a copy "rotated_$file"
done
```

Or for metadata-only rotation:

``` bash
for file in *.mov; do
  ffmpeg -i "$file" -c copy -metadata:s:v:0 rotate=90 "rotated_$file"
done
```

## Checking Rotation Metadata

Verify the current rotation metadata with:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream=rotation -of default=noprint_wrappers=1:nokey=1:nokey=1 video.mov
```

If it returns nothing or 0, the metadata isn’t set. If it returns 90, 180, or 270, the metadata exists.

## Performance Considerations

- **Metadata-only rotation**: Instant, no quality loss
- **Video filter rotation**: 1-2 minutes for 1GB file on modern hardware, slight quality loss from re-encoding
- **Playback filter**: No file changes, works immediately

For a one-time view, use playback filters. For sharing or archiving, use metadata rotation. For compatibility across all devices and players, use frame rotation.

## 2026 Best Practices and Advanced Techniques

For How to Rotate iPhone MOV Videos with FFmpeg on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
