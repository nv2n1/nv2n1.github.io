---
title: "sdl_rect(3)"
name: "sdl_rect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_rect/"
description: "SDL_Rect – Defines a rectangular area"
---

<p>SDL_Rect &#8211; Defines a rectangular area</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 Sint16 x, y;
 Uint16 w, h;
} SDL_Rect;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>x, y</code></p>
<dd>Position of the upper-left corner of the rectangle</p>
<dt><code>w, h</code></p>
<dd>The width and height of the rectangle</dl>
<h2>Description</h2>
<p>A <code>SDL_Rect</code> defines a rectangular area of pixels. It is used by <i></i><code>SDL_BlitSurface</code> to define blitting regions and by several other video functions.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_BlitSurface</code>, <i></i><code>SDL_UpdateRect</code></p>
