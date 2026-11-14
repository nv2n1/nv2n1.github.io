---
title: "aio_fsync(3)"
name: "aio_fsync"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_fsync/"
description: "aio_fsync – asynchronous file synchronization"
---

<h2 class="name">NAME</h2>
<p> aio_fsync &#8211; asynchronous file synchronization </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;aio.h&gt;</code> </p>
<p> <code>int aio_fsync(int </code><i>op</i><code>, struct aiocb *</code><i>aiocbp</i><code>);</code> </p>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>aio_fsync</code>() function does a sync on all outstanding asynchronous I/O operations associated with <i>aiocbp-&gt;aio_fildes</i>. (See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) for a description of the <i>aiocb</i> structure.) </p>
<p> More precisely, if <i>op</i> is <code>O_SYNC</code>, then all currently queued I/O operations shall be completed as if by a call of <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), and if <i>op</i> is <code>O_DSYNC</code>, this call is the asynchronous analog of <code><a href="/docs/linux/man/2-fdatasync/">fdatasync</a></code>(2). </p>
<p> Note that this is a request only; it does not wait for I/O completion. </p>
<p> Apart from <i>aio_fildes</i>, the only field in the structure pointed to by <i>aiocbp</i> that is used by this call is the <i>aio_sigevent</i> field (a <i>sigevent</i> structure, described in <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)), which indicates the desired type of asynchronous notification at completion. All other fields are ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success (the sync request was successfully queued) this function returns 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Out of resources.</p>
<dt><code>EBADF</code></p>
<dd> <i>aio_fildes</i> is not a valid file descriptor open for writing.</p>
<dt><code>EINVAL</code></p>
<dd> Synchronized I/O is not supported for this file, or <i>op</i> is not <code>O_SYNC</code> or <code>O_DSYNC</code>.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>aio_fsync</code>() is not implemented.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_fsync</code>() function is available since glibc 2.1.</p>
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
<td> <code>aio_fsync</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
