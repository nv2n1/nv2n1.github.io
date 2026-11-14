---
title: "ocf_heartbeat_evmsd(7)"
name: "ocf_heartbeat_evmsd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_evmsd/"
description: "ocf_heartbeat_Evmsd – Controls clustered EVMS volume management (deprecated)"
---

<p>ocf_heartbeat_Evmsd &#8211; Controls clustered EVMS volume management (deprecated)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Evmsd</code> [start | stop | monitor | meta-data]</dl>
<h2>Description</h2>
<dd>Deprecation warning: EVMS is no longer actively maintained and should not be used. This agent is deprecated and may be removed from a future release. &#8212; This is a Evmsd Resource Agent.</p>
<h2>Supported Parameters</h2>
<p><code>ignore_deprecation</code></p>
<dl>
<dd>If set to true, suppresses the deprecation warning for this agent. (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a Evmsd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_Evmsd ocf:heartbeat:Evmsd \

op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Evmsd_(resource_agent)">http://www.linux-ha.org/wiki/Evmsd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
