---
title: "ocf_heartbeat_viparip(7)"
name: "ocf_heartbeat_viparip"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_viparip/"
description: "ocf_heartbeat_VIPArip – Manages a virtual IP address through RIP2"
---

<p>ocf_heartbeat_VIPArip &#8211; Manages a virtual IP address through RIP2</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>VIPArip</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Virtual IP Address by RIP2 protocol. This script manages IP alias in different subnet with quagga/ripd. It can add an IP alias, or remove one.</p>
<h2>Supported Parameters</h2>
<p><code>ip</code></p>
<dl>
<dd>The IPv4 address in different subnet, for example &quot;192.168.1.1&quot;. (required, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The nic for broadcast the route information. The ripd uses this nic to broadcast the route informaton to others (optional, string, default eth0)</dl>
<p> <code>zebra_binary</code></p>
<dl>
<dd>Absolute path to the zebra binary. (optional, string, default /usr/sbin/zebra)</dl>
<p> <code>ripd_binary</code></p>
<dl>
<dd>Absolute path to the ripd binary. (optional, string, default /usr/sbin/ripd)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a VIPArip resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_VIPArip ocf:heartbeat:VIPArip \
params \
ip=string \
op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;5s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/VIPArip_(resource_agent)">http://www.linux-ha.org/wiki/VIPArip_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
