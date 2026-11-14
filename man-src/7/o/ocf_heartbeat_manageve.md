---
title: "ocf_heartbeat_manageve(7)"
name: "ocf_heartbeat_manageve"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_manageve/"
description: "ocf_heartbeat_ManageVE – Manages an OpenVZ Virtual Environment (VE)"
---

<p>ocf_heartbeat_ManageVE &#8211; Manages an OpenVZ Virtual Environment (VE)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ManageVE</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This OCF complaint resource agent manages OpenVZ VEs and thus requires a proper OpenVZ installation including a recent vzctl util.</p>
<h2>Supported Parameters</h2>
<p><code>veid</code></p>
<dl>
<dd>OpenVZ ID of virtual environment (see output of vzlist -a for all assigned IDs) (required, integer, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 75.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 75.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a ManageVE resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_ManageVE ocf:heartbeat:ManageVE \
params \
veid=integer \
op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ManageVE_(resource_agent)">http://www.linux-ha.org/wiki/ManageVE_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
