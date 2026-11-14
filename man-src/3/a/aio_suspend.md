---
title: "aio_suspend(3)"
name: "aio_suspend"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_suspend/"
description: "aio_suspend – wait for asynchronous I/O operation or timeout"
---

<h2 class="name">NAME</h2>
<p> aio_suspend &#8211; wait for asynchronous I/O operation or timeout </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;aio.h&gt;
int aio_suspend(const struct aiocb *const aiocb_list[],
                int nitems, const struct timespec *timeout);
Link with - lrt.
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>aio_suspend</code>() function suspends the calling thread until one of the following occurs:</p>
<dl>
<dt>*</p>
<dd> One or more of the asynchronous I/O requests in the list <i>aiocb_list</i> has completed.</p>
<dt>*</p>
<dd> A signal is delivered.</p>
<dt>*</p>
<dd> <i>timeout</i> is not NULL and the specified time interval has passed. (For details of the <i>timespec</i> structure, see <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2).)</dl>
<p> The <i>nitems</i> argument specifies the number of items in <i>aiocb_list</i>. Each item in the list pointed to by <i>aiocb_list</i> must be either NULL (and then is ignored), or a pointer to a control block on which I/O was initiated using <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), or <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3). (See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) for a description of the <i>aiocb</i> structure.) </p>
<p> If <code>CLOCK_MONOTONIC</code> is supported, this clock is used to measure the timeout interval (see <code><a href="/docs/linux/man/3-clock_gettime/">clock_gettime</a></code>(3)).</p>
<h2>RETURN VALUE</h2>
<p> If this function returns after completion of one of the I/O requests specified in <i>aiocb_list</i>, 0 is returned. Otherwise, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The call timed out before any of the indicated operations had completed.</p>
<dt><code>EINTR</code></p>
<dd> The call was ended by signal (possibly the completion signal of one of the operations we were waiting for); see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>ENOSYS</code></p>
<dd> <code>aio_suspend</code>() is not implemented.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_suspend</code>() function is available since glibc 2.1.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>aio_suspend</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> One can achieve polling by using a non-NULL <i>timeout</i> that specifies a zero time interval. </p>
<p> If one or more of the asynchronous I/O operations specified in <i>aiocb_list</i> has already completed at the time of the call to <code>aio_suspend</code>(), then the call returns immediately. </p>
<p> To determine which I/O operations have completed after a successful return from <code>aio_suspend</code>(), use <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3) to scan the list of <i>aiocb</i> structures pointed to by <i>aiocb_list</i>.</p>
<h2>BUGS</h2>
<p> The glibc implementation of <code>aio_suspend</code>() is not async-signal-safe, in violation of the requirements of POSIX.1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
