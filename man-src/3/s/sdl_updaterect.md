---
title: "sdl_updaterect(3)"
name: "sdl_updaterect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_updaterect/"
description: "SDL_UpdateRect – Makes sure the given area is updated on the given screen."
---

<p>SDL_UpdateRect &#8211; Makes sure the given area is updated on the given screen.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_UpdateRect</code>(<code>SDL_Surface *screen, Sint32 x, Sint32 y, Sint32 w, Sint32 h</code>);</p>
<h2>Description</h2>
<p>Makes sure the given area is updated on the given screen. The rectangle must be confined within the screen boundaries (no clipping is done). </p>
<p> If &#8216;<code>x</code>&#8216;, &#8216;<code>y</code>&#8216;, &#8216;<code>w</code>&#8216; and &#8216;<code>h</code>&#8216; are all 0, <code>SDL_UpdateRect</code> will update the entire screen. </p>
<p> This function should not be called while &#8216;<code>screen</code>&#8216; is <i>locked</i>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_UpdateRects</code>, <i></i><code>SDL_Rect</code>, <i></i><code>SDL_Surface</code>, <i></i><code>SDL_LockSurface</code></p>
