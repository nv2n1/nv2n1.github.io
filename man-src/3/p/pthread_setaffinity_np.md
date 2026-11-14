---
title: "pthread_setaffinity_np(3)"
name: "pthread_setaffinity_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_setaffinity_np/"
description: "pthread_setaffinity_np, pthread_getaffinity_np – set/get CPU affinity of a thread"
---

<p>pthread_setaffinity_np, pthread_getaffinity_np &#8211; set/get CPU affinity of a thread</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_setaffinity_np(pthread_t thread, size_t cpusetsize,
                           const cpu_set_t *cpuset);
int pthread_getaffinity_np(pthread_t thread, size_t cpusetsize,
                           cpu_set_t *cpuset);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setaffinity_np</code>() function sets the CPU affinity mask of the thread <i>thread</i> to the CPU set pointed to by <i>cpuset</i>. If the call is successful, and the thread is not currently running on one of the CPUs in <i>cpuset</i>, then it is migrated to one of those CPUs. </p>
<p> The <code>pthread_getaffinity_np</code>() function returns the CPU affinity mask of the thread <i>thread</i> in the buffer pointed to by <i>cpuset</i>. </p>
<p> For more details on CPU affinity masks, see <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2). For a description of a set of macros that can be used to manipulate and inspect CPU sets, see <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3). </p>
<p> The argument <i>cpusetsize</i> is the length (in bytes) of the buffer pointed to by <i>cpuset</i>. Typically, this argument would be specified as <i>sizeof(cpu_set_t)</i>. (It may be some other value, if using the macros described in <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3) for dynamically allocating a CPU set.)</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd>A supplied memory address was invalid.</p>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_setaffinity_np</code>()) The affinity bit mask <i>mask</i> contains no processors that are currently physically on the system and permitted to the thread according to any restrictions that may be imposed by the &quot;cpuset&quot; mechanism described in <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_setaffinity_np</code>()) <i>cpuset</i> specified a CPU that was outside the set supported by the kernel. (The kernel configuration option <code>CONFIG_NR_CPUS</code> defines the range of the set supported by the kernel data type used to represent CPU sets.)</p>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_getaffinity_np</code>()) <i>cpusetsize</i> is smaller than the size of the affinity mask used by the kernel.</p>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
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
<td> <code>pthread_setaffinity_np</code>(), <code>pthread_getaffinity_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>Notes</h2>
<p>After a call to <code>pthread_setaffinity_np</code>(), the set of CPUs on which the thread will actually run is the intersection of the set specified in the <i>cpuset</i> argument and the set of CPUs actually present on the system. The system may further restrict the set of CPUs on which the thread runs if the &quot;cpuset&quot; mechanism described in <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7) is being used. These restrictions on the actual set of CPUs on which the thread will run are silently imposed by the kernel. </p>
<p> These functions are implemented on top of the <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) and <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2) system calls. </p>
<p> In glibc 2.3.3 only, versions of these functions were provided that did not have a <i>cpusetsize</i> argument. Instead the CPU set size given to the underlying system calls was always <i>sizeof(cpu_set_t)</i>. </p>
<p> A new thread created by <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) inherits a copy of its creator&#8217;s CPU affinity mask.</p>
<h2>Examples</h2>
<p>In the following program, the main thread uses <code>pthread_setaffinity_np</code>() to set its CPU affinity mask to include CPUs 0 to 7 (which may not all be available on the system), and then calls <code>pthread_getaffinity_np</code>() to check the resulting CPU affinity mask of the thread. </p>
<pre><code>#define _GNU_SOURCE
#include &lt;errno.h&gt;
#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)
int main(int argc, char *argv[])
{
    int s;
    cpu_set_t cpuset;
    pthread_t thread;
    thread = pthread_self();
    /* Set affinity mask to include CPUs 0 to 7 */
    CPU_ZERO(&amp;cpuset);
    for (int j = 0; j &lt; 8; j++)
        CPU_SET(j, &amp;cpuset);
    s = pthread_setaffinity_np(thread, sizeof(cpuset), &amp;cpuset);
    if (s != 0)
        handle_error_en(s, &quot;pthread_setaffinity_np&quot;);
    /* Check the actual affinity mask assigned to the thread */
    s = pthread_getaffinity_np(thread, sizeof(cpuset), &amp;cpuset);
    if (s != 0)
        handle_error_en(s, &quot;pthread_getaffinity_np&quot;);
    printf(&quot;Set returned by pthread_getaffinity_np() contained:
&quot;);
    for (int j = 0; j &lt; CPU_SETSIZE; j++)
        if (CPU_ISSET(j, &amp;cpuset))
            printf(&quot;    CPU %d
&quot;, j);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setaffinity_np/">pthread_attr_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/3-sched_getcpu/">sched_getcpu</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
