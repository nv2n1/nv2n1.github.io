---
title: "sdl_setcliprect(3)"
name: "sdl_setcliprect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setcliprect/"
description: "SDL_SetClipRect – Sets the clipping rectangle for a surface."
---

<p>SDL_SetClipRect &#8211; Sets the clipping rectangle for a surface.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_SetClipRect</code>(<code>SDL_Surface *surface, SDL_Rect *rect</code>);</p>
<h2>Description</h2>
<p>Sets the clipping rectangle for a surface. When this surface is the destination of a blit, only the area within the clip rectangle will be drawn into. </p>
<p> The rectangle pointed to by <code>rect</code> will be clipped to the edges of the surface so that the clip rectangle for a surface can never fall outside the edges of the surface. </p>
<p> If <code>rect</code> is <code>NULL</code> the clipping rectangle will be set to the full size of the surface.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetClipRect</code>, <i></i><code>SDL_BlitSurface</code>, <i></i><code>SDL_Surface</code></p>
