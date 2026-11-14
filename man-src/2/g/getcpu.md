---
title: "getcpu(2)"
name: "getcpu"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getcpu/"
description: "getcpu – determine CPU and NUMA node on which the calling thread is running"
---

<h2 class="name">NAME</h2>
<p> getcpu &#8211; determine CPU and NUMA node on which the calling thread is running </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/getcpu.h&gt;
int getcpu(unsigned *cpu, unsigned *node, struct getcpu_cache *tcache);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getcpu</code>() system call identifies the processor and node on which the calling thread or process is currently running and writes them into the integers pointed to by the <i>cpu</i> and <i>node</i> arguments. The processor is a unique small integer identifying a CPU. The node is a unique small identifier identifying a NUMA node. When either <i>cpu</i> or <i>node</i> is NULL nothing is written to the respective pointer. </p>
<p> The third argument to this system call is nowadays unused, and should be specified as NULL unless portability to Linux 2.6.23 or earlier is required (see NOTES). </p>
<p> The information placed in <i>cpu</i> is guaranteed to be current only at the time of the call: unless the CPU affinity has been fixed using <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), the kernel might change the CPU at any time. (Normally this does not happen because the scheduler tries to minimize movements between CPUs to keep caches hot, but it is possible.) The caller must allow for the possibility that the information returned in <i>cpu</i> and <i>node</i> is no longer current by the time the call returns.</p>
<h2>RETURN VALUE</h2>
<p> On success, 0 is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Arguments point outside the calling process&#8217;s address space.</dl>
<h2>VERSIONS</h2>
<p> <code>getcpu</code>() was added in kernel 2.6.19 for x86-64 and i386. Library support was added in glibc 2.29 (Earlier glibc versions did not provide a wrapper for this system call, necessitating the use of <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).)</p>
<h2>CONFORMING TO</h2>
<p> <code>getcpu</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> Linux makes a best effort to make this call as fast as possible. (On some architectures, this is done via an implementation in the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7).) The intention of <code>getcpu</code>() is to allow programs to make optimizations with per-CPU data or for NUMA optimization. </p>
<p> The <i>tcache</i> argument is unused since Linux 2.6.24. In earlier kernels, if this argument was non-NULL, then it specified a pointer to a caller-allocated buffer in thread-local storage that was used to provide a caching mechanism for <code>getcpu</code>(). Use of the cache could speed <code>getcpu</code>() calls, at the cost that there was a very small chance that the returned information would be out of date. The caching mechanism was considered to cause problems when migrating threads between CPUs, and so the argument is now ignored.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/3-sched_getcpu/">sched_getcpu</a></code>(3), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
