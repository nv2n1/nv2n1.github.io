---
title: "sdl_condwaittimeout(3)"
name: "sdl_condwaittimeout"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_condwaittimeout/"
description: "SDL_CondWaitTimeout – Wait on a condition variable, with timeout"
---

<p>SDL_CondWaitTimeout &#8211; Wait on a condition variable, with timeout</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_CondWaitTimeout</code>(<code>SDL_cond *cond, SDL_mutex *mutex, Uint32 ms</code>);</p>
<h2>Description</h2>
<p>Wait on the condition variable <code>cond</code> for, at most, <code>ms</code> milliseconds. <code>mut</code> is unlocked so it must be locked when the function is called. Returns <code>SDL_MUTEX_TIMEDOUT</code> if the condition is not signalled in the allotted time, <code>0</code> if it was signalled or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CondWait</code></p>
