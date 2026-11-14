---
title: "sdl_cdplay(3)"
name: "sdl_cdplay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_cdplay/"
description: "SDL_CDPlay – Play a CD"
---

<p>SDL_CDPlay &#8211; Play a CD</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_CDPlay</code>(<code>SDL_CD *cdrom, int start, int length</code>);</p>
<h2>Description</h2>
<p>Plays the given <code>cdrom</code>, starting a frame <code>start</code> for <code>length</code> frames.</p>
<h2>Return Values</h2>
<p>Returns <code>0</code> on success, or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CDPlayTracks</code>, <i></i><code>SDL_CDStop</code></p>
