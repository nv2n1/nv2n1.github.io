---
title: "sdl_cdplaytracks(3)"
name: "sdl_cdplaytracks"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdplaytracks/"
description: "SDL_CDPlayTracks – Play the given CD track(s)"
---

<p>SDL_CDPlayTracks &#8211; Play the given CD track(s)</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_CDPlayTracks</code>(<code>SDL_CD *cdrom, int start_track, int start_frame, int ntracks, int nframes)</code>);</p>
<h2>Description</h2>
<p><code>SDL_CDPlayTracks</code> plays the given CD starting at track <code>start_track</code>, for <code>ntracks</code> tracks. </p>
<p> <code>start_frame</code> is the frame offset, from the beginning of the <code>start_track</code>, at which to start. <code>nframes</code> is the frame offset, from the beginning of the last track (<code>start_track</code>+<code>ntracks</code>), at which to end playing. </p>
<p> <code>SDL_CDPlayTracks</code> should only be called after calling <i></i><code>SDL_CDStatus</code> to get track information about the CD. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Data tracks are ignored.</dl>
<p> </code></p>
<h2>Return Value</h2>
<p>Returns <code>0</code>, or <code>-1</code> if there was an error.</p>
<h2>Examples</h2>
<pre><tt>/* assuming cdrom is a previously opened device */
/* Play the entire CD */
if(CD_INDRIVE(SDL_CDStatus(cdrom)))
 SDL_CDPlayTracks(cdrom, 0, 0, 0, 0);
/* Play the first track */
if(CD_INDRIVE(SDL_CDStatus(cdrom)))
 SDL_CDPlayTracks(cdrom, 0, 0, 1, 0);
/* Play first 15 seconds of the 2nd track */
if(CD_INDRIVE(SDL_CDStatus(cdrom)))
 SDL_CDPlayTracks(cdrom, 1, 0, 0, CD_FPS*15);</tt></pre>
<p>&nbsp;<wbr></p>
<h2>See Also</h2>
<p><i></i><code>SDL_CDPlay</code>, <i></i><code>SDL_CDStatus</code>, <i></i><code>SDL_CD</code></p>
