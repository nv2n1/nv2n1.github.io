---
title: "sched(7)"
name: "sched"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sched/"
description: "sched – overview of CPU scheduling"
---

<p>sched &#8211; overview of CPU scheduling</p>
<h2>Description</h2>
<p>Since Linux 2.6.23, the default scheduler is CFS, the &quot;Completely Fair Scheduler&quot;. The CFS scheduler replaced the earlier &quot;<a href="/docs/linux/man/1-o/">O</a>(1)&quot; scheduler.</p>
<h3>API summary</h3>
<p>Linux provides the following system calls for controlling the CPU scheduling behavior, policy, and priority of processes (or, more precisely, threads).</p>
<dl>
<dt><code><a href="/docs/linux/man/2-nice/">nice</a></code>(2)</p>
<dd>Set a new nice value for the calling thread, and return the new nice value.</p>
<dt><code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2)</p>
<dd>Return the nice value of a thread, a process group, or the set of threads owned by a specified user.</p>
<dt><code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)</p>
<dd>Set the nice value of a thread, a process group, or the set of threads owned by a specified user.</p>
<dt><code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2)</p>
<dd>Set the scheduling policy and parameters of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2)</p>
<dd>Return the scheduling policy of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2)</p>
<dd>Set the scheduling parameters of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2)</p>
<dd>Fetch the scheduling parameters of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2)</p>
<dd>Return the maximum priority available in a specified scheduling policy.</p>
<dt><code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2)</p>
<dd>Return the minimum priority available in a specified scheduling policy.</p>
<dt><code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2)</p>
<dd>Fetch the quantum used for threads that are scheduled under the &quot;round-robin&quot; scheduling policy.</p>
<dt><code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2)</p>
<dd>Cause the caller to relinquish the CPU, so that some other thread be executed.</p>
<dt><code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)</p>
<dd>(Linux-specific) Set the CPU affinity of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2)</p>
<dd>(Linux-specific) Get the CPU affinity of a specified thread.</p>
<dt><code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2)</p>
<dd>Set the scheduling policy and parameters of a specified thread. This (Linux-specific) system call provides a superset of the functionality of <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) and <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2).</p>
<dt><code><a href="/docs/linux/man/2-sched_getattr/">sched_getattr</a></code>(2)</p>
<dd>Fetch the scheduling policy and parameters of a specified thread. This (Linux-specific) system call provides a superset of the functionality of <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2) and <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2).</dl>
<h3>Scheduling policies</h3>
<p>The scheduler is the kernel component that decides which runnable thread will be executed by the CPU next. Each thread has an associated scheduling policy and a <i>static</i> scheduling priority, <i>sched_priority</i>. The scheduler makes its decisions based on knowledge of the scheduling policy and static priority of all threads on the system. </p>
<p> For threads scheduled under one of the normal scheduling policies (<code>SCHED_OTHER</code>, <code>SCHED_IDLE</code>, <code>SCHED_BATCH</code>), <i>sched_priority</i> is not used in scheduling decisions (it must be specified as 0). </p>
<p> Processes scheduled under one of the real-time policies (<code>SCHED_FIFO</code>, <code>SCHED_RR</code>) have a <i>sched_priority</i> value in the range 1 (low) to 99 (high). (As the numbers imply, real-time threads always have higher priority than normal threads.) Note well: POSIX.1 requires an implementation to support only a minimum 32 distinct priority levels for the real-time policies, and some systems supply just this minimum. Portable programs should use <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2) and <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2) to find the range of priorities supported for a particular policy. </p>
<p> Conceptually, the scheduler maintains a list of runnable threads for each possible <i>sched_priority</i> value. In order to determine which thread runs next, the scheduler looks for the nonempty list with the highest static priority and selects the thread at the head of this list. </p>
<p> A thread&#8217;s scheduling policy determines where it will be inserted into the list of threads with equal static priority and how it will move inside this list. </p>
<p> All scheduling is preemptive: if a thread with a higher static priority becomes ready to run, the currently running thread will be preempted and returned to the wait list for its static priority level. The scheduling policy determines the ordering only within the list of runnable threads with equal static priority.</p>
<h3>SCHED_FIFO: First in-first out scheduling</h3>
<p><code>SCHED_FIFO</code> can be used only with static priorities higher than 0, which means that when a <code>SCHED_FIFO</code> thread becomes runnable, it will always immediately preempt any currently running <code>SCHED_OTHER</code>, <code>SCHED_BATCH</code>, or <code>SCHED_IDLE</code> thread. <code>SCHED_FIFO</code> is a simple scheduling algorithm without time slicing. For threads scheduled under the <code>SCHED_FIFO</code> policy, the following rules apply:</p>
<dl>
<dt>1)</p>
<dd>A running <code>SCHED_FIFO</code> thread that has been preempted by another thread of higher priority will stay at the head of the list for its priority and will resume execution as soon as all threads of higher priority are blocked again.</p>
<dt>2)</p>
<dd>When a blocked <code>SCHED_FIFO</code> thread becomes runnable, it will be inserted at the end of the list for its priority.</p>
<dt>3)</p>
<dd>If a call to <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2), <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), or <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3) changes the priority of the running or runnable <code>SCHED_FIFO</code> thread identified by <i>pid</i> the effect on the thread&#8217;s position in the list depends on the direction of the change to threads priority:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the thread&#8217;s priority is raised, it is placed at the end of the list for its new priority. As a consequence, it may preempt a currently running thread with the same priority.</p>
<dt>&bull;</p>
<dd>If the thread&#8217;s priority is unchanged, its position in the run list is unchanged.</p>
<dt>&bull;</p>
<dd>If the thread&#8217;s priority is lowered, it is placed at the front of the list for its new priority.</dl>
</dl>
<dd>According to POSIX.1-2008, changes to a thread&#8217;s priority (or policy) using any mechanism other than <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3) should result in the thread being placed at the end of the list for its priority.</p>
<dt>4)</p>
<dd>A thread calling <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2) will be put at the end of the list.</dl>
<p> No other events will move a thread scheduled under the <code>SCHED_FIFO</code> policy in the wait list of runnable threads with equal static priority. </p>
<p> A <code>SCHED_FIFO</code> thread runs until either it is blocked by an I/O request, it is preempted by a higher priority thread, or it calls <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2).</p>
<h3>SCHED_RR: Round-robin scheduling</h3>
<p><code>SCHED_RR</code> is a simple enhancement of <code>SCHED_FIFO</code>. Everything described above for <code>SCHED_FIFO</code> also applies to <code>SCHED_RR</code>, except that each thread is allowed to run only for a maximum time quantum. If a <code>SCHED_RR</code> thread has been running for a time period equal to or longer than the time quantum, it will be put at the end of the list for its priority. A <code>SCHED_RR</code> thread that has been preempted by a higher priority thread and subsequently resumes execution as a running thread will complete the unexpired portion of its round-robin time quantum. The length of the time quantum can be retrieved using <code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2).</p>
<h3>SCHED_DEADLINE: Sporadic task model deadline scheduling</h3>
<p>Since version 3.14, Linux provides a deadline scheduling policy (<code>SCHED_DEADLINE</code>). This policy is currently implemented using GEDF (Global Earliest Deadline First) in conjunction with CBS (Constant Bandwidth Server). To set and fetch this policy and associated attributes, one must use the Linux-specific <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2) and <code><a href="/docs/linux/man/2-sched_getattr/">sched_getattr</a></code>(2) system calls. </p>
<p> A sporadic task is one that has a sequence of jobs, where each job is activated at most once per period. Each job also has a <i>relative deadline</i>, before which it should finish execution, and a <i>computation time</i>, which is the CPU time necessary for executing the job. The moment when a task wakes up because a new job has to be executed is called the <i>arrival time</i> (also referred to as the request time or release time). The <i>start time</i> is the time at which a task starts its execution. The <i>absolute deadline</i> is thus obtained by adding the relative deadline to the arrival time. </p>
<p> The following diagram clarifies these terms: </p>
<p> arrival/wakeup absolute deadline<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v &#8212;&#8211;x&#8212;&#8212;&#8211;xooooooooooooooooo&#8212;&#8212;&#8211;x&#8212;&#8212;&#8211;x&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;- comp. time -&gt;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;&#8212;&#8212;- relative deadline &#8212;&#8212;&gt;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;&#8212;&#8212;&#8212;&#8212;&#8211; period &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-&gt;| </p>
<p> When setting a <code>SCHED_DEADLINE</code> policy for a thread using <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2), one can specify three parameters: <i>Runtime</i>, <i>Deadline</i>, and <i>Period</i>. These parameters do not necessarily correspond to the aforementioned terms: usual practice is to set Runtime to something bigger than the average computation time (or worst-case execution time for hard real-time tasks), Deadline to the relative deadline, and Period to the period of the task. Thus, for <code>SCHED_DEADLINE</code> scheduling, we have: </p>
<p> arrival/wakeup absolute deadline<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;v &#8212;&#8211;x&#8212;&#8212;&#8211;xooooooooooooooooo&#8212;&#8212;&#8211;x&#8212;&#8212;&#8211;x&#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;&#8211; Runtime &#8212;&#8212;-&gt;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;&#8212;&#8212;&#8212;&#8211; Deadline &#8212;&#8212;&#8212;&#8211;&gt;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;|&lt;&#8212;&#8212;&#8212;&#8212;&#8211; Period &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-&gt;| </p>
<p> The three deadline-scheduling parameters correspond to the <i>sched_runtime</i>, <i>sched_deadline</i>, and <i>sched_period</i> fields of the <i>sched_attr</i> structure; see <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2). These fields express values in nanoseconds. If <i>sched_period</i> is specified as 0, then it is made the same as <i>sched_deadline</i>. </p>
<p> The kernel requires that: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched_runtime&nbsp;&lt;=&nbsp;sched_deadline&nbsp;&lt;=&nbsp;sched_period </p>
<p> In addition, under the current implementation, all of the parameter values must be at least 1024 (i.e., just over one microsecond, which is the resolution of the implementation), and less than 2^63. If any of these checks fails, <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2) fails with the error <code>EINVAL</code>. </p>
<p> The CBS guarantees non-interference between tasks, by throttling threads that attempt to over-run their specified Runtime. </p>
<p> To ensure deadline scheduling guarantees, the kernel must prevent situations where the set of <code>SCHED_DEADLINE</code> threads is not feasible (schedulable) within the given constraints. The kernel thus performs an admittance test when setting or changing <code>SCHED_DEADLINE</code> policy and attributes. This admission test calculates whether the change is feasible; if it is not, <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2) fails with the error <code>EBUSY</code>. </p>
<p> For example, it is required (but not necessarily sufficient) for the total utilization to be less than or equal to the total number of CPUs available, where, since each thread can maximally run for Runtime per Period, that thread&#8217;s utilization is its Runtime divided by its Period. </p>
<p> In order to fulfill the guarantees that are made when a thread is admitted to the <code>SCHED_DEADLINE</code> policy, <code>SCHED_DEADLINE</code> threads are the highest priority (user controllable) threads in the system; if any <code>SCHED_DEADLINE</code> thread is runnable, it will preempt any thread scheduled under one of the other policies. </p>
<p> A call to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) by a thread scheduled under the <code>SCHED_DEADLINE</code> policy fails with the error <code>EAGAIN</code>, unless the thread has its reset-on-fork flag set (see below). </p>
<p> A <code>SCHED_DEADLINE</code> thread that calls <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2) will yield the current job and wait for a new period to begin.</p>
<h3>SCHED_OTHER: Default Linux time-sharing scheduling</h3>
<p><code>SCHED_OTHER</code> can be used at only static priority 0 (i.e., threads under real-time policies always have priority over <code>SCHED_OTHER</code> processes). <code>SCHED_OTHER</code> is the standard Linux time-sharing scheduler that is intended for all threads that do not require the special real-time mechanisms. </p>
<p> The thread to run is chosen from the static priority 0 list based on a <i>dynamic</i> priority that is determined only inside this list. The dynamic priority is based on the nice value (see below) and is increased for each time quantum the thread is ready to run, but denied to run by the scheduler. This ensures fair progress among all <code>SCHED_OTHER</code> threads. </p>
<p> In the Linux kernel source code, the <code>SCHED_OTHER</code> policy is actually named <code>SCHED_NORMAL</code>.</p>
<h3>The nice value</h3>
<p>The nice value is an attribute that can be used to influence the CPU scheduler to favor or disfavor a process in scheduling decisions. It affects the scheduling of <code>SCHED_OTHER</code> and <code>SCHED_BATCH</code> (see below) processes. The nice value can be modified using <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), or <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2). </p>
<p> According to POSIX.1, the nice value is a per-process attribute; that is, the threads in a process should share a nice value. However, on Linux, the nice value is a per-thread attribute: different threads in the same process may have different nice values. </p>
<p> The range of the nice value varies across UNIX systems. On modern Linux, the range is -20 (high priority) to +19 (low priority). On some other systems, the range is -20..20. Very early Linux kernels (Before Linux 2.0) had the range -infinity..15. </p>
<p> The degree to which the nice value affects the relative scheduling of <code>SCHED_OTHER</code> processes likewise varies across UNIX systems and across Linux kernel versions. </p>
<p> With the advent of the CFS scheduler in kernel 2.6.23, Linux adopted an algorithm that causes relative differences in nice values to have a much stronger effect. In the current implementation, each unit of difference in the nice values of two processes results in a factor of 1.25 in the degree to which the scheduler favors the higher priority process. This causes very low nice values (+19) to truly provide little CPU to a process whenever there is any other higher priority load on the system, and makes high nice values (-20) deliver most of the CPU to applications that require it (e.g., some audio applications). </p>
<p> On Linux, the <code>RLIMIT_NICE</code> resource limit can be used to define a limit to which an unprivileged process&#8217;s nice value can be raised; see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) for details. </p>
<p> For further details on the nice value, see the subsections on the autogroup feature and group scheduling, below.</p>
<h3>SCHED_BATCH: Scheduling batch processes</h3>
<p>(Since Linux 2.6.16.) <code>SCHED_BATCH</code> can be used only at static priority 0. This policy is similar to <code>SCHED_OTHER</code> in that it schedules the thread according to its dynamic priority (based on the nice value). The difference is that this policy will cause the scheduler to always assume that the thread is CPU-intensive. Consequently, the scheduler will apply a small scheduling penalty with respect to wakeup behavior, so that this thread is mildly disfavored in scheduling decisions. </p>
<p> This policy is useful for workloads that are noninteractive, but do not want to lower their nice value, and for workloads that want a deterministic scheduling policy without interactivity causing extra preemptions (between the workload&#8217;s tasks).</p>
<h3>SCHED_IDLE: Scheduling very low priority jobs</h3>
<p>(Since Linux 2.6.23.) <code>SCHED_IDLE</code> can be used only at static priority 0; the process nice value has no influence for this policy. </p>
<p> This policy is intended for running jobs at extremely low priority (lower even than a +19 nice value with the <code>SCHED_OTHER</code> or <code>SCHED_BATCH</code> policies).</p>
<h3>Resetting scheduling policy for child processes</h3>
<p>Each thread has a reset-on-fork scheduling flag. When this flag is set, children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) do not inherit privileged scheduling policies. The reset-on-fork flag can be set by either:</p>
<dl>
<dt>*</p>
<dd>ORing the <code>SCHED_RESET_ON_FORK</code> flag into the <i>policy</i> argument when calling <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2) (since Linux 2.6.32); or</p>
<dt>*</p>
<dd>specifying the <code>SCHED_FLAG_RESET_ON_FORK</code> flag in <i>attr.sched_flags</i> when calling <code><a href="/docs/linux/man/2-sched_setattr/">sched_setattr</a></code>(2).</dl>
<p> Note that the constants used with these two APIs have different names. The state of the reset-on-fork flag can analogously be retrieved using <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2) and <code><a href="/docs/linux/man/2-sched_getattr/">sched_getattr</a></code>(2). </p>
<p> The reset-on-fork feature is intended for media-playback applications, and can be used to prevent applications evading the <code>RLIMIT_RTTIME</code> resource limit (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)) by creating multiple child processes. </p>
<p> More precisely, if the reset-on-fork flag is set, the following rules apply for subsequently created children:</p>
<dl>
<dt>*</p>
<dd>If the calling thread has a scheduling policy of <code>SCHED_FIFO</code> or <code>SCHED_RR</code>, the policy is reset to <code>SCHED_OTHER</code> in child processes.</p>
<dt>*</p>
<dd>If the calling process has a negative nice value, the nice value is reset to zero in child processes.</dl>
<p> After the reset-on-fork flag has been enabled, it can be reset only if the thread has the <code>CAP_SYS_NICE</code> capability. This flag is disabled in child processes created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<h3>Privileges and resource limits</h3>
<p>In Linux kernels before 2.6.12, only privileged (<code>CAP_SYS_NICE</code>) threads can set a nonzero static priority (i.e., set a real-time scheduling policy). The only change that an unprivileged thread can make is to set the <code>SCHED_OTHER</code> policy, and this can be done only if the effective user ID of the caller matches the real or effective user ID of the target thread (i.e., the thread specified by <i>pid</i>) whose policy is being changed. </p>
<p> A thread must be privileged (<code>CAP_SYS_NICE</code>) in order to set or modify a <code>SCHED_DEADLINE</code> policy. </p>
<p> Since Linux 2.6.12, the <code>RLIMIT_RTPRIO</code> resource limit defines a ceiling on an unprivileged thread&#8217;s static priority for the <code>SCHED_RR</code> and <code>SCHED_FIFO</code> policies. The rules for changing scheduling policy and priority are as follows:</p>
<dl>
<dt>*</p>
<dd>If an unprivileged thread has a nonzero <code>RLIMIT_RTPRIO</code> soft limit, then it can change its scheduling policy and priority, subject to the restriction that the priority cannot be set to a value higher than the maximum of its current priority and its <code>RLIMIT_RTPRIO</code> soft limit.</p>
<dt>*</p>
<dd>If the <code>RLIMIT_RTPRIO</code> soft limit is 0, then the only permitted changes are to lower the priority, or to switch to a non-real-time policy.</p>
<dt>*</p>
<dd>Subject to the same rules, another unprivileged thread can also make these changes, as long as the effective user ID of the thread making the change matches the real or effective user ID of the target thread.</p>
<dt>*</p>
<dd>Special rules apply for the <code>SCHED_IDLE</code> policy. In Linux kernels before 2.6.39, an unprivileged thread operating under this policy cannot change its policy, regardless of the value of its <code>RLIMIT_RTPRIO</code> resource limit. In Linux kernels since 2.6.39, an unprivileged thread can switch to either the <code>SCHED_BATCH</code> or the <code>SCHED_OTHER</code> policy so long as its nice value falls within the range permitted by its <code>RLIMIT_NICE</code> resource limit (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</dl>
<p> Privileged (<code>CAP_SYS_NICE</code>) threads ignore the <code>RLIMIT_RTPRIO</code> limit; as with older kernels, they can make arbitrary changes to scheduling policy and priority. See <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) for further information on <code>RLIMIT_RTPRIO</code>.</p>
<h3>Limiting the CPU usage of real-time and deadline processes</h3>
<p>A nonblocking infinite loop in a thread scheduled under the <code>SCHED_FIFO</code>, <code>SCHED_RR</code>, or <code>SCHED_DEADLINE</code> policy can potentially block all other threads from accessing the CPU forever. Prior to Linux 2.6.25, the only way of preventing a runaway real-time process from freezing the system was to run (at the console) a shell scheduled under a higher static priority than the tested application. This allows an emergency kill of tested real-time applications that do not block or terminate as expected. </p>
<p> Since Linux 2.6.25, there are other techniques for dealing with runaway real-time and deadline processes. One of these is to use the <code>RLIMIT_RTTIME</code> resource limit to set a ceiling on the CPU time that a real-time process may consume. See <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) for details. </p>
<p> Since version 2.6.25, Linux also provides two <i>/proc</i> files that can be used to reserve a certain amount of CPU time to be used by non-real-time processes. Reserving CPU time in this fashion allows some CPU time to be allocated to (say) a root shell that can be used to kill a runaway process. Both of these files specify time values in microseconds:</p>
<dl>
<dt><i>/proc/sys/kernel/sched_rt_period_us</i></p>
<dd>This file specifies a scheduling period that is equivalent to 100% CPU bandwidth. The value in this file can range from 1 to <code>INT_MAX</code>, giving an operating range of 1 microsecond to around 35 minutes. The default value in this file is 1,000,000 (1 second).</p>
<dt><i>/proc/sys/kernel/sched_rt_runtime_us</i></p>
<dd>The value in this file specifies how much of the &quot;period&quot; time can be used by all real-time and deadline scheduled processes on the system. The value in this file can range from -1 to <code>INT_MAX</code>-1. Specifying -1 makes the run time the same as the period; that is, no CPU time is set aside for non-real-time processes (which was the Linux behavior before kernel 2.6.25). The default value in this file is 950,000 (0.95 seconds), meaning that 5% of the CPU time is reserved for processes that don&#8217;t run under a real-time or deadline scheduling policy.</dl>
<h3>Response time</h3>
<p>A blocked high priority thread waiting for I/O has a certain response time before it is scheduled again. The device driver writer can greatly reduce this response time by using a &quot;slow interrupt&quot; interrupt handler.</p>
<h3>Miscellaneous</h3>
<p>Child processes inherit the scheduling policy and parameters across a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). The scheduling policy and parameters are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Memory locking is usually needed for real-time processes to avoid paging delays; this can be done with <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2) or <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2).</p>
<h3>The autogroup feature</h3>
<p>Since Linux 2.6.38, the kernel provides a feature known as autogrouping to improve interactive desktop performance in the face of multiprocess, CPU-intensive workloads such as building the Linux kernel with large numbers of parallel build processes (i.e., the <code><a href="/docs/linux/man/1-make/">make</a></code>(1) <code>-j</code> flag). </p>
<p> This feature operates in conjunction with the CFS scheduler and requires a kernel that is configured with <code>CONFIG_SCHED_AUTOGROUP</code>. On a running system, this feature is enabled or disabled via the file <i>/proc/sys/kernel/sched_autogroup_enabled</i>; a value of 0 disables the feature, while a value of 1 enables it. The default value in this file is 1, unless the kernel was booted with the <i>noautogroup</i> parameter. </p>
<p> A new autogroup is created when a new session is created via <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2); this happens, for example, when a new terminal window is started. A new process created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s autogroup membership. Thus, all of the processes in a session are members of the same autogroup. An autogroup is automatically destroyed when the last process in the group terminates. </p>
<p> When autogrouping is enabled, all of the members of an autogroup are placed in the same kernel scheduler &quot;task group&quot;. The CFS scheduler employs an algorithm that equalizes the distribution of CPU cycles across task groups. The benefits of this for interactive desktop performance can be described via the following example. </p>
<p> Suppose that there are two autogroups competing for the same CPU (i.e., presume either a single CPU system or the use of <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1) to confine all the processes to the same CPU on an SMP system). The first group contains ten CPU-bound processes from a kernel build started with <i>make -j10</i>. The other contains a single CPU-bound process: a video player. The effect of autogrouping is that the two groups will each receive half of the CPU cycles. That is, the video player will receive 50% of the CPU cycles, rather than just 9% of the cycles, which would likely lead to degraded video playback. The situation on an SMP system is more complex, but the general effect is the same: the scheduler distributes CPU cycles across task groups such that an autogroup that contains a large number of CPU-bound processes does not end up hogging CPU cycles at the expense of the other jobs on the system. </p>
<p> A process&#8217;s autogroup (task group) membership can be viewed via the file <i>/proc/[pid]/autogroup</i>: </p>
<p> $ <code>cat /proc/1/autogroup</code> /autogroup-1 nice 0 </p>
<p> This file can also be used to modify the CPU bandwidth allocated to an autogroup. This is done by writing a number in the &quot;nice&quot; range to the file to set the autogroup&#8217;s nice value. The allowed range is from +19 (low priority) to -20 (high priority). (Writing values outside of this range causes <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to fail with the error <code>EINVAL</code>.) </p>
<p> The autogroup nice setting has the same meaning as the process nice value, but applies to distribution of CPU cycles to the autogroup as a whole, based on the relative nice values of other autogroups. For a process inside an autogroup, the CPU cycles that it receives will be a product of the autogroup&#8217;s nice value (compared to other autogroups) and the process&#8217;s nice value (compared to other processes in the same autogroup. </p>
<p> The use of the <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7) CPU controller to place processes in cgroups other than the root CPU cgroup overrides the effect of autogrouping. </p>
<p> The autogroup feature groups only processes scheduled under non-real-time policies (<code>SCHED_OTHER</code>, <code>SCHED_BATCH</code>, and <code>SCHED_IDLE</code>). It does not group processes scheduled under real-time and deadline policies. Those processes are scheduled according to the rules described earlier.</p>
<h3>The nice value and group scheduling</h3>
<p>When scheduling non-real-time processes (i.e., those scheduled under the <code>SCHED_OTHER</code>, <code>SCHED_BATCH</code>, and <code>SCHED_IDLE</code> policies), the CFS scheduler employs a technique known as &quot;group scheduling&quot;, if the kernel was configured with the <code>CONFIG_FAIR_GROUP_SCHED</code> option (which is typical). </p>
<p> Under group scheduling, threads are scheduled in &quot;task groups&quot;. Task groups have a hierarchical relationship, rooted under the initial task group on the system, known as the &quot;root task group&quot;. Task groups are formed in the following circumstances:</p>
<dl>
<dt>*</p>
<dd>All of the threads in a CPU cgroup form a task group. The parent of this task group is the task group of the corresponding parent cgroup.</p>
<dt>*</p>
<dd>If autogrouping is enabled, then all of the threads that are (implicitly) placed in an autogroup (i.e., the same session, as created by <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2)) form a task group. Each new autogroup is thus a separate task group. The root task group is the parent of all such autogroups.</p>
<dt>*</p>
<dd>If autogrouping is enabled, then the root task group consists of all processes in the root CPU cgroup that were not otherwise implicitly placed into a new autogroup.</p>
<dt>*</p>
<dd>If autogrouping is disabled, then the root task group consists of all processes in the root CPU cgroup.</p>
<dt>*</p>
<dd>If group scheduling was disabled (i.e., the kernel was configured without <code>CONFIG_FAIR_GROUP_SCHED</code>), then all of the processes on the system are notionally placed in a single task group.</dl>
<p> Under group scheduling, a thread&#8217;s nice value has an effect for scheduling decisions <i>only relative to other threads in the same task group</i>. This has some surprising consequences in terms of the traditional semantics of the nice value on UNIX systems. In particular, if autogrouping is enabled (which is the default in various distributions), then employing <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2) or <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1) on a process has an effect only for scheduling relative to other processes executed in the same session (typically: the same terminal window). </p>
<p> Conversely, for two processes that are (for example) the sole CPU-bound processes in different sessions (e.g., different terminal windows, each of whose jobs are tied to different autogroups), <i>modifying the nice value of the process in one of the sessions</i> <i>has no effect</i> in terms of the scheduler&#8217;s decisions relative to the process in the other session. A possibly useful workaround here is to use a command such as the following to modify the autogroup nice value for <i>all</i> of the processes in a terminal session: </p>
<p> $ <code>echo 10 &gt; /proc/self/autogroup</code></p>
<h3>Real-time features in the mainline Linux kernel</h3>
<p>Since kernel version 2.6.18, Linux is gradually becoming equipped with real-time capabilities, most of which are derived from the former <i>realtime-preempt</i> patch set. Until the patches have been completely merged into the mainline kernel, they must be installed to achieve the best real-time performance. These patches are named: </p>
<p> patch-<i>kernelversion</i>-rt<i>patchversion</i> </p>
<p> and can be downloaded from </p>
<p> Without the patches and prior to their full inclusion into the mainline kernel, the kernel configuration offers only the three preemption classes <code>CONFIG_PREEMPT_NONE</code>, <code>CONFIG_PREEMPT_VOLUNTARY</code>, and <code>CONFIG_PREEMPT_DESKTOP</code> which respectively provide no, some, and considerable reduction of the worst-case scheduling latency. </p>
<p> With the patches applied or after their full inclusion into the mainline kernel, the additional configuration item <code>CONFIG_PREEMPT_RT</code> becomes available. If this is selected, Linux is transformed into a regular real-time operating system. The FIFO and RR scheduling policies are then used to run a thread with true real-time priority and a minimum worst-case scheduling latency.</p>
<h2>Notes</h2>
<p>The <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7) CPU controller can be used to limit the CPU consumption of groups of processes. </p>
<p> Originally, Standard Linux was intended as a general-purpose operating system being able to handle background processes, interactive applications, and less demanding real-time applications (applications that need to usually meet timing deadlines). Although the Linux kernel 2.6 allowed for kernel preemption and the newly introduced <a href="/docs/linux/man/1-o/">O</a>(1) scheduler ensures that the time needed to schedule is fixed and deterministic irrespective of the number of active tasks, true real-time computing was not possible up to kernel version 2.6.17.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chcpu/">chcpu</a></code>(1), <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1), <code><a href="/docs/linux/man/1-lscpu/">lscpu</a></code>(1), <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2), <code><a href="/docs/linux/man/2-munlock/">munlock</a></code>(2), <code><a href="/docs/linux/man/2-munlockall/">munlockall</a></code>(2), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/3-pthread_getaffinity_np/">pthread_getaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getschedparam/">pthread_getschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setaffinity_np/">pthread_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-sched_getcpu/">sched_getcpu</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7) </p>
<p> <i>Programming for the real world &#8211; POSIX.4</i> by Bill O. Gallmeister, O&#8217;Reilly &amp; Associates, Inc., ISBN 1-56592-074-0. </p>
<p> The Linux kernel source files <i>Documentation/scheduler/sched-deadline.txt</i>, <i>Documentation/scheduler/sched-rt-group.txt</i>, <i>Documentation/scheduler/sched-design-CFS.txt</i>, and <i>Documentation/scheduler/sched-nice-design.txt</i></p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
