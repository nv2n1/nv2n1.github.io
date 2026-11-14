---
title: "ocf_heartbeat_nova-compute-wait(7)"
name: "ocf_heartbeat_nova-compute-wait"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_nova-compute-wait/"
description: "ocf_heartbeat_nova-compute-wait – OpenStack Nova Compute Server"
---

<p>ocf_heartbeat_nova-compute-wait &#8211; OpenStack Nova Compute Server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nova-compute-wait</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>OpenStack Nova Compute Server.</p>
<h2>Supported Parameters</h2>
<p><code>auth_url</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
<p> (required, string, no default)</dl>
<p> <code>username</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
</dl>
<p> <code>password</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
<p> (required, string, no default)</dl>
<p> <code>tenant_name</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
<p> (required, string, no default)</dl>
<p> <code>domain</code></p>
<dl>
<dd>DNS domain in which hosts live, useful when the cluster uses short names and nova uses FQDN </p>
<p> (optional, string, no default)</dl>
<p> <code>endpoint_type</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
<p> (optional, string, no default)</dl>
<p> <code>no_shared_storage</code></p>
<dl>
<dd>Deprecated &#8211; do not use anymore. </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>evacuation_delay</code></p>
<dl>
<dd>How long to wait for nova to finish evacuating instances elsewhere before starting nova-compute. Only used when the agent detects evacuations might be in progress. </p>
<p> You may need to increase the start timeout when increasing this value. </p>
<p> (optional, integer, default 120)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 600.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 300.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a nova-compute-wait resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_nova-compute-wait ocf:heartbeat:nova-compute-wait \
 params \
 auth_url=<i>string</i> \
 username= \
 password=<i>string</i> \
 tenant_name=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a nova-compute-wait resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_nova-compute-wait ocf:heartbeat:nova-compute-wait \
 auth_url=<i>string</i> \
 username= \
 password=<i>string</i> \
 tenant_name=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/nova-compute-wait_(resource_agent)">http://www.linux-ha.org/wiki/nova-compute-wait_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
