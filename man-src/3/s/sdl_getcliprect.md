---
title: "sdl_getcliprect(3)"
name: "sdl_getcliprect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getcliprect/"
description: "SDL_GetClipRect – Gets the clipping rectangle for a surface."
---

<p>SDL_GetClipRect &#8211; Gets the clipping rectangle for a surface.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> void SDL_GetClipRect</code>(<code>SDL_Surface *surface, SDL_Rect *rect</code>);</p>
<h2>Description</h2>
<p> Gets the clipping rectangle for a surface. When this surface is the destination of a blit, only the area within the clip rectangle is drawn into. </p>
<p> The rectangle pointed to by <code>rect</code> will be filled with the clipping rectangle of the surface.</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_SetClipRect</code>, <i></i><code>SDL_BlitSurface</code>, <i></i><code>SDL_Surface</code></p>
