---
title: "sdl_setcolorkey(3)"
name: "sdl_setcolorkey"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setcolorkey/"
description: "SDL_SetColorKey – Sets the color key (transparent pixel) in a blittable surface and RLE acceleration."
---

<p>SDL_SetColorKey &#8211; Sets the color key (transparent pixel) in a blittable surface and RLE acceleration.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetColorKey</code>(<code>SDL_Surface *surface, Uint32 flag, Uint32 key</code>);</p>
<h2>Description</h2>
<p>&nbsp;<wbr>Sets the color key&nbsp;<wbr>(transparent pixel)&nbsp;<wbr>in a blittable surface and enables or disables RLE blit acceleration. </p>
<p> RLE acceleration can substantially speed up blitting of images with large horizontal runs of transparent pixels (i.e., pixels that match the <code>key</code> value). The <code>key</code> must be of the same pixel format as the <code>surface</code>, <i></i><code>SDL_MapRGB</code> is often useful for obtaining an acceptable value. </p>
<p> If <code>flag</code> is <code>SDL_SRCCOLORKEY</code> then <code>key</code> is the transparent pixel value in the source image of a blit. </p>
<p> If <code>flag</code> is OR&#8217;d with <code>SDL_RLEACCEL</code> then the surface will be draw using RLE acceleration when drawn with <i>SDL_BlitSurface</i>. The surface will actually be encoded for RLE acceleration the first time <i>SDL_BlitSurface</i> or <i>SDL_DisplayFormat</i> is called on the surface. </p>
<p> If <code>flag</code> is 0, this function clears any current color key.</p>
<h2>Return Value</h2>
<p>This function returns <code>0</code>, or <code>-1</code> if there was an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_BlitSurface</code>, <i></i><code>SDL_DisplayFormat</code>, <i></i><code>SDL_MapRGB</code>, <i></i><code>SDL_SetAlpha</code></p>
