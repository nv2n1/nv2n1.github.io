---
title: "pidfd_getfd(2)"
name: "pidfd_getfd"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pidfd_getfd/"
description: "pidfd_getfd – obtain a duplicate of another process’s file descriptor"
---

<h2 class="name">NAME</h2>
<p> pidfd_getfd &#8211; obtain a duplicate of another process&#8217;s file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
int pidfd_getfd(int pidfd, int targetfd, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pidfd_getfd</code>() system call allocates a new file descriptor in the calling process. This new file descriptor is a duplicate of an existing file descriptor, <i>targetfd</i>, in the process referred to by the PID file descriptor <i>pidfd</i>. </p>
<p> The duplicate file descriptor refers to the same open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) as the original file descriptor in the process referred to by <i>pidfd</i>. The two file descriptors thus share file status flags and file offset. Furthermore, operations on the underlying file object (for example, assigning an address to a socket object using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2)) can equally be performed via the duplicate file descriptor. </p>
<p> The close-on-exec flag (<code>FD_CLOEXEC</code>; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) is set on the file descriptor returned by <code>pidfd_getfd</code>(). </p>
<p> The <i>flags</i> argument is reserved for future use. Currently, it must be specified as 0. </p>
<p> Permission to duplicate another process&#8217;s file descriptor is governed by a ptrace access mode <code>PTRACE_MODE_ATTACH_REALCREDS</code> check (see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>pidfd_getfd</code>() returns a file descriptor (a nonnegative integer). On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>pidfd</i> is not a valid PID file descriptor.</p>
<dt><code>EBADF</code></p>
<dd> <i>targetfd</i> is not an open file descriptor in the process referred to by <i>pidfd</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is not 0.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached (see the description of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>EPERM</code></p>
<dd> The calling process did not have <code>PTRACE_MODE_ATTACH_REALCREDS</code> permissions (see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)) over the process referred to by <i>pidfd</i>.</p>
<dt><code>ESRCH</code></p>
<dd> The process referred to by <i>pidfd</i> does not exist (i.e., it has terminated and been waited on).</dl>
<h2>VERSIONS</h2>
<p> <code>pidfd_getfd</code>() first appeared in Linux 5.6.</p>
<h2>CONFORMING TO</h2>
<p> <code>pidfd_getfd</code>() is Linux specific.</p>
<h2>NOTES</h2>
<p> Currently, there is no glibc wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> For a description of PID file descriptors, see <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2). </p>
<p> The effect of <code>pidfd_getfd</code>() is similar to the use of <code>SCM_RIGHTS</code> messages described in <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7), but differs in the following respects:</p>
<dl>
<dt>&bull;</p>
<dd> In order to pass a file descriptor using an <code>SCM_RIGHTS</code> message, the two processes must first establish a UNIX domain socket connection.</p>
<dt>&bull;</p>
<dd> The use of <code>SCM_RIGHTS</code> requires cooperation on the part of the process whose file descriptor is being copied. By contrast, no such cooperation is necessary when using <code>pidfd_getfd</code>().</p>
<dt>&bull;</p>
<dd> The ability to use <code>pidfd_getfd</code>() is restricted by a <code>PTRACE_MODE_ATTACH_REALCREDS</code> ptrace access mode check.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
