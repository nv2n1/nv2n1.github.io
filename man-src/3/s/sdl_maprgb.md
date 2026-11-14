---
title: "sdl_maprgb(3)"
name: "sdl_maprgb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_maprgb/"
description: "SDL_MapRGB – Map a RGB color value to a pixel format."
---

<p>SDL_MapRGB &#8211; Map a RGB color value to a pixel format.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint32 SDL_MapRGB</code>(<code>SDL_PixelFormat *fmt, Uint8 r, Uint8 g, Uint8 b</code>);</p>
<h2>Description</h2>
<p>Maps the RGB color value to the specified pixel format and returns the pixel value as a 32-bit int. </p>
<p> If the format has a palette (8-bit) the index of the closest matching color in the palette will be returned. </p>
<p> If the specified pixel format has an alpha component it will be returned as all 1 bits (fully opaque).</p>
<h2>Return Value</h2>
<p>A pixel value best approximating the given RGB color value for a given pixel format. If the pixel format bpp (color depth) is less than 32-bpp then the unused upper bits of the return value can safely be ignored (e.g., with a 16-bpp format the return value can be assigned to a <code>Uint16</code>, and similarly a <code>Uint8</code> for an 8-bpp format).</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetRGB</code>, <i></i><code>SDL_GetRGBA</code>, <i></i><code>SDL_MapRGBA</code>, <i></i><code>SDL_PixelFormat</code></p>
