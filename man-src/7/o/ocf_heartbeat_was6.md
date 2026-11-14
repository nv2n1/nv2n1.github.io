---
title: "ocf_heartbeat_was6(7)"
name: "ocf_heartbeat_was6"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_was6/"
description: "ocf_heartbeat_WAS6 – Manages a WebSphere Application Server 6 instance"
---

<p>ocf_heartbeat_WAS6 &#8211; Manages a WebSphere Application Server 6 instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>WAS6</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for WAS6. It manages a Websphere Application Server (WAS6) as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>profile</code></p>
<dl>
<dd>The WAS profile name. (optional, string, default default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 300.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 300.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a WAS6 resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_WAS6 ocf:heartbeat:WAS6 \

op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/WAS6_(resource_agent)">http://www.linux-ha.org/wiki/WAS6_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
