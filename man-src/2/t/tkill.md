---
title: "tkill(2)"
name: "tkill"
section: "2"
letter: "t"
url: "/docs/linux/man/2-tkill/"
description: "tkill, tgkill – send a signal to a thread"
---

<h2 class="name">NAME</h2>
<p> tkill, tgkill &#8211; send a signal to a thread </p>
<h2>SYNOPSIS</h2>
<pre><code>
int tkill(int tid, int sig);
int tgkill(int tgid, int tid, int sig);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for <code>tkill</code>(); see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>tgkill</code>() sends the signal <i>sig</i> to the thread with the thread ID <i>tid</i> in the thread group <i>tgid</i>. (By contrast, <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) can be used to send a signal only to a process (i.e., thread group) as a whole, and the signal will be delivered to an arbitrary thread within that process.) </p>
<p> <code>tkill</code>() is an obsolete predecessor to <code>tgkill</code>(). It allows only the target thread ID to be specified, which may result in the wrong thread being signaled if a thread terminates and its thread ID is recycled. Avoid using this system call. </p>
<p> These are the raw system call interfaces, meant for internal thread library use.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The <code>RLIMIT_SIGPENDING</code> resource limit was reached and <i>sig</i> is a real-time signal.</p>
<dt><code>EAGAIN</code></p>
<dd> Insufficient kernel memory was available and <i>sig</i> is a real-time signal.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid thread ID, thread group ID, or signal was specified.</p>
<dt><code>EPERM</code></p>
<dd> Permission denied. For the required permissions, see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<dt><code>ESRCH</code></p>
<dd> No process with the specified thread ID (and thread group ID) exists.</dl>
<h2>VERSIONS</h2>
<p> <code>tkill</code>() is supported since Linux 2.4.19 / 2.5.4. <code>tgkill</code>() was added in Linux 2.5.75. </p>
<p> Library support for <code>tgkill</code>() was added to glibc in version 2.30.</p>
<h2>CONFORMING TO</h2>
<p> <code>tkill</code>() and <code>tgkill</code>() are Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> See the description of <code>CLONE_THREAD</code> in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) for an explanation of thread groups. </p>
<p> Glibc does not provide a wrapper for <code>tkill</code>(); call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). Before glibc 2.30, there was also no wrapper function for <code>tgkill</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
