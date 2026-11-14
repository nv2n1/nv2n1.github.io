---
title: "sdl_getmousestate(3)"
name: "sdl_getmousestate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_getmousestate/"
description: "SDL_GetMouseState – Retrieve the current state of the mouse"
---

<p>SDL_GetMouseState &#8211; Retrieve the current state of the mouse</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> Uint8 SDL_GetMouseState</code>(<code>int *x, int *y</code>);</p>
<h2>Description</h2>
<p>The current button state is returned as a button bitmask, which can be tested using the <code>SDL_BUTTON(X)</code> macros, and <code>x</code> and <code>y</code> are set to the current mouse cursor position. You can pass <code>NULL</code> for either <code>x</code> or <code>y</code>.</p>
<h2>Example</h2>
<pre><tt>SDL_PumpEvents();
if(SDL_GetMouseState(NULL, NULL)&amp;<a href="//www.systutorials.com/docs/linux/man/1-SDL_BUTTON/">SDL_BUTTON</a>(1))
 printf(&quot;Mouse Button 1(left) is pressed.
&quot;);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_GetRelativeMouseState</code>, <i></i><code>SDL_PumpEvents</code></p>
