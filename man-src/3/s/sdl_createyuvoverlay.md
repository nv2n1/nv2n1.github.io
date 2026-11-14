---
title: "sdl_createyuvoverlay(3)"
name: "sdl_createyuvoverlay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createyuvoverlay/"
description: "SDL_CreateYUVOverlay – Create a YUV video overlay"
---

<p>SDL_CreateYUVOverlay &#8211; Create a YUV video overlay</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> SDL_Overlay *SDL_CreateYUVOverlay</code>(<code>int width, int height, Uint32 format, SDL_Surface *display</code>);</p>
<h2>Description</h2>
<p> <code>SDL_CreateYUVOverlay</code> creates a YUV overlay of the specified <code>width</code>, <code>height</code> and <code>format</code> (see <i></i><code>SDL_Overlay</code> for a list of available formats), for the provided <code>display</code>. A <i></i><code>SDL_Overlay</code> structure is returned. </p>
<p> The term &#8216;overlay&#8217; is a misnomer since, unless the overlay is created in hardware, the contents for the display surface underneath the area where the overlay is shown will be overwritten when the overlay is displayed.</p>
<h2>See Also</h2>
<p> <i></i><code>SDL_Overlay</code>, <i></i><code>SDL_DisplayYUVOverlay</code>, <i></i><code>SDL_FreeYUVOverlay</code></p>
