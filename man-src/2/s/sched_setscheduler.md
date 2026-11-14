---
title: "sched_setscheduler(2)"
name: "sched_setscheduler"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_setscheduler/"
description: "sched_setscheduler, sched_getscheduler – set and get scheduling policy/parameters"
---

<h2 class="name">NAME</h2>
<p> sched_setscheduler, sched_getscheduler &#8211; set and get scheduling policy/parameters </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sched.h&gt;
int sched_setscheduler(pid_t pid, int policy,
                       const struct sched_param *param);
int sched_getscheduler(pid_t pid);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>sched_setscheduler</code>() system call sets both the scheduling policy and parameters for the thread whose ID is specified in <i>pid</i>. If <i>pid</i> equals zero, the scheduling policy and parameters of the calling thread will be set. </p>
<p> The scheduling parameters are specified in the <i>param</i> argument, which is a pointer to a structure of the following form: </p>
<p> struct sched_param {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sched_priority;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; }; </p>
<p> In the current implementation, the structure contains only one field, <i>sched_priority</i>. The interpretation of <i>param</i> depends on the selected policy. </p>
<p> Currently, Linux supports the following &quot;normal&quot; (i.e., non-real-time) scheduling policies as values that may be specified in <i>policy</i>:</p>
<dl>
<dt><code>SCHED_OTHER</code></p>
<dd> the standard round-robin time-sharing policy;</p>
<dt><code>SCHED_BATCH</code></p>
<dd> for &quot;batch&quot; style execution of processes; and</p>
<dt><code>SCHED_IDLE</code></p>
<dd> for running <i>very</i> low priority background jobs.</dl>
<p> For each of the above policies, <i>param-&gt;sched_priority</i> must be 0. </p>
<p> Various &quot;real-time&quot; policies are also supported, for special time-critical applications that need precise control over the way in which runnable threads are selected for execution. For the rules governing when a process may use these policies, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). The real-time policies that may be specified in <i>policy</i> are:</p>
<dl>
<dt><code>SCHED_FIFO</code></p>
<dd> a first-in, first-out policy; and</p>
<dt><code>SCHED_RR</code></p>
<dd> a round-robin policy.</dl>
<p> For each of the above policies, <i>param-&gt;sched_priority</i> specifies a scheduling priority for the thread. This is a number in the range returned by calling <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2) and <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2) with the specified <i>policy</i>. On Linux, these system calls return, respectively, 1 and 99. </p>
<p> Since Linux 2.6.32, the <code>SCHED_RESET_ON_FORK</code> flag can be ORed in <i>policy</i> when calling <code>sched_setscheduler</code>(). As a result of including this flag, children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) do not inherit privileged scheduling policies. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for details. </p>
<p> <code>sched_getscheduler</code>() returns the current scheduling policy of the thread identified by <i>pid</i>. If <i>pid</i> equals zero, the policy of the calling thread will be retrieved.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_setscheduler</code>() returns zero. On success, <code>sched_getscheduler</code>() returns the policy for the thread (a nonnegative integer). On error, both calls return -1, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> Invalid arguments: <i>pid</i> is negative or <i>param</i> is NULL.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>sched_setscheduler</code>()) <i>policy</i> is not one of the recognized policies.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>sched_setscheduler</code>()) <i>param</i> does not make sense for the specified <i>policy</i>.</p>
<dt><code>EPERM</code></p>
<dd> The calling thread does not have appropriate privileges.</p>
<dt><code>ESRCH</code></p>
<dd> The thread whose ID is <i>pid</i> could not be found.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008 (but see BUGS below). The <code>SCHED_BATCH</code> and <code>SCHED_IDLE</code> policies are Linux-specific.</p>
<h2>NOTES</h2>
<p> Further details of the semantics of all of the above &quot;normal&quot; and &quot;real-time&quot; scheduling policies can be found in the <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) manual page. That page also describes an additional policy, <code>SCHED_DEADLINE</code>, which is settable only via <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2). </p>
<p> POSIX systems on which <code>sched_setscheduler</code>() and <code>sched_getscheduler</code>() are available define <code>_POSIX_PRIORITY_SCHEDULING</code> in <i>&lt;unistd.h&gt;</i>. </p>
<p> POSIX.1 does not detail the permissions that an unprivileged thread requires in order to call <code>sched_setscheduler</code>(), and details vary across systems. For example, the Solaris 7 manual page says that the real or effective user ID of the caller must match the real user ID or the save set-user-ID of the target. </p>
<p> The scheduling policy and parameters are in fact per-thread attributes on Linux. The value returned from a call to <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) can be passed in the argument <i>pid</i>. Specifying <i>pid</i> as 0 will operate on the attributes of the calling thread, and passing the value returned from a call to <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) will operate on the attributes of the main thread of the thread group. (If you are using the POSIX threads API, then use <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getschedparam/">pthread_getschedparam</a></code>(3), and <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), instead of the <code>sched_*</code>(2) system calls.)</p>
<h2>BUGS</h2>
<p> POSIX.1 says that on success, <code>sched_setscheduler</code>() should return the previous scheduling policy. Linux <code>sched_setscheduler</code>() does not conform to this requirement, since it always returns 0 on success.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_getattr/">sched_getattr</a></code>(2), <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
