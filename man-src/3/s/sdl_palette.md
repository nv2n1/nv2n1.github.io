---
title: "sdl_palette(3)"
name: "sdl_palette"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_palette/"
description: "SDL_Palette – Color palette for 8-bit pixel formats"
---

<p>SDL_Palette &#8211; Color palette for 8-bit pixel formats</p>
<h2>Structure Definition</h2>
<pre><tt>typedef struct{
 int ncolors;
 SDL_Color *colors;
} SDL_Palette;</tt></pre>
<h2>Structure Data</h2>
<dl COMPACT>
<dt><code>ncolors</code></p>
<dd>Number of colors used in this palette</p>
<dt><code>colors</code></p>
<dd>Pointer to <i></i><code>SDL_Color</code> structures that make up the palette.</dl>
<h2>Description</h2>
<p>Each pixel in an 8-bit surface is an index into the <code>colors</code> field of the <code>SDL_Palette</code> structure store in <i></i><code>SDL_PixelFormat</code>. A <code>SDL_Palette</code> should never need to be created manually. It is automatically created when SDL allocates a <code>SDL_PixelFormat</code> for a surface. The colors values of a <i></i><code>SDL_Surface</code>s palette can be set with the <i></i><code>SDL_SetColors</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Color</code>, <i></i><code>SDL_Surface</code>, <i></i><code>SDL_SetColors</code> <i></i><code>SDL_SetPalette</code></p>
