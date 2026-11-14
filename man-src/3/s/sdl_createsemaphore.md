---
title: "sdl_createsemaphore(3)"
name: "sdl_createsemaphore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_createsemaphore/"
description: "SDL_CreateSemaphore – Creates a new semaphore and assigns an initial value to it."
---

<p>SDL_CreateSemaphore &#8211; Creates a new semaphore and assigns an initial value to it.</p>
<h2>Synopsis</h2>
<p><code>#include &quot;SDL.h&quot; #include &quot;SDL_thread.h&quot; </p>
<p> SDL_sem *SDL_CreateSemaphore</code>(<code>Uint32 initial_value</code>);</p>
<h2>Description</h2>
<p><code>SDL_CreateSemaphore()</code> creates a new semaphore and initializes it with the value <code>initial_value</code>. Each locking operation on the semaphore by <i>SDL_SemWait</i>, <i>SDL_SemTryWait</i> or <i>SDL_SemWaitTimeout</i> will atomically decrement the semaphore value. The locking operation will be blocked if the semaphore value is not positive (greater than zero). Each unlock operation by <i>SDL_SemPost</i> will atomically increment the semaphore value.</p>
<h2>Return Value</h2>
<p>Returns a pointer to an initialized semaphore or <code>NULL</code> if there was an error.</p>
<h2>Examples</h2>
<pre><tt>SDL_sem *my_sem;
my_sem = SDL_CreateSemaphore(INITIAL_SEM_VALUE);
if (my_sem == NULL) {
 return CREATE_SEM_FAILED;
}</tt></pre>
<h2>See Also</h2>
<p><i></i><code>SDL_DestroySemaphore</code>, <i></i><code>SDL_SemWait</code>, <i></i><code>SDL_SemTryWait</code>, <i></i><code>SDL_SemWaitTimeout</code>, <i></i><code>SDL_SemPost</code>, <i></i><code>SDL_SemValue</code></p>
