---
title: "pthread_attr_setaffinity_np(3)"
name: "pthread_attr_setaffinity_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_setaffinity_np/"
description: "pthread_attr_setaffinity_np, pthread_attr_getaffinity_np – set/get CPU affinity attribute in thread attributes object"
---

<p>pthread_attr_setaffinity_np, pthread_attr_getaffinity_np &#8211; set/get CPU affinity attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_attr_setaffinity_np(pthread_attr_t *attr,
                                size_t cpusetsize, const cpu_set_t *cpuset);
int pthread_attr_getaffinity_np(const pthread_attr_t *attr,
                                size_t cpusetsize, cpu_set_t *cpuset);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setaffinity_np</code>() function sets the CPU affinity mask attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>cpuset</i>. This attribute determines the CPU affinity mask of a thread created using the thread attributes object <i>attr</i>. </p>
<p> The <code>pthread_attr_getaffinity_np</code>() function returns the CPU affinity mask attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>cpuset</i>. </p>
<p> The argument <i>cpusetsize</i> is the length (in bytes) of the buffer pointed to by <i>cpuset</i>. Typically, this argument would be specified as <i>sizeof(cpu_set_t)</i>. </p>
<p> For more details on CPU affinity masks, see <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2). For a description of a set of macros that can be used to manipulate and inspect CPU sets, see <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_attr_setaffinity_np</code>()) <i>cpuset</i> specified a CPU that was outside the set supported by the kernel. (The kernel configuration option <code>CONFIG_NR_CPUS</code> defines the range of the set supported by the kernel data type used to represent CPU sets.)</p>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_attr_getaffinity_np</code>()) A CPU in the affinity mask of the thread attributes object referred to by <i>attr</i> lies outside the range specified by <i>cpusetsize</i> (i.e., <i>cpuset</i>/<i>cpusetsize</i> is too small).</p>
<dt><code>ENOMEM</code></p>
<dd>(<code>pthread_attr_setaffinity_np</code>()) Could not allocate memory.</dl>
<h2>Versions</h2>
<p>These functions are provided by glibc since version 2.3.4.</p>
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
<td> <code>pthread_attr_setaffinity_np</code>(), <code>pthread_attr_getaffinity_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>Notes</h2>
<p>In glibc 2.3.3 only, versions of these functions were provided that did not have a <i>cpusetsize</i> argument. Instead the CPU set size given to the underlying system calls was always <i>sizeof(cpu_set_t)</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setaffinity_np/">pthread_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
