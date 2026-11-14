---
title: "lio_listio(3)"
name: "lio_listio"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lio_listio/"
description: "lio_listio – initiate a list of I/O requests"
---

<h2 class="name">NAME</h2>
<p> lio_listio &#8211; initiate a list of I/O requests </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;aio.h&gt;
int lio_listio(int mode, struct aiocb *const aiocb_list[],
               int nitems, struct sigevent *sevp);
Link with - lrt.
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>lio_listio</code>() function initiates the list of I/O operations described by the array <i>aiocb_list</i>. </p>
<p> The <i>mode</i> operation has one of the following values:</p>
<dl>
<dt><code>LIO_WAIT</code></p>
<dd> The call blocks until all operations are complete. The <i>sevp</i> argument is ignored.</p>
<dt><code>LIO_NOWAIT</code></p>
<dd> The I/O operations are queued for processing and the call returns immediately. When all of the I/O operations complete, asynchronous notification occurs, as specified by the <i>sevp</i> argument; see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for details. If <i>sevp</i> is NULL, no asynchronous notification occurs.</dl>
<p> The <i>aiocb_list</i> argument is an array of pointers to <i>aiocb</i> structures that describe I/O operations. These operations are executed in an unspecified order. The <i>nitems</i> argument specifies the size of the array <i>aiocb_list</i>. null pointers in <i>aiocb_list</i> are ignored. </p>
<p> In each control block in <i>aiocb_list</i>, the <i>aio_lio_opcode</i> field specifies the I/O operation to be initiated, as follows:</p>
<dl>
<dt><code>LIO_READ</code></p>
<dd> Initiate a read operation. The operation is queued as for a call to <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3) specifying this control block.</p>
<dt><code>LIO_WRITE</code></p>
<dd> Initiate a write operation. The operation is queued as for a call to <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3) specifying this control block.</p>
<dt><code>LIO_NOP</code></p>
<dd> Ignore this control block.</dl>
<p> The remaining fields in each control block have the same meanings as for <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3) and <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3). The <i>aio_sigevent</i> fields of each control block can be used to specify notifications for the individual I/O operations (see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)).</p>
<h2>RETURN VALUE</h2>
<p> If <i>mode</i> is <code>LIO_NOWAIT</code>, <code>lio_listio</code>() returns 0 if all I/O operations are successfully queued. Otherwise, -1 is returned, and <i>errno</i> is set to indicate the error. </p>
<p> If <i>mode</i> is <code>LIO_WAIT</code>, <code>lio_listio</code>() returns 0 when all of the I/O operations have completed successfully. Otherwise, -1 is returned, and <i>errno</i> is set to indicate the error. </p>
<p> The return status from <code>lio_listio</code>() provides information only about the call itself, not about the individual I/O operations. One or more of the I/O operations may fail, but this does not prevent other operations completing. The status of individual I/O operations in <i>aiocb_list</i> can be determined using <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3). When an operation has completed, its return status can be obtained using <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3). Individual I/O operations can fail for the reasons described in <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3) and <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3).</p>
<h2>ERRORS</h2>
<p> The <code>lio_listio</code>() function may fail for the following reasons:</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Out of resources.</p>
<dt><code>EAGAIN</code></p>
<dd> The number of I/O operations specified by <i>nitems</i> would cause the limit <code>AIO_MAX</code> to be exceeded.</p>
<dt><code>EINTR</code></p>
<dd> <i>mode</i> was <code>LIO_WAIT</code> and a signal was caught before all I/O operations completed; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). (This may even be one of the signals used for asynchronous I/O completion notification.)</p>
<dt><code>EINVAL</code></p>
<dd> <i>mode</i> is invalid, or <i>nitems</i> exceeds the limit <code>AIO_LISTIO_MAX</code>.</p>
<dt><code>EIO</code></p>
<dd> One of more of the operations specified by <i>aiocb_list</i> failed. The application can check the status of each operation using <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3).</dl>
<p> If <code>lio_listio</code>() fails with the error <code>EAGAIN</code>, <code>EINTR</code>, or <code>EIO</code>, then some of the operations in <i>aiocb_list</i> may have been initiated. If <code>lio_listio</code>() fails for any other reason, then none of the I/O operations has been initiated.</p>
<h2>VERSIONS</h2>
<p> The <code>lio_listio</code>() function is available since glibc 2.1.</p>
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
<td> <code>lio_listio</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> It is a good idea to zero out the control blocks before use. The control blocks must not be changed while the I/O operations are in progress. The buffer areas being read into or written from must not be accessed during the operations or undefined results may occur. The memory areas involved must remain valid. </p>
<p> Simultaneous I/O operations specifying the same <i>aiocb</i> structure produce undefined results.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-aio_cancel/">aio_cancel</a></code>(3), <code><a href="/docs/linux/man/3-aio_error/">aio_error</a></code>(3), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_return/">aio_return</a></code>(3), <code><a href="/docs/linux/man/3-aio_suspend/">aio_suspend</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
