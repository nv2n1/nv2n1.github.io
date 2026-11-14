---
title: "sdl_addtimer(3)"
name: "sdl_addtimer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_addtimer/"
description: "SDL_AddTimer – Add a timer which will call a callback after the specified number of milliseconds has elapsed."
---

<p>SDL_AddTimer &#8211; Add a timer which will call a callback after the specified number of milliseconds has elapsed.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> SDL_TimerID SDL_AddTimer</code>(<code>Uint32 interval, SDL_NewTimerCallback callback, void *param</code>);</p>
<h2>Callback</h2>
<pre>
<tt>/* type definition for the &quot;new&quot; timer callback function */
typedef Uint32 (*SDL_NewTimerCallback)(Uint32 interval, void *param);</tt>
</pre>
<h2>Description</h2>
<p> Adds a callback function to be run after the specified number of milliseconds has elapsed. The callback function is passed the current timer interval and the user supplied parameter from the <code>SDL_AddTimer</code> call and returns the next timer interval. If the returned value from the callback is the same as the one passed in, the periodic alarm continues, otherwise a new alarm is scheduled. </p>
<p> To cancel a currently running timer call <i>SDL_RemoveTimer</i> with the timer ID returned from <code>SDL_AddTimer</code>. </p>
<p> The timer callback function may run in a different thread than your main program, and so shouldn&#8217;t call any functions from within itself. You may always call <i>SDL_PushEvent</i>, however. </p>
<p> The granularity of the timer is platform-dependent, but you should count on it being at least 10 ms as this is the most common number. This means that if you request a 16 ms timer, your callback will run approximately 20 ms later on an unloaded system. If you wanted to set a flag signaling a frame update at 30 frames per second (every 33 ms), you might set a timer for 30 ms (see example below). If you use this function, you need to pass <code>SDL_INIT_TIMER</code> to <i>SDL_Init</i>.</p>
<h2>Return Value</h2>
<p> Returns an ID value for the added timer or <code>NULL</code> if there was an error.</p>
<h2>Examples</h2>
<pre>
<tt>my_timer_id = SDL_AddTimer((33/10)*10, my_callbackfunc, my_callback_param);</tt>
</pre>
<h2>See Also</h2>
<p> <i></i><code>SDL_RemoveTimer</code>, <i></i><code>SDL_PushEvent</code></p>
