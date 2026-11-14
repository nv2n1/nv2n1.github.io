---
title: "ocf_heartbeat_clustermon(7)"
name: "ocf_heartbeat_clustermon"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_clustermon/"
description: "ocf_heartbeat_ClusterMon – Runs crm_mon in the background, recording the cluster status to an HTML file"
---

<p>ocf_heartbeat_ClusterMon &#8211; Runs crm_mon in the background, recording the cluster status to an HTML file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ClusterMon</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a ClusterMon Resource Agent. It outputs current cluster status to the html.</p>
<h2>Supported Parameters</h2>
<p><code>user</code></p>
<dl>
<dd>The user we want to run crm_mon as (optional, string, default root)</dl>
<p> <code>update</code></p>
<dl>
<dd>How frequently should we update the cluster status (optional, integer, default 15)</dl>
<p> <code>extra_options</code></p>
<dl>
<dd>Additional options to pass to crm_mon. Eg. -n -r (optional, string, no default)</dl>
<p> <code>pidfile</code></p>
<dl>
<dd>PID file location to ensure only one instance is running (optional, string, default /tmp/ClusterMon_default.pid)</dl>
<p> <code>htmlfile</code></p>
<dl>
<dd>Location to write HTML output to. (optional, string, default /tmp/ClusterMon_default.html)</dl>
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
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a ClusterMon resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_ClusterMon ocf:heartbeat:ClusterMon \

op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ClusterMon_(resource_agent)">http://www.linux-ha.org/wiki/ClusterMon_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
