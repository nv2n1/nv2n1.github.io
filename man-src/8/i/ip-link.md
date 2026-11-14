---
title: "ip-link(8)"
name: "ip-link"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-link/"
description: "ip-link – network device configuration"
---

<p>ip-link &#8211; network device configuration</p>
<h2>Synopsis</h2>
<pre><code>ip link

{ COMMAND |

    help }
</code></pre>
<p> <code>ip link add</code> [ <code>link</code> <i>DEVICE</i> ] [ <code>name</code> ] <i>NAME</i><br />
 [ <code>txqueuelen</code> <i>PACKETS</i> ]<br />
 [ <code>address</code> <i>LLADDR</i> ] [ <code>broadcast</code> <i>LLADDR</i> ]<br />
 [ <code>mtu</code> <i>MTU</i> ] [ <code>index</code> <i>IDX</i> ]<br />
 [ <code>numtxqueues</code> <i>QUEUE_COUNT</i> ] [ <code>numrxqueues</code> <i>QUEUE_COUNT</i> ]<br />
 <code>[ </code>gso_max_size <i>BYTES</i> ] [ <code>gso_max_segs</code> <i>SEGMENTS</i> ]<br />
 <code>type</code><i> TYPE</i> [ <i>ARGS</i> ]<br />
 <code>ip link delete </code>{ <i>DEVICE</i> | <code>group </code><i>GROUP</i> } <code>type</code><i> TYPE</i> [ <i>ARGS</i> ]<br />
 <code>ip link set </code>{ <i>DEVICE</i> | <code>group </code><i>GROUP</i> }<br />
 [ { <code>up</code> | <code>down</code> } ]<br />
 [ <code>type</code> <i>ETYPE TYPE_ARGS</i> ]<br />
 [ <code>arp</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>dynamic</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>multicast</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>allmulticast</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>promisc</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>protodown</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>protodown_reason</code> <i>PREASON</i> { <i>on</i> | <i>off</i> } ]<br />
 [ <code>trailers</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>txqueuelen</code> <i>PACKETS</i> ]<br />
 [ <code>name</code> <i>NEWNAME</i> ]<br />
 [ <code>address</code> <i>LLADDR</i> ]<br />
 [ <code>broadcast</code> <i>LLADDR</i> ]<br />
 [ <code>mtu</code> <i>MTU</i> ]<br />
 [ <code>netns</code> { <i>PID</i> | <i>NETNSNAME</i> } ]<br />
 [ <code>link-netnsid</code> <i>ID</i> ]<br />
 [ <code>alias</code> <i>NAME</i> ]<br />
 [ <code>vf</code> <i>NUM</i> [ <code>mac</code> <i>LLADDR</i> ]<br />
 [ <i>VFVLAN-LIST</i> ]<br />
 [ <code>rate</code> <i>TXRATE</i> ]<br />
 [ <code>max_tx_rate</code> <i>TXRATE</i> ]<br />
 [ <code>min_tx_rate</code> <i>TXRATE</i> ]<br />
 [ <code>spoofchk</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>query_rss</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>state</code> { <code>auto</code> | <code>enable</code> | <code>disable</code> } ]<br />
 [ <code>trust</code> { <code>on</code> | <code>off</code> } ]<br />
 [ <code>node_guid</code> eui64 ]<br />
 [ <code>port_guid</code> eui64 ] ]<br />
 [ { <code>xdp</code> | <code>xdpgeneric</code> | <code>xdpdrv</code> | <code>xdpoffload</code> } { <code>off</code> |<br />
 <code>object</code> <i>FILE</i> [ <code>section</code> <i>NAME</i> ] [ <code>verbose</code> ] |<br />
 <code>pinned</code> <i>FILE</i> } ]<br />
 [ <code>master</code> <i>DEVICE</i> ]<br />
 [ <code>nomaster</code> ]<br />
 [ <code>vrf</code> <i>NAME</i> ]<br />
 [ <code>addrgenmode</code> { <code>eui64</code> | <code>none</code> | <code>stable_secret</code> | <code>random</code> } ]<br />
 [ <code>macaddr</code> [ <i>MACADDR</i> ]<br />
 [ { <code>flush</code> | <code>add</code> | <code>del</code> } <i>MACADDR</i> ]<br />
 [ <code>set</code> <i>MACADDR</i> ] ] </p>
<p> <code>ip link show</code> [ <i>DEVICE</i> | <code>group</code> <i>GROUP</i> ] [ <code>up</code> ] [ <code>master</code> <i>DEVICE</i> ] [ <code>type</code> <i>ETYPE</i> ] [ <code>vrf</code> <i>NAME</i> ]<br />
 <code>ip link xstats</code> <code>type</code><i> TYPE</i> [ <i>ARGS</i> ]<br />
 <code>ip link afstats</code> [ <code>dev</code> <i>DEVICE</i> ]<br />
 <code>ip link help</code> [ <i>TYPE</i> ] </p>
<pre><code>TYPE := [

bridge |

bond |

can |

dummy |

hsr |

ifb |

ipoib |

macvlan |

macvtap |

vcan |

vxcan |

veth |

vlan |

vxlan |

ip6tnl |

ipip |

sit |

gre |

gretap |

erspan |

ip6gre |

ip6gretap |

ip6erspan |

vti |

nlmon |

ipvlan |

ipvtap |

lowpan |

geneve |

bareudp |

vrf |

macsec |

netdevsim |

rmnet |

xfrm ]
ETYPE := [ TYPE |

bridge_slave | bond_slave ]
VFVLAN-LIST := [ VFVLAN-LIST ] VFVLAN
VFVLAN :=

[ vlan

VLANID [

qos

VLAN-QOS ] [

proto

VLAN-PROTO ] ]</code></pre>
<p> <code>ip link property add dev </code><i>DEVICE</i> [ <code>altname</code> <i>NAME</i> .. ]<br />
 <code>ip link property del dev </code><i>DEVICE</i> [ <code>altname</code> <i>NAME</i> .. ] </p>
<h2>Description</h2>
<h3>ip link add &#8211; add virtual link</h3>
<dl>
<dt><code>link</code><i> DEVICE </i></p>
<dd>specifies the physical device to act operate on. <i>NAME</i> specifies the name of the new virtual device. <i>TYPE</i> specifies the type of the new device. Link types: <code>bridge</code> &#8211; Ethernet Bridge device <code>bond</code> &#8211; Bonding device <code>dummy</code> &#8211; Dummy network interface <code>hsr</code> &#8211; High-availability Seamless Redundancy device <code>ifb</code> &#8211; Intermediate Functional Block device <code>ipoib</code> &#8211; IP over Infiniband device <code>macvlan</code> &#8211; Virtual interface base on link layer address (MAC) <code>macvtap</code> &#8211; Virtual interface based on link layer address (MAC) and TAP. <code>vcan</code> &#8211; Virtual Controller Area Network interface <code>vxcan</code> &#8211; Virtual Controller Area Network tunnel interface <code>veth</code> &#8211; Virtual ethernet interface <code>vlan</code> &#8211; 802.1q tagged virtual LAN interface <code>vxlan</code> &#8211; Virtual eXtended LAN <code>ip6tnl</code> &#8211; Virtual tunnel interface IPv4|IPv6 over IPv6 <code>ipip</code> &#8211; Virtual tunnel interface IPv4 over IPv4 <code>sit</code> &#8211; Virtual tunnel interface IPv6 over IPv4 <code>gre</code> &#8211; Virtual tunnel interface GRE over IPv4 <code>gretap</code> &#8211; Virtual L2 tunnel interface GRE over IPv4 <code>erspan</code> &#8211; Encapsulated Remote SPAN over GRE and IPv4 <code>ip6gre</code> &#8211; Virtual tunnel interface GRE over IPv6 <code>ip6gretap</code> &#8211; Virtual L2 tunnel interface GRE over IPv6 <code>ip6erspan</code> &#8211; Encapsulated Remote SPAN over GRE and IPv6 <code>vti</code> &#8211; Virtual tunnel interface <code>nlmon</code> &#8211; Netlink monitoring device <code>ipvlan</code> &#8211; Interface for L3 (IPv6/IPv4) based VLANs <code>ipvtap</code> &#8211; Interface for L3 (IPv6/IPv4) based VLANs and TAP <code>lowpan</code> &#8211; Interface for 6LoWPAN (IPv6) over IEEE 802.15.4 / Bluetooth <code>geneve</code> &#8211; GEneric NEtwork Virtualization Encapsulation <code>bareudp</code> &#8211; Bare UDP L3 encapsulation support <code>macsec</code> &#8211; Interface for IEEE 802.1AE MAC Security (MACsec) <code>vrf</code> &#8211; Interface for L3 VRF domains <code>netdevsim</code> &#8211; Interface for netdev API tests <code>rmnet</code> &#8211; Qualcomm rmnet device <code>xfrm</code> &#8211; Virtual xfrm interface</p>
<dt><code>numtxqueues</code><i> QUEUE_COUNT </i></p>
<dd>specifies the number of transmit queues for new device.</p>
<dt><code>numrxqueues</code><i> QUEUE_COUNT </i></p>
<dd>specifies the number of receive queues for new device.</p>
<dt><code>gso_max_size</code><i> BYTES </i></p>
<dd>specifies the recommended maximum size of a Generic Segment Offload packet the new device should accept.</p>
<dt><code>gso_max_segs</code><i> SEGMENTS </i></p>
<dd>specifies the recommended maximum number of a Generic Segment Offload segments the new device should accept.</p>
<dt><code>index</code><i> IDX </i></p>
<dd>specifies the desired index of the new virtual device. The link creation fails, if the index is busy.</p>
<dt>VLAN Type Support</p>
<dd>For a link of type <i>VLAN</i> the following additional arguments are supported: <code>ip link add</code> <code>link</code><i> DEVICE </i> <code>name</code><i> NAME </i> <code>type vlan</code> [ <code>protocol</code><i> VLAN_PROTO </i> ] <code>id</code><i> VLANID </i> [ <code>reorder_hdr</code> { <code>on</code> | <code>off</code> } ] [ <code>gvrp</code> { <code>on</code> | <code>off</code> } ] [ <code>mvrp</code> { <code>on</code> | <code>off</code> } ] [ <code>loose_binding</code> { <code>on</code> | <code>off</code> } ] [ <code>bridge_binding</code> { <code>on</code> | <code>off</code> } ] [ <code>ingress-qos-map</code><i> QOS-MAP </i> ] [ <code>egress-qos-map</code><i> QOS-MAP </i> ] <code>protocol</code><i> VLAN_PROTO </i> &#8211; either 802.1Q or 802.1ad. <code>id</code><i> VLANID </i> &#8211; specifies the VLAN Identifier to use. Note that numbers with a leading &quot; 0 &quot; or &quot; 0x &quot; are interpreted as octal or hexadecimal, respectively. <code>reorder_hdr</code> { <code>on</code> | <code>off</code> } &#8211; specifies whether ethernet headers are reordered or not (default is <code>on</code>). If <code>reorder_hdr</code> is <code>on</code> then VLAN header will be not inserted immediately but only before passing to the physical device (if this device does not support VLAN offloading), the similar on the RX direction &#8211; by default the packet will be untagged before being received by VLAN device. Reordering allows to accelerate tagging on egress and to hide VLAN header on ingress so the packet looks like regular Ethernet packet, at the same time it might be confusing for packet capture as the VLAN header does not exist within the packet. VLAN offloading can be checked by <code><a href="/docs/linux/man/8-ethtool/">ethtool</a></code>(8): <code>ethtool -k</code> &lt;phy_dev&gt; | grep<code> tx-vlan-offload</code> where &lt;phy_dev&gt; is the physical device to which VLAN device is bound. <code>gvrp</code> { <code>on</code> | <code>off</code> } &#8211; specifies whether this VLAN should be registered using GARP VLAN<br />
&nbsp;<wbr>&nbsp;Registration Protocol. <code>mvrp</code> { <code>on</code> | <code>off</code> } &#8211; specifies whether this VLAN should be registered using Multiple VLAN<br />
&nbsp;<wbr>&nbsp;Registration Protocol. <code>loose_binding</code> { <code>on</code> | <code>off</code> } &#8211; specifies whether the VLAN device state is bound to the physical device state. <code>bridge_binding</code> { <code>on</code> | <code>off</code> } &#8211; specifies whether the VLAN device link state tracks the state of bridge ports that are members of the VLAN. <code>ingress-qos-map</code><i> QOS-MAP </i> &#8211; defines a mapping of VLAN header prio field to the Linux internal packet priority on incoming frames. The format is FROM:TO with multiple mappings separated by spaces. <code>egress-qos-map</code><i> QOS-MAP </i> &#8211; defines a mapping of Linux internal packet priority to VLAN header prio field but for outgoing frames. The format is the same as for ingress-qos-map. Linux packet priority can be set by <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8): <code>iptables</code> -t mangle -A POSTROUTING [&#8230;] -j CLASSIFY &#8211;set-class 0:4 and this &quot;4&quot; priority can be used in the egress qos mapping to set VLAN prio &quot;5&quot;: <code>ip</code> link set veth0.10 type vlan egress 4:5</p>
<dt>VXLAN Type Support</p>
<dd>For a link of type <i>VXLAN</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code><i> vxlan </i><code>id</code><i> VNI</i> [ <code>dev</code><i> PHYS_DEV </i> ] [ { <code>group</code> | <code>remote</code> } <i>IPADDR</i> ] [ <code>local</code> { IPADDR<i> | any</i> } ] [ <code>ttl</code><i> TTL </i> ] [ <code>tos</code><i> TOS </i> ] [ <code>df</code><i> DF </i> ] [ <code>flowlabel</code><i> FLOWLABEL </i> ] [ <code>dstport</code><i> PORT </i> ] [ <code>srcport</code><i> MIN MAX </i> ] [ [<code>no</code>]<code>learning</code> ] [ [<code>no</code>]<code>proxy</code> ] [ [<code>no</code>]<code>rsc</code> ] [ [<code>no</code>]<code>l2miss</code> ] [ [<code>no</code>]<code>l3miss</code> ] [ [<code>no</code>]<code>udpcsum</code> ] [ [<code>no</code>]<code>udp6zerocsumtx</code> ] [ [<code>no</code>]<code>udp6zerocsumrx</code> ] [ <code>ageing</code><i> SECONDS </i> ] [ <code>maxaddress</code><i> NUMBER </i> ] [ [<code>no</code>]<code>external</code> ] [ <code>gbp</code> ] [ <code>gpe</code> ] <code>id</code><i> VNI </i> &#8211; specifies the VXLAN Network Identifier (or VXLAN Segment Identifier) to use. <code>dev</code><i> PHYS_DEV</i> &#8211; specifies the physical device to use for tunnel endpoint communication. <code>group</code><i> IPADDR</i> &#8211; specifies the multicast IP address to join. This parameter cannot be specified with the <code>remote</code> parameter. <code>remote</code><i> IPADDR</i> &#8211; specifies the unicast destination IP address to use in outgoing packets when the destination link layer address is not known in the VXLAN device forwarding database. This parameter cannot be specified with the <code>group</code> parameter. <code>local</code><i> IPADDR</i> &#8211; specifies the source IP address to use in outgoing packets. <code>ttl</code><i> TTL</i> &#8211; specifies the TTL value to use in outgoing packets. <code>tos</code><i> TOS</i> &#8211; specifies the TOS value to use in outgoing packets. <code>df</code><i> DF</i> &#8211; specifies the usage of the Don&#8217;t Fragment flag (DF) bit in outgoing packets with IPv4 headers. The value <code>inherit</code> causes the bit to be copied from the original IP header. The values <code>unset</code> and <code>set</code> cause the bit to be always unset or always set, respectively. By default, the bit is not set. <code>flowlabel</code><i> FLOWLABEL</i> &#8211; specifies the flow label to use in outgoing packets. <code>dstport</code><i> PORT</i> &#8211; specifies the UDP destination port to communicate to the remote<br />
&nbsp;<wbr>&nbsp;VXLAN tunnel endpoint. <code>srcport</code><i> MIN MAX</i> &#8211; specifies the range of port numbers to use as UDP source ports to communicate to the remote VXLAN tunnel endpoint. [<code>no</code>]<code>learning</code> &#8211; specifies if unknown source link layer addresses and IP addresses are entered into the VXLAN device forwarding database. [<code>no</code>]<code>rsc</code> &#8211; specifies if route short circuit is turned on. [<code>no</code>]<code>proxy</code> &#8211; specifies ARP proxy is turned on. [<code>no</code>]<code>l2miss</code> &#8211; specifies if netlink LLADDR miss notifications are generated. [<code>no</code>]<code>l3miss</code> &#8211; specifies if netlink IP ADDR miss notifications are generated. [<code>no</code>]<code>udpcsum</code> &#8211; specifies if UDP checksum is calculated for transmitted packets over IPv4. [<code>no</code>]<code>udp6zerocsumtx</code> &#8211; skip UDP checksum calculation for transmitted packets over IPv6. [<code>no</code>]<code>udp6zerocsumrx</code> &#8211; allow incoming UDP packets over IPv6 with zero checksum field. <code>ageing</code><i> SECONDS</i> &#8211; specifies the lifetime in seconds of FDB entries learnt by the kernel. <code>maxaddress</code><i> NUMBER</i> &#8211; specifies the maximum number of FDB entries. [<code>no</code>]<code>external</code> &#8211; specifies whether an external control plane (e.g. <code>ip route encap</code>) or the internal FDB should be used. <code>gbp</code> &#8211; enables the Group Policy extension (VXLAN-GBP). Allows to transport group policy context across VXLAN network peers. If enabled, includes the mark of a packet in the VXLAN header for outgoing packets and fills the packet mark based on the information found in the VXLAN header for incoming packets. Format of upper 16 bits of packet mark (flags); +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+<br />
 |-|-|-|-|-|-|-|-|-|D|-|-|A|-|-|-|<br />
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ <code>D :=</code> Don&#8217;t Learn bit. When set, this bit indicates that the egress VTEP MUST NOT learn the source address of the encapsulated frame. <code>A :=</code> Indicates that the group policy has already been applied to this packet. Policies MUST NOT be applied by devices when the A bit is set. Format of lower 16 bits of packet mark (policy ID): +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+<br />
 | Group Policy ID |<br />
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ Example:<br />
&nbsp;<wbr>&nbsp;iptables -A OUTPUT&nbsp;[&#8230;]&nbsp;-j MARK &#8211;set-mark 0x800FF <code>gpe</code> &#8211; enables the Generic Protocol extension (VXLAN-GPE). Currently, this is only supported together with the <code>external</code> keyword.</p>
<dt>VETH, VXCAN Type Support</p>
<dd>For a link of types <i>VETH/VXCAN</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code> { <code>veth</code> | <code>vxcan</code> } [ <code>peer</code> <code>name </code><i>NAME</i> ] <code>peer</code> <code>name </code><i>NAME</i> &#8211; specifies the virtual pair device name of the <i>VETH/VXCAN</i> tunnel.</p>
<dt>IPIP, SIT Type Support</p>
<dd>For a link of type <i>IPIP</i>or<i>SIT</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code> { <code>ipip</code> | <code>sit</code> } <code> remote </code><i>ADDR</i><code> local </code><i>ADDR</i> [ <code>encap</code> { <code>fou</code> | <code>gue</code> | <code>none</code> } ] [ <code>encap-sport</code> { <i>PORT</i> | <code>auto</code> } ] [ <code>encap-dport </code><i>PORT</i> ] [ [<code>no</code>]<code>encap-csum</code> ] [ <i> [no]encap-remcsum </i> ] [ <i> mode { ip6ip | ipip | mplsip | any } </i> ] [ <code>external</code> ] <code>remote</code><i> ADDR </i> &#8211; specifies the remote address of the tunnel. <code>local</code><i> ADDR </i> &#8211; specifies the fixed local address for tunneled packets. It must be an address on another interface on this host. <code>encap</code> { <code>fou</code> | <code>gue</code> | <code>none</code> } &#8211; specifies type of secondary UDP encapsulation. &quot;fou&quot; indicates Foo-Over-UDP, &quot;gue&quot; indicates Generic UDP Encapsulation. <code>encap-sport</code> { <i>PORT</i> | <code>auto</code> } &#8211; specifies the source port in UDP encapsulation. <i>PORT</i> indicates the port by number, &quot;auto&quot; indicates that the port number should be chosen automatically (the kernel picks a flow based on the flow hash of the encapsulated packet). [<code>no</code>]<code>encap-csum</code> &#8211; specifies if UDP checksums are enabled in the secondary encapsulation. [<code>no</code>]<code>encap-remcsum</code> &#8211; specifies if Remote Checksum Offload is enabled. This is only applicable for Generic UDP Encapsulation. <code>mode</code><i> { ip6ip | ipip | mplsip | any } </i> &#8211; specifies mode in which device should run. &quot;ip6ip&quot; indicates IPv6-Over-IPv4, &quot;ipip&quot; indicates &quot;IPv4-Over-IPv4&quot;, &quot;mplsip&quot; indicates MPLS-Over-IPv4, &quot;any&quot; indicates IPv6, IPv4 or MPLS Over IPv4. Supported for SIT where the default is &quot;ip6ip&quot; and IPIP where the default is &quot;ipip&quot;. IPv6-Over-IPv4 is not supported for IPIP. <code>external</code> &#8211; make this tunnel externally controlled (e.g. <code>ip route encap</code>).</p>
<dt>GRE Type Support</p>
<dd>For a link of type <i>GRE</i> or <i>GRETAP</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code> { <code>gre</code> | <code>gretap</code> } <code> remote </code><i>ADDR</i><code> local </code><i>ADDR</i> [ [<code>no</code>][<code>i</code>|<code>o</code>]<code>seq</code> ] [ [<code>i</code>|<code>o</code>]<code>key</code> <i>KEY</i> | <code>no</code>[<code>i</code>|<code>o</code>]<code>key</code> ] [ [<code>no</code>][<code>i</code>|<code>o</code>]<code>csum</code> ] [ <code>ttl</code><i> TTL </i> ] [ <code>tos</code><i> TOS </i> ] [ [<code>no</code>]<code>pmtudisc</code> ] [ [<code>no</code>]<code>ignore-df</code> ] [ <code>dev</code><i> PHYS_DEV </i> ] [ <code>encap</code> { <code>fou</code> | <code>gue</code> | <code>none</code> } ] [ <code>encap-sport</code> { <i>PORT</i> | <code>auto</code> } ] [ <code>encap-dport </code><i>PORT</i> ] [ [<code>no</code>]<code>encap-csum</code> ] [ [<code>no</code>]<code>encap-remcsum</code> ] [ <code>external</code> ] <code>remote</code><i> ADDR </i> &#8211; specifies the remote address of the tunnel. <code>local</code><i> ADDR </i> &#8211; specifies the fixed local address for tunneled packets. It must be an address on another interface on this host. [<code>no</code>][<code>i</code>|<code>o</code>]<code>seq</code> &#8211; serialize packets. The <code>oseq</code> flag enables sequencing of outgoing packets. The <code>iseq</code> flag requires that all input packets are serialized. [<code>i</code>|<code>o</code>]<code>key</code> <i>KEY</i> | <code>no</code>[<code>i</code>|<code>o</code>]<code>key</code> &#8211; use keyed GRE with key <i>KEY</i>. KEY is either a number or an IPv4 address-like dotted quad. The <code>key</code> parameter specifies the same key to use in both directions. The <code>ikey</code> and <code>okey</code> parameters specify different keys for input and output. [<code>no</code>][<code>i</code>|<code>o</code>]<code>csum</code> &#8211; generate/require checksums for tunneled packets. The <code>ocsum</code> flag calculates checksums for outgoing packets. The <code>icsum</code> flag requires that all input packets have the correct checksum. The <code>csum</code> flag is equivalent to the combination <code>icsum ocsum .</code> <code>ttl</code><i> TTL</i> &#8211; specifies the TTL value to use in outgoing packets. <code>tos</code><i> TOS</i> &#8211; specifies the TOS value to use in outgoing packets. [<code>no</code>]<code>pmtudisc</code> &#8211; enables/disables Path MTU Discovery on this tunnel. It is enabled by default. Note that a fixed ttl is incompatible with this option: tunneling with a fixed ttl always makes pmtu discovery. [<code>no</code>]<code>ignore-df</code> &#8211; enables/disables IPv4 DF suppression on this tunnel. Normally datagrams that exceed the MTU will be fragmented; the presence of the DF flag inhibits this, resulting instead in an ICMP Unreachable (Fragmentation Required) message. Enabling this attribute causes the DF flag to be ignored. <code>dev</code><i> PHYS_DEV</i> &#8211; specifies the physical device to use for tunnel endpoint communication. <code>encap</code> { <code>fou</code> | <code>gue</code> | <code>none</code> } &#8211; specifies type of secondary UDP encapsulation. &quot;fou&quot; indicates Foo-Over-UDP, &quot;gue&quot; indicates Generic UDP Encapsulation. <code>encap-sport</code> { <i>PORT</i> | <code>auto</code> } &#8211; specifies the source port in UDP encapsulation. <i>PORT</i> indicates the port by number, &quot;auto&quot; indicates that the port number should be chosen automatically (the kernel picks a flow based on the flow hash of the encapsulated packet). [<code>no</code>]<code>encap-csum</code> &#8211; specifies if UDP checksums are enabled in the secondary encapsulation. [<code>no</code>]<code>encap-remcsum</code> &#8211; specifies if Remote Checksum Offload is enabled. This is only applicable for Generic UDP Encapsulation. <code>external</code> &#8211; make this tunnel externally controlled (e.g. <code>ip route encap</code>).</p>
<dt>IP6GRE/IP6GRETAP Type Support</p>
<dd>For a link of type <i>IP6GRE/IP6GRETAP</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code> { <code>ip6gre</code> | <code>ip6gretap</code> } <code>remote</code><i> ADDR </i><code>local</code><i> ADDR</i> [ [<code>no</code>][<code>i</code>|<code>o</code>]<code>seq</code> ] [ [<code>i</code>|<code>o</code>]<code>key</code> <i>KEY</i> | <code>no</code>[<code>i</code>|<code>o</code>]<code>key</code> ] [ [<code>no</code>][<code>i</code>|<code>o</code>]<code>csum</code> ] [ <code>hoplimit</code><i> TTL </i> ] [ <code>encaplimit</code><i> ELIM </i> ] [ <code>tclass</code><i> TCLASS </i> ] [ <code>flowlabel</code><i> FLOWLABEL </i> ] [ <code>dscp inherit</code> ] [ <code>[no]allow-localremote</code> ] [ <code>dev</code><i> PHYS_DEV </i> ] [ external ] <code>remote</code><i> ADDR </i> &#8211; specifies the remote IPv6 address of the tunnel. <code>local</code><i> ADDR </i> &#8211; specifies the fixed local IPv6 address for tunneled packets. It must be an address on another interface on this host. [<code>no</code>][<code>i</code>|<code>o</code>]<code>seq</code> &#8211; serialize packets. The <code>oseq</code> flag enables sequencing of outgoing packets. The <code>iseq</code> flag requires that all input packets are serialized. [<code>i</code>|<code>o</code>]<code>key</code> <i>KEY</i> | <code>no</code>[<code>i</code>|<code>o</code>]<code>key</code> &#8211; use keyed GRE with key <i>KEY</i>. KEY is either a number or an IPv4 address-like dotted quad. The <code>key</code> parameter specifies the same key to use in both directions. The <code>ikey</code> and <code>okey</code> parameters specify different keys for input and output. [<code>no</code>][<code>i</code>|<code>o</code>]<code>csum</code> &#8211; generate/require checksums for tunneled packets. The <code>ocsum</code> flag calculates checksums for outgoing packets. The <code>icsum</code> flag requires that all input packets have the correct checksum. The <code>csum</code> flag is equivalent to the combination <code>icsum ocsum</code>. <code>hoplimit</code><i> TTL</i> &#8211; specifies Hop Limit value to use in outgoing packets. <code>encaplimit</code><i> ELIM</i> &#8211; specifies a fixed encapsulation limit. Default is 4. <code>flowlabel</code><i> FLOWLABEL</i> &#8211; specifies a fixed flowlabel. <code>[no]allow-localremote</code> &#8211; specifies whether to allow remote endpoint to have an address configured on local host. <code>tclass</code><i> TCLASS</i> &#8211; specifies the traffic class field on tunneled packets, which can be specified as either a two-digit hex value (e.g. c0) or a predefined string (e.g. internet). The value <code>inherit</code> causes the field to be copied from the original IP header. The values <code>inherit/</code><i>STRING</i> or <code>inherit/</code><i>00</i><code>..</code><i>ff</i> will set the field to <i>STRING</i> or <i>00</i>..<i>ff</i> when tunneling non-IP packets. The default value is 00. external &#8211; make this tunnel externally controlled (or not, which is the default). In the kernel, this is referred to as collect metadata mode. This flag is mutually exclusive with the <code>remote</code>, <code>local</code>, <code>seq</code>, <code>key,</code> <code>csum,</code> <code>hoplimit,</code> <code>encaplimit,</code> <code>flowlabel</code> and <code>tclass</code> options.</p>
<dt>IPoIB Type Support</p>
<dd>For a link of type <i>IPoIB</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i><code> name </code><i>NAME</i> <code>type ipoib </code>[<code> pkey </code><i>PKEY</i> ] [ <code>mode</code> <i>MODE </i>] <code>pkey</code><i> PKEY </i> &#8211; specifies the IB P-Key to use. <code>mode</code><i> MODE </i> &#8211; specifies the mode (datagram or connected) to use.</p>
<dt>ERSPAN Type Support</p>
<dd>For a link of type <i>ERSPAN/IP6ERSPAN</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code> { <code>erspan</code> | <code>ip6erspan</code> } <code>remote</code><i> ADDR </i><code>local</code><i> ADDR </i><code>seq</code> key <i>KEY</i> <code>erspan_ver</code> <i>version </i> [ <code>erspan</code> <i>IDX </i> ] [ <code>erspan_dir</code> { <i>ingress</i> | <i>egress</i> } ] [ <code>erspan_hwid</code> <i>hwid </i> ] [ <code>[no]allow-localremote</code> ] [ external ] <code>remote</code><i> ADDR </i> &#8211; specifies the remote address of the tunnel. <code>local</code><i> ADDR </i> &#8211; specifies the fixed local address for tunneled packets. It must be an address on another interface on this host. <code>erspan_ver</code> <i>version </i> &#8211; specifies the ERSPAN version number. <i>version</i> indicates the ERSPAN version to be created: 0 for version 0 type I, 1 for version 1 (type II) or 2 for version 2 (type III). <code>erspan</code> <i>IDX </i> &#8211; specifies the ERSPAN v1 index field. <i>IDX</i> indicates a 20 bit index/port number associated with the ERSPAN traffic&#8217;s source port and direction. <code>erspan_dir</code> { <i>ingress</i> | <i>egress</i> } &#8211; specifies the ERSPAN v2 mirrored traffic&#8217;s direction. <code>erspan_hwid</code> <i>hwid </i> &#8211; an unique identifier of an ERSPAN v2 engine within a system. <i>hwid</i> is a 6-bit value for users to configure. <code>[no]allow-localremote</code> &#8211; specifies whether to allow remote endpoint to have an address configured on local host. <code>external</code> &#8211; make this tunnel externally controlled (or not, which is the default). In the kernel, this is referred to as collect metadata mode. This flag is mutually exclusive with the <code>remote</code>, <code>local</code>, <code>erspan_ver</code>, <code>erspan</code>, <code>erspan_dir</code> and <code>erspan_hwid</code> options.</p>
<dt>GENEVE Type Support</p>
<dd>For a link of type <i>GENEVE</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code><i> geneve </i><code>id</code><i> VNI </i><code>remote</code><i> IPADDR</i> [ <code>ttl</code><i> TTL </i> ] [ <code>tos</code><i> TOS </i> ] [ <code>df</code><i> DF </i> ] [ <code>flowlabel</code><i> FLOWLABEL </i> ] [ <code>dstport</code><i> PORT</i> ] [ [<code>no</code>]<code>external</code> ] [ [<code>no</code>]<code>udpcsum</code> ] [ [<code>no</code>]<code>udp6zerocsumtx</code> ] [ [<code>no</code>]<code>udp6zerocsumrx</code> ] <code>id</code><i> VNI </i> &#8211; specifies the Virtual Network Identifier to use. <code>remote</code><i> IPADDR</i> &#8211; specifies the unicast destination IP address to use in outgoing packets. <code>ttl</code><i> TTL</i> &#8211; specifies the TTL value to use in outgoing packets. &quot;0&quot; or &quot;auto&quot; means use whatever default value, &quot;inherit&quot; means inherit the inner protocol&#8217;s ttl. Default option is &quot;0&quot;. <code>tos</code><i> TOS</i> &#8211; specifies the TOS value to use in outgoing packets. <code>df</code><i> DF</i> &#8211; specifies the usage of the Don&#8217;t Fragment flag (DF) bit in outgoing packets with IPv4 headers. The value <code>inherit</code> causes the bit to be copied from the original IP header. The values <code>unset</code> and <code>set</code> cause the bit to be always unset or always set, respectively. By default, the bit is not set. <code>flowlabel</code><i> FLOWLABEL</i> &#8211; specifies the flow label to use in outgoing packets. <code>dstport</code><i> PORT</i> &#8211; select a destination port other than the default of 6081. [<code>no</code>]<code>external</code> &#8211; make this tunnel externally controlled (or not, which is the default). This flag is mutually exclusive with the <code>id</code>, <code>remote</code>, <code>ttl</code>, <code>tos</code> and <code>flowlabel</code> options. [<code>no</code>]<code>udpcsum</code> &#8211; specifies if UDP checksum is calculated for transmitted packets over IPv4. [<code>no</code>]<code>udp6zerocsumtx</code> &#8211; skip UDP checksum calculation for transmitted packets over IPv6. [<code>no</code>]<code>udp6zerocsumrx</code> &#8211; allow incoming UDP packets over IPv6 with zero checksum field.</p>
<dt>Bareudp Type Support</p>
<dd>For a link of type <i>Bareudp</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i> <code>type</code><i> bareudp </i><code>dstport</code><i> PORT </i><code>ethertype</code><i> PROTO</i> [ <code>srcportmin</code><i> PORT </i> ] [ [<code>no</code>]<code>multiproto</code> ] <code>dstport</code><i> PORT</i> &#8211; specifies the destination port for the UDP tunnel. <code>ethertype</code><i> PROTO</i> &#8211; specifies the ethertype of the L3 protocol being tunnelled. <code>ethertype</code> can be given as plain Ethernet protocol number or using the protocol name (&quot;ipv4&quot;, &quot;ipv6&quot;, &quot;mpls_uc&quot;, etc.). <code>srcportmin</code><i> PORT</i> &#8211; selects the lowest value of the UDP tunnel source port range. [<code>no</code>]<code>multiproto</code> &#8211; activates support for protocols similar to the one specified by <code>ethertype</code>. When <code>ethertype</code> is &quot;mpls_uc&quot; (that is, unicast MPLS), this allows the tunnel to also handle multicast MPLS. When <code>ethertype</code> is &quot;ipv4&quot;, this allows the tunnel to also handle IPv6. This option is disabled by default.</p>
<dt>MACVLAN and MACVTAP Type Support</p>
<dd>For a link of type <i>MACVLAN</i> or <i>MACVTAP</i> the following additional arguments are supported: <code>ip link add link </code><i>DEVICE</i><code> name </code><i>NAME</i> <code>type</code> { <code>macvlan</code> | <code>macvtap</code> } <code>mode</code> { <code>private</code> | <code>vepa</code> | <code>bridge</code> | <code>passthru</code> [ <code>nopromisc</code> ] | <code>source</code> [ <code>nodst</code> ] } [ <code>bcqueuelen</code> { <code>LENGTH</code> } ] <code>type</code> { <code>macvlan</code> | <code>macvtap</code> } &#8211; specifies the link type to use. <code>macvlan</code> creates just a virtual interface, while <code>macvtap</code> in addition creates a character device <code>/dev/tapX</code> to be used just like a <code>tuntap</code> device. <code>mode private</code> &#8211; Do not allow communication between <code>macvlan</code> instances on the same physical interface, even if the external switch supports hairpin mode. <code>mode vepa</code> &#8211; Virtual Ethernet Port Aggregator mode. Data from one <code>macvlan</code> instance to the other on the same physical interface is transmitted over the physical interface. Either the attached switch needs to support hairpin mode, or there must be a TCP/IP router forwarding the packets in order to allow communication. This is the default mode. <code>mode bridge</code> &#8211; In bridge mode, all endpoints are directly connected to each other, communication is not redirected through the physical interface&#8217;s peer. <code>mode</code> <code>passthru</code> [ <code>nopromisc</code> ] &#8211; This mode gives more power to a single endpoint, usually in <code>macvtap</code> mode. It is not allowed for more than one endpoint on the same physical interface. All traffic will be forwarded to this endpoint, allowing virtio guests to change MAC address or set promiscuous mode in order to bridge the interface or create vlan interfaces on top of it. By default, this mode forces the underlying interface into promiscuous mode. Passing the <code>nopromisc</code> flag prevents this, so the promisc flag may be controlled using standard tools. <code>mode</code> <code>source</code> [ <code>nodst</code> ] &#8211; allows one to set a list of allowed mac address, which is used to match against source mac address from received frames on underlying interface. This allows creating mac based VLAN associations, instead of standard port or tag based. The feature is useful to deploy 802.1x mac based behavior, where drivers of underlying interfaces doesn&#8217;t allows that. By default, packets are also considered (duplicated) for destination-based MACVLAN. Passing the <code>nodst</code> flag stops matching packets from also going through the destination-based flow. <code>bcqueuelen</code> { <code>LENGTH</code> } &#8211; Set the length of the RX queue used to process broadcast and multicast packets. <code>LENGTH</code> must be a positive integer in the range [0-4294967295]. Setting a length of 0 will effectively drop all broadcast/multicast traffic. If not specified the macvlan driver default (1000) is used. Note that all macvlans that share the same underlying device are using the same queue. The parameter here is a <code>request</code>, the actual queue length used will be the maximum length that any macvlan interface has requested. When listing device parameters both the bcqueuelen parameter as well as the actual used bcqueuelen are listed to better help the user understand the setting.</p>
<dt>High-availability Seamless Redundancy (HSR) Support</p>
<dd>For a link of type <i>HSR</i> the following additional arguments are supported: <code>ip link add link </code><i>DEVICE</i><code> name </code><i>NAME</i><code> type hsr</code> <code>slave1</code><i> SLAVE1-IF </i><code>slave2</code><i> SLAVE2-IF </i> [<code> supervision</code> <i>ADDR-BYTE</i> ] [ <code>version</code> { <code>0</code> | <code>1</code> } [ <code>proto</code> { <code>0</code> | <code>1</code> } ] <code>type</code> hsr &#8211; specifies the link type to use, here HSR. <code>slave1</code><i> SLAVE1-IF </i> &#8211; Specifies the physical device used for the first of the two ring ports. <code>slave2</code><i> SLAVE2-IF </i> &#8211; Specifies the physical device used for the second of the two ring ports. <code>supervision</code><i> ADDR-BYTE</i> &#8211; The last byte of the multicast address used for HSR supervision frames. Default option is &quot;0&quot;, possible values 0-255. <code>version</code> { <code>0</code> | <code>1</code> } &#8211; Selects the protocol version of the interface. Default option is &quot;0&quot;, which corresponds to the 2010 version of the HSR standard. Option &quot;1&quot; activates the 2012 version. <code>proto</code> { <code>0</code> | <code>1</code> } &#8211; Selects the protocol at the interface. Default option is &quot;0&quot;, which corresponds to the HSR standard. Option &quot;1&quot; activates the Parallel Redundancy Protocol (PRP).</p>
<dt>BRIDGE Type Support</p>
<dd>For a link of type <i>BRIDGE</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i><code> type bridge </code> [ <code>ageing_time</code><i> AGEING_TIME </i> ] [ <code>group_fwd_mask</code><i> MASK </i> ] [ <code>group_address</code><i> ADDRESS </i> ] [ <code>forward_delay</code><i> FORWARD_DELAY </i> ] [ <code>hello_time</code><i> HELLO_TIME </i> ] [ <code>max_age</code><i> MAX_AGE </i> ] [ <code>stp_state</code><i> STP_STATE </i> ] [ <code>priority</code><i> PRIORITY </i> ] [ <code>vlan_filtering</code><i> VLAN_FILTERING </i> ] [ <code>vlan_protocol</code><i> VLAN_PROTOCOL </i> ] [ <code>vlan_default_pvid</code><i> VLAN_DEFAULT_PVID </i> ] [ <code>vlan_stats_enabled</code><i> VLAN_STATS_ENABLED </i> ] [ <code>vlan_stats_per_port</code><i> VLAN_STATS_PER_PORT </i> ] [ <code>mcast_snooping</code><i> MULTICAST_SNOOPING </i> ] [ <code>mcast_router</code><i> MULTICAST_ROUTER </i> ] [ <code>mcast_query_use_ifaddr</code><i> MCAST_QUERY_USE_IFADDR </i> ] [ <code>mcast_querier</code><i> MULTICAST_QUERIER </i> ] [ <code>mcast_hash_elasticity</code><i> HASH_ELASTICITY </i> ] [ <code>mcast_hash_max</code><i> HASH_MAX </i> ] [ <code>mcast_last_member_count</code><i> LAST_MEMBER_COUNT </i> ] [ <code>mcast_startup_query_count</code><i> STARTUP_QUERY_COUNT </i> ] [ <code>mcast_last_member_interval</code><i> LAST_MEMBER_INTERVAL </i> ] [ <code>mcast_membership_interval</code><i> MEMBERSHIP_INTERVAL </i> ] [ <code>mcast_querier_interval</code><i> QUERIER_INTERVAL </i> ] [ <code>mcast_query_interval</code><i> QUERY_INTERVAL </i> ] [ <code>mcast_query_response_interval</code><i> QUERY_RESPONSE_INTERVAL </i> ] [ <code>mcast_startup_query_interval</code><i> STARTUP_QUERY_INTERVAL </i> ] [ <code>mcast_stats_enabled</code><i> MCAST_STATS_ENABLED </i> ] [ <code>mcast_igmp_version</code><i> IGMP_VERSION </i> ] [ <code>mcast_mld_version</code><i> MLD_VERSION </i> ] [ <code>nf_call_iptables</code><i> NF_CALL_IPTABLES </i> ] [ <code>nf_call_ip6tables</code><i> NF_CALL_IP6TABLES </i> ] [ <code>nf_call_arptables</code><i> NF_CALL_ARPTABLES </i> ] <code>ageing_time</code><i> AGEING_TIME </i> &#8211; configure the bridge&#8217;s FDB entries ageing time, ie the number of seconds a MAC address will be kept in the FDB after a packet has been received from that address. after this time has passed, entries are cleaned up. <code>group_fwd_mask</code><i> MASK </i> &#8211; set the group forward mask. This is the bitmask that is applied to decide whether to forward incoming frames destined to link-local addresses, ie addresses of the form 01:80:C2:00:00:0X (defaults to 0, ie the bridge does not forward any link-local frames). <code>group_address</code><i> ADDRESS </i> &#8211; set the MAC address of the multicast group this bridge uses for STP. The address must be a link-local address in standard Ethernet MAC address format, ie an address of the form 01:80:C2:00:00:0X, with X<br />
&nbsp;in&nbsp;[0, 4..f]. <code>forward_delay</code><i> FORWARD_DELAY </i> &#8211; set the forwarding delay in seconds, ie the time spent in LISTENING state (before moving to LEARNING) and in LEARNING state (before moving to FORWARDING). Only relevant if STP is enabled. Valid values are between 2 and 30. <code>hello_time</code><i> HELLO_TIME </i> &#8211; set the time in seconds between hello packets sent by the bridge, when it is a root bridge or a designated bridges. Only relevant if STP is enabled. Valid values are between 1 and 10. <code>max_age</code><i> MAX_AGE </i> &#8211; set the hello packet timeout, ie the time in seconds until another bridge in the spanning tree is assumed to be dead, after reception of its last hello message. Only relevant if STP is enabled. Valid values are between 6 and 40. <code>stp_state</code><i> STP_STATE </i> &#8211; turn spanning tree protocol on (<i>STP_STATE</i> &gt; 0) or off (<i>STP_STATE</i> == 0). for this bridge. <code>priority</code><i> PRIORITY </i> &#8211; set this bridge&#8217;s spanning tree priority, used during STP root bridge election. <i>PRIORITY</i> is a 16bit unsigned integer. <code>vlan_filtering</code><i> VLAN_FILTERING </i> &#8211; turn VLAN filtering on (<i>VLAN_FILTERING</i> &gt; 0) or off (<i>VLAN_FILTERING</i> == 0). When disabled, the bridge will not consider the VLAN tag when handling packets. <code>vlan_protocol</code> { <code>802.1Q</code> | <code>802.1ad</code> } &#8211; set the protocol used for VLAN filtering. <code>vlan_default_pvid</code><i> VLAN_DEFAULT_PVID </i> &#8211; set the default PVID (native/untagged VLAN ID) for this bridge. <code>vlan_stats_enabled</code><i> VLAN_STATS_ENABLED </i> &#8211; enable (<i>VLAN_STATS_ENABLED</i> == 1) or disable (<i>VLAN_STATS_ENABLED</i> == 0) per-VLAN stats accounting. <code>vlan_stats_per_port</code><i> VLAN_STATS_PER_PORT </i> &#8211; enable (<i>VLAN_STATS_PER_PORT</i> == 1) or disable (<i>VLAN_STATS_PER_PORT</i> == 0) per-VLAN per-port stats accounting. Can be changed only when there are no port VLANs configured. <code>mcast_snooping</code><i> MULTICAST_SNOOPING </i> &#8211; turn multicast snooping on (<i>MULTICAST_SNOOPING</i> &gt; 0) or off (<i>MULTICAST_SNOOPING</i> == 0). <code>mcast_router</code><i> MULTICAST_ROUTER </i> &#8211; set bridge&#8217;s multicast router if IGMP snooping is enabled. <i>MULTICAST_ROUTER</i> is an integer value having the following meaning: <code>0</code> &#8211; disabled. <code>1</code> &#8211; automatic (queried). <code>2</code> &#8211; permanently enabled. <code>mcast_query_use_ifaddr</code><i> MCAST_QUERY_USE_IFADDR </i> &#8211; whether to use the bridge&#8217;s own IP address as source address for IGMP queries (<i>MCAST_QUERY_USE_IFADDR</i> &gt; 0) or the default of 0.0.0.0 (<i>MCAST_QUERY_USE_IFADDR</i> == 0). <code>mcast_querier</code><i> MULTICAST_QUERIER </i> &#8211; enable (<i>MULTICAST_QUERIER</i> &gt; 0) or disable (<i>MULTICAST_QUERIER</i> == 0) IGMP querier, ie sending of multicast queries by the bridge (default: disabled). <code>mcast_querier_interval</code><i> QUERIER_INTERVAL </i> &#8211; interval between queries sent by other routers. if no queries are seen after this delay has passed, the bridge will start to send its own queries (as if <code>mcast_querier</code> was enabled). <code>mcast_hash_elasticity</code><i> HASH_ELASTICITY </i> &#8211; set multicast database hash elasticity, ie the maximum chain length in the multicast hash table (defaults to 4). <code>mcast_hash_max</code><i> HASH_MAX </i> &#8211; set maximum size of multicast hash table (defaults to 512, value must be a power of 2). <code>mcast_last_member_count</code><i> LAST_MEMBER_COUNT </i> &#8211; set multicast last member count, ie the number of queries the bridge will send before stopping forwarding a multicast group after a &quot;leave&quot; message has been received (defaults to 2). <code>mcast_last_member_interval</code><i> LAST_MEMBER_INTERVAL </i> &#8211; interval between queries to find remaining members of a group, after a &quot;leave&quot; message is received. <code>mcast_startup_query_count</code><i> STARTUP_QUERY_COUNT </i> &#8211; set the number of IGMP queries to send during startup phase (defaults to 2). <code>mcast_startup_query_interval</code><i> STARTUP_QUERY_INTERVAL </i> &#8211; interval between queries in the startup phase. <code>mcast_query_interval</code><i> QUERY_INTERVAL </i> &#8211; interval between queries sent by the bridge after the end of the startup phase. <code>mcast_query_response_interval</code><i> QUERY_RESPONSE_INTERVAL </i> &#8211; set the Max Response Time/Maximum Response Delay for IGMP/MLD queries sent by the bridge. <code>mcast_membership_interval</code><i> MEMBERSHIP_INTERVAL </i> &#8211; delay after which the bridge will leave a group, if no membership reports for this group are received. <code>mcast_stats_enabled</code><i> MCAST_STATS_ENABLED </i> &#8211; enable (<i>MCAST_STATS_ENABLED</i> &gt; 0) or disable (<i>MCAST_STATS_ENABLED</i> == 0) multicast (IGMP/MLD) stats accounting. <code>mcast_igmp_version</code><i> IGMP_VERSION </i> &#8211; set the IGMP version. <code>mcast_mld_version</code><i> MLD_VERSION </i> &#8211; set the MLD version. <code>nf_call_iptables</code><i> NF_CALL_IPTABLES </i> &#8211; enable (<i>NF_CALL_IPTABLES</i> &gt; 0) or disable (<i>NF_CALL_IPTABLES</i> == 0) iptables hooks on the bridge. <code>nf_call_ip6tables</code><i> NF_CALL_IP6TABLES </i> &#8211; enable (<i>NF_CALL_IP6TABLES</i> &gt; 0) or disable (<i>NF_CALL_IP6TABLES</i> == 0) ip6tables hooks on the bridge. <code>nf_call_arptables</code><i> NF_CALL_ARPTABLES </i> &#8211; enable (<i>NF_CALL_ARPTABLES</i> &gt; 0) or disable (<i>NF_CALL_ARPTABLES</i> == 0) arptables hooks on the bridge.</p>
<dt>MACsec Type Support</p>
<dd>For a link of type <i>MACsec</i> the following additional arguments are supported: <code>ip link add link </code><i>DEVICE</i><code> name </code><i>NAME</i><code> type macsec</code> [ [ <code>address</code><i> &lt;lladdr&gt;</i> ] <code>port</code><i> PORT</i> | <code>sci</code><i> SCI</i> ] [ <code>cipher</code><i> CIPHER_SUITE</i> ] [ <code>icvlen</code> { <i>8..16</i> } ] [ <code>encrypt</code> { <code>on</code> | <code>off</code> } ] [ <code>send_sci</code> { <code>on</code> | <code>off</code> } ] [ <code>end_station</code> { <code>on</code> | <code>off</code> } ] [ <code>scb</code> { <code>on</code> | <code>off</code> } ] [ <code>protect</code> { <code>on</code> | <code>off</code> } ] [ <code>replay</code> { <code>on</code> | <code>off</code> } <code>window</code> { <i>0..2^32-1</i> } ] [ <code>validate</code> { <code>strict</code> | <code>check</code> | <code>disabled</code> } ] [ <code>encodingsa</code> { <i>0..3</i> } ] <code>address</code><i> &lt;lladdr&gt; </i> &#8211; sets the system identifier component of secure channel for this MACsec device. <code>port</code><i> PORT </i> &#8211; sets the port number component of secure channel for this MACsec device, in a range from 1 to 65535 inclusive. Numbers with a leading &quot; 0 &quot; or &quot; 0x &quot; are interpreted as octal and hexadecimal, respectively. <code>sci</code><i> SCI </i> &#8211; sets the secure channel identifier for this MACsec device. <i>SCI</i> is a 64bit wide number in hexadecimal format. <code>cipher</code><i> CIPHER_SUITE </i> &#8211; defines the cipher suite to use. <code>icvlen</code><i> LENGTH </i> &#8211; sets the length of the Integrity Check Value (ICV). <code>encrypt on </code>or<code> encrypt off</code> &#8211; switches between authenticated encryption, or authenticity mode only. <code>send_sci on </code>or<code> send_sci off</code> &#8211; specifies whether the SCI is included in every packet, or only when it is necessary. <code>end_station on </code>or<code> end_station off</code> &#8211; sets the End Station bit. <code>scb on </code>or<code> scb off</code> &#8211; sets the Single Copy Broadcast bit. <code>protect on </code>or<code> protect off</code> &#8211; enables MACsec protection on the device. <code>replay on </code>or<code> replay off</code> &#8211; enables replay protection on the device. <code>window</code><i> SIZE </i> &#8211; sets the size of the replay window. <code>validate strict </code>or<code> validate check </code>or<code> validate disabled</code> &#8211; sets the validation mode on the device. <code>encodingsa</code><i> AN </i> &#8211; sets the active secure association for transmission.</p>
<dt>VRF Type Support</p>
<dd>For a link of type <i>VRF</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i><code> type vrf table </code><i>TABLE</i> <code>table</code> table id associated with VRF device</p>
<dt>RMNET Type Support</p>
<dd>For a link of type <i>RMNET</i> the following additional arguments are supported: <code>ip link add link </code><i>DEVICE</i><code> name </code><i>NAME</i><code> type rmnet mux_id </code><i>MUXID</i> <code>mux_id</code><i> MUXID </i> &#8211; specifies the mux identifier for the rmnet device, possible values 1-254.</p>
<dt>XFRM Type Support</p>
<dd>For a link of type <i>XFRM</i> the following additional arguments are supported: <code>ip link add </code><i>DEVICE</i><code> type xfrm dev </code><i>PHYS_DEV</i><code> [ if_id </code><i>IF_ID</i><code> ]</code> <code>dev</code><i> PHYS_DEV </i> &#8211; specifies the underlying physical interface from which transform traffic is sent and received. <code>if_id</code><i> IF-ID </i> &#8211; specifies the hexadecimal lookup key used to send traffic to and from specific xfrm policies. Policies must be configured with the same key. If not set, the key defaults to 0 and will match any policies which similarly do not have a lookup key configuration.</dl>
<h3>ip link delete &#8211; delete virtual link</h3>
<dl>
<dt><code>dev</code><i> DEVICE </i></p>
<dd>specifies the virtual device to act operate on.</p>
<dt><code>group</code><i> GROUP </i></p>
<dd>specifies the group of virtual links to delete. Group 0 is not allowed to be deleted since it is the default group.</p>
<dt><code>type</code><i> TYPE </i></p>
<dd>specifies the type of the device.</dl>
<h3>ip link set &#8211; change device attributes</h3>
<p><code>Warning:</code> If multiple parameter changes are requested, <code>ip</code> aborts immediately after any of the changes have failed. This is the only case when <code>ip</code> can move the system to an unpredictable state. The solution is to avoid changing several parameters with one <code>ip link set</code> call. The modifier <code>change</code> is equivalent to <code>set</code>.</p>
<dl>
<dt><code>dev</code><i> DEVICE </i></p>
<dd><i>DEVICE</i> specifies network device to operate on. When configuring SR-IOV Virtual Function (VF) devices, this keyword should specify the associated Physical Function (PF) device.</p>
<dt><code>group</code><i> GROUP </i></p>
<dd><i>GROUP</i> has a dual role: If both group and dev are present, then move the device to the specified group. If only a group is specified, then the command operates on all devices in that group.</p>
<dt><code>up</code> and <code>down</code></p>
<dd>change the state of the device to <code>UP</code> or <code>DOWN</code>.</p>
<dt><code>arp on </code>or<code> arp off</code></p>
<dd>change the <code>NOARP</code> flag on the device.</p>
<dt><code>multicast on </code>or<code> multicast off</code></p>
<dd>change the <code>MULTICAST</code> flag on the device.</p>
<dt><code>allmulticast on </code>or<code> allmulticast off</code></p>
<dd>change the <code>ALLMULTI</code> flag on the device. When enabled, instructs network driver to retrieve all multicast packets from the network to the kernel for further processing.</p>
<dt><code>promisc on </code>or<code> promisc off</code></p>
<dd>change the <code>PROMISC</code> flag on the device. When enabled, activates promiscuous operation of the network device.</p>
<dt><code>trailers on </code>or<code> trailers off</code></p>
<dd>change the <code>NOTRAILERS</code> flag on the device, <code>NOT</code> used by the Linux and exists for BSD compatibility.</p>
<dt><code>protodown on </code>or<code> protodown off</code></p>
<dd>change the <code>PROTODOWN</code> state on the device. Indicates that a protocol error has been detected on the port. Switch drivers can react to this error by doing a phys down on the switch port.</p>
<dt><code>protodown_reason PREASON on </code>or<code> off</code></p>
<dd>set <code>PROTODOWN</code> reasons on the device. protodown reason bit names can be enumerated under /etc/iproute2/protodown_reasons.d/. possible reasons bits 0-31</p>
<dt><code>dynamic on </code>or<code> dynamic off</code></p>
<dd>change the <code>DYNAMIC</code> flag on the device. Indicates that address can change when interface goes down (currently <code>NOT</code> used by the Linux).</p>
<dt><code>name</code><i> NAME</i></p>
<dd>change the name of the device. This operation is not recommended if the device is running or has some addresses already configured.</p>
<dt><code>txqueuelen</code><i> NUMBER</i></p>
<dd>
<dt><code>txqlen</code><i> NUMBER</i></p>
<dd>change the transmit queue length of the device.</p>
<dt><code>mtu</code><i> NUMBER</i></p>
<dd>change the <i>MTU</i> of the device.</p>
<dt><code>address</code><i> LLADDRESS</i></p>
<dd>change the station address of the interface.</p>
<dt><code>broadcast</code><i> LLADDRESS</i></p>
<dd>
<dt><code>brd</code><i> LLADDRESS</i></p>
<dd>
<dt><code>peer</code><i> LLADDRESS</i></p>
<dd>change the link layer broadcast address or the peer address when the interface is <i>POINTOPOINT</i>.</p>
<dt><code>netns</code><i> NETNSNAME </i>|<i> PID</i></p>
<dd>move the device to the network namespace associated with name <i>NETNSNAME </i>or process<i> PID.</i> Some devices are not allowed to change network namespace: loopback, bridge, wireless. These are network namespace local devices. In such case <code>ip</code> tool will return &quot;Invalid argument&quot; error. It is possible to find out if device is local to a single network namespace by checking <code>netns-local</code> flag in the output of the <code>ethtool</code>: <code>ethtool -k</code> <i>DEVICE</i> To change network namespace for wireless devices the <code>iw</code> tool can be used. But it allows to change network namespace only for physical devices and by process <i>PID</i>.</p>
<dt><code>alias</code><i> NAME</i></p>
<dd>give the device a symbolic name for easy reference.</p>
<dt><code>group</code><i> GROUP</i></p>
<dd>specify the group the device belongs to. The available groups are listed in file <code>/etc/iproute2/group</code>.</p>
<dt><code>vf</code><i> NUM</i></p>
<dd>specify a Virtual Function device to be configured. The associated PF device must be specified using the <code>dev</code> parameter. <code>mac</code><i> LLADDRESS</i> &#8211; change the station address for the specified VF. The <code>vf</code> parameter must be specified. <code>vlan</code><i> VLANID</i> &#8211; change the assigned VLAN for the specified VF. When specified, all traffic sent from the VF will be tagged with the specified VLAN ID. Incoming traffic will be filtered for the specified VLAN ID, and will have all VLAN tags stripped before being passed to the VF. Setting this parameter to 0 disables VLAN tagging and filtering. The <code>vf</code> parameter must be specified. <code>qos</code><i> VLAN-QOS</i> &#8211; assign VLAN QOS (priority) bits for the VLAN tag. When specified, all VLAN tags transmitted by the VF will include the specified priority bits in the VLAN tag. If not specified, the value is assumed to be 0. Both the <code>vf</code> and <code>vlan</code> parameters must be specified. Setting both <code>vlan</code> and <code>qos</code> as 0 disables VLAN tagging and filtering for the VF. <code>proto</code><i> VLAN-PROTO</i> &#8211; assign VLAN PROTOCOL for the VLAN tag, either 802.1Q or 802.1ad. Setting to 802.1ad, all traffic sent from the VF will be tagged with VLAN S-Tag. Incoming traffic will have VLAN S-Tags stripped before being passed to the VF. Setting to 802.1ad also enables an option to concatenate another VLAN tag, so both S-TAG and C-TAG will be inserted/stripped for outgoing/incoming traffic, respectively. If not specified, the value is assumed to be 802.1Q. Both the <code>vf</code> and <code>vlan</code> parameters must be specified. <code>rate</code><i> TXRATE</i> &#8212; change the allowed transmit bandwidth, in Mbps, for the specified VF. Setting this parameter to 0 disables rate limiting. <code>vf</code> parameter must be specified. Please use new API <code>max_tx_rate</code> option instead. <code>max_tx_rate</code><i> TXRATE</i> &#8211; change the allowed maximum transmit bandwidth, in Mbps, for the specified VF. Setting this parameter to 0 disables rate limiting. <code>vf</code> parameter must be specified. <code>min_tx_rate</code><i> TXRATE</i> &#8211; change the allowed minimum transmit bandwidth, in Mbps, for the specified VF. Minimum TXRATE should be always &lt;= Maximum TXRATE. Setting this parameter to 0 disables rate limiting. <code>vf</code> parameter must be specified. <code>spoofchk</code><i> on|off</i> &#8211; turn packet spoof checking on or off for the specified VF. <code>query_rss</code><i> on|off</i> &#8211; toggle the ability of querying the RSS configuration of a specific<br />
&nbsp;<wbr>&nbsp;VF. VF RSS information like RSS hash key may be considered sensitive<br />
&nbsp;<wbr>&nbsp;on some devices where this information is shared between VF and PF<br />
&nbsp;<wbr>&nbsp;and thus its querying may be prohibited by default. <code>state</code><i> auto|enable|disable</i> &#8211; set the virtual link state as seen by the specified VF. Setting to auto means a reflection of the PF link state, enable lets the VF to communicate with other VFs on this host even if the PF link state is down, disable causes the HW to drop any packets sent by the VF. <code>trust</code><i> on|off</i> &#8211; trust the specified VF user. This enables that VF user can set a specific feature which may impact security and/or performance. (e.g. VF multicast promiscuous mode) <code>node_guid</code><i> eui64</i> &#8211; configure node GUID for Infiniband VFs. <code>port_guid</code><i> eui64</i> &#8211; configure port GUID for Infiniband VFs.</p>
<dt><code>xdp object | pinned | off</code></p>
<dd>set (or unset) a XDP (&quot;eXpress Data Path&quot;) BPF program to run on every packet at driver level. <code>ip link</code> output will indicate a <code>xdp</code> flag for the networking device. If the driver does not have native XDP support, the kernel will fall back to a slower, driver-independent &quot;generic&quot; XDP variant. The <code>ip link</code> output will in that case indicate <code>xdpgeneric</code> instead of <code>xdp</code> only. If the driver does have native XDP support, but the program is loaded under <code>xdpgeneric object | pinned</code> then the kernel will use the generic XDP variant instead of the native one. <code>xdpdrv</code> has the opposite effect of requestsing that the automatic fallback to the generic XDP variant be disabled and in case driver is not XDP-capable error should be returned. <code>xdpdrv</code> also disables hardware offloads. <code>xdpoffload</code> in ip link output indicates that the program has been offloaded to hardware and can also be used to request the &quot;offload&quot; mode, much like <code>xdpgeneric</code> it forces program to be installed specifically in HW/FW of the apater. <code>off</code> (or <code>none</code> ) &#8211; Detaches any currently attached XDP/BPF program from the given device. <code>object</code><i> FILE </i> &#8211; Attaches a XDP/BPF program to the given device. The <i>FILE</i> points to a BPF ELF file (f.e. generated by LLVM) that contains the BPF program code, map specifications, etc. If a XDP/BPF program is already attached to the given device, an error will be thrown. If no XDP/BPF program is currently attached, the device supports XDP and the program from the BPF ELF file passes the kernel verifier, then it will be attached to the device. If the option <i>-force</i> is passed to <code>ip</code> then any prior attached XDP/BPF program will be atomically overridden and no error will be thrown in this case. If no <code>section</code> option is passed, then the default section name (&quot;prog&quot;) will be assumed, otherwise the provided section name will be used. If no <code>verbose</code> option is passed, then a verifier log will only be dumped on load error. See also <code>EXAMPLES</code> section for usage examples. <code>section</code><i> NAME </i> &#8211; Specifies a section name that contains the BPF program code. If no section name is specified, the default one (&quot;prog&quot;) will be used. This option is to be passed with the <code>object</code> option. <code>verbose</code> &#8211; Act in verbose mode. For example, even in case of success, this will print the verifier log in case a program was loaded from a BPF ELF file. <code>pinned</code><i> FILE </i> &#8211; Attaches a XDP/BPF program to the given device. The <i>FILE</i> points to an already pinned BPF program in the BPF file system. The option <code>section</code> doesn&#8217;t apply here, but otherwise semantics are the same as with the option <code>object</code> described already.</p>
<dt><code>master</code><i> DEVICE</i></p>
<dd>set master device of the device (enslave device).</p>
<dt><code>nomaster</code></p>
<dd>unset master device of the device (release device).</p>
<dt><code>addrgenmode</code><i> eui64|none|stable_secret|random</i></p>
<dd>set the IPv6 address generation mode <i>eui64</i> &#8211; use a Modified EUI-64 format interface identifier <i>none</i> &#8211; disable automatic address generation <i>stable_secret</i> &#8211; generate the interface identifier based on a preset<br />
&nbsp;<wbr>&nbsp;/proc/sys/net/ipv6/conf/{default,DEVICE}/stable_secret <i>random</i> &#8211; like stable_secret, but auto-generate a new random secret if none is set</p>
<dt><code>link-netnsid </code></p>
<dd>set peer netnsid for a cross-netns interface</p>
<dt><code>type</code><i> ETYPE TYPE_ARGS</i></p>
<dd>Change type-specific settings. For a list of supported types and arguments refer to the description of <code>ip link add</code> above. In addition to that, it is possible to manipulate settings to slave devices:</p>
<dt>Bridge Slave Support</p>
<dd>For a link with master <code>bridge</code> the following additional arguments are supported: <code>ip link set type bridge_slave</code> [ <code>fdb_flush</code> ] [ <code>state</code><i> STATE</i> ] [ <code>priority</code><i> PRIO</i> ] [ <code>cost</code><i> COST</i> ] [ <code>guard</code> { <code>on</code> | <code>off</code> } ] [ <code>hairpin</code> { <code>on</code> | <code>off</code> } ] [ <code>fastleave</code> { <code>on</code> | <code>off</code> } ] [ <code>root_block</code> { <code>on</code> | <code>off</code> } ] [ <code>learning</code> { <code>on</code> | <code>off</code> } ] [ <code>flood</code> { <code>on</code> | <code>off</code> } ] [ <code>proxy_arp</code> { <code>on</code> | <code>off</code> } ] [ <code>proxy_arp_wifi</code> { <code>on</code> | <code>off</code> } ] [ <code>mcast_router</code><i> MULTICAST_ROUTER</i> ] [ <code>mcast_fast_leave</code> { <code>on</code> | <code>off</code>} ] [ <code>mcast_flood</code> { <code>on</code> | <code>off</code> } ] [ <code>mcast_to_unicast</code> { <code>on</code> | <code>off</code> } ] [ <code>group_fwd_mask</code> MASK ] [ <code>neigh_suppress</code> { <code>on</code> | <code>off</code> } ] [ <code>vlan_tunnel</code> { <code>on</code> | <code>off</code> } ] [ <code>isolated</code> { <code>on</code> | <code>off</code> } ] [ <code>backup_port</code> DEVICE ] [ <code>nobackup_port</code> ] <code>fdb_flush</code> &#8211; flush bridge slave&#8217;s fdb dynamic entries. <code>state</code><i> STATE</i> &#8211; Set port state. <i>STATE</i> is a number representing the following states: <code>0</code> (disabled), <code>1</code> (listening), <code>2</code> (learning), <code>3</code> (forwarding), <code>4</code> (blocking). <code>priority</code><i> PRIO</i> &#8211; set port priority (allowed values are between 0 and 63, inclusively). <code>cost</code><i> COST</i> &#8211; set port cost (allowed values are between 1 and 65535, inclusively). <code>guard</code> { <code>on</code> | <code>off</code> } &#8211; block incoming BPDU packets on this port. <code>hairpin</code> { <code>on</code> | <code>off</code> } &#8211; enable hairpin mode on this port. This will allow incoming packets on this port to be reflected back. <code>fastleave</code> { <code>on</code> | <code>off</code> } &#8211; enable multicast fast leave on this port. <code>root_block</code> { <code>on</code> | <code>off</code> } &#8211; block this port from becoming the bridge&#8217;s root port. <code>learning</code> { <code>on</code> | <code>off</code> } &#8211; allow MAC address learning on this port. <code>flood</code> { <code>on</code> | <code>off</code> } &#8211; open the flood gates on this port, i.e. forward all unicast frames to this port also. Requires <code>proxy_arp</code> and <code>proxy_arp_wifi</code> to be turned off. <code>proxy_arp</code> { <code>on</code> | <code>off</code> } &#8211; enable proxy ARP on this port. <code>proxy_arp_wifi</code> { <code>on</code> | <code>off</code> } &#8211; enable proxy ARP on this port which meets extended requirements by IEEE 802.11 and Hotspot 2.0 specifications. <code>mcast_router</code><i> MULTICAST_ROUTER</i> &#8211; configure this port for having multicast routers attached. A port with a multicast router will receive all multicast traffic. <i>MULTICAST_ROUTER</i> may be either <code>0</code> to disable multicast routers on this port, <code>1</code> to let the system detect the presence of routers (this is the default), <code>2</code> to permanently enable multicast traffic forwarding on this port or <code>3</code> to enable multicast routers temporarily on this port, not depending on incoming queries. <code>mcast_fast_leave</code> { <code>on</code> | <code>off</code> } &#8211; this is a synonym to the <code>fastleave</code> option above. <code>mcast_flood</code> { <code>on</code> | <code>off</code> } &#8211; controls whether a given port will flood multicast traffic for which<br />
&nbsp;<wbr>&nbsp;there is no MDB entry. <code>mcast_to_unicast</code> { <code>on</code> | <code>off</code> } &#8211; controls whether a given port will replicate packets using unicast<br />
&nbsp;<wbr>&nbsp;instead of multicast. By default this flag is off. <code>group_fwd_mask</code><i> MASK </i> &#8211; set the group forward mask. This is the bitmask that is applied to decide whether to forward incoming frames destined to link-local addresses, ie addresses of the form 01:80:C2:00:00:0X (defaults to 0, ie the bridge does not forward any link-local frames coming on this port). <code>neigh_suppress</code> { <code>on</code> | <code>off</code> } &#8211; controls whether neigh discovery (arp and nd) proxy and suppression is enabled on the port. By default this flag is off. <code>vlan_tunnel</code> { <code>on</code> | <code>off</code> } &#8211; controls whether vlan to tunnel mapping is enabled on the port. By default this flag is off. <code>backup_port</code><i> DEVICE</i> &#8211; if the port loses carrier all traffic will be redirected to the configured backup port <code>nobackup_port</code> &#8211; removes the currently configured backup port</p>
<dt>Bonding Slave Support</p>
<dd>For a link with master <code>bond</code> the following additional arguments are supported: <code>ip link set type bond_slave</code> [ <code>queue_id</code><i> ID</i> ] <code>queue_id</code><i> ID</i> &#8211; set the slave&#8217;s queue ID (a 16bit unsigned value).</p>
<dt>MACVLAN and MACVTAP Support</p>
<dd>Modify list of allowed macaddr for link in source mode. <code>ip link set type { macvlan | macvap } </code> [ <code>macaddr</code><i> </i><i>COMMAND</i><i>MACADDR</i><code> &#8230;</code> ] Commands: <code>add</code> &#8211; add MACADDR to allowed list <code>set</code> &#8211; replace allowed list <code>del</code> &#8211; remove MACADDR from allowed list <code>flush</code> &#8211; flush whole allowed list Update the broadcast/multicast queue length. <code>ip link set type { macvlan | macvap } </code> [ <code>bcqueuelen</code><i> LENGTH </i> ] <code>bcqueuelen</code><i> LENGTH </i> &#8211; Set the length of the RX queue used to process broadcast and multicast packets. <i>LENGTH</i> must be a positive integer in the range [0-4294967295]. Setting a length of 0 will effectively drop all broadcast/multicast traffic. If not specified the macvlan driver default (1000) is used. Note that all macvlans that share the same underlying device are using the same queue. The parameter here is a <code>request</code>, the actual queue length used will be the maximum length that any macvlan interface has requested. When listing device parameters both the bcqueuelen parameter as well as the actual used bcqueuelen are listed to better help the user understand the setting.</dl>
<h3>ip link show &#8211; display device attributes</h3>
<dl>
<dt><code>dev</code><i> NAME </i><code>(default)</code></p>
<dd><i>NAME</i> specifies the network device to show.</p>
<dt><code>group</code><i> GROUP </i></p>
<dd><i>GROUP</i> specifies what group of devices to show.</p>
<dt><code>up</code></p>
<dd>only display running interfaces.</p>
<dt><code>master</code><i> DEVICE </i></p>
<dd><i>DEVICE</i> specifies the master device which enslaves devices to show.</p>
<dt><code>vrf</code><i> NAME </i></p>
<dd><i>NAME</i> specifies the VRF which enslaves devices to show.</p>
<dt><code>type</code><i> TYPE </i></p>
<dd><i>TYPE</i> specifies the type of devices to show. Note that the type name is not checked against the list of supported types &#8211; instead it is sent as-is to the kernel. Later it is used to filter the returned interface list by comparing it with the relevant attribute in case the kernel didn&#8217;t filter already. Therefore any string is accepted, but may lead to empty output.</dl>
<h3>ip link xstats &#8211; display extended statistics</h3>
<dl>
<dt><code>type</code><i> TYPE </i></p>
<dd><i>TYPE</i> specifies the type of devices to display extended statistics for.</dl>
<h3>ip link afstats &#8211; display address-family specific statistics</h3>
<dl>
<dt><code>dev</code><i> DEVICE </i></p>
<dd><i>DEVICE</i> specifies the device to display address-family statistics for.</dl>
<h3>ip link help &#8211; display help</h3>
<p><i>TYPE</i> specifies which help of link type to display.</p>
<h3><i>GROUP</i></h3>
<p>may be a number or a string from the file <code>/etc/iproute2/group</code> which can be manually filled. </p>
<h2>Examples</h2>
<p>ip link show</p>
<dl>
<dd>Shows the state of all network interfaces on the system.</dl>
<p> ip link show type bridge</p>
<dl>
<dd>Shows the bridge devices.</dl>
<p> ip link show type vlan</p>
<dl>
<dd>Shows the vlan devices.</dl>
<p> ip link show master br0</p>
<dl>
<dd>Shows devices enslaved by br0</dl>
<p> ip link set dev ppp0 mtu 1400</p>
<dl>
<dd>Change the MTU the ppp0 device.</dl>
<p> ip link add link eth0 name eth0.10 type vlan id 10</p>
<dl>
<dd>Creates a new vlan device eth0.10 on device eth0.</dl>
<p> ip link delete dev eth0.10</p>
<dl>
<dd>Removes vlan device.</dl>
<p> ip link help gre</p>
<dl>
<dd>Display help for the gre link type.</dl>
<p> ip link add name tun1 type ipip remote 192.168.1.1 local 192.168.1.2 ttl 225 encap gue encap-sport auto encap-dport 5555 encap-csum encap-remcsum</p>
<dl>
<dd>Creates an IPIP that is encapsulated with Generic UDP Encapsulation, and the outer UDP checksum and remote checksum offload are enabled.</dl>
<p> ip link set dev eth0 xdp obj prog.o</p>
<dl>
<dd>Attaches a XDP/BPF program to device eth0, where the program is located in prog.o, section &quot;prog&quot; (default section). In case a XDP/BPF program is already attached, throw an error.</dl>
<p> ip -force link set dev eth0 xdp obj prog.o sec foo</p>
<dl>
<dd>Attaches a XDP/BPF program to device eth0, where the program is located in prog.o, section &quot;foo&quot;. In case a XDP/BPF program is already attached, it will be overridden by the new one.</dl>
<p> ip -force link set dev eth0 xdp pinned /sys/fs/bpf/foo</p>
<dl>
<dd>Attaches a XDP/BPF program to device eth0, where the program was previously pinned as an object node into BPF file system under name foo.</dl>
<p> ip link set dev eth0 xdp off</p>
<dl>
<dd>If a XDP/BPF program is attached on device eth0, detach it and effectively turn off XDP for device eth0.</dl>
<p> ip link add link wpan0 lowpan0 type lowpan</p>
<dl>
<dd>Creates a 6LoWPAN interface named lowpan0 on the underlying IEEE 802.15.4 device wpan0.</dl>
<p> ip link add dev ip6erspan11 type ip6erspan seq key 102 local fc00:100::2 remote fc00:100::1 erspan_ver 2 erspan_dir ingress erspan_hwid 17</p>
<dl>
<dd>Creates a IP6ERSPAN version 2 interface named ip6erspan00.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ip-netns/">ip-netns</a></code>(8), <code><a href="/docs/linux/man/8-ethtool/">ethtool</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
