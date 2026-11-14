---
title: "sdl_creatergbsurfacefrom(3)"
name: "sdl_creatergbsurfacefrom"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_creatergbsurfacefrom/"
description: "SDL_CreateRGBSurfaceFrom – Create an SDL_Surface from pixel data"
---

<p>SDL_CreateRGBSurfaceFrom &#8211; Create an SDL_Surface from pixel data</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_CreateRGBSurfaceFrom</code>(<code>void *pixels, int width, int height, int depth, int pitch, Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask</code>);</p>
<h2>Description</h2>
<p>Creates an SDL_Surface from the provided pixel data. </p>
<p> The data stored in <code>pixels</code> is assumed to be of the <code>depth</code> specified in the parameter list. The pixel data is not copied into the <code>SDL_Surface</code> structure so it should not be freed until the surface has been freed with a called to <i>SDL_FreeSurface</i>. <code>pitch</code> is the length of each scanline in bytes. </p>
<p> See <i></i><code>SDL_CreateRGBSurface</code> for a more detailed description of the other parameters.</p>
<h2>Return Value</h2>
<p>Returns the created surface, or <code>NULL</code> upon error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateRGBSurface</code>, <i></i><code>SDL_FreeSurface</code></p>
