---
title: "sdl_displayformat(3)"
name: "sdl_displayformat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_displayformat/"
description: "SDL_DisplayFormat – Convert a surface to the display format"
---

<p>SDL_DisplayFormat &#8211; Convert a surface to the display format</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_DisplayFormat</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p> This function takes a surface and copies it to a new surface of the pixel format and colors of the video framebuffer, suitable for fast blitting onto the display surface. It calls <i>SDL_ConvertSurface</i> </p>
<p> If you want to take advantage of hardware colorkey or alpha blit acceleration, you should set the colorkey and alpha value before calling this function. </p>
<p> If you want an alpha channel, see <i>SDL_DisplayFormatAlpha</i>.</p>
<h2>Return Value</h2>
<p> If the conversion fails or runs out of memory, it returns <code>NULL</code></p>
<h2>See Also</h2>
<p> <i></i><code>SDL_ConvertSurface</code>, <i></i><code>SDL_DisplayFormatAlpha</code> <i></i><code>SDL_SetAlpha</code>, <i></i><code>SDL_SetColorKey</code>, <i></i><code>SDL_Surface</code></p>
