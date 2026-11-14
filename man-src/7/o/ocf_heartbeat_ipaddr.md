---
title: "ocf_heartbeat_ipaddr(7)"
name: "ocf_heartbeat_ipaddr"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ipaddr/"
description: "ocf_heartbeat_IPaddr – Manages virtual IPv4 addresses (portable version)"
---

<p>ocf_heartbeat_IPaddr &#8211; Manages virtual IPv4 addresses (portable version)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>IPaddr</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages IP alias IP addresses It can add an IP alias, or remove one.</p>
<h2>Supported Parameters</h2>
<p><code>ip</code></p>
<dl>
<dd>The IPv4 address to be configured in dotted quad notation, for example &quot;192.168.1.1&quot;. (required, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The base network interface on which the IP address will be brought online. If left empty, the script will try and determine this from the routing table. Do NOT specify an alias interface in the form eth0:1 or anything here; rather, specify the base interface only. Prerequisite: There must be at least one static IP address, which is not managed by the cluster, assigned to the network interface. If you can not assign any static IP address on the interface, modify this kernel parameter: sysctl -w net.ipv4.conf.all.promote_secondaries=1 (or per device) (optional, string, default eth0)</dl>
<p> <code>cidr_netmask</code></p>
<dl>
<dd>The netmask for the interface in CIDR format. (ie, 24), or in dotted quad notation 255.255.255.0). If unspecified, the script will also try to determine this from the routing table. (optional, string, no default)</dl>
<p> <code>broadcast</code></p>
<dl>
<dd>Broadcast address associated with the IP. If left empty, the script will determine this from the netmask. (optional, string, no default)</dl>
<p> <code>iflabel</code></p>
<dl>
<dd>You can specify an additional label for your IP address here. (optional, string, no default)</dl>
<p> <code>lvs_support</code></p>
<dl>
<dd>Enable support for LVS Direct Routing configurations. In case a IP address is stopped, only move it to the loopback device to allow the local node to continue to service requests, but no longer advertise it on the network. (optional, boolean, default false)</dl>
<p> <code>local_stop_script</code></p>
<dl>
<dd>Script called when the IP is released (optional, string, no default)</dl>
<p> <code>local_start_script</code></p>
<dl>
<dd>Script called when the IP is added (optional, string, no default)</dl>
<p> <code>ARP_INTERVAL_MS</code></p>
<dl>
<dd>milliseconds between ARPs (optional, integer, default 500)</dl>
<p> <code>ARP_REPEAT</code></p>
<dl>
<dd>How many gratuitous ARPs to send out when bringing up a new address (optional, integer, default 10)</dl>
<p> <code>ARP_BACKGROUND</code></p>
<dl>
<dd>run in background (no longer any reason to do this) (optional, boolean, default yes)</dl>
<p> <code>ARP_NETMASK</code></p>
<dl>
<dd>netmask for ARP &#8211; in nonstandard hexadecimal format. (optional, string, default ffffffffffff)</dl>
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
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a IPaddr resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_IPaddr ocf:heartbeat:IPaddr \
params \
ip=string \
op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;5s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/IPaddr_(resource_agent)">http://www.linux-ha.org/wiki/IPaddr_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
