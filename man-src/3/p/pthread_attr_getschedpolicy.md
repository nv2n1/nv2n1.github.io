---
title: "pthread_attr_getschedpolicy(3)"
name: "pthread_attr_getschedpolicy"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_getschedpolicy/"
description: "pthread_attr_setschedpolicy, pthread_attr_getschedpolicy – set/get scheduling policy attribute in thread attributes object"
---

<p>pthread_attr_setschedpolicy, pthread_attr_getschedpolicy &#8211; set/get scheduling policy attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setschedpolicy(pthread_attr_t *attr, int policy);
int pthread_attr_getschedpolicy(const pthread_attr_t *attr, int *policy);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setschedpolicy</code>() function sets the scheduling policy attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>policy</i>. This attribute determines the scheduling policy of a thread created using the thread attributes object <i>attr</i>. </p>
<p> The supported values for <i>policy</i> are <code>SCHED_FIFO</code>, <code>SCHED_RR</code>, and <code>SCHED_OTHER</code>, with the semantics described in <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> The <code>pthread_attr_getschedpolicy</code>() returns the scheduling policy attribute of the thread attributes object <i>attr</i> in the buffer pointed to by <i>policy</i>. </p>
<p> In order for the policy setting made by <code>pthread_attr_setschedpolicy</code>() to have effect when calling <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), the caller must use <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3) to set the inherit-scheduler attribute of the attributes object <i>attr</i> to <code>PTHREAD_EXPLICIT_SCHED</code>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setschedpolicy</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>Invalid value in <i>policy</i>.</dl>
<p> POSIX.1 also documents an optional <code>ENOTSUP</code> error (&quot;attempt was made to set the attribute to an unsupported value&quot;) for <code>pthread_attr_setschedpolicy</code>().</p>
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
<td> <code>pthread_attr_setschedpolicy</code>(), <code>pthread_attr_getschedpolicy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
