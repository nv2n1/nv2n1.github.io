---
title: "ocf_heartbeat_sfex(7)"
name: "ocf_heartbeat_sfex"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sfex/"
description: "ocf_heartbeat_sfex – Manages exclusive acess to shared storage using Shared Disk File EXclusiveness (SF-EX)"
---

<p>ocf_heartbeat_sfex &#8211; Manages exclusive acess to shared storage using Shared Disk File EXclusiveness (SF-EX)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sfex</code> [start | stop | monitor | meta-data]</dl>
<h2>Description</h2>
<dd>Resource script for SF-EX. It manages a shared storage medium exclusively .</p>
<h2>Supported Parameters</h2>
<p><code>device</code></p>
<dl>
<dd>Block device path that stores exclusive control data. (required, string, no default)</dl>
<p> <code>index</code></p>
<dl>
<dd>Location in block device where exclusive control data is stored. 1 or more is specified. Default is 1. (optional, integer, default 1)</dl>
<p> <code>collision_timeout</code></p>
<dl>
<dd>Waiting time when a collision of lock acquisition is detected. Default is 1 second. (optional, integer, default 1)</dl>
<p> <code>monitor_interval</code></p>
<dl>
<dd>Monitor interval(sec). Default is 10 seconds (optional, integer, default 10)</dl>
<p> <code>lock_timeout</code></p>
<dl>
<dd>Valid term of lock(sec). Default is 20 seconds. (optional, integer, default 20)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 600.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a sfex resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_sfex ocf:heartbeat:sfex \
params \
device=string \
op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/sfex_(resource_agent)">http://www.linux-ha.org/wiki/sfex_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
