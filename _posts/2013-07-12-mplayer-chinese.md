---
title: "MPlayer \u4e2d\u6587\u5b57\u5e55\u663e\u793a\u914d\u7f6e\u6307\u5357"
date: 2013-07-12 16:31:49 +0000
modified: 2026-04-12 16:11:09 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /mplayer-chinese/
---

MPlayer is largely unmaintained; **mpv** is the actively developed fork that replaced it. Most MPlayer subtitle commands work in mpv with minor syntax adjustments. This guide covers both.

## External Subtitle Files

### Handling Character Encoding

Chinese subtitle files often display as garbage when the player guesses the encoding wrong. Specify the correct codepage explicitly.

For an `.srt` file in GBK (Simplified Chinese):

``` bash
mpv "Gone with the Wind.avi" --sub-file="Gone.With.the.Wind.1939.Bluray.720p.DTS.2Audio.x264-CHD.chs.srt" --sub-codepage=cp936
```

Or with MPlayer (if you must):

``` bash
mplayer -ass -subcp cp936 "Gone with the Wind.avi" -sub "Gone.With.the.Wind.1939.Bluray.720p.DTS.2Audio.x264-CHD.chs.srt"
```

Common Chinese codepages:

- `cp936` / `gbk` — Simplified Chinese (most common)
- `cp950` / `big5` — Traditional Chinese

### Auto-loading Subtitles

Both mpv and MPlayer can automatically find and load matching subtitle files:

``` bash
mpv "Gone with the Wind.avi"
```

mpv searches for subtitles matching the video filename by default. For stricter control:

``` bash
mpv "Gone with the Wind.avi" --sub-auto=fuzzy
```

With MPlayer, use the `-sub-fuzziness` option:

``` bash
mplayer "Gone with the Wind.avi" -sub-fuzziness 1 -subcp cp936
```

Fuzziness levels:

- `0` — Exact filename match only
- `1` — Load all subtitles containing the video name
- `2` — Load all subtitles in the current directory

## Embedded Subtitles

For `.mkv`, `.ogm`, or other container formats with multiple subtitle streams, select the stream by ID.

First, list available subtitle streams:

``` bash
mpv "file.mkv" --sid=no
```

Then play with the desired subtitle stream (e.g., stream 1):

``` bash
mpv "file.mkv" --sid=1 --sub-codepage=cp936
```

Or with MPlayer:

``` bash
mplayer "file.mkv" -sid 1 -subcp cp936
```

## DVD Playback

For DVD content stored on disk:

``` bash
mpv dvd:// --dvd-device=/path/to/dvd --sid=1 --sub-codepage=cp936
```

With MPlayer:

``` bash
mplayer dvd://1 -dvd-device /path/to/dvd -sid 1 -subcp cp936
```

## Font Issues with ASS/SSA Subtitles

If subtitles render with wrong fonts or missing glyphs, explicitly enable fontconfig (mpv default) or point to a specific font:

``` bash
mpv "file.mkv" --sub-codepage=cp936 --sub-font="WenQuanYi Micro Hei"
```

For MPlayer, ensure `libass` support is compiled in:

``` bash
mplayer -ass -subfont-text-osize 3 "file.mkv" -sid 1 -subcp cp936
```

## Batch Processing

To convert all subtitles in a directory to UTF-8 (recommended for modern systems):

``` bash
for f in *.srt; do iconv -f cp936 -t utf-8 "$f" > "${f%.srt}_utf8.srt"; done
```

Then play without specifying codepage:

``` bash
mpv "video.avi" --sub-file="video_utf8.srt"
```

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
