---
title: "sdl_setgammaramp(3)"
name: "sdl_setgammaramp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setgammaramp/"
description: "SDL_SetGammaRamp – Sets the color gamma lookup tables for the display"
---

<p>SDL_SetGammaRamp &#8211; Sets the color gamma lookup tables for the display</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetGammaRamp</code>(<code>Uint16 *redtable, Uint16 *greentable, Uint16 *bluetable</code>);</p>
<h2>Description</h2>
<p>Sets the gamma lookup tables for the display for each color component. Each table is an array of 256 Uint16 values, representing a mapping between the input and output for that channel. The input is the index into the array, and the output is the 16-bit gamma value at that index, scaled to the output color precision. You may pass NULL to any of the channels to leave them unchanged. </p>
<p> This function adjusts the gamma based on lookup tables, you can also have the gamma calculated based on a &quot;gamma function&quot; parameter with <i>SDL_SetGamma</i>. </p>
<p> Not all display hardware is able to change gamma.</p>
<h2>Return Value</h2>
<p>Returns -1 on error (or if gamma adjustment is not supported).</p>
<h2>See Also</h2>
<p><i>SDL_SetGamma</i> <i>SDL_GetGammaRamp</i></p>
