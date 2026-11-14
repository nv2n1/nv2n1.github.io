---
title: "ocf_heartbeat_rabbitmq-cluster(7)"
name: "ocf_heartbeat_rabbitmq-cluster"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_rabbitmq-cluster/"
description: "ocf_heartbeat_rabbitmq-cluster – rabbitmq clustered"
---

<p>ocf_heartbeat_rabbitmq-cluster &#8211; rabbitmq clustered</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rabbitmq-cluster</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Starts cloned rabbitmq cluster instance. NB: note that this RA cannot be spawned across a mix of pacemaker and pacemaker-remote nodes. Only on pacemaker *or* pacemaker-remote nodes exclusively.</p>
<h2>Supported Parameters</h2>
<p><code>set_policy</code></p>
<dl>
<dd>Policy string to pass to &#8216;rabbitmqctl set_policy&#8217; right after bootstrapping the first rabbitmq instance. </p>
<p> (unique, optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 100.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 90.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 40. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a rabbitmq-cluster resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_rabbitmq-cluster ocf:heartbeat:rabbitmq-cluster \
 op monitor timeout=&quot;40&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a rabbitmq-cluster resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_rabbitmq-cluster ocf:heartbeat:rabbitmq-cluster \
 op monitor timeout=&quot;40&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/rabbitmq-cluster_(resource_agent)">http://www.linux-ha.org/wiki/rabbitmq-cluster_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
