---
title: "sdl_enablekeyrepeat(3)"
name: "sdl_enablekeyrepeat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_enablekeyrepeat/"
description: "SDL_EnableKeyRepeat – Set keyboard repeat rate."
---

<p>SDL_EnableKeyRepeat &#8211; Set keyboard repeat rate.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> int SDL_EnableKeyRepeat</code>(<code>int delay, int interval</code>);</p>
<h2>Description</h2>
<p> Enables or disables the keyboard repeat rate. <code>delay</code> specifies how long the key must be pressed before it begins repeating, it then repeats at the speed specified by <code>interval</code>. Both <code>delay</code> and <code>interval</code> are expressed in milliseconds. </p>
<p> Setting <code>delay</code> to 0 disables key repeating completely. Good default values are <code>SDL_DEFAULT_REPEAT_DELAY</code> and <i>SDL_DEFAULT_REPEAT_INTERVAL</i>.</p>
<h2>Return Value</h2>
<p> Returns <code>0</code> on success and <code>-1</code> on failure.</p>
