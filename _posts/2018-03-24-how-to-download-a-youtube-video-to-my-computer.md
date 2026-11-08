---
title: "Download YouTube Videos with yt-dlp"
date: 2018-03-24 11:41:32 +0000
modified: 2026-04-11 16:00:22 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-download-a-youtube-video-to-my-computer/
---

The most reliable way to download YouTube videos is **yt-dlp**, a maintained fork of youtube-dl that handles modern YouTube changes. It works on Linux, macOS, and Windows.

## Installation

**Linux (Debian/Ubuntu):**

``` bash
sudo apt install yt-dlp
```

**Linux (Fedora/RHEL):**

``` bash
sudo dnf install yt-dlp
```

**macOS:**

``` bash
brew install yt-dlp
```

**Windows or any system with Python 3.9+:**

``` bash
pip install yt-dlp
```

Keep it updated to handle YouTube’s frequent API changes:

``` bash
pip install --upgrade yt-dlp
```

## Basic Download

Download a video in best available quality:

``` bash
yt-dlp https://www.youtube.com/watch?v=VIDEO_ID
```

This merges video and audio into a single file (typically .webm or .mp4).

## Common Downloads

**Audio only (MP3):**

``` bash
yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=VIDEO_ID
```

**List available formats:**

``` bash
yt-dlp -F https://www.youtube.com/watch?v=VIDEO_ID
```

This shows resolution, bitrate, and format codes. Example output:

    [youtube] Extracting video information
    Format ID  | Extension | Resolution | FPS | Video Codec    | Audio Codec | Audio Bitrate
    18         | mp4       | 640x360    |     | h.264          | aac         | 96k
    22         | mp4       | 1280x720   |     | h.264          | aac         | 128k

**Download specific quality (e.g., 1080p with best audio):**

``` bash
yt-dlp -f "bestvideo[height<=1080]+bestaudio/best" https://www.youtube.com/watch?v=VIDEO_ID
```

**Download entire playlist:**

``` bash
yt-dlp https://www.youtube.com/playlist?list=PLAYLIST_ID
```

**Custom filename:**

``` bash
yt-dlp -o "%(uploader)s - %(title)s.%(ext)s" https://www.youtube.com/watch?v=VIDEO_ID
```

Useful template variables:

- `%(title)s` — Video title
- `%(uploader)s` — Channel name
- `%(upload_date)s` — Upload date (YYYYMMDD)
- `%(duration)s` — Duration in seconds
- `%(ext)s` — File extension

**Limit download speed (useful on shared connections):**

``` bash
yt-dlp -r 2M https://www.youtube.com/watch?v=VIDEO_ID
```

**Download to specific directory:**

``` bash
yt-dlp -o ~/Videos/%(title)s.%(ext)s https://www.youtube.com/watch?v=VIDEO_ID
```

## Age-Restricted and Authenticated Content

For age-restricted videos, pull authentication from your browser:

``` bash
yt-dlp --cookies-from-browser firefox https://www.youtube.com/watch?v=VIDEO_ID
```

Works with `firefox`, `chrome`, `chromium`, `edge`, and others. Make sure you’re logged in to YouTube in that browser first.

## Live Streams

Record a live stream as it happens:

``` bash
yt-dlp --wait-for-video 3600 https://www.youtube.com/watch?v=VIDEO_ID
```

This polls for the scheduled stream every 3600 seconds until it starts; the value is the retry interval, not a total wait limit. Once recording begins, it continues until the stream ends.

For already-completed streams (VODs), download normally:

``` bash
yt-dlp https://www.youtube.com/watch?v=VIDEO_ID
```

## Batch Processing

Create a file `urls.txt` with one URL per line:

    https://www.youtube.com/watch?v=ID1
    https://www.youtube.com/watch?v=ID2
    https://www.youtube.com/playlist?list=PLAYLIST_ID

Download all at once:

``` bash
yt-dlp -a urls.txt
```

## Subtitle Handling

Download subtitles automatically:

``` bash
yt-dlp --write-subs https://www.youtube.com/watch?v=VIDEO_ID
```

Download specific subtitle language:

``` bash
yt-dlp --write-subs --sub-langs en https://www.youtube.com/watch?v=VIDEO_ID
```

Download all available subtitles:

``` bash
yt-dlp --write-subs --sub-langs all https://www.youtube.com/watch?v=VIDEO_ID
```

## Configuration File

Create persistent settings in `~/.config/yt-dlp/config`:

    # Best quality, merged into MP4
    -f bestvideo+bestaudio/best
    --merge-output-format mp4

    # Save location and naming
    -o ~/Videos/%(uploader)s/%(title)s.%(ext)s

    # Auto-download subtitles
    --write-subs
    --sub-langs en

    # Metadata
    --write-info-json
    --write-description

    # Throttle on slow connections
    -r 1.5M

Now run just `yt-dlp URL` and all settings apply automatically.

## Post-Processing with FFmpeg

Convert or re-encode during download (requires ffmpeg installed):

``` bash
yt-dlp --postprocessor-args "-c:v libx265 -crf 28" https://www.youtube.com/watch?v=VIDEO_ID
```

This re-encodes with H.265 (HEVC) at quality 28 for smaller file sizes. Higher CRF values = smaller files but lower quality.

Skip re-encoding and just remux to MP4:

``` bash
yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 https://www.youtube.com/watch?v=VIDEO_ID
```

## Troubleshooting

**“No video found” or extraction fails:**\
Update yt-dlp first — YouTube changes frequently:

``` bash
pip install --upgrade yt-dlp
```

Check if the video is still available, region-restricted, or requires login. Age-restricted videos need the `--cookies-from-browser` flag.

**Slow downloads:**\
Check your connection speed. Rate-limit with `-r` if you’re on a shared network. Download during off-peak hours if possible.

**ffmpeg errors:**\
If post-processing fails, install ffmpeg:

``` bash
sudo apt install ffmpeg  # Debian/Ubuntu
sudo dnf install ffmpeg  # Fedora
brew install ffmpeg      # macOS
```

**Permission denied when saving:**\
Verify the output directory exists and you have write permissions:

``` bash
mkdir -p ~/Videos
chmod 755 ~/Videos
```

## Why yt-dlp Over Web Services?

Online converters are unreliable, frequently break when YouTube updates, expose your viewing history to third parties, and may contain malware. yt-dlp keeps everything local, transparent, and under your control.
