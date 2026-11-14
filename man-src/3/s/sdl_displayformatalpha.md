---
title: "sdl_displayformatalpha(3)"
name: "sdl_displayformatalpha"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_displayformatalpha/"
description: "SDL_DisplayFormatAlpha – Convert a surface to the display format"
---

<p>SDL_DisplayFormatAlpha &#8211; Convert a surface to the display format</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> SDL_Surface *SDL_DisplayFormatAlpha</code>(<code>SDL_Surface *surface</code>);</p>
<h2>Description</h2>
<p> This function takes a surface and copies it to a new surface of the pixel format and colors of the video framebuffer plus an alpha channel, suitable for fast blitting onto the display surface. It calls <i>SDL_ConvertSurface</i> </p>
<p> If you want to take advantage of hardware colorkey or alpha blit acceleration, you should set the colorkey and alpha value before calling this function. </p>
<p> This function can be used to convert a colourkey to an alpha channel, if the <code>SDL_SRCCOLORKEY</code> flag is set on the surface. The generated surface will then be transparent (alpha=0) where the pixels match the colourkey, and opaque (alpha=255) elsewhere.</p>
<h2>Return Value</h2>
<p> If the conversion fails or runs out of memory, it returns <code>NULL</code></p>
<h2>See Also</h2>
<p> <i>SDL_ConvertSurface</i>, <i>SDL_SetAlpha</i>, <i>SDL_SetColorKey</i>, <i>SDL_DisplayFormat</i>, <i>SDL_Surface</i></p>
