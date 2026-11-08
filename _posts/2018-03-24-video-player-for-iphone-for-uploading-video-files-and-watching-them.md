---
title: "How to Transfer Videos to iPhone on Linux"
date: 2018-03-24 11:41:32 +0000
modified: 2026-04-11 16:00:20 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /video-player-for-iphone-for-uploading-video-files-and-watching-them/
---

Getting video files from your Linux machine to an iPhone for offline viewing doesn’t require iTunes or complex workarounds. Here are the practical methods that actually work in 2026.

## Quick Upload via VLC’s WiFi Interface

VLC for iOS remains the most straightforward approach for occasional transfers. It’s free, open-source, and handles virtually any codec you throw at it.

**Setup:**

1.  Install VLC from the App Store
2.  Open VLC → Settings → Sharing via WiFi
3.  Toggle it on and note the IP address displayed (e.g., `http://192.168.1.105:8080`)
4.  From your Linux machine, open that address in any browser
5.  Drag and drop video files into the upload area

**Batch transfers with curl:**

``` bash
curl -F "file=@video.mkv" http://192.168.1.105:8080/upload
curl -F "file=@another_video.mp4" http://192.168.1.105:8080/upload
```

Replace the IP with your actual device address. This works reliably over local WiFi without needing any other software.

**For network shares:** VLC also supports SMB/NFS mounting if you want permanent access to a shared folder rather than one-time uploads.

## Transcode First if Needed

Not all codecs work smoothly on iOS. If videos won’t play, transcode to H.264 + AAC (the universal combo for Apple devices) using FFmpeg.

**Single file:**

``` bash
ffmpeg -i input.mkv -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k output.mp4
```

The `-crf` value controls quality (18-20 for high quality, 26-28 for smaller files; 23 is middle ground). `-preset medium` balances speed and compression—use `fast` if you’re in a hurry or `slow` for maximum compression.

**Batch convert a directory:**

``` bash
for file in *.mkv; do
  ffmpeg -i "$file" -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k "${file%.mkv}.mp4"
done
```

This converts all MKV files in the current directory to MP4, preserving original filenames.

## Alternative: Cloud Storage

If you prefer not to deal with local transfers, use cloud storage:

- Upload to Google Drive, Dropbox, or iCloud
- Access via the official app or iOS Files app
- Stream directly or download for offline viewing

This is simpler for occasional use but requires internet access and may have bandwidth limits.

## Premium Options

**Infuse** (\$10-15 one-time purchase) offers a polished interface with better codec support and hardware decoding on newer devices. It includes a web upload interface and integrates with Plex if you run a media server.

**Plex** (freemium) is worth considering if you have multiple devices or a growing video library. It acts as a media server, letting you stream or download to any device. Setup takes more time upfront but scales well.

**Jellyfin** (free, open-source) is the self-hosted alternative to Plex. Full control, no subscriptions, and you own your data. Steeper learning curve but powerful if you’re comfortable running services on Linux.

## Media Server Setup (Jellyfin/Plex)

If you transfer videos regularly or manage a media library, self-hosting pays off:

1.  Install Jellyfin or Plex on your Linux machine
2.  Point it to your video folder
3.  Install the app on iPhone
4.  Stream or download videos on-demand

Both handle transcoding automatically if needed, though this uses CPU. Jellyfin is leaner and respects your privacy; Plex is easier to set up but tracks usage.

## When to Use Each Method

- **One-off transfers, any codec:** VLC WiFi upload
- **Need to optimize file size:** FFmpeg transcode first, then VLC
- **Want a polished app:** Infuse
- **Managing a video library:** Jellyfin (open-source) or Plex (easier)
- **Cloud preference:** Google Drive or Dropbox

Start with VLC for simplicity. Only add complexity if your needs grow beyond occasional transfers.
