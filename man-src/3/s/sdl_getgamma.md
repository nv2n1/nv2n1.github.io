---
title: "sdl_getgamma(3)"
name: "sdl_getgamma"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getgamma/"
description: "SDL_GetGamma – Gets the gamma of the display"
---

<p>SDL_GetGamma &#8211; Gets the gamma of the display</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_GetGamma</code>(<code>float *red, float *green, float *blue</code>);</p>
<h2>Description</h2>
<p>Gets the color gamma of the display. The gamma value for each color component will be place in the parameters <code>red</code>, <code>green</code> and <code>blue</code>. The values can range from 0.1 to 10. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> This function currently only works on XFreee 4.0 and up.</dl>
<p> </code></p>
<h2>See Also</h2>
<p><i></i><code>SDL_SetGamma</code>, <i></i><code>SDL_SetVideoMode</code></p>
