---
title: "aio_read(3)"
name: "aio_read"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aio_read/"
description: "aio_read – asynchronous read"
---

<h2 class="name">NAME</h2>
<p> aio_read &#8211; asynchronous read </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;aio.h&gt;</code> </p>
<p> <code>int aio_read(struct aiocb *</code><i>aiocbp</i><code>);</code> </p>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>aio_read</code>() function queues the I/O request described by the buffer pointed to by <i>aiocbp</i>. This function is the asynchronous analog of <code><a href="/docs/linux/man/2-read/">read</a></code>(2). The arguments of the call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read(fd, buf, count) </p>
<p> correspond (in order) to the fields <i>aio_fildes</i>, <i>aio_buf</i>, and <i>aio_nbytes</i> of the structure pointed to by <i>aiocbp</i>. (See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7) for a description of the <i>aiocb</i> structure.) </p>
<p> The data is read starting at the absolute position <i>aiocbp-&gt;aio_offset</i>, regardless of the file offset. After the call, the value of the file offset is unspecified. </p>
<p> The &quot;asynchronous&quot; means that this call returns as soon as the request has been enqueued; the read may or may not have completed when the call returns. One tests for completion using <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3). The return status of a completed I/O operation can be obtained by <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3). Asynchronous notification of I/O completion can be obtained by setting <i>aiocbp-&gt;aio_sigevent</i> appropriately; see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for details. </p>
<p> If <code>_POSIX_PRIORITIZED_IO</code> is defined, and this file supports it, then the asynchronous operation is submitted at a priority equal to that of the calling process minus <i>aiocbp-&gt;aio_reqprio</i>. </p>
<p> The field <i>aiocbp-&gt;aio_lio_opcode</i> is ignored. </p>
<p> No data is read from a regular file beyond its maximum offset.</p>
<h2>RETURN VALUE</h2>
<p> On success, 0 is returned. On error, the request is not enqueued, -1 is returned, and <i>errno</i> is set appropriately. If an error is detected only later, it will be reported via <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3) (returns status -1) and <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3) (error status&#8212;whatever one would have gotten in <i>errno</i>, such as <code>EBADF</code>).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Out of resources.</p>
<dt><code>EBADF</code></p>
<dd> <i>aio_fildes</i> is not a valid file descriptor open for reading.</p>
<dt><code>EINVAL</code></p>
<dd> One or more of <i>aio_offset</i>, <i>aio_reqprio</i>, or <i>aio_nbytes</i> are invalid.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>aio_read</code>() is not implemented.</p>
<dt><code>EOVERFLOW</code></p>
<dd> The file is a regular file, we start reading before end-of-file and want at least one byte, but the starting position is past the maximum offset for this file.</dl>
<h2>VERSIONS</h2>
<p> The <code>aio_read</code>() function is available since glibc 2.1.</p>
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
<td> <code>aio_read</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> It is a good idea to zero out the control block before use. The control block must not be changed while the read operation is in progress. The buffer area being read into must not be accessed during the operation or undefined results may occur. The memory areas involved must remain valid. </p>
<p> Simultaneous I/O operations specifying the same <i>aiocb</i> structure produce undefined results.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
