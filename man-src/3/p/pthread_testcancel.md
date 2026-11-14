---
title: "pthread_testcancel(3)"
name: "pthread_testcancel"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_testcancel/"
description: "pthread_testcancel – request delivery of any pending cancellation request"
---

<p>pthread_testcancel &#8211; request delivery of any pending cancellation request</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

void pthread_testcancel(void);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>Calling <code>pthread_testcancel</code>() creates a cancellation point within the calling thread, so that a thread that is otherwise executing code that contains no cancellation points will respond to a cancellation request. </p>
<p> If cancelability is disabled (using <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3)), or no cancellation request is pending, then a call to <code>pthread_testcancel</code>() has no effect.</p>
<h2>Return Value</h2>
<p>This function does not return a value. If the calling thread is canceled as a consequence of a call to this function, then the function does not return.</p>
<h2>Errors</h2>
<p>This function always succeeds.</p>
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
<td> <code>pthread_testcancel</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
