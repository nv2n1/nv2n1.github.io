---
title: "ocf_heartbeat_sysinfo(7)"
name: "ocf_heartbeat_sysinfo"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sysinfo/"
description: "ocf_heartbeat_SysInfo – Records various node attributes in the CIB"
---

<p>ocf_heartbeat_SysInfo &#8211; Records various node attributes in the CIB</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SysInfo</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a SysInfo Resource Agent. It records (in the CIB) various attributes of a node Sample Linux output: arch: i686 os: Linux-2.4.26-gentoo-r14 free_swap: 1999 cpu_info: Intel(R) Celeron(R) CPU 2.40GHz cpu_speed: 4771.02 cpu_cores: 1 cpu_load: 0.00 ram_total: 513 ram_free: 117 root_free: 2.4 Sample Darwin output: arch: i386 os: Darwin-8.6.2 cpu_info: Intel Core Duo cpu_speed: 2.16 cpu_cores: 2 cpu_load: 0.18 ram_total: 2016 ram_free: 787 root_free: 13 Units: free_swap: Mb ram_*: Mb root_free: Gb cpu_speed (Linux): bogomips cpu_speed (Darwin): Ghz</p>
<h2>Supported Parameters</h2>
<p><code>pidfile</code></p>
<dl>
<dd>PID file (optional, string, default /var/run/heartbeat/rsctmp/SysInfo-default)</dl>
<p> <code>delay</code></p>
<dl>
<dd>Interval to allow values to stabilize (optional, string, default 0s)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 60s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a SysInfo resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_SysInfo ocf:heartbeat:SysInfo \

op monitor timeout=&quot;20s&quot; interval=&quot;60s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/SysInfo_(resource_agent)">http://www.linux-ha.org/wiki/SysInfo_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
