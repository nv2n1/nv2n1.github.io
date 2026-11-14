---
title: "pthread_attr_setstacksize(3)"
name: "pthread_attr_setstacksize"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_setstacksize/"
description: "pthread_attr_setstacksize, pthread_attr_getstacksize – set/get stack size attribute in thread attributes object"
---

<p>pthread_attr_setstacksize, pthread_attr_getstacksize &#8211; set/get stack size attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setstacksize(pthread_attr_t *attr, size_t stacksize);
int pthread_attr_getstacksize(const pthread_attr_t *attr,
                              size_t *stacksize);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setstacksize</code>() function sets the stack size attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>stacksize</i>. </p>
<p> The stack size attribute determines the minimum size (in bytes) that will be allocated for threads created using the thread attributes object <i>attr</i>. </p>
<p> The <code>pthread_attr_getstacksize</code>() function returns the stack size attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>stacksize</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setstacksize</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>The stack size is less than <code>PTHREAD_STACK_MIN</code> (16384) bytes.</dl>
<p> On some systems, <code>pthread_attr_setstacksize</code>() can fail with the error <code>EINVAL</code> if <i>stacksize</i> is not a multiple of the system page size.</p>
<h2>Versions</h2>
<p>These functions are provided by glibc since version 2.1.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_attr_setstacksize</code>(), <code>pthread_attr_getstacksize</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>For details on the default stack size of new threads, see <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3). </p>
<p> A thread&#8217;s stack size is fixed at the time of thread creation. Only the main thread can dynamically grow its stack. </p>
<p> The <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3) function allows an application to set both the size and location of a caller-allocated stack that is to be used by a thread.</p>
<h2>Bugs</h2>
<p>As at glibc 2.8, if the specified <i>stacksize</i> is not a multiple of <code>STACK_ALIGN</code> (16 bytes on most architectures), it may be rounded <i>downward</i>, in violation of POSIX.1, which says that the allocated stack will be at least <i>stacksize</i> bytes.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setguardsize/">pthread_attr_setguardsize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
