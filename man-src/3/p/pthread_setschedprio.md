---
title: "pthread_setschedprio(3)"
name: "pthread_setschedprio"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_setschedprio/"
description: "pthread_setschedprio – set scheduling priority of a thread"
---

<p>pthread_setschedprio &#8211; set scheduling priority of a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_setschedprio(pthread_t thread, int prio);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setschedprio</code>() function sets the scheduling priority of the thread <i>thread</i> to the value specified in <i>prio</i>. (By contrast <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3) changes both the scheduling policy and priority of a thread.)</p>
<h2>Return Value</h2>
<p>On success, this function returns 0; on error, it returns a nonzero error number. If <code>pthread_setschedprio</code>() fails, the scheduling priority of <i>thread</i> is not changed.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>prio</i> is not valid for the scheduling policy of the specified thread.</p>
<dt><code>EPERM</code></p>
<dd>The caller does not have appropriate privileges to set the specified priority.</p>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
<p> POSIX.1 also documents an <code>ENOTSUP</code> (&quot;attempt was made to set the priority to an unsupported value&quot;) error for <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3).</p>
<h2>Versions</h2>
<p>This function is available in glibc since version 2.3.4.</p>
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
<td> <code>pthread_setschedprio</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>For a description of the permissions required to, and the effect of, changing a thread&#8217;s scheduling priority, and details of the permitted ranges for priorities in each scheduling policy, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
