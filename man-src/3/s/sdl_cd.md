---
title: "sdl_cd(3)"
name: "sdl_cd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cd/"
description: "SDL_CD – CDROM Drive Information"
---

<p>SDL_CD &#8211; CDROM Drive Information</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 int id;
 CDstatus status;
 int numtracks;
 int cur_track;
 int cur_frame;
 SDL_CDtrack track[SDL_MAX_TRACKS+1];
} SDL_CD;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>id</code></p>
<dd>Private drive identifier</p>
<dt><code>status</code></p>
<dd>Drive <i>status</i></p>
<dt><code>numtracks</code></p>
<dd>Number of tracks on the CD</p>
<dt><code>cur_track</code></p>
<dd>Current track</p>
<dt><code>cur_frame</code></p>
<dd>Current frame offset within the track</p>
<dt><code>track</code>[SDL_MAX_TRACKS+1]</p>
<dd>Array of track descriptions. (see <i></i><code>SDL_CDtrack</code>)</dl>
<h2>Description</h2>
<p>An <code>SDL_CD</code> structure is returned by <i></i><code>SDL_CDOpen</code>. It represents an opened CDROM device and stores information on the layout of the tracks on the disc. </p>
<p> A frame is the base data unit of a CD. <code>CD_FPS</code> frames is equal to 1 second of music. SDL provides two macros for converting between time and frames: <code>FRAMES_TO_MSF(f, M,S,F)</code> and <code>MSF_TO_FRAMES</code>.</p>
<h2>Examples</h2>
<pre><tt>int min, sec, frame;
int frame_offset;
FRAMES_TO_MSF(cdrom-&gt;cur_frame, &amp;min, &amp;sec, &amp;frame);
printf(&quot;Current Position: %d minutes, %d seconds, %d frames
&quot;, min, sec, frame);
frame_offset=MSF_TO_FRAMES(min, sec, frame);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CDOpen</code>, <i></i><code>SDL_CDtrack</code></p>
