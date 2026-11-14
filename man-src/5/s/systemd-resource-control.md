---
title: "systemd-resource-control(5)"
name: "systemd-resource-control"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-resource-control/"
description: "systemd.resource-control – Resource control unit settings"
---

<p>systemd.resource-control &#8211; Resource control unit settings</p>
<h2>Synopsis</h2>
<p><i>slice</i>.slice, <i>scope</i>.scope, <i>service</i>.service, <i>socket</i>.socket, <i>mount</i>.mount, <i>swap</i>.swap</p>
<h2>Description</h2>
<p>Unit configuration files for services, slices, scopes, sockets, mount points, and swap devices share a subset of configuration options for resource control of spawned processes. Internally, this relies on the Linux Control Groups (cgroups) kernel concept for organizing processes in a hierarchical tree of named groups for the purpose of resource management. </p>
<p> This man page lists the configuration options shared by those six unit types. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files, and <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), and <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5) for more information on the specific unit configuration files. The resource control configuration options are configured in the [Slice], [Scope], [Service], [Socket], [Mount], or [Swap] sections, depending on the unit type. </p>
<p> In addition, options which control resources available to programs <i>executed</i> by systemd are listed in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5). Those options complement options listed here. </p>
<p> See the m[blue]<code>New Control Group Interfaces</code>m[]<font SIZE="-2">[1]</font> for an introduction on how to make use of resource control APIs from programs.</p>
<h3>Setting resource controls for a group of related units</h3>
<p>As described in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), the settings listed here may be set through the main file of a unit and drop-in snippets in *.d/ directories. The list of directories searched for drop-ins includes names formed by repeatedly truncating the unit name after all dashes. This is particularly convenient to set resource limits for a group of units with similar names. </p>
<p> For example, every user gets their own slice user-<i>nnn</i>.slice. Drop-ins with local configuration that affect user 1000 may be placed in /etc/systemd/system/user-1000.slice, /etc/systemd/system/user-1000.slice.d/*.conf, but also /etc/systemd/system/user-.slice.d/*.conf. This last directory applies to all user slices.</p>
<h2>Implicit Dependencies</h2>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; Units with the <i>Slice=</i> setting set automatically acquire <i>Requires=</i> and <i>After=</i> dependencies on the specified slice unit.</dl>
<h2>Unified And Legacy Control Group Hierarchies</h2>
<p>The unified control group hierarchy is the new version of kernel control group interface, see m[blue]<code>Control Groups v2</code>m[]<font SIZE="-2">[2]</font>. Depending on the resource type, there are differences in resource control capabilities. Also, because of interface changes, some resource types have separate set of options on the unified hierarchy. </p>
<p> CPU</p>
<dl>
<dd><i>CPUWeight=</i> and <i>StartupCPUWeight=</i> replace <i>CPUShares=</i> and <i>StartupCPUShares=</i>, respectively. </p>
<p> The &quot;cpuacct&quot; controller does not exist separately on the unified hierarchy.</dl>
<p> Memory</p>
<dl>
<dd><i>MemoryMax=</i> replaces <i>MemoryLimit=</i>. <i>MemoryLow=</i> and <i>MemoryHigh=</i> are effective only on unified hierarchy.</dl>
<p> IO</p>
<dl>
<dd>&quot;IO&quot;-prefixed settings are a superset of and replace &quot;BlockIO&quot;-prefixed ones. On unified hierarchy, IO resource control also applies to buffered writes.</dl>
<p> To ease the transition, there is best-effort translation between the two versions of settings. For each controller, if any of the settings for the unified hierarchy are present, all settings for the legacy hierarchy are ignored. If the resulting settings are for the other type of hierarchy, the configurations are translated before application. </p>
<p> Legacy control group hierarchy (see m[blue]<code>Control Groups version 1</code>m[]<font SIZE="-2">[3]</font>), also called cgroup-v1, doesn&#8217;t allow safe delegation of controllers to unprivileged processes. If the system uses the legacy control group hierarchy, resource control is disabled for the systemd user instance, see <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</p>
<h2>Options</h2>
<p>Units of the types listed above can have settings for resource control configuration: </p>
<p> <i>CPUAccounting=</i></p>
<dl>
<dd>Turn on CPU usage accounting for this unit. Takes a boolean argument. Note that turning on CPU accounting for one unit will also implicitly turn it on for all units contained in the same slice and for all its parent slices and the units contained therein. The system default for this setting may be controlled with <i>DefaultCPUAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>CPUWeight=</i><i>weight</i>, <i>StartupCPUWeight=</i><i>weight</i></p>
<dl>
<dd>Assign the specified CPU time weight to the processes executed, if the unified control group hierarchy is used on the system. These options take an integer value and control the &quot;cpu.weight&quot; control group attribute. The allowed range is 1 to 10000. Defaults to 100. For details about this control group attribute, see m[blue]<code>Control Groups v2</code>m[]<font SIZE="-2">[2]</font> and m[blue]<code>CFS Scheduler</code>m[]<font SIZE="-2">[4]</font>. The available CPU time is split up among all units within one slice relative to their CPU time weight. A higher weight means more CPU time, a lower weight means less. </p>
<p> While <i>StartupCPUWeight=</i> only applies to the startup phase of the system, <i>CPUWeight=</i> applies to normal runtime of the system, and if the former is not set also to the startup phase. Using <i>StartupCPUWeight=</i> allows prioritizing specific services at boot-up differently than during normal runtime. </p>
<p> These settings replace <i>CPUShares=</i> and <i>StartupCPUShares=</i>.</dl>
<p> <i>CPUQuota=</i></p>
<dl>
<dd>Assign the specified CPU time quota to the processes executed. Takes a percentage value, suffixed with &quot;%&quot;. The percentage specifies how much CPU time the unit shall get at maximum, relative to the total CPU time available on one CPU. Use values &gt; 100% for allotting CPU time on more than one CPU. This controls the &quot;cpu.max&quot; attribute on the unified control group hierarchy and &quot;cpu.cfs_quota_us&quot; on legacy. For details about these control group attributes, see m[blue]<code>Control Groups v2</code>m[]<font SIZE="-2">[2]</font> and m[blue]<code>sched-bwc.txt</code>m[]<font SIZE="-2">[5]</font>. Setting <i>CPUQuota=</i> to an empty value unsets the quota. </p>
<p> Example: <i>CPUQuota=20%</i> ensures that the executed processes will never get more than 20% CPU time on one CPU.</dl>
<p> <i>CPUQuotaPeriodSec=</i></p>
<dl>
<dd>Assign the duration over which the CPU time quota specified by <i>CPUQuota=</i> is measured. Takes a time duration value in seconds, with an optional suffix such as &quot;ms&quot; for milliseconds (or &quot;s&quot; for seconds.) The default setting is 100ms. The period is clamped to the range supported by the kernel, which is [1ms, 1000ms]. Additionally, the period is adjusted up so that the quota interval is also at least 1ms. Setting <i>CPUQuotaPeriodSec=</i> to an empty value resets it to the default. </p>
<p> This controls the second field of &quot;cpu.max&quot; attribute on the unified control group hierarchy and &quot;cpu.cfs_period_us&quot; on legacy. For details about these control group attributes, see m[blue]<code>Control Groups v2</code>m[]<font SIZE="-2">[2]</font> and m[blue]<code>CFS Scheduler</code>m[]<font SIZE="-2">[4]</font>. </p>
<p> Example: <i>CPUQuotaPeriodSec=10ms</i> to request that the CPU quota is measured in periods of 10ms.</dl>
<p> <i>AllowedCPUs=</i></p>
<dl>
<dd>Restrict processes to be executed on specific CPUs. Takes a list of CPU indices or ranges separated by either whitespace or commas. CPU ranges are specified by the lower and upper CPU indices separated by a dash. </p>
<p> Setting <i>AllowedCPUs=</i> doesn&#8217;t guarantee that all of the CPUs will be used by the processes as it may be limited by parent units. The effective configuration is reported as <i>EffectiveCPUs=</i>. </p>
<p> This setting is supported only with the unified control group hierarchy.</dl>
<p> <i>AllowedMemoryNodes=</i></p>
<dl>
<dd>Restrict processes to be executed on specific memory NUMA nodes. Takes a list of memory NUMA nodes indices or ranges separated by either whitespace or commas. Memory NUMA nodes ranges are specified by the lower and upper NUMA nodes indices separated by a dash. </p>
<p> Setting <i>AllowedMemoryNodes=</i> doesn&#8217;t guarantee that all of the memory NUMA nodes will be used by the processes as it may be limited by parent units. The effective configuration is reported as <i>EffectiveMemoryNodes=</i>. </p>
<p> This setting is supported only with the unified control group hierarchy.</dl>
<p> <i>MemoryAccounting=</i></p>
<dl>
<dd>Turn on process and kernel memory accounting for this unit. Takes a boolean argument. Note that turning on memory accounting for one unit will also implicitly turn it on for all units contained in the same slice and for all its parent slices and the units contained therein. The system default for this setting may be controlled with <i>DefaultMemoryAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>MemoryMin=</i><i>bytes</i>, <i>MemoryLow=</i><i>bytes</i></p>
<dl>
<dd>Specify the memory usage protection of the executed processes in this unit. When reclaiming memory, the unit is treated as if it was using less memory resulting in memory to be preferentially reclaimed from unprotected units. Using <i>MemoryLow=</i> results in a weaker protection where memory may still be reclaimed to avoid invoking the OOM killer in case there is no other reclaimable memory. </p>
<p> For a protection to be effective, it is generally required to set a corresponding allocation on all ancestors, which is then distributed between children (with the exception of the root slice). Any <i>MemoryMin=</i> or <i>MemoryLow=</i> allocation that is not explicitly distributed to specific children is used to create a shared protection for all children. As this is a shared protection, the children will freely compete for the memory. </p>
<p> Takes a memory size in bytes. If the value is suffixed with K, M, G or T, the specified memory size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. Alternatively, a percentage value may be specified, which is taken relative to the installed physical memory on the system. If assigned the special value &quot;infinity&quot;, all available memory is protected, which may be useful in order to always inherit all of the protection afforded by ancestors. This controls the &quot;memory.min&quot; or &quot;memory.low&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Memory Interface Files</code>m[]<font SIZE="-2">[6]</font>. </p>
<p> This setting is supported only if the unified control group hierarchy is used and disables <i>MemoryLimit=</i>. </p>
<p> Units may have their children use a default &quot;memory.min&quot; or &quot;memory.low&quot; value by specifying <i>DefaultMemoryMin=</i> or <i>DefaultMemoryLow=</i>, which has the same semantics as <i>MemoryMin=</i> and <i>MemoryLow=</i>. This setting does not affect &quot;memory.min&quot; or &quot;memory.low&quot; in the unit itself. Using it to set a default child allocation is only useful on kernels older than 5.7, which do not support the &quot;memory_recursiveprot&quot; cgroup2 mount option.</dl>
<p> <i>MemoryHigh=</i><i>bytes</i></p>
<dl>
<dd>Specify the throttling limit on memory usage of the executed processes in this unit. Memory usage may go above the limit if unavoidable, but the processes are heavily slowed down and memory is taken away aggressively in such cases. This is the main mechanism to control memory usage of a unit. </p>
<p> Takes a memory size in bytes. If the value is suffixed with K, M, G or T, the specified memory size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. Alternatively, a percentage value may be specified, which is taken relative to the installed physical memory on the system. If assigned the special value &quot;infinity&quot;, no memory throttling is applied. This controls the &quot;memory.high&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Memory Interface Files</code>m[]<font SIZE="-2">[6]</font>. </p>
<p> This setting is supported only if the unified control group hierarchy is used and disables <i>MemoryLimit=</i>.</dl>
<p> <i>MemoryMax=</i><i>bytes</i></p>
<dl>
<dd>Specify the absolute limit on memory usage of the executed processes in this unit. If memory usage cannot be contained under the limit, out-of-memory killer is invoked inside the unit. It is recommended to use <i>MemoryHigh=</i> as the main control mechanism and use <i>MemoryMax=</i> as the last line of defense. </p>
<p> Takes a memory size in bytes. If the value is suffixed with K, M, G or T, the specified memory size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. Alternatively, a percentage value may be specified, which is taken relative to the installed physical memory on the system. If assigned the special value &quot;infinity&quot;, no memory limit is applied. This controls the &quot;memory.max&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Memory Interface Files</code>m[]<font SIZE="-2">[6]</font>. </p>
<p> This setting replaces <i>MemoryLimit=</i>.</dl>
<p> <i>MemorySwapMax=</i><i>bytes</i></p>
<dl>
<dd>Specify the absolute limit on swap usage of the executed processes in this unit. </p>
<p> Takes a swap size in bytes. If the value is suffixed with K, M, G or T, the specified swap size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. If assigned the special value &quot;infinity&quot;, no swap limit is applied. This controls the &quot;memory.swap.max&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Memory Interface Files</code>m[]<font SIZE="-2">[6]</font>. </p>
<p> This setting is supported only if the unified control group hierarchy is used and disables <i>MemoryLimit=</i>.</dl>
<p> <i>TasksAccounting=</i></p>
<dl>
<dd>Turn on task accounting for this unit. Takes a boolean argument. If enabled, the system manager will keep track of the number of tasks in the unit. The number of tasks accounted this way includes both kernel threads and userspace processes, with each thread counting individually. Note that turning on tasks accounting for one unit will also implicitly turn it on for all units contained in the same slice and for all its parent slices and the units contained therein. The system default for this setting may be controlled with <i>DefaultTasksAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>TasksMax=</i><i>N</i></p>
<dl>
<dd>Specify the maximum number of tasks that may be created in the unit. This ensures that the number of tasks accounted for the unit (see above) stays below a specific limit. This either takes an absolute number of tasks or a percentage value that is taken relative to the configured maximum number of tasks on the system. If assigned the special value &quot;infinity&quot;, no tasks limit is applied. This controls the &quot;pids.max&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Process Number Controller</code>m[]<font SIZE="-2">[7]</font>. </p>
<p> The system default for this setting may be controlled with <i>DefaultTasksMax=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>IOAccounting=</i></p>
<dl>
<dd>Turn on Block I/O accounting for this unit, if the unified control group hierarchy is used on the system. Takes a boolean argument. Note that turning on block I/O accounting for one unit will also implicitly turn it on for all units contained in the same slice and all for its parent slices and the units contained therein. The system default for this setting may be controlled with <i>DefaultIOAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5). </p>
<p> This setting replaces <i>BlockIOAccounting=</i> and disables settings prefixed with <i>BlockIO</i> or <i>StartupBlockIO</i>.</dl>
<p> <i>IOWeight=</i><i>weight</i>, <i>StartupIOWeight=</i><i>weight</i></p>
<dl>
<dd>Set the default overall block I/O weight for the executed processes, if the unified control group hierarchy is used on the system. Takes a single weight value (between 1 and 10000) to set the default block I/O weight. This controls the &quot;io.weight&quot; control group attribute, which defaults to 100. For details about this control group attribute, see m[blue]<code>IO Interface Files</code>m[]<font SIZE="-2">[8]</font>. The available I/O bandwidth is split up among all units within one slice relative to their block I/O weight. A higher weight means more I/O bandwidth, a lower weight means less. </p>
<p> While <i>StartupIOWeight=</i> only applies to the startup phase of the system, <i>IOWeight=</i> applies to the later runtime of the system, and if the former is not set also to the startup phase. This allows prioritizing specific services at boot-up differently than during runtime. </p>
<p> These settings replace <i>BlockIOWeight=</i> and <i>StartupBlockIOWeight=</i> and disable settings prefixed with <i>BlockIO</i> or <i>StartupBlockIO</i>.</dl>
<p> <i>IODeviceWeight=</i><i>device</i><i> </i><i>weight</i></p>
<dl>
<dd>Set the per-device overall block I/O weight for the executed processes, if the unified control group hierarchy is used on the system. Takes a space-separated pair of a file path and a weight value to specify the device specific weight value, between 1 and 10000. (Example: &quot;/dev/sda 1000&quot;). The file path may be specified as path to a block device node or as any other file, in which case the backing block device of the file system of the file is determined. This controls the &quot;io.weight&quot; control group attribute, which defaults to 100. Use this option multiple times to set weights for multiple devices. For details about this control group attribute, see m[blue]<code>IO Interface Files</code>m[]<font SIZE="-2">[8]</font>. </p>
<p> This setting replaces <i>BlockIODeviceWeight=</i> and disables settings prefixed with <i>BlockIO</i> or <i>StartupBlockIO</i>. </p>
<p> The specified device node should reference a block device that has an I/O scheduler associated, i.e. should not refer to partition or loopback block devices, but to the originating, physical device. When a path to a regular file or directory is specified it is attempted to discover the correct originating device backing the file system of the specified path. This works correctly only for simpler cases, where the file system is directly placed on a partition or physical block device, or where simple 1:1 encryption using dm-crypt/LUKS is used. This discovery does not cover complex storage and in particular RAID and volume management storage devices.</dl>
<p> <i>IOReadBandwidthMax=</i><i>device</i><i> </i><i>bytes</i>, <i>IOWriteBandwidthMax=</i><i>device</i><i> </i><i>bytes</i></p>
<dl>
<dd>Set the per-device overall block I/O bandwidth maximum limit for the executed processes, if the unified control group hierarchy is used on the system. This limit is not work-conserving and the executed processes are not allowed to use more even if the device has idle capacity. Takes a space-separated pair of a file path and a bandwidth value (in bytes per second) to specify the device specific bandwidth. The file path may be a path to a block device node, or as any other file in which case the backing block device of the file system of the file is used. If the bandwidth is suffixed with K, M, G, or T, the specified bandwidth is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes, respectively, to the base of 1000. (Example: &quot;/dev/disk/by-path/pci-0000:00:1f.2-scsi-0:0:0:0 5M&quot;). This controls the &quot;io.max&quot; control group attributes. Use this option multiple times to set bandwidth limits for multiple devices. For details about this control group attribute, see m[blue]<code>IO Interface Files</code>m[]<font SIZE="-2">[8]</font>. </p>
<p> These settings replace <i>BlockIOReadBandwidth=</i> and <i>BlockIOWriteBandwidth=</i> and disable settings prefixed with <i>BlockIO</i> or <i>StartupBlockIO</i>. </p>
<p> Similar restrictions on block device discovery as for <i>IODeviceWeight=</i> apply, see above.</dl>
<p> <i>IOReadIOPSMax=</i><i>device</i><i> </i><i>IOPS</i>, <i>IOWriteIOPSMax=</i><i>device</i><i> </i><i>IOPS</i></p>
<dl>
<dd>Set the per-device overall block I/O IOs-Per-Second maximum limit for the executed processes, if the unified control group hierarchy is used on the system. This limit is not work-conserving and the executed processes are not allowed to use more even if the device has idle capacity. Takes a space-separated pair of a file path and an IOPS value to specify the device specific IOPS. The file path may be a path to a block device node, or as any other file in which case the backing block device of the file system of the file is used. If the IOPS is suffixed with K, M, G, or T, the specified IOPS is parsed as KiloIOPS, MegaIOPS, GigaIOPS, or TeraIOPS, respectively, to the base of 1000. (Example: &quot;/dev/disk/by-path/pci-0000:00:1f.2-scsi-0:0:0:0 1K&quot;). This controls the &quot;io.max&quot; control group attributes. Use this option multiple times to set IOPS limits for multiple devices. For details about this control group attribute, see m[blue]<code>IO Interface Files</code>m[]<font SIZE="-2">[8]</font>. </p>
<p> These settings are supported only if the unified control group hierarchy is used and disable settings prefixed with <i>BlockIO</i> or <i>StartupBlockIO</i>. </p>
<p> Similar restrictions on block device discovery as for <i>IODeviceWeight=</i> apply, see above.</dl>
<p> <i>IODeviceLatencyTargetSec=</i><i>device</i><i> </i><i>target</i></p>
<dl>
<dd>Set the per-device average target I/O latency for the executed processes, if the unified control group hierarchy is used on the system. Takes a file path and a timespan separated by a space to specify the device specific latency target. (Example: &quot;/dev/sda 25ms&quot;). The file path may be specified as path to a block device node or as any other file, in which case the backing block device of the file system of the file is determined. This controls the &quot;io.latency&quot; control group attribute. Use this option multiple times to set latency target for multiple devices. For details about this control group attribute, see m[blue]<code>IO Interface Files</code>m[]<font SIZE="-2">[8]</font>. </p>
<p> Implies &quot;IOAccounting=yes&quot;. </p>
<p> These settings are supported only if the unified control group hierarchy is used. </p>
<p> Similar restrictions on block device discovery as for <i>IODeviceWeight=</i> apply, see above.</dl>
<p> <i>IPAccounting=</i></p>
<dl>
<dd>Takes a boolean argument. If true, turns on IPv4 and IPv6 network traffic accounting for packets sent or received by the unit. When this option is turned on, all IPv4 and IPv6 sockets created by any process of the unit are accounted for. </p>
<p> When this option is used in socket units, it applies to all IPv4 and IPv6 sockets associated with it (including both listening and connection sockets where this applies). Note that for socket-activated services, this configuration setting and the accounting data of the service unit and the socket unit are kept separate, and displayed separately. No propagation of the setting and the collected statistics is done, in either direction. Moreover, any traffic sent or received on any of the socket unit&#8217;s sockets is accounted to the socket unit &#8212; and never to the service unit it might have activated, even if the socket is used by it. </p>
<p> The system default for this setting may be controlled with <i>DefaultIPAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5).</dl>
<p> <i>IPAddressAllow=</i><i>ADDRESS[/PREFIXLENGTH]&#8230;</i>, <i>IPAddressDeny=</i><i>ADDRESS[/PREFIXLENGTH]&#8230;</i></p>
<dl>
<dd>Turn on network traffic filtering for IP packets sent and received over <code>AF_INET</code> and <code>AF_INET6</code> sockets. Both directives take a space separated list of IPv4 or IPv6 addresses, each optionally suffixed with an address prefix length in bits after a &quot;/&quot; character. If the suffix is omitted, the address is considered a host address, i.e. the filter covers the whole address (32 bits for IPv4, 128 bits for IPv6). </p>
<p> The access lists configured with this option are applied to all sockets created by processes of this unit (or in the case of socket units, associated with it). The lists are implicitly combined with any lists configured for any of the parent slice units this unit might be a member of. By default both access lists are empty. Both ingress and egress traffic is filtered by these settings. In case of ingress traffic the source IP address is checked against these access lists, in case of egress traffic the destination IP address is checked. The following rules are applied in turn: </p>
<dl>
<dd>&bull; Access is granted when the checked IP address matches an entry in the <i>IPAddressAllow=</i> list.</dl>
<dl>
<dd>&bull; Otherwise, access is denied when the checked IP address matches an entry in the <i>IPAddressDeny=</i> list.</dl>
<dl>
<dd>&bull; Otherwise, access is granted.</dl>
<p> In order to implement an allow-listing IP firewall, it is recommended to use a <i>IPAddressDeny=</i><code>any</code> setting on an upper-level slice unit (such as the root slice -.slice or the slice containing all system services system.slice &#8211; see <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details on these slice units), plus individual per-service <i>IPAddressAllow=</i> lines permitting network access to relevant services, and only them. </p>
<p> Note that for socket-activated services, the IP access list configured on the socket unit applies to all sockets associated with it directly, but not to any sockets created by the ultimately activated services for it. Conversely, the IP access list configured for the service is not applied to any sockets passed into the service via socket activation. Thus, it is usually a good idea to replicate the IP access lists on both the socket and the service unit. Nevertheless, it may make sense to maintain one list more open and the other one more restricted, depending on the usecase. </p>
<p> If these settings are used multiple times in the same unit the specified lists are combined. If an empty string is assigned to these settings the specific access list is reset and all previous settings undone. </p>
<p> In place of explicit IPv4 or IPv6 address and prefix length specifications a small set of symbolic names may be used. The following names are defined: </p>
<p> <code>Table 1. Special address/network names</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Symbolic Name </code></td>
<td><code> Definition </code></td>
<td><code> Meaning </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>any</code> </td>
<td> 0.0.0.0/0 ::/0 </td>
<td> Any host
</td>
</tr>
<tr VALIGN=top>
<td> <code>localhost</code> </td>
<td> 127.0.0.0/8 ::1/128 </td>
<td> All addresses on the local loopback
</td>
</tr>
<tr VALIGN=top>
<td> <code>link-local</code> </td>
<td> 169.254.0.0/16 fe80::/64 </td>
<td> All link-local IP addresses
</td>
</tr>
<tr VALIGN=top>
<td> <code>multicast</code> </td>
<td> 224.0.0.0/4 ff00::/8 </td>
<td> All IP multicasting addresses
</td>
</tr>
</table>
<p> Note that these settings might not be supported on some systems (for example if eBPF control group support is not enabled in the underlying kernel or container manager). These settings will have no effect in that case. If compatibility with such systems is desired it is hence recommended to not exclusively rely on them for IP security.</dl>
<p> <i>IPIngressFilterPath=</i><i>BPF_FS_PROGRAM_PATH</i>, <i>IPEgressFilterPath=</i><i>BPF_FS_PROGRAM_PATH</i></p>
<dl>
<dd>Add custom network traffic filters implemented as BPF programs, applying to all IP packets sent and received over <code>AF_INET</code> and <code>AF_INET6</code> sockets. Takes an absolute path to a pinned BPF program in the BPF virtual filesystem (/sys/fs/bpf/). </p>
<p> The filters configured with this option are applied to all sockets created by processes of this unit (or in the case of socket units, associated with it). The filters are loaded in addition to filters any of the parent slice units this unit might be a member of as well as any <i>IPAddressAllow=</i> and <i>IPAddressDeny=</i> filters in any of these units. By default there are no filters specified. </p>
<p> If these settings are used multiple times in the same unit all the specified programs are attached. If an empty string is assigned to these settings the program list is reset and all previous specified programs ignored. </p>
<p> If the path <i>BPF_FS_PROGRAM_PATH</i> in <i>IPIngressFilterPath=</i> assignment is already being handled by <i>BPFProgram=</i> ingress hook, e.g. <i>BPFProgram=</i><code>ingress</code>:<i>BPF_FS_PROGRAM_PATH</i>, the assignment will be still considered valid and the program will be attached to a cgroup. Same for <i>IPEgressFilterPath=</i> path and <code>egress</code> hook. </p>
<p> Note that for socket-activated services, the IP filter programs configured on the socket unit apply to all sockets associated with it directly, but not to any sockets created by the ultimately activated services for it. Conversely, the IP filter programs configured for the service are not applied to any sockets passed into the service via socket activation. Thus, it is usually a good idea, to replicate the IP filter programs on both the socket and the service unit, however it often makes sense to maintain one configuration more open and the other one more restricted, depending on the usecase. </p>
<p> Note that these settings might not be supported on some systems (for example if eBPF control group support is not enabled in the underlying kernel or container manager). These settings will fail the service in that case. If compatibility with such systems is desired it is hence recommended to attach your filter manually (requires <i>Delegate=</i><code>yes</code>) instead of using this setting.</dl>
<p> <i>BPFProgram=</i><i>type</i><i></i><code>:</code><i>program-path</i></p>
<dl>
<dd>Add a custom cgroup BPF program. </p>
<p> <i>BPFProgram=</i> allows attaching BPF hooks to the cgroup of a systemd unit. (This generalizes the functionality exposed via <i>IPEgressFilterPath=</i> for egress and <i>IPIngressFilterPath=</i> for ingress.) Cgroup-bpf hooks in the form of BPF programs loaded to the BPF filesystem are attached with cgroup-bpf attach flags determined by the unit. For details about attachment types and flags see m[blue]<code><a rel="nofollow" href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/bpf.h">https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/include/uapi/linux/bpf.h</a></code>m[]. For general BPF documentation please refer to m[blue]<code><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/bpf/index.html">https://www.kernel.org/doc/html/latest/bpf/index.html</a></code>m[]. </p>
<p> The specification of BPF program consists of a <i>type</i> followed by a <i>program-path</i> with &quot;:&quot; as the separator: <i>type</i><code>:</code><i>program-path</i>. </p>
<p> <i>type</i> is the string name of BPF attach type also used in <code>bpftool</code>. <i>type</i> can be one of <code>egress</code>, <code>ingress</code>, <code>sock_create</code>, <code>sock_ops</code>, <code>device</code>, <code>bind4</code>, <code>bind6</code>, <code>connect4</code>, <code>connect6</code>, <code>post_bind4</code>, <code>post_bind6</code>, <code>sendmsg4</code>, <code>sendmsg6</code>, <code>sysctl</code>, <code>recvmsg4</code>, <code>recvmsg6</code>, <code>getsockopt</code>, <code>setsockopt</code>. </p>
<p> Setting <i>BPFProgram=</i> to an empty value makes previous assignments ineffective. </p>
<p> Multiple assignments of the same <i>type</i>:<i>program-path</i> value have the same effect as a single assignment: the program with the path <i>program-path</i> will be attached to cgroup hook <i>type</i> just once. </p>
<p> If BPF <code>egress</code> pinned to <i>program-path</i> path is already being handled by <i>IPEgressFilterPath=</i>, <i>BPFProgram=</i> assignment will be considered valid and <i>BPFProgram=</i> will be attached to a cgroup. Similarly for <code>ingress</code> hook and <i>IPIngressFilterPath=</i> assignment. </p>
<p> BPF programs passed with <i>BPFProgram=</i> are attached to the cgroup of a unit with BPF attach flag <code>multi</code>, that allows further attachments of the same <i>type</i> within cgroup hierarchy topped by the unit cgroup. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>BPFProgram=egress:/sys/fs/bpf/egress-hook
BPFProgram=bind6:/sys/fs/bpf/sock-addr-hook</pre>
</dl>
</dl>
<p> <i>SocketBindAllow=</i><i>bind-rule</i>, <i>SocketBindDeny=</i><i>bind-rule</i></p>
<dl>
<dd>Allow or deny binding a socket address to a socket by matching it with the <i>bind-rule</i> and applying a corresponding action if there is a match. </p>
<p> <i>bind-rule</i> describes socket properties such as <i>address-family</i>, <i>transport-protocol</i> and <i>ip-ports</i>. </p>
<p> <i>bind-rule</i> := { [<i>address-family</i><code>:</code>][<i>transport-protocol</i><code>:</code>][<i>ip-ports</i>] | <code>any</code> } </p>
<p> <i>address-family</i> := { <code>ipv4</code> | <code>ipv6</code> } </p>
<p> <i>transport-protocol</i> := { <code>tcp</code> | <code>udp</code> } </p>
<p> <i>ip-ports</i> := { <i>ip-port</i> | <i>ip-port-range</i> } </p>
<p> An optional <i>address-family</i> expects <code>ipv4</code> or <code>ipv6</code> values. If not specified, a rule will be matched for both IPv4 and IPv6 addresses and applied depending on other socket fields, e.g. <i>transport-protocol</i>, <i>ip-port</i>. </p>
<p> An optional <i>transport-protocol</i> expects <code>tcp</code> or <code>udp</code> transport protocol names. If not specified, a rule will be matched for any transport protocol. </p>
<p> An optional <i>ip-port</i> value must lie within 1&#8230;65535 interval inclusively, i.e. dynamic port <code>0</code> is not allowed. A range of sequential ports is described by <i>ip-port-range</i> := <i>ip-port-low</i><code>&#8211;</code><i>ip-port-high</i>, where <i>ip-port-low</i> is smaller than or equal to <i>ip-port-high</i> and both are within 1&#8230;65535 inclusively. </p>
<p> A special value <code>any</code> can be used to apply a rule to any address family, transport protocol and any port with a positive value. </p>
<p> To allow multiple rules assign <i>SocketBindAllow=</i> or <i>SocketBindDeny=</i> multiple times. To clear the existing assignments pass an empty <i>SocketBindAllow=</i> or <i>SocketBindDeny=</i> assignment. </p>
<p> For each of <i>SocketBindAllow=</i> and <i>SocketBindDeny=</i>, maximum allowed number of assignments is <code>128</code>. </p>
<dl>
<dd>&bull; Binding to a socket is allowed when a socket address matches an entry in the <i>SocketBindAllow=</i> list.</dl>
<dl>
<dd>&bull; Otherwise, binding is denied when the socket address matches an entry in the <i>SocketBindDeny=</i> list.</dl>
<dl>
<dd>&bull; Otherwise, binding is allowed.</dl>
<p> The feature is implemented with <code>cgroup/bind4</code> and <code>cgroup/bind6</code> cgroup-bpf hooks. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>...
# Allow binding IPv6 socket addresses with a port greater than or equal to 10000.
[Service]
SocketBindAllow=ipv6:10000-65535
SocketBindDeny=any
...
# Allow binding IPv4 and IPv6 socket addresses with 1234 and 4321 ports.
[Service]
SocketBindAllow=1234
SocketBindAllow=4321
SocketBindDeny=any
...
# Deny binding IPv6 socket addresses.
[Service]
SocketBindDeny=ipv6
...
# Deny binding IPv4 and IPv6 socket addresses.
[Service]
SocketBindDeny=any
...
# Allow binding only over TCP
[Service]
SocketBindAllow=tcp
SocketBindDeny=any
...
# Allow binding only over IPv6/TCP
[Service]
SocketBindAllow=ipv6:tcp
SocketBindDeny=any
...
# Allow binding ports within 10000-65535 range over IPv4/UDP.
[Service]
SocketBindAllow=ipv4:udp:10000-65535
SocketBindDeny=any
...</pre>
</dl>
</dl>
<p> <i>DeviceAllow=</i></p>
<dl>
<dd>Control access to specific device nodes by the executed processes. Takes two space-separated strings: a device node specifier followed by a combination of <code>r</code>, <code>w</code>, <code>m</code> to control <i>r</i>eading, <i>w</i>riting, or creation of the specific device node(s) by the unit (<i>m</i>knod), respectively. On cgroup-v1 this controls the &quot;devices.allow&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Device Whitelist Controller</code>m[]<font SIZE="-2">[9]</font>. In the unified cgroup hierarchy this functionality is implemented using eBPF filtering. </p>
<p> The device node specifier is either a path to a device node in the file system, starting with /dev/, or a string starting with either &quot;char-&quot; or &quot;block-&quot; followed by a device group name, as listed in /proc/devices. The latter is useful to allow-list all current and future devices belonging to a specific device group at once. The device group is matched according to filename globbing rules, you may hence use the &quot;*&quot; and &quot;?&quot; wildcards. (Note that such globbing wildcards are not available for device node path specifications!) In order to match device nodes by numeric major/minor, use device node paths in the /dev/char/ and /dev/block/ directories. However, matching devices by major/minor is generally not recommended as assignments are neither stable nor portable between systems or different kernel versions. </p>
<p> Examples: /dev/sda5 is a path to a device node, referring to an ATA or SCSI block device. &quot;char-pts&quot; and &quot;char-alsa&quot; are specifiers for all pseudo TTYs and all ALSA sound devices, respectively. &quot;char-cpu/*&quot; is a specifier matching all CPU related device groups. </p>
<p> Note that allow lists defined this way should only reference device groups which are resolvable at the time the unit is started. Any device groups not resolvable then are not added to the device allow list. In order to work around this limitation, consider extending service units with a pair of <code>After=modprobe [at] xyz.service</code> and <code>Wants=modprobe [at] xyz.service</code> lines that load the necessary kernel module implementing the device group if missing. Example: </p>
<dl>
<dd>
<pre>...
[Unit]
Wants=modprobe [at] loop.service
After=modprobe [at] loop.service
[Service]
DeviceAllow=block-loop
DeviceAllow=/dev/loop-control
...</pre>
</dl>
</dl>
<p> <i>DevicePolicy=auto|closed|strict</i></p>
<dl>
<dd>Control the policy for allowing device access: </p>
<p> <code>strict</code></p>
<dl>
<dd>means to only allow types of access that are explicitly specified.</dl>
<p> <code>closed</code></p>
<dl>
<dd>in addition, allows access to standard pseudo devices including /dev/null, /dev/zero, /dev/full, /dev/random, and /dev/urandom.</dl>
<p> <code>auto</code></p>
<dl>
<dd>in addition, allows access to all devices if no explicit <i>DeviceAllow=</i> is present. This is the default.</dl>
</dl>
<p> <i>Slice=</i></p>
<dl>
<dd>The name of the slice unit to place the unit in. Defaults to system.slice for all non-instantiated units of all unit types (except for slice units themselves see below). Instance units are by default placed in a subslice of system.slice that is named after the template name. </p>
<p> This option may be used to arrange systemd units in a hierarchy of slices each of which might have resource settings applied. </p>
<p> For units of type slice, the only accepted value for this setting is the parent slice. Since the name of a slice unit implies the parent slice, it is hence redundant to ever set this parameter directly for slice units. </p>
<p> Special care should be taken when relying on the default slice assignment in templated service units that have <i>DefaultDependencies=no</i> set, see <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), section &quot;Default Dependencies&quot; for details.</dl>
<p> <i>Delegate=</i></p>
<dl>
<dd>Turns on delegation of further resource control partitioning to processes of the unit. Units where this is enabled may create and manage their own private subhierarchy of control groups below the control group of the unit itself. For unprivileged services (i.e. those using the <i>User=</i> setting) the unit&#8217;s control group will be made accessible to the relevant user. When enabled the service manager will refrain from manipulating control groups or moving processes below the unit&#8217;s control group, so that a clear concept of ownership is established: the control group tree above the unit&#8217;s control group (i.e. towards the root control group) is owned and managed by the service manager of the host, while the control group tree below the unit&#8217;s control group is owned and managed by the unit itself. Takes either a boolean argument or a list of control group controller names. If true, delegation is turned on, and all supported controllers are enabled for the unit, making them available to the unit&#8217;s processes for management. If false, delegation is turned off entirely (and no additional controllers are enabled). If set to a list of controllers, delegation is turned on, and the specified controllers are enabled for the unit. Note that additional controllers than the ones specified might be made available as well, depending on configuration of the containing slice unit or other units contained in it. Note that assigning the empty string will enable delegation, but reset the list of controllers, all assignments prior to this will have no effect. Defaults to false. </p>
<p> Note that controller delegation to less privileged code is only safe on the unified control group hierarchy. Accordingly, access to the specified controllers will not be granted to unprivileged services on the legacy hierarchy, even when requested. </p>
<p> The following controller names may be specified: <code>cpu</code>, <code>cpuacct</code>, <code>cpuset</code>, <code>io</code>, <code>blkio</code>, <code>memory</code>, <code>devices</code>, <code>pids</code>, <code>bpf-firewall</code>, and <code>bpf-devices</code>. </p>
<p> Not all of these controllers are available on all kernels however, and some are specific to the unified hierarchy while others are specific to the legacy hierarchy. Also note that the kernel might support further controllers, which aren&#8217;t covered here yet as delegation is either not supported at all for them or not defined cleanly. </p>
<p> For further details on the delegation model consult m[blue]<code>Control Group APIs and Delegation</code>m[]<font SIZE="-2">[10]</font>.</dl>
<p> <i>DisableControllers=</i></p>
<dl>
<dd>Disables controllers from being enabled for a unit&#8217;s children. If a controller listed is already in use in its subtree, the controller will be removed from the subtree. This can be used to avoid child units being able to implicitly or explicitly enable a controller. Defaults to not disabling any controllers. </p>
<p> It may not be possible to successfully disable a controller if the unit or any child of the unit in question delegates controllers to its children, as any delegated subtree of the cgroup hierarchy is unmanaged by systemd. </p>
<p> Multiple controllers may be specified, separated by spaces. You may also pass <i>DisableControllers=</i> multiple times, in which case each new instance adds another controller to disable. Passing <i>DisableControllers=</i> by itself with no controller name present resets the disabled controller list. </p>
<p> The following controller names may be specified: <code>cpu</code>, <code>cpuacct</code>, <code>cpuset</code>, <code>io</code>, <code>blkio</code>, <code>memory</code>, <code>devices</code>, <code>pids</code>, <code>bpf-firewall</code>, and <code>bpf-devices</code>.</dl>
<p> <i>ManagedOOMSwap=auto|kill</i>, <i>ManagedOOMMemoryPressure=auto|kill</i></p>
<dl>
<dd>Specifies how <code><a href="/docs/linux/man/8-systemd-oomd-service/">systemd-oomd.service</a></code>(8) will act on this unit&#8217;s cgroups. Defaults to <code>auto</code>. </p>
<p> When set to <code>kill</code>, <code>systemd-oomd</code> will actively monitor this unit&#8217;s cgroup metrics to decide whether it needs to act. If the cgroup passes the limits set by <code><a href="/docs/linux/man/5-oomd-conf/">oomd.conf</a></code>(5) or its overrides, <code>systemd-oomd</code> will send a <code>SIGKILL</code> to all of the processes under the chosen candidate cgroup. Note that only descendant cgroups can be eligible candidates for killing; the unit that set its property to <code>kill</code> is not a candidate (unless one of its ancestors set their property to <code>kill</code>). You can find more details on candidates and kill behavior at <code><a href="/docs/linux/man/8-systemd-oomd-service/">systemd-oomd.service</a></code>(8) and <code><a href="/docs/linux/man/5-oomd-conf/">oomd.conf</a></code>(5). Setting either of these properties to <code>kill</code> will also automatically acquire <i>After=</i> and <i>Wants=</i> dependencies on systemd-oomd.service unless <i>DefaultDependencies=no</i>. </p>
<p> When set to <code>auto</code>, <code>systemd-oomd</code> will not actively use this cgroup&#8217;s data for monitoring and detection. However, if an ancestor cgroup has one of these properties set to <code>kill</code>, a unit with <code>auto</code> can still be an eligible candidate for <code>systemd-oomd</code> to act on.</dl>
<p> <i>ManagedOOMMemoryPressureLimit=</i></p>
<dl>
<dd>Overrides the default memory pressure limit set by <code><a href="/docs/linux/man/5-oomd-conf/">oomd.conf</a></code>(5) for this unit (cgroup). Takes a percentage value between 0% and 100%, inclusive. This property is ignored unless <i>ManagedOOMMemoryPressure=</i><code>kill</code>. Defaults to 0%, which means to use the default set by <code><a href="/docs/linux/man/5-oomd-conf/">oomd.conf</a></code>(5).</dl>
<p> <i>ManagedOOMPreference=none|avoid|omit</i></p>
<dl>
<dd>Allows deprioritizing or omitting this unit&#8217;s cgroup as a candidate when <code>systemd-oomd</code> needs to act. Requires support for extended attributes (see <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)) in order to use <code>avoid</code> or <code>omit</code>. Additionally, <code>systemd-oomd</code> will ignore these extended attributes if the unit&#8217;s cgroup is not owned by the root user. </p>
<p> If this property is set to <code>avoid</code>, the service manager will convey this to <code>systemd-oomd</code>, which will only select this cgroup if there are no other viable candidates. </p>
<p> If this property is set to <code>omit</code>, the service manager will convey this to <code>systemd-oomd</code>, which will ignore this cgroup as a candidate and will not perform any actions on it. </p>
<p> It is recommended to use <code>avoid</code> and <code>omit</code> sparingly, as it can adversely affect <code>systemd-oomd</code>&#8216;s kill behavior. Also note that these extended attributes are not applied recursively to cgroups under this unit&#8217;s cgroup. </p>
<p> Defaults to <code>none</code> which means <code>systemd-oomd</code> will rank this unit&#8217;s cgroup as defined in <code><a href="/docs/linux/man/8-systemd-oomd-service/">systemd-oomd.service</a></code>(8) and <code><a href="/docs/linux/man/5-oomd-conf/">oomd.conf</a></code>(5).</dl>
<h2>Deprecated Options</h2>
<p>The following options are deprecated. Use the indicated superseding options instead: </p>
<p> <i>CPUShares=</i><i>weight</i>, <i>StartupCPUShares=</i><i>weight</i></p>
<dl>
<dd>Assign the specified CPU time share weight to the processes executed. These options take an integer value and control the &quot;cpu.shares&quot; control group attribute. The allowed range is 2 to 262144. Defaults to 1024. For details about this control group attribute, see m[blue]<code>CFS Scheduler</code>m[]<font SIZE="-2">[4]</font>. The available CPU time is split up among all units within one slice relative to their CPU time share weight. </p>
<p> While <i>StartupCPUShares=</i> only applies to the startup phase of the system, <i>CPUShares=</i> applies to normal runtime of the system, and if the former is not set also to the startup phase. Using <i>StartupCPUShares=</i> allows prioritizing specific services at boot-up differently than during normal runtime. </p>
<p> Implies &quot;CPUAccounting=yes&quot;. </p>
<p> These settings are deprecated. Use <i>CPUWeight=</i> and <i>StartupCPUWeight=</i> instead.</dl>
<p> <i>MemoryLimit=</i><i>bytes</i></p>
<dl>
<dd>Specify the limit on maximum memory usage of the executed processes. The limit specifies how much process and kernel memory can be used by tasks in this unit. Takes a memory size in bytes. If the value is suffixed with K, M, G or T, the specified memory size is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes (with the base 1024), respectively. Alternatively, a percentage value may be specified, which is taken relative to the installed physical memory on the system. If assigned the special value &quot;infinity&quot;, no memory limit is applied. This controls the &quot;memory.limit_in_bytes&quot; control group attribute. For details about this control group attribute, see m[blue]<code>Memory Resource Controller</code>m[]<font SIZE="-2">[11]</font>. </p>
<p> Implies &quot;MemoryAccounting=yes&quot;. </p>
<p> This setting is deprecated. Use <i>MemoryMax=</i> instead.</dl>
<p> <i>BlockIOAccounting=</i></p>
<dl>
<dd>Turn on Block I/O accounting for this unit, if the legacy control group hierarchy is used on the system. Takes a boolean argument. Note that turning on block I/O accounting for one unit will also implicitly turn it on for all units contained in the same slice and all for its parent slices and the units contained therein. The system default for this setting may be controlled with <i>DefaultBlockIOAccounting=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5). </p>
<p> This setting is deprecated. Use <i>IOAccounting=</i> instead.</dl>
<p> <i>BlockIOWeight=</i><i>weight</i>, <i>StartupBlockIOWeight=</i><i>weight</i></p>
<dl>
<dd>Set the default overall block I/O weight for the executed processes, if the legacy control group hierarchy is used on the system. Takes a single weight value (between 10 and 1000) to set the default block I/O weight. This controls the &quot;blkio.weight&quot; control group attribute, which defaults to 500. For details about this control group attribute, see m[blue]<code>Block IO Controller</code>m[]<font SIZE="-2">[12]</font>. The available I/O bandwidth is split up among all units within one slice relative to their block I/O weight. </p>
<p> While <i>StartupBlockIOWeight=</i> only applies to the startup phase of the system, <i>BlockIOWeight=</i> applies to the later runtime of the system, and if the former is not set also to the startup phase. This allows prioritizing specific services at boot-up differently than during runtime. </p>
<p> Implies &quot;BlockIOAccounting=yes&quot;. </p>
<p> These settings are deprecated. Use <i>IOWeight=</i> and <i>StartupIOWeight=</i> instead.</dl>
<p> <i>BlockIODeviceWeight=</i><i>device</i><i> </i><i>weight</i></p>
<dl>
<dd>Set the per-device overall block I/O weight for the executed processes, if the legacy control group hierarchy is used on the system. Takes a space-separated pair of a file path and a weight value to specify the device specific weight value, between 10 and 1000. (Example: &quot;/dev/sda 500&quot;). The file path may be specified as path to a block device node or as any other file, in which case the backing block device of the file system of the file is determined. This controls the &quot;blkio.weight_device&quot; control group attribute, which defaults to 1000. Use this option multiple times to set weights for multiple devices. For details about this control group attribute, see m[blue]<code>Block IO Controller</code>m[]<font SIZE="-2">[12]</font>. </p>
<p> Implies &quot;BlockIOAccounting=yes&quot;. </p>
<p> This setting is deprecated. Use <i>IODeviceWeight=</i> instead.</dl>
<p> <i>BlockIOReadBandwidth=</i><i>device</i><i> </i><i>bytes</i>, <i>BlockIOWriteBandwidth=</i><i>device</i><i> </i><i>bytes</i></p>
<dl>
<dd>Set the per-device overall block I/O bandwidth limit for the executed processes, if the legacy control group hierarchy is used on the system. Takes a space-separated pair of a file path and a bandwidth value (in bytes per second) to specify the device specific bandwidth. The file path may be a path to a block device node, or as any other file in which case the backing block device of the file system of the file is used. If the bandwidth is suffixed with K, M, G, or T, the specified bandwidth is parsed as Kilobytes, Megabytes, Gigabytes, or Terabytes, respectively, to the base of 1000. (Example: &quot;/dev/disk/by-path/pci-0000:00:1f.2-scsi-0:0:0:0 5M&quot;). This controls the &quot;blkio.throttle.read_bps_device&quot; and &quot;blkio.throttle.write_bps_device&quot; control group attributes. Use this option multiple times to set bandwidth limits for multiple devices. For details about these control group attributes, see m[blue]<code>Block IO Controller</code>m[]<font SIZE="-2">[12]</font>. </p>
<p> Implies &quot;BlockIOAccounting=yes&quot;. </p>
<p> These settings are deprecated. Use <i>IOReadBandwidthMax=</i> and <i>IOWriteBandwidthMax=</i> instead.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/8-systemd-oomd-service/">systemd-oomd.service</a></code>(8), The documentation for control groups and specific controllers in the Linux kernel: m[blue]<code>Control Groups v2</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>New Control Group Interfaces</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/">https://www.freedesktop.org/wiki/Software/systemd/ControlGroupInterface/</a></dl>
<dt> 2.</p>
<dd>Control Groups v2</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html</a></dl>
<dt> 3.</p>
<dd>Control Groups version 1</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/</a></dl>
<dt> 4.</p>
<dd>CFS Scheduler</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html">https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html</a></dl>
<dt> 5.</p>
<dd>sched-bwc.txt</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt">https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt</a></dl>
<dt> 6.</p>
<dd>Memory Interface Files</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#memory-interface-files">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#memory-interface-files</a></dl>
<dt> 7.</p>
<dd>Process Number Controller</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/pids.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/pids.html</a></dl>
<dt> 8.</p>
<dd>IO Interface Files</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#io-interface-files">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#io-interface-files</a></dl>
<dt> 9.</p>
<dd>Device Whitelist Controller</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/devices.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/devices.html</a></dl>
<dt>10.</p>
<dd>Control Group APIs and Delegation</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/CGROUP_DELEGATION">https://systemd.io/CGROUP_DELEGATION</a></dl>
<dt>11.</p>
<dd>Memory Resource Controller</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/memory.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/memory.html</a></dl>
<dt>12.</p>
<dd>Block IO Controller</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/blkio-controller.html">https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/blkio-controller.html</a></dl>
