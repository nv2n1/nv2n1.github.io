---
title: "ioprio_set(2)"
name: "ioprio_set"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioprio_set/"
description: "ioprio_get, ioprio_set – get/set I/O scheduling class and priority"
---

<h2 class="name">NAME</h2>
<p> ioprio_get, ioprio_set &#8211; get/set I/O scheduling class and priority </p>
<h2>SYNOPSIS</h2>
<pre><code>
int ioprio_get(int which, int who);
int ioprio_set(int which, int who, int ioprio);
</code></pre>
<p> <i>Note</i>: There are no glibc wrappers for these system calls; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>ioprio_get</code>() and <code>ioprio_set</code>() system calls get and set the I/O scheduling class and priority of one or more threads. </p>
<p> The <i>which</i> and <i>who</i> arguments identify the thread(s) on which the system calls operate. The <i>which</i> argument determines how <i>who</i> is interpreted, and has one of the following values:</p>
<dl>
<dt><code>IOPRIO_WHO_PROCESS</code></p>
<dd> <i>who</i> is a process ID or thread ID identifying a single process or thread. If <i>who</i> is 0, then operate on the calling thread.</p>
<dt><code>IOPRIO_WHO_PGRP</code></p>
<dd> <i>who</i> is a process group ID identifying all the members of a process group. If <i>who</i> is 0, then operate on the process group of which the caller is a member.</p>
<dt><code>IOPRIO_WHO_USER</code></p>
<dd> <i>who</i> is a user ID identifying all of the processes that have a matching real UID.</dl>
<p> If <i>which</i> is specified as <code>IOPRIO_WHO_PGRP</code> or <code>IOPRIO_WHO_USER</code> when calling <code>ioprio_get</code>(), and more than one process matches <i>who</i>, then the returned priority will be the highest one found among all of the matching processes. One priority is said to be higher than another one if it belongs to a higher priority class (<code>IOPRIO_CLASS_RT</code> is the highest priority class; <code>IOPRIO_CLASS_IDLE</code> is the lowest) or if it belongs to the same priority class as the other process but has a higher priority level (a lower priority number means a higher priority level). </p>
<p> The <i>ioprio</i> argument given to <code>ioprio_set</code>() is a bit mask that specifies both the scheduling class and the priority to be assigned to the target process(es). The following macros are used for assembling and dissecting <i>ioprio</i> values:</p>
<dl>
<dt><code>IOPRIO_PRIO_VALUE(</code><i>class</i><code>, </code><i>data</i><code>)</code></p>
<dd> Given a scheduling <i>class</i> and priority (<i>data</i>), this macro combines the two values to produce an <i>ioprio</i> value, which is returned as the result of the macro.</p>
<dt><code>IOPRIO_PRIO_CLASS(</code><i>mask</i><code>)</code></p>
<dd> Given <i>mask</i> (an <i>ioprio</i> value), this macro returns its I/O class component, that is, one of the values <code>IOPRIO_CLASS_RT</code>, <code>IOPRIO_CLASS_BE</code>, or <code>IOPRIO_CLASS_IDLE</code>.</p>
<dt><code>IOPRIO_PRIO_DATA(</code><i>mask</i><code>)</code></p>
<dd> Given <i>mask</i> (an <i>ioprio</i> value), this macro returns its priority (<i>data</i>) component.</dl>
<p> See the NOTES section for more information on scheduling classes and priorities, as well as the meaning of specifying <i>ioprio</i> as 0. </p>
<p> I/O priorities are supported for reads and for synchronous (<code>O_DIRECT</code>, <code>O_SYNC</code>) writes. I/O priorities are not supported for asynchronous writes because they are issued outside the context of the program dirtying the memory, and thus program-specific priorities do not apply.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>ioprio_get</code>() returns the <i>ioprio</i> value of the process with highest I/O priority of any of the processes that match the criteria specified in <i>which</i> and <i>who</i>. On error, -1 is returned, and <i>errno</i> is set to indicate the error. </p>
<p> On success, <code>ioprio_set</code>() returns 0. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> Invalid value for <i>which</i> or <i>ioprio</i>. Refer to the NOTES section for available scheduler classes and priority levels for <i>ioprio</i>.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have the privilege needed to assign this <i>ioprio</i> to the specified process(es). See the NOTES section for more information on required privileges for <code>ioprio_set</code>().</p>
<dt><code>ESRCH</code></p>
<dd> No process(es) could be found that matched the specification in <i>which</i> and <i>who</i>.</dl>
<h2>VERSIONS</h2>
<p> These system calls have been available on Linux since kernel 2.6.13.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for these system calls; call them using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Two or more processes or threads can share an I/O context. This will be the case when <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) was called with the <code>CLONE_IO</code> flag. However, by default, the distinct threads of a process will <code>not</code> share the same I/O context. This means that if you want to change the I/O priority of all threads in a process, you may need to call <code>ioprio_set</code>() on each of the threads. The thread ID that you would need for this operation is the one that is returned by <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) or <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). </p>
<p> These system calls have an effect only when used in conjunction with an I/O scheduler that supports I/O priorities. As at kernel 2.6.17 the only such scheduler is the Completely Fair Queuing (CFQ) I/O scheduler. </p>
<p> If no I/O scheduler has been set for a thread, then by default the I/O priority will follow the CPU nice value (<code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2)). In Linux kernels before version 2.6.24, once an I/O priority had been set using <code>ioprio_set</code>(), there was no way to reset the I/O scheduling behavior to the default. Since Linux 2.6.24, specifying <i>ioprio</i> as 0 can be used to reset to the default I/O scheduling behavior.</p>
<h3>Selecting an I/O scheduler</h3>
<p> I/O schedulers are selected on a per-device basis via the special file <i>/sys/block/&lt;device&gt;/queue/scheduler</i>. </p>
<p> One can view the current I/O scheduler via the <i>/sys</i> filesystem. For example, the following command displays a list of all schedulers currently loaded in the kernel: </p>
<p> $<code> cat /sys/block/sda/queue/scheduler</code> noop anticipatory deadline [cfq] </p>
<p> The scheduler surrounded by brackets is the one actually in use for the device (<i>sda</i> in the example). Setting another scheduler is done by writing the name of the new scheduler to this file. For example, the following command will set the scheduler for the <i>sda</i> device to <i>cfq</i>: </p>
<p> $<code> su</code> Password: #<code> echo cfq &gt; /sys/block/sda/queue/scheduler</code></p>
<h3>The Completely Fair Queuing (CFQ) I/O scheduler</h3>
<p> Since version 3 (also known as CFQ Time Sliced), CFQ implements I/O nice levels similar to those of CPU scheduling. These nice levels are grouped into three scheduling classes, each one containing one or more priority levels:</p>
<dl>
<dt><code>IOPRIO_CLASS_RT</code> (1)</p>
<dd> This is the real-time I/O class. This scheduling class is given higher priority than any other class: processes from this class are given first access to the disk every time. Thus, this I/O class needs to be used with some care: one I/O real-time process can starve the entire system. Within the real-time class, there are 8 levels of class data (priority) that determine exactly how much time this process needs the disk for on each service. The highest real-time priority level is 0; the lowest is 7. In the future, this might change to be more directly mappable to performance, by passing in a desired data rate instead.</p>
<dt><code>IOPRIO_CLASS_BE</code> (2)</p>
<dd> This is the best-effort scheduling class, which is the default for any process that hasn&#8217;t set a specific I/O priority. The class data (priority) determines how much I/O bandwidth the process will get. Best-effort priority levels are analogous to CPU nice values (see <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2)). The priority level determines a priority relative to other processes in the best-effort scheduling class. Priority levels range from 0 (highest) to 7 (lowest).</p>
<dt><code>IOPRIO_CLASS_IDLE</code> (3)</p>
<dd> This is the idle scheduling class. Processes running at this level get I/O time only when no one else needs the disk. The idle class has no class data. Attention is required when assigning this priority class to a process, since it may become starved if higher priority processes are constantly accessing the disk.</dl>
<p> Refer to the kernel source file <i>Documentation/block/ioprio.txt</i> for more information on the CFQ I/O Scheduler and an example program.</p>
<h3>Required permissions to set I/O priorities</h3>
<p> Permission to change a process&#8217;s priority is granted or denied based on two criteria:</p>
<dl>
<dt><code>Process ownership</code></p>
<dd> An unprivileged process may set the I/O priority only for a process whose real UID matches the real or effective UID of the calling process. A process which has the <code>CAP_SYS_NICE</code> capability can change the priority of any process.</p>
<dt><code>What is the desired priority</code></p>
<dd> Attempts to set very high priorities (<code>IOPRIO_CLASS_RT</code>) require the <code>CAP_SYS_ADMIN</code> capability. Kernel versions up to 2.6.24 also required <code>CAP_SYS_ADMIN</code> to set a very low priority (<code>IOPRIO_CLASS_IDLE</code>), but since Linux 2.6.25, this is no longer required.</dl>
<p> A call to <code>ioprio_set</code>() must follow both rules, or the call will fail with the error <code>EPERM</code>.</p>
<h2>BUGS</h2>
<p> Glibc does not yet provide a suitable header file defining the function prototypes and macros described on this page. Suitable definitions can be found in <i>linux/ioprio.h</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ionice/">ionice</a></code>(1), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7) </p>
<p> <i>Documentation/block/ioprio.txt</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
