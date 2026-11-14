---
title: "sdl_cdstatus(3)"
name: "sdl_cdstatus"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdstatus/"
description: "SDL_CDStatus – Returns the current status of the given drive."
---

<p>SDL_CDStatus &#8211; Returns the current status of the given drive.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> CDstatus SDL_CDStatus</code>(<code>SDL_CD *cdrom</code>); <code>/* Given a status, returns true if there&#8217;s a disk in the drive */ #define CD_INDRIVE(status) ((int)status &gt; 0) </code></p>
<h2>Description</h2>
<p>This function returns the current status of the given drive. Status is described like so: </p>
<pre><tt>typedef enum {
 CD_TRAYEMPTY,
 CD_STOPPED,
 CD_PLAYING,
 CD_PAUSED,
 CD_ERROR = -1
} CDstatus;</tt></pre>
<p>If the drive has a CD in it, the table of contents of the CD and current play position of the CD will be stored in the SDL_CD structure. </p>
<p> The macro <code>CD_INDRIVE</code> is provided for convenience, and given a status returns true if there&#8217;s a disk in the drive. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> SDL_CDStatus</code> also updates the <i></i><code>SDL_CD</code> structure passed to it.</dl>
<h2>Example</h2>
<pre><tt>int playTrack(int track)
{
 int playing = 0;
 if ( CD_INDRIVE(SDL_CDStatus(cdrom)) ) {
 /* clamp to the actual number of tracks on the CD */
 if (track &gt;= cdrom-&gt;numtracks) {
 track = cdrom-&gt;numtracks-1;
 }
 if ( SDL_CDPlayTracks(cdrom, track, 0, 1, 0) == 0 ) {
 playing = 1;
 }
 }
 return playing;
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CD</code></p>
