---
title: "netdevice(7)"
name: "netdevice"
section: "7"
letter: "n"
url: "/docs/linux/man/7-netdevice/"
description: "netdevice – low-level access to Linux network devices"
---

<p>netdevice &#8211; low-level access to Linux network devices</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/ioctl.h&gt;


#include &lt;net/if.h&gt;</code></pre>
<h2>Description</h2>
<p>This man page describes the sockets interface which is used to configure network devices. Linux supports some standard ioctls to configure network devices. They can be used on any socket&#8217;s file descriptor regardless of the family or type. Most of them pass an <i>ifreq</i> structure: struct ifreq {<br />
    char ifr_name[IFNAMSIZ]; /* Interface name */<br />
    union {<br />
        struct sockaddr ifr_addr;<br />
        struct sockaddr ifr_dstaddr;<br />
        struct sockaddr ifr_broadaddr;<br />
        struct sockaddr ifr_netmask;<br />
        struct sockaddr ifr_hwaddr;<br />
        short ifr_flags;<br />
        int ifr_ifindex;<br />
        int ifr_metric;<br />
        int ifr_mtu;<br />
        struct ifmap ifr_map;<br />
        char ifr_slave[IFNAMSIZ];<br />
        char ifr_newname[IFNAMSIZ];<br />
        char *ifr_data;<br />
    };<br />
}; Normally, the user specifies which device to affect by setting <i>ifr_name</i> to the name of the interface. All other members of the structure may share memory.</p>
<h3>Ioctls</h3>
<p>If an ioctl is marked as privileged, then using it requires an effective user ID of 0 or the <code>CAP_NET_ADMIN</code> capability. If this is not the case, <code>EPERM</code> will be returned.</p>
<dl>
<dt><code>SIOCGIFNAME</code></p>
<dd>Given the <i>ifr_ifindex</i>, return the name of the interface in <i>ifr_name</i>. This is the only ioctl which returns its result in <i>ifr_name</i>.</p>
<dt><code>SIOCGIFINDEX</code></p>
<dd>Retrieve the interface index of the interface into <i>ifr_ifindex</i>.</p>
<dt><code>SIOCGIFFLAGS</code>, <code>SIOCSIFFLAGS</code></p>
<dd>Get or set the active flag word of the device. <i>ifr_flags</i> contains a bit mask of the following values: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Device flags
</td>
</tr>
<tr VALIGN=top>
<td>IFF_UP</td>
<td>Interface is running.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_BROADCAST</td>
<td>Valid broadcast address set.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_DEBUG</td>
<td>Internal debugging flag.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_LOOPBACK</td>
<td>Interface is a loopback interface.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_POINTOPOINT</td>
<td>Interface is a point-to-point link.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_RUNNING</td>
<td>Resources allocated.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_NOARP</td>
<td> No arp protocol, L2 destination address not set.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_PROMISC</td>
<td>Interface is in promiscuous mode.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_NOTRAILERS</td>
<td>Avoid use of trailers.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_ALLMULTI</td>
<td>Receive all multicast packets.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_MASTER</td>
<td>Master of a load balancing bundle.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_SLAVE</td>
<td>Slave of a load balancing bundle.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_MULTICAST</td>
<td>Supports multicast
</td>
</tr>
<tr VALIGN=top>
<td>IFF_PORTSEL</td>
<td>Is able to select media type via ifmap.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_AUTOMEDIA</td>
<td>Auto media selection active.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_DYNAMIC</td>
<td> The addresses are lost when the interface goes down.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_LOWER_UP</td>
<td>Driver signals L1 up (since Linux 2.6.17)
</td>
</tr>
<tr VALIGN=top>
<td>IFF_DORMANT</td>
<td>Driver signals dormant (since Linux 2.6.17)
</td>
</tr>
<tr VALIGN=top>
<td>IFF_ECHO</td>
<td>Echo sent packets (since Linux 2.6.25)
</td>
</tr>
</table>
</dl>
<p> Setting the active flag word is a privileged operation, but any process may read it.</p>
<dl>
<dt><code>SIOCGIFPFLAGS</code>, <code>SIOCSIFPFLAGS</code></p>
<dd>Get or set extended (private) flags for the device. <i>ifr_flags</i> contains a bit mask of the following values: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Private flags
</td>
</tr>
<tr VALIGN=top>
<td>IFF_802_1Q_VLAN</td>
<td>Interface is 802.1Q VLAN device.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_EBRIDGE</td>
<td>Interface is Ethernet bridging device.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_SLAVE_INACTIVE</td>
<td>Interface is inactive bonding slave.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_MASTER_8023AD</td>
<td>Interface is 802.3ad bonding master.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_MASTER_ALB</td>
<td>Interface is balanced-alb bonding master.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_BONDING</td>
<td>Interface is a bonding master or slave.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_SLAVE_NEEDARP</td>
<td>Interface needs ARPs for validation.
</td>
</tr>
<tr VALIGN=top>
<td>IFF_ISATAP</td>
<td>Interface is RFC4214 ISATAP interface.
</td>
</tr>
</table>
</dl>
<p> Setting the extended (private) interface flags is a privileged operation.</p>
<dl>
<dt><code>SIOCGIFADDR</code>, <code>SIOCSIFADDR</code></p>
<dd>Get or set the address of the device using <i>ifr_addr</i>. Setting the interface address is a privileged operation. For compatibility, only <code>AF_INET</code> addresses are accepted or returned.</p>
<dt><code>SIOCGIFDSTADDR</code>, <code>SIOCSIFDSTADDR</code></p>
<dd>Get or set the destination address of a point-to-point device using <i>ifr_dstaddr</i>. For compatibility, only <code>AF_INET</code> addresses are accepted or returned. Setting the destination address is a privileged operation.</p>
<dt><code>SIOCGIFBRDADDR</code>, <code>SIOCSIFBRDADDR</code></p>
<dd>Get or set the broadcast address for a device using <i>ifr_brdaddr</i>. For compatibility, only <code>AF_INET</code> addresses are accepted or returned. Setting the broadcast address is a privileged operation.</p>
<dt><code>SIOCGIFNETMASK</code>, <code>SIOCSIFNETMASK</code></p>
<dd>Get or set the network mask for a device using <i>ifr_netmask</i>. For compatibility, only <code>AF_INET</code> addresses are accepted or returned. Setting the network mask is a privileged operation.</p>
<dt><code>SIOCGIFMETRIC</code>, <code>SIOCSIFMETRIC</code></p>
<dd>Get or set the metric of the device using <i>ifr_metric</i>. This is currently not implemented; it sets <i>ifr_metric</i> to 0 if you attempt to read it and returns <code>EOPNOTSUPP</code> if you attempt to set it.</p>
<dt><code>SIOCGIFMTU</code>, <code>SIOCSIFMTU</code></p>
<dd>Get or set the MTU (Maximum Transfer Unit) of a device using <i>ifr_mtu</i>. Setting the MTU is a privileged operation. Setting the MTU to too small values may cause kernel crashes.</p>
<dt><code>SIOCGIFHWADDR</code>, <code>SIOCSIFHWADDR</code></p>
<dd>Get or set the hardware address of a device using <i>ifr_hwaddr</i>. The hardware address is specified in a struct <i>sockaddr</i>. <i>sa_family</i> contains the ARPHRD_* device type, <i>sa_data</i> the L2 hardware address starting from byte 0. Setting the hardware address is a privileged operation.</p>
<dt><code>SIOCSIFHWBROADCAST</code></p>
<dd>Set the hardware broadcast address of a device from <i>ifr_hwaddr</i>. This is a privileged operation.</p>
<dt><code>SIOCGIFMAP</code>, <code>SIOCSIFMAP</code></p>
<dd>Get or set the interface&#8217;s hardware parameters using <i>ifr_map</i>. Setting the parameters is a privileged operation.</p>
<dd>struct ifmap {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;mem_start;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;mem_end;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;base_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;<wbr>&nbsp;irq;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;<wbr>&nbsp;dma;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;<wbr>&nbsp;port; };</p>
<dd>The interpretation of the ifmap structure depends on the device driver and the architecture.</p>
<dt><code>SIOCADDMULTI</code>, <code>SIOCDELMULTI</code></p>
<dd>Add an address to or delete an address from the device&#8217;s link layer multicast filters using <i>ifr_hwaddr</i>. These are privileged operations. See also <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7) for an alternative.</p>
<dt><code>SIOCGIFTXQLEN</code>, <code>SIOCSIFTXQLEN</code></p>
<dd>Get or set the transmit queue length of a device using <i>ifr_qlen</i>. Setting the transmit queue length is a privileged operation.</p>
<dt><code>SIOCSIFNAME</code></p>
<dd>Changes the name of the interface specified in <i>ifr_name</i> to <i>ifr_newname</i>. This is a privileged operation. It is allowed only when the interface is not up.</p>
<dt><code>SIOCGIFCONF</code></p>
<dd>Return a list of interface (network layer) addresses. This currently means only addresses of the <code>AF_INET</code> (IPv4) family for compatibility. Unlike the others, this ioctl passes an <i>ifconf</i> structure:</p>
<dd>struct ifconf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ifc_len;&nbsp;/*&nbsp;size of buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ifc_buf;&nbsp;/*&nbsp;buffer address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ifreq&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ifc_req;&nbsp;/*&nbsp;array of structures&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; };</p>
<dd>If <i>ifc_req</i> is NULL, <code>SIOCGIFCONF</code> returns the necessary buffer size in bytes for receiving all available addresses in <i>ifc_len</i>. Otherwise, <i>ifc_req</i> contains a pointer to an array of <i>ifreq</i> structures to be filled with all currently active L3 interface addresses. <i>ifc_len</i> contains the size of the array in bytes. Within each <i>ifreq</i> structure, <i>ifr_name</i> will receive the interface name, and <i>ifr_addr</i> the address. The actual number of bytes transferred is returned in <i>ifc_len</i>.</p>
<dd>If the size specified by <i>ifc_len</i> is insufficient to store all the addresses, the kernel will skip the exceeding ones and return success. There is no reliable way of detecting this condition once it has occurred. It is therefore recommended to either determine the necessary buffer size beforehand by calling <code>SIOCGIFCONF</code> with <i>ifc_req</i> set to NULL, or to retry the call with a bigger buffer whenever <i>ifc_len</i> upon return differs by less than <i>sizeof(struct ifreq)</i> from its original value.</p>
<dd>If an error occurs accessing the <i>ifconf</i> or <i>ifreq</i> structures, <code>EFAULT</code> will be returned.</dl>
<p> Most protocols support their own ioctls to configure protocol-specific interface options. See the protocol man pages for a description. For configuring IP addresses, see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). In addition, some devices support private ioctls. These are not described here.</p>
<h2>Notes</h2>
<p><code>SIOCGIFCONF</code> and the other ioctls that accept or return only <code>AF_INET</code> socket addresses are IP-specific and perhaps should rather be documented in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). </p>
<p> The names of interfaces with no addresses or that don&#8217;t have the <code>IFF_RUNNING</code> flag set can be found via <i>/proc/net/dev</i>. </p>
<p> Local IPv6 IP addresses can be found via <i>/proc/net</i> or via <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7).</p>
<h2>Bugs</h2>
<p>glibc 2.1 is missing the <i>ifr_newname</i> macro in <i>&lt;net/if.h&gt;</i>. Add the following to your program as a workaround: </p>
<pre><code>#ifndef ifr_newname
#define ifr_newname     ifr_ifru.ifru_slave
#endif</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
