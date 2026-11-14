---
title: "pthread_attr_getstack(3)"
name: "pthread_attr_getstack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_getstack/"
description: "pthread_attr_setstack, pthread_attr_getstack – set/get stack attributes in thread attributes object"
---

<p>pthread_attr_setstack, pthread_attr_getstack &#8211; set/get stack attributes in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setstack(pthread_attr_t *attr,
                          void *stackaddr, size_t stacksize);
int pthread_attr_getstack(const pthread_attr_t *attr,
                          void **stackaddr, size_t *stacksize);

Compile and link with - pthread.</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_attr_getstack</code>(), <code>pthread_attr_setstack</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>pthread_attr_setstack</code>() function sets the stack address and stack size attributes of the thread attributes object referred to by <i>attr</i> to the values specified in <i>stackaddr</i> and <i>stacksize</i>, respectively. These attributes specify the location and size of the stack that should be used by a thread that is created using the thread attributes object <i>attr</i>. </p>
<p> <i>stackaddr</i> should point to the lowest addressable byte of a buffer of <i>stacksize</i> bytes that was allocated by the caller. The pages of the allocated buffer should be both readable and writable. </p>
<p> The <code>pthread_attr_getstack</code>() function returns the stack address and stack size attributes of the thread attributes object referred to by <i>attr</i> in the buffers pointed to by <i>stackaddr</i> and <i>stacksize</i>, respectively.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setstack</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>stacksize</i> is less than <code>PTHREAD_STACK_MIN</code> (16384) bytes. On some systems, this error may also occur if <i>stackaddr</i> or <i>stackaddr&nbsp;+&nbsp;stacksize</i> is not suitably aligned.</dl>
<p> POSIX.1 also documents an <code>EACCES</code> error if the stack area described by <i>stackaddr</i> and <i>stacksize</i> is not both readable and writable by the caller.</p>
<h2>Versions</h2>
<p>These functions are provided by glibc since version 2.2.</p>
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
<td> <code>pthread_attr_setstack</code>(), <code>pthread_attr_getstack</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>These functions are provided for applications that must ensure that a thread&#8217;s stack is placed in a particular location. For most applications, this is not necessary, and the use of these functions should be avoided. (Use <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3) if an application simply requires a stack size other than the default.) </p>
<p> When an application employs <code>pthread_attr_setstack</code>(), it takes over the responsibility of allocating the stack. Any guard size value that was set using <code><a href="/docs/linux/man/3-pthread_attr_setguardsize/">pthread_attr_setguardsize</a></code>(3) is ignored. If deemed necessary, it is the application&#8217;s responsibility to allocate a guard area (one or more pages protected against reading and writing) to handle the possibility of stack overflow. </p>
<p> The address specified in <i>stackaddr</i> should be suitably aligned: for full portability, align it on a page boundary (<i>sysconf(_SC_PAGESIZE)</i>). <code><a href="/docs/linux/man/3-posix_memalign/">posix_memalign</a></code>(3) may be useful for allocation. Probably, <i>stacksize</i> should also be a multiple of the system page size. </p>
<p> If <i>attr</i> is used to create multiple threads, then the caller must change the stack address attribute between calls to <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3); otherwise, the threads will attempt to use the same memory area for their stacks, and chaos will ensue.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/3-posix_memalign/">posix_memalign</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setguardsize/">pthread_attr_setguardsize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstackaddr/">pthread_attr_setstackaddr</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
