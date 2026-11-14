---
title: "ocf_heartbeat_ethmonitor(7)"
name: "ocf_heartbeat_ethmonitor"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ethmonitor/"
description: "ocf_heartbeat_ethmonitor – Monitors network interfaces"
---

<p>ocf_heartbeat_ethmonitor &#8211; Monitors network interfaces</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ethmonitor</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Monitor the vitality of a local network interface. </p>
<p> You may set up this RA as a clone resource to monitor the network interfaces on different nodes, with the same interface name. This is not related to the IP address or the network on which a interface is configured. You may use this RA to move resources away from a node, which has a faulty interface or prevent moving resources to such a node. This gives you independend control of the resources, without involving cluster intercommunication. But it requires your nodes to have more than one network interface. </p>
<p> The resource configuration requires a monitor operation, because the monitor does the main part of the work. In addition to the resource configuration, you need to configure some location constraints, based on a CIB attribute value. The name of the attribute value is configured in the &#8216;name&#8217; option of this RA. </p>
<p> Example constraint configuration using crmsh location loc_connected_node my_resource_grp rule =&quot;rule_loc_connected_node&quot; -INF: ethmonitor eq 0 </p>
<p> Example constraint configuration using pcs. Only allow &#8216;my_resource&#8217; to run on nodes where eth0 ethernet device is available. pcs constraint location my_resource rule score=-INFINITY ethmonitor-eth0 ne 1 </p>
<p> The ethmonitor works in 3 different modes to test the interface vitality. 1. call ip to see if the link status is up (if link is down -&gt; error) 2. call ip and watch the RX counter (if packages come around in a certain time -&gt; success) 3. call arping to check whether any of the IPs found in the local ARP cache answers an ARP REQUEST (one answer -&gt; success) 4. return error</p>
<h2>Supported Parameters</h2>
<p><code>interface</code></p>
<dl>
<dd>The name of the network interface which should be monitored (e.g. eth0). </p>
<p> (unique, required, string, no default)</dl>
<p> <code>name</code></p>
<dl>
<dd>The name of the CIB attribute to set. This is the name to be used in the constraints. Defaults to &quot;ethmonitor-&#8216;interface_name&#8217;&quot;. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>multiplier</code></p>
<dl>
<dd>Multiplier for the value of the CIB attriobute specified in parameter name. </p>
<p> (optional, integer, default 1)</dl>
<p> <code>repeat_count</code></p>
<dl>
<dd>Specify how often the interface will be monitored, before the status is set to failed. You need to set the timeout of the monitoring operation to at least repeat_count * repeat_interval </p>
<p> (optional, integer, default 5)</dl>
<p> <code>repeat_interval</code></p>
<dl>
<dd>Specify how long to wait in seconds between the repeat_counts. </p>
<p> (optional, integer, default 10)</dl>
<p> <code>pktcnt_timeout</code></p>
<dl>
<dd>Timeout for the RX packet counter. Stop listening for packet counter changes after the given number of seconds. </p>
<p> (optional, integer, default 5)</dl>
<p> <code>arping_count</code></p>
<dl>
<dd>Number of ARP REQUEST packets to send for every IP. Usually one ARP REQUEST (arping) is send </p>
<p> (optional, integer, default 1)</dl>
<p> <code>arping_timeout</code></p>
<dl>
<dd>Time in seconds to wait for ARP REQUESTs (all packets of arping_count). This is to limit the time for arp requests, to be able to send requests to more than one node, without running in the monitor operation timeout. </p>
<p> (optional, integer, default 1)</dl>
<p> <code>arping_cache_entries</code></p>
<dl>
<dd>Maximum number of IPs from ARP cache list to check for ARP REQUEST (arping) answers. Newest entries are tried first. </p>
<p> (optional, integer, default 5)</dl>
<p> <code>infiniband_device</code></p>
<dl>
<dd>For interfaces that are infiniband devices. </p>
<p> (optional, string, no default)</dl>
<p> <code>infiniband_port</code></p>
<dl>
<dd>For infiniband devices, this is the port to monitor. </p>
<p> (optional, integer, no default)</dl>
<p> <code>link_status_only</code></p>
<dl>
<dd>Only report success based on link status. Do not perform RX counter or arping related connectivity tests. </p>
<p> (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60s. Suggested interval: 10s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60s. Suggested interval: 10s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a ethmonitor resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_ethmonitor ocf:heartbeat:ethmonitor \
 params \
 interface=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;60s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a ethmonitor resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_ethmonitor ocf:heartbeat:ethmonitor \
 interface=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;60s&quot; interval=&quot;10s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ethmonitor_(resource_agent)">http://www.linux-ha.org/wiki/ethmonitor_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
