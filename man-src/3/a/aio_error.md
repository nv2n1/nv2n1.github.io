---
title: "aio_error(3)"
name: "aio_error"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_error/"
description: "aio_error – get error status of asynchronous I/O operation"
---

<h2 class="name">NAME</h2>
<p> aio_error &#8211; get error status of asynchronous I/O operation </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;aio.h&gt;</code> </p>
<p> <code>int aio_error(const struct aiocb *</code><i>aiocbp</i><code>);</code> </p>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>aio_error</code>() function returns the error status for the asynchronous I/O request with control block pointed to by <i>aiocbp</i>. (See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) for a description of the <i>aiocb</i> structure.)</p>
<h2>RETURN VALUE</h2>
<p> This function returns one of the following:</p>
<dl>
<dt>*</p>
<dd> <code>EINPROGRESS</code>, if the request has not been completed yet.</p>
<dt>*</p>
<dd> <code>ECANCELED</code>, if the request was canceled.</p>
<dt>*</p>
<dd> 0, if the request completed successfully.</p>
<dt>*</p>
<dd> A positive error number, if the asynchronous I/O operation failed. This is the same value that would have been stored in the <i>errno</i> variable in the case of a synchronous <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), or <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2) call.</dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>aiocbp</i> does not point at a control block for an asynchronous I/O request of which the return status (see <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3)) has not been retrieved yet.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>aio_error</code>() is not implemented.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_error</code>() function is available since glibc 2.1.</p>
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
<td> <code>aio_error</code>() </td>
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
<p> <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
