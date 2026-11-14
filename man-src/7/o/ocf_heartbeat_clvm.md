---
title: "ocf_heartbeat_clvm(7)"
name: "ocf_heartbeat_clvm"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_clvm/"
description: "ocf_heartbeat_clvm – clvmd"
---

<p>ocf_heartbeat_clvm &#8211; clvmd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>clvm</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This agent manages the clvmd daemon.</p>
<h2>Supported Parameters</h2>
<p><code>with_cmirrord</code></p>
<dl>
<dd>Start with cmirrord (cluster mirror log daemon). </p>
<p> (optional, boolean, default false)</dl>
<p> <code>daemon_options</code></p>
<dl>
<dd>Options to clvmd. Refer to clvmd.8 for detailed descriptions. </p>
<p> (optional, string, default &quot;-d0&quot;)</dl>
<p> <code>activate_vgs</code></p>
<dl>
<dd>Whether or not to activate all cluster volume groups after starting the clvmd or not. Note that clustered volume groups will always be deactivated before the clvmd stops regardless of what this option is set to. </p>
<p> (optional, boolean, default true)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 90.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 90. Suggested interval: 30.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a clvm resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_clvm ocf:heartbeat:clvm \
 op monitor timeout=&quot;90&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a clvm resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_clvm ocf:heartbeat:clvm \
 op monitor timeout=&quot;90&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/clvm_(resource_agent)">http://www.linux-ha.org/wiki/clvm_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
