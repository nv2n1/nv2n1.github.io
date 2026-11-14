---
title: "vtimes(3)"
name: "vtimes"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vtimes/"
description: "getrusage – get resource usage"
---

<p>getrusage &#8211; get resource usage</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/time.h&gt;

#include &lt;sys/resource.h&gt;
int getrusage(int who, struct rusage *usage);</code></pre>
<h2>Description</h2>
<p><code>getrusage</code>() returns resource usage measures for <i>who</i>, which can be one of the following:</p>
<dl>
<dt><code>RUSAGE_SELF</code></p>
<dd>Return resource usage statistics for the calling process, which is the sum of resources used by all threads in the process.</p>
<dt><code>RUSAGE_CHILDREN</code></p>
<dd>Return resource usage statistics for all children of the calling process that have terminated and been waited for. These statistics will include the resources used by grandchildren, and further removed descendants, if all of the intervening descendants waited on their terminated children.</p>
<dt><code>RUSAGE_THREAD</code> (since Linux 2.6.26)</p>
<dd>Return resource usage statistics for the calling thread. The <code>_GNU_SOURCE</code> feature test macro must be defined (before including <i>any</i> header file) in order to obtain the definition of this constant from <i>&lt;sys/resource.h&gt;</i>.</dl>
<p> The resource usages are returned in the structure pointed to by <i>usage</i>, which has the following form: </p>
<pre><code>struct rusage {
    struct timeval ru_utime; /* user CPU time used */
    struct timeval ru_stime; /* system CPU time used */
    long ru_maxrss;          /* maximum resident set size */
    long ru_ixrss;           /* integral shared memory size */
    long ru_idrss;           /* integral unshared data size */
    long ru_isrss;           /* integral unshared stack size */
    long ru_minflt;          /* page reclaims (soft page faults) */
    long ru_majflt;          /* page faults (hard page faults) */
    long ru_nswap;           /* swaps */
    long ru_inblock;         /* block input operations */
    long ru_oublock;         /* block output operations */
    long ru_msgsnd;          /* IPC messages sent */
    long ru_msgrcv;          /* IPC messages received */
    long ru_nsignals;        /* signals received */
    long ru_nvcsw;           /* voluntary context switches */
    long ru_nivcsw;          /* involuntary context switches */
};</code></pre>
<p> Not all fields are completed; unmaintained fields are set to zero by the kernel. (The unmaintained fields are provided for compatibility with other systems, and because they may one day be supported on Linux.) The fields are interpreted as follows:</p>
<dl>
<dt><i>ru_utime</i></p>
<dd>This is the total amount of time spent executing in user mode, expressed in a <i>timeval</i> structure (seconds plus microseconds).</p>
<dt><i>ru_stime</i></p>
<dd>This is the total amount of time spent executing in kernel mode, expressed in a <i>timeval</i> structure (seconds plus microseconds).</p>
<dt><i>ru_maxrss</i> (since Linux 2.6.32)</p>
<dd>This is the maximum resident set size used (in kilobytes). For <code>RUSAGE_CHILDREN</code>, this is the resident set size of the largest child, not the maximum resident set size of the process tree.</p>
<dt><i>ru_ixrss</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_idrss</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_isrss</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_minflt</i></p>
<dd>The number of page faults serviced without any I/O activity; here I/O activity is avoided by &#8220;reclaiming&#8221; a page frame from the list of pages awaiting reallocation.</p>
<dt><i>ru_majflt</i></p>
<dd>The number of page faults serviced that required I/O activity.</p>
<dt><i>ru_nswap</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_inblock</i> (since Linux 2.6.22)</p>
<dd>The number of times the filesystem had to perform input.</p>
<dt><i>ru_oublock</i> (since Linux 2.6.22)</p>
<dd>The number of times the filesystem had to perform output.</p>
<dt><i>ru_msgsnd</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_msgrcv</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_nsignals</i> (unmaintained)</p>
<dd>This field is currently unused on Linux.</p>
<dt><i>ru_nvcsw</i> (since Linux 2.6)</p>
<dd>The number of times a context switch resulted due to a process voluntarily giving up the processor before its time slice was completed (usually to await availability of a resource).</p>
<dt><i>ru_nivcsw</i> (since Linux 2.6)</p>
<dd>The number of times a context switch resulted due to a higher priority process becoming runnable or because the current process exceeded its time slice.</dl>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd><i>usage</i> points outside the accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd><i>who</i> is invalid.</dl>
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
<td> <code>getrusage</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. POSIX.1 specifies <code>getrusage</code>(), but specifies only the fields <i>ru_utime</i> and <i>ru_stime</i>. </p>
<p> <code>RUSAGE_THREAD</code> is Linux-specific.</p>
<h2>Notes</h2>
<p>Resource usage metrics are preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Including <i>&lt;sys/time.h&gt;</i> is not required these days, but increases portability. (Indeed, <i>struct timeval</i> is defined in <i>&lt;sys/time.h&gt;</i>.) </p>
<p> In Linux kernel versions before 2.6.9, if the disposition of <code>SIGCHLD</code> is set to <code>SIG_IGN</code> then the resource usages of child processes are automatically included in the value returned by <code>RUSAGE_CHILDREN</code>, although POSIX.1-2001 explicitly prohibits this. This nonconformance is rectified in Linux 2.6.9 and later. </p>
<p> The structure definition shown at the start of this page was taken from 4.3BSD Reno. </p>
<p> Ancient systems provided a <code>vtimes</code>() function with a similar purpose to <code>getrusage</code>(). For backward compatibility, glibc (up until version 2.32) also provides <code>vtimes</code>(). All new applications should be written using <code>getrusage</code>(). </p>
<p> See also the description of <i>/proc/[pid]/stat</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-times/">times</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), <code><a href="/docs/linux/man/3-clock/">clock</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
