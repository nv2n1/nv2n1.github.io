---
title: "sdl_setmodstate(3)"
name: "sdl_setmodstate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_setmodstate/"
description: "SDL_SetModState – Set the current key modifier state"
---

<p>SDL_SetModState &#8211; Set the current key modifier state</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> void SDL_SetModState</code>(<code>SDLMod modstate</code>);</p>
<h2>Description</h2>
<p>The inverse of <i></i><code>SDL_GetModState</code>, <code>SDL_SetModState</code> allows you to impose modifier key states on your application. </p>
<p> Simply pass your desired modifier states into <code>modstate</code>. This value my be a logical OR&#8217;d combination of the following: </p>
<pre><tt>typedef enum {
 KMOD_NONE = 0x0000,
 KMOD_LSHIFT= 0x0001,
 KMOD_RSHIFT= 0x0002,
 KMOD_LCTRL = 0x0040,
 KMOD_RCTRL = 0x0080,
 KMOD_LALT = 0x0100,
 KMOD_RALT = 0x0200,
 KMOD_LMETA = 0x0400,
 KMOD_RMETA = 0x0800,
 KMOD_NUM = 0x1000,
 KMOD_CAPS = 0x2000,
 KMOD_MODE = 0x4000,
} SDLMod;</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_GetModState</code></p>
