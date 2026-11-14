---
title: "vtep(5)"
name: "vtep"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vtep/"
description: "vtep – hardware_vtep database schema"
---

<p>vtep &#8211; hardware_vtep database schema </p>
<p> This schema specifies relations that a VTEP can use to integrate physical ports into logical switches maintained by a network virtualization controller such as NSX46 </p>
<p> Glossary:</p>
<dl>
<dd>
<dl>
<dt>VTEP</p>
<dd>VXLAN Tunnel End Point, an entity which originates and/or terminates VXLAN tunnels46</p>
<dt>HSC</p>
<dd>Hardware Switch Controller46</p>
<dt>NVC</p>
<dd>Network Virtualization Controller, e46g46 NSX46</p>
<dt>VRF</p>
<dd>Virtual Routing and Forwarding instance46</dl>
</dl>
<h2>Table Summary</h2>
<p>The following list summarizes the purpose of each of the tables in the <code>hardware_vtep</code> database. Each table is described in more detail on a later page.</p>
<dl>
<dt>Table</p>
<dd>Purpose </p>
<dt> <code>Global</code></p>
<dd>Top-level configuration46 </p>
<dt> <code>Manager</code></p>
<dd>OVSDB management connection46 </p>
<dt> <code>Physical_Switch</code></p>
<dd>A physical switch46 </p>
<dt> <code>Tunnel</code></p>
<dd>A tunnel created by a physical switch46 </p>
<dt> <code>Physical_Port</code></p>
<dd>A port within a physical switch46 </p>
<dt> <code>Logical_Binding_Stats</code></p>
<dd>Statistics for a VLAN on a physical port bound to a logical network46 </p>
<dt> <code>Logical_Switch</code></p>
<dd>A layer-2 domain46 </p>
<dt> <code>Ucast_Macs_Local</code></p>
<dd>Unicast MACs (local) </p>
<dt> <code>Ucast_Macs_Remote</code></p>
<dd>Unicast MACs (remote) </p>
<dt> <code>Mcast_Macs_Local</code></p>
<dd>Multicast MACs (local) </p>
<dt> <code>Mcast_Macs_Remote</code></p>
<dd>Multicast MACs (remote) </p>
<dt> <code>Logical_Router</code></p>
<dd>A logical L3 router46 </p>
<dt> <code>Arp_Sources_Local</code></p>
<dd>ARP source addresses for logical routers </p>
<dt> <code>Arp_Sources_Remote</code></p>
<dd>ARP source addresses for logical routers </p>
<dt> <code>Physical_Locator_Set</code></p>
<dd>Physical_Locator_Set configuration46 </p>
<dt> <code>Physical_Locator</code></p>
<dd>Physical_Locator configuration46 </p>
<dt> <code>ACL_entry</code></p>
<dd>ACL_entry configuration46 </p>
<dt> <code>ACL</code></p>
<dd>ACL configuration46</dl>
<h2>Global TABLE</h2>
<p>Top-level configuration for a hardware VTEP46 There must be exactly one record in the <code>Global</code> table46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>switches</code></p>
<dd>set of <code>Physical_Switch</code>s </p>
<dt> <i>Database Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>managers</code></p>
<dd>set of <code>Manager</code>s</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>switches</code>: set of <code>Physical_Switch</code>s</p>
<dd>The physical switch or switches managed by the VTEP46</p>
<dd>When a physical switch integrates support for this VTEP schema, which is expected to be the most common case, this column should point to one <code>Physical_Switch</code> record that represents the switch itself46 In another possible implementation, a server or a VM presents a VTEP schema front-end interface to one or more physical switches, presumably communicating with those physical switches over a proprietary protocol46 In that case, this column would point to one <code>Physical_Switch</code> for each physical switch, and the set might change over time as the front-end server comes to represent a differing set of switches46</dl>
<p> <i>Database Configuration:</i> These columns primarily configure the database server (<code>ovsdb-server</code>), not the hardware VTEP itself46</p>
<dl>
<dt><code>managers</code>: set of <code>Manager</code>s</p>
<dd>Database clients to which the database server should connect or to which it should listen, along with options for how these connection should be configured46 See the <code>Manager</code> table for more information46</dl>
<h2>Manager TABLE</h2>
<p>Configuration for a database connection to an Open vSwitch Database (OVSDB) client46 </p>
<p> The database server can initiate and maintain active connections to remote clients46 It can also listen for database connections46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Core Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>target</code></p>
<dd>string (must be unique within table)</dl>
</dl>
<dt> <i>Client Failure Detection and Handling:</i></p>
<dl>
<dd>
<dl>
<dt> <code>max_backoff</code></p>
<dd>optional integer, at least 1,000 </p>
<dt> <code>inactivity_probe</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>is_connected</code></p>
<dd>boolean </p>
<dt> <code>status : last_error</code></p>
<dd>optional string </p>
<dt> <code>status : state</code></p>
<dd>optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code> </p>
<dt> <code>status : sec_since_connect</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : sec_since_disconnect</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : locks_held</code></p>
<dd>optional string </p>
<dt> <code>status : locks_waiting</code></p>
<dd>optional string </p>
<dt> <code>status : locks_lost</code></p>
<dd>optional string </p>
<dt> <code>status : n_connections</code></p>
<dd>optional string, containing an integer, at least 2</dl>
</dl>
<dt> <i>Connection Parameters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : dscp</code></p>
<dd>optional string, containing an integer</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Core Features:</i></p>
<dl>
<dt><code>target</code>: string (must be unique within table)</p>
<dd>Connection method for managers46</p>
<dd>The following connection methods are currently supported:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified SSL <i>port</i> (default: 6640) on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name)46</p>
<dd>SSL key and certificate configuration happens outside the database46</p>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified TCP <i>port</i> (default: 6640) on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name)46</p>
<dt><code>pssl:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for SSL connections on the specified TCP <i>port</i> (default: 6640)46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address46</p>
<dt><code>ptcp:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for connections on the specified TCP <i>port</i> (default: 6640)46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address46</dl>
</dl>
</dl>
<p> <i>Client Failure Detection and Handling:</i></p>
<dl>
<dt><code>max_backoff</code>: optional integer, at least 1,000</p>
<dd>Maximum number of milliseconds to wait between connection attempts46 Default is implementation-specific46</p>
<dt><code>inactivity_probe</code>: optional integer</p>
<dd>Maximum number of milliseconds of idle time on connection to the client before sending an inactivity probe message46 If the Open vSwitch database does not communicate with the client for the specified number of seconds, it will send a probe46 If a response is not received for the same additional amount of time, the database server assumes the connection has been broken and attempts to reconnect46 Default is implementation-specific46 A value of 0 disables inactivity probes46</dl>
<p> <i>Status:</i></p>
<dl>
<dt><code>is_connected</code>: boolean</p>
<dd><code>true</code> if currently connected to this manager, <code>false</code> otherwise46</p>
<dt><code>status : last_error</code>: optional string</p>
<dd>A human-readable description of the last error on the connection to the manager; i46e46 <code>strerror(errno)</code>46 This key will exist only if an error has occurred46</p>
<dt><code>status : state</code>: optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code></p>
<dd>The state of the connection to the manager:</p>
<dl>
<dd>
<dl>
<dt><code>VOID</code></p>
<dd>Connection is disabled46</p>
<dt><code>BACKOFF</code></p>
<dd>Attempting to reconnect at an increasing period46</p>
<dt><code>CONNECTING</code></p>
<dd>Attempting to connect46</p>
<dt><code>ACTIVE</code></p>
<dd>Connected, remote host responsive46</p>
<dt><code>IDLE</code></p>
<dd>Connection is idle46 Waiting for response to keep-alive46</dl>
</dl>
<dd>These values may change in the future46 They are provided only for human consumption46</p>
<dt><code>status : sec_since_connect</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time since this manager last successfully connected to the database (in seconds)46 Value is empty if manager has never successfully connected46</p>
<dt><code>status : sec_since_disconnect</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time since this manager last disconnected from the database (in seconds)46 Value is empty if manager has never disconnected46</p>
<dt><code>status : locks_held</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection holds46 Omitted if the connection does not hold any locks46</p>
<dt><code>status : locks_waiting</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection is currently waiting to acquire46 Omitted if the connection is not waiting for any locks46</p>
<dt><code>status : locks_lost</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection has had stolen by another OVSDB client46 Omitted if no locks have been stolen from this connection46</p>
<dt><code>status : n_connections</code>: optional string, containing an integer, at least 2</p>
<dd>When <code>target</code> specifies a connection method that listens for inbound connections (e46g46 <code>ptcp:</code> or <code>pssl:</code>) and more than one connection is actually active, the value is the number of active connections46 Otherwise, this key-value pair is omitted46</p>
<dd>When multiple connections are active, status columns and key-value pairs (other than this one) report the status of one arbitrarily chosen connection46</dl>
<p> <i>Connection Parameters:</i> Additional configuration for a connection between the manager and the database server46</p>
<dl>
<dt><code>other_config : dscp</code>: optional string, containing an integer</p>
<dd>The Differentiated Service Code Point (DSCP) is specified using 6 bits in the Type of Service (TOS) field in the IP header46 DSCP provides a mechanism to classify the network traffic and provide Quality of Service (QoS) on IP networks46 The DSCP value specified here is used when establishing the connection between the manager and the database server46 If no value is specified, a default value of 48 is chosen46 Valid DSCP values must be in the range 0 to 6346</dl>
<h2>Physical_Switch TABLE</h2>
<p>A physical switch that implements a VTEP46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>ports</code></p>
<dd>set of <code>Physical_Port</code>s </p>
<dt> <code>tunnels</code></p>
<dd>set of <code>Tunnel</code>s </p>
<dt> <i>Network Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>management_ips</code></p>
<dd>set of strings </p>
<dt> <code>tunnel_ips</code></p>
<dd>set of strings</dl>
</dl>
<dt> <i>Identification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>string (must be unique within table) </p>
<dt> <code>description</code></p>
<dd>string</dl>
</dl>
<dt> <i>Error Notification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>switch_fault_status : mac_table_exhaustion</code></p>
<dd>none </p>
<dt> <code>switch_fault_status : tunnel_exhaustion</code></p>
<dd>none </p>
<dt> <code>switch_fault_status : unspecified_fault</code></p>
<dd>none</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>ports</code>: set of <code>Physical_Port</code>s</p>
<dd>The physical ports within the switch46</p>
<dt><code>tunnels</code>: set of <code>Tunnel</code>s</p>
<dd>Tunnels created by this switch as instructed by the NVC46</dl>
<p> <i>Network Status:</i></p>
<dl>
<dt><code>management_ips</code>: set of strings</p>
<dd>IPv4 or IPv6 addresses at which the switch may be contacted for management purposes46</p>
<dt><code>tunnel_ips</code>: set of strings</p>
<dd>IPv4 or IPv6 addresses on which the switch may originate or terminate tunnels46</p>
<dd>This column is intended to allow a <code>Manager</code> to determine the <code>Physical_Switch</code> that terminates the tunnel represented by a <code>Physical_Locator</code>46</dl>
<p> <i>Identification:</i></p>
<dl>
<dt><code>name</code>: string (must be unique within table)</p>
<dd>Symbolic name for the switch, such as its hostname46</p>
<dt><code>description</code>: string</p>
<dd>An extended description for the switch, such as its switch login banner46</dl>
<p> <i>Error Notification:</i> An entry in this column indicates to the NVC that this switch has encountered a fault46 The switch must clear this column when the fault has been cleared46</p>
<dl>
<dt><code>switch_fault_status : mac_table_exhaustion</code>: none</p>
<dd>Indicates that the switch has been unable to process MAC entries requested by the NVC due to lack of table resources46</p>
<dt><code>switch_fault_status : tunnel_exhaustion</code>: none</p>
<dd>Indicates that the switch has been unable to create tunnels requested by the NVC due to lack of resources46</p>
<dt><code>switch_fault_status : unspecified_fault</code>: none</p>
<dd>Indicates that an error has occurred in the switch but that no more specific information is available46</dl>
<h2>Tunnel TABLE</h2>
<p>A tunnel created by a <code>Physical_Switch</code>46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>local</code> <code>Physical_Locator</code> </p>
<dt> <code>remote</code> <code>Physical_Locator</code></p>
<dd>
<dt> <i>Bidirectional Forwarding Detection (BFD):</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>BFD Local Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd_config_local : bfd_dst_mac</code></p>
<dd>optional string </p>
<dt> <code>bfd_config_local : bfd_dst_ip</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>BFD Remote Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd_config_remote : bfd_dst_mac</code></p>
<dd>optional string </p>
<dt> <code>bfd_config_remote : bfd_dst_ip</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>BFD Parameters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd_params : enable</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_params : min_rx</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>bfd_params : min_tx</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>bfd_params : decay_min_rx</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>bfd_params : forwarding_if_rx</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_params : cpath_down</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_params : check_tnl_key</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>BFD Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd_status : enabled</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_status : state</code></p>
<dd>optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code> </p>
<dt> <code>bfd_status : forwarding</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_status : diagnostic</code></p>
<dd>optional string </p>
<dt> <code>bfd_status : remote_state</code></p>
<dd>optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code> </p>
<dt> <code>bfd_status : remote_diagnostic</code></p>
<dd>optional string </p>
<dt> <code>bfd_status : info</code></p>
<dd>optional string</dl>
</dl>
</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>local</code>: <code>Physical_Locator</code></p>
<dd>Tunnel end-point local to the physical switch46</p>
<dt><code>remote</code>: <code>Physical_Locator</code></p>
<dd>Tunnel end-point remote to the physical switch46</dl>
<p> <i>Bidirectional Forwarding Detection (BFD):</i> BFD, defined in RFC 5880, allows point to point detection of connectivity failures by occasional transmission of BFD control messages46 VTEPs are expected to implement BFD46 </p>
<p> BFD operates by regularly transmitting BFD control messages at a rate negotiated independently in each direction46 Each endpoint specifies the rate at which it expects to receive control messages, and the rate at which it&#8217;s willing to transmit them46 An endpoint which fails to receive BFD control messages for a period of three times the expected reception rate will signal a connectivity fault46 In the case of a unidirectional connectivity issue, the system not receiving BFD control messages will signal the problem to its peer in the messages it transmits46 </p>
<p> A hardware VTEP is expected to use BFD to determine reachability of devices at the end of the tunnels with which it exchanges data46 This can enable the VTEP to choose a functioning service node among a set of service nodes providing high availability46 It also enables the NVC to report the health status of tunnels46 </p>
<p> In many cases the BFD peer of a hardware VTEP will be an Open vSwitch instance46 The Open vSwitch implementation of BFD aims to comply faithfully with the requirements put forth in RFC 588046 Open vSwitch does not implement the optional Authentication or &#8220;Echo Mode&#8221; features46 </p>
<p> <i>BFD Local Configuration:</i> The HSC writes the key-value pairs in the <code>bfd_config_local</code> column to specify the local configurations to be used for BFD sessions on this tunnel46</p>
<dl>
<dt><code>bfd_config_local : bfd_dst_mac</code>: optional string</p>
<dd>Set to an Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the MAC expected as destination for received BFD packets46 The default is <code>00:23:20:00:00:01</code>46</p>
<dt><code>bfd_config_local : bfd_dst_ip</code>: optional string</p>
<dd>Set to an IPv4 address to set the IP address that is expected as destination for received BFD packets46 The default is <code>16946254461460</code>46</dl>
<p> <i>BFD Remote Configuration:</i> The <code>bfd_config_remote</code> column is the remote counterpart of the <code>bfd_config_local</code> column46 The NVC writes the key-value pairs in this column46</p>
<dl>
<dt><code>bfd_config_remote : bfd_dst_mac</code>: optional string</p>
<dd>Set to an Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the destination MAC to be used for transmitted BFD packets46 The default is <code>00:23:20:00:00:01</code>46</p>
<dt><code>bfd_config_remote : bfd_dst_ip</code>: optional string</p>
<dd>Set to an IPv4 address to set the IP address used as destination for transmitted BFD packets46 The default is <code>16946254461461</code>46</dl>
<p> <i>BFD Parameters:</i> The NVC sets up key-value pairs in the <code>bfd_params</code> column to enable and configure BFD46</p>
<dl>
<dt><code>bfd_params : enable</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>True to enable BFD on this <code>Tunnel</code>46 If not specified, BFD will not be enabled by default46</p>
<dt><code>bfd_params : min_rx</code>: optional string, containing an integer, at least 1</p>
<dd>The shortest interval, in milliseconds, at which this BFD session offers to receive BFD control messages46 The remote endpoint may choose to send messages at a slower rate46 Defaults to <code>1000</code>46</p>
<dt><code>bfd_params : min_tx</code>: optional string, containing an integer, at least 1</p>
<dd>The shortest interval, in milliseconds, at which this BFD session is willing to transmit BFD control messages46 Messages will actually be transmitted at a slower rate if the remote endpoint is not willing to receive as quickly as specified46 Defaults to <code>100</code>46</p>
<dt><code>bfd_params : decay_min_rx</code>: optional string, containing an integer</p>
<dd>An alternate receive interval, in milliseconds, that must be greater than or equal to <code>bfd_params:min_rx</code>46 The implementation should switch from <code>bfd_params:min_rx</code> to <code>bfd_params:decay_min_rx</code> when there is no obvious incoming data traffic at the tunnel, to reduce the CPU and bandwidth cost of monitoring an idle tunnel46 This feature may be disabled by setting a value of 046 This feature is reset whenever <code>bfd_params:decay_min_rx</code> or <code>bfd_params:min_rx</code> changes46</p>
<dt><code>bfd_params : forwarding_if_rx</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When <code>true</code>, traffic received on the <code>Tunnel</code> is used to indicate the capability of packet I/O46 BFD control packets are still transmitted and received46 At least one BFD control packet must be received every 100 * <code>bfd_params:min_rx</code> amount of time46 Otherwise, even if traffic is received, the <code>bfd_params:forwarding</code> will be <code>false</code>46</p>
<dt><code>bfd_params : cpath_down</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to true to notify the remote endpoint that traffic should not be forwarded to this system for some reason other than a connectivity failure on the interface being monitored46 The typical underlying reason is &#8220;concatenated path down,&#8221; that is, that connectivity beyond the local system is down46 Defaults to false46</p>
<dt><code>bfd_params : check_tnl_key</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to true to make BFD accept only control messages with a tunnel key of zero46 By default, BFD accepts control messages with any tunnel key46</dl>
<p> <i>BFD Status:</i> The VTEP sets key-value pairs in the <code>bfd_status</code> column to report the status of BFD on this tunnel46 When BFD is not enabled, with <code>bfd_params:enable</code>, the HSC clears all key-value pairs from <code>bfd_status</code>46</p>
<dl>
<dt><code>bfd_status : enabled</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to true if the BFD session has been successfully enabled46 Set to false if the VTEP cannot support BFD or has insufficient resources to enable BFD on this tunnel46 The NVC will disable the BFD monitoring on the other side of the tunnel once this value is set to false46</p>
<dt><code>bfd_status : state</code>: optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code></p>
<dd>Reports the state of the BFD session46 The BFD session is fully healthy and negotiated if <code>UP</code>46</p>
<dt><code>bfd_status : forwarding</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Reports whether the BFD session believes this <code>Tunnel</code> may be used to forward traffic46 Typically this means the local session is signaling <code>UP</code>, and the remote system isn&#8217;t signaling a problem such as concatenated path down46</p>
<dt><code>bfd_status : diagnostic</code>: optional string</p>
<dd>A diagnostic code specifying the local system&#8217;s reason for the last change in session state46 The error messages are defined in section 4461 of [RFC 5880]46</p>
<dt><code>bfd_status : remote_state</code>: optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code></p>
<dd>Reports the state of the remote endpoint&#8217;s BFD session46</p>
<dt><code>bfd_status : remote_diagnostic</code>: optional string</p>
<dd>A diagnostic code specifying the remote system&#8217;s reason for the last change in session state46 The error messages are defined in section 4461 of [RFC 5880]46</p>
<dt><code>bfd_status : info</code>: optional string</p>
<dd>A short message providing further information about the BFD status (possibly including reasons why BFD could not be enabled)46</dl>
<h2>Physical_Port TABLE</h2>
<p>A port within a <code>Physical_Switch</code>46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>vlan_bindings</code></p>
<dd>map of integer-<code>Logical_Switch</code> pairs, key in range 0 to 4,095 </p>
<dt> <code>acl_bindings</code></p>
<dd>map of integer-<code>ACL</code> pairs, key in range 0 to 4,095 </p>
<dt> <code>vlan_stats</code></p>
<dd>map of integer-<code>Logical_Binding_Stats</code> pairs, key in range 0 to 4,095 </p>
<dt> <i>Identification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>string </p>
<dt> <code>description</code></p>
<dd>string</dl>
</dl>
<dt> <i>Error Notification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>port_fault_status : invalid_vlan_map</code></p>
<dd>none </p>
<dt> <code>port_fault_status : invalid_ACL_binding</code></p>
<dd>none </p>
<dt> <code>port_fault_status : unspecified_fault</code></p>
<dd>none</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>vlan_bindings</code>: map of integer-<code>Logical_Switch</code> pairs, key in range 0 to 4,095</p>
<dd>Identifies how VLANs on the physical port are bound to logical switches46 If, for example, the map contains a (VLAN, logical switch) pair, a packet that arrives on the port in the VLAN is considered to belong to the paired logical switch46 A value of zero in the VLAN field means that untagged traffic on the physical port is mapped to the logical switch46</p>
<dt><code>acl_bindings</code>: map of integer-<code>ACL</code> pairs, key in range 0 to 4,095</p>
<dd>Attach Access Control Lists (ACLs) to the physical port46 The column consists of a map of VLAN tags to <code>ACL</code>s46 If the value of the VLAN tag in the map is 0, this means that the ACL is associated with the entire physical port46 Non-zero values mean that the ACL is to be applied only on packets carrying that VLAN tag value46 Switches will not necessarily support matching on the VLAN tag for all ACLs, and unsupported ACL bindings will cause errors to be reported46 The binding of an ACL to a specific VLAN and the binding of an ACL to the entire physical port should not be combined on a single physical port46 That is, a mix of zero and non-zero keys in the map is not recommended46</p>
<dt><code>vlan_stats</code>: map of integer-<code>Logical_Binding_Stats</code> pairs, key in range 0 to 4,095</p>
<dd>Statistics for VLANs bound to logical switches on the physical port46 An implementation that fully supports such statistics would populate this column with a mapping for every VLAN that is bound in <code>vlan_bindings</code>46 An implementation that does not support such statistics or only partially supports them would not populate this column or partially populate it, respectively46 A value of zero in the VLAN field refers to untagged traffic on the physical port46</dl>
<p> <i>Identification:</i></p>
<dl>
<dt><code>name</code>: string</p>
<dd>Symbolic name for the port46 The name ought to be unique within a given <code>Physical_Switch</code>, but the database is not capable of enforcing this46</p>
<dt><code>description</code>: string</p>
<dd>An extended description for the port46</dl>
<p> <i>Error Notification:</i> An entry in this column indicates to the NVC that the physical port has encountered a fault46 The switch must clear this column when the error has been cleared46</p>
<dl>
<dt><code>port_fault_status : invalid_vlan_map</code>: none</p>
<dd>Indicates that a VLAN-to-logical-switch mapping requested by the controller could not be instantiated by the switch because of a conflict with local configuration46</p>
<dt><code>port_fault_status : invalid_ACL_binding</code>: none</p>
<dd>Indicates that an error has occurred in associating an ACL with a port46</p>
<dt><code>port_fault_status : unspecified_fault</code>: none</p>
<dd>Indicates that an error has occurred on the port but that no more specific information is available46</dl>
<h2>Logical_Binding_Stats TABLE</h2>
<p>Reports statistics for the <code>Logical_Switch</code> with which a VLAN on a <code>Physical_Port</code> is associated46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Statistics:</i></p>
<dl>
<dd>
<dl>
<dt> <code>packets_from_local</code></p>
<dd>integer </p>
<dt> <code>bytes_from_local</code></p>
<dd>integer </p>
<dt> <code>packets_to_local</code></p>
<dd>integer </p>
<dt> <code>bytes_to_local</code></p>
<dd>integer</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Statistics:</i> These statistics count only packets to which the binding applies46</p>
<dl>
<dt><code>packets_from_local</code>: integer</p>
<dd>Number of packets sent by the <code>Physical_Switch</code>46</p>
<dt><code>bytes_from_local</code>: integer</p>
<dd>Number of bytes in packets sent by the <code>Physical_Switch</code>46</p>
<dt><code>packets_to_local</code>: integer</p>
<dd>Number of packets received by the <code>Physical_Switch</code>46</p>
<dt><code>bytes_to_local</code>: integer</p>
<dd>Number of bytes in packets received by the <code>Physical_Switch</code>46</dl>
<h2>Logical_Switch TABLE</h2>
<p>A logical Ethernet switch, whose implementation may span physical and virtual media, possibly crossing L3 domains via tunnels; a logical layer-2 domain; an Ethernet broadcast domain46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Per Logical-Switch Tunnel Key:</i></p>
<dl>
<dd>
<dl>
<dt> <code>tunnel_key</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Identification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>string (must be unique within table) </p>
<dt> <code>description</code></p>
<dd>string</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Per Logical-Switch Tunnel Key:</i> Tunnel protocols tend to have a field that allows the tunnel to be partitioned into sub-tunnels: VXLAN has a VNI, GRE and STT have a key, CAPWAP has a WSI, and so on46 We call these generically &#8220;tunnel keys46&#8221; Given that one needs to use a tunnel key at all, there are at least two reasonable ways to assign their values:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Per <code>Logical_Switch</code>+<code>Physical_Locator</code> pair46 That is, each logical switch may be assigned a different tunnel key on every <code>Physical_Locator</code>46 This model is especially flexible46</p>
<dd>In this model, <code>Physical_Locator</code> carries the tunnel key46 Therefore, one <code>Physical_Locator</code> record will exist for each logical switch carried at a given IP destination46</p>
<dt>&bull;</p>
<dd>Per <code>Logical_Switch</code>46 That is, every tunnel associated with a particular logical switch carries the same tunnel key, regardless of the <code>Physical_Locator</code> to which the tunnel is addressed46 This model may ease switch implementation because it imposes fewer requirements on the hardware datapath46</p>
<dd>In this model, <code>Logical_Switch</code> carries the tunnel key46 Therefore, one <code>Physical_Locator</code> record will exist for each IP destination46</dl>
</dl>
<dl>
<dt><code>tunnel_key</code>: optional integer</p>
<dd>This column is used only in the tunnel key per <code>Logical_Switch</code> model (see above), because only in that model is there a tunnel key associated with a logical switch46</p>
<dd>For <code>vxlan_over_ipv4</code> encapsulation, this column is the VXLAN VNI that identifies a logical switch46 It must be in the range 0 to 16,777,21546</dl>
<p> <i>Identification:</i></p>
<dl>
<dt><code>name</code>: string (must be unique within table)</p>
<dd>Symbolic name for the logical switch46</p>
<dt><code>description</code>: string</p>
<dd>An extended description for the logical switch, such as its switch login banner46</dl>
<h2>Ucast_Macs_Local TABLE</h2>
<p>Mapping of unicast MAC addresses to tunnels (physical locators)46 This table is written by the HSC, so it contains the MAC addresses that have been learned on physical ports by a VTEP46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>MAC</code></p>
<dd>string </p>
<dt> <code>logical_switch</code> <code>Logical_Switch</code> </p>
<dt> <code>locator</code> <code>Physical_Locator</code> </p>
<dt> <code>ipaddr</code></p>
<dd>string</dl>
<h3>Details:</h3>
<dl>
<dt><code>MAC</code>: string</p>
<dd>A MAC address that has been learned by the VTEP46</p>
<dt><code>logical_switch</code>: <code>Logical_Switch</code></p>
<dd>The Logical switch to which this mapping applies46</p>
<dt><code>locator</code>: <code>Physical_Locator</code></p>
<dd>The physical locator to be used to reach this MAC address46 In this table, the physical locator will be one of the tunnel IP addresses of the appropriate VTEP46</p>
<dt><code>ipaddr</code>: string</p>
<dd>The IP address to which this MAC corresponds46 Optional field for the purpose of ARP supression46</dl>
<h2>Ucast_Macs_Remote TABLE</h2>
<p>Mapping of unicast MAC addresses to tunnels (physical locators)46 This table is written by the NVC, so it contains the MAC addresses that the NVC has learned46 These include VM MAC addresses, in which case the physical locators will be hypervisor IP addresses46 The NVC will also report MACs that it has learned from other HSCs in the network, in which case the physical locators will be tunnel IP addresses of the corresponding VTEPs46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>MAC</code></p>
<dd>string </p>
<dt> <code>logical_switch</code> <code>Logical_Switch</code> </p>
<dt> <code>locator</code> <code>Physical_Locator</code> </p>
<dt> <code>ipaddr</code></p>
<dd>string</dl>
<h3>Details:</h3>
<dl>
<dt><code>MAC</code>: string</p>
<dd>A MAC address that has been learned by the NVC46</p>
<dt><code>logical_switch</code>: <code>Logical_Switch</code></p>
<dd>The Logical switch to which this mapping applies46</p>
<dt><code>locator</code>: <code>Physical_Locator</code></p>
<dd>The physical locator to be used to reach this MAC address46 In this table, the physical locator will be either a hypervisor IP address or a tunnel IP addresses of another VTEP46</p>
<dt><code>ipaddr</code>: string</p>
<dd>The IP address to which this MAC corresponds46 Optional field for the purpose of ARP supression46</dl>
<h2>Mcast_Macs_Local TABLE</h2>
<p>Mapping of multicast MAC addresses to tunnels (physical locators)46 This table is written by the HSC, so it contains the MAC addresses that have been learned on physical ports by a VTEP46 These may be learned by IGMP snooping, for example46 This table also specifies how to handle unknown unicast and broadcast packets46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>MAC</code></p>
<dd>string </p>
<dt> <code>logical_switch</code> <code>Logical_Switch</code> </p>
<dt> <code>locator_set</code> <code>Physical_Locator_Set</code> </p>
<dt> <code>ipaddr</code></p>
<dd>string</dl>
<h3>Details:</h3>
<dl>
<dt><code>MAC</code>: string</p>
<dd>A MAC address that has been learned by the VTEP46</p>
<dd>The keyword <code>unknown-dst</code> is used as a special &#8220;Ethernet address&#8221; that indicates the locations to which packets in a logical switch whose destination addresses do not otherwise appear in <code>Ucast_Macs_Local</code> (for unicast addresses) or <code>Mcast_Macs_Local</code> (for multicast addresses) should be sent46</p>
<dt><code>logical_switch</code>: <code>Logical_Switch</code></p>
<dd>The Logical switch to which this mapping applies46</p>
<dt><code>locator_set</code>: <code>Physical_Locator_Set</code></p>
<dd>The physical locator set to be used to reach this MAC address46 In this table, the physical locator set will be contain one or more tunnel IP addresses of the appropriate VTEP(s)46</p>
<dt><code>ipaddr</code>: string</p>
<dd>The IP address to which this MAC corresponds46 Optional field for the purpose of ARP supression46</dl>
<h2>Mcast_Macs_Remote TABLE</h2>
<p>Mapping of multicast MAC addresses to tunnels (physical locators)46 This table is written by the NVC, so it contains the MAC addresses that the NVC has learned46 This table also specifies how to handle unknown unicast and broadcast packets46 </p>
<p> Multicast packet replication may be handled by a service node, in which case the physical locators will be IP addresses of service nodes46 If the VTEP supports replication onto multiple tunnels, then this may be used to replicate directly onto VTEP-hypervisor tunnels46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>MAC</code></p>
<dd>string </p>
<dt> <code>logical_switch</code> <code>Logical_Switch</code> </p>
<dt> <code>locator_set</code> <code>Physical_Locator_Set</code> </p>
<dt> <code>ipaddr</code></p>
<dd>string</dl>
<h3>Details:</h3>
<dl>
<dt><code>MAC</code>: string</p>
<dd>A MAC address that has been learned by the NVC46</p>
<dd>The keyword <code>unknown-dst</code> is used as a special &#8220;Ethernet address&#8221; that indicates the locations to which packets in a logical switch whose destination addresses do not otherwise appear in <code>Ucast_Macs_Remote</code> (for unicast addresses) or <code>Mcast_Macs_Remote</code> (for multicast addresses) should be sent46</p>
<dt><code>logical_switch</code>: <code>Logical_Switch</code></p>
<dd>The Logical switch to which this mapping applies46</p>
<dt><code>locator_set</code>: <code>Physical_Locator_Set</code></p>
<dd>The physical locator set to be used to reach this MAC address46 In this table, the physical locator set will be either a service node IP address or a set of tunnel IP addresses of hypervisors (and potentially other VTEPs)46</p>
<dt><code>ipaddr</code>: string</p>
<dd>The IP address to which this MAC corresponds46 Optional field for the purpose of ARP supression46</dl>
<h2>Logical_Router TABLE</h2>
<p>A logical router, or VRF46 A logical router may be connected to one or more logical switches46 Subnet addresses and interface addresses may be configured on the interfaces46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>switch_binding</code></p>
<dd>map of string-<code>Logical_Switch</code> pairs </p>
<dt> <code>static_routes</code></p>
<dd>map of string-string pairs </p>
<dt> <code>acl_binding</code></p>
<dd>map of string-<code>ACL</code> pairs </p>
<dt> <i>Identification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>string (must be unique within table) </p>
<dt> <code>description</code></p>
<dd>string</dl>
</dl>
<dt> <i>Error Notification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>LR_fault_status : invalid_ACL_binding</code></p>
<dd>none </p>
<dt> <code>LR_fault_status : unspecified_fault</code></p>
<dd>none</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>switch_binding</code>: map of string-<code>Logical_Switch</code> pairs</p>
<dd>Maps from an IPv4 or IPv6 address prefix in CIDR notation to a logical switch46 Multiple prefixes may map to the same switch46 By writing a 32-bit (or 128-bit for v6) address with a /N prefix length, both the router&#8217;s interface address and the subnet prefix can be configured46 For example, 1924668461461/24 creates a /24 subnet for the logical switch attached to the interface and assigns the address 1924668461461 to the router interface46</p>
<dt><code>static_routes</code>: map of string-string pairs</p>
<dd>One or more static routes, mapping IP prefixes to next hop IP addresses46</p>
<dt><code>acl_binding</code>: map of string-<code>ACL</code> pairs</p>
<dd>Maps ACLs to logical router interfaces46 The router interfaces are indicated using IP address notation, and must be the same interfaces created in the <code>switch_binding</code> column46 For example, an ACL could be associated with the logical router interface with an address of 1924668461461 as defined in the example above46</dl>
<p> <i>Identification:</i></p>
<dl>
<dt><code>name</code>: string (must be unique within table)</p>
<dd>Symbolic name for the logical router46</p>
<dt><code>description</code>: string</p>
<dd>An extended description for the logical router46</dl>
<p> <i>Error Notification:</i> An entry in this column indicates to the NVC that the HSC has encountered a fault in configuring state related to the logical router46</p>
<dl>
<dt><code>LR_fault_status : invalid_ACL_binding</code>: none</p>
<dd>Indicates that an error has occurred in associating an ACL with a logical router port46</p>
<dt><code>LR_fault_status : unspecified_fault</code>: none</p>
<dd>Indicates that an error has occurred in configuring the logical router but that no more specific information is available46</dl>
<h2>Arp_Sources_Local TABLE</h2>
<p>MAC address to be used when a VTEP issues ARP requests on behalf of a logical router46 </p>
<p> A distributed logical router is implemented by a set of VTEPs (both hardware VTEPs and vswitches)46 In order for a given VTEP to populate the local ARP cache for a logical router, it issues ARP requests with a source MAC address that is unique to the VTEP46 A single per-VTEP MAC can be re-used across all logical networks46 This table contains the MACs that are used by the VTEPs of a given HSC46 The table provides the mapping from MAC to physical locator for each VTEP so that replies to the ARP requests can be sent back to the correct VTEP using the appropriate physical locator46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>src_mac</code></p>
<dd>string </p>
<dt> <code>locator</code> <code>Physical_Locator</code></dl>
<h3>Details:</h3>
<dl>
<dt><code>src_mac</code>: string</p>
<dd>
<dd>The source MAC to be used by a given VTEP46</p>
<dt><code>locator</code>: <code>Physical_Locator</code></p>
<dd>The <code>Physical_Locator</code> to use for replies to ARP requests from this MAC address46</dl>
<h2>Arp_Sources_Remote TABLE</h2>
<p>MAC address to be used when a remote VTEP issues ARP requests on behalf of a logical router46 </p>
<p> This table is the remote counterpart of <code>Arp_sources_local</code>46 The NVC writes this table to notify the HSC of the MACs that will be used by remote VTEPs when they issue ARP requests on behalf of a distributed logical router46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>src_mac</code></p>
<dd>string </p>
<dt> <code>locator</code> <code>Physical_Locator</code></dl>
<h3>Details:</h3>
<dl>
<dt><code>src_mac</code>: string</p>
<dd>
<dd>The source MAC to be used by a given VTEP46</p>
<dt><code>locator</code>: <code>Physical_Locator</code></p>
<dd>The <code>Physical_Locator</code> to use for replies to ARP requests from this MAC address46</dl>
<h2>Physical_Locator_Set TABLE</h2>
<p>A set of one or more <code>Physical_Locator</code>s46 </p>
<p> This table exists only because OVSDB does not have a way to express the type &#8220;map from string to one or more <code>Physical_Locator</code> records46&#8221;</p>
<h3>Summary:</h3>
<dl>
<dt> <code>locators</code></p>
<dd>immutable set of 1 or more <code>Physical_Locator</code>s</dl>
<h3>Details:</h3>
<dl>
<dt><code>locators</code>: immutable set of 1 or more <code>Physical_Locator</code>s</p>
<dd></dl>
<h2>Physical_Locator TABLE</h2>
<p>Identifies an endpoint to which logical switch traffic may be encapsulated and forwarded46 </p>
<p> For the <code>vxlan_over_ipv4</code> encapsulation, the only encapsulation defined so far, all endpoints associated with a given <code>Logical_Switch</code> must use a common tunnel key, which is carried in the <code>tunnel_key</code> column of <code>Logical_Switch</code>46 </p>
<p> For some encapsulations yet to be defined, we expect <code>Physical_Locator</code> to identify both an endpoint and a tunnel key46 When the first such encapsulation is defined, we expect to add a &#8220;tunnel_key&#8221; column to <code>Physical_Locator</code> to allow the tunnel key to be defined46 </p>
<p> See the &#8220;Per Logical-Switch Tunnel Key&#8221; section in the <code>Logical_Switch</code> table for further discussion of the model46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>encapsulation_type</code></p>
<dd>immutable string, must be <code>vxlan_over_ipv4</code> </p>
<dt> <code>dst_ip</code></p>
<dd>immutable string</dl>
<h3>Details:</h3>
<dl>
<dt><code>encapsulation_type</code>: immutable string, must be <code>vxlan_over_ipv4</code></p>
<dd>The type of tunneling encapsulation46</p>
<dt><code>dst_ip</code>: immutable string</p>
<dd>For <code>vxlan_over_ipv4</code> encapsulation, the IPv4 address of the VXLAN tunnel endpoint46</p>
<dd>We expect that this column could be used for IPv4 or IPv6 addresses in encapsulations to be introduced later46</dl>
<h2>ACL_entry TABLE</h2>
<p>Describes the individual entries that comprise an Access Control List46 </p>
<p> Each entry in the table is a single rule to match on certain header fields46 While there are a large number of fields that can be matched on, most hardware cannot match on arbitrary combinations of fields46 It is common to match on either L2 fields (described below in the L2 group of columns) or L3/L4 fields (the L3/L4 group of columns) but not both46 The hardware switch controller may log an error if an ACL entry requires it to match on an incompatible mixture of fields46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>sequence</code></p>
<dd>integer </p>
<dt> <i>L2 fields:</i></p>
<dl>
<dd>
<dl>
<dt> <code>source_mac</code></p>
<dd>optional string </p>
<dt> <code>dest_mac</code></p>
<dd>optional string </p>
<dt> <code>ethertype</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>L3/L4 fields:</i></p>
<dl>
<dd>
<dl>
<dt> <code>source_ip</code></p>
<dd>optional string </p>
<dt> <code>source_mask</code></p>
<dd>optional string </p>
<dt> <code>dest_ip</code></p>
<dd>optional string </p>
<dt> <code>dest_mask</code></p>
<dd>optional string </p>
<dt> <code>protocol</code></p>
<dd>optional integer </p>
<dt> <code>source_port_min</code></p>
<dd>optional integer </p>
<dt> <code>source_port_max</code></p>
<dd>optional integer </p>
<dt> <code>dest_port_min</code></p>
<dd>optional integer </p>
<dt> <code>dest_port_max</code></p>
<dd>optional integer </p>
<dt> <code>tcp_flags</code></p>
<dd>optional integer </p>
<dt> <code>tcp_flags_mask</code></p>
<dd>optional integer </p>
<dt> <code>icmp_type</code></p>
<dd>optional integer </p>
<dt> <code>icmp_code</code></p>
<dd>optional integer</dl>
</dl>
<dt> <code>direction</code></p>
<dd>string, either <code>ingress</code> or <code>egress</code> </p>
<dt> <code>action</code></p>
<dd>string, either <code>deny</code> or <code>permit</code> </p>
<dt> <i>Error Notification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>acle_fault_status : invalid_acl_entry</code></p>
<dd>none </p>
<dt> <code>acle_fault_status : unspecified_fault</code></p>
<dd>none</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>sequence</code>: integer</p>
<dd>The sequence number for the ACL entry for the purpose of ordering entries in an ACL46 Lower numbered entries are matched before higher numbered entries46</dl>
<p> <i>L2 fields:</i></p>
<dl>
<dt><code>source_mac</code>: optional string</p>
<dd>Source MAC address, in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i></p>
<dt><code>dest_mac</code>: optional string</p>
<dd>Destination MAC address, in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i></p>
<dt><code>ethertype</code>: optional string</p>
<dd>Ethertype in hexadecimal, in the form <i>0xAAAA</i></dl>
<p> <i>L3/L4 fields:</i></p>
<dl>
<dt><code>source_ip</code>: optional string</p>
<dd>Source IP address, in the form <i>xx46xx46xx46xx</i> for IPv4 or appropriate colon-separated hexadecimal notation for IPv646</p>
<dt><code>source_mask</code>: optional string</p>
<dd>Mask that determines which bits of source_ip to match on, in the form <i>xx46xx46xx46xx</i> for IPv4 or appropriate colon-separated hexadecimal notation for IPv646</p>
<dt><code>dest_ip</code>: optional string</p>
<dd>Destination IP address, in the form <i>xx46xx46xx46xx</i> for IPv4 or appropriate colon-separated hexadecimal notation for IPv646</p>
<dt><code>dest_mask</code>: optional string</p>
<dd>Mask that determines which bits of dest_ip to match on, in the form <i>xx46xx46xx46xx</i> for IPv4 or appropriate colon-separated hexadecimal notation for IPv646</p>
<dt><code>protocol</code>: optional integer</p>
<dd>Protocol number in the IPv4 header, or value of the &quot;next header&quot; field in the IPv6 header46</p>
<dt><code>source_port_min</code>: optional integer</p>
<dd>Lower end of the range of source port values46 The value specified is included in the range46</p>
<dt><code>source_port_max</code>: optional integer</p>
<dd>Upper end of the range of source port values46 The value specified is included in the range46</p>
<dt><code>dest_port_min</code>: optional integer</p>
<dd>Lower end of the range of destination port values46 The value specified is included in the range46</p>
<dt><code>dest_port_max</code>: optional integer</p>
<dd>Upper end of the range of destination port values46 The value specified is included in the range46</p>
<dt><code>tcp_flags</code>: optional integer</p>
<dd>Integer representing the value of TCP flags to match46 For example, the SYN flag is the second least significant bit in the TCP flags46 Hence a value of 2 would indicate that the &quot;SYN&quot; flag should be set (assuming an appropriate mask)46</p>
<dt><code>tcp_flags_mask</code>: optional integer</p>
<dd>Integer representing the mask to apply when matching TCP flags46 For example, a value of 2 would imply that the &quot;SYN&quot; flag should be matched and all other flags ignored46</p>
<dt><code>icmp_type</code>: optional integer</p>
<dd>ICMP type to be matched46</p>
<dt><code>icmp_code</code>: optional integer</p>
<dd>ICMP code to be matched46</p>
<dt><code>direction</code>: string, either <code>ingress</code> or <code>egress</code></p>
<dd>Direction of traffic to match on the specified port, either &quot;ingress&quot; (toward the logical switch or router) or &quot;egress&quot; (leaving the logical switch or router)46</p>
<dt><code>action</code>: string, either <code>deny</code> or <code>permit</code></p>
<dd>Action to take for this rule, either &quot;permit&quot; or &quot;deny&quot;46</dl>
<p> <i>Error Notification:</i> An entry in this column indicates to the NVC that the ACL could not be configured as requested46 The switch must clear this column when the error has been cleared46</p>
<dl>
<dt><code>acle_fault_status : invalid_acl_entry</code>: none</p>
<dd>Indicates that an ACL entry requested by the controller could not be instantiated by the switch, e46g46 because it requires an unsupported combination of fields to be matched46</p>
<dt><code>acle_fault_status : unspecified_fault</code>: none</p>
<dd>Indicates that an error has occurred in configuring the ACL entry but no more specific information is available46</dl>
<h2>Acl Table</h2>
<p>Access Control List table46 Each ACL is constructed as a set of entries from the <code>ACL_entry</code> table46 Packets that are not matched by any entry in the ACL are allowed by default46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>acl_entries</code></p>
<dd>set of 1 or more <code>ACL_entry</code>s </p>
<dt> <code>acl_name</code></p>
<dd>string (must be unique within table) </p>
<dt> <i>Error Notification:</i></p>
<dl>
<dd>
<dl>
<dt> <code>acl_fault_status : invalid_acl</code></p>
<dd>none </p>
<dt> <code>acl_fault_status : resource_shortage</code></p>
<dd>none </p>
<dt> <code>acl_fault_status : unspecified_fault</code></p>
<dd>none</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>acl_entries</code>: set of 1 or more <code>ACL_entry</code>s</p>
<dd>A set of references to entries in the <code>ACL_entry</code> table46</p>
<dt><code>acl_name</code>: string (must be unique within table)</p>
<dd>A human readable name for the ACL, which may (for example) be displayed on the switch CLI46</dl>
<p> <i>Error Notification:</i> An entry in this column indicates to the NVC that the ACL could not be configured as requested46 The switch must clear this column when the error has been cleared46</p>
<dl>
<dt><code>acl_fault_status : invalid_acl</code>: none</p>
<dd>Indicates that an ACL requested by the controller could not be instantiated by the switch, e46g46, because it requires an unsupported combination of fields to be matched46</p>
<dt><code>acl_fault_status : resource_shortage</code>: none</p>
<dd>Indicates that an ACL requested by the controller could not be instantiated by the switch due to a shortage of resources (e46g46 TCAM space)46</p>
<dt><code>acl_fault_status : unspecified_fault</code>: none</p>
<dd>Indicates that an error has occurred in configuring the ACL but no more specific information is available46 </p>
</dl>
