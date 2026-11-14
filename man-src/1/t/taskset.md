---
title: "taskset(1)"
name: "taskset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-taskset/"
description: "taskset – set or retrieve a process’s CPU affinity"
---

<h2 class="name">NAME</h2>
<p> taskset &#8211; set or retrieve a process&#8217;s CPU affinity </p>
<h2>SYNOPSIS</h2>
<p> <code>taskset</code> [options] <i>mask command</i> [<i>argument</i>&#8230;] </p>
<p> <code>taskset</code> [options] <code>-p</code> [<i>mask</i>] <i>pid</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>taskset</code> command is used to set or retrieve the CPU affinity of a running process given its <i>pid</i>, or to launch a new <i>command</i> with a given CPU affinity. CPU affinity is a scheduler property that &quot;bonds&quot; a process to a given set of CPUs on the system. The Linux scheduler will honor the given CPU affinity and the process will not run on any other CPUs. Note that the Linux scheduler also supports natural CPU affinity: the scheduler attempts to keep processes on the same CPU as long as practical for performance reasons. Therefore, forcing a specific CPU affinity is useful only in certain applications. </p>
<p> The CPU affinity is represented as a bitmask, with the lowest order bit corresponding to the first logical CPU and the highest order bit corresponding to the last logical CPU. Not all CPUs may exist on a given system but a mask may specify more CPUs than are present. A retrieved mask will reflect only the bits that correspond to CPUs physically on the system. If an invalid mask is given (i.e., one that corresponds to no valid CPUs on the current system) an error is returned. The masks may be specified in hexadecimal (with or without a leading &quot;0x&quot;), or as a CPU list with the <code>&#8211;cpu-list</code> option. For example, </p>
<p> <code>0x00000001</code></p>
<dl>
<dt>
<dd> is processor #0,</dl>
<p> <code>0x00000003</code></p>
<dl>
<dt>
<dd> is processors #0 and #1,</dl>
<p> <code>0xFFFFFFFF</code></p>
<dl>
<dt>
<dd> is processors #0 through #31,</dl>
<p> <code>32</code></p>
<dl>
<dt>
<dd> is processors #1, #4, and #5,</dl>
<p> <code>&#8211;cpu-list 0-2,6</code></p>
<dl>
<dt>
<dd> is processors #0, #1, #2, and #6.</dl>
<p> <code>&#8211;cpu-list 0-10:2</code></p>
<dl>
<dt>
<dd> is processors #0, #2, #4, #6, #8 and #10. The suffix &quot;:N&quot; specifies stride in the range, for example 0-10:3 is interpreted as 0,3,6,9 list.</dl>
<p> When <code>taskset</code> returns, it is guaranteed that the given program has been scheduled to a legal CPU.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all-tasks</code></p>
<dl>
<dt>
<dd> Set or retrieve the CPU affinity of all the tasks (threads) for a given PID.</dl>
<p> <code>-c</code>, <code>&#8211;cpu-list</code></p>
<dl>
<dt>
<dd> Interpret <i>mask</i> as numerical list of processors instead of a bitmask. Numbers are separated by commas and may include ranges. For example: <code>0,5,8-11</code>.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code></p>
<dl>
<dt>
<dd> Operate on an existing PID and do not launch a new task.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>USAGE</h2>
<p> The default behavior is to run a new command with a given affinity mask:</p>
<dl>
<dt>
<dd> <code>taskset</code> <i>mask</i> <i>command</i> [<i>arguments</i>]</dl>
<p> You can also retrieve the CPU affinity of an existing task:</p>
<dl>
<dt>
<dd> <code>taskset -p</code> <i>pid</i></dl>
<p> Or set it:</p>
<dl>
<dt>
<dd> <code>taskset -p</code> <i>mask pid</i></dl>
<h2>PERMISSIONS</h2>
<p> A user can change the CPU affinity of a process belonging to the same user. A user must possess <code>CAP_SYS_NICE</code> to change the CPU affinity of a process belonging to another user. A user can retrieve the affinity mask of any process.</p>
<h2>AUTHORS</h2>
<p> Written by Robert M. Love.</p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2004 Robert M. Love. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1), <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) </p>
<p> See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for a description of the Linux scheduling scheme.</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>taskset</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
