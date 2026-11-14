---
title: "sched_rr_get_interval(2)"
name: "sched_rr_get_interval"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_rr_get_interval/"
description: "sched_rr_get_interval – get the SCHED_RR interval for the named process"
---

<h2 class="name">NAME</h2>
<p> sched_rr_get_interval &#8211; get the SCHED_RR interval for the named process </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sched.h&gt;</code> </p>
<p> <code>int sched_rr_get_interval(pid_t </code><i>pid</i><code>, struct timespec *</code><i>tp</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>sched_rr_get_interval</code>() writes into the <i>timespec</i> structure pointed to by <i>tp</i> the round-robin time quantum for the process identified by <i>pid</i>. The specified process should be running under the <code>SCHED_RR</code> scheduling policy. </p>
<p> The <i>timespec</i> structure has the following form: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> If <i>pid</i> is zero, the time quantum for the calling process is written into <i>*tp</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_rr_get_interval</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Problem with copying information to user space.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid pid.</p>
<dt><code>ENOSYS</code></p>
<dd> The system call is not yet implemented (only on rather old kernels).</p>
<dt><code>ESRCH</code></p>
<dd> Could not find a process with the ID <i>pid</i>.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> POSIX systems on which <code>sched_rr_get_interval</code>() is available define <code>_POSIX_PRIORITY_SCHEDULING</code> in <i>&lt;unistd.h&gt;</i>.</p>
<h3>Linux notes</h3>
<p> POSIX does not specify any mechanism for controlling the size of the round-robin time quantum. Older Linux kernels provide a (nonportable) method of doing this. The quantum can be controlled by adjusting the process&#8217;s nice value (see <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)). Assigning a negative (i.e., high) nice value results in a longer quantum; assigning a positive (i.e., low) nice value results in a shorter quantum. The default quantum is 0.1 seconds; the degree to which changing the nice value affects the quantum has varied somewhat across kernel versions. This method of adjusting the quantum was removed starting with Linux 2.6.24. </p>
<p> Linux 3.9 added a new mechanism for adjusting (and viewing) the <code>SCHED_RR</code> quantum: the <i>/proc/sys/kernel/sched_rr_timeslice_ms</i> file exposes the quantum as a millisecond value, whose default is 100. Writing 0 to this file resets the quantum to the default value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
