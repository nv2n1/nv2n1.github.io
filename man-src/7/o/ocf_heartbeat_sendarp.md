---
title: "ocf_heartbeat_sendarp(7)"
name: "ocf_heartbeat_sendarp"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sendarp/"
description: "ocf_heartbeat_SendArp – Broadcasts unsolicited ARP announcements"
---

<p>ocf_heartbeat_SendArp &#8211; Broadcasts unsolicited ARP announcements</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SendArp</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This RA can be used _instead_ of the IPaddr2 or IPaddr RA to send gratuitous ARP for an IP address on a given interface, without adding the address to that interface. For example, if for some resaon you wanted to send gratuitous ARP for addresses managed by IPaddr2 or IPaddr on an additional interface.</p>
<h2>Supported Parameters</h2>
<p><code>ip</code></p>
<dl>
<dd>The IP address for sending ARP packet. </p>
<p> (required, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The NIC for sending ARP packet. </p>
<p> (required, string, no default)</dl>
<p> <code>background</code></p>
<dl>
<dd>Send ARPs in background. Set to false if you want to test if sending ARPs succeeded. </p>
<p> (optional, boolean, default true)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a SendArp resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_SendArp ocf:heartbeat:SendArp \
 params \
 ip=<i>string</i> \
 nic=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a SendArp resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_SendArp ocf:heartbeat:SendArp \
 ip=<i>string</i> \
 nic=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/SendArp_(resource_agent)">http://www.linux-ha.org/wiki/SendArp_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
