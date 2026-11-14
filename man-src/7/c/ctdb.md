---
title: "ctdb(7)"
name: "ctdb"
section: "7"
letter: "c"
url: "/docs/linux/man/7-ctdb/"
description: "ctdb – Clustered TDB"
---

<p>ctdb &#8211; Clustered TDB</p>
<h2>Description</h2>
<p>CTDB is a clustered database component in clustered Samba that provides a high-availability load-sharing CIFS server cluster. </p>
<p> The main functions of CTDB are: </p>
<dl>
<dd>&bull; Provide a clustered version of the TDB database with automatic rebuild/recovery of the databases upon node failures.</dl>
<dl>
<dd>&bull; Monitor nodes in the cluster and services running on each node.</dl>
<dl>
<dd>&bull; Manage a pool of public IP addresses that are used to provide services to clients. Alternatively, CTDB can be used with LVS.</dl>
<p> Combined with a cluster filesystem CTDB provides a full high-availablity (HA) environment for services such as clustered Samba, NFS and other services.</p>
<h2>Anatomy Of A Ctdb Cluster</h2>
<p>A CTDB cluster is a collection of nodes with 2 or more network interfaces. All nodes provide network (usually file/NAS) services to clients. Data served by file services is stored on shared storage (usually a cluster filesystem) that is accessible by all nodes. </p>
<p> CTDB provides an &quot;all active&quot; cluster, where services are load balanced across all nodes.</p>
<h2>Recovery Lock</h2>
<p>CTDB uses a <i>recovery lock</i> to avoid a <i>split brain</i>, where a cluster becomes partitioned and each partition attempts to operate independently. Issues that can result from a split brain include file data corruption, because file locking metadata may not be tracked correctly. </p>
<p> CTDB uses a <i>cluster leader and follower</i> model of cluster management. All nodes in a cluster elect one node to be the leader. The leader node coordinates privileged operations such as database recovery and IP address failover. CTDB refers to the leader node as the <i>recovery master</i>. This node takes and holds the recovery lock to assert its privileged role in the cluster. </p>
<p> The recovery lock is implemented using a file residing in shared storage (usually) on a cluster filesystem. To support a recovery lock the cluster filesystem must support lock coherence. See <code><a href="/docs/linux/man/1-ping_pong/">ping_pong</a></code>(1) for more details. </p>
<p> If a cluster becomes partitioned (for example, due to a communication failure) and a different recovery master is elected by the nodes in each partition, then only one of these recovery masters will be able to take the recovery lock. The recovery master in the &quot;losing&quot; partition will not be able to take the recovery lock and will be excluded from the cluster. The nodes in the &quot;losing&quot; partition will elect each node in turn as their recovery master so eventually all the nodes in that partition will be excluded. </p>
<p> CTDB does sanity checks to ensure that the recovery lock is held as expected. </p>
<p> CTDB can run without a recovery lock but this is not recommended as there will be no protection from split brains.</p>
<h2>Private Vs Public Addresses</h2>
<p>Each node in a CTDB cluster has multiple IP addresses assigned to it: </p>
<dl>
<dd>&bull; A single private IP address that is used for communication between nodes.</dl>
<dl>
<dd>&bull; One or more public IP addresses that are used to provide NAS or other services.</dl>
<h3>Private address</h3>
<p>Each node is configured with a unique, permanently assigned private address. This address is configured by the operating system. This address uniquely identifies a physical node in the cluster and is the address that CTDB daemons will use to communicate with the CTDB daemons on other nodes. </p>
<p> Private addresses are listed in the file specified by the <i>CTDB_NODES</i> configuration variable (see <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5), default /etc/ctdb/nodes). This file contains the list of private addresses for all nodes in the cluster, one per line. This file must be the same on all nodes in the cluster. </p>
<p> Private addresses should not be used by clients to connect to services provided by the cluster. </p>
<p> It is strongly recommended that the private addresses are configured on a private network that is separate from client networks. </p>
<p> Example /etc/ctdb/nodes for a four node cluster: </p>
<dl>
<dd>
<pre>192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4</pre>
</dl>
<h3>Public addresses</h3>
<p>Public addresses are used to provide services to clients. Public addresses are not configured at the operating system level and are not permanently associated with a particular node. Instead, they are managed by CTDB and are assigned to interfaces on physical nodes at runtime. </p>
<p> The CTDB cluster will assign/reassign these public addresses across the available healthy nodes in the cluster. When one node fails, its public addresses will be taken over by one or more other nodes in the cluster. This ensures that services provided by all public addresses are always available to clients, as long as there are nodes available capable of hosting this address. </p>
<p> The public address configuration is stored in a file on each node specified by the <i>CTDB_PUBLIC_ADDRESSES</i> configuration variable (see <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5), recommended /etc/ctdb/public_addresses). This file contains a list of the public addresses that the node is capable of hosting, one per line. Each entry also contains the netmask and the interface to which the address should be assigned. </p>
<p> Example /etc/ctdb/public_addresses for a node that can host 4 public addresses, on 2 different interfaces: </p>
<dl>
<dd>
<pre>10.1.1.1/24 eth1
10.1.1.2/24 eth1
10.1.2.1/24 eth2
10.1.2.2/24 eth2</pre>
</dl>
<p> In many cases the public addresses file will be the same on all nodes. However, it is possible to use different public address configurations on different nodes. </p>
<p> Example: 4 nodes partitioned into two subgroups: </p>
<dl>
<dd>
<pre>Node 0:/etc/ctdb/public_addresses
 10.1.1.1/24 eth1
 10.1.1.2/24 eth1
Node 1:/etc/ctdb/public_addresses
 10.1.1.1/24 eth1
 10.1.1.2/24 eth1
Node 2:/etc/ctdb/public_addresses
 10.1.2.1/24 eth2
 10.1.2.2/24 eth2
Node 3:/etc/ctdb/public_addresses
 10.1.2.1/24 eth2
 10.1.2.2/24 eth2</pre>
</dl>
<p> In this example nodes 0 and 1 host two public addresses on the 10.1.1.x network while nodes 2 and 3 host two public addresses for the 10.1.2.x network. </p>
<p> Public address 10.1.1.1 can be hosted by either of nodes 0 or 1 and will be available to clients as long as at least one of these two nodes are available. </p>
<p> If both nodes 0 and 1 become unavailable then public address 10.1.1.1 also becomes unavailable. 10.1.1.1 can not be failed over to nodes 2 or 3 since these nodes do not have this public address configured. </p>
<p> The <code>ctdb ip</code> command can be used to view the current assignment of public addresses to physical nodes.</p>
<h2>Node Status</h2>
<p>The current status of each node in the cluster can be viewed by the <code>ctdb status</code> command. </p>
<p> A node can be in one of the following states: </p>
<p> OK</p>
<dl>
<dd>This node is healthy and fully functional. It hosts public addresses to provide services.</dl>
<p> DISCONNECTED</p>
<dl>
<dd>This node is not reachable by other nodes via the private network. It is not currently participating in the cluster. It <i>does not</i> host public addresses to provide services. It might be shut down.</dl>
<p> DISABLED</p>
<dl>
<dd>This node has been administratively disabled. This node is partially functional and participates in the cluster. However, it <i>does not</i> host public addresses to provide services.</dl>
<p> UNHEALTHY</p>
<dl>
<dd>A service provided by this node has failed a health check and should be investigated. This node is partially functional and participates in the cluster. However, it <i>does not</i> host public addresses to provide services. Unhealthy nodes should be investigated and may require an administrative action to rectify.</dl>
<p> BANNED</p>
<dl>
<dd>CTDB is not behaving as designed on this node. For example, it may have failed too many recovery attempts. Such nodes are banned from participating in the cluster for a configurable time period before they attempt to rejoin the cluster. A banned node <i>does not</i> host public addresses to provide services. All banned nodes should be investigated and may require an administrative action to rectify.</dl>
<p> STOPPED</p>
<dl>
<dd>This node has been administratively exclude from the cluster. A stopped node does no participate in the cluster and <i>does not</i> host public addresses to provide services. This state can be used while performing maintenance on a node.</dl>
<p> PARTIALLYONLINE</p>
<dl>
<dd>A node that is partially online participates in a cluster like a healthy (OK) node. Some interfaces to serve public addresses are down, but at least one interface is up. See also <code>ctdb ifaces</code>.</dl>
<h2>Capabilities</h2>
<p>Cluster nodes can have several different capabilities enabled. These are listed below. </p>
<p> RECMASTER</p>
<dl>
<dd>Indicates that a node can become the CTDB cluster recovery master. The current recovery master is decided via an election held by all active nodes with this capability. </p>
<p> Default is YES.</dl>
<p> LMASTER</p>
<dl>
<dd>Indicates that a node can be the location master (LMASTER) for database records. The LMASTER always knows which node has the latest copy of a record in a volatile database. </p>
<p> Default is YES.</dl>
<p> LVS</p>
<dl>
<dd>Indicates that a node is configued in Linux Virtual Server (LVS) mode. In this mode the entire CTDB cluster uses one single public address for the entire cluster instead of using multiple public addresses in failover mode. This is an alternative to using a load-balancing layer-4 switch. See the LVS section for more details.</dl>
<p> The RECMASTER and LMASTER capabilities can be disabled when CTDB is used to create a cluster spanning across WAN links. In this case CTDB acts as a WAN accelerator.</p>
<h2>Lvs</h2>
<p>LVS is a mode where CTDB presents one single IP address for the entire cluster. This is an alternative to using public IP addresses and round-robin DNS to loadbalance clients across the cluster. </p>
<p> This is similar to using a layer-4 loadbalancing switch but with some restrictions. </p>
<p> In this mode the cluster selects a set of nodes in the cluster and loadbalance all client access to the LVS address across this set of nodes. This set of nodes are all LVS capable nodes that are HEALTHY, or if no HEALTHY nodes exists all LVS capable nodes regardless of health status. LVS will however never loadbalance traffic to nodes that are BANNED, STOPPED, DISABLED or DISCONNECTED. The <code>ctdb lvs</code> command is used to show which nodes are currently load-balanced across. </p>
<p> One of the these nodes are elected as the LVSMASTER. This node receives all traffic from clients coming in to the LVS address and multiplexes it across the internal network to one of the nodes that LVS is using. When responding to the client, that node will send the data back directly to the client, bypassing the LVSMASTER node. The command <code>ctdb lvsmaster</code> will show which node is the current LVSMASTER. </p>
<p> The path used for a client I/O is: </p>
<dl>
<dd>1. Client sends request packet to LVSMASTER.</dl>
<dl>
<dd>2. LVSMASTER passes the request on to one node across the internal network.</dl>
<dl>
<dd>3. Selected node processes the request.</dl>
<dl>
<dd>4. Node responds back to client.</dl>
<p> This means that all incoming traffic to the cluster will pass through one physical node, which limits scalability. You can send more data to the LVS address that one physical node can multiplex. This means that you should not use LVS if your I/O pattern is write-intensive since you will be limited in the available network bandwidth that node can handle. LVS does work wery well for read-intensive workloads where only smallish READ requests are going through the LVSMASTER bottleneck and the majority of the traffic volume (the data in the read replies) goes straight from the processing node back to the clients. For read-intensive i/o patterns you can acheive very high throughput rates in this mode. </p>
<p> Note: you can use LVS and public addresses at the same time. </p>
<p> If you use LVS, you must have a permanent address configured for the public interface on each node. This address must be routable and the cluster nodes must be configured so that all traffic back to client hosts are routed through this interface. This is also required in order to allow samba/winbind on the node to talk to the domain controller. This LVS IP address can not be used to initiate outgoing traffic. </p>
<p> Make sure that the domain controller and the clients are reachable from a node <i>before</i> you enable LVS. Also ensure that outgoing traffic to these hosts is routed out through the configured public interface.</p>
<h3>Configuration</h3>
<p>To activate LVS on a CTDB node you must specify the <i>CTDB_PUBLIC_INTERFACE</i> and <i>CTDB_LVS_PUBLIC_IP</i> configuration variables. Setting the latter variable also enables the LVS capability on the node at startup. </p>
<p> Example: </p>
<dl>
<dd>
<pre>CTDB_PUBLIC_INTERFACE=eth1
CTDB_LVS_PUBLIC_IP=10.1.1.237</pre>
</dl>
<h2>Tracking And Resetting Tcp Connections</h2>
<p>CTDB tracks TCP connections from clients to public IP addresses, on known ports. When an IP address moves from one node to another, all existing TCP connections to that IP address are reset. The node taking over this IP address will also send gratuitous ARPs (for IPv4, or neighbour advertisement, for IPv6). This allows clients to reconnect quickly, rather than waiting for TCP timeouts, which can be very long. </p>
<p> It is important that established TCP connections do not survive a release and take of a public IP address on the same node. Such connections can get out of sync with sequence and ACK numbers, potentially causing a disruptive ACK storm.</p>
<h2>Nat Gateway</h2>
<p>NAT gateway (NATGW) is an optional feature that is used to configure fallback routing for nodes. This allows cluster nodes to connect to external services (e.g. DNS, AD, NIS and LDAP) when they do not host any public addresses (e.g. when they are unhealthy). </p>
<p> This also applies to node startup because CTDB marks nodes as UNHEALTHY until they have passed a &quot;monitor&quot; event. In this context, NAT gateway helps to avoid a &quot;chicken and egg&quot; situation where a node needs to access an external service to become healthy. </p>
<p> Another way of solving this type of problem is to assign an extra static IP address to a public interface on every node. This is simpler but it uses an extra IP address per node, while NAT gateway generally uses only one extra IP address.</p>
<h3>Operation</h3>
<p>One extra NATGW public address is assigned on the public network to each NATGW group. Each NATGW group is a set of nodes in the cluster that shares the same NATGW address to talk to the outside world. Normally there would only be one NATGW group spanning an entire cluster, but in situations where one CTDB cluster spans multiple physical sites it might be useful to have one NATGW group for each site. </p>
<p> There can be multiple NATGW groups in a cluster but each node can only be member of one NATGW group. </p>
<p> In each NATGW group, one of the nodes is selected by CTDB to be the NATGW master and the other nodes are consider to be NATGW slaves. NATGW slaves establish a fallback default route to the NATGW master via the private network. When a NATGW slave hosts no public IP addresses then it will use this route for outbound connections. The NATGW master hosts the NATGW public IP address and routes outgoing connections from slave nodes via this IP address. It also establishes a fallback default route.</p>
<h3>Configuration</h3>
<p>NATGW is usually configured similar to the following example configuration: </p>
<dl>
<dd>
<pre>CTDB_NATGW_NODES=/etc/ctdb/natgw_nodes
CTDB_NATGW_PRIVATE_NETWORK=192.168.1.0/24
CTDB_NATGW_PUBLIC_IP=10.0.0.227/24
CTDB_NATGW_PUBLIC_IFACE=eth0
CTDB_NATGW_DEFAULT_GATEWAY=10.0.0.1</pre>
</dl>
<p> Normally any node in a NATGW group can act as the NATGW master. Some configurations may have special nodes that lack connectivity to a public network. In such cases, those nodes can be flagged with the &quot;slave-only&quot; option in the <i>CTDB_NATGW_NODES</i> file to limit the NATGW functionality of those nodes. </p>
<p> See the NAT GATEWAY section in <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5) for more details of NATGW configuration.</p>
<h3>Implementation details</h3>
<p>When the NATGW functionality is used, one of the nodes is selected to act as a NAT gateway for all the other nodes in the group when they need to communicate with the external services. The NATGW master is selected to be a node that is most likely to have usable networks. </p>
<p> The NATGW master hosts the NATGW public IP address <i>CTDB_NATGW_PUBLIC_IP</i> on the configured public interfaces <i>CTDB_NATGW_PUBLIC_IFACE</i> and acts as a router, masquerading outgoing connections from slave nodes via this IP address. If <i>CTDB_NATGW_DEFAULT_GATEWAY</i> is set then it also establishes a fallback default route to the configured this gateway with a metric of 10. A metric 10 route is used so it can co-exist with other default routes that may be available. </p>
<p> A NATGW slave establishes its fallback default route to the NATGW master via the private network <i>CTDB_NATGW_PRIVATE_NETWORK</i>with a metric of 10. This route is used for outbound connections when no other default route is available because the node hosts no public addresses. A metric 10 routes is used so that it can co-exist with other default routes that may be available when the node is hosting public addresses. </p>
<p> <i>CTDB_NATGW_STATIC_ROUTES</i> can be used to have NATGW create more specific routes instead of just default routes. </p>
<p> This is implemented in the 11.natgw eventscript. Please see the eventscript file and the NAT GATEWAY section in <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5) for more details.</p>
<h2>Policy Routing</h2>
<p>Policy routing is an optional CTDB feature to support complex network topologies. Public addresses may be spread across several different networks (or VLANs) and it may not be possible to route packets from these public addresses via the system&#8217;s default route. Therefore, CTDB has support for policy routing via the 13.per_ip_routing eventscript. This allows routing to be specified for packets sourced from each public address. The routes are added and removed as CTDB moves public addresses between nodes.</p>
<h3>Configuration variables</h3>
<p>There are 4 configuration variables related to policy routing: <i>CTDB_PER_IP_ROUTING_CONF</i>, <i>CTDB_PER_IP_ROUTING_RULE_PREF</i>, <i>CTDB_PER_IP_ROUTING_TABLE_ID_LOW</i>, <i>CTDB_PER_IP_ROUTING_TABLE_ID_HIGH</i>. See the POLICY ROUTING section in <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5) for more details.</p>
<h3>Configuration</h3>
<p>The format of each line of <i>CTDB_PER_IP_ROUTING_CONF</i> is: </p>
<dl>
<dd>
<pre>&lt;public_address&gt; &lt;network&gt; [ &lt;gateway&gt; ]</pre>
</dl>
<p> Leading whitespace is ignored and arbitrary whitespace may be used as a separator. Lines that have a &quot;public address&quot; item that doesn&#8217;t match an actual public address are ignored. This means that comment lines can be added using a leading character such as &#8216;#&#8217;, since this will never match an IP address. </p>
<p> A line without a gateway indicates a link local route. </p>
<p> For example, consider the configuration line: </p>
<dl>
<dd>
<pre> 192.168.1.99 192.168.1.1/24</pre>
</dl>
<p> If the corresponding public_addresses line is: </p>
<dl>
<dd>
<pre> 192.168.1.99/24 eth2,eth3</pre>
</dl>
<p> <i>CTDB_PER_IP_ROUTING_RULE_PREF</i> is 100, and CTDB adds the address to eth2 then the following routing information is added: </p>
<dl>
<dd>
<pre> ip rule add from 192.168.1.99 pref 100 table ctdb.192.168.1.99
 ip route add 192.168.1.0/24 dev eth2 table ctdb.192.168.1.99</pre>
</dl>
<p> This causes traffic from 192.168.1.1 to 192.168.1.0/24 go via eth2. </p>
<p> The <code>ip rule</code> command will show (something like &#8211; depending on other public addresses and other routes on the system): </p>
<dl>
<dd>
<pre> 0: from all lookup local 
 100: from 192.168.1.99 lookup ctdb.192.168.1.99
 32766: from all lookup main 
 32767: from all lookup default </pre>
</dl>
<p> <code>ip route show table ctdb.192.168.1.99</code> will show: </p>
<dl>
<dd>
<pre> 192.168.1.0/24 dev eth2 scope link</pre>
</dl>
<p> The usual use for a line containing a gateway is to add a default route corresponding to a particular source address. Consider this line of configuration: </p>
<dl>
<dd>
<pre> 192.168.1.99 0.0.0.0/0 192.168.1.1</pre>
</dl>
<p> In the situation described above this will cause an extra routing command to be executed: </p>
<dl>
<dd>
<pre> ip route add 0.0.0.0/0 via 192.168.1.1 dev eth2 table ctdb.192.168.1.99</pre>
</dl>
<p> With both configuration lines, <code>ip route show table ctdb.192.168.1.99</code> will show: </p>
<dl>
<dd>
<pre> 192.168.1.0/24 dev eth2 scope link 
 default via 192.168.1.1 dev eth2 </pre>
</dl>
<h3>Sample configuration</h3>
<p>Here is a more complete example configuration. </p>
<dl>
<dd>
<pre>/etc/ctdb/public_addresses:
 192.168.1.98 eth2,eth3
 192.168.1.99 eth2,eth3
/etc/ctdb/policy_routing:
 192.168.1.98 192.168.1.0/24
 192.168.1.98 192.168.200.0/24 192.168.1.254
 192.168.1.98 0.0.0.0/0 192.168.1.1
 192.168.1.99 192.168.1.0/24
 192.168.1.99 192.168.200.0/24 192.168.1.254
 192.168.1.99 0.0.0.0/0 192.168.1.1</pre>
</dl>
<p> The routes local packets as expected, the default route is as previously discussed, but packets to 192.168.200.0/24 are routed via the alternate gateway 192.168.1.254.</p>
<h2>Notification Script</h2>
<p>When certain state changes occur in CTDB, it can be configured to perform arbitrary actions via a notification script. For example, sending SNMP traps or emails when a node becomes unhealthy or similar. </p>
<p> This is activated by setting the <i>CTDB_NOTIFY_SCRIPT</i> configuration variable. The specified script must be executable. </p>
<p> Use of the provided /etc/ctdb/notify.sh script is recommended. It executes files in /etc/ctdb/notify.d/. </p>
<p> CTDB currently generates notifications after CTDB changes to these states:</p>
<dl>
<dd>init</dl>
<dl>
<dd>setup</dl>
<dl>
<dd>startup</dl>
<dl>
<dd>healthy</dl>
<dl>
<dd>unhealthy</dl>
<h2>Debug Levels</h2>
<p>Valid values for DEBUGLEVEL are:</p>
<dl>
<dd>ERR (0)</dl>
<dl>
<dd>WARNING (1)</dl>
<dl>
<dd>NOTICE (2)</dl>
<dl>
<dd>INFO (3)</dl>
<dl>
<dd>DEBUG (4)</dl>
<h2>Remote Cluster Nodes</h2>
<p>It is possible to have a CTDB cluster that spans across a WAN link. For example where you have a CTDB cluster in your datacentre but you also want to have one additional CTDB node located at a remote branch site. This is similar to how a WAN accelerator works but with the difference that while a WAN-accelerator often acts as a Proxy or a MitM, in the ctdb remote cluster node configuration the Samba instance at the remote site IS the genuine server, not a proxy and not a MitM, and thus provides 100% correct CIFS semantics to clients. </p>
<p> See the cluster as one single multihomed samba server where one of the NICs (the remote node) is very far away. </p>
<p> NOTE: This does require that the cluster filesystem you use can cope with WAN-link latencies. Not all cluster filesystems can handle WAN-link latencies! Whether this will provide very good WAN-accelerator performance or it will perform very poorly depends entirely on how optimized your cluster filesystem is in handling high latency for data and metadata operations. </p>
<p> To activate a node as being a remote cluster node you need to set the following two parameters in /etc/sysconfig/ctdb for the remote node: </p>
<dl>
<dd>
<pre>CTDB_CAPABILITY_LMASTER=no
CTDB_CAPABILITY_RECMASTER=no</pre>
</dl>
<p> Verify with the command &quot;ctdb getcapabilities&quot; that that node no longer has the recmaster or the lmaster capabilities.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ctdb/">ctdb</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/1-ctdbd_wrapper/">ctdbd_wrapper</a></code>(1), <code><a href="/docs/linux/man/1-ltdbtool/">ltdbtool</a></code>(1), <code><a href="/docs/linux/man/1-onnode/">onnode</a></code>(1), <code><a href="/docs/linux/man/1-ping_pong/">ping_pong</a></code>(1), <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5), <code><a href="/docs/linux/man/7-ctdb-statistics/">ctdb-statistics</a></code>(7), <code><a href="/docs/linux/man/7-ctdb-tunables/">ctdb-tunables</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>Author</h2>
<p>This documentation was written by Ronnie Sahlberg, Amitay Isaacs, Martin Schwenke</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[].</p>
