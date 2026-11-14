---
title: "pthread_setcanceltype(3)"
name: "pthread_setcanceltype"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_setcanceltype/"
description: "pthread_setcancelstate, pthread_setcanceltype – set cancelability state and type"
---

<p>pthread_setcancelstate, pthread_setcanceltype &#8211; set cancelability state and type</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_setcancelstate(int state, int *oldstate);
int pthread_setcanceltype(int type, int *oldtype);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setcancelstate</code>() sets the cancelability state of the calling thread to the value given in <i>state</i>. The previous cancelability state of the thread is returned in the buffer pointed to by <i>oldstate</i>. The <i>state</i> argument must have one of the following values:</p>
<dl>
<dt><code>PTHREAD_CANCEL_ENABLE</code></p>
<dd>The thread is cancelable. This is the default cancelability state in all new threads, including the initial thread. The thread&#8217;s cancelability type determines when a cancelable thread will respond to a cancellation request.</p>
<dt><code>PTHREAD_CANCEL_DISABLE</code></p>
<dd>The thread is not cancelable. If a cancellation request is received, it is blocked until cancelability is enabled.</dl>
<p> The <code>pthread_setcanceltype</code>() sets the cancelability type of the calling thread to the value given in <i>type</i>. The previous cancelability type of the thread is returned in the buffer pointed to by <i>oldtype</i>. The <i>type</i> argument must have one of the following values:</p>
<dl>
<dt><code>PTHREAD_CANCEL_DEFERRED</code></p>
<dd>A cancellation request is deferred until the thread next calls a function that is a cancellation point (see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)). This is the default cancelability type in all new threads, including the initial thread.</p>
<dd>Even with deferred cancellation, a cancellation point in an asynchronous signal handler may still be acted upon and the effect is as if it was an asynchronous cancellation.</p>
<dt><code>PTHREAD_CANCEL_ASYNCHRONOUS</code></p>
<dd>The thread can be canceled at any time. (Typically, it will be canceled immediately upon receiving a cancellation request, but the system doesn&#8217;t guarantee this.)</dl>
<p> The set-and-get operation performed by each of these functions is atomic with respect to other threads in the process calling the same function.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p>The <code>pthread_setcancelstate</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>Invalid value for <i>state</i>.</dl>
<p> The <code>pthread_setcanceltype</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>Invalid value for <i>type</i>.</dl>
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
<td> <code>pthread_setcancelstate</code>(), <code>pthread_setcanceltype</code>() </td>
<td>Thread safety</td>
<td> MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_setcancelstate</code>(), <code>pthread_setcanceltype</code>() </td>
<td>Async-cancel-safety</td>
<td> AC-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>For details of what happens when a thread is canceled, see <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3). </p>
<p> Briefly disabling cancelability is useful if a thread performs some critical action that must not be interrupted by a cancellation request. Beware of disabling cancelability for long periods, or around operations that may block for long periods, since that will render the thread unresponsive to cancellation requests.</p>
<h3>Asynchronous cancelability</h3>
<p>Setting the cancelability type to <code>PTHREAD_CANCEL_ASYNCHRONOUS</code> is rarely useful. Since the thread could be canceled at <i>any</i> time, it cannot safely reserve resources (e.g., allocating memory with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)), acquire mutexes, semaphores, or locks, and so on. Reserving resources is unsafe because the application has no way of knowing what the state of these resources is when the thread is canceled; that is, did cancellation occur before the resources were reserved, while they were reserved, or after they were released? Furthermore, some internal data structures (e.g., the linked list of free blocks managed by the <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) family of functions) may be left in an inconsistent state if cancellation occurs in the middle of the function call. Consequently, clean-up handlers cease to be useful. </p>
<p> Functions that can be safely asynchronously canceled are called <i>async-cancel-safe functions</i>. POSIX.1-2001 and POSIX.1-2008 require only that <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code>pthread_setcancelstate</code>(), and <code>pthread_setcanceltype</code>() be async-cancel-safe. In general, other library functions can&#8217;t be safely called from an asynchronously cancelable thread. </p>
<p> One of the few circumstances in which asynchronous cancelability is useful is for cancellation of a thread that is in a pure compute-bound loop.</p>
<h3>Portability notes</h3>
<p>The Linux threading implementations permit the <i>oldstate</i> argument of <code>pthread_setcancelstate</code>() to be NULL, in which case the information about the previous cancelability state is not returned to the caller. Many other implementations also permit a NULL <i>oldstat</i> argument, but POSIX.1 does not specify this point, so portable applications should always specify a non-NULL value in <i>oldstate</i>. A precisely analogous set of statements applies for the <i>oldtype</i> argument of <code>pthread_setcanceltype</code>().</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code><a href="/docs/linux/man/3-pthread_testcancel/">pthread_testcancel</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
