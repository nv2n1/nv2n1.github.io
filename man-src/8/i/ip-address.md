---
title: "ip-address(8)"
name: "ip-address"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-address/"
description: "ip-address – protocol address management"
---

<p>ip-address &#8211; protocol address management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

address

{ COMMAND |

    help }
</code></pre>
<p> <code>ip address</code> { <code>add</code> | <code>change</code> | <code>replace</code> } <i>IFADDR</i><code> dev </code><i>IFNAME</i> [ <i>LIFETIME</i> ] [ <i>CONFFLAG-LIST</i> ]<br />
 <code>ip address del</code> <i>IFADDR</i><code> dev </code><i>IFNAME</i><code> [ </code><i>mngtmpaddr</i><code> ]</code><br />
 <code>ip address</code> { <code>save</code> | <code>flush</code> } [ <code>dev</code> <i>IFNAME</i> ] [ <code>scope</code> <i>SCOPE-ID</i> ] [ <code>metric</code> <i>METRIC</i> ] [ <code>to</code> <i>PREFIX</i> ] [ <i>FLAG-LIST</i> ] [ <code>label</code> <i>PATTERN</i> ] [ <i>up</i> ]<br />
 <code>ip address</code> [ <code>show</code> [ <code>dev</code> <i>IFNAME</i> ] [ <code>scope</code> <i>SCOPE-ID</i> ] [ <code>to</code> <i>PREFIX</i> ] [ <i>FLAG-LIST</i> ] [ <code>label</code> <i>PATTERN</i> ] [ <code>master</code> <i>DEVICE</i> ] [ <code>type</code> <i>TYPE</i> ] [ <code>vrf</code> <i>NAME</i> ] [ <code>up</code> ] ] </p>
<pre><code>ip address { showdump | restore }
IFADDR := PREFIX | ADDR

peer

PREFIX [

broadcast

ADDR ] [

anycast

ADDR ] [

label

LABEL ] [

scope

SCOPE-ID ]
SCOPE-ID :=

[ host | link | global |

NUMBER ]
FLAG-LIST := [ FLAG-LIST ] FLAG
FLAG := [

[-]permanent |

[-]dynamic |

[-]secondary |

[-]primary |

[-]tentative |

[-]deprecated |

[-]dadfailed |

[-]temporary |

CONFFLAG-LIST ]
CONFFLAG-LIST := [ CONFFLAG-LIST ] CONFFLAG
CONFFLAG :=

[ home | mngtmpaddr | nodad | optimstic | noprefixroute | autojoin ]
LIFETIME := [

valid_lft LFT

] [ preferred_lft

LFT ]
LFT := [

forever |

SECONDS ]
TYPE := [

bridge |

bridge_slave |

bond |

bond_slave |

can |

dummy |

hsr |

ifb |

ipoib |

macvlan |

macvtap |

vcan |

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

vrf |

nlmon |

ipvlan |

lowpan |

geneve |

macsec ]
</code></pre>
<h2>Description</h2>
<p>The <code>address</code> is a protocol (IPv4 or IPv6) address attached to a network device. Each device must have at least one address to use the corresponding protocol. It is possible to have several different addresses attached to one device. These addresses are not discriminated, so that the term <code>alias</code> is not quite appropriate for them and we do not use it in this document. The <code>ip address</code> command displays addresses and their properties, adds new addresses and deletes old ones.</p>
<h3>ip address add &#8211; add new protocol address.</h3>
<dl>
<dt><code>dev</code><i> IFNAME </i></p>
<dd>the name of the device to add the address to.</p>
<dt><code>local</code><i> ADDRESS </i><code>(default)</code></p>
<dd>the address of the interface. The format of the address depends on the protocol. It is a dotted quad for IP and a sequence of hexadecimal halfwords separated by colons for IPv6. The <i>ADDRESS</i> may be followed by a slash and a decimal number which encodes the network prefix length.</p>
<dt><code>peer</code><i> ADDRESS</i></p>
<dd>the address of the remote endpoint for pointopoint interfaces. Again, the <i>ADDRESS</i> may be followed by a slash and a decimal number, encoding the network prefix length. If a peer address is specified, the local address cannot have a prefix length. The network prefix is associated with the peer rather than with the local address.</p>
<dt><code>broadcast</code><i> ADDRESS</i></p>
<dd>the broadcast address on the interface. It is possible to use the special symbols <code>&#8216;+&#8217;</code> and <code>&#8216;-&#8216;</code> instead of the broadcast address. In this case, the broadcast address is derived by setting/resetting the host bits of the interface prefix.</p>
<dt><code>label</code><i> LABEL</i></p>
<dd>Each address may be tagged with a label string. In order to preserve compatibility with Linux-2.0 net aliases, this string must coincide with the name of the device or must be prefixed with the device name followed by colon. The maximum allowed total length of label is 15 characters.</p>
<dt><code>scope</code><i> SCOPE_VALUE</i></p>
<dd>the scope of the area where this address is valid. The available scopes are listed in file <code>/etc/iproute2/rt_scopes</code>. Predefined scope values are: <code>global</code> &#8211; the address is globally valid. <code>site</code> &#8211; (IPv6 only, deprecated) the address is site local, i.e. it is valid inside this site. <code>link</code> &#8211; the address is link local, i.e. it is valid only on this device. <code>host</code> &#8211; the address is valid only inside this host.</p>
<dt><code>metric</code><i> NUMBER</i></p>
<dd>priority of prefix route associated with address.</p>
<dt><code>valid_lft</code><i> LFT</i></p>
<dd>the valid lifetime of this address; see section 5.5.4 of RFC 4862. When it expires, the address is removed by the kernel. Defaults to <code>forever</code>.</p>
<dt><code>preferred_lft</code><i> LFT</i></p>
<dd>the preferred lifetime of this address; see section 5.5.4 of RFC 4862. When it expires, the address is no longer used for new outgoing connections. Defaults to <code>forever</code>.</p>
<dt><code>home</code></p>
<dd>(IPv6 only) designates this address the &quot;home address&quot; as defined in RFC 6275.</p>
<dt><code>mngtmpaddr</code></p>
<dd>(IPv6 only) make the kernel manage temporary addresses created from this one as template on behalf of Privacy Extensions (RFC3041). For this to become active, the <code>use_tempaddr</code> sysctl setting has to be set to a value greater than zero. The given address needs to have a prefix length of 64. This flag allows to use privacy extensions in a manually configured network, just like if stateless auto-configuration was active.</p>
<dt><code>nodad</code></p>
<dd>(IPv6 only) do not perform Duplicate Address Detection (RFC 4862) when adding this address.</p>
<dt><code>optimistic</code></p>
<dd>(IPv6 only) When performing Duplicate Address Detection, use the RFC 4429 optimistic variant.</p>
<dt><code>noprefixroute</code></p>
<dd>Do not automatically create a route for the network prefix of the added address, and don&#8217;t search for one to delete when removing the address. Changing an address to add this flag will remove the automatically added prefix route, changing it to remove this flag will create the prefix route automatically.</p>
<dt><code>autojoin</code></p>
<dd>Joining multicast groups on Ethernet level via <code>ip maddr</code> command does not work if connected to an Ethernet switch that does IGMP snooping since the switch would not replicate multicast packets on ports that did not have IGMP reports for the multicast addresses. Linux VXLAN interfaces created via <code>ip link add vxlan</code> have the <code>group</code> option that enables them to do the required join. Using the <code>autojoin</code> flag when adding a multicast address enables similar functionality for Openvswitch VXLAN interfaces as well as other tunneling mechanisms that need to receive multicast traffic.</dl>
<h3>ip address delete &#8211; delete protocol address</h3>
<p><code>Arguments:</code> coincide with the arguments of <code>ip addr add.</code> The device name is a required argument. The rest are optional. If no arguments are given, the first address is deleted.</p>
<h3>ip address show &#8211; look at protocol addresses</h3>
<dl>
<dt><code>dev</code><i> IFNAME </i><code>(default)</code></p>
<dd>name of device.</p>
<dt><code>scope</code><i> SCOPE_VAL</i></p>
<dd>only list addresses with this scope.</p>
<dt><code>to</code><i> PREFIX</i></p>
<dd>only list addresses matching this prefix.</p>
<dt><code>label</code><i> PATTERN</i></p>
<dd>only list addresses with labels matching the <i>PATTERN</i>. <i>PATTERN</i> is a usual shell style pattern.</p>
<dt><code>master</code><i> DEVICE</i></p>
<dd>only list interfaces enslaved to this master device.</p>
<dt><code>vrf</code><i> NAME </i></p>
<dd>only list interfaces enslaved to this vrf.</p>
<dt><code>type</code><i> TYPE</i></p>
<dd>only list interfaces of the given type. Note that the type name is not checked against the list of supported types &#8211; instead it is sent as-is to the kernel. Later it is used to filter the returned interface list by comparing it with the relevant attribute in case the kernel didn&#8217;t filter already. Therefore any string is accepted, but may lead to empty output.</p>
<dt><code>up</code></p>
<dd>only list running interfaces.</p>
<dt><code>dynamic</code> and <code>permanent</code></p>
<dd>(IPv6 only) only list addresses installed due to stateless address configuration or only list permanent (not dynamic) addresses. These two flags are inverses of each other, so <code>-dynamic</code> is equal to <code>permanent</code> and <code>-permanent</code> is equal to <code>dynamic</code>.</p>
<dt><code>tentative</code></p>
<dd>(IPv6 only) only list addresses which have not yet passed duplicate address detection.</p>
<dt><code>-tentative</code></p>
<dd>(IPv6 only) only list addresses which are not in the process of duplicate address detection currently.</p>
<dt><code>deprecated</code></p>
<dd>(IPv6 only) only list deprecated addresses.</p>
<dt><code>-deprecated</code></p>
<dd>(IPv6 only) only list addresses not being deprecated.</p>
<dt><code>dadfailed</code></p>
<dd>(IPv6 only) only list addresses which have failed duplicate address detection.</p>
<dt><code>-dadfailed</code></p>
<dd>(IPv6 only) only list addresses which have not failed duplicate address detection.</p>
<dt><code>temporary</code> or <code>secondary</code></p>
<dd>List temporary IPv6 or secondary IPv4 addresses only. The Linux kernel shares a single bit for those, so they are actually aliases for each other although the meaning differs depending on address family.</p>
<dt><code>-temporary</code> or <code>-secondary</code></p>
<dd>These flags are aliases for <code>primary</code>.</p>
<dt><code>primary</code></p>
<dd>List only primary addresses, in IPv6 exclude temporary ones. This flag is the inverse of <code>temporary</code> and <code>secondary</code>.</p>
<dt><code>-primary</code></p>
<dd>This is an alias for <code>temporary</code> or <code>secondary</code>.</dl>
<h3>ip address flush &#8211; flush protocol addresses</h3>
<p>This command flushes the protocol addresses selected by some criteria. This command has the same arguments as <code>show</code> except that <code>type</code> and <code>master</code> selectors are not supported. Another difference is that it does not run when no arguments are given. <code>Warning:</code> This command and other <code>flush</code> commands are unforgiving. They will cruelly purge all the addresses. With the <code>-statistics</code> option, the command becomes verbose. It prints out the number of deleted addresses and the number of rounds made to flush the address list. If this option is given twice, <code>ip address flush</code> also dumps all the deleted addresses in the format described in the previous subsection. </p>
<h2>Examples</h2>
<p>ip address show</p>
<dl>
<dd>Shows IPv4 and IPv6 addresses assigned to all network interfaces. The &#8216;show&#8217; subcommand can be omitted.</dl>
<p> ip address show up</p>
<dl>
<dd>Same as above except that only addresses assigned to active network interfaces are shown.</dl>
<p> ip address show dev eth0</p>
<dl>
<dd>Shows IPv4 and IPv6 addresses assigned to network interface eth0.</dl>
<p> ip address add 2001:0db8:85a3::0370:7334/64 dev eth1</p>
<dl>
<dd>Adds an IPv6 address to network interface eth1.</dl>
<p> ip address delete 2001:0db8:85a3::0370:7334/64 dev eth1</p>
<dl>
<dd>Delete the IPv6 address added above.</dl>
<p> ip address flush dev eth4 scope global</p>
<dl>
<dd>Removes all global IPv4 and IPv6 addresses from device eth4. Without &#8216;scope global&#8217; it would remove all addresses including IPv6 link-local ones.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
