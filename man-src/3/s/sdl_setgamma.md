---
title: "sdl_setgamma(3)"
name: "sdl_setgamma"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setgamma/"
description: "SDL_SetGamma – Sets the color gamma function for the display"
---

<p>SDL_SetGamma &#8211; Sets the color gamma function for the display</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetGamma</code>(<code>float redgamma, float greengamma, float bluegamma</code>);</p>
<h2>Description</h2>
<p>Sets the &quot;gamma function&quot; for the display of each color component. Gamma controls the brightness/contrast of colors displayed on the screen. A gamma value of 1.0 is identity (i.e., no adjustment is made). </p>
<p> This function adjusts the gamma based on the &quot;gamma function&quot; parameter, you can directly specify lookup tables for gamma adjustment with <i>SDL_SetGammaRamp</i>. </p>
<p> Not all display hardware is able to change gamma.</p>
<h2>Return Value</h2>
<p>Returns -1 on error (or if gamma adjustment is not supported).</p>
<h2>See Also</h2>
<p><i>SDL_GetGammaRamp</i> <i>SDL_SetGammaRamp</i></p>
