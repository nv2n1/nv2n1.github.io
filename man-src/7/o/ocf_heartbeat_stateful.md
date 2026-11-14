---
title: "ocf_heartbeat_stateful(7)"
name: "ocf_heartbeat_stateful"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_stateful/"
description: "ocf_heartbeat_Stateful – Example stateful resource agent"
---

<p>ocf_heartbeat_Stateful &#8211; Example stateful resource agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Stateful</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is an example resource agent that impliments two states</p>
<h2>Supported Parameters</h2>
<p><code>state</code></p>
<dl>
<dd>Location to store the resource state in (optional, string, default /var/run/heartbeat/rsctmp/Stateful-{OCF_RESOURCE_INSTANCE}.state)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a Stateful resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_Stateful ocf:heartbeat:Stateful \

op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Stateful_(resource_agent)">http://www.linux-ha.org/wiki/Stateful_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
