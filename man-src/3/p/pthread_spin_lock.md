---
title: "pthread_spin_lock(3)"
name: "pthread_spin_lock"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_spin_lock/"
description: "pthread_spin_lock, pthread_spin_trylock, pthread_spin_unlock – lock and unlock a spin lock"
---

<p>pthread_spin_lock, pthread_spin_trylock, pthread_spin_unlock &#8211; lock and unlock a spin lock</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_spin_lock(pthread_spinlock_t *lock);
int pthread_spin_trylock(pthread_spinlock_t *lock);
int pthread_spin_unlock(pthread_spinlock_t *lock);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_spin_lock</code>(), <code>pthread_spin_trylock</code>(): </p>
<dl>
<dd>_POSIX_C_SOURCE &gt;= 200112L</dl>
<h2>Description</h2>
<p>The <code>pthread_spin_lock</code>() function locks the spin lock referred to by <i>lock</i>. If the spin lock is currently unlocked, the calling thread acquires the lock immediately. If the spin lock is currently locked by another thread, the calling thread spins, testing the lock until it becomes available, at which point the calling thread acquires the lock. </p>
<p> Calling <code>pthread_spin_lock</code>() on a lock that is already held by the caller or a lock that has not been initialized with <code><a href="/docs/linux/man/3-pthread_spin_init/">pthread_spin_init</a></code>(3) results in undefined behavior. </p>
<p> The <code>pthread_spin_trylock</code>() function is like <code>pthread_spin_lock</code>(), except that if the spin lock referred to by <i>lock</i> is currently locked, then, instead of spinning, the call returns immediately with the error <code>EBUSY</code>. </p>
<p> The <code>pthread_spin_unlock</code>() function unlocks the spin lock referred to <i>lock</i>. If any threads are spinning on the lock, one of those threads will then acquire the lock. </p>
<p> Calling <code>pthread_spin_unlock</code>() on a lock that is not held by the caller results in undefined behavior.</p>
<h2>Return Value</h2>
<p>On success, these functions return zero. On failure, they return an error number.</p>
<h2>Errors</h2>
<p><code>pthread_spin_lock</code>() may fail with the following errors:</p>
<dl>
<dt><code>EDEADLOCK</code></p>
<dd>The system detected a deadlock condition.</dl>
<p> <code>pthread_spin_trylock</code>() fails with the following errors:</p>
<dl>
<dt><code>EBUSY</code></p>
<dd>The spin lock is currently locked by another thread.</dl>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.2.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001.</p>
<h2>Notes</h2>
<p>Applying any of the functions described on this page to an uninitialized spin lock results in undefined behavior. </p>
<p> Carefully read NOTES in <code><a href="/docs/linux/man/3-pthread_spin_init/">pthread_spin_init</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_spin_destroy/">pthread_spin_destroy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_init/">pthread_spin_init</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
