---
title: "sdl_overlay(3)"
name: "sdl_overlay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_overlay/"
description: "SDL_Overlay – YUV video overlay"
---

<p>SDL_Overlay &#8211; YUV video overlay</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint32 format;
 int w, h;
 int planes;
 Uint16 *pitches;
 Uint8 **pixels;
 Uint32 hw_overlay:1;
} SDL_Overlay;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>format</code></p>
<dd>Overlay format (see below)</p>
<dt><code>w, h</code></p>
<dd>Width and height of overlay</p>
<dt><code>planes</code></p>
<dd>Number of planes in the overlay. Usually either 1 or 3</p>
<dt><code>pitches</code></p>
<dd>An array of pitches, one for each plane. Pitch is the length of a row in bytes.</p>
<dt><code>pixels</code></p>
<dd>An array of pointers to teh data of each plane. The overlay should be locked before these pointers are used.</p>
<dt><code>hw_overlay</code></p>
<dd>This will be set to 1 if the overlay is hardware accelerated.</dl>
<h2>Description</h2>
<p>A <code>SDL_Overlay</code> is similar to a <i></i><code>SDL_Surface</code> except it stores a YUV overlay. All the fields are read only, except for <code>pixels</code> which should be <i>locked</i> before use. The <code>format</code> field stores the format of the overlay which is one of the following: </p>
<pre><tt>#define SDL_YV12_OVERLAY 0x32315659 /* Planar mode: Y + V + U */
#define SDL_IYUV_OVERLAY 0x56555949 /* Planar mode: Y + U + V */
#define SDL_YUY2_OVERLAY 0x32595559 /* Packed mode: Y0+U0+Y1+V0 */
#define SDL_UYVY_OVERLAY 0x59565955 /* Packed mode: U0+Y0+V0+Y1 */
#define SDL_YVYU_OVERLAY 0x55595659 /* Packed mode: Y0+V0+Y1+U0 */</tt></pre>
<p>&nbsp;<wbr>More information on YUV formats can be found at&nbsp;<wbr><i><a rel="nofollow" href="http://www.webartz.com/fourcc/indexyuv.htm">http://www.webartz.com/fourcc/indexyuv.htm</a>&nbsp;<wbr>(link to URL&nbsp;<wbr><a href="http://www.webartz.com/fourcc/indexyuv.htm)">http://www.webartz.com/fourcc/indexyuv.htm)</a>&nbsp;<wbr></i>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateYUVOverlay</code>, <i></i><code>SDL_LockYUVOverlay</code>, <i></i><code>SDL_UnlockYUVOverlay</code>, <i></i><code>SDL_FreeYUVOverlay</code></p>
