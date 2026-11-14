---
title: "sched_yield(2)"
name: "sched_yield"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_yield/"
description: "sched_yield – yield the processor"
---

<h2 class="name">NAME</h2>
<p> sched_yield &#8211; yield the processor </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sched.h&gt;</code> </p>
<p> <code>int sched_yield(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sched_yield</code>() causes the calling thread to relinquish the CPU. The thread is moved to the end of the queue for its static priority and a new thread gets to run.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_yield</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> In the Linux implementation, <code>sched_yield</code>() always succeeds.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> If the calling thread is the only thread in the highest priority list at that time, it will continue to run after a call to <code>sched_yield</code>(). </p>
<p> POSIX systems on which <code>sched_yield</code>() is available define <code>_POSIX_PRIORITY_SCHEDULING</code> in <i>&lt;unistd.h&gt;</i>. </p>
<p> Strategic calls to <code>sched_yield</code>() can improve performance by giving other threads or processes a chance to run when (heavily) contended resources (e.g., mutexes) have been released by the caller. Avoid calling <code>sched_yield</code>() unnecessarily or inappropriately (e.g., when resources needed by other schedulable threads are still held by the caller), since doing so will result in unnecessary context switches, which will degrade system performance. </p>
<p> <code>sched_yield</code>() is intended for use with real-time scheduling policies (i.e., <code>SCHED_FIFO</code> or <code>SCHED_RR</code>). Use of <code>sched_yield</code>() with nondeterministic scheduling policies such as <code>SCHED_OTHER</code> is unspecified and very likely means your application design is broken.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
