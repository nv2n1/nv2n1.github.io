---
title: "sdl_maprgba(3)"
name: "sdl_maprgba"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_maprgba/"
description: "SDL_MapRGBA – Map a RGBA color value to a pixel format."
---

<p>SDL_MapRGBA &#8211; Map a RGBA color value to a pixel format.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint32 SDL_MapRGBA</code>(<code>SDL_PixelFormat *fmt, Uint8 r, Uint8 g, Uint8 b, Uint8 a</code>);</p>
<h2>Description</h2>
<p>Maps the RGBA color value to the specified pixel format and returns the pixel value as a 32-bit int. </p>
<p> If the format has a palette (8-bit) the index of the closest matching color in the palette will be returned. </p>
<p> If the specified pixel format has no alpha component the alpha value will be ignored (as it will be in formats with a palette).</p>
<h2>Return Value</h2>
<p>A pixel value best approximating the given RGBA color value for a given pixel format. If the pixel format bpp (color depth) is less than 32-bpp then the unused upper bits of the return value can safely be ignored (e.g., with a 16-bpp format the return value can be assigned to a <code>Uint16</code>, and similarly a <code>Uint8</code> for an 8-bpp format).</p>
<h2>See Also</h2>
<p><i>SDL_GetRGB</i>, <i>SDL_GetRGBA</i>, <i>SDL_MapRGB</i>, <i>SDL_PixelFormat</i></p>
