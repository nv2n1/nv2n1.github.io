---
title: "ocf_heartbeat_serveraid(7)"
name: "ocf_heartbeat_serveraid"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_serveraid/"
description: "ocf_heartbeat_ServeRAID – Enables and disables shared ServeRAID merge groups"
---

<p>ocf_heartbeat_ServeRAID &#8211; Enables and disables shared ServeRAID merge groups</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ServeRAID</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for ServeRAID. It enables/disables shared ServeRAID merge groups.</p>
<h2>Supported Parameters</h2>
<p><code>serveraid</code></p>
<dl>
<dd>The adapter number of the ServeRAID adapter. (required, integer, no default)</dl>
<p> <code>mergegroup</code></p>
<dl>
<dd>The logical drive under consideration. (required, integer, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 40.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 40.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
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
<p>The following is an example configuration for a ServeRAID resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_ServeRAID ocf:heartbeat:ServeRAID \
params \
serveraid=integer \
mergegroup=integer \
op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ServeRAID_(resource_agent)">http://www.linux-ha.org/wiki/ServeRAID_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
