---
title: "raw(7)"
name: "raw"
section: "7"
letter: "r"
url: "/docs/linux/man/7-raw/"
description: "raw – Linux IPv4 raw sockets"
---

<p>raw &#8211; Linux IPv4 raw sockets</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;

#include &lt;netinet/in.h&gt;

raw_socket = socket(AF_INET, SOCK_RAW, int protocol);</code></pre>
<h2>Description</h2>
<p>Raw sockets allow new IPv4 protocols to be implemented in user space. A raw socket receives or sends the raw datagram not including link level headers. </p>
<p> The IPv4 layer generates an IP header when sending a packet unless the <code>IP_HDRINCL</code> socket option is enabled on the socket. When it is enabled, the packet must contain an IP header. For receiving, the IP header is always included in the packet. </p>
<p> In order to create a raw socket, a process must have the <code>CAP_NET_RAW</code> capability in the user namespace that governs its network namespace. </p>
<p> All packets or errors matching the <i>protocol</i> number specified for the raw socket are passed to this socket. For a list of the allowed protocols, see the IANA list of assigned protocol numbers at and <code><a href="/docs/linux/man/3-getprotobyname/">getprotobyname</a></code>(3). </p>
<p> A protocol of <code>IPPROTO_RAW</code> implies enabled <code>IP_HDRINCL</code> and is able to send any IP protocol that is specified in the passed header. Receiving of all IP protocols via <code>IPPROTO_RAW</code> is not possible using raw sockets.</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>IP Header fields modified on sending by <code>IP_HDRINCL</code>
</td>
</tr>
<tr VALIGN=top>
<td>IP Checksum</td>
<td>Always filled in
</td>
</tr>
<tr VALIGN=top>
<td>Source Address</td>
<td>Filled in when zero
</td>
</tr>
<tr VALIGN=top>
<td>Packet ID</td>
<td>Filled in when zero
</td>
</tr>
<tr VALIGN=top>
<td>Total Length</td>
<td>Always filled in
</td>
</tr>
</table>
</dl>
<p> If <code>IP_HDRINCL</code> is specified and the IP header has a nonzero destination address, then the destination address of the socket is used to route the packet. When <code>MSG_DONTROUTE</code> is specified, the destination address should refer to a local interface, otherwise a routing table lookup is done anyway but gatewayed routes are ignored. </p>
<p> If <code>IP_HDRINCL</code> isn&#8217;t set, then IP header options can be set on raw sockets with <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2); see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) for more information. </p>
<p> Starting with Linux 2.2, all IP header fields and options can be set using IP socket options. This means raw sockets are usually needed only for new protocols or protocols with no user interface (like ICMP). </p>
<p> When a packet is received, it is passed to any raw sockets which have been bound to its protocol before it is passed to other protocol handlers (e.g., kernel protocol modules).</p>
<h3>Address format</h3>
<p>For sending and receiving datagrams (<code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), and similar), raw sockets use the standard <i>sockaddr_in</i> address structure defined in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). The <i>sin_port</i> field could be used to specify the IP protocol number, but it is ignored for sending in Linux 2.2 and later, and should be always set to 0 (see BUGS). For incoming packets, <i>sin_port</i> is set to zero.</p>
<h3>Socket options</h3>
<p>Raw socket options can be set with <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and read with <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) by passing the <code>IPPROTO_RAW</code> family flag.</p>
<dl>
<dt><code>ICMP_FILTER</code></p>
<dd>Enable a special filter for raw sockets bound to the <code>IPPROTO_ICMP</code> protocol. The value has a bit set for each ICMP message type which should be filtered out. The default is to filter no ICMP messages.</dl>
<p> In addition, all <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) <code>IPPROTO_IP</code> socket options valid for datagram sockets are supported.</p>
<h3>Error handling</h3>
<p>Errors originating from the network are passed to the user only when the socket is connected or the <code>IP_RECVERR</code> flag is enabled. For connected sockets, only <code>EMSGSIZE</code> and <code>EPROTO</code> are passed for compatibility. With <code>IP_RECVERR</code>, all network errors are saved in the error queue.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>User tried to send to a broadcast address without having the broadcast flag set on the socket.</p>
<dt><code>EFAULT</code></p>
<dd>An invalid memory address was supplied.</p>
<dt><code>EINVAL</code></p>
<dd>Invalid argument.</p>
<dt><code>EMSGSIZE</code></p>
<dd>Packet too big. Either Path MTU Discovery is enabled (the <code>IP_MTU_DISCOVER</code> socket flag) or the packet size exceeds the maximum allowed IPv4 packet size of 64 kB.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd>Invalid flag has been passed to a socket call (like <code>MSG_OOB</code>).</p>
<dt><code>EPERM</code></p>
<dd>The user doesn&#8217;t have permission to open raw sockets. Only processes with an effective user ID of 0 or the <code>CAP_NET_RAW</code> attribute may do that.</p>
<dt><code>EPROTO</code></p>
<dd>An ICMP error has arrived reporting a parameter problem.</dl>
<h2>Versions</h2>
<p><code>IP_RECVERR</code> and <code>ICMP_FILTER</code> are new in Linux 2.2. They are Linux extensions and should not be used in portable programs. </p>
<p> Linux 2.0 enabled some bug-to-bug compatibility with BSD in the raw socket code when the <code>SO_BSDCOMPAT</code> socket option was set; since Linux 2.2, this option no longer has that effect.</p>
<h2>Notes</h2>
<p>By default, raw sockets do path MTU (Maximum Transmission Unit) discovery. This means the kernel will keep track of the MTU to a specific target IP address and return <code>EMSGSIZE</code> when a raw packet write exceeds it. When this happens, the application should decrease the packet size. Path MTU discovery can be also turned off using the <code>IP_MTU_DISCOVER</code> socket option or the <i>/proc/sys/net/ipv4/ip_no_pmtu_disc</i> file, see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) for details. When turned off, raw sockets will fragment outgoing packets that exceed the interface MTU. However, disabling it is not recommended for performance and reliability reasons. </p>
<p> A raw socket can be bound to a specific local address using the <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) call. If it isn&#8217;t bound, all packets with the specified IP protocol are received. In addition, a raw socket can be bound to a specific network device using <code>SO_BINDTODEVICE</code>; see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). </p>
<p> An <code>IPPROTO_RAW</code> socket is send only. If you really want to receive all IP packets, use a <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7) socket with the <code>ETH_P_IP</code> protocol. Note that packet sockets don&#8217;t reassemble IP fragments, unlike raw sockets. </p>
<p> If you want to receive all ICMP packets for a datagram socket, it is often better to use <code>IP_RECVERR</code> on that particular socket; see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). </p>
<p> Raw sockets may tap all IP protocols in Linux, even protocols like ICMP or TCP which have a protocol module in the kernel. In this case, the packets are passed to both the kernel module and the raw socket(s). This should not be relied upon in portable programs, many other BSD socket implementation have limitations here. </p>
<p> Linux never changes headers passed from the user (except for filling in some zeroed fields as described for <code>IP_HDRINCL</code>). This differs from many other implementations of raw sockets. </p>
<p> Raw sockets are generally rather unportable and should be avoided in programs intended to be portable. </p>
<p> Sending on raw sockets should take the IP protocol from <i>sin_port</i>; this ability was lost in Linux 2.2. The workaround is to use <code>IP_HDRINCL</code>.</p>
<h2>Bugs</h2>
<p>Transparent proxy extensions are not described. </p>
<p> When the <code>IP_HDRINCL</code> option is set, datagrams will not be fragmented and are limited to the interface MTU. </p>
<p> Setting the IP protocol for sending in <i>sin_port</i> got lost in Linux 2.2. The protocol that the socket was bound to or that was specified in the initial <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) call is always used.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) </p>
<p> <code>RFC 1191</code> for path MTU discovery. <code>RFC 791</code> and the <i>&lt;linux/ip.h&gt;</i> header file for the IP protocol.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
