---
title: "io_getevents(2)"
name: "io_getevents"
section: "2"
letter: "i"
url: "/docs/linux/man/2-io_getevents/"
description: "io_getevents – read asynchronous I/O events from the completion queue"
---

<h2 class="name">NAME</h2>
<p> io_getevents &#8211; read asynchronous I/O events from the completion queue </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/aio_abi.h&gt; /* Defines needed types */
#include &lt;linux/time.h&gt;    /* Defines 'struct timespec' */
int io_getevents(aio_context_t ctx_id, long min_nr, long nr,
                 struct io_event *events, struct timespec *timeout);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: this page describes the raw Linux system call interface. The wrapper function provided by <i>libaio</i> uses a different type for the <i>ctx_id</i> argument. See NOTES. </p>
<p> The <code>io_getevents</code>() system call attempts to read at least <i>min_nr</i> events and up to <i>nr</i> events from the completion queue of the AIO context specified by <i>ctx_id</i>. </p>
<p> The <i>timeout</i> argument specifies the amount of time to wait for events, and is specified as a relative timeout in a structure of the following form: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;[0 .. 999999999]&nbsp;*/ }; </p>
<p> The specified time will be rounded up to the system clock granularity and is guaranteed not to expire early. </p>
<p> Specifying <i>timeout</i> as NULL means block indefinitely until at least <i>min_nr</i> events have been obtained.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>io_getevents</code>() returns the number of events read. This may be 0, or a value less than <i>min_nr</i>, if the <i>timeout</i> expired. It may also be a nonzero value less than <i>min_nr</i>, if the call was interrupted by a signal handler. </p>
<p> For the failure return, see NOTES.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Either <i>events</i> or <i>timeout</i> is an invalid pointer.</p>
<dt><code>EINTR</code></p>
<dd> Interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>ctx_id</i> is invalid. <i>min_nr</i> is out of range or <i>nr</i> is out of range.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>io_getevents</code>() is not implemented on this architecture.</dl>
<h2>VERSIONS</h2>
<p> The asynchronous I/O system calls first appeared in Linux 2.5.</p>
<h2>CONFORMING TO</h2>
<p> <code>io_getevents</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper function for this system call. You could invoke it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). But instead, you probably want to use the <code>io_getevents</code>() wrapper function provided by <i>libaio</i>. </p>
<p> Note that the <i>libaio</i> wrapper function uses a different type (<i>io_context_t</i>) for the <i>ctx_id</i> argument. Note also that the <i>libaio</i> wrapper does not follow the usual C library conventions for indicating errors: on error it returns a negated error number (the negative of one of the values listed in ERRORS). If the system call is invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), then the return value follows the usual conventions for indicating an error: -1, with <i>errno</i> set to a (positive) value that indicates the error.</p>
<h2>BUGS</h2>
<p> An invalid <i>ctx_id</i> may cause a segmentation fault instead of generating the error <code>EINVAL</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-io_cancel/">io_cancel</a></code>(2), <code><a href="/docs/linux/man/2-io_destroy/">io_destroy</a></code>(2), <code><a href="/docs/linux/man/2-io_setup/">io_setup</a></code>(2), <code><a href="/docs/linux/man/2-io_submit/">io_submit</a></code>(2), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
