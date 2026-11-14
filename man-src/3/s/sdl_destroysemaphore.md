---
title: "sdl_destroysemaphore(3)"
name: "sdl_destroysemaphore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_destroysemaphore/"
description: "SDL_DestroySemaphore – Destroys a semaphore that was created by SDL_CreateSemaphore."
---

<p>SDL_DestroySemaphore &#8211; Destroys a semaphore that was created by <i>SDL_CreateSemaphore</i>.</p>
<h2>Synopsis</h2>
<p> <code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> void SDL_DestroySemaphore</code>(<code>SDL_sem *sem</code>);</p>
<h2>Description</h2>
<p> <code>SDL_DestroySemaphore</code> destroys the semaphore pointed to by <code>sem</code> that was created by <i></i><code>SDL_CreateSemaphore</code>. It is not safe to destroy a semaphore if there are threads currently blocked waiting on it.</p>
<h2>Examples</h2>
<pre>
<tt>if (my_sem != NULL) {
        SDL_DestroySemaphore(my_sem);
        my_sem = NULL;
}</tt>
</pre>
<h2>See Also</h2>
<p> <i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemPost</code>, <i></i><code>SDL_SemValue</code></p>
