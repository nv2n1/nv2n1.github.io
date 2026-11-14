---
title: "perf_event_open(2)"
name: "perf_event_open"
section: "2"
letter: "p"
url: "/docs/linux/man/2-perf_event_open/"
description: "perf_event_open – set up performance monitoring"
---

<h2 class="name">NAME</h2>
<p> perf_event_open &#8211; set up performance monitoring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/hw_breakpoint.h&gt;
#include &lt;linux/perf_event.h&gt;
int perf_event_open(struct perf_event_attr *attr,
                    pid_t pid, int cpu, int group_fd,
                    unsigned long flags);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> Given a list of parameters, <code>perf_event_open</code>() returns a file descriptor, for use in subsequent system calls (<code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), etc.). </p>
<p> A call to <code>perf_event_open</code>() creates a file descriptor that allows measuring performance information. Each file descriptor corresponds to one event that is measured; these can be grouped together to measure multiple events simultaneously. </p>
<p> Events can be enabled and disabled in two ways: via <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) and via <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). When an event is disabled it does not count or generate overflows but does continue to exist and maintain its count value. </p>
<p> Events come in two flavors: counting and sampled. A <i>counting</i> event is one that is used for counting the aggregate number of events that occur. In general, counting event results are gathered with a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) call. A <i>sampling</i> event periodically writes measurements to a buffer that can then be accessed via <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<h3>Arguments</h3>
<p> The <i>pid</i> and <i>cpu</i> arguments allow specifying which process and CPU to monitor:</p>
<dl>
<dt><code>pid == 0</code> and <code>cpu == -1</code></p>
<dd> This measures the calling process/thread on any CPU.</p>
<dt><code>pid == 0</code> and <code>cpu &gt;= 0</code></p>
<dd> This measures the calling process/thread only when running on the specified CPU.</p>
<dt><code>pid &gt; 0</code> and <code>cpu == -1</code></p>
<dd> This measures the specified process/thread on any CPU.</p>
<dt><code>pid &gt; 0</code> and <code>cpu &gt;= 0</code></p>
<dd> This measures the specified process/thread only when running on the specified CPU.</p>
<dt><code>pid == -1</code> and <code>cpu &gt;= 0</code></p>
<dd> This measures all processes/threads on the specified CPU. This requires <code>CAP_PERFMON</code> (since Linux 5.8) or <code>CAP_SYS_ADMIN</code> capability or a <i>/proc/sys/kernel/perf_event_paranoid</i> value of less than 1.</p>
<dt><code>pid == -1</code> and <code>cpu == -1</code></p>
<dd> This setting is invalid and will return an error.</dl>
<p> When <i>pid</i> is greater than zero, permission to perform this system call is governed by <code>CAP_PERFMON</code> (since Linux 5.9) and a ptrace access mode <code>PTRACE_MODE_READ_REALCREDS</code> check on older Linux versions; see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2). </p>
<p> The <i>group_fd</i> argument allows event groups to be created. An event group has one event which is the group leader. The leader is created first, with <i>group_fd</i> = -1. The rest of the group members are created with subsequent <code>perf_event_open</code>() calls with <i>group_fd</i> being set to the file descriptor of the group leader. (A single event on its own is created with <i>group_fd</i> = -1 and is considered to be a group with only 1 member.) An event group is scheduled onto the CPU as a unit: it will be put onto the CPU only if all of the events in the group can be put onto the CPU. This means that the values of the member events can be meaningfully compared&#8212;added, divided (to get ratios), and so on&#8212;with each other, since they have counted events for the same set of executed instructions. </p>
<p> The <i>flags</i> argument is formed by ORing together zero or more of the following values:</p>
<dl>
<dt><code>PERF_FLAG_FD_CLOEXEC</code> (since Linux 3.14)</p>
<dd> This flag enables the close-on-exec flag for the created event file descriptor, so that the file descriptor is automatically closed on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Setting the close-on-exec flags at creation time, rather than later with <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), avoids potential race conditions where the calling thread invokes <code>perf_event_open</code>() and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) at the same time as another thread calls <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) then <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>PERF_FLAG_FD_NO_GROUP</code></p>
<dd> This flag tells the event to ignore the <i>group_fd</i> parameter except for the purpose of setting up output redirection using the <code>PERF_FLAG_FD_OUTPUT</code> flag.</p>
<dt><code>PERF_FLAG_FD_OUTPUT</code> (broken since Linux 2.6.35)</p>
<dd> This flag re-routes the event&#8217;s sampled output to instead be included in the mmap buffer of the event specified by <i>group_fd</i>.</p>
<dt><code>PERF_FLAG_PID_CGROUP</code> (since Linux 2.6.39)</p>
<dd> This flag activates per-container system-wide monitoring. A container is an abstraction that isolates a set of resources for finer-grained control (CPUs, memory, etc.). In this mode, the event is measured only if the thread running on the monitored CPU belongs to the designated container (cgroup). The cgroup is identified by passing a file descriptor opened on its directory in the cgroupfs filesystem. For instance, if the cgroup to monitor is called <i>test</i>, then a file descriptor opened on <i>/dev/cgroup/test</i> (assuming cgroupfs is mounted on <i>/dev/cgroup</i>) must be passed as the <i>pid</i> parameter. cgroup monitoring is available only for system-wide events and may therefore require extra permissions.</dl>
<p> The <i>perf_event_attr</i> structure provides detailed configuration information for the event being created. </p>
<p> struct perf_event_attr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type of event&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of attribute structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 config;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Type-specific configuration&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 sample_period;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Period of sampling&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 sample_freq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Frequency of sampling&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 sample_type;&nbsp;<wbr>&nbsp;/*&nbsp;Specifies values included in sample&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 read_format;&nbsp;<wbr>&nbsp;/*&nbsp;Specifies values returned in read&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 disabled&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;off by default&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inherit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;children inherit it&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pinned&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;must always be on PMU&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclusive&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;only group on PMU&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_user&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count user&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_kernel : 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_hv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count hypervisor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_idle&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count when idle&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mmap&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;include mmap data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;include comm data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;use freq, not period&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inherit_stat&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;per task counts&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;enable_on_exec : 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;next exec enables&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;task&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;trace fork/exit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;watermark&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;wakeup_watermark&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;precise_ip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 2,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;skid constraint&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mmap_data&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;non-exec mmap data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sample_id_all&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;sample_type all events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_host&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count in host&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_guest&nbsp;<wbr>&nbsp;: 1,&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;don&#8217;t count in guest&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_callchain_kernel : 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;exclude kernel callchains&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exclude_callchain_user&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;exclude user callchains&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mmap2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include mmap with inode data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comm_exec&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;flag comm events that are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;due to exec&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;use_clockid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;use clockid for time fields&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;context_switch :&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;context switch data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write_backward :&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;Write ring buffer from end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to beginning&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;namespaces&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include namespaces data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ksymbol&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include ksymbol events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bpf_event&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include bpf events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aux_output&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;generate AUX records<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;instead of events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cgroup&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include cgroup events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;text_poke&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;<wbr>&nbsp;1,&nbsp;<wbr>&nbsp;/*&nbsp;include text poke events&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__reserved_1&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 30; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 wakeup_events;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;wakeup every n events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 wakeup_watermark;&nbsp;/*&nbsp;bytes before wakeup&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bp_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;breakpoint type&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 bp_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;breakpoint address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 kprobe_func;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for perf_kprobe&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 uprobe_path;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for perf_uprobe&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 config1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;extension of config&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 bp_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;breakpoint length&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 kprobe_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;with kprobe_func&nbsp;==&nbsp;NULL&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 probe_offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;for perf_[k,u]probe&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 config2;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;extension of config1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 branch_sample_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;enum perf_branch_sample_type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 sample_regs_user;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user regs to dump on samples&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 sample_stack_user;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;size of stack to dump on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;samples&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s32 clockid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;clock to use for time fields&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 sample_regs_intr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;regs to dump on samples&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 aux_watermark;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;aux bytes before wakeup&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 sample_max_stack;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;max frames in callchain&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16&nbsp;__reserved_2;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;align to u64&nbsp;*/ </p>
<p> }; </p>
<p> The fields of the <i>perf_event_attr</i> structure are described in more detail below:</p>
<dl>
<dt><i>type</i></p>
<dd> This field specifies the overall event type. It has one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_TYPE_HARDWARE</code></p>
<dd> This indicates one of the &quot;generalized&quot; hardware events provided by the kernel. See the <i>config</i> field definition for more details.</p>
<dt><code>PERF_TYPE_SOFTWARE</code></p>
<dd> This indicates one of the software-defined events provided by the kernel (even if no hardware support is available).</p>
<dt><code>PERF_TYPE_TRACEPOINT</code></p>
<dd> This indicates a tracepoint provided by the kernel tracepoint infrastructure.</p>
<dt><code>PERF_TYPE_HW_CACHE</code></p>
<dd> This indicates a hardware cache event. This has a special encoding, described in the <i>config</i> field definition.</p>
<dt><code>PERF_TYPE_RAW</code></p>
<dd> This indicates a &quot;raw&quot; implementation-specific event in the <i>config</i> field.</p>
<dt><code>PERF_TYPE_BREAKPOINT</code> (since Linux 2.6.33)</p>
<dd> This indicates a hardware breakpoint as provided by the CPU. Breakpoints can be read/write accesses to an address as well as execution of an instruction address.</p>
<dt>dynamic PMU</p>
<dd> Since Linux 2.6.38, <code>perf_event_open</code>() can support multiple PMUs. To enable this, a value exported by the kernel can be used in the <i>type</i> field to indicate which PMU to use. The value to use can be found in the sysfs filesystem: there is a subdirectory per PMU instance under <i>/sys/bus/event_source/devices</i>. In each subdirectory there is a <i>type</i> file whose content is an integer that can be used in the <i>type</i> field. For instance, <i>/sys/bus/event_source/devices/cpu/type</i> contains the value for the core CPU PMU, which is usually 4.</p>
<dt><code>kprobe</code> and <code>uprobe</code> (since Linux 4.17)</p>
<dd> These two dynamic PMUs create a kprobe/uprobe and attach it to the file descriptor generated by perf_event_open. The kprobe/uprobe will be destroyed on the destruction of the file descriptor. See fields <i>kprobe_func</i>, <i>uprobe_path</i>, <i>kprobe_addr</i>, and <i>probe_offset</i> for more details.</dl>
</dl>
<dt><i>size</i></p>
<dd> The size of the <i>perf_event_attr</i> structure for forward/backward compatibility. Set this using <i>sizeof(struct perf_event_attr)</i> to allow the kernel to see the struct size at the time of compilation.</p>
<dt>
<dd> The related define <code>PERF_ATTR_SIZE_VER0</code> is set to 64; this was the size of the first published struct. <code>PERF_ATTR_SIZE_VER1</code> is 72, corresponding to the addition of breakpoints in Linux 2.6.33. <code>PERF_ATTR_SIZE_VER2</code> is 80 corresponding to the addition of branch sampling in Linux 3.4. <code>PERF_ATTR_SIZE_VER3</code> is 96 corresponding to the addition of <i>sample_regs_user</i> and <i>sample_stack_user</i> in Linux 3.7. <code>PERF_ATTR_SIZE_VER4</code> is 104 corresponding to the addition of <i>sample_regs_intr</i> in Linux 3.19. <code>PERF_ATTR_SIZE_VER5</code> is 112 corresponding to the addition of <i>aux_watermark</i> in Linux 4.1.</p>
<dt><i>config</i></p>
<dd> This specifies which event you want, in conjunction with the <i>type</i> field. The <i>config1</i> and <i>config2</i> fields are also taken into account in cases where 64 bits is not enough to fully specify the event. The encoding of these fields are event dependent.</p>
<dt>
<dd> There are various ways to set the <i>config</i> field that are dependent on the value of the previously described <i>type</i> field. What follows are various possible settings for <i>config</i> separated out by <i>type</i>.</p>
<dt>
<dd> If <i>type</i> is <code>PERF_TYPE_HARDWARE</code>, we are measuring one of the generalized hardware CPU events. Not all of these are available on all platforms. Set <i>config</i> to one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_COUNT_HW_CPU_CYCLES</code></p>
<dd> Total cycles. Be wary of what happens during CPU frequency scaling.</p>
<dt><code>PERF_COUNT_HW_INSTRUCTIONS</code></p>
<dd> Retired instructions. Be careful, these can be affected by various issues, most notably hardware interrupt counts.</p>
<dt><code>PERF_COUNT_HW_CACHE_REFERENCES</code></p>
<dd> Cache accesses. Usually this indicates Last Level Cache accesses but this may vary depending on your CPU. This may include prefetches and coherency messages; again this depends on the design of your CPU.</p>
<dt><code>PERF_COUNT_HW_CACHE_MISSES</code></p>
<dd> Cache misses. Usually this indicates Last Level Cache misses; this is intended to be used in conjunction with the <code>PERF_COUNT_HW_CACHE_REFERENCES</code> event to calculate cache miss rates.</p>
<dt><code>PERF_COUNT_HW_BRANCH_INSTRUCTIONS</code></p>
<dd> Retired branch instructions. Prior to Linux 2.6.35, this used the wrong event on AMD processors.</p>
<dt><code>PERF_COUNT_HW_BRANCH_MISSES</code></p>
<dd> Mispredicted branch instructions.</p>
<dt><code>PERF_COUNT_HW_BUS_CYCLES</code></p>
<dd> Bus cycles, which can be different from total cycles.</p>
<dt><code>PERF_COUNT_HW_STALLED_CYCLES_FRONTEND</code> (since Linux 3.0)</p>
<dd> Stalled cycles during issue.</p>
<dt><code>PERF_COUNT_HW_STALLED_CYCLES_BACKEND</code> (since Linux 3.0)</p>
<dd> Stalled cycles during retirement.</p>
<dt><code>PERF_COUNT_HW_REF_CPU_CYCLES</code> (since Linux 3.3)</p>
<dd> Total cycles; not affected by CPU frequency scaling.</dl>
</dl>
<dt>
<dd> If <i>type</i> is <code>PERF_TYPE_SOFTWARE</code>, we are measuring software events provided by the kernel. Set <i>config</i> to one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_COUNT_SW_CPU_CLOCK</code></p>
<dd> This reports the CPU clock, a high-resolution per-CPU timer.</p>
<dt><code>PERF_COUNT_SW_TASK_CLOCK</code></p>
<dd> This reports a clock count specific to the task that is running.</p>
<dt><code>PERF_COUNT_SW_PAGE_FAULTS</code></p>
<dd> This reports the number of page faults.</p>
<dt><code>PERF_COUNT_SW_CONTEXT_SWITCHES</code></p>
<dd> This counts context switches. Until Linux 2.6.34, these were all reported as user-space events, after that they are reported as happening in the kernel.</p>
<dt><code>PERF_COUNT_SW_CPU_MIGRATIONS</code></p>
<dd> This reports the number of times the process has migrated to a new CPU.</p>
<dt><code>PERF_COUNT_SW_PAGE_FAULTS_MIN</code></p>
<dd> This counts the number of minor page faults. These did not require disk I/O to handle.</p>
<dt><code>PERF_COUNT_SW_PAGE_FAULTS_MAJ</code></p>
<dd> This counts the number of major page faults. These required disk I/O to handle.</p>
<dt><code>PERF_COUNT_SW_ALIGNMENT_FAULTS</code> (since Linux 2.6.33)</p>
<dd> This counts the number of alignment faults. These happen when unaligned memory accesses happen; the kernel can handle these but it reduces performance. This happens only on some architectures (never on x86).</p>
<dt><code>PERF_COUNT_SW_EMULATION_FAULTS</code> (since Linux 2.6.33)</p>
<dd> This counts the number of emulation faults. The kernel sometimes traps on unimplemented instructions and emulates them for user space. This can negatively impact performance.</p>
<dt><code>PERF_COUNT_SW_DUMMY</code> (since Linux 3.12)</p>
<dd> This is a placeholder event that counts nothing. Informational sample record types such as mmap or comm must be associated with an active event. This dummy event allows gathering such records without requiring a counting event.</dl>
</dl>
</dl>
<dl>
<dt>
<dd> If <i>type</i> is <code>PERF_TYPE_TRACEPOINT</code>, then we are measuring kernel tracepoints. The value to use in <i>config</i> can be obtained from under debugfs <i>tracing/events/*/*/id</i> if ftrace is enabled in the kernel.</dl>
<dl>
<dt>
<dd> If <i>type</i> is <code>PERF_TYPE_HW_CACHE</code>, then we are measuring a hardware CPU cache event. To calculate the appropriate <i>config</i> value, use the following equation:</p>
<dl>
<dt>
<dd>
<p> config = (perf_hw_cache_id) |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(perf_hw_cache_op_id&nbsp;&lt;&lt;&nbsp;8)&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(perf_hw_cache_op_result_id&nbsp;&lt;&lt;&nbsp;16); </p>
<p> where <i>perf_hw_cache_id</i> is one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_COUNT_HW_CACHE_L1D</code></p>
<dd> for measuring Level 1 Data Cache</p>
<dt><code>PERF_COUNT_HW_CACHE_L1I</code></p>
<dd> for measuring Level 1 Instruction Cache</p>
<dt><code>PERF_COUNT_HW_CACHE_LL</code></p>
<dd> for measuring Last-Level Cache</p>
<dt><code>PERF_COUNT_HW_CACHE_DTLB</code></p>
<dd> for measuring the Data TLB</p>
<dt><code>PERF_COUNT_HW_CACHE_ITLB</code></p>
<dd> for measuring the Instruction TLB</p>
<dt><code>PERF_COUNT_HW_CACHE_BPU</code></p>
<dd> for measuring the branch prediction unit</p>
<dt><code>PERF_COUNT_HW_CACHE_NODE</code> (since Linux 3.1)</p>
<dd> for measuring local memory accesses</dl>
</dl>
<p> and <i>perf_hw_cache_op_id</i> is one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_COUNT_HW_CACHE_OP_READ</code></p>
<dd> for read accesses</p>
<dt><code>PERF_COUNT_HW_CACHE_OP_WRITE</code></p>
<dd> for write accesses</p>
<dt><code>PERF_COUNT_HW_CACHE_OP_PREFETCH</code></p>
<dd> for prefetch accesses</dl>
</dl>
<p> and <i>perf_hw_cache_op_result_id</i> is one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_COUNT_HW_CACHE_RESULT_ACCESS</code></p>
<dd> to measure accesses</p>
<dt><code>PERF_COUNT_HW_CACHE_RESULT_MISS</code></p>
<dd> to measure misses</dl>
</dl>
</dl>
<p> If <i>type</i> is <code>PERF_TYPE_RAW</code>, then a custom &quot;raw&quot; <i>config</i> value is needed. Most CPUs support events that are not covered by the &quot;generalized&quot; events. These are implementation defined; see your CPU manual (for example the Intel Volume 3B documentation or the AMD BIOS and Kernel Developer Guide). The libpfm4 library can be used to translate from the name in the architectural manuals to the raw hex value <code>perf_event_open</code>() expects in this field. </p>
<p> If <i>type</i> is <code>PERF_TYPE_BREAKPOINT</code>, then leave <i>config</i> set to zero. Its parameters are set in other places. </p>
<p> If <i>type</i> is <code>kprobe</code> or <code>uprobe</code>, set <i>retprobe</i> (bit 0 of <i>config</i>, see <i>/sys/bus/event_source/devices/[k,u]probe/format/retprobe</i>) for kretprobe/uretprobe. See fields <i>kprobe_func</i>, <i>uprobe_path</i>, <i>kprobe_addr</i>, and <i>probe_offset</i> for more details.</dl>
<dl>
<dt><i>kprobe_func</i>, <i>uprobe_path</i>, <i>kprobe_addr</i>, and <i>probe_offset</i></p>
<dd> These fields describe the kprobe/uprobe for dynamic PMUs <code>kprobe</code> and <code>uprobe</code>. For <code>kprobe</code>: use <i>kprobe_func</i> and <i>probe_offset</i>, or use <i>kprobe_addr</i> and leave <i>kprobe_func</i> as NULL. For <code>uprobe</code>: use <i>uprobe_path</i> and <i>probe_offset</i>.</p>
<dt><i>sample_period</i>, <i>sample_freq</i></p>
<dd> A &quot;sampling&quot; event is one that generates an overflow notification every N events, where N is given by <i>sample_period</i>. A sampling event has <i>sample_period</i> &gt; 0. When an overflow occurs, requested data is recorded in the mmap buffer. The <i>sample_type</i> field controls what data is recorded on each overflow.</p>
<dt>
<dd> <i>sample_freq</i> can be used if you wish to use frequency rather than period. In this case, you set the <i>freq</i> flag. The kernel will adjust the sampling period to try and achieve the desired rate. The rate of adjustment is a timer tick.</p>
<dt><i>sample_type</i></p>
<dd> The various bits in this field specify which values to include in the sample. They will be recorded in a ring-buffer, which is available to user space using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). The order in which the values are saved in the sample are documented in the MMAP Layout subsection below; it is not the <i>enum perf_event_sample_format</i> order.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_SAMPLE_IP</code></p>
<dd> Records instruction pointer.</p>
<dt><code>PERF_SAMPLE_TID</code></p>
<dd> Records the process and thread IDs.</p>
<dt><code>PERF_SAMPLE_TIME</code></p>
<dd> Records a timestamp.</p>
<dt><code>PERF_SAMPLE_ADDR</code></p>
<dd> Records an address, if applicable.</p>
<dt><code>PERF_SAMPLE_READ</code></p>
<dd> Record counter values for all events in a group, not just the group leader.</p>
<dt><code>PERF_SAMPLE_CALLCHAIN</code></p>
<dd> Records the callchain (stack backtrace).</p>
<dt><code>PERF_SAMPLE_ID</code></p>
<dd> Records a unique ID for the opened event&#8217;s group leader.</p>
<dt><code>PERF_SAMPLE_CPU</code></p>
<dd> Records CPU number.</p>
<dt><code>PERF_SAMPLE_PERIOD</code></p>
<dd> Records the current sampling period.</p>
<dt><code>PERF_SAMPLE_STREAM_ID</code></p>
<dd> Records a unique ID for the opened event. Unlike <code>PERF_SAMPLE_ID</code> the actual ID is returned, not the group leader. This ID is the same as the one returned by <code>PERF_FORMAT_ID</code>.</p>
<dt><code>PERF_SAMPLE_RAW</code></p>
<dd> Records additional data, if applicable. Usually returned by tracepoint events.</p>
<dt><code>PERF_SAMPLE_BRANCH_STACK</code> (since Linux 3.4)</p>
<dd> This provides a record of recent branches, as provided by CPU branch sampling hardware (such as Intel Last Branch Record). Not all hardware supports this feature.</p>
<dt>
<dd> See the <i>branch_sample_type</i> field for how to filter which branches are reported.</p>
<dt><code>PERF_SAMPLE_REGS_USER</code> (since Linux 3.7)</p>
<dd> Records the current user-level CPU register state (the values in the process before the kernel was called).</p>
<dt><code>PERF_SAMPLE_STACK_USER</code> (since Linux 3.7)</p>
<dd> Records the user level stack, allowing stack unwinding.</p>
<dt><code>PERF_SAMPLE_WEIGHT</code> (since Linux 3.10)</p>
<dd> Records a hardware provided weight value that expresses how costly the sampled event was. This allows the hardware to highlight expensive events in a profile.</p>
<dt><code>PERF_SAMPLE_DATA_SRC</code> (since Linux 3.10)</p>
<dd> Records the data source: where in the memory hierarchy the data associated with the sampled instruction came from. This is available only if the underlying hardware supports this feature.</p>
<dt><code>PERF_SAMPLE_IDENTIFIER</code> (since Linux 3.12)</p>
<dd> Places the <code>SAMPLE_ID</code> value in a fixed position in the record, either at the beginning (for sample events) or at the end (if a non-sample event).</p>
<dt>
<dd> This was necessary because a sample stream may have records from various different event sources with different <i>sample_type</i> settings. Parsing the event stream properly was not possible because the format of the record was needed to find <code>SAMPLE_ID</code>, but the format could not be found without knowing what event the sample belonged to (causing a circular dependency).</p>
<dt>
<dd> The <code>PERF_SAMPLE_IDENTIFIER</code> setting makes the event stream always parsable by putting <code>SAMPLE_ID</code> in a fixed location, even though it means having duplicate <code>SAMPLE_ID</code> values in records.</p>
<dt><code>PERF_SAMPLE_TRANSACTION</code> (since Linux 3.13)</p>
<dd> Records reasons for transactional memory abort events (for example, from Intel TSX transactional memory support).</p>
<dt>
<dd> The <i>precise_ip</i> setting must be greater than 0 and a transactional memory abort event must be measured or no values will be recorded. Also note that some perf_event measurements, such as sampled cycle counting, may cause extraneous aborts (by causing an interrupt during a transaction).</p>
<dt><code>PERF_SAMPLE_REGS_INTR</code> (since Linux 3.19)</p>
<dd> Records a subset of the current CPU register state as specified by <i>sample_regs_intr</i>. Unlike <code>PERF_SAMPLE_REGS_USER</code> the register values will return kernel register state if the overflow happened while kernel code is running. If the CPU supports hardware sampling of register state (i.e., PEBS on Intel x86) and <i>precise_ip</i> is set higher than zero then the register values returned are those captured by hardware at the time of the sampled instruction&#8217;s retirement.</p>
<dt><code>PERF_SAMPLE_PHYS_ADDR</code> (since Linux 4.13)</p>
<dd> Records physical address of data like in <code>PERF_SAMPLE_ADDR</code>.</p>
<dt><code>PERF_SAMPLE_CGROUP</code> (since Linux 5.7)</p>
<dd> Records (perf_event) cgroup ID of the process. This corresponds to the <i>id</i> field in the <code>PERF_RECORD_CGROUP</code> event.</dl>
</dl>
<dt><i>read_format</i></p>
<dd> This field specifies the format of the data returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) on a <code>perf_event_open</code>() file descriptor.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_FORMAT_TOTAL_TIME_ENABLED</code></p>
<dd> Adds the 64-bit <i>time_enabled</i> field. This can be used to calculate estimated totals if the PMU is overcommitted and multiplexing is happening.</p>
<dt><code>PERF_FORMAT_TOTAL_TIME_RUNNING</code></p>
<dd> Adds the 64-bit <i>time_running</i> field. This can be used to calculate estimated totals if the PMU is overcommitted and multiplexing is happening.</p>
<dt><code>PERF_FORMAT_ID</code></p>
<dd> Adds a 64-bit unique value that corresponds to the event group.</p>
<dt><code>PERF_FORMAT_GROUP</code></p>
<dd> Allows all counter values in an event group to be read with one read.</dl>
</dl>
<dt><i>disabled</i></p>
<dd> The <i>disabled</i> bit specifies whether the counter starts out disabled or enabled. If disabled, the event can later be enabled by <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), or <i>enable_on_exec</i>.</p>
<dt>
<dd> When creating an event group, typically the group leader is initialized with <i>disabled</i> set to 1 and any child events are initialized with <i>disabled</i> set to 0. Despite <i>disabled</i> being 0, the child events will not start until the group leader is enabled.</p>
<dt><i>inherit</i></p>
<dd> The <i>inherit</i> bit specifies that this counter should count events of child tasks as well as the task specified. This applies only to new children, not to any existing children at the time the counter is created (nor to any new children of existing children).</p>
<dt>
<dd> Inherit does not work for some combinations of <i>read_format</i> values, such as <code>PERF_FORMAT_GROUP</code>.</p>
<dt><i>pinned</i></p>
<dd> The <i>pinned</i> bit specifies that the counter should always be on the CPU if at all possible. It applies only to hardware counters and only to group leaders. If a pinned counter cannot be put onto the CPU (e.g., because there are not enough hardware counters or because of a conflict with some other event), then the counter goes into an &#8216;error&#8217; state, where reads return end-of-file (i.e., <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0) until the counter is subsequently enabled or disabled.</p>
<dt><i>exclusive</i></p>
<dd> The <i>exclusive</i> bit specifies that when this counter&#8217;s group is on the CPU, it should be the only group using the CPU&#8217;s counters. In the future this may allow monitoring programs to support PMU features that need to run alone so that they do not disrupt other hardware counters.</p>
<dt>
<dd> Note that many unexpected situations may prevent events with the <i>exclusive</i> bit set from ever running. This includes any users running a system-wide measurement as well as any kernel use of the performance counters (including the commonly enabled NMI Watchdog Timer interface).</p>
<dt><i>exclude_user</i></p>
<dd> If this bit is set, the count excludes events that happen in user space.</p>
<dt><i>exclude_kernel</i></p>
<dd> If this bit is set, the count excludes events that happen in kernel space.</p>
<dt><i>exclude_hv</i></p>
<dd> If this bit is set, the count excludes events that happen in the hypervisor. This is mainly for PMUs that have built-in support for handling this (such as POWER). Extra support is needed for handling hypervisor measurements on most machines.</p>
<dt><i>exclude_idle</i></p>
<dd> If set, don&#8217;t count when the CPU is running the idle task. While you can currently enable this for any event type, it is ignored for all but software events.</p>
<dt><i>mmap</i></p>
<dd> The <i>mmap</i> bit enables generation of <code>PERF_RECORD_MMAP</code> samples for every <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) call that has <code>PROT_EXEC</code> set. This allows tools to notice new executable code being mapped into a program (dynamic shared libraries for example) so that addresses can be mapped back to the original code.</p>
<dt><i>comm</i></p>
<dd> The <i>comm</i> bit enables tracking of process command name as modified by the <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) and <code>prctl</code>(PR_SET_NAME) system calls as well as writing to <i>/proc/self/comm</i>. If the <i>comm_exec</i> flag is also successfully set (possible since Linux 3.16), then the misc flag <code>PERF_RECORD_MISC_COMM_EXEC</code> can be used to differentiate the <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) case from the others.</p>
<dt><i>freq</i></p>
<dd> If this bit is set, then <i>sample_frequency</i> not <i>sample_period</i> is used when setting up the sampling interval.</p>
<dt><i>inherit_stat</i></p>
<dd> This bit enables saving of event counts on context switch for inherited tasks. This is meaningful only if the <i>inherit</i> field is set.</p>
<dt><i>enable_on_exec</i></p>
<dd> If this bit is set, a counter is automatically enabled after a call to <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2).</p>
<dt><i>task</i></p>
<dd> If this bit is set, then fork/exit notifications are included in the ring buffer.</p>
<dt><i>watermark</i></p>
<dd> If set, have an overflow notification happen when we cross the <i>wakeup_watermark</i> boundary. Otherwise, overflow notifications happen after <i>wakeup_events</i> samples.</p>
<dt><i>precise_ip</i> (since Linux 2.6.35)</p>
<dd> This controls the amount of skid. Skid is how many instructions execute between an event of interest happening and the kernel being able to stop and record the event. Smaller skid is better and allows more accurate reporting of which events correspond to which instructions, but hardware is often limited with how small this can be.</p>
<dt>
<dd> The possible values of this field are the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> <code>SAMPLE_IP</code> can have arbitrary skid.</p>
<dt>1</p>
<dd> <code>SAMPLE_IP</code> must have constant skid.</p>
<dt>2</p>
<dd> <code>SAMPLE_IP</code> requested to have 0 skid.</p>
<dt>3</p>
<dd> <code>SAMPLE_IP</code> must have 0 skid. See also the description of <code>PERF_RECORD_MISC_EXACT_IP</code>.</dl>
</dl>
<dt><i>mmap_data</i> (since Linux 2.6.36)</p>
<dd> This is the counterpart of the <i>mmap</i> field. This enables generation of <code>PERF_RECORD_MMAP</code> samples for <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) calls that do not have <code>PROT_EXEC</code> set (for example data and SysV shared memory).</p>
<dt><i>sample_id_all</i> (since Linux 2.6.38)</p>
<dd> If set, then TID, TIME, ID, STREAM_ID, and CPU can additionally be included in non-<code>PERF_RECORD_SAMPLE</code>s if the corresponding <i>sample_type</i> is selected.</p>
<dt>
<dd> If <code>PERF_SAMPLE_IDENTIFIER</code> is specified, then an additional ID value is included as the last value to ease parsing the record stream. This may lead to the <i>id</i> value appearing twice.</p>
<dt>
<dd> The layout is described by this pseudo-structure:</p>
<dt>
<dd> struct sample_id {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u32 pid, tid;&nbsp;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_TID set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u64 time;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_TIME set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u64 id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_ID set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u64 stream_id;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_STREAM_ID set&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u32 cpu, res;&nbsp;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_CPU set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{&nbsp;u64 id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_IDENTIFIER set&nbsp;*/ };</p>
<dt><i>exclude_host</i> (since Linux 3.2)</p>
<dd> When conducting measurements that include processes running VM instances (i.e., have executed a <code>KVM_RUN</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)), only measure events happening inside a guest instance. This is only meaningful outside the guests; this setting does not change counts gathered inside of a guest. Currently, this functionality is x86 only.</p>
<dt><i>exclude_guest</i> (since Linux 3.2)</p>
<dd> When conducting measurements that include processes running VM instances (i.e., have executed a <code>KVM_RUN</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)), do not measure events happening inside guest instances. This is only meaningful outside the guests; this setting does not change counts gathered inside of a guest. Currently, this functionality is x86 only.</p>
<dt><i>exclude_callchain_kernel</i> (since Linux 3.7)</p>
<dd> Do not include kernel callchains.</p>
<dt><i>exclude_callchain_user</i> (since Linux 3.7)</p>
<dd> Do not include user callchains.</p>
<dt><i>mmap2</i> (since Linux 3.16)</p>
<dd> Generate an extended executable mmap record that contains enough additional information to uniquely identify shared mappings. The <i>mmap</i> flag must also be set for this to work.</p>
<dt><i>comm_exec</i> (since Linux 3.16)</p>
<dd> This is purely a feature-detection flag, it does not change kernel behavior. If this flag can successfully be set, then, when <i>comm</i> is enabled, the <code>PERF_RECORD_MISC_COMM_EXEC</code> flag will be set in the <i>misc</i> field of a comm record header if the rename event being reported was caused by a call to <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2). This allows tools to distinguish between the various types of process renaming.</p>
<dt><i>use_clockid</i> (since Linux 4.1)</p>
<dd> This allows selecting which internal Linux clock to use when generating timestamps via the <i>clockid</i> field. This can make it easier to correlate perf sample times with timestamps generated by other tools.</p>
<dt><i>context_switch</i> (since Linux 4.3)</p>
<dd> This enables the generation of <code>PERF_RECORD_SWITCH</code> records when a context switch occurs. It also enables the generation of <code>PERF_RECORD_SWITCH_CPU_WIDE</code> records when sampling in CPU-wide mode. This functionality is in addition to existing tracepoint and software events for measuring context switches. The advantage of this method is that it will give full information even with strict <i>perf_event_paranoid</i> settings.</p>
<dt><i>write_backward</i> (since Linux 4.6)</p>
<dd> This causes the ring buffer to be written from the end to the beginning. This is to support reading from overwritable ring buffer.</p>
<dt><i>namespaces</i> (since Linux 4.11)</p>
<dd> This enables the generation of <code>PERF_RECORD_NAMESPACES</code> records when a task enters a new namespace. Each namespace has a combination of device and inode numbers.</p>
<dt><i>ksymbol</i> (since Linux 5.0)</p>
<dd> This enables the generation of <code>PERF_RECORD_KSYMBOL</code> records when new kernel symbols are registered or unregistered. This is analyzing dynamic kernel functions like eBPF.</p>
<dt><i>bpf_event</i> (since Linux 5.0)</p>
<dd> This enables the generation of <code>PERF_RECORD_BPF_EVENT</code> records when an eBPF program is loaded or unloaded.</p>
<dt><i>auxevent</i> (since Linux 5.4)</p>
<dd> This allows normal (non-AUX) events to generate data for AUX events if the hardware supports it.</p>
<dt><i>cgroup</i> (since Linux 5.7)</p>
<dd> This enables the generation of <code>PERF_RECORD_CGROUP</code> records when a new cgroup is created (and activated).</p>
<dt><i>text_poke</i> (since Linux 5.8)</p>
<dd> This enables the generation of <code>PERF_RECORD_TEXT_POKE</code> records when there&#8217;s a changes to the kernel text (i.e., self-modifying code).</p>
<dt><i>wakeup_events</i>, <i>wakeup_watermark</i></p>
<dd> This union sets how many samples (<i>wakeup_events</i>) or bytes (<i>wakeup_watermark</i>) happen before an overflow notification happens. Which one is used is selected by the <i>watermark</i> bit flag.</p>
<dt>
<dd> <i>wakeup_events</i> counts only <code>PERF_RECORD_SAMPLE</code> record types. To receive overflow notification for all <code>PERF_RECORD</code> types choose watermark and set <i>wakeup_watermark</i> to 1.</p>
<dt>
<dd> Prior to Linux 3.0, setting <i>wakeup_events</i> to 0 resulted in no overflow notifications; more recent kernels treat 0 the same as 1.</p>
<dt><i>bp_type</i> (since Linux 2.6.33)</p>
<dd> This chooses the breakpoint type. It is one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>HW_BREAKPOINT_EMPTY</code></p>
<dd> No breakpoint.</p>
<dt><code>HW_BREAKPOINT_R</code></p>
<dd> Count when we read the memory location.</p>
<dt><code>HW_BREAKPOINT_W</code></p>
<dd> Count when we write the memory location.</p>
<dt><code>HW_BREAKPOINT_RW</code></p>
<dd> Count when we read or write the memory location.</p>
<dt><code>HW_BREAKPOINT_X</code></p>
<dd> Count when we execute code at the memory location.</dl>
<p> The values can be combined via a bitwise or, but the combination of <code>HW_BREAKPOINT_R</code> or <code>HW_BREAKPOINT_W</code> with <code>HW_BREAKPOINT_X</code> is not allowed.</dl>
<dt><i>bp_addr</i> (since Linux 2.6.33)</p>
<dd> This is the address of the breakpoint. For execution breakpoints, this is the memory address of the instruction of interest; for read and write breakpoints, it is the memory address of the memory location of interest.</p>
<dt><i>config1</i> (since Linux 2.6.39)</p>
<dd> <i>config1</i> is used for setting events that need an extra register or otherwise do not fit in the regular config field. Raw OFFCORE_EVENTS on Nehalem/Westmere/SandyBridge use this field on Linux 3.3 and later kernels.</p>
<dt><i>bp_len</i> (since Linux 2.6.33)</p>
<dd> <i>bp_len</i> is the length of the breakpoint being measured if <i>type</i> is <code>PERF_TYPE_BREAKPOINT</code>. Options are <code>HW_BREAKPOINT_LEN_1</code>, <code>HW_BREAKPOINT_LEN_2</code>, <code>HW_BREAKPOINT_LEN_4</code>, and <code>HW_BREAKPOINT_LEN_8</code>. For an execution breakpoint, set this to <i>sizeof(long)</i>.</p>
<dt><i>config2</i> (since Linux 2.6.39)</p>
<dd> <i>config2</i> is a further extension of the <i>config1</i> field.</p>
<dt><i>branch_sample_type</i> (since Linux 3.4)</p>
<dd> If <code>PERF_SAMPLE_BRANCH_STACK</code> is enabled, then this specifies what branches to include in the branch record.</p>
<dt>
<dd> The first part of the value is the privilege level, which is a combination of one of the values listed below. If the user does not set privilege level explicitly, the kernel will use the event&#8217;s privilege level. Event and branch privilege levels do not have to match.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_SAMPLE_BRANCH_USER</code></p>
<dd> Branch target is in user space.</p>
<dt><code>PERF_SAMPLE_BRANCH_KERNEL</code></p>
<dd> Branch target is in kernel space.</p>
<dt><code>PERF_SAMPLE_BRANCH_HV</code></p>
<dd> Branch target is in hypervisor.</p>
<dt><code>PERF_SAMPLE_BRANCH_PLM_ALL</code></p>
<dd> A convenience value that is the three preceding values ORed together.</dl>
<p> In addition to the privilege value, at least one or more of the following bits must be set.</p>
<dl>
<dt><code>PERF_SAMPLE_BRANCH_ANY</code></p>
<dd> Any branch type.</p>
<dt><code>PERF_SAMPLE_BRANCH_ANY_CALL</code></p>
<dd> Any call branch (includes direct calls, indirect calls, and far jumps).</p>
<dt><code>PERF_SAMPLE_BRANCH_IND_CALL</code></p>
<dd> Indirect calls.</p>
<dt><code>PERF_SAMPLE_BRANCH_CALL</code> (since Linux 4.4)</p>
<dd> Direct calls.</p>
<dt><code>PERF_SAMPLE_BRANCH_ANY_RETURN</code></p>
<dd> Any return branch.</p>
<dt><code>PERF_SAMPLE_BRANCH_IND_JUMP</code> (since Linux 4.2)</p>
<dd> Indirect jumps.</p>
<dt><code>PERF_SAMPLE_BRANCH_COND</code> (since Linux 3.16)</p>
<dd> Conditional branches.</p>
<dt><code>PERF_SAMPLE_BRANCH_ABORT_TX</code> (since Linux 3.11)</p>
<dd> Transactional memory aborts.</p>
<dt><code>PERF_SAMPLE_BRANCH_IN_TX</code> (since Linux 3.11)</p>
<dd> Branch in transactional memory transaction.</p>
<dt><code>PERF_SAMPLE_BRANCH_NO_TX</code> (since Linux 3.11)</p>
<dd> Branch not in transactional memory transaction. <code>PERF_SAMPLE_BRANCH_CALL_STACK</code> (since Linux 4.1) Branch is part of a hardware-generated call stack. This requires hardware support, currently only found on Intel x86 Haswell or newer.</dl>
</dl>
<dt><i>sample_regs_user</i> (since Linux 3.7)</p>
<dd> This bit mask defines the set of user CPU registers to dump on samples. The layout of the register mask is architecture-specific and is described in the kernel header file <i>arch/ARCH/include/uapi/asm/perf_regs.h</i>.</p>
<dt><i>sample_stack_user</i> (since Linux 3.7)</p>
<dd> This defines the size of the user stack to dump if <code>PERF_SAMPLE_STACK_USER</code> is specified.</p>
<dt><i>clockid</i> (since Linux 4.1)</p>
<dd> If <i>use_clockid</i> is set, then this field selects which internal Linux timer to use for timestamps. The available timers are defined in <i>linux/time.h</i>, with <code>CLOCK_MONOTONIC</code>, <code>CLOCK_MONOTONIC_RAW</code>, <code>CLOCK_REALTIME</code>, <code>CLOCK_BOOTTIME</code>, and <code>CLOCK_TAI</code> currently supported.</p>
<dt><i>aux_watermark</i> (since Linux 4.1)</p>
<dd> This specifies how much data is required to trigger a <code>PERF_RECORD_AUX</code> sample.</p>
<dt><i>sample_max_stack</i> (since Linux 4.8)</p>
<dd> When <i>sample_type</i> includes <code>PERF_SAMPLE_CALLCHAIN</code>, this field specifies how many stack frames to report when generating the callchain.</dl>
<h3>Reading results</h3>
<p> Once a <code>perf_event_open</code>() file descriptor has been opened, the values of the events can be read from the file descriptor. The values that are there are specified by the <i>read_format</i> field in the <i>attr</i> structure at open time. </p>
<p> If you attempt to read into a buffer that is not big enough to hold the data, the error <code>ENOSPC</code> results. </p>
<p> Here is the layout of the data returned by a read:</p>
<dl>
<dt>*</p>
<dd> If <code>PERF_FORMAT_GROUP</code> was specified to allow reading all events in a group at once:</p>
<dt>
<dd> struct read_format {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The number of events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 time_enabled;&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_TOTAL_TIME_ENABLED&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 time_running;&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_TOTAL_TIME_RUNNING&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The value of the event&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;values[nr]; };</p>
<dt>*</p>
<dd> If <code>PERF_FORMAT_GROUP</code> was <i>not</i> specified:</p>
<dt>
<dd> struct read_format {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 value;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The value of the event&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 time_enabled;&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_TOTAL_TIME_ENABLED&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 time_running;&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_TOTAL_TIME_RUNNING&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_FORMAT_ID&nbsp;*/ };</dl>
<p> The values read are as follows:</p>
<dl>
<dt><i>nr</i></p>
<dd> The number of events in this file descriptor. Available only if <code>PERF_FORMAT_GROUP</code> was specified.</p>
<dt><i>time_enabled</i>, <i>time_running</i></p>
<dd> Total time the event was enabled and running. Normally these values are the same. Multiplexing happens if the number of events is more than the number of available PMU counter slots. In that case the events run only part of the time and the <i>time_enabled</i> and <i>time running</i> values can be used to scale an estimated value for the count.</p>
<dt><i>value</i></p>
<dd> An unsigned 64-bit value containing the counter result.</p>
<dt><i>id</i></p>
<dd> A globally unique value for this particular event; only present if <code>PERF_FORMAT_ID</code> was specified in <i>read_format</i>.</dl>
<h3>MMAP layout</h3>
<p> When using <code>perf_event_open</code>() in sampled mode, asynchronous events (like counter overflow or <code>PROT_EXEC</code> mmap tracking) are logged into a ring-buffer. This ring-buffer is created and accessed through <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). </p>
<p> The mmap size should be 1+2^n pages, where the first page is a metadata page (<i>struct perf_event_mmap_page</i>) that contains various bits of information such as where the ring-buffer head is. </p>
<p> Before kernel 2.6.39, there is a bug that means you must allocate an mmap ring buffer when sampling even if you do not plan to access it. </p>
<p> The structure of the first metadata mmap page is as follows: </p>
<p> struct perf_event_mmap_page {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 version;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;version number of this structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 compat_version;&nbsp;/*&nbsp;lowest version this is compat with&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 lock;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seqlock for synchronization&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 index;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;hardware counter identifier&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__s64 offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;add to hardware counter value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 time_enabled;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;time event active&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 time_running;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;time event on CPU&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;capabilities;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 cap_usr_time&nbsp;/&nbsp;cap_usr_rdpmc&nbsp;/&nbsp;cap_bit0 : 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cap_bit0_is_deprecated : 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cap_user_rdpmc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cap_user_time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cap_user_time_zero&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: 1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 pmc_width;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 time_shift;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 time_mult;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 time_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64&nbsp;__reserved[120];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pad to 1 k&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 data_head;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;head in the data section&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 data_tail;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;user-space written tail&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 data_offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;where the buffer starts&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 data_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;data buffer size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 aux_head;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 aux_tail;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 aux_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u64 aux_size; </p>
<p> } </p>
<p> The following list describes the fields in the <i>perf_event_mmap_page</i> structure in more detail:</p>
<dl>
<dt><i>version</i></p>
<dd> Version number of this structure.</p>
<dt><i>compat_version</i></p>
<dd> The lowest version this is compatible with.</p>
<dt><i>lock</i></p>
<dd> A seqlock for synchronization.</p>
<dt><i>index</i></p>
<dd> A unique hardware counter identifier.</p>
<dt><i>offset</i></p>
<dd> When using rdpmc for reads this offset value must be added to the one returned by rdpmc to get the current total event count.</p>
<dt><i>time_enabled</i></p>
<dd> Time the event was active.</p>
<dt><i>time_running</i></p>
<dd> Time the event was running.</p>
<dt><i>cap_usr_time</i> / <i>cap_usr_rdpmc</i> / <i>cap_bit0</i> (since Linux 3.4)</p>
<dd> There was a bug in the definition of <i>cap_usr_time</i> and <i>cap_usr_rdpmc</i> from Linux 3.4 until Linux 3.11. Both bits were defined to point to the same location, so it was impossible to know if <i>cap_usr_time</i> or <i>cap_usr_rdpmc</i> were actually set.</p>
<dt>
<dd> Starting with Linux 3.12, these are renamed to <i>cap_bit0</i> and you should use the <i>cap_user_time</i> and <i>cap_user_rdpmc</i> fields instead.</p>
<dt><i>cap_bit0_is_deprecated</i> (since Linux 3.12)</p>
<dd> If set, this bit indicates that the kernel supports the properly separated <i>cap_user_time</i> and <i>cap_user_rdpmc</i> bits.</p>
<dt>
<dd> If not-set, it indicates an older kernel where <i>cap_usr_time</i> and <i>cap_usr_rdpmc</i> map to the same bit and thus both features should be used with caution.</p>
<dt><i>cap_user_rdpmc</i> (since Linux 3.12)</p>
<dd> If the hardware supports user-space read of performance counters without syscall (this is the &quot;rdpmc&quot; instruction on x86), then the following code can be used to do a read:</p>
<dt>
<dd> u32 seq, time_mult, time_shift, idx, width; u64 count, enabled, running; u64 cyc, time_offset; </p>
<p> do {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;seq&nbsp;=&nbsp;pc-&gt;lock;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;barrier();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;enabled&nbsp;=&nbsp;pc-&gt;time_enabled;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;running&nbsp;=&nbsp;pc-&gt;time_running; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pc-&gt;cap_usr_time&nbsp;&amp;&amp;&nbsp;enabled&nbsp;!=&nbsp;running)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cyc&nbsp;=&nbsp;rdtsc();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_offset&nbsp;=&nbsp;pc-&gt;time_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_mult&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;pc-&gt;time_mult;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_shift&nbsp;<wbr>&nbsp;=&nbsp;pc-&gt;time_shift;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;idx&nbsp;=&nbsp;pc-&gt;index;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count&nbsp;=&nbsp;pc-&gt;offset; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pc-&gt;cap_usr_rdpmc&nbsp;&amp;&amp;&nbsp;idx)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;width&nbsp;=&nbsp;pc-&gt;pmc_width;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count&nbsp;+=&nbsp;rdpmc(idx &#8211; 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;barrier(); } while (pc-&gt;lock != seq);</p>
<dt><i>cap_user_time</i> (since Linux 3.12)</p>
<dd> This bit indicates the hardware has a constant, nonstop timestamp counter (TSC on x86).</p>
<dt><i>cap_user_time_zero</i> (since Linux 3.12)</p>
<dd> Indicates the presence of <i>time_zero</i> which allows mapping timestamp values to the hardware clock.</p>
<dt><i>pmc_width</i></p>
<dd> If <i>cap_usr_rdpmc</i>, this field provides the bit-width of the value read using the rdpmc or equivalent instruction. This can be used to sign extend the result like:</p>
<dt>
<dd> pmc &lt;&lt;= 64 &#8211; pmc_width; pmc &gt;&gt;= 64 &#8211; pmc_width; // signed shift right count += pmc;</p>
<dt><i>time_shift</i>, <i>time_mult</i>, <i>time_offset</i></p>
<dd>
<dt>
<dd> If <i>cap_usr_time</i>, these fields can be used to compute the time delta since <i>time_enabled</i> (in nanoseconds) using rdtsc or similar.</p>
<dt>
<dd> u64 quot, rem; u64 delta; </p>
<p> quot = cyc &gt;&gt; time_shift; rem = cyc &amp; (((u64)1 &lt;&lt; time_shift) &#8211; 1); delta = time_offset + quot * time_mult +<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;((rem&nbsp;*&nbsp;time_mult)&nbsp;&gt;&gt;&nbsp;time_shift);</p>
<dt>
<dd> Where <i>time_offset</i>, <i>time_mult</i>, <i>time_shift</i>, and <i>cyc</i> are read in the seqcount loop described above. This delta can then be added to enabled and possible running (if idx), improving the scaling:</p>
<dt>
<dd> enabled += delta; if (idx)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;running&nbsp;+=&nbsp;delta; quot = count / running; rem = count % running; count = quot * enabled + (rem * enabled) / running;</p>
<dt><i>time_zero</i> (since Linux 3.12)</p>
<dd>
<dt>
<dd> If <i>cap_usr_time_zero</i> is set, then the hardware clock (the TSC timestamp counter on x86) can be calculated from the <i>time_zero</i>, <i>time_mult</i>, and <i>time_shift</i> values:</p>
<dt>
<dd> time = timestamp &#8211; time_zero; quot = time / time_mult; rem = time % time_mult; cyc = (quot &lt;&lt; time_shift) + (rem &lt;&lt; time_shift) / time_mult;</p>
<dt>
<dd> And vice versa:</p>
<dt>
<dd> quot = cyc &gt;&gt; time_shift; rem = cyc &amp; (((u64)1 &lt;&lt; time_shift) &#8211; 1); timestamp = time_zero + quot * time_mult +<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;((rem&nbsp;*&nbsp;time_mult)&nbsp;&gt;&gt;&nbsp;time_shift);</p>
<dt><i>data_head</i></p>
<dd> This points to the head of the data section. The value continuously increases, it does not wrap. The value needs to be manually wrapped by the size of the mmap buffer before accessing the samples.</p>
<dt>
<dd> On SMP-capable platforms, after reading the <i>data_head</i> value, user space should issue an rmb().</p>
<dt><i>data_tail</i></p>
<dd> When the mapping is <code>PROT_WRITE</code>, the <i>data_tail</i> value should be written by user space to reflect the last read data. In this case, the kernel will not overwrite unread data.</p>
<dt><i>data_offset</i> (since Linux 4.1)</p>
<dd> Contains the offset of the location in the mmap buffer where perf sample data begins.</p>
<dt><i>data_size</i> (since Linux 4.1)</p>
<dd> Contains the size of the perf sample region within the mmap buffer.</p>
<dt><i>aux_head</i>, <i>aux_tail</i>, <i>aux_offset</i>, <i>aux_size</i> (since Linux 4.1)</p>
<dd> The AUX region allows <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)-ing a separate sample buffer for high-bandwidth data streams (separate from the main perf sample buffer). An example of a high-bandwidth stream is instruction tracing support, as is found in newer Intel processors.</p>
<dt>
<dd> To set up an AUX area, first <i>aux_offset</i> needs to be set with an offset greater than <i>data_offset</i>+<i>data_size</i> and <i>aux_size</i> needs to be set to the desired buffer size. The desired offset and size must be page aligned, and the size must be a power of two. These values are then passed to mmap in order to map the AUX buffer. Pages in the AUX buffer are included as part of the <code>RLIMIT_MEMLOCK</code> resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)), and also as part of the <i>perf_event_mlock_kb</i> allowance.</p>
<dt>
<dd> By default, the AUX buffer will be truncated if it will not fit in the available space in the ring buffer. If the AUX buffer is mapped as a read only buffer, then it will operate in ring buffer mode where old data will be overwritten by new. In overwrite mode, it might not be possible to infer where the new data began, and it is the consumer&#8217;s job to disable measurement while reading to avoid possible data races.</p>
<dt>
<dd> The <i>aux_head</i> and <i>aux_tail</i> ring buffer pointers have the same behavior and ordering rules as the previous described <i>data_head</i> and <i>data_tail</i>.</dl>
<p> The following 2^n ring-buffer pages have the layout described below. </p>
<p> If <i>perf_event_attr.sample_id_all</i> is set, then all event types will have the sample_type selected fields related to where/when (identity) an event took place (TID, TIME, ID, CPU, STREAM_ID) described in <code>PERF_RECORD_SAMPLE</code> below, it will be stashed just after the <i>perf_event_header</i> and the fields already present for the existing fields, that is, at the end of the payload. This allows a newer perf.data file to be supported by older perf tools, with the new optional fields being ignored. </p>
<p> The mmap values start with a header: </p>
<p> struct perf_event_header {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;misc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;size; }; </p>
<p> Below, we describe the <i>perf_event_header</i> fields in more detail. For ease of reading, the fields with shorter descriptions are presented first.</p>
<dl>
<dt><i>size</i></p>
<dd> This indicates the size of the record.</p>
<dt><i>misc</i></p>
<dd> The <i>misc</i> field contains additional information about the sample.</p>
<dt>
<dd> The CPU mode can be determined from this value by masking with <code>PERF_RECORD_MISC_CPUMODE_MASK</code> and looking for one of the following (note these are not bit masks, only one can be set at a time):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_RECORD_MISC_CPUMODE_UNKNOWN</code></p>
<dd> Unknown CPU mode.</p>
<dt><code>PERF_RECORD_MISC_KERNEL</code></p>
<dd> Sample happened in the kernel.</p>
<dt><code>PERF_RECORD_MISC_USER</code></p>
<dd> Sample happened in user code.</p>
<dt><code>PERF_RECORD_MISC_HYPERVISOR</code></p>
<dd> Sample happened in the hypervisor.</p>
<dt><code>PERF_RECORD_MISC_GUEST_KERNEL</code> (since Linux 2.6.35)</p>
<dd> Sample happened in the guest kernel.</p>
<dt><code>PERF_RECORD_MISC_GUEST_USER (since Linux 2.6.35)</code></p>
<dd> Sample happened in guest user code.</dl>
</dl>
</dl>
<dl>
<dt>
<dd> Since the following three statuses are generated by different record types, they alias to the same bit:</p>
<dl>
<dt><code>PERF_RECORD_MISC_MMAP_DATA</code> (since Linux 3.10)</p>
<dd> This is set when the mapping is not executable; otherwise the mapping is executable.</p>
<dt><code>PERF_RECORD_MISC_COMM_EXEC</code> (since Linux 3.16)</p>
<dd> This is set for a <code>PERF_RECORD_COMM</code> record on kernels more recent than Linux 3.16 if a process name change was caused by an <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) system call.</p>
<dt><code>PERF_RECORD_MISC_SWITCH_OUT</code> (since Linux 4.3)</p>
<dd> When a <code>PERF_RECORD_SWITCH</code> or <code>PERF_RECORD_SWITCH_CPU_WIDE</code> record is generated, this bit indicates that the context switch is away from the current process (instead of into the current process).</dl>
</dl>
<dl>
<dt>
<dd> In addition, the following bits can be set:</p>
<dl>
<dt><code>PERF_RECORD_MISC_EXACT_IP</code></p>
<dd> This indicates that the content of <code>PERF_SAMPLE_IP</code> points to the actual instruction that triggered the event. See also <i>perf_event_attr.precise_ip</i>.</p>
<dt><code>PERF_RECORD_MISC_EXT_RESERVED</code> (since Linux 2.6.35)</p>
<dd> This indicates there is extended data available (currently not used).</p>
<dt><code>PERF_RECORD_MISC_PROC_MAP_PARSE_TIMEOUT</code></p>
<dd> This bit is not set by the kernel. It is reserved for the user-space perf utility to indicate that <i>/proc/i[pid]/maps</i> parsing was taking too long and was stopped, and thus the mmap records may be truncated.</dl>
</dl>
<dl>
<dt><i>type</i></p>
<dd> The <i>type</i> value is one of the below. The values in the corresponding record (that follows the header) depend on the <i>type</i> selected as shown.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_RECORD_MMAP</code></p>
<dd> The MMAP events record the <code>PROT_EXEC</code> mappings so that we can correlate user-space IPs to code. They have the following structure:</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid, tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pgoff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;filename[]; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pid</i></p>
<dd> is the process ID.</p>
<dt><i>tid</i></p>
<dd> is the thread ID.</p>
<dt><i>addr</i></p>
<dd> is the address of the allocated memory. <i>len</i> is the length of the allocated memory. <i>pgoff</i> is the page offset of the allocated memory. <i>filename</i> is a string describing the backing of the allocated memory.</dl>
</dl>
<dt><code>PERF_RECORD_LOST</code></p>
<dd> This record indicates when events are lost.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lost;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>id</i></p>
<dd> is the unique event ID for the samples that were lost.</p>
<dt><i>lost</i></p>
<dd> is the number of events that were lost.</dl>
</dl>
<dt><code>PERF_RECORD_COMM</code></p>
<dd> This record indicates a change in the process name.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;comm[];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pid</i></p>
<dd> is the process ID.</p>
<dt><i>tid</i></p>
<dd> is the thread ID.</p>
<dt><i>comm</i></p>
<dd> is a string containing the new name of the process.</dl>
</dl>
<dt><code>PERF_RECORD_EXIT</code></p>
<dd> This record indicates a process exit event.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid, ppid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid, ptid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dt><code>PERF_RECORD_THROTTLE</code>, <code>PERF_RECORD_UNTHROTTLE</code></p>
<dd> This record indicates a throttle/unthrottle event.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream_id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dt><code>PERF_RECORD_FORK</code></p>
<dd> This record indicates a fork event.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid, ppid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid, ptid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dt><code>PERF_RECORD_READ</code></p>
<dd> This record indicates a read event.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid, tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct read_format values;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dt><code>PERF_RECORD_SAMPLE</code></p>
<dd> This record indicates a sample.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sample_id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_IDENTIFIER&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ip;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_IP&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid, tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_TID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_TIME&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_ADDR&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream_id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_STREAM_ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpu, res;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_CPU&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;period;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_PERIOD&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct read_format v;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_READ&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_CALLCHAIN&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ips[nr];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_CALLCHAIN&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_RAW&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;data[size];&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_RAW&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bnr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_BRANCH_STACK&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_branch_entry lbr[bnr];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_BRANCH_STACK&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abi;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_REGS_USER&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regs[weight(mask)];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_REGS_USER&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_STACK_USER&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;data[size];&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_STACK_USER&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dyn_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_STACK_USER&nbsp;&amp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size&nbsp;!=&nbsp;0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;weight;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_WEIGHT&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;data_src;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_DATA_SRC&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;transaction;&nbsp;/*&nbsp;if PERF_SAMPLE_TRANSACTION&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abi;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_REGS_INTR&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;regs[weight(mask)];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_REGS_INTR&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;phys_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_PHYS_ADDR&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cgroup;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;if PERF_SAMPLE_CGROUP&nbsp;*/ };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>sample_id</i></p>
<dd> If <code>PERF_SAMPLE_IDENTIFIER</code> is enabled, a 64-bit unique ID is included. This is a duplication of the <code>PERF_SAMPLE_ID</code> <i>id</i> value, but included at the beginning of the sample so parsers can easily obtain the value.</p>
<dt><i>ip</i></p>
<dd> If <code>PERF_SAMPLE_IP</code> is enabled, then a 64-bit instruction pointer value is included.</p>
<dt><i>pid</i>, <i>tid</i></p>
<dd> If <code>PERF_SAMPLE_TID</code> is enabled, then a 32-bit process ID and 32-bit thread ID are included.</p>
<dt><i>time</i></p>
<dd> If <code>PERF_SAMPLE_TIME</code> is enabled, then a 64-bit timestamp is included. This is obtained via local_clock() which is a hardware timestamp if available and the jiffies value if not.</p>
<dt><i>addr</i></p>
<dd> If <code>PERF_SAMPLE_ADDR</code> is enabled, then a 64-bit address is included. This is usually the address of a tracepoint, breakpoint, or software event; otherwise the value is 0.</p>
<dt><i>id</i></p>
<dd> If <code>PERF_SAMPLE_ID</code> is enabled, a 64-bit unique ID is included. If the event is a member of an event group, the group leader ID is returned. This ID is the same as the one returned by <code>PERF_FORMAT_ID</code>.</p>
<dt><i>stream_id</i></p>
<dd> If <code>PERF_SAMPLE_STREAM_ID</code> is enabled, a 64-bit unique ID is included. Unlike <code>PERF_SAMPLE_ID</code> the actual ID is returned, not the group leader. This ID is the same as the one returned by <code>PERF_FORMAT_ID</code>.</p>
<dt><i>cpu</i>, <i>res</i></p>
<dd> If <code>PERF_SAMPLE_CPU</code> is enabled, this is a 32-bit value indicating which CPU was being used, in addition to a reserved (unused) 32-bit value.</p>
<dt><i>period</i></p>
<dd> If <code>PERF_SAMPLE_PERIOD</code> is enabled, a 64-bit value indicating the current sampling period is written.</p>
<dt><i>v</i></p>
<dd> If <code>PERF_SAMPLE_READ</code> is enabled, a structure of type read_format is included which has values for all events in the event group. The values included depend on the <i>read_format</i> value used at <code>perf_event_open</code>() time.</p>
<dt><i>nr</i>, <i>ips[nr]</i></p>
<dd> If <code>PERF_SAMPLE_CALLCHAIN</code> is enabled, then a 64-bit number is included which indicates how many following 64-bit instruction pointers will follow. This is the current callchain.</p>
<dt><i>size</i>, <i>data[size]</i></p>
<dd> If <code>PERF_SAMPLE_RAW</code> is enabled, then a 32-bit value indicating size is included followed by an array of 8-bit values of length size. The values are padded with 0 to have 64-bit alignment.</p>
<dt>
<dd> This RAW record data is opaque with respect to the ABI. The ABI doesn&#8217;t make any promises with respect to the stability of its content, it may vary depending on event, hardware, and kernel version.</p>
<dt><i>bnr</i>, <i>lbr[bnr]</i></p>
<dd> If <code>PERF_SAMPLE_BRANCH_STACK</code> is enabled, then a 64-bit value indicating the number of records is included, followed by <i>bnr</i> <i>perf_branch_entry</i> structures which each include the fields:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>from</i></p>
<dd> This indicates the source instruction (may not be a branch).</p>
<dt><i>to</i></p>
<dd> The branch target.</p>
<dt><i>mispred</i></p>
<dd> The branch target was mispredicted.</p>
<dt><i>predicted</i></p>
<dd> The branch target was predicted.</p>
<dt><i>in_tx</i> (since Linux 3.11)</p>
<dd> The branch was in a transactional memory transaction.</p>
<dt><i>abort</i> (since Linux 3.11)</p>
<dd> The branch was in an aborted transactional memory transaction.</p>
<dt><i>cycles</i> (since Linux 4.3)</p>
<dd> This reports the number of cycles elapsed since the previous branch stack update.</dl>
<p> The entries are from most to least recent, so the first entry has the most recent branch. </p>
<p> Support for <i>mispred</i>, <i>predicted</i>, and <i>cycles</i> is optional; if not supported, those values will be 0. </p>
<p> The type of branches recorded is specified by the <i>branch_sample_type</i> field.</dl>
<dt><i>abi</i>, <i>regs[weight(mask)]</i></p>
<dd> If <code>PERF_SAMPLE_REGS_USER</code> is enabled, then the user CPU registers are recorded.</p>
<dt>
<dd> The <i>abi</i> field is one of <code>PERF_SAMPLE_REGS_ABI_NONE</code>, <code>PERF_SAMPLE_REGS_ABI_32</code>, or <code>PERF_SAMPLE_REGS_ABI_64</code>.</p>
<dt>
<dd> The <i>regs</i> field is an array of the CPU registers that were specified by the <i>sample_regs_user</i> attr field. The number of values is the number of bits set in the <i>sample_regs_user</i> bit mask.</p>
<dt><i>size</i>, <i>data[size]</i>, <i>dyn_size</i></p>
<dd> If <code>PERF_SAMPLE_STACK_USER</code> is enabled, then the user stack is recorded. This can be used to generate stack backtraces. <i>size</i> is the size requested by the user in <i>sample_stack_user</i> or else the maximum record size. <i>data</i> is the stack data (a raw dump of the memory pointed to by the stack pointer at the time of sampling). <i>dyn_size</i> is the amount of data actually dumped (can be less than <i>size</i>). Note that <i>dyn_size</i> is omitted if <i>size</i> is 0.</p>
<dt><i>weight</i></p>
<dd> If <code>PERF_SAMPLE_WEIGHT</code> is enabled, then a 64-bit value provided by the hardware is recorded that indicates how costly the event was. This allows expensive events to stand out more clearly in profiles.</p>
<dt><i>data_src</i></p>
<dd> If <code>PERF_SAMPLE_DATA_SRC</code> is enabled, then a 64-bit value is recorded that is made up of the following fields:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>mem_op</i></p>
<dd> Type of opcode, a bitwise combination of:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_MEM_OP_NA</code></p>
<dd> Not available</p>
<dt><code>PERF_MEM_OP_LOAD</code></p>
<dd> Load instruction</p>
<dt><code>PERF_MEM_OP_STORE</code></p>
<dd> Store instruction</p>
<dt><code>PERF_MEM_OP_PFETCH</code></p>
<dd> Prefetch</p>
<dt><code>PERF_MEM_OP_EXEC</code></p>
<dd> Executable code</dl>
</dl>
<dt><i>mem_lvl</i></p>
<dd> Memory hierarchy level hit or miss, a bitwise combination of the following, shifted left by <code>PERF_MEM_LVL_SHIFT</code>:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_MEM_LVL_NA</code></p>
<dd> Not available</p>
<dt><code>PERF_MEM_LVL_HIT</code></p>
<dd> Hit</p>
<dt><code>PERF_MEM_LVL_MISS</code></p>
<dd> Miss</p>
<dt><code>PERF_MEM_LVL_L1</code></p>
<dd> Level 1 cache</p>
<dt><code>PERF_MEM_LVL_LFB</code></p>
<dd> Line fill buffer</p>
<dt><code>PERF_MEM_LVL_L2</code></p>
<dd> Level 2 cache</p>
<dt><code>PERF_MEM_LVL_L3</code></p>
<dd> Level 3 cache</p>
<dt><code>PERF_MEM_LVL_LOC_RAM</code></p>
<dd> Local DRAM</p>
<dt><code>PERF_MEM_LVL_REM_RAM1</code></p>
<dd> Remote DRAM 1 hop</p>
<dt><code>PERF_MEM_LVL_REM_RAM2</code></p>
<dd> Remote DRAM 2 hops</p>
<dt><code>PERF_MEM_LVL_REM_CCE1</code></p>
<dd> Remote cache 1 hop</p>
<dt><code>PERF_MEM_LVL_REM_CCE2</code></p>
<dd> Remote cache 2 hops</p>
<dt><code>PERF_MEM_LVL_IO</code></p>
<dd> I/O memory</p>
<dt><code>PERF_MEM_LVL_UNC</code></p>
<dd> Uncached memory</dl>
</dl>
<dt><i>mem_snoop</i></p>
<dd> Snoop mode, a bitwise combination of the following, shifted left by <code>PERF_MEM_SNOOP_SHIFT</code>:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_MEM_SNOOP_NA</code></p>
<dd> Not available</p>
<dt><code>PERF_MEM_SNOOP_NONE</code></p>
<dd> No snoop</p>
<dt><code>PERF_MEM_SNOOP_HIT</code></p>
<dd> Snoop hit</p>
<dt><code>PERF_MEM_SNOOP_MISS</code></p>
<dd> Snoop miss</p>
<dt><code>PERF_MEM_SNOOP_HITM</code></p>
<dd> Snoop hit modified</dl>
</dl>
<dt><i>mem_lock</i></p>
<dd> Lock instruction, a bitwise combination of the following, shifted left by <code>PERF_MEM_LOCK_SHIFT</code>:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_MEM_LOCK_NA</code></p>
<dd> Not available</p>
<dt><code>PERF_MEM_LOCK_LOCKED</code></p>
<dd> Locked transaction</dl>
</dl>
<dt><i>mem_dtlb</i></p>
<dd> TLB access hit or miss, a bitwise combination of the following, shifted left by <code>PERF_MEM_TLB_SHIFT</code>:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_MEM_TLB_NA</code></p>
<dd> Not available</p>
<dt><code>PERF_MEM_TLB_HIT</code></p>
<dd> Hit</p>
<dt><code>PERF_MEM_TLB_MISS</code></p>
<dd> Miss</p>
<dt><code>PERF_MEM_TLB_L1</code></p>
<dd> Level 1 TLB</p>
<dt><code>PERF_MEM_TLB_L2</code></p>
<dd> Level 2 TLB</p>
<dt><code>PERF_MEM_TLB_WK</code></p>
<dd> Hardware walker</p>
<dt><code>PERF_MEM_TLB_OS</code></p>
<dd> OS fault handler</dl>
</dl>
</dl>
</dl>
<dt><i>transaction</i></p>
<dd> If the <code>PERF_SAMPLE_TRANSACTION</code> flag is set, then a 64-bit field is recorded describing the sources of any transactional memory aborts.</p>
<dt>
<dd> The field is a bitwise combination of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_TXN_ELISION</code></p>
<dd> Abort from an elision type transaction (Intel-CPU-specific).</p>
<dt><code>PERF_TXN_TRANSACTION</code></p>
<dd> Abort from a generic transaction.</p>
<dt><code>PERF_TXN_SYNC</code></p>
<dd> Synchronous abort (related to the reported instruction).</p>
<dt><code>PERF_TXN_ASYNC</code></p>
<dd> Asynchronous abort (not related to the reported instruction).</p>
<dt><code>PERF_TXN_RETRY</code></p>
<dd> Retryable abort (retrying the transaction may have succeeded).</p>
<dt><code>PERF_TXN_CONFLICT</code></p>
<dd> Abort due to memory conflicts with other threads.</p>
<dt><code>PERF_TXN_CAPACITY_WRITE</code></p>
<dd> Abort due to write capacity overflow.</p>
<dt><code>PERF_TXN_CAPACITY_READ</code></p>
<dd> Abort due to read capacity overflow.</dl>
</dl>
<dt>
<dd> In addition, a user-specified abort code can be obtained from the high 32 bits of the field by shifting right by <code>PERF_TXN_ABORT_SHIFT</code> and masking with the value <code>PERF_TXN_ABORT_MASK</code>.</p>
<dt><i>abi</i>, <i>regs[weight(mask)]</i></p>
<dd> If <code>PERF_SAMPLE_REGS_INTR</code> is enabled, then the user CPU registers are recorded.</p>
<dt>
<dd> The <i>abi</i> field is one of <code>PERF_SAMPLE_REGS_ABI_NONE</code>, <code>PERF_SAMPLE_REGS_ABI_32</code>, or <code>PERF_SAMPLE_REGS_ABI_64</code>.</p>
<dt>
<dd> The <i>regs</i> field is an array of the CPU registers that were specified by the <i>sample_regs_intr</i> attr field. The number of values is the number of bits set in the <i>sample_regs_intr</i> bit mask.</p>
<dt><i>phys_addr</i></p>
<dd> If the <code>PERF_SAMPLE_PHYS_ADDR</code> flag is set, then the 64-bit physical address is recorded.</p>
<dt><i>cgroup</i></p>
<dd> If the <code>PERF_SAMPLE_CGROUP</code> flag is set, then the 64-bit cgroup ID (for the perf_event subsystem) is recorded. To get the pathname of the cgroup, the ID should match to one in a <code>PERF_RECORD_CGROUP .</code></dl>
</dl>
<dt><code>PERF_RECORD_MMAP2</code></p>
<dd> This record includes extended information on <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) calls returning executable mappings. The format is similar to that of the <code>PERF_RECORD_MMAP</code> record, but includes extra values that allow uniquely identifying shared mappings.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pgoff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maj;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;min;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ino;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ino_generation;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;filename[];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pid</i></p>
<dd> is the process ID.</p>
<dt><i>tid</i></p>
<dd> is the thread ID.</p>
<dt><i>addr</i></p>
<dd> is the address of the allocated memory.</p>
<dt><i>len</i></p>
<dd> is the length of the allocated memory.</p>
<dt><i>pgoff</i></p>
<dd> is the page offset of the allocated memory.</p>
<dt><i>maj</i></p>
<dd> is the major ID of the underlying device.</p>
<dt><i>min</i></p>
<dd> is the minor ID of the underlying device.</p>
<dt><i>ino</i></p>
<dd> is the inode number.</p>
<dt><i>ino_generation</i></p>
<dd> is the inode generation.</p>
<dt><i>prot</i></p>
<dd> is the protection information.</p>
<dt><i>flags</i></p>
<dd> is the flags information.</p>
<dt><i>filename</i></p>
<dd> is a string describing the backing of the allocated memory.</dl>
</dl>
<dt><code>PERF_RECORD_AUX</code> (since Linux 4.1)</p>
<dd> This record reports that new data is available in the separate AUX buffer region.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aux_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aux_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>aux_offset</i></p>
<dd> offset in the AUX mmap region where the new data begins.</p>
<dt><i>aux_size</i></p>
<dd> size of the data made available.</p>
<dt><i>flags</i></p>
<dd> describes the AUX update.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_AUX_FLAG_TRUNCATED</code></p>
<dd> if set, then the data returned was truncated to fit the available buffer size.</p>
<dt><code>PERF_AUX_FLAG_OVERWRITE</code></p>
<dd> if set, then the data returned has overwritten previous data.</dl>
</dl>
</dl>
</dl>
<dt><code>PERF_RECORD_ITRACE_START</code> (since Linux 4.1)</p>
<dd> This record indicates which process has initiated an instruction trace event, allowing tools to properly correlate the instruction addresses in the AUX buffer with the proper executable.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pid</i></p>
<dd> process ID of the thread starting an instruction trace.</p>
<dt><i>tid</i></p>
<dd> thread ID of the thread starting an instruction trace.</dl>
</dl>
<dt><code>PERF_RECORD_LOST_SAMPLES</code> (since Linux 4.2)</p>
<dd> When using hardware sampling (such as Intel PEBS) this record indicates some number of samples that may have been lost.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lost;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>lost</i></p>
<dd> the number of potentially lost samples.</dl>
</dl>
<dt><code>PERF_RECORD_SWITCH</code> (since Linux 4.3)</p>
<dd> This record indicates a context switch has happened. The <code>PERF_RECORD_MISC_SWITCH_OUT</code> bit in the <i>misc</i> field indicates whether it was a context switch into or away from the current process.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dt><code>PERF_RECORD_SWITCH_CPU_WIDE</code> (since Linux 4.3)</p>
<dd> As with <code>PERF_RECORD_SWITCH</code> this record indicates a context switch has happened, but it only occurs when sampling in CPU-wide mode and provides additional information on the process being switched to/from. The <code>PERF_RECORD_MISC_SWITCH_OUT</code> bit in the <i>misc</i> field indicates whether it was a context switch into or away from the current process.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 next_prev_pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 next_prev_tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>next_prev_pid</i></p>
<dd> The process ID of the previous (if switching in) or next (if switching out) process on the CPU.</p>
<dt><i>next_prev_tid</i></p>
<dd> The thread ID of the previous (if switching in) or next (if switching out) thread on the CPU.</dl>
</dl>
<dt><code>PERF_RECORD_NAMESPACES</code> (since Linux 4.11)</p>
<dd> This record includes various namespace information of a process.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nr_namespaces;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;{&nbsp;u64 dev, inode&nbsp;}&nbsp;[nr_namespaces];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>pid</i></p>
<dd> is the process ID</p>
<dt><i>tid</i></p>
<dd> is the thread ID</p>
<dt><i>nr_namespace</i></p>
<dd> is the number of namespaces in this record</dl>
</dl>
<dt>
<dd> Each namespace has <i>dev</i> and <i>inode</i> fields and is recorded in the fixed position like below:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>NET_NS_INDEX</code>=<code>0</code></p>
<dd> Network namespace</p>
<dt><code>UTS_NS_INDEX</code>=<code>1</code></p>
<dd> UTS namespace</p>
<dt><code>IPC_NS_INDEX</code>=<code>2</code></p>
<dd> IPC namespace</p>
<dt><code>PID_NS_INDEX</code>=<code>3</code></p>
<dd> PID namespace</p>
<dt><code>USER_NS_INDEX</code>=<code>4</code></p>
<dd> User namespace</p>
<dt><code>MNT_NS_INDEX</code>=<code>5</code></p>
<dd> Mount namespace</p>
<dt><code>CGROUP_NS_INDEX</code>=<code>6</code></p>
<dd> Cgroup namespace</dl>
</dl>
<dt><code>PERF_RECORD_KSYMBOL</code> (since Linux 5.0)</p>
<dd> This record indicates kernel symbol register/unregister events.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ksym_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;name[];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>addr</i></p>
<dd> is the address of the kernel symbol.</p>
<dt><i>len</i></p>
<dd> is the length of the kernel symbol.</p>
<dt><i>ksym_type</i></p>
<dd> is the type of the kernel symbol. Currently the following types are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_RECORD_KSYMBOL_TYPE_BPF</code></p>
<dd> The kernel symbol is a BPF function.</dl>
</dl>
<dt><i>flags</i></p>
<dd> If the <code>PERF_RECORD_KSYMBOL_FLAGS_UNREGISTER</code> is set, then this event is for unregistering the kernel symbol.</dl>
</dl>
<dt><code>PERF_RECORD_BPF_EVENT</code> (since Linux 5.0)</p>
<dd> This record indicates BPF program is loaded or unloaded.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16 type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16 flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u8 tag[BPF_TAG_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>type</i></p>
<dd> is one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PERF_BPF_EVENT_PROG_LOAD</code></p>
<dd> A BPF program is loaded</p>
<dt><code>PERF_BPF_EVENT_PROG_UNLOAD</code></p>
<dd> A BPF program is unloaded</dl>
</dl>
<dt><i>id</i></p>
<dd> is the ID of the BPF program.</p>
<dt><i>tag</i></p>
<dd> is the tag of the BPF program. Currently, <code>BPF_TAG_SIZE</code> is defined as 8.</dl>
</dl>
<dt><code>PERF_RECORD_CGROUP</code> (since Linux 5.7)</p>
<dd> This record indicates a new cgroup is created and activated.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;path[];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>id</i></p>
<dd> is the cgroup identifier. This can be also retrieved by <code><a href="/docs/linux/man/2-name_to_handle_at/">name_to_handle_at</a></code>(2) on the cgroup path (as a file handle).</p>
<dt><i>path</i></p>
<dd> is the path of the cgroup from the root.</dl>
</dl>
<dt><code>PERF_RECORD_TEXT_POKE</code> (since Linux 5.8)</p>
<dd> This record indicates a change in the kernel text. This includes addition and removal of the text and the corresponding length is zero in this case.</p>
<dt>
<dd> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_header header;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;old_len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;new_len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bytes[];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sample_id sample_id; };</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>addr</i></p>
<dd> is the address of the change</p>
<dt><i>old_len</i></p>
<dd> is the old length</p>
<dt><i>new_len</i></p>
<dd> is the new length</p>
<dt><i>bytes</i></p>
<dd> contains old bytes immediately followed by new bytes.</dl>
</dl>
</dl>
</dl>
</dl>
<h3>Overflow handling</h3>
<p> Events can be set to notify when a threshold is crossed, indicating an overflow. Overflow conditions can be captured by monitoring the event file descriptor with <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). Alternatively, the overflow events can be captured via sa signal handler, by enabling I/O signaling on the file descriptor; see the discussion of the <code>F_SETOWN</code> and <code>F_SETSIG</code> operations in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). </p>
<p> Overflows are generated only by sampling events (<i>sample_period</i> must have a nonzero value). </p>
<p> There are two ways to generate overflow notifications. </p>
<p> The first is to set a <i>wakeup_events</i> or <i>wakeup_watermark</i> value that will trigger if a certain number of samples or bytes have been written to the mmap ring buffer. In this case, <code>POLL_IN</code> is indicated. </p>
<p> The other way is by use of the <code>PERF_EVENT_IOC_REFRESH</code> ioctl. This ioctl adds to a counter that decrements each time the event overflows. When nonzero, <code>POLL_IN</code> is indicated, but once the counter reaches 0 <code>POLL_HUP</code> is indicated and the underlying event is disabled. </p>
<p> Refreshing an event group leader refreshes all siblings and refreshing with a parameter of 0 currently enables infinite refreshes; these behaviors are unsupported and should not be relied on. </p>
<p> Starting with Linux 3.18, <code>POLL_HUP</code> is indicated if the event being monitored is attached to a different process and that process exits.</p>
<h3>rdpmc instruction</h3>
<p> Starting with Linux 3.4 on x86, you can use the <i>rdpmc</i> instruction to get low-latency reads without having to enter the kernel. Note that using <i>rdpmc</i> is not necessarily faster than other methods for reading event values. </p>
<p> Support for this can be detected with the <i>cap_usr_rdpmc</i> field in the mmap page; documentation on how to calculate event values can be found in that section. </p>
<p> Originally, when rdpmc support was enabled, any process (not just ones with an active perf event) could use the rdpmc instruction to access the counters. Starting with Linux 4.0, rdpmc support is only allowed if an event is currently enabled in a process&#8217;s context. To restore the old behavior, write the value 2 to <i>/sys/devices/cpu/rdpmc</i>.</p>
<h3>perf_event ioctl calls</h3>
<p> Various ioctls act on <code>perf_event_open</code>() file descriptors:</p>
<dl>
<dt><code>PERF_EVENT_IOC_ENABLE</code></p>
<dd> This enables the individual event or event group specified by the file descriptor argument.</p>
<dt>
<dd> If the <code>PERF_IOC_FLAG_GROUP</code> bit is set in the ioctl argument, then all events in a group are enabled, even if the event specified is not the group leader (but see BUGS).</p>
<dt><code>PERF_EVENT_IOC_DISABLE</code></p>
<dd> This disables the individual counter or event group specified by the file descriptor argument.</p>
<dt>
<dd> Enabling or disabling the leader of a group enables or disables the entire group; that is, while the group leader is disabled, none of the counters in the group will count. Enabling or disabling a member of a group other than the leader affects only that counter; disabling a non-leader stops that counter from counting but doesn&#8217;t affect any other counter.</p>
<dt>
<dd> If the <code>PERF_IOC_FLAG_GROUP</code> bit is set in the ioctl argument, then all events in a group are disabled, even if the event specified is not the group leader (but see BUGS).</p>
<dt><code>PERF_EVENT_IOC_REFRESH</code></p>
<dd> Non-inherited overflow counters can use this to enable a counter for a number of overflows specified by the argument, after which it is disabled. Subsequent calls of this ioctl add the argument value to the current count. An overflow notification with <code>POLL_IN</code> set will happen on each overflow until the count reaches 0; when that happens a notification with <code>POLL_HUP</code> set is sent and the event is disabled. Using an argument of 0 is considered undefined behavior.</p>
<dt><code>PERF_EVENT_IOC_RESET</code></p>
<dd> Reset the event count specified by the file descriptor argument to zero. This resets only the counts; there is no way to reset the multiplexing <i>time_enabled</i> or <i>time_running</i> values.</p>
<dt>
<dd> If the <code>PERF_IOC_FLAG_GROUP</code> bit is set in the ioctl argument, then all events in a group are reset, even if the event specified is not the group leader (but see BUGS).</p>
<dt><code>PERF_EVENT_IOC_PERIOD</code></p>
<dd> This updates the overflow period for the event.</p>
<dt>
<dd> Since Linux 3.7 (on ARM) and Linux 3.14 (all other architectures), the new period takes effect immediately. On older kernels, the new period did not take effect until after the next overflow.</p>
<dt>
<dd> The argument is a pointer to a 64-bit value containing the desired new period.</p>
<dt>
<dd> Prior to Linux 2.6.36, this ioctl always failed due to a bug in the kernel.</p>
<dt><code>PERF_EVENT_IOC_SET_OUTPUT</code></p>
<dd> This tells the kernel to report event notifications to the specified file descriptor rather than the default one. The file descriptors must all be on the same CPU.</p>
<dt>
<dd> The argument specifies the desired file descriptor, or -1 if output should be ignored.</p>
<dt><code>PERF_EVENT_IOC_SET_FILTER</code> (since Linux 2.6.33)</p>
<dd> This adds an ftrace filter to this event.</p>
<dt>
<dd> The argument is a pointer to the desired ftrace filter.</p>
<dt><code>PERF_EVENT_IOC_ID</code> (since Linux 3.12)</p>
<dd> This returns the event ID value for the given event file descriptor.</p>
<dt>
<dd> The argument is a pointer to a 64-bit unsigned integer to hold the result.</p>
<dt><code>PERF_EVENT_IOC_SET_BPF</code> (since Linux 4.1)</p>
<dd> This allows attaching a Berkeley Packet Filter (BPF) program to an existing kprobe tracepoint event. You need <code>CAP_PERFMON</code> (since Linux 5.8) or <code>CAP_SYS_ADMIN</code> privileges to use this ioctl.</p>
<dt>
<dd> The argument is a BPF program file descriptor that was created by a previous <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2) system call.</p>
<dt><code>PERF_EVENT_IOC_PAUSE_OUTPUT</code> (since Linux 4.7)</p>
<dd> This allows pausing and resuming the event&#8217;s ring-buffer. A paused ring-buffer does not prevent generation of samples, but simply discards them. The discarded samples are considered lost, and cause a <code>PERF_RECORD_LOST</code> sample to be generated when possible. An overflow signal may still be triggered by the discarded sample even though the ring-buffer remains empty.</p>
<dt>
<dd> The argument is an unsigned 32-bit integer. A nonzero value pauses the ring-buffer, while a zero value resumes the ring-buffer.</p>
<dt><code>PERF_EVENT_MODIFY_ATTRIBUTES</code> (since Linux 4.17)</p>
<dd> This allows modifying an existing event without the overhead of closing and reopening a new event. Currently this is supported only for breakpoint events.</p>
<dt>
<dd> The argument is a pointer to a <i>perf_event_attr</i> structure containing the updated event settings.</p>
<dt><code>PERF_EVENT_IOC_QUERY_BPF</code> (since Linux 4.16)</p>
<dd> This allows querying which Berkeley Packet Filter (BPF) programs are attached to an existing kprobe tracepoint. You can only attach one BPF program per event, but you can have multiple events attached to a tracepoint. Querying this value on one tracepoint event returns the ID of all BPF programs in all events attached to the tracepoint. You need <code>CAP_PERFMON</code> (since Linux 5.8) or <code>CAP_SYS_ADMIN</code> privileges to use this ioctl.</p>
<dt>
<dd> The argument is a pointer to a structure struct perf_event_query_bpf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ids_len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prog_cnt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ids[0]; };</p>
<dt>
<dd> The <i>ids_len</i> field indicates the number of ids that can fit in the provided <i>ids</i> array. The <i>prog_cnt</i> value is filled in by the kernel with the number of attached BPF programs. The <i>ids</i> array is filled with the ID of each attached BPF program. If there are more programs than will fit in the array, then the kernel will return <code>ENOSPC</code> and <i>ids_len</i> will indicate the number of program IDs that were successfully copied.</dl>
<h3>Using <a href="/docs/linux/man/2-prctl/">prctl</a>(2)</h3>
<p> A process can enable or disable all currently open event groups using the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_TASK_PERF_EVENTS_ENABLE</code> and <code>PR_TASK_PERF_EVENTS_DISABLE</code> operations. This applies only to events created locally by the calling process. This does not apply to events created by other processes attached to the calling process or inherited events from a parent process. Only group leaders are enabled and disabled, not any other members of the groups.</p>
<h3>perf_event related configuration files</h3>
<p> Files in <i>/proc/sys/kernel/</i></p>
<dl>
<dt>
<dd>
<dl>
<dt><i>/proc/sys/kernel/perf_event_paranoid</i></p>
<dd> The <i>perf_event_paranoid</i> file can be set to restrict access to the performance counters.</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>2</p>
<dd> allow only user-space measurements (default since Linux 4.6).</p>
<dt>1</p>
<dd> allow both kernel and user measurements (default before Linux 4.6).</p>
<dt>0</p>
<dd> allow access to CPU-specific data but not raw tracepoint samples.</p>
<dt>-1</p>
<dd> no restrictions.</dl>
</dl>
<dt>
<dd> The existence of the <i>perf_event_paranoid</i> file is the official method for determining if a kernel supports <code>perf_event_open</code>().</p>
<dt><i>/proc/sys/kernel/perf_event_max_sample_rate</i></p>
<dd> This sets the maximum sample rate. Setting this too high can allow users to sample at a rate that impacts overall machine performance and potentially lock up the machine. The default value is 100000 (samples per second).</p>
<dt><i>/proc/sys/kernel/perf_event_max_stack</i></p>
<dd> This file sets the maximum depth of stack frame entries reported when generating a call trace.</p>
<dt><i>/proc/sys/kernel/perf_event_mlock_kb</i></p>
<dd> Maximum number of pages an unprivileged user can <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2). The default is 516 (kB).</dl>
</dl>
<p> Files in <i>/sys/bus/event_source/devices/</i> </p>
<dl>
<dt>
<dd> Since Linux 2.6.34, the kernel supports having multiple PMUs available for monitoring. Information on how to program these PMUs can be found under <i>/sys/bus/event_source/devices/</i>. Each subdirectory corresponds to a different PMU.</p>
<dl>
<dt><i>/sys/bus/event_source/devices/*/type</i> (since Linux 2.6.38)</p>
<dd> This contains an integer that can be used in the <i>type</i> field of <i>perf_event_attr</i> to indicate that you wish to use this PMU.</p>
<dt><i>/sys/bus/event_source/devices/cpu/rdpmc</i> (since Linux 3.4)</p>
<dd> If this file is 1, then direct user-space access to the performance counter registers is allowed via the rdpmc instruction. This can be disabled by echoing 0 to the file.</p>
<dt>
<dd> As of Linux 4.0 the behavior has changed, so that 1 now means only allow access to processes with active perf events, with 2 indicating the old allow-anyone-access behavior.</p>
<dt><i>/sys/bus/event_source/devices/*/format/</i> (since Linux 3.4)</p>
<dd> This subdirectory contains information on the architecture-specific subfields available for programming the various <i>config</i> fields in the <i>perf_event_attr</i> struct.</p>
<dt>
<dd> The content of each file is the name of the config field, followed by a colon, followed by a series of integer bit ranges separated by commas. For example, the file <i>event</i> may contain the value <i>config1:1,6-10,44</i> which indicates that event is an attribute that occupies bits 1,6-10, and 44 of <i>perf_event_attr::config1</i>.</p>
<dt><i>/sys/bus/event_source/devices/*/events/</i> (since Linux 3.4)</p>
<dd> This subdirectory contains files with predefined events. The contents are strings describing the event settings expressed in terms of the fields found in the previously mentioned <i>./format/</i> directory. These are not necessarily complete lists of all events supported by a PMU, but usually a subset of events deemed useful or interesting.</p>
<dt>
<dd> The content of each file is a list of attribute names separated by commas. Each entry has an optional value (either hex or decimal). If no value is specified, then it is assumed to be a single-bit field with a value of 1. An example entry may look like this: <i>event=0x2,inv,ldlat=3</i>.</p>
<dt><i>/sys/bus/event_source/devices/*/uevent</i></p>
<dd> This file is the standard kernel device interface for injecting hotplug events.</p>
<dt><i>/sys/bus/event_source/devices/*/cpumask</i> (since Linux 3.7)</p>
<dd> The <i>cpumask</i> file contains a comma-separated list of integers that indicate a representative CPU number for each socket (package) on the motherboard. This is needed when setting up uncore or northbridge events, as those PMUs present socket-wide events.</dl>
</dl>
<h2>RETURN VALUE</h2>
<p> <code>perf_event_open</code>() returns the new file descriptor, or -1 if an error occurred (in which case, <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<p> The errors returned by <code>perf_event_open</code>() can be inconsistent, and may vary across processor architectures and performance monitoring units.</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> Returned if the <i>perf_event_attr</i> <i>size</i> value is too small (smaller than <code>PERF_ATTR_SIZE_VER0</code>), too big (larger than the page size), or larger than the kernel supports and the extra bytes are not zero. When <code>E2BIG</code> is returned, the <i>perf_event_attr</i> <i>size</i> field is overwritten by the kernel to be the size of the structure it was expecting.</p>
<dt><code>EACCES</code></p>
<dd> Returned when the requested event requires <code>CAP_PERFMON</code> (since Linux 5.8) or <code>CAP_SYS_ADMIN</code> permissions (or a more permissive perf_event paranoid setting). Some common cases where an unprivileged process may encounter this error: attaching to a process owned by a different user; monitoring all processes on a given CPU (i.e., specifying the <i>pid</i> argument as -1); and not setting <i>exclude_kernel</i> when the paranoid setting requires it.</p>
<dt><code>EBADF</code></p>
<dd> Returned if the <i>group_fd</i> file descriptor is not valid, or, if <code>PERF_FLAG_PID_CGROUP</code> is set, the cgroup file descriptor in <i>pid</i> is not valid.</p>
<dt><code>EBUSY</code> (since Linux 4.1)</p>
<dd> Returned if another event already has exclusive access to the PMU.</p>
<dt><code>EFAULT</code></p>
<dd> Returned if the <i>attr</i> pointer points at an invalid memory address.</p>
<dt><code>EINVAL</code></p>
<dd> Returned if the specified event is invalid. There are many possible reasons for this. A not-exhaustive list: <i>sample_freq</i> is higher than the maximum setting; the <i>cpu</i> to monitor does not exist; <i>read_format</i> is out of range; <i>sample_type</i> is out of range; the <i>flags</i> value is out of range; <i>exclusive</i> or <i>pinned</i> set and the event is not a group leader; the event <i>config</i> values are out of range or set reserved bits; the generic event selected is not supported; or there is not enough room to add the selected event.</p>
<dt><code>EINTR</code></p>
<dd> Returned when trying to mix perf and ftrace handling for a uprobe.</p>
<dt><code>EMFILE</code></p>
<dd> Each opened event uses one file descriptor. If a large number of events are opened, the per-process limit on the number of open file descriptors will be reached, and no more events can be created.</p>
<dt><code>ENODEV</code></p>
<dd> Returned when the event involves a feature not supported by the current CPU.</p>
<dt><code>ENOENT</code></p>
<dd> Returned if the <i>type</i> setting is not valid. This error is also returned for some unsupported generic events.</p>
<dt><code>ENOSPC</code></p>
<dd> Prior to Linux 3.3, if there was not enough room for the event, <code>ENOSPC</code> was returned. In Linux 3.3, this was changed to <code>EINVAL</code>. <code>ENOSPC</code> is still returned if you try to add more breakpoint events than supported by the hardware.</p>
<dt><code>ENOSYS</code></p>
<dd> Returned if <code>PERF_SAMPLE_STACK_USER</code> is set in <i>sample_type</i> and it is not supported by hardware.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> Returned if an event requiring a specific hardware feature is requested but there is no hardware support. This includes requesting low-skid events if not supported, branch tracing if it is not available, sampling if no PMU interrupt is available, and branch stacks for software events.</p>
<dt><code>EOVERFLOW</code> (since Linux 4.8)</p>
<dd> Returned if <code>PERF_SAMPLE_CALLCHAIN</code> is requested and <i>sample_max_stack</i> is larger than the maximum specified in <i>/proc/sys/kernel/perf_event_max_stack</i>.</p>
<dt><code>EPERM</code></p>
<dd> Returned on many (but not all) architectures when an unsupported <i>exclude_hv</i>, <i>exclude_idle</i>, <i>exclude_user</i>, or <i>exclude_kernel</i> setting is specified.</p>
<dt>
<dd> It can also happen, as with <code>EACCES</code>, when the requested event requires <code>CAP_PERFMON</code> (since Linux 5.8) or <code>CAP_SYS_ADMIN</code> permissions (or a more permissive perf_event paranoid setting). This includes setting a breakpoint on a kernel address, and (since Linux 3.13) setting a kernel function-trace tracepoint.</p>
<dt><code>ESRCH</code></p>
<dd> Returned if attempting to attach to a process that does not exist.</dl>
<h2>VERSION</h2>
<p> <code>perf_event_open</code>() was introduced in Linux 2.6.31 but was called <code>perf_counter_open</code>(). It was renamed in Linux 2.6.32.</p>
<h2>CONFORMING TO</h2>
<p> This <code>perf_event_open</code>() system call Linux-specific and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). See the example below. </p>
<p> The official way of knowing if <code>perf_event_open</code>() support is enabled is checking for the existence of the file <i>/proc/sys/kernel/perf_event_paranoid</i>. </p>
<p> <code>CAP_PERFMON</code> capability (since Linux 5.8) provides secure approach to performance monitoring and observability operations in a system according to the principal of least privilege (POSIX IEEE 1003.1e). Accessing system performance monitoring and observability operations using <code>CAP_PERFMON</code> rather than the much more powerful <code>CAP_SYS_ADMIN</code> excludes chances to misuse credentials and makes operations more secure. <code>CAP_SYS_ADMIN</code> usage for secure system performance monitoring and observability is discouraged in favor of the <code>CAP_PERFMON</code> capability.</p>
<h2>BUGS</h2>
<p> The <code>F_SETOWN_EX</code> option to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) is needed to properly get overflow signals in threads. This was introduced in Linux 2.6.32. </p>
<p> Prior to Linux 2.6.33 (at least for x86), the kernel did not check if events could be scheduled together until read time. The same happens on all known kernels if the NMI watchdog is enabled. This means to see if a given set of events works you have to <code>perf_event_open</code>(), start, then read before you know for sure you can get valid measurements. </p>
<p> Prior to Linux 2.6.34, event constraints were not enforced by the kernel. In that case, some events would silently return &quot;0&quot; if the kernel scheduled them in an improper counter slot. </p>
<p> Prior to Linux 2.6.34, there was a bug when multiplexing where the wrong results could be returned. </p>
<p> Kernels from Linux 2.6.35 to Linux 2.6.39 can quickly crash the kernel if &quot;inherit&quot; is enabled and many threads are started. </p>
<p> Prior to Linux 2.6.35, <code>PERF_FORMAT_GROUP</code> did not work with attached processes. </p>
<p> There is a bug in the kernel code between Linux 2.6.36 and Linux 3.0 that ignores the &quot;watermark&quot; field and acts as if a wakeup_event was chosen if the union has a nonzero value in it. </p>
<p> From Linux 2.6.31 to Linux 3.4, the <code>PERF_IOC_FLAG_GROUP</code> ioctl argument was broken and would repeatedly operate on the event specified rather than iterating across all sibling events in a group. </p>
<p> From Linux 3.4 to Linux 3.11, the mmap <i>cap_usr_rdpmc</i> and <i>cap_usr_time</i> bits mapped to the same location. Code should migrate to the new <i>cap_user_rdpmc</i> and <i>cap_user_time</i> fields instead. </p>
<p> Always double-check your results! Various generalized events have had wrong values. For example, retired branches measured the wrong thing on AMD machines until Linux 2.6.35.</p>
<h2>EXAMPLES</h2>
<p> The following is a short example that measures the total instruction count of a call to <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3). </p>
<p> #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;linux/perf_event.h&gt; #include &lt;asm/unistd.h&gt; </p>
<p> static long perf_event_open(struct perf_event_attr *hw_event, pid_t pid,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int cpu, int group_fd, unsigned long flags) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;syscall(__NR_perf_event_open, hw_event, pid, cpu,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;group_fd, flags);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret; } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct perf_event_attr pe;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long long count;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;pe, 0, sizeof(pe));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.type&nbsp;=&nbsp;PERF_TYPE_HARDWARE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.size&nbsp;=&nbsp;sizeof(pe);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.config&nbsp;=&nbsp;PERF_COUNT_HW_INSTRUCTIONS;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.disabled&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.exclude_kernel&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pe.exclude_hv&nbsp;=&nbsp;1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;perf_event_open(&amp;pe, 0, -1, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Error opening leader&nbsp;%llx
&quot;, pe.config);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ioctl(fd, PERF_EVENT_IOC_RESET, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ioctl(fd, PERF_EVENT_IOC_ENABLE, 0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Measuring instruction count for this printf
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ioctl(fd, PERF_EVENT_IOC_DISABLE, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read(fd,&nbsp;&amp;count, sizeof(count)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Used&nbsp;%lld instructions
&quot;, count); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf/">perf</a></code>(1), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2) </p>
<p> <i>Documentation/admin-guide/perf-security.rst</i> in the kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
