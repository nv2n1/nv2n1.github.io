---
title: "ocf_heartbeat_ipaddr2(7)"
name: "ocf_heartbeat_ipaddr2"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ipaddr2/"
description: "ocf_heartbeat_IPaddr2 – Manages virtual IPv4 and IPv6 addresses (Linux specific version)"
---

<p>ocf_heartbeat_IPaddr2 &#8211; Manages virtual IPv4 and IPv6 addresses (Linux specific version)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>IPaddr2</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This Linux-specific resource manages IP alias IP addresses. It can add an IP alias, or remove one. In addition, it can implement Cluster Alias IP functionality if invoked as a clone resource. </p>
<p> If used as a clone, you should explicitly set clone-node-max &gt;= 2, and/or clone-max &lt; number of nodes. In case of node failure, clone instances need to be re-allocated on surviving nodes. This would not be possible if there is already an instance on those nodes, and clone-node-max=1 (which is the default).</p>
<h2>Supported Parameters</h2>
<p><code>ip</code></p>
<dl>
<dd>The IPv4 (dotted quad notation) or IPv6 address (colon hexadecimal notation) example IPv4 &quot;192.168.1.1&quot;. example IPv6 &quot;2001:db8:DC28:0:0:FC57:D4C8:1FFF&quot;. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>nic</code></p>
<dl>
<dd>The base network interface on which the IP address will be brought online. If left empty, the script will try and determine this from the routing table. </p>
<p> Do NOT specify an alias interface in the form eth0:1 or anything here; rather, specify the base interface only. If you want a label, see the iflabel parameter. </p>
<p> Prerequisite: </p>
<p> There must be at least one static IP address, which is not managed by the cluster, assigned to the network interface. If you can not assign any static IP address on the interface, modify this kernel parameter: </p>
<p> sysctl -w net.ipv4.conf.all.promote_secondaries=1 # (or per device) </p>
<p> (optional, string, no default)</dl>
<p> <code>cidr_netmask</code></p>
<dl>
<dd>The netmask for the interface in CIDR format (e.g., 24 and not 255.255.255.0) </p>
<p> If unspecified, the script will also try to determine this from the routing table. </p>
<p> (optional, string, no default)</dl>
<p> <code>broadcast</code></p>
<dl>
<dd>Broadcast address associated with the IP. If left empty, the script will determine this from the netmask. </p>
<p> (optional, string, no default)</dl>
<p> <code>iflabel</code></p>
<dl>
<dd>You can specify an additional label for your IP address here. This label is appended to your interface name. </p>
<p> A label can be specified in nic parameter but it is deprecated. If a label is specified in nic name, this parameter has no effect. </p>
<p> (optional, string, no default)</dl>
<p> <code>lvs_support</code></p>
<dl>
<dd>Enable support for LVS Direct Routing configurations. In case a IP address is stopped, only move it to the loopback device to allow the local node to continue to service requests, but no longer advertise it on the network. </p>
<p> Notes for IPv6: It is not necessary to enable this option on IPv6. Instead, enable &#8216;lvs_ipv6_addrlabel&#8217; option for LVS-DR usage on IPv6. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>lvs_ipv6_addrlabel</code></p>
<dl>
<dd>Enable adding IPv6 address label so IPv6 traffic originating from the address&#8217;s interface does not use this address as the source. This is necessary for LVS-DR health checks to realservers to work. Without it, the most recently added IPv6 address (probably the address added by IPaddr2) will be used as the source address for IPv6 traffic from that interface and since that address exists on loopback on the realservers, the realserver response to pings/connections will never leave its loopback. See RFC3484 for the detail of the source address selection. </p>
<p> See also &#8216;lvs_ipv6_addrlabel_value&#8217; parameter. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>lvs_ipv6_addrlabel_value</code></p>
<dl>
<dd>Specify IPv6 address label value used when &#8216;lvs_ipv6_addrlabel&#8217; is enabled. The value should be an unused label in the policy table which is shown by &#8216;ip addrlabel list&#8217; command. You would rarely need to change this parameter. </p>
<p> (optional, integer, default 99)</dl>
<p> <code>mac</code></p>
<dl>
<dd>Set the interface MAC address explicitly. Currently only used in case of the Cluster IP Alias. Leave empty to chose automatically. </p>
<p> (optional, string, no default)</dl>
<p> <code>clusterip_hash</code></p>
<dl>
<dd>Specify the hashing algorithm used for the Cluster IP functionality. </p>
<p> (optional, string, default &quot;sourceip-sourceport&quot;)</dl>
<p> <code>unique_clone_address</code></p>
<dl>
<dd>If true, add the clone ID to the supplied value of IP to create a unique address to manage </p>
<p> (optional, boolean, default false)</dl>
<p> <code>arp_interval</code></p>
<dl>
<dd>Specify the interval between unsolicited ARP packets in milliseconds. </p>
<p> (optional, integer, default 200)</dl>
<p> <code>arp_count</code></p>
<dl>
<dd>Number of unsolicited ARP packets to send. </p>
<p> (optional, integer, default 5)</dl>
<p> <code>arp_bg</code></p>
<dl>
<dd>Whether or not to send the ARP packets in the background. </p>
<p> (optional, string, default &quot;true&quot;)</dl>
<p> <code>arp_mac</code></p>
<dl>
<dd>MAC address to send the ARP packets to. </p>
<p> You really shouldn&#8217;t be touching this. </p>
<p> (optional, string, default &quot;ffffffffffff&quot;)</dl>
<p> <code>arp_sender</code></p>
<dl>
<dd>The program to send ARP packets with on start. For infiniband interfaces, default is ipoibarping. If ipoibarping is not available, set this to send_arp. </p>
<p> (optional, string, no default)</dl>
<p> <code>flush_routes</code></p>
<dl>
<dd>Flush the routing table on stop. This is for applications which use the cluster IP address and which run on the same physical host that the IP address lives on. The Linux kernel may force that application to take a shortcut to the local loopback interface, instead of the interface the address is really bound to. Under those circumstances, an application may, somewhat unexpectedly, continue to use connections for some time even after the IP address is deconfigured. Set this parameter in order to immediately disable said shortcut when the IP address goes away. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>preferred_lft</code></p>
<dl>
<dd>For IPv6, set the preferred lifetime of the IP address. This can be used to ensure that the created IP address will not be used as a source address for routing. Expects a value as specified in section 5.5.4 of RFC 4862. </p>
<p> (optional, string, default &quot;forever&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 20s. Suggested interval: 10s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a IPaddr2 resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_IPaddr2 ocf:heartbeat:IPaddr2 \
 params \
 ip=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a IPaddr2 resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_IPaddr2 ocf:heartbeat:IPaddr2 \
 ip=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/IPaddr2_(resource_agent)">http://www.linux-ha.org/wiki/IPaddr2_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
