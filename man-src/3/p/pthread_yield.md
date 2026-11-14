---
title: "pthread_yield(3)"
name: "pthread_yield"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_yield/"
description: "pthread_yield – yield the processor"
---

<p>pthread_yield &#8211; yield the processor</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_yield(void);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p><code>pthread_yield</code>() causes the calling thread to relinquish the CPU. The thread is placed at the end of the run queue for its static priority and another thread is scheduled to run. For further details, see <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2)</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_yield</code>() returns 0; on error, it returns an error number.</p>
<h2>Errors</h2>
<p>On Linux, this call always succeeds (but portable and future-proof applications should nevertheless handle a possible error return).</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_yield</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This call is nonstandard, but present on several other systems. Use the standardized <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2) instead.</p>
<h2>Notes</h2>
<p>On Linux, this function is implemented as a call to <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2). </p>
<p> <code>pthread_yield</code>() is intended for use with real-time scheduling policies (i.e., <code>SCHED_FIFO</code> or <code>SCHED_RR</code>). Use of <code>pthread_yield</code>() with nondeterministic scheduling policies such as <code>SCHED_OTHER</code> is unspecified and very likely means your application design is broken.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
