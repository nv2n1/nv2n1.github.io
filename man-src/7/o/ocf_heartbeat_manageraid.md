---
title: "ocf_heartbeat_manageraid(7)"
name: "ocf_heartbeat_manageraid"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_manageraid/"
description: "ocf_heartbeat_ManageRAID – Manages RAID devices"
---

<p>ocf_heartbeat_ManageRAID &#8211; Manages RAID devices</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ManageRAID</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Manages starting, stopping and monitoring of RAID devices which are preconfigured in /etc/conf.d/HB-ManageRAID.</p>
<h2>Supported Parameters</h2>
<p><code>raidname</code></p>
<dl>
<dd>Name (case sensitive) of RAID to manage. (preconfigured in /etc/conf.d/HB-ManageRAID) (required, string, no default)</dl>
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
<p>The following is an example configuration for a ManageRAID resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_ManageRAID ocf:heartbeat:ManageRAID \
params \
raidname=string \
op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ManageRAID_(resource_agent)">http://www.linux-ha.org/wiki/ManageRAID_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
