---
title: "sdl_getkeystate(3)"
name: "sdl_getkeystate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getkeystate/"
description: "SDL_GetKeyState – Get a snapshot of the current keyboard state"
---

<p>SDL_GetKeyState &#8211; Get a snapshot of the current keyboard state</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 *SDL_GetKeyState</code>(<code>int *numkeys</code>);</p>
<h2>Description</h2>
<p>Gets a snapshot of the current keyboard state. The current state is return as a pointer to an array, the size of this array is stored in <code>numkeys</code>. The array is indexed by the <i></i><code>SDLK_*</code> symbols. A value of 1 means the key is pressed and a value of 0 means its not. The pointer returned is a pointer to an internal SDL array and should not be freed by the caller. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> Use </code><i></i><code>SDL_PumpEvents</code> to update the state array.</dl>
<h2>Example</h2>
<pre><tt>Uint8 *keystate = SDL_GetKeyState(NULL);
if ( keystate[SDLK_RETURN] ) printf(&quot;Return Key Pressed.
&quot;);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL Key Symbols</code>, <i></i><code>SDL_PumpEvents</code></p>
