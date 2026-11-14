---
title: "cgroups(7)"
name: "cgroups"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cgroups/"
description: "cgroups – Linux control groups"
---

<p>cgroups &#8211; Linux control groups</p>
<h2>Description</h2>
<p>Control groups, usually referred to as cgroups, are a Linux kernel feature which allow processes to be organized into hierarchical groups whose usage of various types of resources can then be limited and monitored. The kernel&#8217;s cgroup interface is provided through a pseudo-filesystem called cgroupfs. Grouping is implemented in the core cgroup kernel code, while resource tracking and limits are implemented in a set of per-resource-type subsystems (memory, CPU, and so on).</p>
<h3>Terminology</h3>
<p>A <i>cgroup</i> is a collection of processes that are bound to a set of limits or parameters defined via the cgroup filesystem. </p>
<p> A <i>subsystem</i> is a kernel component that modifies the behavior of the processes in a cgroup. Various subsystems have been implemented, making it possible to do things such as limiting the amount of CPU time and memory available to a cgroup, accounting for the CPU time used by a cgroup, and freezing and resuming execution of the processes in a cgroup. Subsystems are sometimes also known as <i>resource controllers</i> (or simply, controllers). </p>
<p> The cgroups for a controller are arranged in a <i>hierarchy</i>. This hierarchy is defined by creating, removing, and renaming subdirectories within the cgroup filesystem. At each level of the hierarchy, attributes (e.g., limits) can be defined. The limits, control, and accounting provided by cgroups generally have effect throughout the subhierarchy underneath the cgroup where the attributes are defined. Thus, for example, the limits placed on a cgroup at a higher level in the hierarchy cannot be exceeded by descendant cgroups.</p>
<h3>Cgroups version 1 and version 2</h3>
<p>The initial release of the cgroups implementation was in Linux 2.6.24. Over time, various cgroup controllers have been added to allow the management of various types of resources. However, the development of these controllers was largely uncoordinated, with the result that many inconsistencies arose between controllers and management of the cgroup hierarchies became rather complex. A longer description of these problems can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v2.rst</i> (or <i>Documentation/cgroup-v2.txt</i> in Linux 4.17 and earlier). </p>
<p> Because of the problems with the initial cgroups implementation (cgroups version 1), starting in Linux 3.10, work began on a new, orthogonal implementation to remedy these problems. Initially marked experimental, and hidden behind the <i>-o&nbsp;__DEVEL__sane_behavior</i> mount option, the new version (cgroups version 2) was eventually made official with the release of Linux 4.5. Differences between the two versions are described in the text below. The file <i>cgroup.sane_behavior</i>, present in cgroups v1, is a relic of this mount option. The file always reports &quot;0&quot; and is only retained for backward compatibility. </p>
<p> Although cgroups v2 is intended as a replacement for cgroups v1, the older system continues to exist (and for compatibility reasons is unlikely to be removed). Currently, cgroups v2 implements only a subset of the controllers available in cgroups v1. The two systems are implemented so that both v1 controllers and v2 controllers can be mounted on the same system. Thus, for example, it is possible to use those controllers that are supported under version 2, while also using version 1 controllers where version 2 does not yet support those controllers. The only restriction here is that a controller can&#8217;t be simultaneously employed in both a cgroups v1 hierarchy and in the cgroups v2 hierarchy.</p>
<h2>Cgroups Version 1</h2>
<p>Under cgroups v1, each controller may be mounted against a separate cgroup filesystem that provides its own hierarchical organization of the processes on the system. It is also possible to comount multiple (or even all) cgroups v1 controllers against the same cgroup filesystem, meaning that the comounted controllers manage the same hierarchical organization of processes. </p>
<p> For each mounted hierarchy, the directory tree mirrors the control group hierarchy. Each control group is represented by a directory, with each of its child control cgroups represented as a child directory. For instance, <i>/user/joe/1.session</i> represents control group <i>1.session</i>, which is a child of cgroup <i>joe</i>, which is a child of <i>/user</i>. Under each cgroup directory is a set of files which can be read or written to, reflecting resource limits and a few general cgroup properties.</p>
<h3>Tasks (threads) versus processes</h3>
<p>In cgroups v1, a distinction is drawn between <i>processes</i> and <i>tasks</i>. In this view, a process can consist of multiple tasks (more commonly called threads, from a user-space perspective, and called such in the remainder of this man page). In cgroups v1, it is possible to independently manipulate the cgroup memberships of the threads in a process. </p>
<p> The cgroups v1 ability to split threads across different cgroups caused problems in some cases. For example, it made no sense for the <i>memory</i> controller, since all of the threads of a process share a single address space. Because of these problems, the ability to independently manipulate the cgroup memberships of the threads in a process was removed in the initial cgroups v2 implementation, and subsequently restored in a more limited form (see the discussion of &quot;thread mode&quot; below).</p>
<h3>Mounting v1 controllers</h3>
<p>The use of cgroups requires a kernel built with the <code>CONFIG_CGROUP</code> option. In addition, each of the v1 controllers has an associated configuration option that must be set in order to employ that controller. </p>
<p> In order to use a v1 controller, it must be mounted against a cgroup filesystem. The usual place for such mounts is under a <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystem mounted at <i>/sys/fs/cgroup</i>. Thus, one might mount the <i>cpu</i> controller as follows: </p>
<p> mount -t cgroup -o cpu none /sys/fs/cgroup/cpu </p>
<p> It is possible to comount multiple controllers against the same hierarchy. For example, here the <i>cpu</i> and <i>cpuacct</i> controllers are comounted against a single hierarchy: </p>
<p> mount -t cgroup -o cpu,cpuacct none /sys/fs/cgroup/cpu,cpuacct </p>
<p> Comounting controllers has the effect that a process is in the same cgroup for all of the comounted controllers. Separately mounting controllers allows a process to be in cgroup <i>/foo1</i> for one controller while being in <i>/foo2/foo3</i> for another. </p>
<p> It is possible to comount all v1 controllers against the same hierarchy: </p>
<p> mount -t cgroup -o all cgroup /sys/fs/cgroup </p>
<p> (One can achieve the same result by omitting <i>-o all</i>, since it is the default if no controllers are explicitly specified.) </p>
<p> It is not possible to mount the same controller against multiple cgroup hierarchies. For example, it is not possible to mount both the <i>cpu</i> and <i>cpuacct</i> controllers against one hierarchy, and to mount the <i>cpu</i> controller alone against another hierarchy. It is possible to create multiple mount points with exactly the same set of comounted controllers. However, in this case all that results is multiple mount points providing a view of the same hierarchy. </p>
<p> Note that on many systems, the v1 controllers are automatically mounted under <i>/sys/fs/cgroup</i>; in particular, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) automatically creates such mount points.</p>
<h3>Unmounting v1 controllers</h3>
<p>A mounted cgroup filesystem can be unmounted using the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) command, as in the following example: </p>
<p> umount /sys/fs/cgroup/pids </p>
<p> <i>But note well</i>: a cgroup filesystem is unmounted only if it is not busy, that is, it has no child cgroups. If this is not the case, then the only effect of the <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) is to make the mount invisible. Thus, to ensure that the mount point is really removed, one must first remove all child cgroups, which in turn can be done only after all member processes have been moved from those cgroups to the root cgroup.</p>
<h3>Cgroups version 1 controllers</h3>
<p>Each of the cgroups version 1 controllers is governed by a kernel configuration option (listed below). Additionally, the availability of the cgroups feature is governed by the <code>CONFIG_CGROUPS</code> kernel configuration option.</p>
<dl>
<dt><i>cpu</i> (since Linux 2.6.24; <i></i><code>CONFIG_CGROUP_SCHED</code>)</p>
<dd>Cgroups can be guaranteed a minimum number of &quot;CPU shares&quot; when a system is busy. This does not limit a cgroup&#8217;s CPU usage if the CPUs are not busy. For further information, see <i>Documentation/scheduler/sched-design-CFS.rst</i> (or <i>Documentation/scheduler/sched-design-CFS.txt</i> in Linux 5.2 and earlier).</p>
<dd>In Linux 3.2, this controller was extended to provide CPU &quot;bandwidth&quot; control. If the kernel is configured with <code>CONFIG_CFS_BANDWIDTH</code>, then within each scheduling period (defined via a file in the cgroup directory), it is possible to define an upper limit on the CPU time allocated to the processes in a cgroup. This upper limit applies even if there is no other competition for the CPU. Further information can be found in the kernel source file <i>Documentation/scheduler/sched-bwc.rst</i> (or <i>Documentation/scheduler/sched-bwc.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>cpuacct</i> (since Linux 2.6.24; <i></i><code>CONFIG_CGROUP_CPUACCT</code>)</p>
<dd>This provides accounting for CPU usage by groups of processes.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/cpuacct.rst</i> (or <i>Documentation/cgroup-v1/cpuacct.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>cpuset</i> (since Linux 2.6.24; <i></i><code>CONFIG_CPUSETS</code>)</p>
<dd>This cgroup can be used to bind the processes in a cgroup to a specified set of CPUs and NUMA nodes.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/cpusets.rst</i> (or <i>Documentation/cgroup-v1/cpusets.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>memory</i> (since Linux 2.6.25; <i></i><code>CONFIG_MEMCG</code>)</p>
<dd>The memory controller supports reporting and limiting of process memory, kernel memory, and swap used by cgroups.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/memory.rst</i> (or <i>Documentation/cgroup-v1/memory.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>devices</i> (since Linux 2.6.26; <i></i><code>CONFIG_CGROUP_DEVICE</code>)</p>
<dd>This supports controlling which processes may create (mknod) devices as well as open them for reading or writing. The policies may be specified as allow-lists and deny-lists. Hierarchy is enforced, so new rules must not violate existing rules for the target or ancestor cgroups.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/devices.rst</i> (or <i>Documentation/cgroup-v1/devices.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>freezer</i> (since Linux 2.6.28; <i></i><code>CONFIG_CGROUP_FREEZER</code>)</p>
<dd>The <i>freezer</i> cgroup can suspend and restore (resume) all processes in a cgroup. Freezing a cgroup <i>/A</i> also causes its children, for example, processes in <i>/A/B</i>, to be frozen.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/freezer-subsystem.rst</i> (or <i>Documentation/cgroup-v1/freezer-subsystem.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>net_cls</i> (since Linux 2.6.29; <i></i><code>CONFIG_CGROUP_NET_CLASSID</code>)</p>
<dd>This places a classid, specified for the cgroup, on network packets created by a cgroup. These classids can then be used in firewall rules, as well as used to shape traffic using <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8). This applies only to packets leaving the cgroup, not to traffic arriving at the cgroup.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/net_cls.rst</i> (or <i>Documentation/cgroup-v1/net_cls.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>blkio</i> (since Linux 2.6.33; <i></i><code>CONFIG_BLK_CGROUP</code>)</p>
<dd>The <i>blkio</i> cgroup controls and limits access to specified block devices by applying IO control in the form of throttling and upper limits against leaf nodes and intermediate nodes in the storage hierarchy.</p>
<dd>Two policies are available. The first is a proportional-weight time-based division of disk implemented with CFQ. This is in effect for leaf nodes using CFQ. The second is a throttling policy which specifies upper I/O rate limits on a device.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/blkio-controller.rst</i> (or <i>Documentation/cgroup-v1/blkio-controller.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>perf_event</i> (since Linux 2.6.39; <i></i><code>CONFIG_CGROUP_PERF</code>)</p>
<dd>This controller allows <i>perf</i> monitoring of the set of processes grouped in a cgroup.</p>
<dd>Further information can be found in the kernel source files</p>
<dt><i>net_prio</i> (since Linux 3.3; <i></i><code>CONFIG_CGROUP_NET_PRIO</code>)</p>
<dd>This allows priorities to be specified, per network interface, for cgroups.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/net_prio.rst</i> (or <i>Documentation/cgroup-v1/net_prio.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>hugetlb</i> (since Linux 3.5; <i></i><code>CONFIG_CGROUP_HUGETLB</code>)</p>
<dd>This supports limiting the use of huge pages by cgroups.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/hugetlb.rst</i> (or <i>Documentation/cgroup-v1/hugetlb.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>pids</i> (since Linux 4.3; <i></i><code>CONFIG_CGROUP_PIDS</code>)</p>
<dd>This controller permits limiting the number of process that may be created in a cgroup (and its descendants).</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/pids.rst</i> (or <i>Documentation/cgroup-v1/pids.txt</i> in Linux 5.2 and earlier).</p>
<dt><i>rdma</i> (since Linux 4.11; <i></i><code>CONFIG_CGROUP_RDMA</code>)</p>
<dd>The RDMA controller permits limiting the use of RDMA/IB-specific resources per cgroup.</p>
<dd>Further information can be found in the kernel source file <i>Documentation/admin-guide/cgroup-v1/rdma.rst</i> (or <i>Documentation/cgroup-v1/rdma.txt</i> in Linux 5.2 and earlier).</dl>
<h3>Creating cgroups and moving processes</h3>
<p>A cgroup filesystem initially contains a single root cgroup, &#8216;/&#8217;, which all processes belong to. A new cgroup is created by creating a directory in the cgroup filesystem: </p>
<p> mkdir /sys/fs/cgroup/cpu/cg1 </p>
<p> This creates a new empty cgroup. </p>
<p> A process may be moved to this cgroup by writing its PID into the cgroup&#8217;s <i>cgroup.procs</i> file: </p>
<p> echo $$ &gt; /sys/fs/cgroup/cpu/cg1/cgroup.procs </p>
<p> Only one PID at a time should be written to this file. </p>
<p> Writing the value 0 to a <i>cgroup.procs</i> file causes the writing process to be moved to the corresponding cgroup. </p>
<p> When writing a PID into the <i>cgroup.procs</i>, all threads in the process are moved into the new cgroup at once. </p>
<p> Within a hierarchy, a process can be a member of exactly one cgroup. Writing a process&#8217;s PID to a <i>cgroup.procs</i> file automatically removes it from the cgroup of which it was previously a member. </p>
<p> The <i>cgroup.procs</i> file can be read to obtain a list of the processes that are members of a cgroup. The returned list of PIDs is not guaranteed to be in order. Nor is it guaranteed to be free of duplicates. (For example, a PID may be recycled while reading from the list.) </p>
<p> In cgroups v1, an individual thread can be moved to another cgroup by writing its thread ID (i.e., the kernel thread ID returned by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)) to the <i>tasks</i> file in a cgroup directory. This file can be read to discover the set of threads that are members of the cgroup.</p>
<h3>Removing cgroups</h3>
<p>To remove a cgroup, it must first have no child cgroups and contain no (nonzombie) processes. So long as that is the case, one can simply remove the corresponding directory pathname. Note that files in a cgroup directory cannot and need not be removed.</p>
<h3>Cgroups v1 release notification</h3>
<p>Two files can be used to determine whether the kernel provides notifications when a cgroup becomes empty. A cgroup is considered to be empty when it contains no child cgroups and no member processes. </p>
<p> A special file in the root directory of each cgroup hierarchy, <i>release_agent</i>, can be used to register the pathname of a program that may be invoked when a cgroup in the hierarchy becomes empty. The pathname of the newly empty cgroup (relative to the cgroup mount point) is provided as the sole command-line argument when the <i>release_agent</i> program is invoked. The <i>release_agent</i> program might remove the cgroup directory, or perhaps repopulate it with a process. </p>
<p> The default value of the <i>release_agent</i> file is empty, meaning that no release agent is invoked. </p>
<p> The content of the <i>release_agent</i> file can also be specified via a mount option when the cgroup filesystem is mounted: </p>
<p> mount -o release_agent=pathname &#8230; </p>
<p> Whether or not the <i>release_agent</i> program is invoked when a particular cgroup becomes empty is determined by the value in the <i>notify_on_release</i> file in the corresponding cgroup directory. If this file contains the value 0, then the <i>release_agent</i> program is not invoked. If it contains the value 1, the <i>release_agent</i> program is invoked. The default value for this file in the root cgroup is 0. At the time when a new cgroup is created, the value in this file is inherited from the corresponding file in the parent cgroup.</p>
<h3>Cgroup v1 named hierarchies</h3>
<p>In cgroups v1, it is possible to mount a cgroup hierarchy that has no attached controllers: </p>
<p> mount -t cgroup -o none,name=somename none /some/mount/point </p>
<p> Multiple instances of such hierarchies can be mounted; each hierarchy must have a unique name. The only purpose of such hierarchies is to track processes. (See the discussion of release notification below.) An example of this is the <i>name=systemd</i> cgroup hierarchy that is used by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) to track services and user sessions. </p>
<p> Since Linux 5.0, the <i>cgroup_no_v1</i> kernel boot option (described below) can be used to disable cgroup v1 named hierarchies, by specifying <i>cgroup_no_v1=named</i>.</p>
<h2>Cgroups Version 2</h2>
<p>In cgroups v2, all mounted controllers reside in a single unified hierarchy. While (different) controllers may be simultaneously mounted under the v1 and v2 hierarchies, it is not possible to mount the same controller simultaneously under both the v1 and the v2 hierarchies. </p>
<p> The new behaviors in cgroups v2 are summarized here, and in some cases elaborated in the following subsections.</p>
<dl>
<dt>1.</p>
<dd>Cgroups v2 provides a unified hierarchy against which all controllers are mounted.</p>
<dt>2.</p>
<dd>&quot;Internal&quot; processes are not permitted. With the exception of the root cgroup, processes may reside only in leaf nodes (cgroups that do not themselves contain child cgroups). The details are somewhat more subtle than this, and are described below.</p>
<dt>3.</p>
<dd>Active cgroups must be specified via the files <i>cgroup.controllers</i> and <i>cgroup.subtree_control</i>.</p>
<dt>4.</p>
<dd>The <i>tasks</i> file has been removed. In addition, the <i>cgroup.clone_children</i> file that is employed by the <i>cpuset</i> controller has been removed.</p>
<dt>5.</p>
<dd>An improved mechanism for notification of empty cgroups is provided by the <i>cgroup.events</i> file.</dl>
<p> For more changes, see the <i>Documentation/admin-guide/cgroup-v2.rst</i> file in the kernel source (or <i>Documentation/cgroup-v2.txt</i> in Linux 4.17 and earlier). </p>
<p> Some of the new behaviors listed above saw subsequent modification with the addition in Linux 4.14 of &quot;thread mode&quot; (described below).</p>
<h3>Cgroups v2 unified hierarchy</h3>
<p>In cgroups v1, the ability to mount different controllers against different hierarchies was intended to allow great flexibility for application design. In practice, though, the flexibility turned out to be less useful than expected, and in many cases added complexity. Therefore, in cgroups v2, all available controllers are mounted against a single hierarchy. The available controllers are automatically mounted, meaning that it is not necessary (or possible) to specify the controllers when mounting the cgroup v2 filesystem using a command such as the following: </p>
<p> mount -t cgroup2 none /mnt/cgroup2 </p>
<p> A cgroup v2 controller is available only if it is not currently in use via a mount against a cgroup v1 hierarchy. Or, to put things another way, it is not possible to employ the same controller against both a v1 hierarchy and the unified v2 hierarchy. This means that it may be necessary first to unmount a v1 controller (as described above) before that controller is available in v2. Since <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) makes heavy use of some v1 controllers by default, it can in some cases be simpler to boot the system with selected v1 controllers disabled. To do this, specify the <i>cgroup_no_v1=list</i> option on the kernel boot command line; <i>list</i> is a comma-separated list of the names of the controllers to disable, or the word <i>all</i> to disable all v1 controllers. (This situation is correctly handled by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), which falls back to operating without the specified controllers.) </p>
<p> Note that on many modern systems, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) automatically mounts the <i>cgroup2</i> filesystem at <i>/sys/fs/cgroup/unified</i> during the boot process.</p>
<h3>Cgroups v2 mount options</h3>
<p>The following options (<i>mount -o</i>) can be specified when mounting the group v2 filesystem:</p>
<dl>
<dt><i>nsdelegate</i> (since Linux 4.15)</p>
<dd>Treat cgroup namespaces as delegation boundaries. For details, see below.</p>
<dt><i>memory_localevents</i> (since Linux 5.2)</p>
<dd>The <i>memory.events</i> should show statistics only for the cgroup itself, and not for any descendant cgroups. This was the behavior before Linux 5.2. Starting in Linux 5.2, the default behavior is to include statistics for descendant cgroups in <i>memory.events</i>, and this mount option can be used to revert to the legacy behavior. This option is system wide and can be set on mount or modified through remount only from the initial mount namespace; it is silently ignored in noninitial namespaces.</dl>
<h3>Cgroups v2 controllers</h3>
<p>The following controllers, documented in the kernel source file <i>Documentation/admin-guide/cgroup-v2.rst</i> (or <i>Documentation/cgroup-v2.txt</i> in Linux 4.17 and earlier), are supported in cgroups version 2:</p>
<dl>
<dt><i>cpu</i> (since Linux 4.15)</p>
<dd>This is the successor to the version 1 <i>cpu</i> and <i>cpuacct</i> controllers.</p>
<dt><i>cpuset</i> (since Linux 5.0)</p>
<dd>This is the successor of the version 1 <i>cpuset</i> controller.</p>
<dt><i>freezer</i> (since Linux 5.2)</p>
<dd>This is the successor of the version 1 <i>freezer</i> controller.</p>
<dt><i>hugetlb</i> (since Linux 5.6)</p>
<dd>This is the successor of the version 1 <i>hugetlb</i> controller.</p>
<dt><i>io</i> (since Linux 4.5)</p>
<dd>This is the successor of the version 1 <i>blkio</i> controller.</p>
<dt><i>memory</i> (since Linux 4.5)</p>
<dd>This is the successor of the version 1 <i>memory</i> controller.</p>
<dt><i>perf_event</i> (since Linux 4.11)</p>
<dd>This is the same as the version 1 <i>perf_event</i> controller.</p>
<dt><i>pids</i> (since Linux 4.5)</p>
<dd>This is the same as the version 1 <i>pids</i> controller.</p>
<dt><i>rdma</i> (since Linux 4.11)</p>
<dd>This is the same as the version 1 <i>rdma</i> controller.</dl>
<p> There is no direct equivalent of the <i>net_cls</i> and <i>net_prio</i> controllers from cgroups version 1. Instead, support has been added to <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) to allow eBPF filters that hook on cgroup v2 pathnames to make decisions about network traffic on a per-cgroup basis. </p>
<p> The v2 <i>devices</i> controller provides no interface files; instead, device control is gated by attaching an eBPF (<code>BPF_CGROUP_DEVICE</code>) program to a v2 cgroup.</p>
<h3>Cgroups v2 subtree control</h3>
<p>Each cgroup in the v2 hierarchy contains the following two files:</p>
<dl>
<dt><i>cgroup.controllers</i></p>
<dd>This read-only file exposes a list of the controllers that are <i>available</i> in this cgroup. The contents of this file match the contents of the <i>cgroup.subtree_control</i> file in the parent cgroup.</p>
<dt><i>cgroup.subtree_control</i></p>
<dd>This is a list of controllers that are <i>active</i> (<i>enabled</i>) in the cgroup. The set of controllers in this file is a subset of the set in the <i>cgroup.controllers</i> of this cgroup. The set of active controllers is modified by writing strings to this file containing space-delimited controller names, each preceded by &#8216;+&#8217; (to enable a controller) or &#8216;-&#8216; (to disable a controller), as in the following example:</p>
<dd>echo &#8216;+pids -memory&#8217; &gt; x/y/cgroup.subtree_control</p>
<dd>An attempt to enable a controller that is not present in <i>cgroup.controllers</i> leads to an <code>ENOENT</code> error when writing to the <i>cgroup.subtree_control</i> file.</dl>
<p> Because the list of controllers in <i>cgroup.subtree_control</i> is a subset of those <i>cgroup.controllers</i>, a controller that has been disabled in one cgroup in the hierarchy can never be re-enabled in the subtree below that cgroup. </p>
<p> A cgroup&#8217;s <i>cgroup.subtree_control</i> file determines the set of controllers that are exercised in the <i>child</i> cgroups. When a controller (e.g., <i>pids</i>) is present in the <i>cgroup.subtree_control</i> file of a parent cgroup, then the corresponding controller-interface files (e.g., <i>pids.max</i>) are automatically created in the children of that cgroup and can be used to exert resource control in the child cgroups.</p>
<h3>Cgroups v2 no internal processes rule</h3>
<p>Cgroups v2 enforces a so-called &quot;no internal processes&quot; rule. Roughly speaking, this rule means that, with the exception of the root cgroup, processes may reside only in leaf nodes (cgroups that do not themselves contain child cgroups). This avoids the need to decide how to partition resources between processes which are members of cgroup A and processes in child cgroups of A. </p>
<p> For instance, if cgroup <i>/cg1/cg2</i> exists, then a process may reside in <i>/cg1/cg2</i>, but not in <i>/cg1</i>. This is to avoid an ambiguity in cgroups v1 with respect to the delegation of resources between processes in <i>/cg1</i> and its child cgroups. The recommended approach in cgroups v2 is to create a subdirectory called <i>leaf</i> for any nonleaf cgroup which should contain processes, but no child cgroups. Thus, processes which previously would have gone into <i>/cg1</i> would now go into <i>/cg1/leaf</i>. This has the advantage of making explicit the relationship between processes in <i>/cg1/leaf</i> and <i>/cg1</i>&#8216;s other children. </p>
<p> The &quot;no internal processes&quot; rule is in fact more subtle than stated above. More precisely, the rule is that a (nonroot) cgroup can&#8217;t both (1) have member processes, and (2) distribute resources into child cgroups&#8212;that is, have a nonempty <i>cgroup.subtree_control</i> file. Thus, it <i>is</i> possible for a cgroup to have both member processes and child cgroups, but before controllers can be enabled for that cgroup, the member processes must be moved out of the cgroup (e.g., perhaps into the child cgroups). </p>
<p> With the Linux 4.14 addition of &quot;thread mode&quot; (described below), the &quot;no internal processes&quot; rule has been relaxed in some cases.</p>
<h3>Cgroups v2 cgroup.events file</h3>
<p>Each nonroot cgroup in the v2 hierarchy contains a read-only file, <i>cgroup.events</i>, whose contents are key-value pairs (delimited by newline characters, with the key and value separated by spaces) providing state information about the cgroup: </p>
<p> $ <code>cat mygrp/cgroup.events</code> populated 1 frozen 0 </p>
<p> The following keys may appear in this file:</p>
<dl>
<dt><i>populated</i></p>
<dd>The value of this key is either 1, if this cgroup or any of its descendants has member processes, or otherwise 0.</p>
<dt><i>frozen</i> (since Linux 5.2)</p>
<dd>The value of this key is 1 if this cgroup is currently frozen, or 0 if it is not.</dl>
<p> The <i>cgroup.events</i> file can be monitored, in order to receive notification when the value of one of its keys changes. Such monitoring can be done using <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7), which notifies changes as <code>IN_MODIFY</code> events, or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), which notifies changes by returning the <code>POLLPRI</code> and <code>POLLERR</code> bits in the <i>revents</i> field.</p>
<h3>Cgroup v2 release notification</h3>
<p>Cgroups v2 provides a new mechanism for obtaining notification when a cgroup becomes empty. The cgroups v1 <i>release_agent</i> and <i>notify_on_release</i> files are removed, and replaced by the <i>populated</i> key in the <i>cgroup.events</i> file. This key either has the value 0, meaning that the cgroup (and its descendants) contain no (nonzombie) member processes, or 1, meaning that the cgroup (or one of its descendants) contains member processes. </p>
<p> The cgroups v2 release-notification mechanism offers the following advantages over the cgroups v1 <i>release_agent</i> mechanism:</p>
<dl>
<dt>*</p>
<dd>It allows for cheaper notification, since a single process can monitor multiple <i>cgroup.events</i> files (using the techniques described earlier). By contrast, the cgroups v1 mechanism requires the expense of creating a process for each notification.</p>
<dt>*</p>
<dd>Notification for different cgroup subhierarchies can be delegated to different processes. By contrast, the cgroups v1 mechanism allows only one release agent for an entire hierarchy.</dl>
<h3>Cgroups v2 cgroup.stat file</h3>
<p>Each cgroup in the v2 hierarchy contains a read-only <i>cgroup.stat</i> file (first introduced in Linux 4.14) that consists of lines containing key-value pairs. The following keys currently appear in this file:</p>
<dl>
<dt><i>nr_descendants</i></p>
<dd>This is the total number of visible (i.e., living) descendant cgroups underneath this cgroup.</p>
<dt><i>nr_dying_descendants</i></p>
<dd>This is the total number of dying descendant cgroups underneath this cgroup. A cgroup enters the dying state after being deleted. It remains in that state for an undefined period (which will depend on system load) while resources are freed before the cgroup is destroyed. Note that the presence of some cgroups in the dying state is normal, and is not indicative of any problem.</p>
<dd>A process can&#8217;t be made a member of a dying cgroup, and a dying cgroup can&#8217;t be brought back to life.</dl>
<h3>Limiting the number of descendant cgroups</h3>
<p>Each cgroup in the v2 hierarchy contains the following files, which can be used to view and set limits on the number of descendant cgroups under that cgroup:</p>
<dl>
<dt><i>cgroup.max.depth</i> (since Linux 4.14)</p>
<dd>This file defines a limit on the depth of nesting of descendant cgroups. A value of 0 in this file means that no descendant cgroups can be created. An attempt to create a descendant whose nesting level exceeds the limit fails (<i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2) fails with the error <code>EAGAIN</code>).</p>
<dd>Writing the string <i>&quot;max&quot;</i> to this file means that no limit is imposed. The default value in this file is <i>&quot;max&quot;</i>.</p>
<dt><i>cgroup.max.descendants</i> (since Linux 4.14)</p>
<dd>This file defines a limit on the number of live descendant cgroups that this cgroup may have. An attempt to create more descendants than allowed by the limit fails (<i><a href="/docs/linux/man/2-mkdir/">mkdir</a></i>(2) fails with the error <code>EAGAIN</code>).</p>
<dd>Writing the string <i>&quot;max&quot;</i> to this file means that no limit is imposed. The default value in this file is <i>&quot;max&quot;</i>.</dl>
<h2>Cgroups Delegation: Delegating A Hierarchy To A Less Privileged User</h2>
<p>In the context of cgroups, delegation means passing management of some subtree of the cgroup hierarchy to a nonprivileged user. Cgroups v1 provides support for delegation based on file permissions in the cgroup hierarchy but with less strict containment rules than v2 (as noted below). Cgroups v2 supports delegation with containment by explicit design. The focus of the discussion in this section is on delegation in cgroups v2, with some differences for cgroups v1 noted along the way. </p>
<p> Some terminology is required in order to describe delegation. A <i>delegater</i> is a privileged user (i.e., root) who owns a parent cgroup. A <i>delegatee</i> is a nonprivileged user who will be granted the permissions needed to manage some subhierarchy under that parent cgroup, known as the <i>delegated subtree</i>. </p>
<p> To perform delegation, the delegater makes certain directories and files writable by the delegatee, typically by changing the ownership of the objects to be the user ID of the delegatee. Assuming that we want to delegate the hierarchy rooted at (say) <i>/dlgt_grp</i> and that there are not yet any child cgroups under that cgroup, the ownership of the following is changed to the user ID of the delegatee:</p>
<dl>
<dt><i>/dlgt_grp</i></p>
<dd>Changing the ownership of the root of the subtree means that any new cgroups created under the subtree (and the files they contain) will also be owned by the delegatee.</p>
<dt><i>/dlgt_grp/cgroup.procs</i></p>
<dd>Changing the ownership of this file means that the delegatee can move processes into the root of the delegated subtree.</p>
<dt><i>/dlgt_grp/cgroup.subtree_control</i> (cgroups v2 only)</p>
<dd>Changing the ownership of this file means that the delegatee can enable controllers (that are present in <i>/dlgt_grp/cgroup.controllers</i>) in order to further redistribute resources at lower levels in the subtree. (As an alternative to changing the ownership of this file, the delegater might instead add selected controllers to this file.)</p>
<dt><i>/dlgt_grp/cgroup.threads</i> (cgroups v2 only)</p>
<dd>Changing the ownership of this file is necessary if a threaded subtree is being delegated (see the description of &quot;thread mode&quot;, below). This permits the delegatee to write thread IDs to the file. (The ownership of this file can also be changed when delegating a domain subtree, but currently this serves no purpose, since, as described below, it is not possible to move a thread between domain cgroups by writing its thread ID to the <i>cgroup.threads</i> file.)</p>
<dd>In cgroups v1, the corresponding file that should instead be delegated is the <i>tasks</i> file.</dl>
<p> The delegater should <i>not</i> change the ownership of any of the controller interfaces files (e.g., <i>pids.max</i>, <i>memory.high</i>) in <i>dlgt_grp</i>. Those files are used from the next level above the delegated subtree in order to distribute resources into the subtree, and the delegatee should not have permission to change the resources that are distributed into the delegated subtree. </p>
<p> See also the discussion of the <i>/sys/kernel/cgroup/delegate</i> file in NOTES for information about further delegatable files in cgroups v2. </p>
<p> After the aforementioned steps have been performed, the delegatee can create child cgroups within the delegated subtree (the cgroup subdirectories and the files they contain will be owned by the delegatee) and move processes between cgroups in the subtree. If some controllers are present in <i>dlgt_grp/cgroup.subtree_control</i>, or the ownership of that file was passed to the delegatee, the delegatee can also control the further redistribution of the corresponding resources into the delegated subtree.</p>
<h3>Cgroups v2 delegation: nsdelegate and cgroup namespaces</h3>
<p>Starting with Linux 4.13, there is a second way to perform cgroup delegation in the cgroups v2 hierarchy. This is done by mounting or remounting the cgroup v2 filesystem with the <i>nsdelegate</i> mount option. For example, if the cgroup v2 filesystem has already been mounted, we can remount it with the <i>nsdelegate</i> option as follows: </p>
<p> mount -t cgroup2 -o remount,nsdelegate \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;none&nbsp;/sys/fs/cgroup/unified </p>
<p> The effect of this mount option is to cause cgroup namespaces to automatically become delegation boundaries. More specifically, the following restrictions apply for processes inside the cgroup namespace:</p>
<dl>
<dt>*</p>
<dd>Writes to controller interface files in the root directory of the namespace will fail with the error <code>EPERM</code>. Processes inside the cgroup namespace can still write to delegatable files in the root directory of the cgroup namespace such as <i>cgroup.procs</i> and <i>cgroup.subtree_control</i>, and can create subhierarchy underneath the root directory.</p>
<dt>*</p>
<dd>Attempts to migrate processes across the namespace boundary are denied (with the error <code>ENOENT</code>). Processes inside the cgroup namespace can still (subject to the containment rules described below) move processes between cgroups <i>within</i> the subhierarchy under the namespace root.</dl>
<p> The ability to define cgroup namespaces as delegation boundaries makes cgroup namespaces more useful. To understand why, suppose that we already have one cgroup hierarchy that has been delegated to a nonprivileged user, <i>cecilia</i>, using the older delegation technique described above. Suppose further that <i>cecilia</i> wanted to further delegate a subhierarchy under the existing delegated hierarchy. (For example, the delegated hierarchy might be associated with an unprivileged container run by <i>cecilia</i>.) Even if a cgroup namespace was employed, because both hierarchies are owned by the unprivileged user <i>cecilia</i>, the following illegitimate actions could be performed:</p>
<dl>
<dt>*</p>
<dd>A process in the inferior hierarchy could change the resource controller settings in the root directory of that hierarchy. (These resource controller settings are intended to allow control to be exercised from the <i>parent</i> cgroup; a process inside the child cgroup should not be allowed to modify them.)</p>
<dt>*</p>
<dd>A process inside the inferior hierarchy could move processes into and out of the inferior hierarchy if the cgroups in the superior hierarchy were somehow visible.</dl>
<p> Employing the <i>nsdelegate</i> mount option prevents both of these possibilities. </p>
<p> The <i>nsdelegate</i> mount option only has an effect when performed in the initial mount namespace; in other mount namespaces, the option is silently ignored. </p>
<p> <i>Note</i>: On some systems, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) automatically mounts the cgroup v2 filesystem. In order to experiment with the <i>nsdelegate</i> operation, it may be useful to boot the kernel with the following command-line options: </p>
<p> cgroup_no_v1=all systemd.legacy_systemd_cgroup_controller </p>
<p> These options cause the kernel to boot with the cgroups v1 controllers disabled (meaning that the controllers are available in the v2 hierarchy), and tells <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) not to mount and use the cgroup v2 hierarchy, so that the v2 hierarchy can be manually mounted with the desired options after boot-up.</p>
<h3>Cgroup delegation containment rules</h3>
<p>Some delegation <i>containment rules</i> ensure that the delegatee can move processes between cgroups within the delegated subtree, but can&#8217;t move processes from outside the delegated subtree into the subtree or vice versa. A nonprivileged process (i.e., the delegatee) can write the PID of a &quot;target&quot; process into a <i>cgroup.procs</i> file only if all of the following are true:</p>
<dl>
<dt>*</p>
<dd>The writer has write permission on the <i>cgroup.procs</i> file in the destination cgroup.</p>
<dt>*</p>
<dd>The writer has write permission on the <i>cgroup.procs</i> file in the nearest common ancestor of the source and destination cgroups. Note that in some cases, the nearest common ancestor may be the source or destination cgroup itself. This requirement is not enforced for cgroups v1 hierarchies, with the consequence that containment in v1 is less strict than in v2. (For example, in cgroups v1 the user that owns two distinct delegated subhierarchies can move a process between the hierarchies.)</p>
<dt>*</p>
<dd>If the cgroup v2 filesystem was mounted with the <i>nsdelegate</i> option, the writer must be able to see the source and destination cgroups from its cgroup namespace.</p>
<dt>*</p>
<dd>In cgroups v1: the effective UID of the writer (i.e., the delegatee) matches the real user ID or the saved set-user-ID of the target process. Before Linux 4.11, this requirement also applied in cgroups v2 (This was a historical requirement inherited from cgroups v1 that was later deemed unnecessary, since the other rules suffice for containment in cgroups v2.)</dl>
<p> <i>Note</i>: one consequence of these delegation containment rules is that the unprivileged delegatee can&#8217;t place the first process into the delegated subtree; instead, the delegater must place the first process (a process owned by the delegatee) into the delegated subtree.</p>
<h2>Cgroups Version 2 Thread Mode</h2>
<p>Among the restrictions imposed by cgroups v2 that were not present in cgroups v1 are the following:</p>
<dl>
<dt>*</p>
<dd><i>No thread-granularity control</i>: all of the threads of a process must be in the same cgroup.</p>
<dt>*</p>
<dd><i>No internal processes</i>: a cgroup can&#8217;t both have member processes and exercise controllers on child cgroups.</dl>
<p> Both of these restrictions were added because the lack of these restrictions had caused problems in cgroups v1. In particular, the cgroups v1 ability to allow thread-level granularity for cgroup membership made no sense for some controllers. (A notable example was the <i>memory</i> controller: since threads share an address space, it made no sense to split threads across different <i>memory</i> cgroups.) </p>
<p> Notwithstanding the initial design decision in cgroups v2, there were use cases for certain controllers, notably the <i>cpu</i> controller, for which thread-level granularity of control was meaningful and useful. To accommodate such use cases, Linux 4.14 added <i>thread mode</i> for cgroups v2. </p>
<p> Thread mode allows the following:</p>
<dl>
<dt>*</p>
<dd>The creation of <i>threaded subtrees</i> in which the threads of a process may be spread across cgroups inside the tree. (A threaded subtree may contain multiple multithreaded processes.)</p>
<dt>*</p>
<dd>The concept of <i>threaded controllers,</i> which can distribute resources across the cgroups in a threaded subtree.</p>
<dt>*</p>
<dd>A relaxation of the &quot;no internal processes rule&quot;, so that, within a threaded subtree, a cgroup can both contain member threads and exercise resource control over child cgroups.</dl>
<p> With the addition of thread mode, each nonroot cgroup now contains a new file, <i>cgroup.type</i>, that exposes, and in some circumstances can be used to change, the &quot;type&quot; of a cgroup. This file contains one of the following type values:</p>
<dl>
<dt><i>domain</i></p>
<dd>This is a normal v2 cgroup that provides process-granularity control. If a process is a member of this cgroup, then all threads of the process are (by definition) in the same cgroup. This is the default cgroup type, and provides the same behavior that was provided for cgroups in the initial cgroups v2 implementation.</p>
<dt><i>threaded</i></p>
<dd>This cgroup is a member of a threaded subtree. Threads can be added to this cgroup, and controllers can be enabled for the cgroup.</p>
<dt><i>domain threaded</i></p>
<dd>This is a domain cgroup that serves as the root of a threaded subtree. This cgroup type is also known as &quot;threaded root&quot;.</p>
<dt><i>domain invalid</i></p>
<dd>This is a cgroup inside a threaded subtree that is in an &quot;invalid&quot; state. Processes can&#8217;t be added to the cgroup, and controllers can&#8217;t be enabled for the cgroup. The only thing that can be done with this cgroup (other than deleting it) is to convert it to a <i>threaded</i> cgroup by writing the string <i>&quot;threaded&quot;</i> to the <i>cgroup.type</i> file.</p>
<dd>The rationale for the existence of this &quot;interim&quot; type during the creation of a threaded subtree (rather than the kernel simply immediately converting all cgroups under the threaded root to the type <i>threaded</i>) is to allow for possible future extensions to the thread mode model</dl>
<h3>Threaded versus domain controllers</h3>
<p>With the addition of threads mode, cgroups v2 now distinguishes two types of resource controllers:</p>
<dl>
<dt>*</p>
<dd><i>Threaded</i> controllers: these controllers support thread-granularity for resource control and can be enabled inside threaded subtrees, with the result that the corresponding controller-interface files appear inside the cgroups in the threaded subtree. As at Linux 4.19, the following controllers are threaded: <i>cpu</i>, <i>perf_event</i>, and <i>pids</i>.</p>
<dt>*</p>
<dd><i>Domain</i> controllers: these controllers support only process granularity for resource control. From the perspective of a domain controller, all threads of a process are always in the same cgroup. Domain controllers can&#8217;t be enabled inside a threaded subtree.</dl>
<h3>Creating a threaded subtree</h3>
<p>There are two pathways that lead to the creation of a threaded subtree. The first pathway proceeds as follows:</p>
<dl>
<dt>1.</p>
<dd>We write the string <i>&quot;threaded&quot;</i> to the <i>cgroup.type</i> file of a cgroup <i>y/z</i> that currently has the type <i>domain</i>. This has the following effects:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>The type of the cgroup <i>y/z</i> becomes <i>threaded</i>.</p>
<dt>*</p>
<dd>The type of the parent cgroup, <i>y</i>, becomes <i>domain threaded</i>. The parent cgroup is the root of a threaded subtree (also known as the &quot;threaded root&quot;).</p>
<dt>*</p>
<dd>All other cgroups under <i>y</i> that were not already of type <i>threaded</i> (because they were inside already existing threaded subtrees under the new threaded root) are converted to type <i>domain invalid</i>. Any subsequently created cgroups under <i>y</i> will also have the type <i>domain invalid</i>.</dl>
</dl>
<dt>2.</p>
<dd>We write the string <i>&quot;threaded&quot;</i> to each of the <i>domain invalid</i> cgroups under <i>y</i>, in order to convert them to the type <i>threaded</i>. As a consequence of this step, all threads under the threaded root now have the type <i>threaded</i> and the threaded subtree is now fully usable. The requirement to write <i>&quot;threaded&quot;</i> to each of these cgroups is somewhat cumbersome, but allows for possible future extensions to the thread-mode model.</dl>
<p> The second way of creating a threaded subtree is as follows:</p>
<dl>
<dt>1.</p>
<dd>In an existing cgroup, <i>z</i>, that currently has the type <i>domain</i>, we (1) enable one or more threaded controllers and (2) make a process a member of <i>z</i>. (These two steps can be done in either order.) This has the following consequences:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>The type of <i>z</i> becomes <i>domain threaded</i>.</p>
<dt>*</p>
<dd>All of the descendant cgroups of <i>x</i> that were not already of type <i>threaded</i> are converted to type <i>domain invalid</i>.</dl>
</dl>
<dt>2.</p>
<dd>As before, we make the threaded subtree usable by writing the string <i>&quot;threaded&quot;</i> to each of the <i>domain invalid</i> cgroups under <i>y</i>, in order to convert them to the type <i>threaded</i>.</dl>
<p> One of the consequences of the above pathways to creating a threaded subtree is that the threaded root cgroup can be a parent only to <i>threaded</i> (and <i>domain invalid</i>) cgroups. The threaded root cgroup can&#8217;t be a parent of a <i>domain</i> cgroups, and a <i>threaded</i> cgroup can&#8217;t have a sibling that is a <i>domain</i> cgroup.</p>
<h3>Using a threaded subtree</h3>
<p>Within a threaded subtree, threaded controllers can be enabled in each subgroup whose type has been changed to <i>threaded</i>; upon doing so, the corresponding controller interface files appear in the children of that cgroup. </p>
<p> A process can be moved into a threaded subtree by writing its PID to the <i>cgroup.procs</i> file in one of the cgroups inside the tree. This has the effect of making all of the threads in the process members of the corresponding cgroup and makes the process a member of the threaded subtree. The threads of the process can then be spread across the threaded subtree by writing their thread IDs (see <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)) to the <i>cgroup.threads</i> files in different cgroups inside the subtree. The threads of a process must all reside in the same threaded subtree. </p>
<p> As with writing to <i>cgroup.procs</i>, some containment rules apply when writing to the <i>cgroup.threads</i> file:</p>
<dl>
<dt>*</p>
<dd>The writer must have write permission on the cgroup.threads file in the destination cgroup.</p>
<dt>*</p>
<dd>The writer must have write permission on the <i>cgroup.procs</i> file in the common ancestor of the source and destination cgroups. (In some cases, the common ancestor may be the source or destination cgroup itself.)</p>
<dt>*</p>
<dd>The source and destination cgroups must be in the same threaded subtree. (Outside a threaded subtree, an attempt to move a thread by writing its thread ID to the <i>cgroup.threads</i> file in a different <i>domain</i> cgroup fails with the error <code>EOPNOTSUPP</code>.)</dl>
<p> The <i>cgroup.threads</i> file is present in each cgroup (including <i>domain</i> cgroups) and can be read in order to discover the set of threads that is present in the cgroup. The set of thread IDs obtained when reading this file is not guaranteed to be ordered or free of duplicates. </p>
<p> The <i>cgroup.procs</i> file in the threaded root shows the PIDs of all processes that are members of the threaded subtree. The <i>cgroup.procs</i> files in the other cgroups in the subtree are not readable. </p>
<p> Domain controllers can&#8217;t be enabled in a threaded subtree; no controller-interface files appear inside the cgroups underneath the threaded root. From the point of view of a domain controller, threaded subtrees are invisible: a multithreaded process inside a threaded subtree appears to a domain controller as a process that resides in the threaded root cgroup. </p>
<p> Within a threaded subtree, the &quot;no internal processes&quot; rule does not apply: a cgroup can both contain member processes (or thread) and exercise controllers on child cgroups.</p>
<h3>Rules for writing to cgroup.type and creating threaded subtrees</h3>
<p>A number of rules apply when writing to the <i>cgroup.type</i> file:</p>
<dl>
<dt>*</p>
<dd>Only the string <i>&quot;threaded&quot;</i> may be written. In other words, the only explicit transition that is possible is to convert a <i>domain</i> cgroup to type <i>threaded</i>.</p>
<dt>*</p>
<dd>The effect of writing <i>&quot;threaded&quot;</i> depends on the current value in <i>cgroup.type</i>, as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><i>domain</i> or <i>domain threaded</i>: start the creation of a threaded subtree (whose root is the parent of this cgroup) via the first of the pathways described above;</p>
<dt>&bull;</p>
<dd><i>domain invalid</i>: convert this cgroup (which is inside a threaded subtree) to a usable (i.e., <i>threaded</i>) state;</p>
<dt>&bull;</p>
<dd><i>threaded</i>: no effect (a &quot;no-op&quot;).</dl>
</dl>
<dt>*</p>
<dd>We can&#8217;t write to a <i>cgroup.type</i> file if the parent&#8217;s type is <i>domain invalid</i>. In other words, the cgroups of a threaded subtree must be converted to the <i>threaded</i> state in a top-down manner.</dl>
<p> There are also some constraints that must be satisfied in order to create a threaded subtree rooted at the cgroup <i>x</i>:</p>
<dl>
<dt>*</p>
<dd>There can be no member processes in the descendant cgroups of <i>x</i>. (The cgroup <i>x</i> can itself have member processes.)</p>
<dt>*</p>
<dd>No domain controllers may be enabled in <i>x</i>&#8216;s <i>cgroup.subtree_control</i> file.</dl>
<p> If any of the above constraints is violated, then an attempt to write <i>&quot;threaded&quot;</i> to a <i>cgroup.type</i> file fails with the error <code>ENOTSUP</code>.</p>
<h3>The domain threaded cgroup type</h3>
<p>According to the pathways described above, the type of a cgroup can change to <i>domain threaded</i> in either of the following cases:</p>
<dl>
<dt>*</p>
<dd>The string <i>&quot;threaded&quot;</i> is written to a child cgroup.</p>
<dt>*</p>
<dd>A threaded controller is enabled inside the cgroup and a process is made a member of the cgroup.</dl>
<p> A <i>domain threaded</i> cgroup, <i>x</i>, can revert to the type <i>domain</i> if the above conditions no longer hold true&#8212;that is, if all <i>threaded</i> child cgroups of <i>x</i> are removed and either <i>x</i> no longer has threaded controllers enabled or no longer has member processes. </p>
<p> When a <i>domain threaded</i> cgroup <i>x</i> reverts to the type <i>domain</i>:</p>
<dl>
<dt>*</p>
<dd>All <i>domain invalid</i> descendants of <i>x</i> that are not in lower-level threaded subtrees revert to the type <i>domain</i>.</p>
<dt>*</p>
<dd>The root cgroups in any lower-level threaded subtrees revert to the type <i>domain threaded</i>.</dl>
<h3>Exceptions for the root cgroup</h3>
<p>The root cgroup of the v2 hierarchy is treated exceptionally: it can be the parent of both <i>domain</i> and <i>threaded</i> cgroups. If the string <i>threaded</i> is written to the <i>cgroup.type</i> file of one of the children of the root cgroup, then</p>
<dl>
<dt>*</p>
<dd>The type of that cgroup becomes <i>threaded</i>.</p>
<dt>*</p>
<dd>The type of any descendants of that cgroup that are not part of lower-level threaded subtrees changes to <i>domain invalid</i>.</dl>
<p> Note that in this case, there is no cgroup whose type becomes <i>domain threaded</i>. (Notionally, the root cgroup can be considered as the threaded root for the cgroup whose type was changed to <i>threaded</i>.) </p>
<p> The aim of this exceptional treatment for the root cgroup is to allow a threaded cgroup that employs the <i>cpu</i> controller to be placed as high as possible in the hierarchy, so as to minimize the (small) cost of traversing the cgroup hierarchy.</p>
<h3>The cgroups v2 cpu controller and realtime threads</h3>
<p>As at Linux 4.19, the cgroups v2 <i>cpu</i> controller does not support control of realtime threads (specifically threads scheduled under any of the policies <code>SCHED_FIFO</code>, <code>SCHED_RR</code>, described <code>SCHED_DEADLINE</code>; see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)). Therefore, the <i>cpu</i> controller can be enabled in the root cgroup only if all realtime threads are in the root cgroup. (If there are realtime threads in nonroot cgroups, then a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) of the string <i>&quot;+cpu&quot;</i> to the <i>cgroup.subtree_control</i> file fails with the error <code>EINVAL</code>.) </p>
<p> On some systems, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) places certain realtime threads in nonroot cgroups in the v2 hierarchy. On such systems, these threads must first be moved to the root cgroup before the <i>cpu</i> controller can be enabled.</p>
<h2>Errors</h2>
<p>The following errors can occur for <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2):</p>
<dl>
<dt><code>EBUSY</code></p>
<dd>An attempt to mount a cgroup version 1 filesystem specified neither the <i>name=</i> option (to mount a named hierarchy) nor a controller name (or <i>all</i>).</dl>
<h2>Notes</h2>
<p>A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s cgroup memberships. A process&#8217;s cgroup memberships are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> The <code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2) <code>CLONE_INTO_CGROUP</code> flag can be used to create a child process that begins its life in a different version 2 cgroup from the parent process.</p>
<h3>/proc files</h3>
<dl>
<dt><i>/proc/cgroups</i> (since Linux 2.6.24)</p>
<dd>This file contains information about the controllers that are compiled into the kernel. An example of the contents of this file (reformatted for readability) is the following:</p>
<dd>#subsys_name hierarchy num_cgroups enabled cpuset 4 1 1 cpu 8 1 1 cpuacct 8 1 1 blkio 6 1 1 memory 3 1 1 devices 10 84 1 freezer 7 1 1 net_cls 9 1 1 perf_event 5 1 1 net_prio 9 1 1 hugetlb 0 1 0 pids 2 1 1</p>
<dd>The fields in this file are, from left to right:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The name of the controller.</p>
<dt>2.</p>
<dd>The unique ID of the cgroup hierarchy on which this controller is mounted. If multiple cgroups v1 controllers are bound to the same hierarchy, then each will show the same hierarchy ID in this field. The value in this field will be 0 if:</p>
<dl>
<dd>
<dl>
<dt>a)</p>
<dd>the controller is not mounted on a cgroups v1 hierarchy;</p>
<dt>b)</p>
<dd>the controller is bound to the cgroups v2 single unified hierarchy; or</p>
<dt>c)</p>
<dd>the controller is disabled (see below).</dl>
</dl>
<dt>3.</p>
<dd>The number of control groups in this hierarchy using this controller.</p>
<dt>4.</p>
<dd>This field contains the value 1 if this controller is enabled, or 0 if it has been disabled (via the <i>cgroup_disable</i> kernel command-line boot parameter).</dl>
</dl>
<dt><i>/proc/[pid]/cgroup</i> (since Linux 2.6.24)</p>
<dd>This file describes control groups to which the process with the corresponding PID belongs. The displayed information differs for cgroups version 1 and version 2 hierarchies.</p>
<dd>For each cgroup hierarchy of which the process is a member, there is one entry containing three colon-separated fields:</p>
<dd>hierarchy-ID:controller-list:cgroup-path</p>
<dd>For example:</p>
<dd>5:cpuacct,cpu,cpuset:/daemons</p>
<dd>The colon-separated fields are, from left to right:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>For cgroups version 1 hierarchies, this field contains a unique hierarchy ID number that can be matched to a hierarchy ID in <i>/proc/cgroups</i>. For the cgroups version 2 hierarchy, this field contains the value 0.</p>
<dt>2.</p>
<dd>For cgroups version 1 hierarchies, this field contains a comma-separated list of the controllers bound to the hierarchy. For the cgroups version 2 hierarchy, this field is empty.</p>
<dt>3.</p>
<dd>This field contains the pathname of the control group in the hierarchy to which the process belongs. This pathname is relative to the mount point of the hierarchy.</dl>
</dl>
</dl>
<h3>/sys/kernel/cgroup files</h3>
<dl>
<dt><i>/sys/kernel/cgroup/delegate</i> (since Linux 4.15)</p>
<dd>This file exports a list of the cgroups v2 files (one per line) that are delegatable (i.e., whose ownership should be changed to the user ID of the delegatee). In the future, the set of delegatable files may change or grow, and this file provides a way for the kernel to inform user-space applications of which files must be delegated. As at Linux 4.15, one sees the following when inspecting this file:</p>
<dd>$ <code>cat /sys/kernel/cgroup/delegate</code> cgroup.procs cgroup.subtree_control cgroup.threads</p>
<dt><i>/sys/kernel/cgroup/features</i> (since Linux 4.15)</p>
<dd>Over time, the set of cgroups v2 features that are provided by the kernel may change or grow, or some features may not be enabled by default. This file provides a way for user-space applications to discover what features the running kernel supports and has enabled. Features are listed one per line:</p>
<dd>$ <code>cat /sys/kernel/cgroup/features</code> nsdelegate memory_localevents</p>
<dd>The entries that can appear in this file are:</p>
<dl>
<dd>
<dl>
<dt><i>memory_localevents</i> (since Linux 5.2)</p>
<dd>The kernel supports the <i>memory_localevents</i> mount option.</p>
<dt><i>nsdelegate</i> (since Linux 4.15)</p>
<dd>The kernel supports the <i>nsdelegate</i> mount option.</dl>
</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-prlimit/">prlimit</a></code>(1), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemd-cgls/">systemd-cgls</a></code>(1), <code><a href="/docs/linux/man/1-systemd-cgtop/">systemd-cgtop</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-ioprio_set/">ioprio_set</a></code>(2), <code><a href="/docs/linux/man/2-perf_event_open/">perf_event_open</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/7-cgroup_namespaces/">cgroup_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7) </p>
<p> The kernel source file <i>Documentation/admin-guide/cgroup-v2.rst</i>.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
