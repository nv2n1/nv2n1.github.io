---
title: "ocf_heartbeat_garbd(7)"
name: "ocf_heartbeat_garbd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_garbd/"
description: "ocf_heartbeat_garbd – Manages a galera arbitrator instance"
---

<p>ocf_heartbeat_garbd &#8211; Manages a galera arbitrator instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>garbd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for managing Galera arbitrator.</p>
<h2>Supported Parameters</h2>
<p><code>binary</code></p>
<dl>
<dd>Location of the Galera arbitrator binary </p>
<p> (optional, string, default &quot;/usr/sbin/garbd&quot;)</dl>
<p> <code>user</code></p>
<dl>
<dd>User running the garbd process </p>
<p> (optional, string, default &quot;mysql&quot;)</dl>
<p> <code>group</code></p>
<dl>
<dd>Group running garbd (for logfile permissions) </p>
<p> (optional, string, default &quot;mysql&quot;)</dl>
<p> <code>log</code></p>
<dl>
<dd>The logfile to be used for garbd. </p>
<p> (optional, string, default &quot;/var/log/garbd.log&quot;)</dl>
<p> <code>pid</code></p>
<dl>
<dd>The pidfile to be used for garbd. </p>
<p> (optional, string, default &quot;/var/run/garbd.pid&quot;)</dl>
<p> <code>options</code></p>
<dl>
<dd>Additional parameters which are passed to garbd on startup. </p>
<p> (optional, string, no default)</dl>
<p> <code>wsrep_cluster_address</code></p>
<dl>
<dd>The galera cluster address. This takes the form of: <a href="gcomm://node:port,node:port,node:port">gcomm://node:port,node:port,node:port</a> </p>
<p> Unlike Galera servers, port is mandatory for garbd. </p>
<p> (required, string, no default)</dl>
<p> <code>wsrep_cluster_name</code></p>
<dl>
<dd>The group name of the Galera cluster to connect to. </p>
<p> (required, string, no default)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 20.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a garbd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_garbd ocf:heartbeat:garbd \
 params \
 wsrep_cluster_address=<i>string</i> \
 wsrep_cluster_name=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;20&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a garbd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_garbd ocf:heartbeat:garbd \
 wsrep_cluster_address=<i>string</i> \
 wsrep_cluster_name=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;20&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/garbd_(resource_agent)">http://www.linux-ha.org/wiki/garbd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
