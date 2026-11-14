---
title: "pthread_attr_setguardsize(3)"
name: "pthread_attr_setguardsize"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_setguardsize/"
description: "pthread_attr_setguardsize, pthread_attr_getguardsize – set/get guard size attribute in thread attributes object"
---

<p>pthread_attr_setguardsize, pthread_attr_getguardsize &#8211; set/get guard size attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setguardsize(pthread_attr_t *attr, size_t guardsize);
int pthread_attr_getguardsize(const pthread_attr_t *attr,
                              size_t *guardsize);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setguardsize</code>() function sets the guard size attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>guardsize</i>. </p>
<p> If <i>guardsize</i> is greater than 0, then for each new thread created using <i>attr</i> the system allocates an additional region of at least <i>guardsize</i> bytes at the end of the thread&#8217;s stack to act as the guard area for the stack (but see BUGS). </p>
<p> If <i>guardsize</i> is 0, then new threads created with <i>attr</i> will not have a guard area. </p>
<p> The default guard size is the same as the system page size. </p>
<p> If the stack address attribute has been set in <i>attr</i> (using <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3) or <code><a href="/docs/linux/man/3-pthread_attr_setstackaddr/">pthread_attr_setstackaddr</a></code>(3)), meaning that the caller is allocating the thread&#8217;s stack, then the guard size attribute is ignored (i.e., no guard area is created by the system): it is the application&#8217;s responsibility to handle stack overflow (perhaps by using <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2) to manually define a guard area at the end of the stack that it has allocated). </p>
<p> The <code>pthread_attr_getguardsize</code>() function returns the guard size attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>guardsize</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p>POSIX.1 documents an <code>EINVAL</code> error if <i>attr</i> or <i>guardsize</i> is invalid. On Linux these functions always succeed (but portable and future-proof applications should nevertheless handle a possible error return).</p>
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
<td> <code>pthread_attr_setguardsize</code>(), <code>pthread_attr_getguardsize</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>A guard area consists of virtual memory pages that are protected to prevent read and write access. If a thread overflows its stack into the guard area, then, on most hard architectures, it receives a <code>SIGSEGV</code> signal, thus notifying it of the overflow. Guard areas start on page boundaries, and the guard size is internally rounded up to the system page size when creating a thread. (Nevertheless, <code>pthread_attr_getguardsize</code>() returns the guard size that was set by <code>pthread_attr_setguardsize</code>().) </p>
<p> Setting a guard size of 0 may be useful to save memory in an application that creates many threads and knows that stack overflow can never occur. </p>
<p> Choosing a guard size larger than the default size may be necessary for detecting stack overflows if a thread allocates large data structures on the stack.</p>
<h2>Bugs</h2>
<p>As at glibc 2.8, the NPTL threading implementation includes the guard area within the stack size allocation, rather than allocating extra space at the end of the stack, as POSIX.1 requires. (This can result in an <code>EINVAL</code> error from <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) if the guard size value is too large, leaving no space for the actual stack.) </p>
<p> The obsolete LinuxThreads implementation did the right thing, allocating extra space at the end of the stack for the guard area.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_getattr_np/">pthread_getattr_np</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
