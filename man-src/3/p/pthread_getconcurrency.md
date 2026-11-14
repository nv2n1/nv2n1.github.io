---
title: "pthread_getconcurrency(3)"
name: "pthread_getconcurrency"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_getconcurrency/"
description: "pthread_setconcurrency, pthread_getconcurrency – set/get the concurrency level"
---

<p>pthread_setconcurrency, pthread_getconcurrency &#8211; set/get the concurrency level</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_setconcurrency(int new_level);
int pthread_getconcurrency(void);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setconcurrency</code>() function informs the implementation of the application&#8217;s desired concurrency level, specified in <i>new_level</i>. The implementation takes this only as a hint: POSIX.1 does not specify the level of concurrency that should be provided as a result of calling <code>pthread_setconcurrency</code>(). </p>
<p> Specifying <i>new_level</i> as 0 instructs the implementation to manage the concurrency level as it deems appropriate. </p>
<p> <code>pthread_getconcurrency</code>() returns the current value of the concurrency level for this process.</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_setconcurrency</code>() returns 0; on error, it returns a nonzero error number. </p>
<p> <code>pthread_getconcurrency</code>() always succeeds, returning the concurrency level set by a previous call to <code>pthread_setconcurrency</code>(), or 0, if <code>pthread_setconcurrency</code>() has not previously been called.</p>
<h2>Errors</h2>
<p><code>pthread_setconcurrency</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>new_level</i> is negative.</dl>
<p> POSIX.1 also documents an <code>EAGAIN</code> error (&quot;the value specified by <i>new_level</i> would cause a system resource to be exceeded&quot;).</p>
<h2>Versions</h2>
<p>These functions are available in glibc since version 2.1.</p>
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
<td> <code>pthread_setconcurrency</code>(), <code>pthread_getconcurrency</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The default concurrency level is 0. </p>
<p> Concurrency levels are meaningful only for M:N threading implementations, where at any moment a subset of a process&#8217;s set of user-level threads may be bound to a smaller number of kernel-scheduling entities. Setting the concurrency level allows the application to give the system a hint as to the number of kernel-scheduling entities that should be provided for efficient execution of the application. </p>
<p> Both LinuxThreads and NPTL are 1:1 threading implementations, so setting the concurrency level has no meaning. In other words, on Linux these functions merely exist for compatibility with other systems, and they have no effect on the execution of a program.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_setscope/">pthread_attr_setscope</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
