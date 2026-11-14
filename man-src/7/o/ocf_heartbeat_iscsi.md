---
title: "ocf_heartbeat_iscsi(7)"
name: "ocf_heartbeat_iscsi"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_iscsi/"
description: "ocf_heartbeat_iscsi – Manages a local iSCSI initiator and its connections to iSCSI targets"
---

<p>ocf_heartbeat_iscsi &#8211; Manages a local iSCSI initiator and its connections to iSCSI targets</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>iscsi</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>OCF Resource Agent for iSCSI. Add (start) or remove (stop) iSCSI targets.</p>
<h2>Supported Parameters</h2>
<p><code>portal</code></p>
<dl>
<dd>The iSCSI portal address in the form: {ip_address|hostname}[&quot;:&quot;port] (required, string, no default)</dl>
<p> <code>target</code></p>
<dl>
<dd>The iSCSI target IQN. (required, string, no default)</dl>
<p> <code>discovery_type</code></p>
<dl>
<dd>Target discovery type. Check the open-iscsi documentation for supported discovery types. (optional, string, default sendtargets)</dl>
<p> <code>iscsiadm</code></p>
<dl>
<dd>open-iscsi administration utility binary. (optional, string, default iscsiadm)</dl>
<p> <code>udev</code></p>
<dl>
<dd>If the next resource depends on the udev creating a device then we wait until it is finished. On a normally loaded host this should be done quickly, but you may be unlucky. If you are not using udev set this to &quot;no&quot;, otherwise we will spin in a loop until a timeout occurs. (optional, string, default yes)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 120.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 120.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a iscsi resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_iscsi ocf:heartbeat:iscsi \
params \
portal=string \
target=string \
op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;120&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/iscsi_(resource_agent)">http://www.linux-ha.org/wiki/iscsi_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
