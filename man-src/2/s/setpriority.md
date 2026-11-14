---
title: "setpriority(2)"
name: "setpriority"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setpriority/"
description: "getpriority, setpriority – get/set program scheduling priority"
---

<h2 class="name">NAME</h2>
<p> getpriority, setpriority &#8211; get/set program scheduling priority </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/time.h&gt;</code><br />
 <code>#include &lt;sys/resource.h&gt;</code> </p>
<p> <code>int getpriority(int </code><i>which</i><code>, id_t </code><i>who</i><code>);</code><br />
 <code>int setpriority(int </code><i>which</i><code>, id_t </code><i>who</i><code>, int </code><i>prio</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The scheduling priority of the process, process group, or user, as indicated by <i>which</i> and <i>who</i> is obtained with the <code>getpriority</code>() call and set with the <code>setpriority</code>() call. The process attribute dealt with by these system calls is the same attribute (also known as the &quot;nice&quot; value) that is dealt with by <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2). </p>
<p> The value <i>which</i> is one of <code>PRIO_PROCESS</code>, <code>PRIO_PGRP</code>, or <code>PRIO_USER</code>, and <i>who</i> is interpreted relative to <i>which</i> (a process identifier for <code>PRIO_PROCESS</code>, process group identifier for <code>PRIO_PGRP</code>, and a user ID for <code>PRIO_USER</code>). A zero value for <i>who</i> denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process. </p>
<p> The <i>prio</i> argument is a value in the range -20 to 19 (but see NOTES below). with -20 being the highest priority and 19 being the lowest priority. Attempts to set a priority outside this range are silently clamped to the range. The default priority is 0; lower values give a process a higher scheduling priority. </p>
<p> The <code>getpriority</code>() call returns the highest priority (lowest numerical value) enjoyed by any of the specified processes. The <code>setpriority</code>() call sets the priorities of all of the specified processes to the specified value. </p>
<p> Traditionally, only a privileged process could lower the nice value (i.e., set a higher priority). However, since Linux 2.6.12, an unprivileged process can decrease the nice value of a target process that has a suitable <code>RLIMIT_NICE</code> soft limit; see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) for details.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>getpriority</code>() returns the calling thread&#8217;s nice value, which may be a negative number. On error, it returns -1 and sets <i>errno</i> to indicate the cause of the error. </p>
<p> Since a successful call to <code>getpriority</code>() can legitimately return the value -1, it is necessary to clear the external variable <i>errno</i> prior to the call, then check <i>errno</i> afterward to determine if -1 is an error or a legitimate value. </p>
<p> <code>setpriority</code>() returns 0 on success. On error, it returns -1 and sets <i>errno</i> to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>which</i> was not one of <code>PRIO_PROCESS</code>, <code>PRIO_PGRP</code>, or <code>PRIO_USER</code>.</p>
<dt><code>ESRCH</code></p>
<dd> No process was located using the <i>which</i> and <i>who</i> values specified.</dl>
<p> In addition to the errors indicated above, <code>setpriority</code>() may fail if:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The caller attempted to set a lower nice value (i.e., a higher process priority), but did not have the required privilege (on Linux: did not have the <code>CAP_SYS_NICE</code> capability).</p>
<dt><code>EPERM</code></p>
<dd> A process was located, but its effective user ID did not match either the effective or the real user ID of the caller, and was not privileged (on Linux: did not have the <code>CAP_SYS_NICE</code> capability). But see NOTES below.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (these interfaces first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> For further details on the nice value, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> <i>Note</i>: the addition of the &quot;autogroup&quot; feature in Linux 2.6.38 means that the nice value no longer has its traditional effect in many circumstances. For details, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> A child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s nice value. The nice value is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The details on the condition for <code>EPERM</code> depend on the system. The above description is what POSIX.1-2001 says, and seems to be followed on all System V-like systems. Linux kernels before 2.6.12 required the real or effective user ID of the caller to match the real user of the process <i>who</i> (instead of its effective user ID). Linux 2.6.12 and later require the effective user ID of the caller to match the real or effective user ID of the process <i>who</i>. All BSD-like systems (SunOS 4.1.3, Ultrix 4.2, 4.3BSD, FreeBSD 4.3, OpenBSD-2.5, &#8230;) behave in the same manner as Linux 2.6.12 and later. </p>
<p> Including <i>&lt;sys/time.h&gt;</i> is not required these days, but increases portability. (Indeed, <i>&lt;sys/resource.h&gt;</i> defines the <i>rusage</i> structure with fields of type <i>struct timeval</i> defined in <i>&lt;sys/time.h&gt;</i>.)</p>
<h3>C library/kernel differences</h3>
<p> Within the kernel, nice values are actually represented using the range 40..1 (since negative numbers are error codes) and these are the values employed by the <code>setpriority</code>() and <code>getpriority</code>() system calls. The glibc wrapper functions for these system calls handle the translations between the user-land and kernel representations of the nice value according to the formula <i>unice&nbsp;=&nbsp;20 &#8211; knice</i>. (Thus, the kernel&#8217;s 40..1 range corresponds to the range -20..19 as seen by user space.)</p>
<h2>BUGS</h2>
<p> According to POSIX, the nice value is a per-process setting. However, under the current Linux/NPTL implementation of POSIX threads, the nice value is a per-thread attribute: different threads in the same process can have different nice values. Portable applications should avoid relying on the Linux behavior, which may be made standards conformant in the future.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) </p>
<p> <i>Documentation/scheduler/sched-nice-design.txt</i> in the Linux kernel source tree (since Linux 2.6.23)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
