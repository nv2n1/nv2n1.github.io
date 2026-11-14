---
title: "ocf_heartbeat_pingd(7)"
name: "ocf_heartbeat_pingd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_pingd/"
description: "ocf_heartbeat_pingd – Monitors connectivity to specific hosts or IP addresses (\"ping nodes\") (deprecated)"
---

<p>ocf_heartbeat_pingd &#8211; Monitors connectivity to specific hosts or IP addresses (&quot;ping nodes&quot;) (deprecated)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pingd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Deprecation warning: This agent is deprecated and may be removed from a future release. See the ocf:pacemaker:pingd resource agent for a supported alternative. &#8212; This is a pingd Resource Agent. It records (in the CIB) the current number of ping nodes a node can connect to.</p>
<h2>Supported Parameters</h2>
<p><code>pidfile</code></p>
<dl>
<dd>PID file (optional, string, default /var/run/heartbeat/rsctmp/pingd-default)</dl>
<p> <code>user</code></p>
<dl>
<dd>The user we want to run pingd as (optional, string, default root)</dl>
<p> <code>dampen</code></p>
<dl>
<dd>The time to wait (dampening) further changes occur (optional, integer, default 1s)</dl>
<p> <code>set</code></p>
<dl>
<dd>The name of the instance_attributes set to place the value in. Rarely needs to be specified. (optional, integer, no default)</dl>
<p> <code>name</code></p>
<dl>
<dd>The name of the attributes to set. This is the name to be used in the constraints. (optional, integer, default default)</dl>
<p> <code>section</code></p>
<dl>
<dd>The section place the value in. Rarely needs to be specified. (optional, integer, no default)</dl>
<p> <code>multiplier</code></p>
<dl>
<dd>The number by which to multiply the number of connected ping nodes by (optional, integer, no default)</dl>
<p> <code>host_list</code></p>
<dl>
<dd>The list of ping nodes to count. Defaults to all configured ping nodes. Rarely needs to be specified. (optional, integer, no default)</dl>
<p> <code>ignore_deprecation</code></p>
<dl>
<dd>If set to true, suppresses the deprecation warning for this agent. (optional, boolean, default false)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a pingd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_pingd ocf:heartbeat:pingd \

op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/pingd_(resource_agent)">http://www.linux-ha.org/wiki/pingd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
