---
title: "sdl_semwaittimeout(3)"
name: "sdl_semwaittimeout"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_semwaittimeout/"
description: "SDL_SemWaitTimeout – Lock a semaphore, but only wait up to a specified maximum time."
---

<p>SDL_SemWaitTimeout &#8211; Lock a semaphore, but only wait up to a specified maximum time.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> int SDL_SemWaitTimeout</code>(<code>SDL_sem *sem, Uint32 timeout</code>);</p>
<h2>Description</h2>
<p><code>SDL_SemWaitTimeout()</code> is a varient of <i>SDL_SemWait</i> with a maximum timeout value. If the value of the semaphore pointed to by <code>sem</code> is positive (greater than zero) it will atomically decrement the semaphore value and return 0, otherwise it will wait up to <code>timeout</code> milliseconds trying to lock the semaphore. This function is to be avoided if possible since on some platforms it is implemented by polling the semaphore every millisecond in a busy loop. </p>
<p> After <code>SDL_SemWaitTimeout()</code> is successful, the semaphore can be released and its count atomically incremented by a successful call to <i>SDL_SemPost</i>.</p>
<h2>Return Value</h2>
<p>Returns <code>0</code> if the semaphore was successfully locked or either <code>SDL_MUTEX_TIMEOUT</code> or <code>-1</code> if the timeout period was exceeded or there was an error, respectivly. </p>
<p> If the semaphore was not successfully locked, the semaphore will be unchanged.</p>
<h2>Examples</h2>
<pre><tt>res = SDL_SemWaitTimeout(my_sem, WAIT_TIMEOUT_MILLISEC);
if (res == SDL_MUTEX_TIMEOUT) {
 return TRY_AGAIN;
}
if (res == -1) {
 return WAIT_ERROR;
}
...
SDL_SemPost(my_sem);</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_CreateSemaphore</code>, <i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemPost</code>, <i></i><code>SDL_SemValue</code></p>
