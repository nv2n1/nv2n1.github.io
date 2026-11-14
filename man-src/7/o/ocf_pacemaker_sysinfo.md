---
title: "ocf_pacemaker_sysinfo(7)"
name: "ocf_pacemaker_sysinfo"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_sysinfo/"
description: "ocf_pacemaker_SysInfo – SysInfo resource agent"
---

<p>ocf_pacemaker_SysInfo &#8211; SysInfo resource agent</p>
<h2>Synopsis</h2>
<p><code>OCF_RESKEY_pidfile</code>=string [<code>OCF_RESKEY_delay</code>=string] [<code>OCF_RESKEY_disks</code>=string] [<code>OCF_RESKEY_disk_unit</code>=string] [<code>OCF_RESKEY_min_disk_free</code>=string] <code>SysInfo</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>This is a SysInfo Resource Agent. It records (in the CIB) various attributes of a node Sample Linux output: arch: i686 os: Linux-2.4.26-gentoo-r14 free_swap: 1999 cpu_info: Intel(R) Celeron(R) CPU 2.40GHz cpu_speed: 4771.02 cpu_cores: 1 cpu_load: 0.00 ram_total: 513 ram_free: 117 root_free: 2.4 #health_disk: red Sample Darwin output: arch: i386 os: Darwin-8.6.2 cpu_info: Intel Core Duo cpu_speed: 2.16 cpu_cores: 2 cpu_load: 0.18 ram_total: 2016 ram_free: 787 root_free: 13 #health_disk: green Units: free_swap: Mb ram_*: Mb cpu_speed (Linux): bogomips cpu_speed (Darwin): Ghz *_free: GB (or user-defined: disk_unit)</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_pidfile</code> = string [/SysInfo-]</p>
<dl>
<dd>PID file</dl>
<p> <code>OCF_RESKEY_delay</code> = string [0s]</p>
<dl>
<dd>Dampening Delay </p>
<p> Interval to allow values to stabilize</dl>
<p> <code>OCF_RESKEY_disks</code> = string</p>
<dl>
<dd>List of Filesytems/Paths to query for free disk space </p>
<p> Filesystems or Paths to be queried for free disk space as a SPACE separated list &#8211; e.g &quot;/dev/sda1 /tmp&quot;. Results will be written to an attribute with leading slashes removed, and other slashes replaced with underscore, and the word &#8216;free&#8217; appended &#8211; e.g for /dev/sda1 it would be &#8216;dev_sda1_free&#8217;. Note: The root filesystem &#8216;/&#8217; is always queried to an attribute named &#8216;root_free&#8217;</dl>
<p> <code>OCF_RESKEY_disk_unit</code> = string [G]</p>
<dl>
<dd>Unit to report disk free space in </p>
<p> Unit to report disk free space in. Can be one of: B, K, M, G, T, P (case-insensitive)</dl>
<p> <code>OCF_RESKEY_min_disk_free</code> = string []</p>
<dl>
<dd>minimum disk free space required </p>
<p> The amount of free space required in monitored disks. If any of the monitored disks has less than this amount of free space, , with the node attribute &quot;#health_disk&quot; changing to &quot;red&quot;, all resources will move away from the node. Set the node-health-strategy property appropriately for this to take effect. If the unit is not specified, it defaults to disk_unit.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
