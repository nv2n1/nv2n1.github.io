---
title: "sdl_sempost(3)"
name: "sdl_sempost"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_sempost/"
description: "SDL_SemPost – Unlock a semaphore."
---

<p>SDL_SemPost &#8211; Unlock a semaphore.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_SemPost</code>(<code>SDL_sem *sem</code>);</p>
<h2>Description</h2>
<p><code>SDL_SemPost</code> unlocks the semaphore pointed to by <code>sem</code> and atomically increments the semaphores value. Threads that were blocking on the semaphore may be scheduled after this call succeeds. </p>
<p> <code>SDL_SemPost</code> should be called after a semaphore is locked by a successful call to <i>SDL_SemWait</i>, <i>SDL_SemTryWait</i> or <i>SDL_SemWaitTimeout</i>.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> if successful or <code>-1</code> if there was an error (leaving the semaphore unchanged).</p>
<h2>Examples</h2>
<pre><tt>SDL_SemPost(my_sem);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemValue</code></p>
