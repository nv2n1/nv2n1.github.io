---
title: "uclampset(1)"
name: "uclampset"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uclampset/"
description: "uclampset – manipulate the utilization clamping attributes of the system or a process"
---

<h2 class="name">NAME</h2>
<p> uclampset &#8211; manipulate the utilization clamping attributes of the system or a process </p>
<h2>SYNOPSIS</h2>
<p> <code>uclampset</code> [options] [<code>-m</code> <i>uclamp_min</i>] [<code>-M</code> <i>uclamp_max] _command argument</i> </p>
<p> <code>uclampset</code> [options] [<code>-m</code> <i>uclamp_min</i>] [<code>-M</code> <i>uclamp_max</i>] <code>-p</code> <i>PID</i></p>
<h2>DESCRIPTION</h2>
<p> <code>uclampset</code> sets or retrieves the utilization clamping attributes of an existing <i>PID</i>, or runs <i>command</i> with the given attributes. </p>
<p> Utilization clamping is a new feature added in v5.3. It gives a hint to the scheduler about the allowed range of utilization the task should be operating at. </p>
<p> The utilization of the task affects frequency selection and task placement. Only schedutil cpufreq governor understands handling util clamp hints at the time of writing. Consult your kernel docs for further info about other cpufreq governors support. </p>
<p> If you&#8217;re running on asymmetric heterogeneous system like Arm&#8217;s big.LITTLE. Utilization clamping can help bias task placement. If the task is boosted such that <i>util_min</i> value is higher than the little cores&#8217; capacity, then the scheduler will do its best to place it on a big core. </p>
<p> Similarly, if <i>util_max</i> is smaller than or equal the capacity of the little cores, then the scheduler can still choose to place it there even if the actual utilization of the task is at max. </p>
<p> Setting a task&#8217;s <i>uclamp_min</i> to a none zero value will effectively boost the task as when it runs it&#8217;ll always start from this utilization value. </p>
<p> By setting a task&#8217;s <i>uclamp_max</i> below 1024, this will effectively cap the task as when it runs it&#8217;ll never be able to go above this utilization value. </p>
<p> The full utilization range is: [0:1024]. The special value -1 is used to reset to system&#8217;s default.</p>
<h2>OPTIONS</h2>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> Set <i>util_min</i> value.</dl>
<p> <code>-M</code></p>
<dl>
<dt>
<dd> Set <i>util_max</i> value.</dl>
<p> <code>-a</code>, <code>&#8211;all-tasks</code></p>
<dl>
<dt>
<dd> Set or retrieve the utilization clamping attributes of all the tasks (threads) for a given PID.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code></p>
<dl>
<dt>
<dd> Operate on an existing PID and do not launch a new task.</dl>
<p> <code>-s</code>, <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Set or retrieve the system-wide utilization clamping attributes.</dl>
<p> <code>-R</code>, <code>&#8211;reset-on-fork</code></p>
<dl>
<dt>
<dd> Set <code>SCHED_FLAG_RESET_ON_FORK</code> flag.</dl>
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
<dd> <code>uclampset</code> <i>[-m uclamp_min]</i> <i>[-M uclamp_max]</i> <i>command</i> [<i>arguments</i>]</dl>
<p> You can also retrieve the utilization clamping attributes of an existing task:</p>
<dl>
<dt>
<dd> <code>uclampset -p</code> <i>PID</i></dl>
<p> Or set them:</p>
<dl>
<dt>
<dd> <code>uclampset -p</code> <i>PID</i> <i>[-m uclamp_min]</i> <i>[-M uclamp_max]</i></dl>
<p> Or control the system-wide attributes:</p>
<dl>
<dt>
<dd> <code>uclampset -s</code> <i>[-m uclamp_min]</i> <i>[-M uclamp_max]</i></dl>
<h2>PERMISSIONS</h2>
<p> A user must possess <code>CAP_SYS_NICE</code> to change the scheduling attributes of a process. Any user can retrieve the scheduling information.</p>
<h2>NOTES</h2>
<p> The system wide utilization clamp attributes are there to control the <i>allowed</i> range the tasks can use. By default both <i>uclamp_min</i> and <i>uclamp_max</i> are set to 1024. This means users can set the utilization clamp values for their task across the full range [0:1024]. </p>
<p> For example:</p>
<dl>
<dt>
<dd> <code>uclampset -s</code> -m 512 -M 700</dl>
<p> will prevent any task from being boosted higher than 512. And all tasks in the systems are capped to a utilization of 700. Effectively rendering the maximum performance of the system to 700. </p>
<p> Consult your kernel docs for the exact expected behavior on that kernel.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) </p>
<p> See <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) and <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2) for a description of the Linux scheduling scheme.</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>uclampset</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
