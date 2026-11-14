---
title: "sdl_semvalue(3)"
name: "sdl_semvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_semvalue/"
description: "SDL_SemValue – Return the current value of a semaphore."
---

<p>SDL_SemValue &#8211; Return the current value of a semaphore.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL/SDL_thread.h&quot; </p>
<p> Uint32 SDL_SemValue</code>(<code>SDL_sem *sem</code>);</p>
<h2>Description</h2>
<p><code>SDL_SemValue()</code> returns the current semaphore value from the semaphore pointed to by <code>sem</code>.</p>
<h2>Return Value</h2>
<p>Returns current value of the semaphore.</p>
<h2>Examples</h2>
<pre><tt> sem_value = SDL_SemValue(my_sem);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemPost</code></p>
