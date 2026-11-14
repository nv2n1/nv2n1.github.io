---
title: "sdl_condsignal(3)"
name: "sdl_condsignal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_condsignal/"
description: "SDL_CondSignal – Restart a thread wait on a condition variable"
---

<p>SDL_CondSignal &#8211; Restart a thread wait on a condition variable</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_CondSignal</code>(<code>SDL_cond *cond</code>);</p>
<h2>Description</h2>
<p>Restart one of the threads that are waiting on the condition variable, <code>cond</code>. Returns <code>0</code> on success of <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CondWait</code>, <i></i><code>SDL_CondBroadcast</code></p>
