---
title: "io_setup(2)"
name: "io_setup"
section: "2"
letter: "i"
url: "/docs/linux/man/2-io_setup/"
description: "io_setup – create an asynchronous I/O context"
---

<h2 class="name">NAME</h2>
<p> io_setup &#8211; create an asynchronous I/O context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/aio_abi.h&gt; /* Defines needed types */
long io_setup(unsigned nr_events, aio_context_t *ctx_idp);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: this page describes the raw Linux system call interface. The wrapper function provided by <i>libaio</i> uses a different type for the <i>ctx_idp</i> argument. See NOTES. </p>
<p> The <code>io_setup</code>() system call creates an asynchronous I/O context suitable for concurrently processing <i>nr_events</i> operations. The <i>ctx_idp</i> argument must not point to an AIO context that already exists, and must be initialized to 0 prior to the call. On successful creation of the AIO context, <i>*ctx_idp</i> is filled in with the resulting handle.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>io_setup</code>() returns 0. For the failure return, see NOTES.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The specified <i>nr_events</i> exceeds the limit of available events, as defined in <i>/proc/sys/fs/aio-max-nr</i> (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt><code>EFAULT</code></p>
<dd> An invalid pointer is passed for <i>ctx_idp</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>ctx_idp</i> is not initialized, or the specified <i>nr_events</i> exceeds internal limits. <i>nr_events</i> should be greater than 0.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel resources are available.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>io_setup</code>() is not implemented on this architecture.</dl>
<h2>VERSIONS</h2>
<p> The asynchronous I/O system calls first appeared in Linux 2.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>io_setup</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper function for this system call. You could invoke it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). But instead, you probably want to use the <code>io_setup</code>() wrapper function provided by <i>libaio</i>. </p>
<p> Note that the <i>libaio</i> wrapper function uses a different type (<i>io_context_t&nbsp;*</i>) for the <i>ctx_idp</i> argument. Note also that the <i>libaio</i> wrapper does not follow the usual C library conventions for indicating errors: on error it returns a negated error number (the negative of one of the values listed in ERRORS). If the system call is invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then the return value follows the usual conventions for indicating an error: -1, with <i>errno</i> set to a (positive) value that indicates the error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_getevents/">io_getevents</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
