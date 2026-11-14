---
title: "io_cancel(2)"
name: "io_cancel"
section: "2"
letter: "i"
url: "/docs/linux/man/2-io_cancel/"
description: "io_cancel – cancel an outstanding asynchronous I/O operation"
---

<h2 class="name">NAME</h2>
<p> io_cancel &#8211; cancel an outstanding asynchronous I/O operation </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/aio_abi.h&gt; /* Defines needed types */
int io_cancel(aio_context_t ctx_id, struct iocb *iocb,
              struct io_event *result);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: this page describes the raw Linux system call interface. The wrapper function provided by <i>libaio</i> uses a different type for the <i>ctx_id</i> argument. See NOTES. </p>
<p> The <code>io_cancel</code>() system call attempts to cancel an asynchronous I/O operation previously submitted with <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2). The <i>iocb</i> argument describes the operation to be canceled and the <i>ctx_id</i> argument is the AIO context to which the operation was submitted. If the operation is successfully canceled, the event will be copied into the memory pointed to by <i>result</i> without being placed into the completion queue.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>io_cancel</code>() returns 0. For the failure return, see NOTES.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The <i>iocb</i> specified was not canceled.</p>
<dt><code>EFAULT</code></p>
<dd> One of the data structures points to invalid data.</p>
<dt><code>EINVAL</code></p>
<dd> The AIO context specified by <i>ctx_id</i> is invalid.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>io_cancel</code>() is not implemented on this architecture.</dl>
<h2>VERSIONS</h2>
<p> The asynchronous I/O system calls first appeared in Linux 2.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>io_cancel</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper function for this system call. You could invoke it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). But instead, you probably want to use the <code>io_cancel</code>() wrapper function provided by <i>libaio</i>. </p>
<p> Note that the <i>libaio</i> wrapper function uses a different type (<i>io_context_t</i>) for the <i>ctx_id</i> argument. Note also that the <i>libaio</i> wrapper does not follow the usual C library conventions for indicating errors: on error it returns a negated error number (the negative of one of the values listed in ERRORS). If the system call is invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then the return value follows the usual conventions for indicating an error: -1, with <i>errno</i> set to a (positive) value that indicates the error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
