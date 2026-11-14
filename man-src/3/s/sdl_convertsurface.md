---
title: "sdl_convertsurface(3)"
name: "sdl_convertsurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_convertsurface/"
description: "SDL_ConvertSurface – Converts a surface to the same format as another surface."
---

<p>SDL_ConvertSurface &#8211; Converts a surface to the same format as another surface.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL/SDL.h&quot; </p>
<p> SDL_Surface *SDL_ConvertSurface</code>(<code>SDL_Surface *src, SDL_PixelFormat *fmt, Uint32 flags</code>);</p>
<h2>Description</h2>
<p>Creates a new surface of the specified format, and then copies and maps the given surface to it. If this function fails, it returns <code>NULL</code>. </p>
<p> The <code>flags</code> parameter is passed to <i></i><code>SDL_CreateRGBSurface</code> and has those semantics. </p>
<p> This function is used internally by <i></i><code>SDL_DisplayFormat</code>. </p>
<p> This function can only be called after SDL_Init.</p>
<h2>Return Value</h2>
<p>Returns either a pointer to the new surface, or <code>NULL</code> on error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateRGBSurface</code>, <i></i><code>SDL_DisplayFormat</code>, <i></i><code>SDL_PixelFormat</code>, <i></i><code>SDL_Surface</code></p>
