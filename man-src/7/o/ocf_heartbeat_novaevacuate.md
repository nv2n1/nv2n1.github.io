---
title: "ocf_heartbeat_novaevacuate(7)"
name: "ocf_heartbeat_novaevacuate"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_novaevacuate/"
description: "ocf_heartbeat_NovaEvacuate – Evacuator for OpenStack Nova Compute Server"
---

<p>ocf_heartbeat_NovaEvacuate &#8211; Evacuator for OpenStack Nova Compute Server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>NovaEvacuate</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Facility for tacking a list of compute nodes and reliably evacuating the ones that fence_evacuate has flagged.</p>
<h2>Supported Parameters</h2>
<p><code>auth_url</code></p>
<dl>
<dd>Authorization URL for connecting to keystone in admin context </p>
<p> (required, string, no default)</dl>
<p> <code>username</code></p>
<dl>
<dd>Username for connecting to keystone in admin context </p>
</dl>
<p> <code>password</code></p>
<dl>
<dd>Password for connecting to keystone in admin context </p>
<p> (required, string, no default)</dl>
<p> <code>tenant_name</code></p>
<dl>
<dd>Tenant name for connecting to keystone in admin context. Note that with Keystone V3 tenant names are only unique within a domain. </p>
<p> (required, string, no default)</dl>
<p> <code>endpoint_type</code></p>
<dl>
<dd>Nova API location (internal, public or admin URL) </p>
<p> (optional, string, no default)</dl>
<p> <code>no_shared_storage</code></p>
<dl>
<dd>Disable shared storage recovery for instances. Use at your own risk! </p>
<p> (optional, boolean, default 0)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 600. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a NovaEvacuate resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_NovaEvacuate ocf:heartbeat:NovaEvacuate \
 params \
 auth_url=<i>string</i> \
 username= \
 password=<i>string</i> \
 tenant_name=<i>string</i> \
 op monitor timeout=&quot;600&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a NovaEvacuate resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_NovaEvacuate ocf:heartbeat:NovaEvacuate \
 auth_url=<i>string</i> \
 username= \
 password=<i>string</i> \
 tenant_name=<i>string</i> \
 op monitor timeout=&quot;600&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/NovaEvacuate_(resource_agent)">http://www.linux-ha.org/wiki/NovaEvacuate_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
