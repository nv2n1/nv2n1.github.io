---
title: "sdl_removetimer(3)"
name: "sdl_removetimer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_removetimer/"
description: "SDL_RemoveTimer – Remove a timer which was added with SDL_AddTimer."
---

<p>SDL_RemoveTimer &#8211; Remove a timer which was added with <i>SDL_AddTimer</i>.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; </p>
<p> SDL_bool SDL_RemoveTimer</code>(<code>SDL_TimerID id</code>);</p>
<h2>Description</h2>
<p> Removes a timer callback previously added with <i>SDL_AddTimer</i>.</p>
<h2>Return Value</h2>
<p> Returns a boolean value indicating success.</p>
<h2>Examples</h2>
<pre>
<tt>SDL_RemoveTimer(my_timer_id);</tt>
</pre>
<h2>See Also</h2>
<p> <i></i><code>SDL_AddTimer</code></p>
