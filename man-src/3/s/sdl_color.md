---
title: "sdl_color(3)"
name: "sdl_color"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_color/"
description: "SDL_Color – Format independent color description"
---

<p>SDL_Color &#8211; Format independent color description</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Uint8 r;
 Uint8 g;
 Uint8 b;
 Uint8 unused;
} SDL_Color;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>r</code></p>
<dd>Red intensity</p>
<dt><code>g</code></p>
<dd>Green intensity</p>
<dt><code>b</code></p>
<dd>Blue intensity</p>
<dt><code>unused</code></p>
<dd>Unused</dl>
<h2>Description</h2>
<p><code>SDL_Color</code> describes a color in a format independent way. You can convert a <code>SDL_Color</code> to a pixel value for a certain pixel format using <i></i><code>SDL_MapRGB</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_PixelFormat</code>, <i></i><code>SDL_SetColors</code>, <i></i><code>SDL_Palette</code></p>
