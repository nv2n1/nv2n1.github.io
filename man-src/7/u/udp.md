---
title: "udp(7)"
name: "udp"
section: "7"
letter: "u"
url: "/docs/linux/man/7-udp/"
description: "udp – User Datagram Protocol for IPv4"
---

<p>udp &#8211; User Datagram Protocol for IPv4</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;


#include &lt;netinet/in.h&gt;


#include &lt;netinet/udp.h&gt;
udp_socket = socket(AF_INET, SOCK_DGRAM, 0);</code></pre>
<h2>Description</h2>
<p>This is an implementation of the User Datagram Protocol described in RFC 768. It implements a connectionless, unreliable datagram packet service. Packets may be reordered or duplicated before they arrive. UDP generates and checks checksums to catch transmission errors. When a UDP socket is created, its local and remote addresses are unspecified. Datagrams can be sent immediately using <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) with a valid destination address as an argument. When <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) is called on the socket, the default destination address is set and datagrams can now be sent using <code><a href="/docs/linux/man/2-send/">send</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) without specifying a destination address. It is still possible to send to other destinations by passing an address to <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). In order to receive packets, the socket can be bound to a local address first by using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). Otherwise, the socket layer will automatically assign a free local port out of the range defined by <i>/proc/sys/net/ipv4/ip_local_port_range</i> and bind the socket to <code>INADDR_ANY</code>. All receive operations return only one packet. When the packet is smaller than the passed buffer, only that much data is returned; when it is bigger, the packet is truncated and the <code>MSG_TRUNC</code> flag is set. <code>MSG_WAITALL</code> is not supported. IP options may be sent or received using the socket options described in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). They are processed by the kernel only when the appropriate <i>/proc</i> parameter is enabled (but still passed to the user even when it is turned off). See <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). When the <code>MSG_DONTROUTE</code> flag is set on sending, the destination address must refer to a local interface address and the packet is sent only to that interface. By default, Linux UDP does path MTU (Maximum Transmission Unit) discovery. This means the kernel will keep track of the MTU to a specific target IP address and return <code>EMSGSIZE</code> when a UDP packet write exceeds it. When this happens, the application should decrease the packet size. Path MTU discovery can be also turned off using the <code>IP_MTU_DISCOVER</code> socket option or the <i>/proc/sys/net/ipv4/ip_no_pmtu_disc</i> file; see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) for details. When turned off, UDP will fragment outgoing UDP packets that exceed the interface MTU. However, disabling it is not recommended for performance and reliability reasons.</p>
<h3>Address format</h3>
<p>UDP uses the IPv4 <i>sockaddr_in</i> address format described in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<h3>Error handling</h3>
<p>All fatal errors will be passed to the user as an error return even when the socket is not connected. This includes asynchronous errors received from the network. You may get an error for an earlier packet that was sent on the same socket. This behavior differs from many other BSD socket implementations which don&#8217;t pass any errors unless the socket is connected. Linux&#8217;s behavior is mandated by <code>RFC 1122</code>. For compatibility with legacy code, in Linux 2.0 and 2.2 it was possible to set the <code>SO_BSDCOMPAT</code> <code>SOL_SOCKET</code> option to receive remote errors only when the socket has been connected (except for <code>EPROTO</code> and <code>EMSGSIZE</code>). Locally generated errors are always passed. Support for this socket option was removed in later kernels; see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for further information. When the <code>IP_RECVERR</code> option is enabled, all errors are stored in the socket error queue, and can be received by <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) with the <code>MSG_ERRQUEUE</code> flag set.</p>
<h3>/proc interfaces</h3>
<p>System-wide UDP parameter settings can be accessed by files in the directory <i>/proc/sys/net/ipv4/</i>.</p>
<dl>
<dt><i>udp_mem</i> (since Linux 2.6.25)</p>
<dd>This is a vector of three integers governing the number of pages allowed for queueing by all UDP sockets.</p>
<dl>
<dd>
<dl>
<dt><i>min</i></p>
<dd>Below this number of pages, UDP is not bothered about its memory appetite. When the amount of memory allocated by UDP exceeds this number, UDP starts to moderate memory usage.</p>
<dt><i>pressure</i></p>
<dd>This value was introduced to follow the format of <i>tcp_mem</i> (see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)).</p>
<dt><i>max</i></p>
<dd>Number of pages allowed for queueing by all UDP sockets.</dl>
</dl>
<dd>Defaults values for these three items are calculated at boot time from the amount of available memory.</p>
<dt><i>udp_rmem_min</i> (integer; default value: PAGE_SIZE; since Linux 2.6.25)</p>
<dd>Minimal size, in bytes, of receive buffers used by UDP sockets in moderation. Each UDP socket is able to use the size for receiving data, even if total pages of UDP sockets exceed <i>udp_mem</i> pressure.</p>
<dt><i>udp_wmem_min</i> (integer; default value: PAGE_SIZE; since Linux 2.6.25)</p>
<dd>Minimal size, in bytes, of send buffer used by UDP sockets in moderation. Each UDP socket is able to use the size for sending data, even if total pages of UDP sockets exceed <i>udp_mem</i> pressure.</dl>
<h3>Socket options</h3>
<p>To set or get a UDP socket option, call <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to write the option with the option level argument set to <code>IPPROTO_UDP</code>. Unless otherwise noted, <i>optval</i> is a pointer to an <i>int</i>. Following is a list of UDP-specific socket options. For details of some other socket options that are also applicable for UDP sockets, see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7).</p>
<dl>
<dt><code>UDP_CORK</code> (since Linux 2.5.44)</p>
<dd>If this option is enabled, then all data output on this socket is accumulated into a single datagram that is transmitted when the option is disabled. This option should not be used in code intended to be portable.</dl>
<h3>Ioctls</h3>
<p>These ioctls can be accessed using <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2). The correct syntax is: </p>
<pre><code>int value;
error = ioctl(udp_socket, ioctl_type, &amp;value);

FIONREAD(SIOCINQ)

Gets a pointer to an integer as argument.Returns the size of the next pending datagram in the integer in bytes,
    or 0 when no datagram is pending.Warning :

    Using
        FIONREAD,

    it is impossible to distinguish the case where no datagram is pending
        from the case where the next pending datagram contains zero bytes of data.It is safer to use
            select(2),

    poll(2),

    or
        epoll(7)

                to distinguish these cases.

            TIOCOUTQ(SIOCOUTQ)

                Returns the number of data bytes in the local send queue.Supported only with Linux 2.4 and
            above.</code></pre>
<p> In addition, all ioctls documented in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) and <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) are supported.</p>
<h2>Errors</h2>
<p>All errors documented for <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) or <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) may be returned by a send or receive on a UDP socket.</p>
<dl>
<dt><code>ECONNREFUSED</code></p>
<dd>No receiver was associated with the destination address. This might be caused by a previous packet sent over the socket.</dl>
<h2>Versions</h2>
<p><code>IP_RECVERR</code> is a new feature in Linux 2.2.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-udplite/">udplite</a></code>(7) </p>
<p> The kernel source file <i>Documentation/networking/ip-sysctl.txt</i>. </p>
<p> RFC 768 for the User Datagram Protocol.<br />
 RFC 1122 for the host requirements.<br />
 RFC 1191 for a description of path MTU discovery.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
