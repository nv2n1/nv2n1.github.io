---
title: "sdl_getgammaramp(3)"
name: "sdl_getgammaramp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getgammaramp/"
description: "SDL_GetGammaRamp – Gets the color gamma lookup tables for the display"
---

<p>SDL_GetGammaRamp &#8211; Gets the color gamma lookup tables for the display</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_GetGammaRamp</code>(<code>Uint16 *redtable, Uint16 *greentable, Uint16 *bluetable</code>);</p>
<h2>Description</h2>
<p>Gets the gamma translation lookup tables currently used by the display. Each table is an array of 256 Uint16 values. </p>
<p> Not all display hardware is able to change gamma.</p>
<h2>Return Value</h2>
<p>Returns -1 on error.</p>
<h2>See Also</h2>
<p><i>SDL_SetGamma</i> <i>SDL_SetGammaRamp</i></p>
