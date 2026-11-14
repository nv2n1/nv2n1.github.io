---
title: "sdl_semtrywait(3)"
name: "sdl_semtrywait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_semtrywait/"
description: "SDL_SemTryWait – Attempt to lock a semaphore but don’t suspend the thread."
---

<p>SDL_SemTryWait &#8211; Attempt to lock a semaphore but don&#8217;t suspend the thread.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_SemTryWait</code>(<code>SDL_sem *sem</code>);</p>
<h2>Description</h2>
<p><code>SDL_SemTryWait</code> is a non-blocking varient of <i></i><code>SDL_SemWait</code>. If the value of the semaphore pointed to by <code>sem</code> is positive it will atomically decrement the semaphore value and return 0, otherwise it will return <code>SDL_MUTEX_TIMEOUT</code> instead of suspending the thread. </p>
<p> After <code>SDL_SemTryWait</code> is successful, the semaphore can be released and its count atomically incremented by a successful call to <i>SDL_SemPost</i>.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> if the semaphore was successfully locked or either <code>SDL_MUTEX_TIMEOUT</code> or <code>-1</code> if the thread would have suspended or there was an error, respectivly. </p>
<p> If the semaphore was not successfully locked, the semaphore will be unchanged.</p>
<h2>Examples</h2>
<pre><tt>res = SDL_SemTryWait(my_sem);
if (res == SDL_MUTEX_TIMEOUT) {
 return TRY_AGAIN;
}
if (res == -1) {
 return WAIT_ERROR;
}
...
SDL_SemPost(my_sem);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemPost</code>, <i></i><code>SDL_SemValue</code></p>
