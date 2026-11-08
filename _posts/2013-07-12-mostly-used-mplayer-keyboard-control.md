---
title: "Essential MPlayer Keyboard Shortcuts"
date: 2013-07-12 16:31:51 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/mostly-used-mplayer-keyboard-control/
---

MPlayer is largely unmaintained; **mpv** is the actively developed fork that handles 95% of these commands with compatible bindings. That said, if you’re still running MPlayer or need legacy support, here’s what you need to know.

MPlayer uses a fully configurable keyboard control layer. Most of these shortcuts work in mpv as well, though some have been renamed or require filter syntax adjustments. Check the <a href="https://mpv.io/manual/stable/" rel="nofollow noopener" target="_blank">mpv manual</a> for mpv-specific details.

## Playback Control

**p** or **space**\
: Pause/unpause playback.

**q** or **esc**\
: Stop and quit.

**u**\
: Stop playback (quit only if `-idle` not set).

**.** (period)\
: Frame-by-frame stepping. First press pauses; each subsequent press advances one frame. Any other key unpauses.

## Seeking

**← →** (left/right arrow)\
: Seek backward/forward 10 seconds.

**↑ ↓** (up/down arrow)\
: Seek forward/backward 1 minute.

**Page Up / Page Down**\
: Seek forward/backward 10 minutes.

**! @**\
: Seek to beginning of previous/next chapter.

## Playback Speed

**\[ \]**\
: Decrease/increase playback speed by 10%.

**{ }**\
: Halve/double playback speed.

**backspace**\
: Reset to normal speed.

## Playlist Navigation

**\< \>**\
: Previous/next file in playlist.

**Enter**\
: Next file (continues past end of playlist).

**Home / End**\
: Next/previous entry in parent playtree list.

## Volume and Audio

\*\*/ \* **or** 9 0\*\*\
: Decrease/increase volume.

**m**\
: Toggle mute.

**( )**\
: Adjust audio balance (favor left or right channel).

**+ –**\
: Adjust audio delay by ±0.1 seconds.

## Audio and Subtitle Tracks

**\#** (DVDs, MPEG, Matroska, AVI)\
: Cycle available audio tracks.

**\_** (MPEG-TS, AVI, libavformat)\
: Cycle available video tracks.

**v**\
: Toggle subtitle visibility.

**j**\
: Cycle through available subtitles.

**y g**\
: Step forward/backward in subtitle list.

**a**\
: Toggle subtitle alignment (top/middle/bottom).

**x z**\
: Adjust subtitle delay by ±0.1 seconds.

**r t**\
: Move subtitles up/down.

**f**\
: Toggle “forced subtitles” display.

## Display and Video

**f**\
: Toggle fullscreen.

**t**\
: Toggle always-on-top window.

**o**\
: Cycle OSD states (none → seek indicator → seek + timer → seek + timer + total time).

**d**\
: Cycle frame dropping (none → skip display → skip decoding).

**w e**\
: Decrease/increase pan-and-scan range.

**i**\
: Show filename on OSD.

**s** (requires `-vf screenshot`)\
: Take screenshot or start/stop continuous screenshot mode.

**d** (hardware video output: xvmc, vdpau, or software filters: yadif, kerndeint)\
: Activate/deactivate deinterlacer.

**a** (DVD playback)\
: Cycle through available DVD angles.

## Hardware-Accelerated Video Output

The following apply when using hardware acceleration (xv, vidix, mga) or software filters (`-vf eq`, `-vf eq2`, `-vf hue`):

**1 2**\
: Adjust contrast.

**3 4**\
: Adjust brightness.

**5 6**\
: Adjust hue.

**7 8**\
: Adjust saturation.

## Legacy GUI Mode

If MPlayer was compiled with GUI support, these keys take precedence:

**Enter**\
: Start playback.

**Esc**\
: Stop playback.

**l**\
: Load file.

**t**\
: Load subtitle.

**c**\
: Open skin browser.

**p**\
: Open playlist.

**r**\
: Open preferences.

## Modern Alternative: mpv

If starting fresh, use **mpv** instead. It’s faster, better maintained, and most keybindings are identical. The main differences:

- Screenshot: **s** (built-in, no filter needed)
- Cycle tracks: **\#** for audio, **\_** for video (same as MPlayer)
- Speed adjustment: **\[ \]** or **{ }** (same syntax)
- Deinterlacing: **d** toggles the `yadif` filter automatically

For full details, consult the <a href="https://www.mplayerhq.hu/design7/info.html" rel="nofollow noopener" target="_blank">MPlayer manual</a> or <a href="https://mpv.io/manual/stable/" rel="nofollow noopener" target="_blank">mpv documentation</a>.
