---
title: "sched_get_priority_max(2)"
name: "sched_get_priority_max"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_get_priority_max/"
description: "sched_get_priority_max, sched_get_priority_min – get static priority range"
---

<h2 class="name">NAME</h2>
<p> sched_get_priority_max, sched_get_priority_min &#8211; get static priority range </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sched.h&gt;</code> </p>
<p> <code>int sched_get_priority_max(int </code><i>policy</i><code>);</code> </p>
<p> <code>int sched_get_priority_min(int </code><i>policy</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sched_get_priority_max</code>() returns the maximum priority value that can be used with the scheduling algorithm identified by <i>policy</i>. <code>sched_get_priority_min</code>() returns the minimum priority value that can be used with the scheduling algorithm identified by <i>policy</i>. Supported <i>policy</i> values are <code>SCHED_FIFO</code>, <code>SCHED_RR</code>, <code>SCHED_OTHER</code>, <code>SCHED_BATCH</code>, <code>SCHED_IDLE</code>, and <code>SCHED_DEADLINE</code>. Further details about these policies can be found in <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> Processes with numerically higher priority values are scheduled before processes with numerically lower priority values. Thus, the value returned by <code>sched_get_priority_max</code>() will be greater than the value returned by <code>sched_get_priority_min</code>(). </p>
<p> Linux allows the static priority range 1 to 99 for the <code>SCHED_FIFO</code> and <code>SCHED_RR</code> policies, and the priority 0 for the remaining policies. Scheduling priority ranges for the various policies are not alterable. </p>
<p> The range of scheduling priorities may vary on other POSIX systems, thus it is a good idea for portable applications to use a virtual priority range and map it to the interval given by <code>sched_get_priority_max</code>() and <code>sched_get_priority_min</code> POSIX.1 requires a spread of at least 32 between the maximum and the minimum values for <code>SCHED_FIFO</code> and <code>SCHED_RR</code>. </p>
<p> POSIX systems on which <code>sched_get_priority_max</code>() and <code>sched_get_priority_min</code>() are available define <code>_POSIX_PRIORITY_SCHEDULING</code> in <i>&lt;unistd.h&gt;</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_get_priority_max</code>() and <code>sched_get_priority_min</code>() return the maximum/minimum priority value for the named scheduling policy. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The argument <i>policy</i> does not identify a defined scheduling policy.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
