---
title: "io_destroy(2)"
name: "io_destroy"
section: "2"
letter: "i"
url: "/docs/linux/man/2-io_destroy/"
description: "io_destroy – destroy an asynchronous I/O context"
---

<h2 class="name">NAME</h2>
<p> io_destroy &#8211; destroy an asynchronous I/O context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/aio_abi.h&gt; /* Defines needed types */
int io_destroy(aio_context_t ctx_id);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: this page describes the raw Linux system call interface. The wrapper function provided by <i>libaio</i> uses a different type for the <i>ctx_id</i> argument. See NOTES. </p>
<p> The <code>io_destroy</code>() system call will attempt to cancel all outstanding asynchronous I/O operations against <i>ctx_id</i>, will block on the completion of all operations that could not be canceled, and will destroy the <i>ctx_id</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>io_destroy</code>() returns 0. For the failure return, see NOTES.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The context pointed to is invalid.</p>
<dt><code>EINVAL</code></p>
<dd> The AIO context specified by <i>ctx_id</i> is invalid.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>io_destroy</code>() is not implemented on this architecture.</dl>
<h2>VERSIONS</h2>
<p> The asynchronous I/O system calls first appeared in Linux 2.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>io_destroy</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper function for this system call. You could invoke it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). But instead, you probably want to use the <code>io_destroy</code>() wrapper function provided by <i>libaio</i>. </p>
<p> Note that the <i>libaio</i> wrapper function uses a different type (<i>io_context_t</i>) for the <i>ctx_id</i> argument. Note also that the <i>libaio</i> wrapper does not follow the usual C library conventions for indicating errors: on error it returns a negated error number (the negative of one of the values listed in ERRORS). If the system call is invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then the return value follows the usual conventions for indicating an error: -1, with <i>errno</i> set to a (positive) value that indicates the error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
