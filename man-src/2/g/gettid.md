---
title: "gettid(2)"
name: "gettid"
section: "2"
letter: "g"
url: "/docs/linux/man/2-gettid/"
description: "gettid – get thread identification"
---

<h2 class="name">NAME</h2>
<p> gettid &#8211; get thread identification </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
pid_t gettid(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>gettid</code>() returns the caller&#8217;s thread ID (TID). In a single-threaded process, the thread ID is equal to the process ID (PID, as returned by <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)). In a multithreaded process, all threads have the same PID, but each one has a unique TID. For further details, see the discussion of <code>CLONE_THREAD</code> in <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, returns the thread ID of the calling thread.</p>
<h2>ERRORS</h2>
<p> This call is always successful.</p>
<h2>VERSIONS</h2>
<p> The <code>gettid</code>() system call first appeared on Linux in kernel 2.4.11. Library support was added in glibc 2.30. (Earlier glibc versions did not provide a wrapper for this system call, necessitating the use of <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).)</p>
<h2>CONFORMING TO</h2>
<p> <code>gettid</code>() is Linux-specific and should not be used in programs that are intended to be portable.</p>
<h2>NOTES</h2>
<p> The thread ID returned by this call is not the same thing as a POSIX thread ID (i.e., the opaque value returned by <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3)). </p>
<p> In a new thread group created by a <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) call that does not specify the <code>CLONE_THREAD</code> flag (or, equivalently, a new process created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)), the new process is a thread group leader, and its thread group ID (the value returned by <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2)) is the same as its thread ID (the value returned by <code>gettid</code>()).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-capget/">capget</a></code>(2), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-tgkill/">tgkill</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
