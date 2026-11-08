---
title: "Converting AC3 and DTS Audio to AAC in MKV Files"
date: 2015-04-15 06:38:26 +0000
author: "David Yang"
layout: post
categories: [linux-systems-administration]
canonical: /getting-rid-dts-ac3-audio-using-ffmpeg-linux-play-mkv-files-ios-android/
---

MKV files encoded with AC3 or DTS audio won’t play sound on most iOS and Android devices. These are proprietary formats with licensing restrictions—mobile players either don’t support them or refuse to decode them by default. The video plays fine, but you get silence.

The solution is straightforward: re-encode the audio track to AAC or MP3 while keeping the video stream intact. This takes just a few seconds per file.

## Basic Conversion

For a single file, use ffmpeg to convert AC3/DTS audio to AAC:

``` bash
ffmpeg -i input.mkv -c:v copy -c:a aac -b:a 128k output.mkv
```

Breaking this down:

- `-c:v copy` — copy the video stream unchanged (no re-encoding)
- `-c:a aac` — encode audio to AAC codec
- `-b:a 128k` — set audio bitrate to 128 kbps (use 192k or 256k for higher quality)

AAC is preferred for mobile devices—it delivers better quality at lower bitrates than MP3. If you need MP3 for older device compatibility:

``` bash
ffmpeg -i input.mkv -c:v copy -c:a libmp3lame -b:a 192k output.mkv
```

## Check the Audio Codec First

Before converting, verify what codec you’re dealing with:

``` bash
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 input.mkv
```

This outputs just the codec name. If it shows `ac3` or `dts`, conversion is needed. For a more detailed view:

``` bash
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,codec_long_name,duration -of default=noprint_wrappers=1 input.mkv
```

## Batch Processing Multiple Files

For directories with many MKV files, create a simple bash script:

``` bash
#!/bin/bash

for file in *.mkv; do
    output="${file%.mkv}_converted.mkv"
    ffmpeg -i "$file" -c:v copy -c:a aac -b:a 128k "$output"
done
```

Save as `convert_audio.sh`, make it executable, and run in your media directory:

``` bash
chmod +x convert_audio.sh
./convert_audio.sh
```

For more precise control, use `find` to process files recursively:

``` bash
find . -name "*.mkv" -exec bash -c '
    for file; do
        output="${file%.mkv}_converted.mkv"
        ffmpeg -i "$file" -c:v copy -c:a aac -b:a 128k "$output"
    done
' _ {} +
```

## Handling Multiple Audio Tracks

If an MKV contains multiple audio tracks, specify which ones to convert:

``` bash
ffmpeg -i input.mkv -c:v copy -c:a:0 aac -c:a:1 copy output.mkv
```

This converts the first audio track to AAC and copies the second track unchanged. This is useful when you have both a surround track (AC3) and a stereo track (already compatible).

To copy all audio tracks without re-encoding:

``` bash
ffmpeg -i input.mkv -c:v copy -c:a copy output.mkv
```

This is fast but won’t solve AC3/DTS compatibility issues.

To see all audio tracks before processing:

``` bash
ffprobe -v error -select_streams a -show_entries stream=index,codec_name input.mkv
```

## Parallel Processing for Large Libraries

Audio encoding is CPU-light and typically takes just seconds per file. Speed up batch operations by running multiple ffmpeg instances in parallel using GNU parallel:

``` bash
find . -name "*.mkv" | parallel ffmpeg -i {} -c:v copy -c:a aac -b:a 128k {.}_converted.mkv
```

Limit parallel jobs with `-j`:

``` bash
find . -name "*.mkv" | parallel -j 4 ffmpeg -i {} -c:v copy -c:a aac -b:a 128k {.}_converted.mkv
```

Install parallel on Debian/Ubuntu with `sudo apt install parallel` or on RHEL/CentOS with `sudo dnf install parallel`.

## Verify the Output

After conversion, confirm the audio codec changed:

``` bash
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 output.mkv
```

Then test playback on your target device. Modern Android players (MX Player, VLC for Android) and iOS apps handle AAC natively.

## If Playback Still Fails

If the file still won’t play after audio conversion, the video codec itself may be incompatible. Check the video codec:

``` bash
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name input.mkv
```

If it’s HEVC/H.265 and your device is older, re-encode to H.264:

``` bash
ffmpeg -i input.mkv -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k output.mkv
```

This is significantly slower than audio-only conversion but ensures maximum device compatibility. Use `-preset fast` to speed things up at the cost of slightly larger files, or `-preset slow` for better compression.
