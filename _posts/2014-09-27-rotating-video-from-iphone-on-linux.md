---
title: "Rotating iPhone Videos with FFmpeg on Linux"
date: 2014-09-27 09:25:42 +0000
modified: 2026-04-11 16:22:13 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /rotating-video-from-iphone-on-linux/
---

iPhone videos often play rotated 90 degrees when opened in non-Apple software on Linux because the rotation data is stored as metadata rather than baked into the video stream itself. FFmpeg handles this reliably by re-encoding with the transpose filter, which physically rotates the frame data.

## Understanding the Transpose Filter

FFmpeg’s transpose filter supports four transposition modes that combine rotation with optional flips:

- `0` = 90° counter-clockwise + vertical flip
- `1` = 90° clockwise
- `2` = 90° counter-clockwise
- `3` = 90° clockwise + vertical flip

For typical iPhone portrait videos that need 90° clockwise rotation, use transpose mode 1:

``` bash
ffmpeg -i input.mov -vf "transpose=1" -c:v libx264 -crf 23 output.mp4
```

The `-crf` value controls quality on a 0-51 scale (lower is better). CRF 23 is reasonable for general use and balances quality against file size.

## Checking Video Dimensions

Before rotating, check the input dimensions with ffprobe:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 input.mov
```

This outputs something like `1920x1080`. After a 90° rotation, dimensions swap to `1080x1920`. You can then decide whether to preserve the full resolution or scale down for distribution.

## Rotating with Correct Aspect Ratio

Explicitly scale the output to match the rotated dimensions. For a 1920×1080 input becoming 1080×1920 after rotation:

``` bash
ffmpeg -i input.mov -vf "transpose=1,scale=1080:1920" -c:v libx264 -crf 23 output.mp4
```

If you want to scale down for faster encoding or smaller files:

``` bash
ffmpeg -i input.mov -vf "transpose=1,scale=540:960" -c:v libx264 -crf 23 output.mp4
```

Scale dimensions should maintain the aspect ratio of the rotated video. Use this if you want FFmpeg to automatically adjust one dimension to avoid stretching:

``` bash
ffmpeg -i input.mov -vf "transpose=1,scale=1080:1920:force_original_aspect_ratio=decrease" -c:v libx264 -crf 23 output.mp4
```

## Quality Settings

Choose your CRF based on intended use:

- **CRF 18-22**: High quality, larger files. Use for archival or distribution requiring minimal degradation.
- **CRF 23-28**: Balanced quality and file size. Suitable for most general purposes.
- **CRF 28+**: Smaller files with visible quality loss. Use only when file size is critical.

For better compression with H.265 (HEVC), use libx265 with lower CRF:

``` bash
ffmpeg -i input.mov -vf "transpose=1,scale=1080:1920" -c:v libx265 -crf 18 output.mp4
```

H.265 offers roughly 40-50% better compression than H.264 at the same quality level, though encoding takes longer.

## Batch Processing Multiple Files

Rotate multiple iPhone videos in sequence:

``` bash
for file in *.mov; do
  ffmpeg -i "$file" -vf "transpose=1,scale=1080:1920" -c:v libx264 -crf 23 "${file%.mov}_rotated.mp4"
done
```

For parallel processing on multi-core systems, use GNU Parallel:

``` bash
find . -name "*.mov" | parallel ffmpeg -i {} -vf "transpose=1,scale=1080:1920" -c:v libx264 -crf 23 "{.}_rotated.mp4"
```

This speeds up batch operations significantly on systems with 4+ cores. Install with `apt install parallel` on Debian/Ubuntu or `brew install parallel` on macOS.

## Format and Codec Conversion

iPhone videos typically arrive as MOV files with H.264 encoding. Convert to MP4 with modern codecs for broader device compatibility:

``` bash
ffmpeg -i input.mov -vf "transpose=1" -c:v libx264 -c:a aac -b:a 128k output.mp4
```

For better compression with H.265:

``` bash
ffmpeg -i input.mov -vf "transpose=1" -c:v libx265 -c:a aac -b:a 128k output.mp4
```

Specify `-c:a aac` to ensure audio is encoded in a universally compatible format. Use `-c:a copy` if the source audio is already in AAC format and you want to skip re-encoding it.

## Handling Rotation Metadata

Some iPhone videos include rotation metadata that players should respect. Check for it:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream_side_data_list input.mov
```

If you see rotation metadata, you can copy the video without re-encoding and only update the metadata:

``` bash
ffmpeg -i input.mov -c copy -metadata:s:v rotate=0 output.mp4
```

However, this only modifies the metadata tag—it doesn’t visually rotate the frames. Many players still won’t display it correctly. The transpose filter method is more reliable because it performs actual frame rotation that works everywhere.

## Arbitrary Rotation Angles

For non-90° rotations, use the rotate filter instead:

``` bash
# Rotate 45 degrees
ffmpeg -i input.mov -vf "rotate=PI/4" output.mp4

# Rotate 30 degrees
ffmpeg -i input.mov -vf "rotate=PI/6" output.mp4
```

Angles are specified in radians. The rotate filter uses interpolation, so it’s slower than transpose for 90° increments. Stick with transpose when rotating by multiples of 90 degrees.

For 270° rotation (equivalent to counter-clockwise), use transpose=2:

``` bash
ffmpeg -i input.mov -vf "transpose=2,scale=1080:1920" -c:v libx264 -crf 23 output.mp4
```

## Verifying the Output

After rotation, verify the result plays correctly and has the expected dimensions:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration -of csv=p=0 output.mp4
```

If the rotated video still displays incorrectly in your player, check whether the player respects the metadata or frame-level rotation. VLC, mpv, and most modern browsers handle transposed frames correctly. Older media players or certain Android devices may still have issues with metadata-only rotation, making frame-level rotation via transpose the safest approach.
