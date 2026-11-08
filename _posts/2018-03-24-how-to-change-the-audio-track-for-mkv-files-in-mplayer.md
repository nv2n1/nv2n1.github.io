---
title: "Switching Audio Tracks in MKV Files with MPlayer"
date: 2018-03-24 08:14:54 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-audio-track-for-mkv-files-in-mplayer/
---

MKV (Matroska) containers frequently contain multiple audio tracks. You can cycle through them during playback using keyboard shortcuts.

### Using mplayer

Press `#` to cycle through available audio tracks while the video is playing. This works for MKV, AVI, MPEG, and other container formats that mplayer supports.

``` bash
mplayer video.mkv
# Then press # during playback to switch tracks
```

You can also specify which audio track to play from the command line:

``` bash
mplayer -aid 1 video.mkv    # Play first audio track
mplayer -aid 2 video.mkv    # Play second audio track
```

The `-aid` option takes a 1-based track number. Use `mplayer -identify video.mkv` to list available audio tracks and their IDs.

### Modern alternatives

mplayer is largely unmaintained. Consider **mpv** instead — it’s actively developed, handles MKV better, and offers superior codec support:

``` bash
mpv video.mkv
# Press 'j' to cycle audio tracks during playback
```

Specify a track directly:

``` bash
mpv --aid=1 video.mkv
```

List all tracks before playing:

``` bash
mpv --sid=no video.mkv    # Show track info without playing
```

### Using ffmpeg to inspect or extract tracks

To see what audio tracks are in an MKV file:

``` bash
ffprobe -v error -select_streams a -show_entries stream=index,codec_name,language video.mkv
```

Extract a specific audio track:

``` bash
ffmpeg -i video.mkv -map 0:a:1 -c copy audio_track2.aac
```

Replace the audio track entirely:

``` bash
ffmpeg -i video.mkv -i new_audio.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mkv
```

### Using mkvtoolnix for direct MKV manipulation

If you need to permanently change which audio track plays by default, use mkvtoolnix:

``` bash
mkvpropedit video.mkv --edit track:a1 --set flag-default=1
mkvpropedit video.mkv --edit track:a2 --set flag-default=0
```

This sets track `a1` (first audio) as the default without re-encoding.

### VLC as a GUI option

If you prefer a graphical interface:

``` bash
vlc video.mkv
# Use Audio menu → Audio Track to switch
```

### Quick reference

| Tool       | Cycle tracks | Set track     | Extract track    |
|------------|--------------|---------------|------------------|
| mplayer    | `#` key      | `-aid 1`      | N/A (use ffmpeg) |
| mpv        | `j` key      | `--aid=1`     | N/A (use ffmpeg) |
| ffmpeg     | N/A          | N/A           | `-map 0:a:1`     |
| mkvtoolnix | N/A          | `mkvpropedit` | `mkvextract`     |

For most workflows, **mpv is the best choice** — it’s modern, actively maintained, and handles complex containers reliably.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
