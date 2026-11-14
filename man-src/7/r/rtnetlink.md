---
title: "rtnetlink(7)"
name: "rtnetlink"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rtnetlink/"
description: "rtnetlink – Linux IPv4 routing socket"
---

<p>rtnetlink &#8211; Linux IPv4 routing socket</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;asm/types.h&gt;

#include &lt;linux/if_link.h&gt;

#include &lt;linux/netlink.h&gt;

#include &lt;linux/rtnetlink.h&gt;

#include &lt;sys/socket.h&gt;
rtnetlink_socket = socket(AF_NETLINK, int socket_type, NETLINK_ROUTE);</code></pre>
<h2>Description</h2>
<p>Rtnetlink allows the kernel&#8217;s routing tables to be read and altered. It is used within the kernel to communicate between various subsystems, though this usage is not documented here, and for communication with user-space programs. Network routes, IP addresses, link parameters, neighbor setups, queueing disciplines, traffic classes and packet classifiers may all be controlled through <code>NETLINK_ROUTE</code> sockets. It is based on netlink messages; see <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) for more information.</p>
<h3>Routing attributes</h3>
<p>Some rtnetlink messages have optional attributes after the initial header: unsigned int rtm_flags;<br />
}<br />
;</p>
<p>rtm_typeRoute type</p>
<p>        RTN_UNSPECunknown route</p>
<p>            RTN_UNICASTa gateway or<br />
    direct route</p>
<p>        RTN_LOCALa local interface route</p>
<p>            RTN_BROADCAST<br />
                a local broadcast<br />
                route(sent as a broadcast)</p>
<p>                    RTN_ANYCAST<br />
    a local broadcast route(sent as a unicast)</p>
<p>        RTN_MULTICASTa multicast route</p>
<p>    RTN_BLACKHOLEa packet dropping route</p>
<p>    RTN_UNREACHABLEan unreachable destination</p>
<p>    RTN_PROHIBITa packet rejection route</p>
<p>    RTN_THROWcontinue routing lookup in another table</p>
<p>    RTN_NATa network address translation rule</p>
<p>    RTN_XRESOLVE<br />
    refer to an external resolver(not implemented)</p>
<p>        rtm_protocolRoute origin</p>
<p>    RTPROT_UNSPECunknown</p>
<p>    RTPROT_REDIRECT<br />
    by an ICMP redirect(currently unused)</p>
<p>        RTPROT_KERNELby the kernel</p>
<p>    RTPROT_BOOTduring boot</p>
<p>    RTPROT_STATICby the administrator These attributes should be manipulated using only the RTA_* macros or libnetlink, see <code><a href="/docs/linux/man/3-rtnetlink/">rtnetlink</a></code>(3).</p>
<h3>Messages</h3>
<p>Rtnetlink consists of these message types (in addition to standard netlink messages):</p>
<dl>
<dt><code>RTM_NEWLINK</code>, <code>RTM_DELLINK</code>, <code>RTM_GETLINK</code></p>
<dd>Create, remove, or get information about a specific network interface. These messages contain an <i>ifinfomsg</i> structure followed by a series of <i>rtattr</i> structures.</p>
<dd>struct ifinfomsg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;ifi_family;&nbsp;/*&nbsp;AF_UNSPEC&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short ifi_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Device type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifi_index;&nbsp;<wbr>&nbsp;/*&nbsp;Interface index&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifi_flags;&nbsp;<wbr>&nbsp;/*&nbsp;Device flags&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifi_change;&nbsp;/*&nbsp;change mask&nbsp;*/ };</p>
<dd><i>ifi_flags</i> contains the device flags, see <code><a href="/docs/linux/man/7-netdevice/">netdevice</a></code>(7); <i>ifi_index</i> is the unique interface index (since Linux 3.7, it is possible to feed a nonzero value with the <code>RTM_NEWLINK</code> message, thus creating a link with the given <i>ifindex</i>); <i>ifi_change</i> is reserved for future use and should be always set to 0xFFFFFFFF. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Routing attributes
</td>
</tr>
<tr VALIGN=top>
<td><code>rta_type</code></td>
<td>Value type</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_UNSPEC</code></td>
<td>&#8211;</td>
<td>unspecified
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_ADDRESS</code></td>
<td>hardware address</td>
<td>interface L2 address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_BROADCAST</code></td>
<td>hardware address</td>
<td>L2 broadcast address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_IFNAME</code></td>
<td>asciiz string</td>
<td>Device name
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_MTU</code></td>
<td>unsigned int</td>
<td>MTU of the device
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_LINK</code></td>
<td>int</td>
<td>Link type
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_QDISC</code></td>
<td>asciiz string</td>
<td>Queueing discipline
</td>
</tr>
<tr VALIGN=top>
<td><code>IFLA_STATS</code></td>
<td> see below </td>
<td>Interface Statistics
</td>
</tr>
</table>
<dd>The value type for <code>IFLA_STATS</code> is <i>struct rtnl_link_stats</i> (<i>struct net_device_stats</i> in Linux 2.4 and earlier).</p>
<dt><code>RTM_NEWADDR</code>, <code>RTM_DELADDR</code>, <code>RTM_GETADDR</code></p>
<dd>Add, remove, or receive information about an IP address associated with an interface. In Linux 2.2, an interface can carry multiple IP addresses, this replaces the alias device concept in 2.0. In Linux 2.2, these messages support IPv4 and IPv6 addresses. They contain an <i>ifaddrmsg</i> structure, optionally followed by <i>rtattr</i> routing attributes.</p>
<dd>struct ifaddrmsg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char ifa_family;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address type&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char ifa_prefixlen;&nbsp;/*&nbsp;Prefixlength of address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char ifa_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char ifa_scope;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address scope&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;ifa_index;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Interface index&nbsp;*/ };</p>
<dd><i>ifa_family</i> is the address family type (currently <code>AF_INET</code> or <code>AF_INET6</code>), <i>ifa_prefixlen</i> is the length of the address mask of the address if defined for the family (like for IPv4), <i>ifa_scope</i> is the address scope, <i>ifa_index</i> is the interface index of the interface the address is associated with. <i>ifa_flags</i> is a flag word of <code>IFA_F_SECONDARY</code> for secondary address (old alias interface), <code>IFA_F_PERMANENT</code> for a permanent address set by the user and other undocumented flags. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Attributes
</td>
</tr>
<tr VALIGN=top>
<td><code>rta_type</code></td>
<td>Value type</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_UNSPEC</code></td>
<td>&#8211;</td>
<td>unspecified
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_ADDRESS</code></td>
<td>raw protocol address</td>
<td>interface address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_LOCAL</code></td>
<td>raw protocol address</td>
<td>local address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_LABEL</code></td>
<td>asciiz string</td>
<td>name of the interface
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_BROADCAST</code></td>
<td>raw protocol address</td>
<td>broadcast address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_ANYCAST</code></td>
<td>raw protocol address</td>
<td>anycast address
</td>
</tr>
<tr VALIGN=top>
<td><code>IFA_CACHEINFO</code></td>
<td>struct ifa_cacheinfo</td>
<td>Address information
</td>
</tr>
</table>
<dt><code>RTM_NEWROUTE</code>, <code>RTM_DELROUTE</code>, <code>RTM_GETROUTE</code></p>
<dd>Create, remove, or receive information about a network route. These messages contain an <i>rtmsg</i> structure with an optional sequence of <i>rtattr</i> structures following. For <code>RTM_GETROUTE</code>, setting <i>rtm_dst_len</i> and <i>rtm_src_len</i> to 0 means you get all entries for the specified routing table. For the other fields, except <i>rtm_table</i> and <i>rtm_protocol</i>, 0 is the wildcard.</p>
<dd>struct rtmsg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_family;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address family of route&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_dst_len;&nbsp;<wbr>&nbsp;/*&nbsp;Length of destination&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_src_len;&nbsp;<wbr>&nbsp;/*&nbsp;Length of source&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_tos;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;TOS filter&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_table;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Routing table ID;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;see RTA_TABLE below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_protocol;&nbsp;/*&nbsp;Routing protocol;&nbsp;see below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_scope;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See below&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char rtm_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;See below&nbsp;*/ </p>
<pre><code>unsigned int rtm_flags;
}
;

rtm_typeRoute type

        RTN_UNSPECunknown route

            RTN_UNICASTa gateway or
    direct route

        RTN_LOCALa local interface route

            RTN_BROADCAST
                a local broadcast
                route(sent as a broadcast)

                    RTN_ANYCAST
    a local broadcast route(sent as a unicast)

        RTN_MULTICASTa multicast route

    RTN_BLACKHOLEa packet dropping route

    RTN_UNREACHABLEan unreachable destination

    RTN_PROHIBITa packet rejection route

    RTN_THROWcontinue routing lookup in another table

    RTN_NATa network address translation rule

    RTN_XRESOLVE
    refer to an external resolver(not implemented)

        rtm_protocolRoute origin

    RTPROT_UNSPECunknown

    RTPROT_REDIRECT
    by an ICMP redirect(currently unused)

        RTPROT_KERNELby the kernel

    RTPROT_BOOTduring boot

    RTPROT_STATICby the administrator</code></pre>
<p> Values larger than <code>RTPROT_STATIC</code> are not interpreted by the kernel, they are just for user information. They may be used to tag the source of a routing information or to distinguish between multiple routing daemons. See <i>&lt;linux/rtnetlink.h&gt;</i> for the routing daemon identifiers which are already assigned.</p>
<dd><i>rtm_scope</i> is the distance to the destination: </p>
<table>
<tr VALIGN=top>
<td><code>RT_SCOPE_UNIVERSE</code></td>
<td>global route
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_SCOPE_SITE</code></td>
<td> interior route in the local autonomous system
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_SCOPE_LINK</code></td>
<td>route on this link
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_SCOPE_HOST</code></td>
<td>route on the local host
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_SCOPE_NOWHERE</code></td>
<td>destination doesn&#8217;t exist
</td>
</tr>
</table>
<p> The values between <code>RT_SCOPE_UNIVERSE</code> and <code>RT_SCOPE_SITE</code> are available to the user.</p>
<dd>The <i>rtm_flags</i> have the following meanings: </p>
<table>
<tr VALIGN=top>
<td><code>RTM_F_NOTIFY</code></td>
<td> if the route changes, notify the user via rtnetlink
</td>
</tr>
<tr VALIGN=top>
<td><code>RTM_F_CLONED</code></td>
<td>route is cloned from another route
</td>
</tr>
<tr VALIGN=top>
<td><code>RTM_F_EQUALIZE</code></td>
<td>a multipath equalizer (not yet implemented)
</td>
</tr>
</table>
<p> <i>rtm_table</i> specifies the routing table </p>
<table>
<tr VALIGN=top>
<td><code>RT_TABLE_UNSPEC</code></td>
<td>an unspecified routing table
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_TABLE_DEFAULT</code></td>
<td>the default table
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_TABLE_MAIN</code></td>
<td>the main table
</td>
</tr>
<tr VALIGN=top>
<td><code>RT_TABLE_LOCAL</code></td>
<td>the local table
</td>
</tr>
</table>
<p> The user may assign arbitrary values between <code>RT_TABLE_UNSPEC</code> and <code>RT_TABLE_DEFAULT</code>. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Attributes
</td>
</tr>
<tr VALIGN=top>
<td><code>rta_type&nbsp;<wbr>&nbsp;</code></td>
<td>Value type&nbsp;<wbr>&nbsp;</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_UNSPEC&nbsp;<wbr>&nbsp;</code></td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_DST&nbsp;<wbr>&nbsp;</code></td>
<td>protocol address&nbsp;<wbr>&nbsp;</td>
<td>Route destination address
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_SRC&nbsp;<wbr>&nbsp;</code></td>
<td>protocol address&nbsp;<wbr>&nbsp;</td>
<td>Route source address
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_IIF&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>Input interface index
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_OIF&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>Output interface index
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_GATEWAY&nbsp;<wbr>&nbsp;</code></td>
<td>protocol address&nbsp;<wbr>&nbsp;</td>
<td>The gateway of the route
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_PRIORITY&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>Priority of route
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_PREFSRC&nbsp;<wbr>&nbsp;</code></td>
<td>protocol address&nbsp;<wbr>&nbsp;</td>
<td>Preferred source address
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_METRICS&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>Route metric
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_MULTIPATH&nbsp;<wbr>&nbsp;</code></td>
<td>&nbsp;<wbr>&nbsp;</td>
<td> Multipath nexthop data br (see below).
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_PROTOINFO&nbsp;<wbr>&nbsp;</code></td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>No longer used
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_FLOW&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>Route realm
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_CACHEINFO&nbsp;<wbr>&nbsp;</code></td>
<td>struct rta_cacheinfo&nbsp;<wbr>&nbsp;</td>
<td>(see linux/rtnetlink.h)
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_SESSION&nbsp;<wbr>&nbsp;</code></td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>No longer used
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_MP_ALGO&nbsp;<wbr>&nbsp;</code></td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>No longer used
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_TABLE&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td> Routing table ID; if set,<br />
 rtm_table is ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_MARK&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_MFC_STATS&nbsp;<wbr>&nbsp;</code></td>
<td>struct rta_mfc_stats&nbsp;<wbr>&nbsp;</td>
<td>(see linux/rtnetlink.h)
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_VIA&nbsp;<wbr>&nbsp;</code></td>
<td>struct rtvia&nbsp;<wbr>&nbsp;</td>
<td> Gateway in different AF (see below)
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_NEWDST&nbsp;<wbr>&nbsp;</code></td>
<td>protocol address&nbsp;<wbr>&nbsp;</td>
<td> Change packet destination address
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_PREF&nbsp;<wbr>&nbsp;</code></td>
<td>char&nbsp;<wbr>&nbsp;</td>
<td> RFC4191 IPv6 router preference (see below)
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_ENCAP_TYPE&nbsp;<wbr>&nbsp;</code></td>
<td>short&nbsp;<wbr>&nbsp;</td>
<td> Encapsulation type for<br />
 lwtunnels (see below)
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_ENCAP&nbsp;<wbr>&nbsp;</code></td>
<td>&nbsp;<wbr>&nbsp;</td>
<td>Defined by RTA_ENCAP_TYPE
</td>
</tr>
<tr VALIGN=top>
<td><code>RTA_EXPIRES&nbsp;<wbr>&nbsp;</code></td>
<td>int&nbsp;<wbr>&nbsp;</td>
<td> Expire time for IPv6 routes (in seconds)
</td>
</tr>
</table>
<dd><code>RTA_MULTIPATH</code> contains several packed instances of <i>struct rtnexthop</i> together with nested RTAs (<code>RTA_GATEWAY</code>):</p>
<dd>struct rtnexthop {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short rtnh_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Length of struct&nbsp;+&nbsp;length<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of RTAs&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;rtnh_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;(see<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linux/rtnetlink.h)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;rtnh_hops;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Nexthop priority&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rtnh_ifindex;&nbsp;/*&nbsp;Interface index for this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nexthop&nbsp;*/ }</p>
<dd>There exist a bunch of <code>RTNH_*</code> macros similar to <code>RTA_*</code> and <code>NLHDR_*</code> macros useful to handle these structures.</p>
<dd>struct rtvia {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short rtvia_family;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;rtvia_addr[0]; };</p>
<dd><i>rtvia_addr</i> is the address, <i>rtvia_family</i> is its family type.</p>
<dd><code>RTA_PREF</code> may contain values <code>ICMPV6_ROUTER_PREF_LOW</code>, <code>ICMPV6_ROUTER_PREF_MEDIUM</code>, and <code>ICMPV6_ROUTER_PREF_HIGH</code> defined incw <i>&lt;linux/icmpv6.h&gt;</i>.</p>
<dd><code>RTA_ENCAP_TYPE</code> may contain values <code>LWTUNNEL_ENCAP_MPLS</code>, <code>LWTUNNEL_ENCAP_IP</code>, <code>LWTUNNEL_ENCAP_ILA</code>, or <code>LWTUNNEL_ENCAP_IP6</code> defined in <i>&lt;linux/lwtunnel.h&gt;</i>.</p>
<dd><code>Fill these values in!</code></p>
<dt><code>RTM_NEWNEIGH</code>, <code>RTM_DELNEIGH</code>, <code>RTM_GETNEIGH</code></p>
<dd>Add, remove, or receive information about a neighbor table entry (e.g., an ARP entry). The message contains an <i>ndmsg</i> structure.</p>
<dd>struct ndmsg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char ndm_family;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_ifindex;&nbsp;<wbr>&nbsp;/*&nbsp;Interface index&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_state;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;State&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_type; }; struct nda_cacheinfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_confirmed;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_used;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_updated;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ndm_refcnt; };</p>
<dd><i>ndm_state</i> is a bit mask of the following states: </p>
<table>
<tr VALIGN=top>
<td><code>NUD_INCOMPLETE</code></td>
<td>a currently resolving cache entry
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_REACHABLE</code></td>
<td>a confirmed working cache entry
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_STALE</code></td>
<td>an expired cache entry
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_DELAY</code></td>
<td>an entry waiting for a timer
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_PROBE</code></td>
<td>a cache entry that is currently reprobed
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_FAILED</code></td>
<td>an invalid cache entry
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_NOARP</code></td>
<td>a device with no destination cache
</td>
</tr>
<tr VALIGN=top>
<td><code>NUD_PERMANENT</code></td>
<td>a static entry
</td>
</tr>
</table>
<p> Valid <i>ndm_flags</i> are: </p>
<table>
<tr VALIGN=top>
<td><code>NTF_PROXY</code></td>
<td>a proxy arp entry
</td>
</tr>
<tr VALIGN=top>
<td><code>NTF_ROUTER</code></td>
<td>an IPv6 router
</td>
</tr>
</table>
<p> The <i>rtattr</i> struct has the following meanings for the <i>rta_type</i> field: </p>
<table>
<tr VALIGN=top>
<td><code>NDA_UNSPEC</code></td>
<td>unknown type
</td>
</tr>
<tr VALIGN=top>
<td><code>NDA_DST</code></td>
<td>a neighbor cache n/w layer destination address
</td>
</tr>
<tr VALIGN=top>
<td><code>NDA_LLADDR</code></td>
<td>a neighbor cache link layer address
</td>
</tr>
<tr VALIGN=top>
<td><code>NDA_CACHEINFO</code></td>
<td>cache statistics
</td>
</tr>
</table>
<p> If the <i>rta_type</i> field is <code>NDA_CACHEINFO</code>, then a <i>struct nda_cacheinfo</i> header follows.</p>
<dt><code>RTM_NEWRULE</code>, <code>RTM_DELRULE</code>, <code>RTM_GETRULE</code></p>
<dd>Add, delete, or retrieve a routing rule. Carries a <i>struct rtmsg</i></p>
<dt><code>RTM_NEWQDISC</code>, <code>RTM_DELQDISC</code>, <code>RTM_GETQDISC</code></p>
<dd>Add, remove, or get a queueing discipline. The message contains a <i>struct tcmsg</i> and may be followed by a series of attributes.</p>
<dd>struct tcmsg {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcm_family;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcm_ifindex;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;interface index&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcm_handle;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Qdisc handle&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcm_parent;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent qdisc&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcm_info; }; </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Attributes
</td>
</tr>
<tr VALIGN=top>
<td><code>rta_type&nbsp;<wbr>&nbsp;</code></td>
<td>Value type&nbsp;<wbr>&nbsp;</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_UNSPEC&nbsp;<wbr>&nbsp;</code></td>
<td>&#8211;&nbsp;<wbr>&nbsp;</td>
<td>unspecified
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_KIND&nbsp;<wbr>&nbsp;</code></td>
<td>asciiz string&nbsp;<wbr>&nbsp;</td>
<td>Name of queueing discipline
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_OPTIONS&nbsp;<wbr>&nbsp;</code></td>
<td>byte sequence&nbsp;<wbr>&nbsp;</td>
<td>Qdisc-specific options follow
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_STATS&nbsp;<wbr>&nbsp;</code></td>
<td>struct tc_stats&nbsp;<wbr>&nbsp;</td>
<td>Qdisc statistics
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_XSTATS&nbsp;<wbr>&nbsp;</code></td>
<td>qdisc-specific&nbsp;<wbr>&nbsp;</td>
<td>Module-specific statistics
</td>
</tr>
<tr VALIGN=top>
<td><code>TCA_RATE&nbsp;<wbr>&nbsp;</code></td>
<td>struct tc_estimator&nbsp;<wbr>&nbsp;</td>
<td>Rate limit
</td>
</tr>
</table>
<p> In addition, various other qdisc-module-specific attributes are allowed. For more information see the appropriate include files.</p>
<dt><code>RTM_NEWTCLASS</code>, <code>RTM_DELTCLASS</code>, <code>RTM_GETTCLASS</code></p>
<dd>Add, remove, or get a traffic class. These messages contain a <i>struct tcmsg</i> as described above.</p>
<dt><code>RTM_NEWTFILTER</code>, <code>RTM_DELTFILTER</code>, <code>RTM_GETTFILTER</code></p>
<dd>Add, remove, or receive information about a traffic filter. These messages contain a <i>struct tcmsg</i> as described above.</dl>
<h2>Versions</h2>
<p><code>rtnetlink</code> is a new feature of Linux 2.2.</p>
<h2>Bugs</h2>
<p>This manual page is incomplete.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3), <code><a href="/docs/linux/man/3-rtnetlink/">rtnetlink</a></code>(3), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
