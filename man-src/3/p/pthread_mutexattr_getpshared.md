---
title: "pthread_mutexattr_getpshared(3)"
name: "pthread_mutexattr_getpshared"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_mutexattr_getpshared/"
description: "pthread_mutexattr_getpshared, pthread_mutexattr_setpshared – get/set process-shared mutex attribute"
---

<p>pthread_mutexattr_getpshared, pthread_mutexattr_setpshared &#8211; get/set process-shared mutex attribute</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_mutexattr_getpshared(const pthread_mutexattr_t *attr,
                                 int *pshared);
int pthread_mutexattr_setpshared(pthread_mutexattr_t *attr,
                                 int pshared);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>These functions get and set the process-shared attribute in a mutex attributes object. This attribute must be appropriately set to ensure correct, efficient operation of a mutex created using this attributes object. </p>
<p> The process-shared attribute can have one of the following values:</p>
<dl>
<dt><code>PTHREAD_PROCESS_PRIVATE</code></p>
<dd>Mutexes created with this attributes object are to be shared only among threads in the same process that initialized the mutex. This is the default value for the process-shared mutex attribute.</p>
<dt><code>PTHREAD_PROCESS_SHARED</code></p>
<dd>Mutexes created with this attributes object can be shared between any threads that have access to the memory containing the object, including threads in different processes.</dl>
<p> <code>pthread_mutexattr_getpshared</code>() places the value of the process-shared attribute of the mutex attributes object referred to by <i>attr</i> in the location pointed to by <i>pshared</i>. </p>
<p> <code>pthread_mutexattr_setpshared</code>() sets the value of the process-shared attribute of the mutex attributes object referred to by <i>attr</i> to the value specified in <code>pshared</code>. </p>
<p> If <i>attr</i> does not refer to an initialized mutex attributes object, the behavior is undefined.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0. On error, they return a positive error number.</p>
<h2>Errors</h2>
<p><code>pthread_mutexattr_setpshared</code>() can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>The value specified in <i>pshared</i> is invalid.</p>
<dt><code>ENOTSUP</code></p>
<dd><i>pshared is</i> <code>PTHREAD_PROCESS_SHARED</code> but the implementation does not support process-shared mutexes.</dl>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_mutexattr_init/">pthread_mutexattr_init</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
