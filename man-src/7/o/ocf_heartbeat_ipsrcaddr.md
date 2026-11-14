---
title: "ocf_heartbeat_ipsrcaddr(7)"
name: "ocf_heartbeat_ipsrcaddr"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ipsrcaddr/"
description: "ocf_heartbeat_IPsrcaddr – Manages the preferred source address for outgoing IP packets"
---

<p>ocf_heartbeat_IPsrcaddr &#8211; Manages the preferred source address for outgoing IP packets</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>IPsrcaddr</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for IPsrcaddr. It manages the preferred source address modification.</p>
<h2>Supported Parameters</h2>
<p><code>ipaddress</code></p>
<dl>
<dd>The IP address. </p>
<p> (required, string, no default)</dl>
<p> <code>cidr_netmask</code></p>
<dl>
<dd>The netmask for the interface in CIDR format. (ie, 24), or in dotted quad notation 255.255.255.0). </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a IPsrcaddr resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_IPsrcaddr ocf:heartbeat:IPsrcaddr \
 params \
 ipaddress=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a IPsrcaddr resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_IPsrcaddr ocf:heartbeat:IPsrcaddr \
 ipaddress=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/IPsrcaddr_(resource_agent)">http://www.linux-ha.org/wiki/IPsrcaddr_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
