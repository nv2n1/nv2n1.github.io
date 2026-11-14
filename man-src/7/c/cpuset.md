---
title: "cpuset(7)"
name: "cpuset"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cpuset/"
description: "cpuset – confine processes to processor and memory node subsets"
---

<p>cpuset &#8211; confine processes to processor and memory node subsets</p>
<h2>Description</h2>
<p>The cpuset filesystem is a pseudo-filesystem interface to the kernel cpuset mechanism, which is used to control the processor placement and memory placement of processes. It is commonly mounted at <i>/dev/cpuset</i>. </p>
<p> On systems with kernels compiled with built in support for cpusets, all processes are attached to a cpuset, and cpusets are always present. If a system supports cpusets, then it will have the entry <code>nodev cpuset</code> in the file <i>/proc/filesystems</i>. By mounting the cpuset filesystem (see the <code>EXAMPLES</code> section below), the administrator can configure the cpusets on a system to control the processor and memory placement of processes on that system. By default, if the cpuset configuration on a system is not modified or if the cpuset filesystem is not even mounted, then the cpuset mechanism, though present, has no effect on the system&#8217;s behavior. </p>
<p> A cpuset defines a list of CPUs and memory nodes. </p>
<p> The CPUs of a system include all the logical processing units on which a process can execute, including, if present, multiple processor cores within a package and Hyper-Threads within a processor core. Memory nodes include all distinct banks of main memory; small and SMP systems typically have just one memory node that contains all the system&#8217;s main memory, while NUMA (non-uniform memory access) systems have multiple memory nodes. </p>
<p> Cpusets are represented as directories in a hierarchical pseudo-filesystem, where the top directory in the hierarchy (<i>/dev/cpuset</i>) represents the entire system (all online CPUs and memory nodes) and any cpuset that is the child (descendant) of another parent cpuset contains a subset of that parent&#8217;s CPUs and memory nodes. The directories and files representing cpusets have normal filesystem permissions. </p>
<p> Every process in the system belongs to exactly one cpuset. A process is confined to run only on the CPUs in the cpuset it belongs to, and to allocate memory only on the memory nodes in that cpuset. When a process <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)s, the child process is placed in the same cpuset as its parent. With sufficient privilege, a process may be moved from one cpuset to another and the allowed CPUs and memory nodes of an existing cpuset may be changed. </p>
<p> When the system begins booting, a single cpuset is defined that includes all CPUs and memory nodes on the system, and all processes are in that cpuset. During the boot process, or later during normal system operation, other cpusets may be created, as subdirectories of this top cpuset, under the control of the system administrator, and processes may be placed in these other cpusets. </p>
<p> Cpusets are integrated with the <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) scheduling affinity mechanism and the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) and <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2) memory-placement mechanisms in the kernel. Neither of these mechanisms let a process make use of a CPU or memory node that is not allowed by that process&#8217;s cpuset. If changes to a process&#8217;s cpuset placement conflict with these other mechanisms, then cpuset placement is enforced even if it means overriding these other mechanisms. The kernel accomplishes this overriding by silently restricting the CPUs and memory nodes requested by these other mechanisms to those allowed by the invoking process&#8217;s cpuset. This can result in these other calls returning an error, if for example, such a call ends up requesting an empty set of CPUs or memory nodes, after that request is restricted to the invoking process&#8217;s cpuset. </p>
<p> Typically, a cpuset is used to manage the CPU and memory-node confinement for a set of cooperating processes such as a batch scheduler job, and these other mechanisms are used to manage the placement of individual processes or memory regions within that set or job.</p>
<h2>Files</h2>
<p>Each directory below <i>/dev/cpuset</i> represents a cpuset and contains a fixed set of pseudo-files describing the state of that cpuset. </p>
<p> New cpusets are created using the <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) system call or the <code><a href="/docs/linux/man/1-mkdir/">mkdir</a></code>(1) command. The properties of a cpuset, such as its flags, allowed CPUs and memory nodes, and attached processes, are queried and modified by reading or writing to the appropriate file in that cpuset&#8217;s directory, as listed below. </p>
<p> The pseudo-files in each cpuset directory are automatically created when the cpuset is created, as a result of the <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) invocation. It is not possible to directly add or remove these pseudo-files. </p>
<p> A cpuset directory that contains no child cpuset directories, and has no attached processes, can be removed using <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) or <code><a href="/docs/linux/man/1-rmdir/">rmdir</a></code>(1). It is not necessary, or possible, to remove the pseudo-files inside the directory before removing it. </p>
<p> The pseudo-files in each cpuset directory are small text files that may be read and written using traditional shell utilities such as <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), and <code><a href="/docs/linux/man/1-echo/">echo</a></code>(1), or from a program by using file I/O library functions or system calls, such as <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), and <code><a href="/docs/linux/man/2-close/">close</a></code>(2). </p>
<p> The pseudo-files in a cpuset directory represent internal kernel state and do not have any persistent image on disk. Each of these per-cpuset files is listed and described below.</p>
<dl>
<dt><i>tasks</i></p>
<dd>List of the process IDs (PIDs) of the processes in that cpuset. The list is formatted as a series of ASCII decimal numbers, each followed by a newline. A process may be added to a cpuset (automatically removing it from the cpuset that previously contained it) by writing its PID to that cpuset&#8217;s <i>tasks</i> file (with or without a trailing newline).</p>
<dd><code>Warning:</code> only one PID may be written to the <i>tasks</i> file at a time. If a string is written that contains more than one PID, only the first one will be used.</p>
<dt><i>notify_on_release</i></p>
<dd>Flag (0 or 1). If set (1), that cpuset will receive special handling after it is released, that is, after all processes cease using it (i.e., terminate or are moved to a different cpuset) and all child cpuset directories have been removed. See the <code>Notify On Release</code> section, below.</p>
<dt><i>cpuset.cpus</i></p>
<dd>List of the physical numbers of the CPUs on which processes in that cpuset are allowed to execute. See <code>List Format</code> below for a description of the format of <i>cpus</i>.</p>
<dd>The CPUs allowed to a cpuset may be changed by writing a new list to its <i>cpus</i> file.</p>
<dt><i>cpuset.cpu_exclusive</i></p>
<dd>Flag (0 or 1). If set (1), the cpuset has exclusive use of its CPUs (no sibling or cousin cpuset may overlap CPUs). By default, this is off (0). Newly created cpusets also initially default this to off (0).</p>
<dd>Two cpusets are <i>sibling</i> cpusets if they share the same parent cpuset in the <i>/dev/cpuset</i> hierarchy. Two cpusets are <i>cousin</i> cpusets if neither is the ancestor of the other. Regardless of the <i>cpu_exclusive</i> setting, if one cpuset is the ancestor of another, and if both of these cpusets have nonempty <i>cpus</i>, then their <i>cpus</i> must overlap, because the <i>cpus</i> of any cpuset are always a subset of the <i>cpus</i> of its parent cpuset.</p>
<dt><i>cpuset.mems</i></p>
<dd>List of memory nodes on which processes in this cpuset are allowed to allocate memory. See <code>List Format</code> below for a description of the format of <i>mems</i>.</p>
<dt><i>cpuset.mem_exclusive</i></p>
<dd>Flag (0 or 1). If set (1), the cpuset has exclusive use of its memory nodes (no sibling or cousin may overlap). Also if set (1), the cpuset is a <code>Hardwall</code> cpuset (see below). By default, this is off (0). Newly created cpusets also initially default this to off (0).</p>
<dd>Regardless of the <i>mem_exclusive</i> setting, if one cpuset is the ancestor of another, then their memory nodes must overlap, because the memory nodes of any cpuset are always a subset of the memory nodes of that cpuset&#8217;s parent cpuset.</p>
<dt><i>cpuset.mem_hardwall</i> (since Linux 2.6.26)</p>
<dd>Flag (0 or 1). If set (1), the cpuset is a <code>Hardwall</code> cpuset (see below). Unlike <code>mem_exclusive</code>, there is no constraint on whether cpusets marked <code>mem_hardwall</code> may have overlapping memory nodes with sibling or cousin cpusets. By default, this is off (0). Newly created cpusets also initially default this to off (0).</p>
<dt><i>cpuset.memory_migrate</i> (since Linux 2.6.16)</p>
<dd>Flag (0 or 1). If set (1), then memory migration is enabled. By default, this is off (0). See the <code>Memory Migration</code> section, below.</p>
<dt><i>cpuset.memory_pressure</i> (since Linux 2.6.16)</p>
<dd>A measure of how much memory pressure the processes in this cpuset are causing. See the <code>Memory Pressure</code> section, below. Unless <i>memory_pressure_enabled</i> is enabled, always has value zero (0). This file is read-only. See the <code>WARNINGS</code> section, below.</p>
<dt><i>cpuset.memory_pressure_enabled</i> (since Linux 2.6.16)</p>
<dd>Flag (0 or 1). This file is present only in the root cpuset, normally <i>/dev/cpuset</i>. If set (1), the <i>memory_pressure</i> calculations are enabled for all cpusets in the system. By default, this is off (0). See the <code>Memory Pressure</code> section, below.</p>
<dt><i>cpuset.memory_spread_page</i> (since Linux 2.6.17)</p>
<dd>Flag (0 or 1). If set (1), pages in the kernel page cache (filesystem buffers) are uniformly spread across the cpuset. By default, this is off (0) in the top cpuset, and inherited from the parent cpuset in newly created cpusets. See the <code>Memory Spread</code> section, below.</p>
<dt><i>cpuset.memory_spread_slab</i> (since Linux 2.6.17)</p>
<dd>Flag (0 or 1). If set (1), the kernel slab caches for file I/O (directory and inode structures) are uniformly spread across the cpuset. By default, is off (0) in the top cpuset, and inherited from the parent cpuset in newly created cpusets. See the <code>Memory Spread</code> section, below.</p>
<dt><i>cpuset.sched_load_balance</i> (since Linux 2.6.24)</p>
<dd>Flag (0 or 1). If set (1, the default) the kernel will automatically load balance processes in that cpuset over the allowed CPUs in that cpuset. If cleared (0) the kernel will avoid load balancing processes in this cpuset, <i>unless</i> some other cpuset with overlapping CPUs has its <i>sched_load_balance</i> flag set. See <code>Scheduler Load Balancing</code>, below, for further details.</p>
<dt><i>cpuset.sched_relax_domain_level</i> (since Linux 2.6.26)</p>
<dd>Integer, between -1 and a small positive value. The <i>sched_relax_domain_level</i> controls the width of the range of CPUs over which the kernel scheduler performs immediate rebalancing of runnable tasks across CPUs. If <i>sched_load_balance</i> is disabled, then the setting of <i>sched_relax_domain_level</i> does not matter, as no such load balancing is done. If <i>sched_load_balance</i> is enabled, then the higher the value of the <i>sched_relax_domain_level</i>, the wider the range of CPUs over which immediate load balancing is attempted. See <code>Scheduler Relax Domain Level</code>, below, for further details.</dl>
<p> In addition to the above pseudo-files in each directory below <i>/dev/cpuset</i>, each process has a pseudo-file, <i>/proc/&lt;pid&gt;/cpuset</i>, that displays the path of the process&#8217;s cpuset directory relative to the root of the cpuset filesystem. </p>
<p> Also the <i>/proc/&lt;pid&gt;/status</i> file for each process has four added lines, displaying the process&#8217;s <i>Cpus_allowed</i> (on which CPUs it may be scheduled) and <i>Mems_allowed</i> (on which memory nodes it may obtain memory), in the two formats <code>Mask Format</code> and <code>List Format</code> (see below) as shown in the following example: </p>
<p> Cpus_allowed: ffffffff,ffffffff,ffffffff,ffffffff Cpus_allowed_list: 0-127 Mems_allowed: ffffffff,ffffffff Mems_allowed_list: 0-63 </p>
<p> The &quot;allowed&quot; fields were added in Linux 2.6.24; the &quot;allowed_list&quot; fields were added in Linux 2.6.26.</p>
<h2>Extended Capabilities</h2>
<p>In addition to controlling which <i>cpus</i> and <i>mems</i> a process is allowed to use, cpusets provide the following extended capabilities.</p>
<h3>Exclusive cpusets</h3>
<p>If a cpuset is marked <i>cpu_exclusive</i> or <i>mem_exclusive</i>, no other cpuset, other than a direct ancestor or descendant, may share any of the same CPUs or memory nodes. </p>
<p> A cpuset that is <i>mem_exclusive</i> restricts kernel allocations for buffer cache pages and other internal kernel data pages commonly shared by the kernel across multiple users. All cpusets, whether <i>mem_exclusive</i> or not, restrict allocations of memory for user space. This enables configuring a system so that several independent jobs can share common kernel data, while isolating each job&#8217;s user allocation in its own cpuset. To do this, construct a large <i>mem_exclusive</i> cpuset to hold all the jobs, and construct child, non-<i>mem_exclusive</i> cpusets for each individual job. Only a small amount of kernel memory, such as requests from interrupt handlers, is allowed to be placed on memory nodes outside even a <i>mem_exclusive</i> cpuset.</p>
<h3>Hardwall</h3>
<p>A cpuset that has <i>mem_exclusive</i> or <i>mem_hardwall</i> set is a <i>hardwall</i> cpuset. A <i>hardwall</i> cpuset restricts kernel allocations for page, buffer, and other data commonly shared by the kernel across multiple users. All cpusets, whether <i>hardwall</i> or not, restrict allocations of memory for user space. </p>
<p> This enables configuring a system so that several independent jobs can share common kernel data, such as filesystem pages, while isolating each job&#8217;s user allocation in its own cpuset. To do this, construct a large <i>hardwall</i> cpuset to hold all the jobs, and construct child cpusets for each individual job which are not <i>hardwall</i> cpusets. </p>
<p> Only a small amount of kernel memory, such as requests from interrupt handlers, is allowed to be taken outside even a <i>hardwall</i> cpuset.</p>
<h3>Notify on release</h3>
<p>If the <i>notify_on_release</i> flag is enabled (1) in a cpuset, then whenever the last process in the cpuset leaves (exits or attaches to some other cpuset) and the last child cpuset of that cpuset is removed, the kernel will run the command <i>/sbin/cpuset_release_agent</i>, supplying the pathname (relative to the mount point of the cpuset filesystem) of the abandoned cpuset. This enables automatic removal of abandoned cpusets. </p>
<p> The default value of <i>notify_on_release</i> in the root cpuset at system boot is disabled (0). The default value of other cpusets at creation is the current value of their parent&#8217;s <i>notify_on_release</i> setting. </p>
<p> The command <i>/sbin/cpuset_release_agent</i> is invoked, with the name (<i>/dev/cpuset</i> relative path) of the to-be-released cpuset in <i>argv[1]</i>. </p>
<p> The usual contents of the command <i>/sbin/cpuset_release_agent</i> is simply the shell script: </p>
<p> #!/bin/sh rmdir /dev/cpuset/$1 </p>
<p> As with other flag values below, this flag can be changed by writing an ASCII number 0 or 1 (with optional trailing newline) into the file, to clear or set the flag, respectively.</p>
<h3>Memory pressure</h3>
<p>The <i>memory_pressure</i> of a cpuset provides a simple per-cpuset running average of the rate that the processes in a cpuset are attempting to free up in-use memory on the nodes of the cpuset to satisfy additional memory requests. </p>
<p> This enables batch managers that are monitoring jobs running in dedicated cpusets to efficiently detect what level of memory pressure that job is causing. </p>
<p> This is useful both on tightly managed systems running a wide mix of submitted jobs, which may choose to terminate or reprioritize jobs that are trying to use more memory than allowed on the nodes assigned them, and with tightly coupled, long-running, massively parallel scientific computing jobs that will dramatically fail to meet required performance goals if they start to use more memory than allowed to them. </p>
<p> This mechanism provides a very economical way for the batch manager to monitor a cpuset for signs of memory pressure. It&#8217;s up to the batch manager or other user code to decide what action to take if it detects signs of memory pressure. </p>
<p> Unless memory pressure calculation is enabled by setting the pseudo-file <i>/dev/cpuset/cpuset.memory_pressure_enabled</i>, it is not computed for any cpuset, and reads from any <i>memory_pressure</i> always return zero, as represented by the ASCII string &quot;0
&quot;. See the <code>WARNINGS</code> section, below. </p>
<p> A per-cpuset, running average is employed for the following reasons:</p>
<dl>
<dt>*</p>
<dd>Because this meter is per-cpuset rather than per-process or per virtual memory region, the system load imposed by a batch scheduler monitoring this metric is sharply reduced on large systems, because a scan of the tasklist can be avoided on each set of queries.</p>
<dt>*</p>
<dd>Because this meter is a running average rather than an accumulating counter, a batch scheduler can detect memory pressure with a single read, instead of having to read and accumulate results for a period of time.</p>
<dt>*</p>
<dd>Because this meter is per-cpuset rather than per-process, the batch scheduler can obtain the key information&#8212;memory pressure in a cpuset&#8212;with a single read, rather than having to query and accumulate results over all the (dynamically changing) set of processes in the cpuset.</dl>
<p> The <i>memory_pressure</i> of a cpuset is calculated using a per-cpuset simple digital filter that is kept within the kernel. For each cpuset, this filter tracks the recent rate at which processes attached to that cpuset enter the kernel direct reclaim code. </p>
<p> The kernel direct reclaim code is entered whenever a process has to satisfy a memory page request by first finding some other page to repurpose, due to lack of any readily available already free pages. Dirty filesystem pages are repurposed by first writing them to disk. Unmodified filesystem buffer pages are repurposed by simply dropping them, though if that page is needed again, it will have to be reread from disk. </p>
<p> The <i>cpuset.memory_pressure</i> file provides an integer number representing the recent (half-life of 10 seconds) rate of entries to the direct reclaim code caused by any process in the cpuset, in units of reclaims attempted per second, times 1000.</p>
<h3>Memory spread</h3>
<p>There are two Boolean flag files per cpuset that control where the kernel allocates pages for the filesystem buffers and related in-kernel data structures. They are called <i>cpuset.memory_spread_page</i> and <i>cpuset.memory_spread_slab</i>. </p>
<p> If the per-cpuset Boolean flag file <i>cpuset.memory_spread_page</i> is set, then the kernel will spread the filesystem buffers (page cache) evenly over all the nodes that the faulting process is allowed to use, instead of preferring to put those pages on the node where the process is running. </p>
<p> If the per-cpuset Boolean flag file <i>cpuset.memory_spread_slab</i> is set, then the kernel will spread some filesystem-related slab caches, such as those for inodes and directory entries, evenly over all the nodes that the faulting process is allowed to use, instead of preferring to put those pages on the node where the process is running. </p>
<p> The setting of these flags does not affect the data segment (see <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2)) or stack segment pages of a process. </p>
<p> By default, both kinds of memory spreading are off and the kernel prefers to allocate memory pages on the node local to where the requesting process is running. If that node is not allowed by the process&#8217;s NUMA memory policy or cpuset configuration or if there are insufficient free memory pages on that node, then the kernel looks for the nearest node that is allowed and has sufficient free memory. </p>
<p> When new cpusets are created, they inherit the memory spread settings of their parent. </p>
<p> Setting memory spreading causes allocations for the affected page or slab caches to ignore the process&#8217;s NUMA memory policy and be spread instead. However, the effect of these changes in memory placement caused by cpuset-specified memory spreading is hidden from the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) or <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2) calls. These two NUMA memory policy calls always appear to behave as if no cpuset-specified memory spreading is in effect, even if it is. If cpuset memory spreading is subsequently turned off, the NUMA memory policy most recently specified by these calls is automatically reapplied. </p>
<p> Both <i>cpuset.memory_spread_page</i> and <i>cpuset.memory_spread_slab</i> are Boolean flag files. By default, they contain &quot;0&quot;, meaning that the feature is off for that cpuset. If a &quot;1&quot; is written to that file, that turns the named feature on. </p>
<p> Cpuset-specified memory spreading behaves similarly to what is known (in other contexts) as round-robin or interleave memory placement. </p>
<p> Cpuset-specified memory spreading can provide substantial performance improvements for jobs that:</p>
<dl>
<dt>a)</p>
<dd>need to place thread-local data on memory nodes close to the CPUs which are running the threads that most frequently access that data; but also</p>
<dt>b)</p>
<dd>need to access large filesystem data sets that must to be spread across the several nodes in the job&#8217;s cpuset in order to fit.</dl>
<p> Without this policy, the memory allocation across the nodes in the job&#8217;s cpuset can become very uneven, especially for jobs that might have just a single thread initializing or reading in the data set.</p>
<h3>Memory migration</h3>
<p>Normally, under the default setting (disabled) of <i>cpuset.memory_migrate</i>, once a page is allocated (given a physical page of main memory), then that page stays on whatever node it was allocated, so long as it remains allocated, even if the cpuset&#8217;s memory-placement policy <i>mems</i> subsequently changes. </p>
<p> When memory migration is enabled in a cpuset, if the <i>mems</i> setting of the cpuset is changed, then any memory page in use by any process in the cpuset that is on a memory node that is no longer allowed will be migrated to a memory node that is allowed. </p>
<p> Furthermore, if a process is moved into a cpuset with <i>memory_migrate</i> enabled, any memory pages it uses that were on memory nodes allowed in its previous cpuset, but which are not allowed in its new cpuset, will be migrated to a memory node allowed in the new cpuset. </p>
<p> The relative placement of a migrated page within the cpuset is preserved during these migration operations if possible. For example, if the page was on the second valid node of the prior cpuset, then the page will be placed on the second valid node of the new cpuset, if possible.</p>
<h3>Scheduler load balancing</h3>
<p>The kernel scheduler automatically load balances processes. If one CPU is underutilized, the kernel will look for processes on other more overloaded CPUs and move those processes to the underutilized CPU, within the constraints of such placement mechanisms as cpusets and <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2). </p>
<p> The algorithmic cost of load balancing and its impact on key shared kernel data structures such as the process list increases more than linearly with the number of CPUs being balanced. For example, it costs more to load balance across one large set of CPUs than it does to balance across two smaller sets of CPUs, each of half the size of the larger set. (The precise relationship between the number of CPUs being balanced and the cost of load balancing depends on implementation details of the kernel process scheduler, which is subject to change over time, as improved kernel scheduler algorithms are implemented.) </p>
<p> The per-cpuset flag <i>sched_load_balance</i> provides a mechanism to suppress this automatic scheduler load balancing in cases where it is not needed and suppressing it would have worthwhile performance benefits. </p>
<p> By default, load balancing is done across all CPUs, except those marked isolated using the kernel boot time &quot;isolcpus=&quot; argument. (See <code>Scheduler Relax Domain Level</code>, below, to change this default.) </p>
<p> This default load balancing across all CPUs is not well suited to the following two situations:</p>
<dl>
<dt>*</p>
<dd>On large systems, load balancing across many CPUs is expensive. If the system is managed using cpusets to place independent jobs on separate sets of CPUs, full load balancing is unnecessary.</p>
<dt>*</p>
<dd>Systems supporting real-time on some CPUs need to minimize system overhead on those CPUs, including avoiding process load balancing if that is not needed.</dl>
<p> When the per-cpuset flag <i>sched_load_balance</i> is enabled (the default setting), it requests load balancing across all the CPUs in that cpuset&#8217;s allowed CPUs, ensuring that load balancing can move a process (not otherwise pinned, as by <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)) from any CPU in that cpuset to any other. </p>
<p> When the per-cpuset flag <i>sched_load_balance</i> is disabled, then the scheduler will avoid load balancing across the CPUs in that cpuset, <i>except</i> in so far as is necessary because some overlapping cpuset has <i>sched_load_balance</i> enabled. </p>
<p> So, for example, if the top cpuset has the flag <i>sched_load_balance</i> enabled, then the scheduler will load balance across all CPUs, and the setting of the <i>sched_load_balance</i> flag in other cpusets has no effect, as we&#8217;re already fully load balancing. </p>
<p> Therefore in the above two situations, the flag <i>sched_load_balance</i> should be disabled in the top cpuset, and only some of the smaller, child cpusets would have this flag enabled. </p>
<p> When doing this, you don&#8217;t usually want to leave any unpinned processes in the top cpuset that might use nontrivial amounts of CPU, as such processes may be artificially constrained to some subset of CPUs, depending on the particulars of this flag setting in descendant cpusets. Even if such a process could use spare CPU cycles in some other CPUs, the kernel scheduler might not consider the possibility of load balancing that process to the underused CPU. </p>
<p> Of course, processes pinned to a particular CPU can be left in a cpuset that disables <i>sched_load_balance</i> as those processes aren&#8217;t going anywhere else anyway.</p>
<h3>Scheduler relax domain level</h3>
<p>The kernel scheduler performs immediate load balancing whenever a CPU becomes free or another task becomes runnable. This load balancing works to ensure that as many CPUs as possible are usefully employed running tasks. The kernel also performs periodic load balancing off the software clock described in <code><a href="/docs/linux/man/7-time/">time</a></code>(7). The setting of <i>sched_relax_domain_level</i> applies only to immediate load balancing. Regardless of the <i>sched_relax_domain_level</i> setting, periodic load balancing is attempted over all CPUs (unless disabled by turning off <i>sched_load_balance</i>.) In any case, of course, tasks will be scheduled to run only on CPUs allowed by their cpuset, as modified by <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2) system calls. </p>
<p> On small systems, such as those with just a few CPUs, immediate load balancing is useful to improve system interactivity and to minimize wasteful idle CPU cycles. But on large systems, attempting immediate load balancing across a large number of CPUs can be more costly than it is worth, depending on the particular performance characteristics of the job mix and the hardware. </p>
<p> The exact meaning of the small integer values of <i>sched_relax_domain_level</i> will depend on internal implementation details of the kernel scheduler code and on the non-uniform architecture of the hardware. Both of these will evolve over time and vary by system architecture and kernel version. </p>
<p> As of this writing, when this capability was introduced in Linux 2.6.26, on certain popular architectures, the positive values of <i>sched_relax_domain_level</i> have the following meanings. </p>
<dl>
<dt><code>(1)</code></p>
<dd>Perform immediate load balancing across Hyper-Thread siblings on the same core.</p>
<dt><code>(2)</code></p>
<dd>Perform immediate load balancing across other cores in the same package.</p>
<dt><code>(3)</code></p>
<dd>Perform immediate load balancing across other CPUs on the same node or blade.</p>
<dt><code>(4)</code></p>
<dd>Perform immediate load balancing across over several (implementation detail) nodes [On NUMA systems].</p>
<dt><code>(5)</code></p>
<dd>Perform immediate load balancing across over all CPUs in system [On NUMA systems].</dl>
<p> The <i>sched_relax_domain_level</i> value of zero (0) always means don&#8217;t perform immediate load balancing, hence that load balancing is done only periodically, not immediately when a CPU becomes available or another task becomes runnable. </p>
<p> The <i>sched_relax_domain_level</i> value of minus one (-1) always means use the system default value. The system default value can vary by architecture and kernel version. This system default value can be changed by kernel boot-time &quot;relax_domain_level=&quot; argument. </p>
<p> In the case of multiple overlapping cpusets which have conflicting <i>sched_relax_domain_level</i> values, then the highest such value applies to all CPUs in any of the overlapping cpusets. In such cases, the value <code>minus one (-1)</code> is the lowest value, overridden by any other value, and the value <code>zero (0)</code> is the next lowest value.</p>
<h2>Formats</h2>
<p>The following formats are used to represent sets of CPUs and memory nodes.</p>
<h3>Mask format</h3>
<p>The <code>Mask Format</code> is used to represent CPU and memory-node bit masks in the <i>/proc/&lt;pid&gt;/status</i> file. </p>
<p> This format displays each 32-bit word in hexadecimal (using ASCII characters &quot;0&quot; &#8211; &quot;9&quot; and &quot;a&quot; &#8211; &quot;f&quot;); words are filled with leading zeros, if required. For masks longer than one word, a comma separator is used between words. Words are displayed in big-endian order, which has the most significant bit first. The hex digits within a word are also in big-endian order. </p>
<p> The number of 32-bit words displayed is the minimum number needed to display all bits of the bit mask, based on the size of the bit mask. </p>
<p> Examples of the <code>Mask Format</code>: </p>
<p> 00000001 # just bit 0 set 40000000,00000000,00000000 # just bit 94 set 00000001,00000000,00000000 # just bit 64 set 000000ff,00000000 # bits 32-39 set 00000000,000e3862 # 1,5,6,11-13,17-19 set </p>
<p> A mask with bits 0, 1, 2, 4, 8, 16, 32, and 64 set displays as: </p>
<p> 00000001,00000001,00010117 </p>
<p> The first &quot;1&quot; is for bit 64, the second for bit 32, the third for bit 16, the fourth for bit 8, the fifth for bit 4, and the &quot;7&quot; is for bits 2, 1, and 0.</p>
<h3>List format</h3>
<p>The <code>List Format</code> for <i>cpus</i> and <i>mems</i> is a comma-separated list of CPU or memory-node numbers and ranges of numbers, in ASCII decimal. </p>
<p> Examples of the <code>List Format</code>: </p>
<p> 0-4,9 # bits 0, 1, 2, 3, 4, and 9 set 0-2,7,12-14 # bits 0, 1, 2, 7, 12, 13, and 14 set</p>
<h2>Rules</h2>
<p>The following rules apply to each cpuset:</p>
<dl>
<dt>*</p>
<dd>Its CPUs and memory nodes must be a (possibly equal) subset of its parent&#8217;s.</p>
<dt>*</p>
<dd>It can be marked <i>cpu_exclusive</i> only if its parent is.</p>
<dt>*</p>
<dd>It can be marked <i>mem_exclusive</i> only if its parent is.</p>
<dt>*</p>
<dd>If it is <i>cpu_exclusive</i>, its CPUs may not overlap any sibling.</p>
<dt>*</p>
<dd>If it is <i>memory_exclusive</i>, its memory nodes may not overlap any sibling.</dl>
<h2>Permissions</h2>
<p>The permissions of a cpuset are determined by the permissions of the directories and pseudo-files in the cpuset filesystem, normally mounted at <i>/dev/cpuset</i>. </p>
<p> For instance, a process can put itself in some other cpuset (than its current one) if it can write the <i>tasks</i> file for that cpuset. This requires execute permission on the encompassing directories and write permission on the <i>tasks</i> file. </p>
<p> An additional constraint is applied to requests to place some other process in a cpuset. One process may not attach another to a cpuset unless it would have permission to send that process a signal (see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)). </p>
<p> A process may create a child cpuset if it can access and write the parent cpuset directory. It can modify the CPUs or memory nodes in a cpuset if it can access that cpuset&#8217;s directory (execute permissions on the each of the parent directories) and write the corresponding <i>cpus</i> or <i>mems</i> file. </p>
<p> There is one minor difference between the manner in which these permissions are evaluated and the manner in which normal filesystem operation permissions are evaluated. The kernel interprets relative pathnames starting at a process&#8217;s current working directory. Even if one is operating on a cpuset file, relative pathnames are interpreted relative to the process&#8217;s current working directory, not relative to the process&#8217;s current cpuset. The only ways that cpuset paths relative to a process&#8217;s current cpuset can be used are if either the process&#8217;s current working directory is its cpuset (it first did a <code>cd</code> or <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) to its cpuset directory beneath <i>/dev/cpuset</i>, which is a bit unusual) or if some user code converts the relative cpuset path to a full filesystem path. </p>
<p> In theory, this means that user code should specify cpusets using absolute pathnames, which requires knowing the mount point of the cpuset filesystem (usually, but not necessarily, <i>/dev/cpuset</i>). In practice, all user level code that this author is aware of simply assumes that if the cpuset filesystem is mounted, then it is mounted at <i>/dev/cpuset</i>. Furthermore, it is common practice for carefully written user code to verify the presence of the pseudo-file <i>/dev/cpuset/tasks</i> in order to verify that the cpuset pseudo-filesystem is currently mounted.</p>
<h2>Warnings</h2>
<h3>Enabling memory_pressure</h3>
<p>By default, the per-cpuset file <i>cpuset.memory_pressure</i> always contains zero (0). Unless this feature is enabled by writing &quot;1&quot; to the pseudo-file <i>/dev/cpuset/cpuset.memory_pressure_enabled</i>, the kernel does not compute per-cpuset <i>memory_pressure</i>.</p>
<h3>Using the echo command</h3>
<p>When using the <code>echo</code> command at the shell prompt to change the values of cpuset files, beware that the built-in <code>echo</code> command in some shells does not display an error message if the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call fails. For example, if the command: </p>
<p> echo 19 &gt; cpuset.mems </p>
<p> failed because memory node 19 was not allowed (perhaps the current system does not have a memory node 19), then the <code>echo</code> command might not display any error. It is better to use the <code>/bin/echo</code> external command to change cpuset file settings, as this command will display <code><a href="/docs/linux/man/2-write/">write</a></code>(2) errors, as in the example: </p>
<p> /bin/echo 19 &gt; cpuset.mems /bin/echo: write error: Invalid argument</p>
<h2>Exceptions</h2>
<h3>Memory placement</h3>
<p>Not all allocations of system memory are constrained by cpusets, for the following reasons. </p>
<p> If hot-plug functionality is used to remove all the CPUs that are currently assigned to a cpuset, then the kernel will automatically update the <i>cpus_allowed</i> of all processes attached to CPUs in that cpuset to allow all CPUs. When memory hot-plug functionality for removing memory nodes is available, a similar exception is expected to apply there as well. In general, the kernel prefers to violate cpuset placement, rather than starving a process that has had all its allowed CPUs or memory nodes taken offline. User code should reconfigure cpusets to refer only to online CPUs and memory nodes when using hot-plug to add or remove such resources. </p>
<p> A few kernel-critical, internal memory-allocation requests, marked GFP_ATOMIC, must be satisfied immediately. The kernel may drop some request or malfunction if one of these allocations fail. If such a request cannot be satisfied within the current process&#8217;s cpuset, then we relax the cpuset, and look for memory anywhere we can find it. It&#8217;s better to violate the cpuset than stress the kernel. </p>
<p> Allocations of memory requested by kernel drivers while processing an interrupt lack any relevant process context, and are not confined by cpusets.</p>
<h3>Renaming cpusets</h3>
<p>You can use the <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) system call to rename cpusets. Only simple renaming is supported; that is, changing the name of a cpuset directory is permitted, but moving a directory into a different directory is not permitted.</p>
<h2>Errors</h2>
<p>The Linux kernel implementation of cpusets sets <i>errno</i> to specify the reason for a failed system call affecting cpusets. </p>
<p> The possible <i>errno</i> settings and their meaning when set on a failed cpuset call are as listed below.</p>
<dl>
<dt><code>E2BIG</code></p>
<dd>Attempted a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) on a special cpuset file with a length larger than some kernel-determined upper limit on the length of such writes.</p>
<dt><code>EACCES</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) the process ID (PID) of a process to a cpuset <i>tasks</i> file when one lacks permission to move that process.</p>
<dt><code>EACCES</code></p>
<dd>Attempted to add, using <code><a href="/docs/linux/man/2-write/">write</a></code>(2), a CPU or memory node to a cpuset, when that CPU or memory node was not already in its parent.</p>
<dt><code>EACCES</code></p>
<dd>Attempted to set, using <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <i>cpuset.cpu_exclusive</i> or <i>cpuset.mem_exclusive</i> on a cpuset whose parent lacks the same setting.</p>
<dt><code>EACCES</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a <i>cpuset.memory_pressure</i> file.</p>
<dt><code>EACCES</code></p>
<dd>Attempted to create a file in a cpuset directory.</p>
<dt><code>EBUSY</code></p>
<dd>Attempted to remove, using <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), a cpuset with attached processes.</p>
<dt><code>EBUSY</code></p>
<dd>Attempted to remove, using <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), a cpuset with child cpusets.</p>
<dt><code>EBUSY</code></p>
<dd>Attempted to remove a CPU or memory node from a cpuset that is also in a child of that cpuset.</p>
<dt><code>EEXIST</code></p>
<dd>Attempted to create, using <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), a cpuset that already exists.</p>
<dt><code>EEXIST</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) a cpuset to a name that already exists.</p>
<dt><code>EFAULT</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a cpuset file using a buffer that is outside the writing processes accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to change a cpuset, using <code><a href="/docs/linux/man/2-write/">write</a></code>(2), in a way that would violate a <i>cpu_exclusive</i> or <i>mem_exclusive</i> attribute of that cpuset or any of its siblings.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) an empty <i>cpuset.cpus</i> or <i>cpuset.mems</i> list to a cpuset which has attached processes or child cpusets.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a <i>cpuset.cpus</i> or <i>cpuset.mems</i> list which included a range with the second number smaller than the first number.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a <i>cpuset.cpus</i> or <i>cpuset.mems</i> list which included an invalid character in the string.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a list to a <i>cpuset.cpus</i> file that did not include any online CPUs.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a list to a <i>cpuset.mems</i> file that did not include any online memory nodes.</p>
<dt><code>EINVAL</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a list to a <i>cpuset.mems</i> file that included a node that held no memory.</p>
<dt><code>EIO</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) a string to a cpuset <i>tasks</i> file that does not begin with an ASCII decimal integer.</p>
<dt><code>EIO</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) a cpuset into a different directory.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) a <i>/proc/&lt;pid&gt;/cpuset</i> file for a cpuset path that is longer than the kernel page size.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>Attempted to create, using <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), a cpuset whose base directory name is longer than 255 characters.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>Attempted to create, using <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), a cpuset whose full pathname, including the mount point (typically &quot;/dev/cpuset/&quot;) prefix, is longer than 4095 characters.</p>
<dt><code>ENODEV</code></p>
<dd>The cpuset was removed by another process at the same time as a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) was attempted on one of the pseudo-files in the cpuset directory.</p>
<dt><code>ENOENT</code></p>
<dd>Attempted to create, using <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), a cpuset in a parent cpuset that doesn&#8217;t exist.</p>
<dt><code>ENOENT</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-access/">access</a></code>(2) or <code><a href="/docs/linux/man/2-open/">open</a></code>(2) a nonexistent file in a cpuset directory.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory is available within the kernel; can occur on a variety of system calls affecting cpusets, but only if the system is extremely short of memory.</p>
<dt><code>ENOSPC</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) the process ID (PID) of a process to a cpuset <i>tasks</i> file when the cpuset had an empty <i>cpuset.cpus</i> or empty <i>cpuset.mems</i> setting.</p>
<dt><code>ENOSPC</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) an empty <i>cpuset.cpus</i> or <i>cpuset.mems</i> setting to a cpuset that has tasks attached.</p>
<dt><code>ENOTDIR</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2) a nonexistent cpuset.</p>
<dt><code>EPERM</code></p>
<dd>Attempted to remove a file from a cpuset directory.</p>
<dt><code>ERANGE</code></p>
<dd>Specified a <i>cpuset.cpus</i> or <i>cpuset.mems</i> list to the kernel which included a number too large for the kernel to set in its bit masks.</p>
<dt><code>ESRCH</code></p>
<dd>Attempted to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) the process ID (PID) of a nonexistent process to a cpuset <i>tasks</i> file.</dl>
<h2>Versions</h2>
<p>Cpusets appeared in version 2.6.12 of the Linux kernel.</p>
<h2>Notes</h2>
<p>Despite its name, the <i>pid</i> parameter is actually a thread ID, and each thread in a threaded group can be attached to a different cpuset. The value returned from a call to <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) can be passed in the argument <i>pid</i>.</p>
<h2>Bugs</h2>
<p><i>cpuset.memory_pressure</i> cpuset files can be opened for writing, creation, or truncation, but then the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) fails with <i>errno</i> set to <code>EACCES</code>, and the creation and truncation options on <code><a href="/docs/linux/man/2-open/">open</a></code>(2) have no effect.</p>
<h2>Examples</h2>
<p>The following examples demonstrate querying and setting cpuset options using shell commands.</p>
<h3>Creating and attaching to a cpuset.</h3>
<p>To create a new cpuset and attach the current command shell to it, the steps are: </p>
<dl>
<dt>1)</p>
<dd>mkdir /dev/cpuset (if not already done)</p>
<dt>2)</p>
<dd>mount -t cpuset none /dev/cpuset (if not already done)</p>
<dt>3)</p>
<dd>Create the new cpuset using <code><a href="/docs/linux/man/1-mkdir/">mkdir</a></code>(1).</p>
<dt>4)</p>
<dd>Assign CPUs and memory nodes to the new cpuset.</p>
<dt>5)</p>
<dd>Attach the shell to the new cpuset.</dl>
<p> For example, the following sequence of commands will set up a cpuset named &quot;Charlie&quot;, containing just CPUs 2 and 3, and memory node 1, and then attach the current shell to that cpuset. </p>
<p> $<code> mkdir /dev/cpuset</code> $<code> mount -t cpuset cpuset /dev/cpuset</code> $<code> cd /dev/cpuset</code> $<code> mkdir Charlie</code> $<code> cd Charlie</code> $<code> /bin/echo 2-3 &gt; cpuset.cpus</code> $<code> /bin/echo 1 &gt; cpuset.mems</code> $<code> /bin/echo $$ &gt; tasks</code> # The current shell is now running in cpuset Charlie # The next line should display &#8216;/Charlie&#8217; $<code> cat /proc/self/cpuset</code></p>
<h3>Migrating a job to different memory nodes.</h3>
<p>To migrate a job (the set of processes attached to a cpuset) to different CPUs and memory nodes in the system, including moving the memory pages currently allocated to that job, perform the following steps. </p>
<dl>
<dt>1)</p>
<dd>Let&#8217;s say we want to move the job in cpuset <i>alpha</i> (CPUs 4-7 and memory nodes 2-3) to a new cpuset <i>beta</i> (CPUs 16-19 and memory nodes 8-9).</p>
<dt>2)</p>
<dd>First create the new cpuset <i>beta</i>.</p>
<dt>3)</p>
<dd>Then allow CPUs 16-19 and memory nodes 8-9 in <i>beta</i>.</p>
<dt>4)</p>
<dd>Then enable <i>memory_migration</i> in <i>beta</i>.</p>
<dt>5)</p>
<dd>Then move each process from <i>alpha</i> to <i>beta</i>.</dl>
<p> The following sequence of commands accomplishes this. </p>
<p> $<code> cd /dev/cpuset</code> $<code> mkdir beta</code> $<code> cd beta</code> $<code> /bin/echo 16-19 &gt; cpuset.cpus</code> $<code> /bin/echo 8-9 &gt; cpuset.mems</code> $<code> /bin/echo 1 &gt; cpuset.memory_migrate</code> $<code> while read i; do /bin/echo $i; done &lt; ../alpha/tasks &gt; tasks</code> </p>
<p> The above should move any processes in <i>alpha</i> to <i>beta</i>, and any memory held by these processes on memory nodes 2-3 to memory nodes 8-9, respectively. </p>
<p> Notice that the last step of the above sequence did not do: </p>
<p> $<code> cp ../alpha/tasks tasks</code> </p>
<p> The <i>while</i> loop, rather than the seemingly easier use of the <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1) command, was necessary because only one process PID at a time may be written to the <i>tasks</i> file. </p>
<p> The same effect (writing one PID at a time) as the <i>while</i> loop can be accomplished more efficiently, in fewer keystrokes and in syntax that works on any shell, but alas more obscurely, by using the <code>-u</code> (unbuffered) option of <code><a href="/docs/linux/man/1-sed/">sed</a></code>(1): </p>
<p> $<code> sed -un p &lt; ../alpha/tasks &gt; tasks</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1), <code><a href="/docs/linux/man/2-get_mempolicy/">get_mempolicy</a></code>(2), <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-set_mempolicy/">set_mempolicy</a></code>(2), <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7), <code><a href="/docs/linux/man/7-numa/">numa</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7), <code><a href="/docs/linux/man/8-migratepages/">migratepages</a></code>(8), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8) </p>
<p> <i>Documentation/admin-guide/cgroup-v1/cpusets.rst</i> in the Linux kernel source tree (or <i>Documentation/cgroup-v1/cpusets.txt</i> before Linux 4.18, and <i>Documentation/cpusets.txt</i> before Linux 2.6.29)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
