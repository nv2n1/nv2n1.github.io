---
title: "sdl_semwait(3)"
name: "sdl_semwait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_semwait/"
description: "SDL_SemWait – Lock a semaphore and suspend the thread if the semaphore value is zero."
---

<p>SDL_SemWait &#8211; Lock a semaphore and suspend the thread if the semaphore value is zero.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_SemWait</code>(<code>SDL_sem *sem</code>);</p>
<h2>Description</h2>
<p><code>SDL_SemWait()</code> suspends the calling thread until either the semaphore pointed to by <code>sem</code> has a positive value, the call is interrupted by a signal or error. If the call is successful it will atomically decrement the semaphore value. </p>
<p> After <code>SDL_SemWait()</code> is successful, the semaphore can be released and its count atomically incremented by a successful call to <i>SDL_SemPost</i>.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> if successful or <code>-1</code> if there was an error (leaving the semaphore unchanged).</p>
<h2>Examples</h2>
<pre><tt>if (SDL_SemWait(my_sem) == -1) {
 return WAIT_FAILED;
}
...
SDL_SemPost(my_sem);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemPost</code>, <i></i><code>SDL_SemValue</code></p>
