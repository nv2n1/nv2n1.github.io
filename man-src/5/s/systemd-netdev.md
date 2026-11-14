---
title: "systemd-netdev(5)"
name: "systemd-netdev"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-netdev/"
description: "systemd.netdev – Virtual Network Device configuration"
---

<p>systemd.netdev &#8211; Virtual Network Device configuration</p>
<h2>Synopsis</h2>
<p><i>netdev</i>.netdev</p>
<h2>Description</h2>
<p>A plain ini-style text file that encodes configuration about a virtual network device, used by <code><a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a></code>(8). See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax. </p>
<p> The main Virtual Network Device file must have the extension .netdev; other extensions are ignored. Virtual network devices are created as soon as networkd is started. If a netdev with the specified name already exists, networkd will use that as-is rather than create its own. Note that the settings of the pre-existing netdev will not be changed by networkd. </p>
<p> The .netdev files are read from the files located in the system network directory /lib/systemd/network, the volatile runtime network directory /run/systemd/network and the local administration network directory /etc/systemd/network. All configuration files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority, files in /run/ take precedence over files with the same name in /lib/. This can be used to override a system-supplied configuration file with a local file if needed. As a special case, an empty file (file size 0) or symlink with the same name pointing to /dev/null disables the configuration file entirely (it is &quot;masked&quot;). </p>
<p> Along with the netdev file foo.netdev, a &quot;drop-in&quot; directory foo.netdev.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be merged in the alphanumeric order and parsed after the main file itself has been parsed. This is useful to alter or add configuration settings, without having to modify the main configuration file. Each drop-in file must have appropriate section headers. </p>
<p> In addition to /etc/systemd/network, drop-in &quot;.d&quot; directories can be placed in /lib/systemd/network or /run/systemd/network directories. Drop-in files in /etc/ take precedence over those in /run/ which in turn take precedence over those in /lib/. Drop-in files under any of these directories take precedence over the main netdev file wherever located. (Of course, since /run/ is temporary and /usr/lib/ is for vendors, it is unlikely drop-ins should be used in either of those places.)</p>
<h2>Supported Netdev Kinds</h2>
<p>The following kinds of virtual network devices may be configured in .netdev files: </p>
<p> <code>Table 1. Supported kinds of virtual network devices</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Kind </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>bond</i> </td>
<td> A bond device is an aggregation of all its slave devices. See m[blue]<code>Linux Ethernet Bonding Driver HOWTO</code>m[]<font SIZE="-2">[1]</font> for details.
</td>
</tr>
<tr VALIGN=top>
<td> <i>bridge</i> </td>
<td> A bridge device is a software switch, and each of its slave devices and the bridge itself are ports of the switch.
</td>
</tr>
<tr VALIGN=top>
<td> <i>dummy</i> </td>
<td> A dummy device drops all packets sent to it.
</td>
</tr>
<tr VALIGN=top>
<td> <i>gre</i> </td>
<td> A Level 3 GRE tunnel over IPv4. See m[blue]<code>RFC 2784</code>m[]<font SIZE="-2">[2]</font> for details.
</td>
</tr>
<tr VALIGN=top>
<td> <i>gretap</i> </td>
<td> A Level 2 GRE tunnel over IPv4.
</td>
</tr>
<tr VALIGN=top>
<td> <i>erspan</i> </td>
<td> ERSPAN mirrors traffic on one or more source ports and delivers the mirrored traffic to one or more destination ports on another switch. The traffic is encapsulated in generic routing encapsulation (GRE) and is therefore routable across a layer 3 network between the source switch and the destination switch.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ip6gre</i> </td>
<td> A Level 3 GRE tunnel over IPv6.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ip6tnl</i> </td>
<td> An IPv4 or IPv6 tunnel over IPv6
</td>
</tr>
<tr VALIGN=top>
<td> <i>ip6gretap</i> </td>
<td> A Level 2 GRE tunnel over IPv6.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ipip</i> </td>
<td> An IPv4 over IPv4 tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ipvlan</i> </td>
<td> An IPVLAN device is a stacked device which receives packets from its underlying device based on IP address filtering.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ipvtap</i> </td>
<td> An IPVTAP device is a stacked device which receives packets from its underlying device based on IP address filtering and can be accessed using the tap user space interface.
</td>
</tr>
<tr VALIGN=top>
<td> <i>macvlan</i> </td>
<td> A macvlan device is a stacked device which receives packets from its underlying device based on MAC address filtering.
</td>
</tr>
<tr VALIGN=top>
<td> <i>macvtap</i> </td>
<td> A macvtap device is a stacked device which receives packets from its underlying device based on MAC address filtering.
</td>
</tr>
<tr VALIGN=top>
<td> <i>sit</i> </td>
<td> An IPv6 over IPv4 tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>tap</i> </td>
<td> A persistent Level 2 tunnel between a network device and a device node.
</td>
</tr>
<tr VALIGN=top>
<td> <i>tun</i> </td>
<td> A persistent Level 3 tunnel between a network device and a device node.
</td>
</tr>
<tr VALIGN=top>
<td> <i>veth</i> </td>
<td> An Ethernet tunnel between a pair of network devices.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vlan</i> </td>
<td> A VLAN is a stacked device which receives packets from its underlying device based on VLAN tagging. See m[blue]<code>IEEE 802.1Q</code>m[]<font SIZE="-2">[3]</font> for details.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vti</i> </td>
<td> An IPv4 over IPSec tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vti6</i> </td>
<td> An IPv6 over IPSec tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vxlan</i> </td>
<td> A virtual extensible LAN (vxlan), for connecting Cloud computing deployments.
</td>
</tr>
<tr VALIGN=top>
<td> <i>geneve</i> </td>
<td> A GEneric NEtwork Virtualization Encapsulation (GENEVE) netdev driver.
</td>
</tr>
<tr VALIGN=top>
<td> <i>l2tp</i> </td>
<td> A Layer 2 Tunneling Protocol (L2TP) is a tunneling protocol used to support virtual private networks (VPNs) or as part of the delivery of services by ISPs. It does not provide any encryption or confidentiality by itself
</td>
</tr>
<tr VALIGN=top>
<td> <i>macsec</i> </td>
<td> Media Access Control Security (MACsec) is an 802.1AE IEEE industry-standard security technology that provides secure communication for all traffic on Ethernet links. MACsec provides point-to-point security on Ethernet links between directly connected nodes and is capable of identifying and preventing most security threats.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vrf</i> </td>
<td> A Virtual Routing and Forwarding (m[blue]<code>VRF</code>m[]<font SIZE="-2">[4]</font>) interface to create separate routing and forwarding domains.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vcan</i> </td>
<td> The virtual CAN driver (vcan). Similar to the network loopback devices, vcan offers a virtual local CAN interface.
</td>
</tr>
<tr VALIGN=top>
<td> <i>vxcan</i> </td>
<td> The virtual CAN tunnel driver (vxcan). Similar to the virtual ethernet driver veth, vxcan implements a local CAN traffic tunnel between two virtual CAN network devices. When creating a vxcan, two vxcan devices are created as pair. When one end receives the packet it appears on its pair and vice versa. The vxcan can be used for cross namespace communication.
</td>
</tr>
<tr VALIGN=top>
<td> <i>wireguard</i> </td>
<td> WireGuard Secure Network Tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>nlmon</i> </td>
<td> A Netlink monitor device. Use an nlmon device when you want to monitor system Netlink messages.
</td>
</tr>
<tr VALIGN=top>
<td> <i>fou</i> </td>
<td> Foo-over-UDP tunneling.
</td>
</tr>
<tr VALIGN=top>
<td> <i>xfrm</i> </td>
<td> A virtual tunnel interface like vti/vti6 but with several advantages.
</td>
</tr>
<tr VALIGN=top>
<td> <i>ifb</i> </td>
<td> The Intermediate Functional Block (ifb) pseudo network interface acts as a QoS concentrator for multiple different sources of traffic.
</td>
</tr>
<tr VALIGN=top>
<td> <i>bareudp</i> </td>
<td> Bare UDP tunnels provide a generic L3 encapsulation support for tunnelling different L3 protocols like MPLS, IP etc. inside of an UDP tunnel.
</td>
</tr>
<tr VALIGN=top>
<td> <i>batadv</i> </td>
<td> m[blue]<code>B.A.T.M.A.N. Advanced</code>m[]<font SIZE="-2">[5]</font> is a routing protocol for multi-hop mobile ad-hoc networks which operates on layer 2.
</td>
</tr>
</table>
<h2>[Match] Section Options</h2>
<p>A virtual network device is only created if the [Match] section matches the current environment, or if the section is empty. The following keys are accepted: </p>
<p> <i>Host=</i></p>
<dl>
<dd>Matches against the hostname or machine ID of the host. See &quot;ConditionHost=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Virtualization=</i></p>
<dl>
<dd>Checks whether the system is executed in a virtualized environment and optionally test whether it is a specific implementation. See &quot;ConditionVirtualization=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>KernelCommandLine=</i></p>
<dl>
<dd>Checks whether a specific kernel command line option is set. See &quot;ConditionKernelCommandLine=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>KernelVersion=</i></p>
<dl>
<dd>Checks whether the kernel version (as reported by <code>uname -r</code>) matches a certain expression. See &quot;ConditionKernelVersion=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Architecture=</i></p>
<dl>
<dd>Checks whether the system is running on a specific architecture. See &quot;ConditionArchitecture=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Firmware=</i></p>
<dl>
<dd>Checks whether the system is running on a machine with the specified firmware. See &quot;ConditionFirmware=&quot; in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<h2>[Netdev] Section Options</h2>
<p>The [NetDev] section accepts the following keys: </p>
<p> <i>Description=</i></p>
<dl>
<dd>A free-form description of the netdev.</dl>
<p> <i>Name=</i></p>
<dl>
<dd>The interface name used when creating the netdev. This setting is compulsory.</dl>
<p> <i>Kind=</i></p>
<dl>
<dd>The netdev kind. This setting is compulsory. See the &quot;Supported netdev kinds&quot; section for the valid keys.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>The maximum transmission unit in bytes to set for the device. The usual suffixes K, M, G are supported and are understood to the base of 1024. For &quot;tun&quot; or &quot;tap&quot; devices, <i>MTUBytes=</i> setting is not currently supported in [NetDev] section. Please specify it in [Link] section of corresponding <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) files.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>The MAC address to use for the device. For &quot;tun&quot; or &quot;tap&quot; devices, setting <i>MACAddress=</i> in the [NetDev] section is not supported. Please specify it in [Link] section of the corresponding <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) file. If this option is not set, &quot;vlan&quot; devices inherit the MAC address of the physical interface. For other kind of netdevs, if this option is not set, then MAC address is generated based on the interface name and the <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5).</dl>
<h2>[Bridge] Section Options</h2>
<p>The [Bridge] section only applies for netdevs of kind &quot;bridge&quot;, and accepts the following keys: </p>
<p> <i>HelloTimeSec=</i></p>
<dl>
<dd>HelloTimeSec specifies the number of seconds between two hello packets sent out by the root bridge and the designated bridges. Hello packets are used to communicate information about the topology throughout the entire bridged local area network.</dl>
<p> <i>MaxAgeSec=</i></p>
<dl>
<dd>MaxAgeSec specifies the number of seconds of maximum message age. If the last seen (received) hello packet is more than this number of seconds old, the bridge in question will start the takeover procedure in attempt to become the Root Bridge itself.</dl>
<p> <i>ForwardDelaySec=</i></p>
<dl>
<dd>ForwardDelaySec specifies the number of seconds spent in each of the Listening and Learning states before the Forwarding state is entered.</dl>
<p> <i>AgeingTimeSec=</i></p>
<dl>
<dd>This specifies the number of seconds a MAC Address will be kept in the forwarding database after having a packet received from this MAC Address.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>The priority of the bridge. An integer between 0 and 65535. A lower value means higher priority. The bridge having the lowest priority will be elected as root bridge.</dl>
<p> <i>GroupForwardMask=</i></p>
<dl>
<dd>A 16-bit bitmask represented as an integer which allows forwarding of link local frames with 802.1D reserved addresses (01:80:C2:00:00:0X). A logical AND is performed between the specified bitmask and the exponentiation of 2^X, the lower nibble of the last octet of the MAC address. For example, a value of 8 would allow forwarding of frames addressed to 01:80:C2:00:00:03 (802.1X PAE).</dl>
<p> <i>DefaultPVID=</i></p>
<dl>
<dd>This specifies the default port VLAN ID of a newly attached bridge port. Set this to an integer in the range 1&#8230;4094 or &quot;none&quot; to disable the PVID.</dl>
<p> <i>MulticastQuerier=</i></p>
<dl>
<dd>Takes a boolean. This setting controls the IFLA_BR_MCAST_QUERIER option in the kernel. If enabled, the kernel will send general ICMP queries from a zero source address. This feature should allow faster convergence on startup, but it causes some multicast-aware switches to misbehave and disrupt forwarding of multicast packets. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MulticastSnooping=</i></p>
<dl>
<dd>Takes a boolean. This setting controls the IFLA_BR_MCAST_SNOOPING option in the kernel. If enabled, IGMP snooping monitors the Internet Group Management Protocol (IGMP) traffic between hosts and multicast routers. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>VLANFiltering=</i></p>
<dl>
<dd>Takes a boolean. This setting controls the IFLA_BR_VLAN_FILTERING option in the kernel. If enabled, the bridge will be started in VLAN-filtering mode. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>VLANProtocol=</i></p>
<dl>
<dd>Allows setting the protocol used for VLAN filtering. Takes <code>802.1q</code> or, <code>802.1ad</code>, and defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>STP=</i></p>
<dl>
<dd>Takes a boolean. This enables the bridge&#8217;s Spanning Tree Protocol (STP). When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MulticastIGMPVersion=</i></p>
<dl>
<dd>Allows changing bridge&#8217;s multicast Internet Group Management Protocol (IGMP) version. Takes an integer 2 or 3. When unset, the kernel&#8217;s default will be used.</dl>
<h2>[Vlan] Section Options</h2>
<p>The [VLAN] section only applies for netdevs of kind &quot;vlan&quot;, and accepts the following key: </p>
<p> <i>Id=</i></p>
<dl>
<dd>The VLAN ID to use. An integer in the range 0&#8230;4094. This setting is compulsory.</dl>
<p> <i>Protocol=</i></p>
<dl>
<dd>Allows setting the protocol used for the VLAN interface. Takes &quot;802.1q&quot; or, &quot;802.1ad&quot;, and defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>GVRP=</i></p>
<dl>
<dd>Takes a boolean. The Generic VLAN Registration Protocol (GVRP) is a protocol that allows automatic learning of VLANs on a network. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MVRP=</i></p>
<dl>
<dd>Takes a boolean. Multiple VLAN Registration Protocol (MVRP) formerly known as GARP VLAN Registration Protocol (GVRP) is a standards-based Layer 2 network protocol, for automatic configuration of VLAN information on switches. It was defined in the 802.1ak amendment to 802.1Q-2005. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>LooseBinding=</i></p>
<dl>
<dd>Takes a boolean. The VLAN loose binding mode, in which only the operational state is passed from the parent to the associated VLANs, but the VLAN device state is not changed. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>ReorderHeader=</i></p>
<dl>
<dd>Takes a boolean. When enabled, the VLAN reorder header is used and VLAN interfaces behave like physical interfaces. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>EgressQOSMaps=</i></p>
<dl>
<dd>Defines a mapping of Linux internal packet priority (<code>SO_PRIORITY</code>) to VLAN header PCP field for outgoing frames. Takes a whitespace-separated list of unsigned integer pairs in the format &quot;from&quot;-&quot;to&quot;, e.g., &quot;21-7 45-5&quot; ranges 1-4294967294. Note that &quot;from&quot; must be greater than or equal to &quot;to&quot;. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IngressQOSMaps=</i></p>
<dl>
<dd>Defines a mapping of Linux internal packet priority (<code>SO_PRIORITY</code>) to VLAN header PCP field for incoming frames. Takes a whitespace-separated list of unsigned integer pairs in the format &quot;from&quot;-&quot;to&quot;, e.g., &quot;21-7 45-5&quot; ranges 1-4294967294. Note that &quot;from&quot; must be greater than or equal to &quot;to&quot;. When unset, the kernel&#8217;s default will be used.</dl>
<h2>[Macvlan] Section Options</h2>
<p>The [MACVLAN] section only applies for netdevs of kind &quot;macvlan&quot;, and accepts the following key: </p>
<p> <i>Mode=</i></p>
<dl>
<dd>The MACVLAN mode to use. The supported options are &quot;private&quot;, &quot;vepa&quot;, &quot;bridge&quot;, &quot;passthru&quot;, and &quot;source&quot;.</dl>
<p> <i>SourceMACAddress=</i></p>
<dl>
<dd>A whitespace-separated list of remote hardware addresses allowed on the MACVLAN. This option only has an effect in source mode. Use full colon-, hyphen- or dot-delimited hexadecimal. This option may appear more than once, in which case the lists are merged. If the empty string is assigned to this option, the list of hardware addresses defined prior to this is reset. Defaults to unset.</dl>
<p> <i>BroadcastMulticastQueueLength=</i></p>
<dl>
<dd>Specifies the length of the receive queue for broadcast/multicast packets. An unsigned integer in the range 0&#8230;4294967294. Defaults to unset.</dl>
<h2>[Macvtap] Section Options</h2>
<p>The [MACVTAP] section applies for netdevs of kind &quot;macvtap&quot; and accepts the same keys as [MACVLAN].</p>
<h2>[Ipvlan] Section Options</h2>
<p>The [IPVLAN] section only applies for netdevs of kind &quot;ipvlan&quot;, and accepts the following key: </p>
<p> <i>Mode=</i></p>
<dl>
<dd>The IPVLAN mode to use. The supported options are &quot;L2&quot;,&quot;L3&quot; and &quot;L3S&quot;.</dl>
<p> <i>Flags=</i></p>
<dl>
<dd>The IPVLAN flags to use. The supported options are &quot;bridge&quot;,&quot;private&quot; and &quot;vepa&quot;.</dl>
<h2>[Ipvtap] Section Options</h2>
<p>The [IPVTAP] section only applies for netdevs of kind &quot;ipvtap&quot; and accepts the same keys as [IPVLAN].</p>
<h2>[Vxlan] Section Options</h2>
<p>The [VXLAN] section only applies for netdevs of kind &quot;vxlan&quot;, and accepts the following keys: </p>
<p> <i>VNI=</i></p>
<dl>
<dd>The VXLAN Network Identifier (or VXLAN Segment ID). Takes a number in the range 1&#8230;16777215.</dl>
<p> <i>Remote=</i></p>
<dl>
<dd>Configures destination IP address.</dl>
<p> <i>Local=</i></p>
<dl>
<dd>Configures local IP address.</dl>
<p> <i>Group=</i></p>
<dl>
<dd>Configures VXLAN multicast group IP address. All members of a VXLAN must use the same multicast group address.</dl>
<p> <i>TOS=</i></p>
<dl>
<dd>The Type Of Service byte value for a vxlan interface.</dl>
<p> <i>TTL=</i></p>
<dl>
<dd>A fixed Time To Live N on Virtual eXtensible Local Area Network packets. Takes &quot;inherit&quot; or a number in the range 0&#8230;255. 0 is a special value meaning inherit the inner protocol&#8217;s TTL value. &quot;inherit&quot; means that it will inherit the outer protocol&#8217;s TTL value.</dl>
<p> <i>MacLearning=</i></p>
<dl>
<dd>Takes a boolean. When true, enables dynamic MAC learning to discover remote MAC addresses.</dl>
<p> <i>FDBAgeingSec=</i></p>
<dl>
<dd>The lifetime of Forwarding Database entry learnt by the kernel, in seconds.</dl>
<p> <i>MaximumFDBEntries=</i></p>
<dl>
<dd>Configures maximum number of FDB entries.</dl>
<p> <i>ReduceARPProxy=</i></p>
<dl>
<dd>Takes a boolean. When true, bridge-connected VXLAN tunnel endpoint answers ARP requests from the local bridge on behalf of remote Distributed Overlay Virtual Ethernet m[blue]<code>(DVOE)</code>m[]<font SIZE="-2">[6]</font> clients. Defaults to false.</dl>
<p> <i>L2MissNotification=</i></p>
<dl>
<dd>Takes a boolean. When true, enables netlink LLADDR miss notifications.</dl>
<p> <i>L3MissNotification=</i></p>
<dl>
<dd>Takes a boolean. When true, enables netlink IP address miss notifications.</dl>
<p> <i>RouteShortCircuit=</i></p>
<dl>
<dd>Takes a boolean. When true, route short circuiting is turned on.</dl>
<p> <i>UDPChecksum=</i></p>
<dl>
<dd>Takes a boolean. When true, transmitting UDP checksums when doing VXLAN/IPv4 is turned on.</dl>
<p> <i>UDP6ZeroChecksumTx=</i></p>
<dl>
<dd>Takes a boolean. When true, sending zero checksums in VXLAN/IPv6 is turned on.</dl>
<p> <i>UDP6ZeroChecksumRx=</i></p>
<dl>
<dd>Takes a boolean. When true, receiving zero checksums in VXLAN/IPv6 is turned on.</dl>
<p> <i>RemoteChecksumTx=</i></p>
<dl>
<dd>Takes a boolean. When true, remote transmit checksum offload of VXLAN is turned on.</dl>
<p> <i>RemoteChecksumRx=</i></p>
<dl>
<dd>Takes a boolean. When true, remote receive checksum offload in VXLAN is turned on.</dl>
<p> <i>GroupPolicyExtension=</i></p>
<dl>
<dd>Takes a boolean. When true, it enables Group Policy VXLAN extension security label mechanism across network peers based on VXLAN. For details about the Group Policy VXLAN, see the m[blue]<code>VXLAN Group Policy</code>m[]<font SIZE="-2">[7]</font> document. Defaults to false.</dl>
<p> <i>GenericProtocolExtension=</i></p>
<dl>
<dd>Takes a boolean. When true, Generic Protocol Extension extends the existing VXLAN protocol to provide protocol typing, OAM, and versioning capabilities. For details about the VXLAN GPE Header, see the m[blue]<code>Generic Protocol Extension for VXLAN</code>m[]<font SIZE="-2">[8]</font> document. If destination port is not specified and Generic Protocol Extension is set then default port of 4790 is used. Defaults to false.</dl>
<p> <i>DestinationPort=</i></p>
<dl>
<dd>Configures the default destination UDP port. If the destination port is not specified then Linux kernel default will be used. Set to 4789 to get the IANA assigned value.</dl>
<p> <i>PortRange=</i></p>
<dl>
<dd>Configures the source port range for the VXLAN. The kernel assigns the source UDP port based on the flow to help the receiver to do load balancing. When this option is not set, the normal range of local UDP ports is used.</dl>
<p> <i>FlowLabel=</i></p>
<dl>
<dd>Specifies the flow label to use in outgoing packets. The valid range is 0-1048575.</dl>
<p> <i>IPDoNotFragment=</i></p>
<dl>
<dd>Allows setting the IPv4 Do not Fragment (DF) bit in outgoing packets, or to inherit its value from the IPv4 inner header. Takes a boolean value, or &quot;inherit&quot;. Set to &quot;inherit&quot; if the encapsulated protocol is IPv6. When unset, the kernel&#8217;s default will be used.</dl>
<h2>[Geneve] Section Options</h2>
<p>The [GENEVE] section only applies for netdevs of kind &quot;geneve&quot;, and accepts the following keys: </p>
<p> <i>Id=</i></p>
<dl>
<dd>Specifies the Virtual Network Identifier (VNI) to use, a number between 0 and 16777215. This field is mandatory.</dl>
<p> <i>Remote=</i></p>
<dl>
<dd>Specifies the unicast destination IP address to use in outgoing packets.</dl>
<p> <i>TOS=</i></p>
<dl>
<dd>Specifies the TOS value to use in outgoing packets. Takes a number between 1 and 255.</dl>
<p> <i>TTL=</i></p>
<dl>
<dd>Accepts the same values as in the [VXLAN] section, except that when unset or set to 0, the kernel&#8217;s default will be used, meaning that packet TTL will be set from /proc/sys/net/ipv4/ip_default_ttl.</dl>
<p> <i>UDPChecksum=</i></p>
<dl>
<dd>Takes a boolean. When true, specifies that UDP checksum is calculated for transmitted packets over IPv4.</dl>
<p> <i>UDP6ZeroChecksumTx=</i></p>
<dl>
<dd>Takes a boolean. When true, skip UDP checksum calculation for transmitted packets over IPv6.</dl>
<p> <i>UDP6ZeroChecksumRx=</i></p>
<dl>
<dd>Takes a boolean. When true, allows incoming UDP packets over IPv6 with zero checksum field.</dl>
<p> <i>DestinationPort=</i></p>
<dl>
<dd>Specifies destination port. Defaults to 6081. If not set or assigned the empty string, the default port of 6081 is used.</dl>
<p> <i>FlowLabel=</i></p>
<dl>
<dd>Specifies the flow label to use in outgoing packets.</dl>
<p> <i>IPDoNotFragment=</i></p>
<dl>
<dd>Accepts the same key as in [VXLAN] section.</dl>
<p> <i>Independent=</i></p>
<dl>
<dd>Takes a boolean. When true, the vxlan interface is created without any underlying network interface. Defaults to false, which means that a .network file that requests this tunnel using <i>Tunnel=</i> is required for the tunnel to be created.</dl>
<h2>[Bareudp] Section Options</h2>
<p>The [BareUDP] section only applies for netdevs of kind &quot;bareudp&quot;, and accepts the following keys: </p>
<p> <i>DestinationPort=</i></p>
<dl>
<dd>Specifies the destination UDP port (in range 1&#8230;65535). This is mandatory.</dl>
<p> <i>EtherType=</i></p>
<dl>
<dd>Specifies the L3 protocol. Takes one of &quot;ipv4&quot;, &quot;ipv6&quot;, &quot;mpls-uc&quot; or &quot;mpls-mc&quot;. This is mandatory.</dl>
<h2>[L2Tp] Section Options</h2>
<p>The [L2TP] section only applies for netdevs of kind &quot;l2tp&quot;, and accepts the following keys: </p>
<p> <i>TunnelId=</i></p>
<dl>
<dd>Specifies the tunnel identifier. Takes an number in the range 1&#8230;4294967295. The value used must match the &quot;PeerTunnelId=&quot; value being used at the peer. This setting is compulsory.</dl>
<p> <i>PeerTunnelId=</i></p>
<dl>
<dd>Specifies the peer tunnel id. Takes a number in the range 1&#8230;4294967295. The value used must match the &quot;TunnelId=&quot; value being used at the peer. This setting is compulsory.</dl>
<p> <i>Remote=</i></p>
<dl>
<dd>Specifies the IP address of the remote peer. This setting is compulsory.</dl>
<p> <i>Local=</i></p>
<dl>
<dd>Specifies the IP address of the local interface. Takes an IP address, or the special values &quot;auto&quot;, &quot;static&quot;, or &quot;dynamic&quot;. When an address is set, then the local interface must have the address. If &quot;auto&quot;, then one of the addresses on the local interface is used. Similarly, if &quot;static&quot; or &quot;dynamic&quot; is set, then one of the static or dynamic addresses on the local interface is used. Defaults to &quot;auto&quot;.</dl>
<p> <i>EncapsulationType=</i></p>
<dl>
<dd>Specifies the encapsulation type of the tunnel. Takes one of &quot;udp&quot; or &quot;ip&quot;.</dl>
<p> <i>UDPSourcePort=</i></p>
<dl>
<dd>Specifies the UDP source port to be used for the tunnel. When UDP encapsulation is selected it&#8217;s mandatory. Ignored when IP encapsulation is selected.</dl>
<p> <i>UDPDestinationPort=</i></p>
<dl>
<dd>Specifies destination port. When UDP encapsulation is selected it&#8217;s mandatory. Ignored when IP encapsulation is selected.</dl>
<p> <i>UDPChecksum=</i></p>
<dl>
<dd>Takes a boolean. When true, specifies that UDP checksum is calculated for transmitted packets over IPv4.</dl>
<p> <i>UDP6ZeroChecksumTx=</i></p>
<dl>
<dd>Takes a boolean. When true, skip UDP checksum calculation for transmitted packets over IPv6.</dl>
<p> <i>UDP6ZeroChecksumRx=</i></p>
<dl>
<dd>Takes a boolean. When true, allows incoming UDP packets over IPv6 with zero checksum field.</dl>
<h2>[L2Tpsession] Section Options</h2>
<p>The [L2TPSession] section only applies for netdevs of kind &quot;l2tp&quot;, and accepts the following keys: </p>
<p> <i>Name=</i></p>
<dl>
<dd>Specifies the name of the session. This setting is compulsory.</dl>
<p> <i>SessionId=</i></p>
<dl>
<dd>Specifies the session identifier. Takes an number in the range 1&#8230;4294967295. The value used must match the &quot;SessionId=&quot; value being used at the peer. This setting is compulsory.</dl>
<p> <i>PeerSessionId=</i></p>
<dl>
<dd>Specifies the peer session identifier. Takes an number in the range 1&#8230;4294967295. The value used must match the &quot;PeerSessionId=&quot; value being used at the peer. This setting is compulsory.</dl>
<p> <i>Layer2SpecificHeader=</i></p>
<dl>
<dd>Specifies layer2specific header type of the session. One of &quot;none&quot; or &quot;default&quot;. Defaults to &quot;default&quot;.</dl>
<h2>[Macsec] Section Options</h2>
<p>The [MACsec] section only applies for network devices of kind &quot;macsec&quot;, and accepts the following keys: </p>
<p> <i>Port=</i></p>
<dl>
<dd>Specifies the port to be used for the MACsec transmit channel. The port is used to make secure channel identifier (SCI). Takes a value between 1 and 65535. Defaults to unset.</dl>
<p> <i>Encrypt=</i></p>
<dl>
<dd>Takes a boolean. When true, enable encryption. Defaults to unset.</dl>
<h2>[Macsecreceivechannel] Section Options</h2>
<p>The [MACsecReceiveChannel] section only applies for network devices of kind &quot;macsec&quot;, and accepts the following keys: </p>
<p> <i>Port=</i></p>
<dl>
<dd>Specifies the port to be used for the MACsec receive channel. The port is used to make secure channel identifier (SCI). Takes a value between 1 and 65535. This option is compulsory, and is not set by default.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>Specifies the MAC address to be used for the MACsec receive channel. The MAC address used to make secure channel identifier (SCI). This setting is compulsory, and is not set by default.</dl>
<h2>[Macsectransmitassociation] Section Options</h2>
<p>The [MACsecTransmitAssociation] section only applies for network devices of kind &quot;macsec&quot;, and accepts the following keys: </p>
<p> <i>PacketNumber=</i></p>
<dl>
<dd>Specifies the packet number to be used for replay protection and the construction of the initialization vector (along with the secure channel identifier [SCI]). Takes a value between 1-4,294,967,295. Defaults to unset.</dl>
<p> <i>KeyId=</i></p>
<dl>
<dd>Specifies the identification for the key. Takes a number between 0-255. This option is compulsory, and is not set by default.</dl>
<p> <i>Key=</i></p>
<dl>
<dd>Specifies the encryption key used in the transmission channel. The same key must be configured on the peer&#8217;s matching receive channel. This setting is compulsory, and is not set by default. Takes a 128-bit key encoded in a hexadecimal string, for example &quot;dffafc8d7b9a43d5b9a3dfbbf6a30c16&quot;.</dl>
<p> <i>KeyFile=</i></p>
<dl>
<dd>Takes an absolute path to a file which contains a 128-bit key encoded in a hexadecimal string, which will be used in the transmission channel. When this option is specified, <i>Key=</i> is ignored. Note that the file must be readable by the user &quot;systemd-network&quot;, so it should be, e.g., owned by &quot;root:systemd-network&quot; with a &quot;0640&quot; file mode. If the path refers to an <code>AF_UNIX</code> stream socket in the file system a connection is made to it and the key read from it.</dl>
<p> <i>Activate=</i></p>
<dl>
<dd>Takes a boolean. If enabled, then the security association is activated. Defaults to unset.</dl>
<p> <i>UseForEncoding=</i></p>
<dl>
<dd>Takes a boolean. If enabled, then the security association is used for encoding. Only one [MACsecTransmitAssociation] section can enable this option. When enabled, <i>Activate=yes</i> is implied. Defaults to unset.</dl>
<h2>[Macsecreceiveassociation] Section Options</h2>
<p>The [MACsecReceiveAssociation] section only applies for network devices of kind &quot;macsec&quot;, and accepts the following keys: </p>
<p> <i>Port=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecReceiveChannel] section.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecReceiveChannel] section.</dl>
<p> <i>PacketNumber=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecTransmitAssociation] section.</dl>
<p> <i>KeyId=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecTransmitAssociation] section.</dl>
<p> <i>Key=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecTransmitAssociation] section.</dl>
<p> <i>KeyFile=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecTransmitAssociation] section.</dl>
<p> <i>Activate=</i></p>
<dl>
<dd>Accepts the same key as in [MACsecTransmitAssociation] section.</dl>
<h2>[Tunnel] Section Options</h2>
<p>The [Tunnel] section only applies for netdevs of kind &quot;ipip&quot;, &quot;sit&quot;, &quot;gre&quot;, &quot;gretap&quot;, &quot;ip6gre&quot;, &quot;ip6gretap&quot;, &quot;vti&quot;, &quot;vti6&quot;, &quot;ip6tnl&quot;, and &quot;erspan&quot; and accepts the following keys: </p>
<p> <i>Local=</i></p>
<dl>
<dd>A static local address for tunneled packets. It must be an address on another interface of this host, or the special value &quot;any&quot;.</dl>
<p> <i>Remote=</i></p>
<dl>
<dd>The remote endpoint of the tunnel. Takes an IP address or the special value &quot;any&quot;.</dl>
<p> <i>TOS=</i></p>
<dl>
<dd>The Type Of Service byte value for a tunnel interface. For details about the TOS, see the m[blue]<code>Type of Service in the Internet Protocol Suite</code>m[]<font SIZE="-2">[9]</font> document.</dl>
<p> <i>TTL=</i></p>
<dl>
<dd>A fixed Time To Live N on tunneled packets. N is a number in the range 1&#8230;255. 0 is a special value meaning that packets inherit the TTL value. The default value for IPv4 tunnels is 0 (inherit). The default value for IPv6 tunnels is 64.</dl>
<p> <i>DiscoverPathMTU=</i></p>
<dl>
<dd>Takes a boolean. When true, enables Path MTU Discovery on the tunnel.</dl>
<p> <i>IPv6FlowLabel=</i></p>
<dl>
<dd>Configures the 20-bit flow label (see m[blue]<code>RFC 6437</code>m[]<font SIZE="-2">[10]</font>) field in the IPv6 header (see m[blue]<code>RFC 2460</code>m[]<font SIZE="-2">[11]</font>), which is used by a node to label packets of a flow. It is only used for IPv6 tunnels. A flow label of zero is used to indicate packets that have not been labeled. It can be configured to a value in the range 0&#8230;0xFFFFF, or be set to &quot;inherit&quot;, in which case the original flowlabel is used.</dl>
<p> <i>CopyDSCP=</i></p>
<dl>
<dd>Takes a boolean. When true, the Differentiated Service Code Point (DSCP) field will be copied to the inner header from outer header during the decapsulation of an IPv6 tunnel packet. DSCP is a field in an IP packet that enables different levels of service to be assigned to network traffic. Defaults to &quot;no&quot;.</dl>
<p> <i>EncapsulationLimit=</i></p>
<dl>
<dd>The Tunnel Encapsulation Limit option specifies how many additional levels of encapsulation are permitted to be prepended to the packet. For example, a Tunnel Encapsulation Limit option containing a limit value of zero means that a packet carrying that option may not enter another tunnel before exiting the current tunnel. (see m[blue]<code>RFC 2473</code>m[]<font SIZE="-2">[12]</font>). The valid range is 0-255 and &quot;none&quot;. Defaults to 4.</dl>
<p> <i>Key=</i></p>
<dl>
<dd>The <i>Key=</i> parameter specifies the same key to use in both directions (<i>InputKey=</i> and <i>OutputKey=</i>). The <i>Key=</i> is either a number or an IPv4 address-like dotted quad. It is used as mark-configured SAD/SPD entry as part of the lookup key (both in data and control path) in IP XFRM (framework used to implement IPsec protocol). See m[blue]<code>ip-xfrm &#8212; transform configuration</code>m[]<font SIZE="-2">[13]</font> for details. It is only used for VTI/VTI6, GRE, GRETAP, and ERSPAN tunnels.</dl>
<p> <i>InputKey=</i></p>
<dl>
<dd>The <i>InputKey=</i> parameter specifies the key to use for input. The format is same as <i>Key=</i>. It is only used for VTI/VTI6, GRE, GRETAP, and ERSPAN tunnels.</dl>
<p> <i>OutputKey=</i></p>
<dl>
<dd>The <i>OutputKey=</i> parameter specifies the key to use for output. The format is same as <i>Key=</i>. It is only used for VTI/VTI6, GRE, GRETAP, and ERSPAN tunnels.</dl>
<p> <i>Mode=</i></p>
<dl>
<dd>An &quot;ip6tnl&quot; tunnel can be in one of three modes &quot;ip6ip6&quot; for IPv6 over IPv6, &quot;ipip6&quot; for IPv4 over IPv6 or &quot;any&quot; for either.</dl>
<p> <i>Independent=</i></p>
<dl>
<dd>Takes a boolean. When false (the default), the tunnel is always created over some network device, and a .network file that requests this tunnel using <i>Tunnel=</i> is required for the tunnel to be created. When true, the tunnel is created independently of any network as &quot;tunnel [at] NONE&quot;.</dl>
<p> <i>AssignToLoopback=</i></p>
<dl>
<dd>Takes a boolean. If set to &quot;yes&quot;, the loopback interface &quot;lo&quot; is used as the underlying device of the tunnel interface. Defaults to &quot;no&quot;.</dl>
<p> <i>AllowLocalRemote=</i></p>
<dl>
<dd>Takes a boolean. When true allows tunnel traffic on <i>ip6tnl</i> devices where the remote endpoint is a local host address. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>FooOverUDP=</i></p>
<dl>
<dd>Takes a boolean. Specifies whether <i>FooOverUDP=</i> tunnel is to be configured. Defaults to false. This takes effects only for IPIP, SIT, GRE, and GRETAP tunnels. For more detail information see m[blue]<code>Foo over UDP</code>m[]<font SIZE="-2">[14]</font></dl>
<p> <i>FOUDestinationPort=</i></p>
<dl>
<dd>This setting specifies the UDP destination port for encapsulation. This field is mandatory when <i>FooOverUDP=yes</i>, and is not set by default.</dl>
<p> <i>FOUSourcePort=</i></p>
<dl>
<dd>This setting specifies the UDP source port for encapsulation. Defaults to <code>0</code> &#8212; that is, the source port for packets is left to the network stack to decide.</dl>
<p> <i>Encapsulation=</i></p>
<dl>
<dd>Accepts the same key as in the [FooOverUDP] section.</dl>
<p> <i>IPv6RapidDeploymentPrefix=</i></p>
<dl>
<dd>Reconfigure the tunnel for m[blue]<code>IPv6 Rapid Deployment</code>m[]<font SIZE="-2">[15]</font>, also known as 6rd. The value is an ISP-specific IPv6 prefix with a non-zero length. Only applicable to SIT tunnels.</dl>
<p> <i>ISATAP=</i></p>
<dl>
<dd>Takes a boolean. If set, configures the tunnel as Intra-Site Automatic Tunnel Addressing Protocol (ISATAP) tunnel. Only applicable to SIT tunnels. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>SerializeTunneledPackets=</i></p>
<dl>
<dd>Takes a boolean. If set to yes, then packets are serialized. Only applies for GRE, GRETAP, and ERSPAN tunnels. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>ERSPANIndex=</i></p>
<dl>
<dd>Specifies the ERSPAN index field for the interface, an integer in the range 1&#8230;1048575 associated with the ERSPAN traffic&#8217;s source port and direction. This field is mandatory.</dl>
<h2>[Foooverudp] Section Options</h2>
<p>The [FooOverUDP] section only applies for netdevs of kind &quot;fou&quot; and accepts the following keys: </p>
<p> <i>Encapsulation=</i></p>
<dl>
<dd>Specifies the encapsulation mechanism used to store networking packets of various protocols inside the UDP packets. Supports the following values: &quot;FooOverUDP&quot; provides the simplest no-frills model of UDP encapsulation, it simply encapsulates packets directly in the UDP payload. &quot;GenericUDPEncapsulation&quot; is a generic and extensible encapsulation, it allows encapsulation of packets for any IP protocol and optional data as part of the encapsulation. For more detailed information see m[blue]<code>Generic UDP Encapsulation</code>m[]<font SIZE="-2">[16]</font>. Defaults to &quot;FooOverUDP&quot;.</dl>
<p> <i>Port=</i></p>
<dl>
<dd>Specifies the port number where the encapsulated packets will arrive. Those packets will be removed and manually fed back into the network stack with the encapsulation removed to be sent to the real destination. This option is mandatory.</dl>
<p> <i>PeerPort=</i></p>
<dl>
<dd>Specifies the peer port number. Defaults to unset. Note that when peer port is set &quot;Peer=&quot; address is mandatory.</dl>
<p> <i>Protocol=</i></p>
<dl>
<dd>The <i>Protocol=</i> specifies the protocol number of the packets arriving at the UDP port. When <i>Encapsulation=FooOverUDP</i>, this field is mandatory and is not set by default. Takes an IP protocol name such as &quot;gre&quot; or &quot;ipip&quot;, or an integer within the range 1&#8230;255. When <i>Encapsulation=GenericUDPEncapsulation</i>, this must not be specified.</dl>
<p> <i>Peer=</i></p>
<dl>
<dd>Configures peer IP address. Note that when peer address is set &quot;PeerPort=&quot; is mandatory.</dl>
<p> <i>Local=</i></p>
<dl>
<dd>Configures local IP address.</dl>
<h2>[Peer] Section Options</h2>
<p>The [Peer] section only applies for netdevs of kind &quot;veth&quot; and accepts the following keys: </p>
<p> <i>Name=</i></p>
<dl>
<dd>The interface name used when creating the netdev. This setting is compulsory.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>The peer MACAddress, if not set, it is generated in the same way as the MAC address of the main interface.</dl>
<h2>[Vxcan] Section Options</h2>
<p>The [VXCAN] section only applies for netdevs of kind &quot;vxcan&quot; and accepts the following key: </p>
<p> <i>Peer=</i></p>
<dl>
<dd>The peer interface name used when creating the netdev. This setting is compulsory.</dl>
<h2>[Tun] Section Options</h2>
<p>The [Tun] section only applies for netdevs of kind &quot;tun&quot;, and accepts the following keys: </p>
<p> <i>MultiQueue=</i></p>
<dl>
<dd>Takes a boolean. Configures whether to use multiple file descriptors (queues) to parallelize packets sending and receiving. Defaults to &quot;no&quot;.</dl>
<p> <i>PacketInfo=</i></p>
<dl>
<dd>Takes a boolean. Configures whether packets should be prepended with four extra bytes (two flag bytes and two protocol bytes). If disabled, it indicates that the packets will be pure IP packets. Defaults to &quot;no&quot;.</dl>
<p> <i>VNetHeader=</i></p>
<dl>
<dd>Takes a boolean. Configures IFF_VNET_HDR flag for a tun or tap device. It allows sending and receiving larger Generic Segmentation Offload (GSO) packets. This may increase throughput significantly. Defaults to &quot;no&quot;.</dl>
<p> <i>User=</i></p>
<dl>
<dd>User to grant access to the /dev/net/tun device.</dl>
<p> <i>Group=</i></p>
<dl>
<dd>Group to grant access to the /dev/net/tun device.</dl>
<h2>[Tap] Section Options</h2>
<p>The [Tap] section only applies for netdevs of kind &quot;tap&quot;, and accepts the same keys as the [Tun] section.</p>
<h2>[Wireguard] Section Options</h2>
<p>The [WireGuard] section accepts the following keys: </p>
<p> <i>PrivateKey=</i></p>
<dl>
<dd>The Base64 encoded private key for the interface. It can be generated using the <code>wg genkey</code> command (see <code><a href="/docs/linux/man/8-wg/">wg</a></code>(8)). This option or <i>PrivateKeyFile=</i> is mandatory to use WireGuard. Note that because this information is secret, you may want to set the permissions of the .netdev file to be owned by &quot;root:systemd-network&quot; with a &quot;0640&quot; file mode.</dl>
<p> <i>PrivateKeyFile=</i></p>
<dl>
<dd>Takes an absolute path to a file which contains the Base64 encoded private key for the interface. When this option is specified, then <i>PrivateKey=</i> is ignored. Note that the file must be readable by the user &quot;systemd-network&quot;, so it should be, e.g., owned by &quot;root:systemd-network&quot; with a &quot;0640&quot; file mode. If the path refers to an <code>AF_UNIX</code> stream socket in the file system a connection is made to it and the key read from it.</dl>
<p> <i>ListenPort=</i></p>
<dl>
<dd>Sets UDP port for listening. Takes either value between 1 and 65535 or &quot;auto&quot;. If &quot;auto&quot; is specified, the port is automatically generated based on interface name. Defaults to &quot;auto&quot;.</dl>
<p> <i>FirewallMark=</i></p>
<dl>
<dd>Sets a firewall mark on outgoing WireGuard packets from this interface. Takes a number between 1 and 4294967295.</dl>
<h2>[Wireguardpeer] Section Options</h2>
<p>The [WireGuardPeer] section accepts the following keys: </p>
<p> <i>PublicKey=</i></p>
<dl>
<dd>Sets a Base64 encoded public key calculated by <code>wg pubkey</code> (see <code><a href="/docs/linux/man/8-wg/">wg</a></code>(8)) from a private key, and usually transmitted out of band to the author of the configuration file. This option is mandatory for this section.</dl>
<p> <i>PresharedKey=</i></p>
<dl>
<dd>Optional preshared key for the interface. It can be generated by the <code>wg genpsk</code> command. This option adds an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance. Note that because this information is secret, you may want to set the permissions of the .netdev file to be owned by &quot;root:systemd-network&quot; with a &quot;0640&quot; file mode.</dl>
<p> <i>PresharedKeyFile=</i></p>
<dl>
<dd>Takes an absolute path to a file which contains the Base64 encoded preshared key for the peer. When this option is specified, then <i>PresharedKey=</i> is ignored. Note that the file must be readable by the user &quot;systemd-network&quot;, so it should be, e.g., owned by &quot;root:systemd-network&quot; with a &quot;0640&quot; file mode. If the path refers to an <code>AF_UNIX</code> stream socket in the file system a connection is made to it and the key read from it.</dl>
<p> <i>AllowedIPs=</i></p>
<dl>
<dd>Sets a comma-separated list of IP (v4 or v6) addresses with CIDR masks from which this peer is allowed to send incoming traffic and to which outgoing traffic for this peer is directed. </p>
<p> The catch-all 0.0.0.0/0 may be specified for matching all IPv4 addresses, and ::/0 may be specified for matching all IPv6 addresses. </p>
<p> Note that this only affects <i>routing inside the network interface itself</i>, i.e. the packets that pass through the tunnel itself. To cause packets to be sent via the tunnel in the first place, an appropriate route needs to be added as well &#8212; either in the &quot;[Routes]&quot; section on the &quot;.network&quot; matching the wireguard interface, or externally to systemd-networkd.</dl>
<p> <i>Endpoint=</i></p>
<dl>
<dd>Sets an endpoint IP address or hostname, followed by a colon, and then a port number. This endpoint will be updated automatically once to the most recent source IP address and port of correctly authenticated packets from the peer at configuration time.</dl>
<p> <i>PersistentKeepalive=</i></p>
<dl>
<dd>Sets a seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from a peer, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds. If set to 0 or &quot;off&quot;, this option is disabled. By default or when unspecified, this option is off. Most users will not need this.</dl>
<h2>[Bond] Section Options</h2>
<p>The [Bond] section accepts the following key: </p>
<p> <i>Mode=</i></p>
<dl>
<dd>Specifies one of the bonding policies. The default is &quot;balance-rr&quot; (round robin). Possible values are &quot;balance-rr&quot;, &quot;active-backup&quot;, &quot;balance-xor&quot;, &quot;broadcast&quot;, &quot;802.3ad&quot;, &quot;balance-tlb&quot;, and &quot;balance-alb&quot;.</dl>
<p> <i>TransmitHashPolicy=</i></p>
<dl>
<dd>Selects the transmit hash policy to use for slave selection in balance-xor, 802.3ad, and tlb modes. Possible values are &quot;layer2&quot;, &quot;layer3+4&quot;, &quot;layer2+3&quot;, &quot;encap2+3&quot;, and &quot;encap3+4&quot;.</dl>
<p> <i>LACPTransmitRate=</i></p>
<dl>
<dd>Specifies the rate with which link partner transmits Link Aggregation Control Protocol Data Unit packets in 802.3ad mode. Possible values are &quot;slow&quot;, which requests partner to transmit LACPDUs every 30 seconds, and &quot;fast&quot;, which requests partner to transmit LACPDUs every second. The default value is &quot;slow&quot;.</dl>
<p> <i>MIIMonitorSec=</i></p>
<dl>
<dd>Specifies the frequency that Media Independent Interface link monitoring will occur. A value of zero disables MII link monitoring. This value is rounded down to the nearest millisecond. The default value is 0.</dl>
<p> <i>UpDelaySec=</i></p>
<dl>
<dd>Specifies the delay before a link is enabled after a link up status has been detected. This value is rounded down to a multiple of MIIMonitorSec. The default value is 0.</dl>
<p> <i>DownDelaySec=</i></p>
<dl>
<dd>Specifies the delay before a link is disabled after a link down status has been detected. This value is rounded down to a multiple of MIIMonitorSec. The default value is 0.</dl>
<p> <i>LearnPacketIntervalSec=</i></p>
<dl>
<dd>Specifies the number of seconds between instances where the bonding driver sends learning packets to each slave peer switch. The valid range is 1-0x7fffffff; the default value is 1. This option has an effect only for the balance-tlb and balance-alb modes.</dl>
<p> <i>AdSelect=</i></p>
<dl>
<dd>Specifies the 802.3ad aggregation selection logic to use. Possible values are &quot;stable&quot;, &quot;bandwidth&quot; and &quot;count&quot;.</dl>
<p> <i>AdActorSystemPriority=</i></p>
<dl>
<dd>Specifies the 802.3ad actor system priority. Takes a number in the range 1&#8230;65535.</dl>
<p> <i>AdUserPortKey=</i></p>
<dl>
<dd>Specifies the 802.3ad user defined portion of the port key. Takes a number in the range 0&#8230;1023.</dl>
<p> <i>AdActorSystem=</i></p>
<dl>
<dd>Specifies the 802.3ad system MAC address. This cannot be a null or multicast address.</dl>
<p> <i>FailOverMACPolicy=</i></p>
<dl>
<dd>Specifies whether the active-backup mode should set all slaves to the same MAC address at the time of enslavement or, when enabled, to perform special handling of the bond&#8217;s MAC address in accordance with the selected policy. The default policy is none. Possible values are &quot;none&quot;, &quot;active&quot; and &quot;follow&quot;.</dl>
<p> <i>ARPValidate=</i></p>
<dl>
<dd>Specifies whether or not ARP probes and replies should be validated in any mode that supports ARP monitoring, or whether non-ARP traffic should be filtered (disregarded) for link monitoring purposes. Possible values are &quot;none&quot;, &quot;active&quot;, &quot;backup&quot; and &quot;all&quot;.</dl>
<p> <i>ARPIntervalSec=</i></p>
<dl>
<dd>Specifies the ARP link monitoring frequency. A value of 0 disables ARP monitoring. The default value is 0, and the default unit seconds.</dl>
<p> <i>ARPIPTargets=</i></p>
<dl>
<dd>Specifies the IP addresses to use as ARP monitoring peers when ARPIntervalSec is greater than 0. These are the targets of the ARP request sent to determine the health of the link to the targets. Specify these values in IPv4 dotted decimal format. At least one IP address must be given for ARP monitoring to function. The maximum number of targets that can be specified is 16. The default value is no IP addresses.</dl>
<p> <i>ARPAllTargets=</i></p>
<dl>
<dd>Specifies the quantity of ARPIPTargets that must be reachable in order for the ARP monitor to consider a slave as being up. This option affects only active-backup mode for slaves with ARPValidate enabled. Possible values are &quot;any&quot; and &quot;all&quot;.</dl>
<p> <i>PrimaryReselectPolicy=</i></p>
<dl>
<dd>Specifies the reselection policy for the primary slave. This affects how the primary slave is chosen to become the active slave when failure of the active slave or recovery of the primary slave occurs. This option is designed to prevent flip-flopping between the primary slave and other slaves. Possible values are &quot;always&quot;, &quot;better&quot; and &quot;failure&quot;.</dl>
<p> <i>ResendIGMP=</i></p>
<dl>
<dd>Specifies the number of IGMP membership reports to be issued after a failover event. One membership report is issued immediately after the failover, subsequent packets are sent in each 200ms interval. The valid range is 0-255. Defaults to 1. A value of 0 prevents the IGMP membership report from being issued in response to the failover event.</dl>
<p> <i>PacketsPerSlave=</i></p>
<dl>
<dd>Specify the number of packets to transmit through a slave before moving to the next one. When set to 0, then a slave is chosen at random. The valid range is 0-65535. Defaults to 1. This option only has effect when in balance-rr mode.</dl>
<p> <i>GratuitousARP=</i></p>
<dl>
<dd>Specify the number of peer notifications (gratuitous ARPs and unsolicited IPv6 Neighbor Advertisements) to be issued after a failover event. As soon as the link is up on the new slave, a peer notification is sent on the bonding device and each VLAN sub-device. This is repeated at each link monitor interval (ARPIntervalSec or MIIMonitorSec, whichever is active) if the number is greater than 1. The valid range is 0-255. The default value is 1. These options affect only the active-backup mode.</dl>
<p> <i>AllSlavesActive=</i></p>
<dl>
<dd>Takes a boolean. Specifies that duplicate frames (received on inactive ports) should be dropped when false, or delivered when true. Normally, bonding will drop duplicate frames (received on inactive ports), which is desirable for most users. But there are some times it is nice to allow duplicate frames to be delivered. The default value is false (drop duplicate frames received on inactive ports).</dl>
<p> <i>DynamicTransmitLoadBalancing=</i></p>
<dl>
<dd>Takes a boolean. Specifies if dynamic shuffling of flows is enabled. Applies only for balance-tlb mode. Defaults to unset.</dl>
<p> <i>MinLinks=</i></p>
<dl>
<dd>Specifies the minimum number of links that must be active before asserting carrier. The default value is 0.</dl>
<p> For more detail information see m[blue]<code>Linux Ethernet Bonding Driver HOWTO</code>m[]<font SIZE="-2">[1]</font></p>
<h2>[Xfrm] Section Options</h2>
<p>The [Xfrm] section accepts the following keys: </p>
<p> <i>InterfaceId=</i></p>
<dl>
<dd>Sets the ID/key of the xfrm interface which needs to be associated with a SA/policy. Can be decimal or hexadecimal, valid range is 1-0xffffffff. This is mandatory.</dl>
<p> <i>Independent=</i></p>
<dl>
<dd>Takes a boolean. If false (the default), the xfrm interface must have an underlying device which can be used for hardware offloading.</dl>
<p> For more detail information see m[blue]<code>Virtual XFRM Interfaces</code>m[]<font SIZE="-2">[17]</font>.</p>
<h2>[Vrf] Section Options</h2>
<p>The [VRF] section only applies for netdevs of kind &quot;vrf&quot; and accepts the following key: </p>
<p> <i>Table=</i></p>
<dl>
<dd>The numeric routing table identifier. This setting is compulsory.</dl>
<h2>[Batmanadvanced] Section Options</h2>
<p>The [BatmanAdvanced] section only applies for netdevs of kind &quot;batadv&quot; and accepts the following keys: </p>
<p> <i>GatewayMode=</i></p>
<dl>
<dd>Takes one of &quot;off&quot;, &quot;server&quot;, or &quot;client&quot;. A batman-adv node can either run in server mode (sharing its internet connection with the mesh) or in client mode (searching for the most suitable internet connection in the mesh) or having the gateway support turned off entirely (which is the default setting).</dl>
<p> <i>Aggregation=</i></p>
<dl>
<dd>Takes a boolean value. Enables or disables aggregation of originator messages. Defaults to true.</dl>
<p> <i>BridgeLoopAvoidance=</i></p>
<dl>
<dd>Takes a boolean value. Enables or disables avoidance of loops on bridges. Defaults to true.</dl>
<p> <i>DistributedArpTable=</i></p>
<dl>
<dd>Takes a boolean value. Enables or disables the distributed ARP table. Defaults to true.</dl>
<p> <i>Fragmentation=</i></p>
<dl>
<dd>Takes a boolean value. Enables or disables fragmentation. Defaults to true.</dl>
<p> <i>HopPenalty=</i></p>
<dl>
<dd>The hop penalty setting allows to modify <code><a href="/docs/linux/man/8-batctl/">batctl</a></code>(8) preference for multihop routes vs. short routes. This integer value is applied to the TQ (Transmit Quality) of each forwarded OGM (Originator Message), thereby propagating the cost of an extra hop (the packet has to be received and retransmitted which costs airtime). A higher hop penalty will make it more unlikely that other nodes will choose this node as intermediate hop towards any given destination. The default hop penalty of &#8217;15&#8217; is a reasonable value for most setups and probably does not need to be changed. However, mobile nodes could choose a value of 255 (maximum value) to avoid being chosen as a router by other nodes. The minimum value is 0.</dl>
<p> <i>OriginatorIntervalSec=</i></p>
<dl>
<dd>The value specifies the interval in seconds, unless another time unit is specified in which batman-adv floods the network with its protocol information. See <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for more information.</dl>
<p> <i>GatewayBandwidthDown=</i></p>
<dl>
<dd>If the node is a server, this parameter is used to inform other nodes in the network about this node&#8217;s internet connection download bandwidth in bits per second. Just enter any number suffixed with K, M, G or T (base 1000) and the batman-adv module will propagate the entered value in the mesh.</dl>
<p> <i>GatewayBandwidthUp=</i></p>
<dl>
<dd>If the node is a server, this parameter is used to inform other nodes in the network about this node&#8217;s internet connection upload bandwidth in bits per second. Just enter any number suffixed with K, M, G or T (base 1000) and the batman-adv module will propagate the entered value in the mesh.</dl>
<p> <i>RoutingAlgorithm=</i></p>
<dl>
<dd>This can be either &quot;batman-v&quot; or &quot;batman-iv&quot; and describes which routing_algo of <code><a href="/docs/linux/man/8-batctl/">batctl</a></code>(8) to use. The algorithm cannot be changed after interface creation. Defaults to &quot;batman-v&quot;.</dl>
<h2>Examples</h2>
<p><code>Example 1.&nbsp;/etc/systemd/network/25-bridge.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=bridge0
Kind=bridge</pre>
</dl>
<p> <code>Example 2.&nbsp;/etc/systemd/network/25-vlan1.netdev</code> </p>
<dl>
<dd>
<pre>[Match]
Virtualization=no
[NetDev]
Name=vlan1
Kind=vlan
[VLAN]
Id=1</pre>
</dl>
<p> <code>Example 3.&nbsp;/etc/systemd/network/25-ipip.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=ipip-tun
Kind=ipip
MTUBytes=1480
[Tunnel]
Local=192.168.223.238
Remote=192.169.224.239
TTL=64</pre>
</dl>
<p> <code>Example 4.&nbsp;/etc/systemd/network/1-fou-tunnel.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=fou-tun
Kind=fou
[FooOverUDP]
Port=5555
Protocol=4</pre>
</dl>
<p> <code>Example 5.&nbsp;/etc/systemd/network/25-fou-ipip.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=ipip-tun
Kind=ipip
[Tunnel]
Independent=yes
Local=10.65.208.212
Remote=10.65.208.211
FooOverUDP=yes
FOUDestinationPort=5555</pre>
</dl>
<p> <code>Example 6.&nbsp;/etc/systemd/network/25-tap.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=tap-test
Kind=tap
[Tap]
MultiQueue=yes
PacketInfo=yes</pre>
</dl>
<p> <code>Example 7.&nbsp;/etc/systemd/network/25-sit.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=sit-tun
Kind=sit
MTUBytes=1480
[Tunnel]
Local=10.65.223.238
Remote=10.65.223.239</pre>
</dl>
<p> <code>Example 8.&nbsp;/etc/systemd/network/25-6rd.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=6rd-tun
Kind=sit
MTUBytes=1480
[Tunnel]
Local=10.65.223.238
IPv6RapidDeploymentPrefix=2602::/24</pre>
</dl>
<p> <code>Example 9.&nbsp;/etc/systemd/network/25-gre.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=gre-tun
Kind=gre
MTUBytes=1480
[Tunnel]
Local=10.65.223.238
Remote=10.65.223.239</pre>
</dl>
<p> <code>Example 10.&nbsp;/etc/systemd/network/25-ip6gre.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=ip6gre-tun
Kind=ip6gre
[Tunnel]
Key=123</pre>
</dl>
<p> <code>Example 11.&nbsp;/etc/systemd/network/25-vti.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=vti-tun
Kind=vti
MTUBytes=1480
[Tunnel]
Local=10.65.223.238
Remote=10.65.223.239</pre>
</dl>
<p> <code>Example 12.&nbsp;/etc/systemd/network/25-veth.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=veth-test
Kind=veth
[Peer]
Name=veth-peer</pre>
</dl>
<p> <code>Example 13.&nbsp;/etc/systemd/network/25-bond.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=bond1
Kind=bond
[Bond]
Mode=802.3ad
TransmitHashPolicy=layer3+4
MIIMonitorSec=1s
LACPTransmitRate=fast</pre>
</dl>
<p> <code>Example 14.&nbsp;/etc/systemd/network/25-dummy.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=dummy-test
Kind=dummy
MACAddress=12:34:56:78:9a:bc</pre>
</dl>
<p> <code>Example 15.&nbsp;/etc/systemd/network/25-vrf.netdev</code> </p>
<p> Create a VRF interface with table 42. </p>
<dl>
<dd>
<pre>[NetDev]
Name=vrf-test
Kind=vrf
[VRF]
Table=42</pre>
</dl>
<p> <code>Example 16.&nbsp;/etc/systemd/network/25-macvtap.netdev</code> </p>
<p> Create a MacVTap device. </p>
<dl>
<dd>
<pre>[NetDev]
Name=macvtap-test
Kind=macvtap</pre>
</dl>
<p> <code>Example 17.&nbsp;/etc/systemd/network/25-wireguard.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=wg0
Kind=wireguard
[WireGuard]
PrivateKey=EEGlnEPYJV//kbvvIqxKkQwOiS+UENyPncC4bF46ong=
ListenPort=51820
[WireGuardPeer]
PublicKey=RDf+LSpeEre7YEIKaxg+wbpsNV7du+ktR99uBEtIiCA=
AllowedIPs=fd31:bf08:57cb::/48,192.168.26.0/24
Endpoint=wireguard.example.com:51820</pre>
</dl>
<p> <code>Example 18.&nbsp;/etc/systemd/network/27-xfrm.netdev</code> </p>
<dl>
<dd>
<pre>[NetDev]
Name=xfrm0
Kind=xfrm
[Xfrm]
Independent=yes</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a></code>(8), <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Linux Ethernet Bonding Driver HOWTO</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/networking/bonding.txt">https://www.kernel.org/doc/Documentation/networking/bonding.txt</a></dl>
<dt> 2.</p>
<dd>RFC 2784</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc2784">https://tools.ietf.org/html/rfc2784</a></dl>
<dt> 3.</p>
<dd>IEEE 802.1Q</p>
<dl>
<dd><a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1Q.html">http://www.ieee802.org/1/pages/802.1Q.html</a></dl>
<dt> 4.</p>
<dd>VRF</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/networking/vrf.txt">https://www.kernel.org/doc/Documentation/networking/vrf.txt</a></dl>
<dt> 5.</p>
<dd>B.A.T.M.A.N. Advanced</p>
<dl>
<dd><a rel="nofollow" href="https://www.open-mesh.org/projects/open-mesh/wiki">https://www.open-mesh.org/projects/open-mesh/wiki</a></dl>
<dt> 6.</p>
<dd>(DVOE)</p>
<dl>
<dd><a rel="nofollow" href="https://en.wikipedia.org/wiki/Distributed_Overlay_Virtual_Ethernet">https://en.wikipedia.org/wiki/Distributed_Overlay_Virtual_Ethernet</a></dl>
<dt> 7.</p>
<dd>VXLAN Group Policy</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/draft-smith-vxlan-group-policy">https://tools.ietf.org/html/draft-smith-vxlan-group-policy</a></dl>
<dt> 8.</p>
<dd>Generic Protocol Extension for VXLAN</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/draft-ietf-nvo3-vxlan-gpe-07">https://tools.ietf.org/html/draft-ietf-nvo3-vxlan-gpe-07</a></dl>
<dt> 9.</p>
<dd>Type of Service in the Internet Protocol Suite</p>
<dl>
<dd><a rel="nofollow" href="http://tools.ietf.org/html/rfc1349">http://tools.ietf.org/html/rfc1349</a></dl>
<dt>10.</p>
<dd>RFC 6437</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6437">https://tools.ietf.org/html/rfc6437</a></dl>
<dt>11.</p>
<dd>RFC 2460</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc2460">https://tools.ietf.org/html/rfc2460</a></dl>
<dt>12.</p>
<dd>RFC 2473</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc2473#section-4.1.1">https://tools.ietf.org/html/rfc2473#section-4.1.1</a></dl>
<dt>13.</p>
<dd>ip-xfrm &#8212; transform configuration</p>
<dl>
<dd><a rel="nofollow" href="http://man7.org/linux/man-pages/man8/ip-xfrm.8.html">http://man7.org/linux/man-pages/man8/ip-xfrm.8.html</a></dl>
<dt>14.</p>
<dd>Foo over UDP</p>
<dl>
<dd><a rel="nofollow" href="https://lwn.net/Articles/614348">https://lwn.net/Articles/614348</a></dl>
<dt>15.</p>
<dd>IPv6 Rapid Deployment</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc5569">https://tools.ietf.org/html/rfc5569</a></dl>
<dt>16.</p>
<dd>Generic UDP Encapsulation</p>
<dl>
<dd><a rel="nofollow" href="https://lwn.net/Articles/615044">https://lwn.net/Articles/615044</a></dl>
<dt>17.</p>
<dd>Virtual XFRM Interfaces</p>
<dl>
<dd><a rel="nofollow" href="https://lwn.net/Articles/757391">https://lwn.net/Articles/757391</a></dl>
