---
title: "sdl_condbroadcast(3)"
name: "sdl_condbroadcast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_condbroadcast/"
description: "SDL_CondBroadcast – Restart all threads waiting on a condition variable"
---

<p>SDL_CondBroadcast &#8211; Restart all threads waiting on a condition variable</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_CondBroadcast</code>(<code>SDL_cond *cond</code>);</p>
<h2>Description</h2>
<p>Restarts all threads that are waiting on the condition variable, <code>cond</code>. Returns <code>0</code> on success, or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CondSignal</code>, <i></i><code>SDL_CondWait</code></p>
