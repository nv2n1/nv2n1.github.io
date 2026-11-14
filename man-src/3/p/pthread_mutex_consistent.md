---
title: "pthread_mutex_consistent(3)"
name: "pthread_mutex_consistent"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_mutex_consistent/"
description: "pthread_mutex_consistent – make a robust mutex consistent"
---

<p>pthread_mutex_consistent &#8211; make a robust mutex consistent</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_mutex_consistent(pthread_mutex_t *mutex);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_mutex_consistent</code>(): </p>
<dl>
<dd>_POSIX_C_SOURCE &gt;= 200809L</dl>
<h2>Description</h2>
<p>This function makes a robust mutex consistent if it is in an inconsistent state. A mutex can be left in an inconsistent state if its owner terminates while holding the mutex, in which case the next owner who acquires the mutex will succeed and be notified by a return value of <code>EOWNERDEAD</code> from a call to <code>pthread_mutex_lock</code>().</p>
<h2>Return Value</h2>
<p>On success, <i>pthread_mutex_consistent</i>() returns 0. Otherwise, it returns a positive error number to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>The mutex is either not robust or is not in an inconsistent state.</dl>
<h2>Versions</h2>
<p><code>pthread_mutex_consistent</code>() was added to glibc in version 2.12.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2008.</p>
<h2>Notes</h2>
<p><code>pthread_mutex_consistent</code>() simply informs the implementation that the state (shared data) guarded by the mutex has been restored to a consistent state and that normal operations can now be performed with the mutex. It is the application&#8217;s responsibility to ensure that the shared data has been restored to a consistent state before calling <code>pthread_mutex_consistent</code>(). Before the addition of <code>pthread_mutex_consistent</code>() to POSIX, glibc defined the following equivalent nonstandard function if <code>_GNU_SOURCE</code> was defined: </p>
<pre><code>int pthread_mutex_consistent(const pthread_mutex_t *mutex);</code></pre>
<p> This GNU-specific API, which first appeared in glibc 2.4, is nowadays obsolete and should not be used in new programs.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_mutexattr_setrobust/">pthread_mutexattr_setrobust</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutexattr_init/">pthread_mutexattr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutexattr_getrobust/">pthread_mutexattr_getrobust</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutexattr_setrobust/">pthread_mutexattr_setrobust</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
