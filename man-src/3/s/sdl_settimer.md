---
title: "sdl_settimer(3)"
name: "sdl_settimer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_settimer/"
description: "SDL_SetTimer – Set a callback to run after the specified number of milliseconds has elapsed."
---

<p>SDL_SetTimer &#8211; Set a callback to run after the specified number of milliseconds has elapsed.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; </p>
<p> int SDL_SetTimer</code>(<code>Uint32 interval, SDL_TimerCallback callback</code>);</p>
<h2>Callback</h2>
<p>/* Function prototype for the timer callback function */ typedef Uint32 (*SDL_TimerCallback)(Uint32 interval);</p>
<h2>Description</h2>
<p>Set a callback to run after the specified number of milliseconds has elapsed. The callback function is passed the current timer interval and returns the next timer interval. If the returned value is the same as the one passed in, the periodic alarm continues, otherwise a new alarm is scheduled. </p>
<p> To cancel a currently running timer, call <code>SDL_SetTimer(0, NULL);</code> </p>
<p> The timer callback function may run in a different thread than your main constant, and so shouldn&#8217;t call any functions from within itself. </p>
<p> The maximum resolution of this timer is 10 ms, which means that if you request a 16 ms timer, your callback will run approximately 20 ms later on an unloaded system. If you wanted to set a flag signaling a frame update at 30 frames per second (every 33 ms), you might set a timer for 30 ms (see example below). </p>
<p> If you use this function, you need to pass <code>SDL_INIT_TIMER</code> to <code>SDL_Init()</code>. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> This function is kept for compatibility but has been superseded by the new timer functions </code><i>SDL_AddTimer</i> and <i>SDL_RemoveTimer</i> which support multiple timers.</dl>
<h2>Examples</h2>
<pre><tt>SDL_SetTimer((33/10)*10, my_callback);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_AddTimer</code></p>
