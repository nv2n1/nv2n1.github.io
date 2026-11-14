---
title: "ocf_heartbeat_route(7)"
name: "ocf_heartbeat_route"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_route/"
description: "ocf_heartbeat_Route – Manages network routes"
---

<p>ocf_heartbeat_Route &#8211; Manages network routes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Route</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Enables and disables network routes. </p>
<p> Supports host and net routes, routes via a gateway address, and routes using specific source addresses. </p>
<p> This resource agent is useful if a node&#8217;s routing table needs to be manipulated based on node role assignment. </p>
<p> Consider the following example use case: </p>
<p> &#8211; One cluster node serves as an IPsec tunnel endpoint. </p>
<p> &#8211; All other nodes use the IPsec tunnel to reach hosts in a specific remote network. </p>
<p> Then, here is how you would implement this scheme making use of the Route resource agent: </p>
<p> &#8211; Configure an ipsec LSB resource. </p>
<p> &#8211; Configure a cloned Route OCF resource. </p>
<p> &#8211; Create an order constraint to ensure that ipsec is started before Route. </p>
<p> &#8211; Create a colocation constraint between the ipsec and Route resources, to make sure no instance of your cloned Route resource is started on the tunnel endpoint itself.</p>
<h2>Supported Parameters</h2>
<p><code>destination</code></p>
<dl>
<dd>The destination network (or host) to be configured for the route. Specify the netmask suffix in CIDR notation (e.g. &quot;/24&quot;). If no suffix is given, a host route will be created. Specify &quot;0.0.0.0/0&quot; or &quot;default&quot; if you want this resource to set the system default route. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>device</code></p>
<dl>
<dd>The outgoing network device to use for this route. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>gateway</code></p>
<dl>
<dd>The gateway IP address to use for this route. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>source</code></p>
<dl>
<dd>The source IP address to be configured for the route. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>table</code></p>
<dl>
<dd>The routing table to be configured for the route. </p>
<p> (optional, string, no default)</dl>
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
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Route resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Route ocf:heartbeat:Route \
 params \
 destination=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Route resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Route ocf:heartbeat:Route \
 destination=<i>string</i> \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Route_(resource_agent)">http://www.linux-ha.org/wiki/Route_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
