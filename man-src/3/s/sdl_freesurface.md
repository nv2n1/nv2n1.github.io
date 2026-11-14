---
title: "sdl_freesurface(3)"
name: "sdl_freesurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_freesurface/"
description: "SDL_FreeSurface – Frees (deletes) a SDL_Surface"
---

<p>SDL_FreeSurface &#8211; Frees (deletes) a SDL_Surface</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_FreeSurface</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p>Frees the resources used by a previously created <code>SDL_Surface</code>. If the surface was created using <i>SDL_CreateRGBSurfaceFrom</i> then the pixel data is not freed.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateRGBSurface</code> <i></i><code>SDL_CreateRGBSurfaceFrom</code></p>
