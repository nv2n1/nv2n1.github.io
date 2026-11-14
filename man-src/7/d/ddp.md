---
title: "ddp(7)"
name: "ddp"
section: "7"
letter: "d"
url: "/docs/linux/man/7-ddp/"
description: "ddp – Linux AppleTalk protocol implementation"
---

<p>ddp &#8211; Linux AppleTalk protocol implementation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;


#include &lt;netatalk/at.h&gt;
ddp_socket = socket(AF_APPLETALK, SOCK_DGRAM, 0);


raw_socket = socket(AF_APPLETALK, SOCK_RAW, protocol);</code></pre>
<h2>Description</h2>
<p>Linux implements the AppleTalk protocols described in <i>Inside AppleTalk</i>. Only the DDP layer and AARP are present in the kernel. They are designed to be used via the <code>netatalk</code> protocol libraries. This page documents the interface for those who wish or need to use the DDP layer directly. The communication between AppleTalk and the user program works using a BSD-compatible socket interface. For more information on sockets, see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). An AppleTalk socket is created by calling the <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) function with a <code>AF_APPLETALK</code> socket family argument. Valid socket types are <code>SOCK_DGRAM</code> to open a <code>ddp</code> socket or <code>SOCK_RAW</code> to open a <code>raw</code> socket. <i>protocol</i> is the AppleTalk protocol to be received or sent. For <code>SOCK_RAW</code> you must specify <code>ATPROTO_DDP</code>. Raw sockets may be opened only by a process with effective user ID 0 or when the process has the <code>CAP_NET_RAW</code> capability.</p>
<h3>Address format</h3>
<p>An AppleTalk socket address is defined as a combination of a network number, a node number, and a port number. </p>
<pre><code>struct at_addr {
    unsigned short s_net;
    unsigned char s_node;
};
struct sockaddr_atalk {
    sa_family_t sat_family;  /* address family */
    unsigned char sat_port;  /* port */
    struct at_addr sat_addr; /* net/node */
};</code></pre>
<p> <i>sat_family</i> is always set to <code>AF_APPLETALK</code>. <i>sat_port</i> contains the port. The port numbers below 129 are known as <i>reserved ports</i>. Only processes with the effective user ID 0 or the <code>CAP_NET_BIND_SERVICE</code> capability may <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) to these sockets. <i>sat_addr</i> is the host address. The <i>net</i> member of <i>struct at_addr</i> contains the host network in network byte order. The value of <code>AT_ANYNET</code> is a wildcard and also implies &#8220;this network.&#8221; The <i>node</i> member of <i>struct at_addr</i> contains the host node number. The value of <code>AT_ANYNODE</code> is a wildcard and also implies &#8220;this node.&#8221; The value of <code>ATADDR_BCAST</code> is a link local broadcast address.</p>
<h3>Socket options</h3>
<p>No protocol-specific socket options are supported.</p>
<h3>/proc interfaces</h3>
<p>IP supports a set of <i>/proc</i> interfaces to configure some global AppleTalk parameters. The parameters can be accessed by reading or writing files in the directory <i>/proc/sys/net/atalk/</i>.</p>
<dl>
<dt><i>aarp-expiry-time</i></p>
<dd>The time interval (in seconds) before an AARP cache entry expires.</p>
<dt><i>aarp-resolve-time</i></p>
<dd>The time interval (in seconds) before an AARP cache entry is resolved.</p>
<dt><i>aarp-retransmit-limit</i></p>
<dd>The number of retransmissions of an AARP query before the node is declared dead.</p>
<dt><i>aarp-tick-time</i></p>
<dd>The timer rate (in seconds) for the timer driving AARP.</dl>
<p> The default values match the specification and should never need to be changed.</p>
<h3>Ioctls</h3>
<p>All ioctls described in <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) apply to DDP.</p>
<h2>Errors</h2>
<dl>
<dt><code>EACCES</code></p>
<dd>The user tried to execute an operation without the necessary permissions. These include sending to a broadcast address without having the broadcast flag set, and trying to bind to a reserved port without effective user ID 0 or <code>CAP_NET_BIND_SERVICE</code>.</p>
<dt><code>EADDRINUSE</code></p>
<dd>Tried to bind to an address already in use.</p>
<dt><code>EADDRNOTAVAIL</code></p>
<dd>A nonexistent interface was requested or the requested source address was not local.</p>
<dt><code>EAGAIN</code></p>
<dd>Operation on a nonblocking socket would block.</p>
<dt><code>EALREADY</code></p>
<dd>A connection operation on a nonblocking socket is already in progress.</p>
<dt><code>ECONNABORTED</code></p>
<dd>A connection was closed during an <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2).</p>
<dt><code>EHOSTUNREACH</code></p>
<dd>No routing table entry matches the destination address.</p>
<dt><code>EINVAL</code></p>
<dd>Invalid argument passed.</p>
<dt><code>EISCONN</code></p>
<dd><code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) was called on an already connected socket.</p>
<dt><code>EMSGSIZE</code></p>
<dd>Datagram is bigger than the DDP MTU.</p>
<dt><code>ENODEV</code></p>
<dd>Network device not available or not capable of sending IP.</p>
<dt><code>ENOENT</code></p>
<dd><code>SIOCGSTAMP</code> was called on a socket where no packet arrived.</p>
<dt><code>ENOMEM</code> and <code>ENOBUFS</code></p>
<dd>Not enough memory available.</p>
<dt><code>ENOPKG</code></p>
<dd>A kernel subsystem was not configured.</p>
<dt><code>ENOPROTOOPT</code> and <code>EOPNOTSUPP</code></p>
<dd>Invalid socket option passed.</p>
<dt><code>ENOTCONN</code></p>
<dd>The operation is defined only on a connected socket, but the socket wasn&#8217;t connected.</p>
<dt><code>EPERM</code></p>
<dd>User doesn&#8217;t have permission to set high priority, make a configuration change, or send signals to the requested process or group.</p>
<dt><code>EPIPE</code></p>
<dd>The connection was unexpectedly closed or shut down by the other end.</p>
<dt><code>ESOCKTNOSUPPORT</code></p>
<dd>The socket was unconfigured, or an unknown socket type was requested.</dl>
<h2>Versions</h2>
<p>AppleTalk is supported by Linux 2.0 or higher. The <i>/proc</i> interfaces exist since Linux 2.2.</p>
<h2>Notes</h2>
<p>Be very careful with the <code>SO_BROADCAST</code> option; it is not privileged in Linux. It is easy to overload the network with careless sending to broadcast addresses.</p>
<h3>Compatibility</h3>
<p>The basic AppleTalk socket interface is compatible with <code>netatalk</code> on BSD-derived systems. Many BSD systems fail to check <code>SO_BROADCAST</code> when sending broadcast frames; this can lead to compatibility problems. </p>
<p> The raw socket mode is unique to Linux and exists to support the alternative CAP package and AppleTalk monitoring tools more easily.</p>
<h2>Bugs</h2>
<p>There are too many inconsistent error values. </p>
<p> The ioctls used to configure routing tables, devices, AARP tables, and other devices are not yet described.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
