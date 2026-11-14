---
title: "socket(2)"
name: "socket"
section: "2"
letter: "s"
url: "/docs/linux/man/2-socket/"
description: "socket – create an endpoint for communication"
---

<h2 class="name">NAME</h2>
<p> socket &#8211; create an endpoint for communication </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code> /* See NOTES */<br />
 <code>#include &lt;sys/socket.h&gt;</code> </p>
<p> <code>int socket(int </code><i>domain</i><code>, int </code><i>type</i><code>, int </code><i>protocol</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>socket</code>() creates an endpoint for communication and returns a file descriptor that refers to that endpoint. The file descriptor returned by a successful call will be the lowest-numbered file descriptor not currently open for the process. </p>
<p> The <i>domain</i> argument specifies a communication domain; this selects the protocol family which will be used for communication. These families are defined in <i>&lt;sys/socket.h&gt;</i>. The formats currently understood by the Linux kernel include: </p>
<table>
<tr VALIGN=top>
<td>Name&nbsp;</td>
<td>Purpose</td>
<td>Man page
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_UNIX</code> &nbsp;</td>
<td> Local communication </td>
<td> <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_LOCAL</code> &nbsp;</td>
<td> Synonym for <code>AF_UNIX</code> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_INET</code> &nbsp;</td>
<td>IPv4 Internet protocols</td>
<td> <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_AX25</code> &nbsp;</td>
<td> Amateur radio AX.25 protocol </td>
<td> <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_IPX</code> &nbsp;</td>
<td>IPX &#8211; Novell protocols</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_APPLETALK</code> &nbsp;</td>
<td>AppleTalk</td>
<td> <code><a href="/docs/linux/man/7-ddp/">ddp</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_X25</code> &nbsp;</td>
<td>ITU-T X.25 / ISO-8208 protocol</td>
<td> <code><a href="/docs/linux/man/7-x25/">x25</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_INET6</code> &nbsp;</td>
<td>IPv6 Internet protocols</td>
<td> <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_DECnet</code> &nbsp;</td>
<td> DECet protocol sockets </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_KEY</code> &nbsp;</td>
<td> Key management protocol, originally developed for usage with IPsec </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_NETLINK</code> &nbsp;</td>
<td> Kernel user interface device </td>
<td> <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_PACKET</code> &nbsp;</td>
<td> Low-level packet interface </td>
<td> <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_RDS</code> &nbsp;</td>
<td> Reliable Datagram Sockets (RDS) protocol </td>
<td> <code><a href="/docs/linux/man/7-rds/">rds</a></code>(7)<br />
 <code><a href="/docs/linux/man/7-rds-rdma/">rds-rdma</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_PPPOX</code> &nbsp;</td>
<td> Generic PPP transport layer, for setting up L2 tunnels (L2TP and PPPoE) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_LLC</code> &nbsp;</td>
<td> Logical link control (IEEE 802.2 LLC) protocol </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_IB</code> &nbsp;</td>
<td> InfiniBand native addressing </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_MPLS</code> &nbsp;</td>
<td> Multiprotocol Label Switching </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_CAN</code> &nbsp;</td>
<td> Controller Area Network automotive bus protocol </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_TIPC</code> &nbsp;</td>
<td> TIPC, &quot;cluster domain sockets&quot; protocol </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_BLUETOOTH</code> &nbsp;</td>
<td> Bluetooth low-level socket protocol </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_ALG</code> &nbsp;</td>
<td> Interface to kernel crypto API </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_VSOCK</code> &nbsp;</td>
<td> VSOCK (originally &quot;VMWare VSockets&quot;) protocol for hypervisor-guest communication </td>
<td> <code><a href="/docs/linux/man/7-vsock/">vsock</a></code>(7)
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_KCM</code> &nbsp;</td>
<td> KCM (kernel connection multiplexer) interface </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> <code>AF_XDP</code> &nbsp;</td>
<td> XDP (express data path) interface </td>
<td>
</td>
</tr>
</table>
<p> Further details of the above address families, as well as information on several other address families, can be found in <code><a href="/docs/linux/man/7-address_families/">address_families</a></code>(7). </p>
<p> The socket has the indicated <i>type</i>, which specifies the communication semantics. Currently defined types are:</p>
<dl>
<dt><code>SOCK_STREAM</code></p>
<dd> Provides sequenced, reliable, two-way, connection-based byte streams. An out-of-band data transmission mechanism may be supported.</p>
<dt><code>SOCK_DGRAM</code></p>
<dd> Supports datagrams (connectionless, unreliable messages of a fixed maximum length).</p>
<dt><code>SOCK_SEQPACKET</code></p>
<dd> Provides a sequenced, reliable, two-way connection-based data transmission path for datagrams of fixed maximum length; a consumer is required to read an entire packet with each input system call.</p>
<dt><code>SOCK_RAW</code></p>
<dd> Provides raw network protocol access.</p>
<dt><code>SOCK_RDM</code></p>
<dd> Provides a reliable datagram layer that does not guarantee ordering.</p>
<dt><code>SOCK_PACKET</code></p>
<dd> Obsolete and should not be used in new programs; see <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7).</dl>
<p> Some socket types may not be implemented by all protocol families. </p>
<p> Since Linux 2.6.27, the <i>type</i> argument serves a second purpose: in addition to specifying a socket type, it may include the bitwise OR of any of the following values, to modify the behavior of <code>socket</code>():</p>
<dl>
<dt><code>SOCK_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>SOCK_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<p> The <i>protocol</i> specifies a particular protocol to be used with the socket. Normally only a single protocol exists to support a particular socket type within a given protocol family, in which case <i>protocol</i> can be specified as 0. However, it is possible that many protocols may exist, in which case a particular protocol must be specified in this manner. The protocol number to use is specific to the &#8220;communication domain&#8221; in which communication is to take place; see <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5). See <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3) on how to map protocol name strings to protocol numbers. </p>
<p> Sockets of type <code>SOCK_STREAM</code> are full-duplex byte streams. They do not preserve record boundaries. A stream socket must be in a <i>connected</i> state before any data may be sent or received on it. A connection to another socket is created with a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) call. Once connected, data may be transferred using <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2) calls or some variant of the <code><a href="/docs/linux/man/2-send/">send</a></code>(2) and <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) calls. When a session has been completed a <code><a href="/docs/linux/man/2-close/">close</a></code>(2) may be performed. Out-of-band data may also be transmitted as described in <code><a href="/docs/linux/man/2-send/">send</a></code>(2) and received as described in <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2). </p>
<p> The communications protocols which implement a <code>SOCK_STREAM</code> ensure that data is not lost or duplicated. If a piece of data for which the peer protocol has buffer space cannot be successfully transmitted within a reasonable length of time, then the connection is considered to be dead. When <code>SO_KEEPALIVE</code> is enabled on the socket the protocol checks in a protocol-specific manner if the other end is still alive. A <code>SIGPIPE</code> signal is raised if a process sends or receives on a broken stream; this causes naive processes, which do not handle the signal, to exit. <code>SOCK_SEQPACKET</code> sockets employ the same system calls as <code>SOCK_STREAM</code> sockets. The only difference is that <code><a href="/docs/linux/man/2-read/">read</a></code>(2) calls will return only the amount of data requested, and any data remaining in the arriving packet will be discarded. Also all message boundaries in incoming datagrams are preserved. </p>
<p> <code>SOCK_DGRAM</code> and <code>SOCK_RAW</code> sockets allow sending of datagrams to correspondents named in <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) calls. Datagrams are generally received with <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), which returns the next datagram along with the address of its sender. </p>
<p> <code>SOCK_PACKET</code> is an obsolete socket type to receive raw packets directly from the device driver. Use <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7) instead. </p>
<p> An <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETOWN</code> operation can be used to specify a process or process group to receive a <code>SIGURG</code> signal when the out-of-band data arrives or <code>SIGPIPE</code> signal when a <code>SOCK_STREAM</code> connection breaks unexpectedly. This operation may also be used to set the process or process group that receives the I/O and asynchronous notification of I/O events via <code>SIGIO</code>. Using <code>F_SETOWN</code> is equivalent to an <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) call with the <code>FIOSETOWN</code> or <code>SIOCSPGRP</code> argument. </p>
<p> When the network signals an error condition to the protocol module (e.g., using an ICMP message for IP) the pending error flag is set for the socket. The next operation on this socket will return the error code of the pending error. For some protocols it is possible to enable a per-socket error queue to retrieve detailed information about the error; see <code>IP_RECVERR</code> in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7). </p>
<p> The operation of sockets is controlled by socket level <i>options</i>. These options are defined in <i>&lt;sys/socket.h&gt;</i>. The functions <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) are used to set and get options.</p>
<h2>RETURN VALUE</h2>
<p> On success, a file descriptor for the new socket is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Permission to create a socket of the specified type and/or protocol is denied.</p>
<dt><code>EAFNOSUPPORT</code></p>
<dd> The implementation does not support the specified address family.</p>
<dt><code>EINVAL</code></p>
<dd> Unknown protocol, or protocol family not available.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flags in <i>type</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOBUFS</code> or <code>ENOMEM</code></p>
<dd> Insufficient memory is available. The socket cannot be created until sufficient resources are freed.</p>
<dt><code>EPROTONOSUPPORT</code></p>
<dd> The protocol type or the specified protocol is not supported within this domain.</dl>
<p> Other errors may be generated by the underlying protocol modules.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, 4.4BSD. </p>
<p> The <code>SOCK_NONBLOCK</code> and <code>SOCK_CLOEXEC</code> flags are Linux-specific. </p>
<p> <code>socket</code>() appeared in 4.2BSD. It is generally portable to/from non-BSD systems supporting clones of the BSD socket layer (including System V variants).</p>
<h2>NOTES</h2>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> The manifest constants used under 4.x BSD for protocol families are <code>PF_UNIX</code>, <code>PF_INET</code>, and so on, while <code>AF_UNIX</code>, <code>AF_INET</code>, and so on are used for address families. However, already the BSD man page promises: &quot;The protocol family generally is the same as the address family&quot;, and subsequent standards use AF_* everywhere.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>socket</code>() is shown in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/7-address_families/">address_families</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) </p>
<p> &#8220;An Introductory 4.3BSD Interprocess Communication Tutorial&#8221; and &#8220;BSD Interprocess Communication Tutorial&#8221;, reprinted in <i>UNIX Programmer&#8217;s Supplementary Documents Volume 1.</i></p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
