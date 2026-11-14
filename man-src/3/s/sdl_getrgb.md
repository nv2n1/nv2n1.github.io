---
title: "sdl_getrgb(3)"
name: "sdl_getrgb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getrgb/"
description: "SDL_GetRGB – Get RGB values from a pixel in the specified pixel format."
---

<p>SDL_GetRGB &#8211; Get RGB values from a pixel in the specified pixel format.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_GetRGB</code>(<code>Uint32 pixel, SDL_PixelFormat *fmt, Uint8 *r, Uint8 *g, Uint8 *b</code>);</p>
<h2>Description</h2>
<p>Get RGB component values from a pixel stored in the specified pixel format. </p>
<p> This function uses the entire 8-bit [0..255] range when converting color components from pixel formats with less than 8-bits per RGB component (e.g., a completely white pixel in 16-bit RGB565 format would return [0xff, 0xff, 0xff] not [0xf8, 0xfc, 0xf8]).</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetRGBA</code>, <i></i><code>SDL_MapRGB</code>, <i></i><code>SDL_MapRGBA</code>, <i></i><code>SDL_PixelFormat</code></p>
