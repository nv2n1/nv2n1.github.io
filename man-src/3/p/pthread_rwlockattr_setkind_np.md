---
title: "pthread_rwlockattr_setkind_np(3)"
name: "pthread_rwlockattr_setkind_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_rwlockattr_setkind_np/"
description: "pthread_rwlockattr_setkind_np, pthread_rwlockattr_getkind_np – set/get the read-write lock kind of the thread read-write lock attribute object"
---

<p>pthread_rwlockattr_setkind_np, pthread_rwlockattr_getkind_np &#8211; set/get the read-write lock kind of the thread read-write lock attribute object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_rwlockattr_setkind_np(pthread_rwlockattr_t *attr,
                                  int pref);
int pthread_rwlockattr_getkind_np(const pthread_rwlockattr_t *attr,
                                  int *pref);

Compile and link with -pthread.



Feature Test Macro Requirements for glibc (see
feature_test_macros(7)):</code></pre>
<p> <code>pthread_rwlockattr_setkind_np</code>(), <code>pthread_rwlockattr_getkind_np</code>(): </p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _POSIX_C_SOURCE &gt;= 200809L</dl>
<h2>Description</h2>
<p>The <code>pthread_rwlockattr_setkind_np</code>() function sets the &quot;lock kind&quot; attribute of the read-write lock attribute object referred to by <i>attr</i> to the value specified in <i>pref</i>. The argument <i>pref</i> may be set to one of the following:</p>
<dl>
<dt><code>PTHREAD_RWLOCK_PREFER_READER_NP</code></p>
<dd>This is the default. A thread may hold multiple read locks; that is, read locks are recursive. According to The Single Unix Specification, the behavior is unspecified when a reader tries to place a lock, and there is no write lock but writers are waiting. Giving preference to the reader, as is set by <code>PTHREAD_RWLOCK_PREFER_READER_NP</code>, implies that the reader will receive the requested lock, even if a writer is waiting. As long as there are readers, the writer will be starved.</p>
<dt><code>PTHREAD_RWLOCK_PREFER_WRITER_NP</code></p>
<dd>This is intended as the write lock analog of <code>PTHREAD_RWLOCK_PREFER_READER_NP</code>. This is ignored by glibc because the POSIX requirement to support recursive read locks would cause this option to create trivial deadlocks; instead use <code>PTHREAD_RWLOCK_PREFER_WRITER_NONRECURSIVE_NP</code> which ensures the application developer will not take recursive read locks thus avoiding deadlocks.</p>
<dt><code>PTHREAD_RWLOCK_PREFER_WRITER_NONRECURSIVE_NP</code></p>
<dd>Setting the lock kind to this avoids writer starvation as long as any read locking is not done in a recursive fashion.</dl>
<p> The <code>pthread_rwlockattr_getkind_np</code>() function returns the value of the lock kind attribute of the read-write lock attribute object referred to by <i>attr</i> in the pointer <i>pref</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0. Given valid pointer arguments, <code>pthread_rwlockattr_getkind_np</code>() always succeeds. On error, <code>pthread_rwlockattr_setkind_np</code>() returns a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>pref</i> specifies an unsupported value.</dl>
<h2>Versions</h2>
<p>The <code>pthread_rwlockattr_getkind_np</code>() and <code>pthread_rwlockattr_setkind_np</code>() functions first appeared in glibc 2.1.</p>
<h2>Conforming To</h2>
<p>These functions are non-standard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
