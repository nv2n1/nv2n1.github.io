---
title: "ocf_heartbeat_drbd(7)"
name: "ocf_heartbeat_drbd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_drbd/"
description: "ocf_heartbeat_drbd – Manages a DRBD resource (deprecated)"
---

<p>ocf_heartbeat_drbd &#8211; Manages a DRBD resource (deprecated)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>drbd</code> [start | stop | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Deprecation warning: This agent is deprecated and may be removed from a future release. See the ocf:linbit:drbd resource agent for a supported alternative. &#8212; This resource agent manages a Distributed Replicated Block Device (DRBD) object as a master/slave resource. DRBD is a mechanism for replicating storage; please see the documentation for setup details.</p>
<h2>Supported Parameters</h2>
<p><code>drbd_resource</code></p>
<dl>
<dd>The name of the drbd resource from the drbd.conf file. (required, string, default drbd0)</dl>
<p> <code>drbdconf</code></p>
<dl>
<dd>Full path to the drbd.conf file. (optional, string, default /etc/drbd.conf)</dl>
<p> <code>clone_overrides_hostname</code></p>
<dl>
<dd>Whether or not to override the hostname with the clone number. This can be used to create floating peer configurations; drbd will be told to use node_&lt;cloneno&gt; as the hostname instead of the real uname, which can then be used in drbd.conf. (optional, boolean, default no)</dl>
<p> <code>ignore_deprecation</code></p>
<dl>
<dd>If set to true, suppresses the deprecation warning for this agent. (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 240.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 90.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 90.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 100.</dl>
<p> <code>monitor (Slave role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 20.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a drbd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_drbd ocf:heartbeat:drbd \
params \
drbd_resource=&quot;drbd0&quot; \
op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;20&quot; role=&quot;Slave&quot;
op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; role=&quot;Master&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/drbd_(resource_agent)">http://www.linux-ha.org/wiki/drbd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
