---
title: "sdl_getrelativemousestate(3)"
name: "sdl_getrelativemousestate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getrelativemousestate/"
description: "SDL_GetRelativeMouseState – Retrieve the current state of the mouse"
---

<p>SDL_GetRelativeMouseState &#8211; Retrieve the current state of the mouse</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_GetRelativeMouseState</code>(<code>int *x, int *y</code>);</p>
<h2>Description</h2>
<p>The current button state is returned as a button bitmask, which can be tested using the <code>SDL_BUTTON(X)</code> macros, and <code>x</code> and <code>y</code> are set to the change in the mouse position since the last call to <code>SDL_GetRelativeMouseState</code> or since event initialization. You can pass <code>NULL</code> for either <code>x</code> or <code>y</code>.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_GetMouseState</code></p>
