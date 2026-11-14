---
title: "chrt(1)"
name: "chrt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chrt/"
description: "chrt – manipulate the real-time attributes of a process"
---

<h2 class="name">NAME</h2>
<p> chrt &#8211; manipulate the real-time attributes of a process </p>
<h2>SYNOPSIS</h2>
<p> <code>chrt</code> [options] <i>priority command argument</i> &#8230; </p>
<p> <code>chrt</code> [options] <code>-p</code> [<i>priority</i>] <i>PID</i></p>
<h2>DESCRIPTION</h2>
<p> <code>chrt</code> sets or retrieves the real-time scheduling attributes of an existing <i>PID</i>, or runs <i>command</i> with the given attributes.</p>
<h2>POLICIES</h2>
<p> <code>-o</code>, <code>&#8211;other</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_OTHER</code> (time-sharing scheduling). This is the default Linux scheduling policy.</dl>
<p> <code>-f</code>, <code>&#8211;fifo</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_FIFO</code> (first in-first out).</dl>
<p> <code>-r</code>, <code>&#8211;rr</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_RR</code> (round-robin scheduling). When no policy is defined, the <code>SCHED_RR</code> is used as the default.</dl>
<p> <code>-b</code>, <code>&#8211;batch</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_BATCH</code> (scheduling batch processes). Linux-specific, supported since 2.6.16. The priority argument has to be set to zero.</dl>
<p> <code>-i</code>, <code>&#8211;idle</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_IDLE</code> (scheduling very low priority jobs). Linux-specific, supported since 2.6.23. The priority argument has to be set to zero.</dl>
<p> <code>-d</code>, <code>&#8211;deadline</code></p>
<dl>
<dt>
<dd> Set scheduling policy to <code>SCHED_DEADLINE</code> (sporadic task model deadline scheduling). Linux-specific, supported since 3.14. The priority argument has to be set to zero. See also <code>&#8211;sched-runtime</code>, <code>&#8211;sched-deadline</code> and <code>&#8211;sched-period</code>. The relation between the options required by the kernel is runtime &lArr; deadline &lArr; period. <code>chrt</code> copies <i>period</i> to <i>deadline</i> if <code>&#8211;sched-deadline</code> is not specified and <i>deadline</i> to <i>runtime</i> if <code>&#8211;sched-runtime</code> is not specified. It means that at least <code>&#8211;sched-period</code> has to be specified. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for more details.</dl>
<h2>SCHEDULING OPTIONS</h2>
<p> <code>-T</code>, <code>&#8211;sched-runtime</code> <i>nanoseconds</i></p>
<dl>
<dt>
<dd> Specifies runtime parameter for <code>SCHED_DEADLINE</code> policy (Linux-specific).</dl>
<p> <code>-P</code>, <code>&#8211;sched-period</code> <i>nanoseconds</i></p>
<dl>
<dt>
<dd> Specifies period parameter for <code>SCHED_DEADLINE</code> policy (Linux-specific).</dl>
<p> <code>-D</code>, <code>&#8211;sched-deadline</code> <i>nanoseconds</i></p>
<dl>
<dt>
<dd> Specifies deadline parameter for <code>SCHED_DEADLINE</code> policy (Linux-specific).</dl>
<p> <code>-R</code>, <code>&#8211;reset-on-fork</code></p>
<dl>
<dt>
<dd> Use <code>SCHED_RESET_ON_FORK</code> or <code>SCHED_FLAG_RESET_ON_FORK</code> flag. Linux-specific, supported since 2.6.31.</dl>
<p> Each thread has a <i>reset-on-fork</i> scheduling flag. When this flag is set, children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) do not inherit privileged scheduling policies. After the <i>reset-on-fork</i> flag has been enabled, it can be reset only if the thread has the <code>CAP_SYS_NICE</code> capability. This flag is disabled in child processes created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> More precisely, if the <i>reset-on-fork</i> flag is set, the following rules apply for subsequently created children: </p>
<dl>
<dt>
<dd> &bull; If the calling thread has a scheduling policy of <code>SCHED_FIFO</code> or <code>SCHED_RR</code>, the policy is reset to <code>SCHED_OTHER</code> in child processes.</dl>
<dl>
<dt>
<dd> &bull; If the calling process has a negative nice value, the nice value is reset to zero in child processes.</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all-tasks</code></p>
<dl>
<dt>
<dd> Set or retrieve the scheduling attributes of all the tasks (threads) for a given PID.</dl>
<p> <code>-m</code>, <code>&#8211;max</code></p>
<dl>
<dt>
<dd> Show minimum and maximum valid priorities, then exit.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code></p>
<dl>
<dt>
<dd> Operate on an existing PID and do not launch a new task.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show status information.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>USAGE</h2>
<p> The default behavior is to run a new command:</p>
<dl>
<dt>
<dd> <code>chrt</code> <i>priority</i> <i>command</i> [<i>arguments</i>]</dl>
<p> You can also retrieve the real-time attributes of an existing task:</p>
<dl>
<dt>
<dd> <code>chrt -p</code> <i>PID</i></dl>
<p> Or set them:</p>
<dl>
<dt>
<dd> <code>chrt -r -p</code> <i>priority PID</i></dl>
<h2>PERMISSIONS</h2>
<p> A user must possess <code>CAP_SYS_NICE</code> to change the scheduling attributes of a process. Any user can retrieve the scheduling information.</p>
<h2>NOTES</h2>
<p> Only <code>SCHED_FIFO</code>, <code>SCHED_OTHER</code> and <code>SCHED_RR</code> are part of POSIX 1003.1b Process Scheduling. The other scheduling attributes may be ignored on some systems. </p>
<p> Linux&#8217; default scheduling policy is <code>SCHED_OTHER</code>.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) </p>
<p> See <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) for a description of the Linux scheduling scheme.</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>chrt</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
