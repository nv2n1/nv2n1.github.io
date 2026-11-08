---
title: "Convert FLV Videos to MP4 Using FFmpeg"
date: 2018-03-24 11:42:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-convert-flv-to-mp4-with-ffmpeg/
---

Converting FLV files to MP4 is straightforward with FFmpeg. The basic command takes just seconds:

``` bash
ffmpeg -i input.flv output.mp4
```

FFmpeg will automatically select suitable video and audio codecs for MP4 format. This works for most FLV files without additional configuration.

## Preserving original quality

If you want to skip re-encoding and copy the streams as-is, use the `copy` codec option:

``` bash
ffmpeg -i input.flv -vcodec copy -acodec copy output.mp4
```

This is much faster since it doesn’t re-encode. However, it only works if the codecs inside the FLV are compatible with MP4 containers. Common issues include:

- FLV with Sorenson Spark video codec (incompatible with MP4) — requires re-encoding
- FLV with unusual audio codecs — may need conversion

If the copy method fails, FFmpeg will tell you and you’ll need to re-encode.

## Common scenarios

**Re-encode with quality control:**

``` bash
ffmpeg -i input.flv -c:v libx264 -crf 23 -c:a aac -b:a 128k output.mp4
```

The `-crf` value ranges from 0–51 (lower = better quality, default 23). The `-b:a 128k` sets audio bitrate. Adjust these based on your quality needs and file size constraints.

**Batch convert multiple files:**

``` bash
for file in *.flv; do
  ffmpeg -i "$file" -c:v libx264 -c:a aac "${file%.flv}.mp4"
done
```

**Convert and optimize for streaming:**

``` bash
ffmpeg -i input.flv -c:v libx264 -preset medium -c:a aac -b:a 192k -movflags +faststart output.mp4
```

The `-movflags +faststart` moves the MP4 metadata to the beginning of the file, letting players start streaming immediately without downloading the entire file first.

## Checking codec compatibility

Before converting, check what’s actually in your FLV file:

``` bash
ffprobe input.flv
```

Look for the `Video:` and `Audio:` lines. If you see codecs like `flv1` (Sorenson Spark), you’ll need to re-encode rather than copy.

## Performance tips

- Use `-preset fast` or `-preset ultrafast` if speed matters more than quality
- Use `-preset slow` for better compression if you have time
- Add `-threads 0` to use all CPU cores (usually automatic)
- For very large files, consider two-pass encoding for optimal quality-to-size ratio:

``` bash
ffmpeg -i input.flv -c:v libx264 -b:v 1000k -pass 1 -an -f mp4 /dev/null
ffmpeg -i input.flv -c:v libx264 -b:v 1000k -pass 2 -c:a aac -b:a 128k output.mp4
```

FLV support in modern players is nearly gone, so converting to MP4 ensures compatibility across browsers, phones, and media players.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
