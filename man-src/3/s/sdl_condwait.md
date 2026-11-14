---
title: "sdl_condwait(3)"
name: "sdl_condwait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_condwait/"
description: "SDL_CondWait – Wait on a condition variable"
---

<p>SDL_CondWait &#8211; Wait on a condition variable</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_CondWait</code>(<code>SDL_cond *cond, SDL_mutex *mut</code>);</p>
<h2>Description</h2>
<p>Wait on the condition variable <code>cond</code> and unlock the provided mutex. The mutex must the locked before entering this function. Returns <code>0</code> when it is signalled, or <code>-1</code> on an error.</p>
<h2>See Also</h2>
<p><i></i><code>SDL_CondWaitTimeout</code>, <i></i><code>SDL_CondSignal</code>, <i></i><code>SDL_mutexP</code></p>
