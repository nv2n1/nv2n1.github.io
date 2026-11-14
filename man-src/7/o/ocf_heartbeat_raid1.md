---
title: "ocf_heartbeat_raid1(7)"
name: "ocf_heartbeat_raid1"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_raid1/"
description: "ocf_heartbeat_Raid1 – Manages a software RAID1 device on shared storage"
---

<p>ocf_heartbeat_Raid1 &#8211; Manages a software RAID1 device on shared storage</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Raid1</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for RAID1. It manages a software Raid1 device on a shared storage medium.</p>
<h2>Supported Parameters</h2>
<p><code>raidconf</code></p>
<dl>
<dd>The RAID configuration file. e.g. /etc/raidtab or /etc/mdadm.conf. (required, string, no default)</dl>
<p> <code>raiddev</code></p>
<dl>
<dd>The block device to use. (required, string, no default)</dl>
<p> <code>homehost</code></p>
<dl>
<dd>The value for the homehost directive; this is an mdadm feature to protect RAIDs against being activated by accident. It is recommended to create RAIDs managed by the cluster with &quot;homehost&quot; set to a special value, so they are not accidentially auto-assembled by nodes not supposed to own them. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a Raid1 resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_Raid1 ocf:heartbeat:Raid1 \
params \
raidconf=string \
raiddev=string \
op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Raid1_(resource_agent)">http://www.linux-ha.org/wiki/Raid1_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
