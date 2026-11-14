---
title: "sched_setparam(2)"
name: "sched_setparam"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_setparam/"
description: "sched_setparam, sched_getparam – set and get scheduling parameters"
---

<h2 class="name">NAME</h2>
<p> sched_setparam, sched_getparam &#8211; set and get scheduling parameters </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sched.h&gt;
int sched_setparam(pid_t pid, const struct sched_param *param);
int sched_getparam(pid_t pid, struct sched_param *param);
struct sched_param {
    ... int sched_priority;
    ...
};
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>sched_setparam</code>() sets the scheduling parameters associated with the scheduling policy for the thread whose thread ID is specified in <i>pid</i>. If <i>pid</i> is zero, then the parameters of the calling thread are set. The interpretation of the argument <i>param</i> depends on the scheduling policy of the thread identified by <i>pid</i>. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for a description of the scheduling policies supported under Linux. </p>
<p> <code>sched_getparam</code>() retrieves the scheduling parameters for the thread identified by <i>pid</i>. If <i>pid</i> is zero, then the parameters of the calling thread are retrieved. </p>
<p> <code>sched_setparam</code>() checks the validity of <i>param</i> for the scheduling policy of the thread. The value <i>param-&gt;sched_priority</i> must lie within the range given by <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2) and <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2). </p>
<p> For a discussion of the privileges and resource limits related to scheduling priority and policy, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> POSIX systems on which <code>sched_setparam</code>() and <code>sched_getparam</code>() are available define <code>_POSIX_PRIORITY_SCHEDULING</code> in <i>&lt;unistd.h&gt;</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_setparam</code>() and <code>sched_getparam</code>() return 0. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> Invalid arguments: <i>param</i> is NULL or <i>pid</i> is negative</p>
<dt><code>EINVAL</code></p>
<dd> (<code>sched_setparam</code>()) The argument <i>param</i> does not make sense for the current scheduling policy.</p>
<dt><code>EPERM</code></p>
<dd> (<code>sched_setparam</code>()) The caller does not have appropriate privileges (Linux: does not have the <code>CAP_SYS_NICE</code> capability).</p>
<dt><code>ESRCH</code></p>
<dd> The thread whose ID is <i>pid</i> could not be found.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
