---
title: "aio_cancel(3)"
name: "aio_cancel"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_cancel/"
description: "aio_cancel – cancel an outstanding asynchronous I/O request"
---

<h2 class="name">NAME</h2>
<p> aio_cancel &#8211; cancel an outstanding asynchronous I/O request </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;aio.h&gt;</code> </p>
<p> <code>int aio_cancel(int </code><i>fd</i><code>, struct aiocb *</code><i>aiocbp</i><code>);</code> </p>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>aio_cancel</code>() function attempts to cancel outstanding asynchronous I/O requests for the file descriptor <i>fd</i>. If <i>aiocbp</i> is NULL, all such requests are canceled. Otherwise, only the request described by the control block pointed to by <i>aiocbp</i> is canceled. (See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) for a description of the <i>aiocb</i> structure.) </p>
<p> Normal asynchronous notification occurs for canceled requests (see <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) and <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)). The request return status (<code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3)) is set to -1, and the request error status (<code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3)) is set to <code>ECANCELED</code>. The control block of requests that cannot be canceled is not changed. </p>
<p> If the request could not be canceled, then it will terminate in the usual way after performing the I/O operation. (In this case, <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3) will return the status <code>EINPROGRESSS</code>.) </p>
<p> If <i>aiocbp</i> is not NULL, and <i>fd</i> differs from the file descriptor with which the asynchronous operation was initiated, unspecified results occur. </p>
<p> Which operations are cancelable is implementation-defined.</p>
<h2>RETURN VALUE</h2>
<p> The <code>aio_cancel</code>() function returns one of the following values:</p>
<dl>
<dt><code>AIO_CANCELED</code></p>
<dd> All requests were successfully canceled.</p>
<dt><code>AIO_NOTCANCELED</code></p>
<dd> At least one of the requests specified was not canceled because it was in progress. In this case, one may check the status of individual requests using <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3).</p>
<dt><code>AIO_ALLDONE</code></p>
<dd> All requests had already been completed before the call.</p>
<dt>-1</p>
<dd> An error occurred. The cause of the error can be found by inspecting <i>errno</i>.</dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>aio_cancel</code>() is not implemented.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_cancel</code>() function is available since glibc 2.1.</p>
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
<td> <code>aio_cancel</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
