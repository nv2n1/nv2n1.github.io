---
title: "sdl_getvideosurface(3)"
name: "sdl_getvideosurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getvideosurface/"
description: "SDL_GetVideoSurface – returns a pointer to the current display surface"
---

<p>SDL_GetVideoSurface &#8211; returns a pointer to the current display surface</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_GetVideoSurface</code>(<code>void</code>);</p>
<h2>Description</h2>
<p>This function returns a pointer to the current display surface. If SDL is doing format conversion on the display surface, this function returns the publicly visible surface, not the real video surface.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Surface</code></p>
