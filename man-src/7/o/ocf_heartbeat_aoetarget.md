---
title: "ocf_heartbeat_aoetarget(7)"
name: "ocf_heartbeat_aoetarget"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_aoetarget/"
description: "ocf_heartbeat_AoEtarget – Manages ATA-over-Ethernet (AoE) target exports"
---

<p>ocf_heartbeat_AoEtarget &#8211; Manages ATA-over-Ethernet (AoE) target exports</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>AoEtarget</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This resource agent manages an ATA-over-Ethernet (AoE) target using vblade. It exports any block device, or file, as an AoE target using the specified Ethernet device, shelf, and slot number.</p>
<h2>Supported Parameters</h2>
<p><code>device</code></p>
<dl>
<dd>The local block device (or file) to export as an AoE target. (required, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The local Ethernet interface to use for exporting this AoE target. (required, string, default eth0)</dl>
<p> <code>shelf</code></p>
<dl>
<dd>The AoE shelf number to use when exporting this target. (optional, integer, no default)</dl>
<p> <code>slot</code></p>
<dl>
<dd>The AoE slot number to use when exporting this target. (required, integer, no default)</dl>
<p> <code>pid</code></p>
<dl>
<dd>The file to record the daemon pid to. (optional, string, default /var/run/heartbeat/rsctmp/AoEtarget-default.pid)</dl>
<p> <code>binary</code></p>
<dl>
<dd>Location of the vblade binary. (optional, string, default /usr/sbin/vblade)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 15.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 15.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 15. Suggested interval: 10.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 15.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 15.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a AoEtarget resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_AoEtarget ocf:heartbeat:AoEtarget \
params \
device=string \
nic=&quot;eth0&quot; \
slot=integer \
op monitor timeout=&quot;15&quot; interval=&quot;10&quot; depth=&quot;0&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/AoEtarget_(resource_agent)">http://www.linux-ha.org/wiki/AoEtarget_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
