---
title: "sdl_getrgba(3)"
name: "sdl_getrgba"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getrgba/"
description: "SDL_GetRGBA – Get RGBA values from a pixel in the specified pixel format."
---

<p>SDL_GetRGBA &#8211; Get RGBA values from a pixel in the specified pixel format.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_GetRGBA</code>(<code>Uint32 pixel, SDL_PixelFormat *fmt, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a</code>);</p>
<h2>Description</h2>
<p>Get RGBA component values from a pixel stored in the specified pixel format. </p>
<p> This function uses the entire 8-bit [0..255] range when converting color components from pixel formats with less than 8-bits per RGB component (e.g., a completely white pixel in 16-bit RGB565 format would return [0xff, 0xff, 0xff] not [0xf8, 0xfc, 0xf8]). </p>
<p> If the surface has no alpha component, the alpha will be returned as 0xff (100% opaque).</p>
<h2>See Also</h2>
<p><i>SDL_GetRGB</i>, <i>SDL_MapRGB</i>, <i>SDL_MapRGBA</i>, <i>SDL_PixelFormat</i></p>
