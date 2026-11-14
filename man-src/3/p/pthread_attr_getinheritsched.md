---
title: "pthread_attr_getinheritsched(3)"
name: "pthread_attr_getinheritsched"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_getinheritsched/"
description: "pthread_attr_setinheritsched, pthread_attr_getinheritsched – set/get inherit-scheduler attribute in thread attributes object"
---

<p>pthread_attr_setinheritsched, pthread_attr_getinheritsched &#8211; set/get inherit-scheduler attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setinheritsched(pthread_attr_t *attr,
                                 int inheritsched);
int pthread_attr_getinheritsched(const pthread_attr_t *attr,
                                 int *inheritsched);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setinheritsched</code>() function sets the inherit-scheduler attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>inheritsched</i>. The inherit-scheduler attribute determines whether a thread created using the thread attributes object <i>attr</i> will inherit its scheduling attributes from the calling thread or whether it will take them from <i>attr</i>. </p>
<p> The following scheduling attributes are affected by the inherit-scheduler attribute: scheduling policy (<code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3)), scheduling priority (<code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3)), and contention scope (<code><a href="/docs/linux/man/3-pthread_attr_setscope/">pthread_attr_setscope</a></code>(3)). </p>
<p> The following values may be specified in <i>inheritsched</i>:</p>
<dl>
<dt><code>PTHREAD_INHERIT_SCHED</code></p>
<dd>Threads that are created using <i>attr</i> inherit scheduling attributes from the creating thread; the scheduling attributes in <i>attr</i> are ignored.</p>
<dt><code>PTHREAD_EXPLICIT_SCHED</code></p>
<dd>Threads that are created using <i>attr</i> take their scheduling attributes from the values specified by the attributes object.</dl>
<p> The default setting of the inherit-scheduler attribute in a newly initialized thread attributes object is <code>PTHREAD_INHERIT_SCHED</code>. </p>
<p> The <code>pthread_attr_getinheritsched</code>() returns the inherit-scheduler attribute of the thread attributes object <i>attr</i> in the buffer pointed to by <i>inheritsched</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setinheritsched</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>Invalid value in <i>inheritsched</i>.</dl>
<p> POSIX.1 also documents an optional <code>ENOTSUP</code> error (&quot;attempt was made to set the attribute to an unsupported value&quot;) for <code>pthread_attr_setinheritsched</code>().</p>
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
<td> <code>pthread_attr_setinheritsched</code>(), <code>pthread_attr_getinheritsched</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Bugs</h2>
<p>As at glibc 2.8, if a thread attributes object is initialized using <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), then the scheduling policy of the attributes object is set to <code>SCHED_OTHER</code> and the scheduling priority is set to 0. However, if the inherit-scheduler attribute is then set to <code>PTHREAD_EXPLICIT_SCHED</code>, then a thread created using the attribute object wrongly inherits its scheduling attributes from the creating thread. This bug does not occur if either the scheduling policy or scheduling priority attribute is explicitly set in the thread attributes object before calling <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3).</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setscope/">pthread_attr_setscope</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
