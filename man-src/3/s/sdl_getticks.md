---
title: "sdl_getticks(3)"
name: "sdl_getticks"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getticks/"
description: "SDL_GetTicks – Get the number of milliseconds since the SDL library initialization."
---

<p>SDL_GetTicks &#8211; Get the number of milliseconds since the SDL library initialization.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint32 SDL_GetTicks</code>(<code>void</code>)</p>
<h2>Description</h2>
<p>Get the number of milliseconds since the SDL library initialization. Note that this value wraps if the program runs for more than ~49 days.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_Delay</code></p>
