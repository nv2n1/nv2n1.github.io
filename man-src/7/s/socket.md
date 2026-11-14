---
title: "socket(7)"
name: "socket"
section: "7"
letter: "s"
url: "/docs/linux/man/7-socket/"
description: "socket – Linux socket interface"
---

<p>socket &#8211; Linux socket interface</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;
sockfd = socket(int socket_family, int socket_type, int protocol);</code></pre>
<h2>Description</h2>
<p>This manual page describes the Linux networking socket layer user interface. The BSD compatible sockets are the uniform interface between the user process and the network protocol stacks in the kernel. The protocol modules are grouped into <i>protocol families</i> such as <code>AF_INET</code>, <code>AF_IPX</code>, and <code>AF_PACKET</code>, and <i>socket types</i> such as <code>SOCK_STREAM</code> or <code>SOCK_DGRAM</code>. See <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) for more information on families and types.</p>
<h3>Socket-layer functions</h3>
<p>These functions are used by the user process to send or receive packets and to do other socket operations. For more information see their respective manual pages. <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) creates a socket, <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) connects a socket to a remote socket address, the <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) function binds a socket to a local socket address, <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) tells the socket that new connections shall be accepted, and <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) is used to get a new socket with a new incoming connection. <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2) returns two connected anonymous sockets (implemented only for a few local families like <code>AF_UNIX</code>) <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2), and <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) send data over a socket, and <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) receive data from a socket. <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/2-select/">select</a></code>(2) wait for arriving data or a readiness to send data. In addition, the standard I/O operations like <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-writev/">writev</a></code>(2), <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), and <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2) can be used to read and write data. <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2) returns the local socket address and <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2) returns the remote socket address. <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) and <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) are used to set or get socket layer or protocol options. <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) can be used to set or read some other options. <code><a href="/docs/linux/man/2-close/">close</a></code>(2) is used to close a socket. <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) closes parts of a full-duplex socket connection. Seeking, or calling <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2) or <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2) with a nonzero position is not supported on sockets. It is possible to do nonblocking I/O on sockets by setting the <code>O_NONBLOCK</code> flag on a socket file descriptor using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). Then all operations that would block will (usually) return with <code>EAGAIN</code> (operation should be retried later); <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) will return <code>EINPROGRESS</code> error. The user can then wait for various events via <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) or <code><a href="/docs/linux/man/2-select/">select</a></code>(2). </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>I/O events
</td>
</tr>
<tr VALIGN=top>
<td>Event</td>
<td>Poll flag</td>
<td>Occurrence
</td>
</tr>
<tr VALIGN=top>
<td>Read</td>
<td>POLLIN</td>
<td> New data arrived.
</td>
</tr>
<tr VALIGN=top>
<td>Read</td>
<td>POLLIN</td>
<td> A connection setup has been completed (for connection-oriented sockets)
</td>
</tr>
<tr VALIGN=top>
<td>Read</td>
<td>POLLHUP</td>
<td> A disconnection request has been initiated by the other end.
</td>
</tr>
<tr VALIGN=top>
<td>Read</td>
<td>POLLHUP</td>
<td> A connection is broken (only for connection-oriented protocols). When the socket is written <code>SIGPIPE</code> is also sent.
</td>
</tr>
<tr VALIGN=top>
<td>Write</td>
<td>POLLOUT</td>
<td> Socket has enough send buffer space for writing new data.
</td>
</tr>
<tr VALIGN=top>
<td>Read/Write</td>
<td> POLLIN |<br />
 POLLOUT </td>
<td> An outgoing <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) finished.
</td>
</tr>
<tr VALIGN=top>
<td>Read/Write</td>
<td>POLLERR</td>
<td>An asynchronous error occurred.
</td>
</tr>
<tr VALIGN=top>
<td>Read/Write</td>
<td>POLLHUP</td>
<td>The other end has shut down one direction.
</td>
</tr>
<tr VALIGN=top>
<td>Exception</td>
<td>POLLPRI</td>
<td> Urgent data arrived. <code>SIGURG</code> is sent then.
</td>
</tr>
</table>
<p> An alternative to <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/2-select/">select</a></code>(2) is to let the kernel inform the application about events via a <code>SIGIO</code> signal. For that the <code>O_ASYNC</code> flag must be set on a socket file descriptor via <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and a valid signal handler for <code>SIGIO</code> must be installed via <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2). See the <i>Signals</i> discussion below.</p>
<h3>Socket address structures</h3>
<p>Each socket domain has its own format for socket addresses, with a domain-specific address structure. Each of these structures begins with an integer &quot;family&quot; field (typed as <i>sa_family_t</i>) that indicates the type of the address structure. This allows the various system calls (e.g., <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-getpeername/">getpeername</a></code>(2)), which are generic to all socket domains, to determine the domain of a particular socket address. To allow any type of socket address to be passed to interfaces in the sockets API, the type <i>struct sockaddr</i> is defined. The purpose of this type is purely to allow casting of domain-specific socket address types to a &quot;generic&quot; type, so as to avoid compiler warnings about type mismatches in calls to the sockets API. In addition, the sockets API provides the data type <i>struct sockaddr_storage.</i> This type is suitable to accommodate all supported domain-specific socket address structures; it is large enough and is aligned properly. (In particular, it is large enough to hold IPv6 socket addresses.) The structure includes the following field, which can be used to identify the type of socket address actually stored in the structure: </p>
<pre><code>sa_family_t ss_family;</code></pre>
<p> The <i>sockaddr_storage</i> structure is useful in programs that must handle socket addresses in a generic way (e.g., programs that must deal with both IPv4 and IPv6 socket addresses).</p>
<h3>Socket options</h3>
<p>The socket options listed below can be set by using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and read with <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) with the socket level set to <code>SOL_SOCKET</code> for all sockets. Unless otherwise noted, <i>optval</i> is a pointer to an <i>int</i>.</p>
<dl>
<dt><code>SO_ACCEPTCONN</code></p>
<dd>Returns a value indicating whether or not this socket has been marked to accept connections with <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2). The value 0 indicates that this is not a listening socket, the value 1 indicates that this is a listening socket. This socket option is read-only.</p>
<dt><code>SO_ATTACH_FILTER</code> (since Linux 2.2), <code>SO_ATTACH_BPF</code> (since Linux 3.19)</p>
<dd>Attach a classic BPF (<code>SO_ATTACH_FILTER</code>) or an extended BPF (<code>SO_ATTACH_BPF</code>) program to the socket for use as a filter of incoming packets. A packet will be dropped if the filter program returns zero. If the filter program returns a nonzero value which is less than the packet&#8217;s data length, the packet will be truncated to the length returned. If the value returned by the filter is greater than or equal to the packet&#8217;s data length, the packet is allowed to proceed unmodified.</p>
<dd>The argument for <code>SO_ATTACH_FILTER</code> is a <i>sock_fprog</i> structure, defined in <i>&lt;linux/filter.h&gt;</i>:</p>
<dd>struct sock_fprog {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sock_filter&nbsp;*filter; };</p>
<dd>The argument for <code>SO_ATTACH_BPF</code> is a file descriptor returned by the <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2) system call and must refer to a program of type <code>BPF_PROG_TYPE_SOCKET_FILTER</code>.</p>
<dd>These options may be set multiple times for a given socket, each time replacing the previous filter program. The classic and extended versions may be called on the same socket, but the previous filter will always be replaced such that a socket never has more than one filter defined.</p>
<dd>Both classic and extended BPF are explained in the kernel source file <i>Documentation/networking/filter.txt</i></p>
<dt><code>SO_ATTACH_REUSEPORT_CBPF</code>, <code>SO_ATTACH_REUSEPORT_EBPF</code></p>
<dd>For use with the <code>SO_REUSEPORT</code> option, these options allow the user to set a classic BPF (<code>SO_ATTACH_REUSEPORT_CBPF</code>) or an extended BPF (<code>SO_ATTACH_REUSEPORT_EBPF</code>) program which defines how packets are assigned to the sockets in the reuseport group (that is, all sockets which have <code>SO_REUSEPORT</code> set and are using the same local address to receive packets).</p>
<dd>The BPF program must return an index between 0 and N-1 representing the socket which should receive the packet (where N is the number of sockets in the group). If the BPF program returns an invalid index, socket selection will fall back to the plain <code>SO_REUSEPORT</code> mechanism.</p>
<dd>Sockets are numbered in the order in which they are added to the group (that is, the order of <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) calls for UDP sockets or the order of <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) calls for TCP sockets). New sockets added to a reuseport group will inherit the BPF program. When a socket is removed from a reuseport group (via <code><a href="/docs/linux/man/2-close/">close</a></code>(2)), the last socket in the group will be moved into the closed socket&#8217;s position.</p>
<dd>These options may be set repeatedly at any time on any socket in the group to replace the current BPF program used by all sockets in the group.</p>
<dd><code>SO_ATTACH_REUSEPORT_CBPF</code> takes the same argument type as <code>SO_ATTACH_FILTER</code> and <code>SO_ATTACH_REUSEPORT_EBPF</code> takes the same argument type as <code>SO_ATTACH_BPF</code>.</p>
<dd>UDP support for this feature is available since Linux 4.5; TCP support is available since Linux 4.6.</p>
<dt><code>SO_BINDTODEVICE</code></p>
<dd>Bind this socket to a particular device like &#8220;eth0&#8221;, as specified in the passed interface name. If the name is an empty string or the option length is zero, the socket device binding is removed. The passed option is a variable-length null-terminated interface name string with the maximum size of <code>IFNAMSIZ</code>. If a socket is bound to an interface, only packets received from that particular interface are processed by the socket. Note that this works only for some socket types, particularly <code>AF_INET</code> sockets. It is not supported for packet sockets (use normal <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) there).</p>
<dd>Before Linux 3.8, this socket option could be set, but could not retrieved with <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2). Since Linux 3.8, it is readable. The <i>optlen</i> argument should contain the buffer size available to receive the device name and is recommended to be <code>IFNAMSIZ</code> bytes. The real device name length is reported back in the <i>optlen</i> argument.</p>
<dt><code>SO_BROADCAST</code></p>
<dd>Set or get the broadcast flag. When enabled, datagram sockets are allowed to send packets to a broadcast address. This option has no effect on stream-oriented sockets.</p>
<dt><code>SO_BSDCOMPAT</code></p>
<dd>Enable BSD bug-to-bug compatibility. This is used by the UDP protocol module in Linux 2.0 and 2.2. If enabled, ICMP errors received for a UDP socket will not be passed to the user program. In later kernel versions, support for this option has been phased out: Linux 2.4 silently ignores it, and Linux 2.6 generates a kernel warning (printk()) if a program uses this option. Linux 2.0 also enabled BSD bug-to-bug compatibility options (random header changing, skipping of the broadcast flag) for raw sockets with this option, but that was removed in Linux 2.2.</p>
<dt><code>SO_DEBUG</code></p>
<dd>Enable socket debugging. Allowed only for processes with the <code>CAP_NET_ADMIN</code> capability or an effective user ID of 0.</p>
<dt><code>SO_DETACH_FILTER</code> (since Linux 2.2), <code>SO_DETACH_BPF</code> (since Linux 3.19)</p>
<dd>These two options, which are synonyms, may be used to remove the classic or extended BPF program attached to a socket with either <code>SO_ATTACH_FILTER</code> or <code>SO_ATTACH_BPF</code>. The option value is ignored.</p>
<dt><code>SO_DOMAIN</code> (since Linux 2.6.32)</p>
<dd>Retrieves the socket domain as an integer, returning a value such as <code>AF_INET6</code>. See <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) for details. This socket option is read-only.</p>
<dt><code>SO_ERROR</code></p>
<dd>Get and clear the pending socket error. This socket option is read-only. Expects an integer.</p>
<dt><code>SO_DONTROUTE</code></p>
<dd>Don&#8217;t send via a gateway, send only to directly connected hosts. The same effect can be achieved by setting the <code>MSG_DONTROUTE</code> flag on a socket <code><a href="/docs/linux/man/2-send/">send</a></code>(2) operation. Expects an integer boolean flag.</p>
<dt><code>SO_INCOMING_CPU</code> (gettable since Linux 3.19, settable since Linux 4.4)</p>
<dd>Sets or gets the CPU affinity of a socket. Expects an integer flag.</p>
<dd>int cpu = 1; setsockopt(fd, SOL_SOCKET, SO_INCOMING_CPU, &amp;cpu,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(cpu));</p>
<dd>Because all of the packets for a single stream (i.e., all packets for the same 4-tuple) arrive on the single RX queue that is associated with a particular CPU, the typical use case is to employ one listening process per RX queue, with the incoming flow being handled by a listener on the same CPU that is handling the RX queue. This provides optimal NUMA behavior and keeps CPU caches hot.</p>
<dt><code>SO_INCOMING_NAPI_ID</code> (gettable since Linux 4.12)</p>
<dd>Returns a system-level unique ID called NAPI ID that is associated with a RX queue on which the last packet associated with that socket is received.</p>
<dd>This can be used by an application to split the incoming flows among worker threads based on the RX queue on which the packets associated with the flows are received. It allows each worker thread to be associated with a NIC HW receive queue and service all the connection requests received on that RX queue. This mapping between a app thread and a HW NIC queue streamlines the flow of data from the NIC to the application.</p>
<dt><code>SO_KEEPALIVE</code></p>
<dd>Enable sending of keep-alive messages on connection-oriented sockets. Expects an integer boolean flag.</p>
<dt><code>SO_LINGER</code></p>
<dd>Sets or gets the <code>SO_LINGER</code> option. The argument is a <i>linger</i> structure.</p>
<dd>struct linger {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int l_onoff;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;linger active&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int l_linger;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;how many seconds to linger for&nbsp;*/ };</p>
<dd>When enabled, a <code><a href="/docs/linux/man/2-close/">close</a></code>(2) or <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2) will not return until all queued messages for the socket have been successfully sent or the linger timeout has been reached. Otherwise, the call returns immediately and the closing is done in the background. When the socket is closed as part of <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2), it always lingers in the background.</p>
<dt><code>SO_LOCK_FILTER</code></p>
<dd>When set, this option will prevent changing the filters associated with the socket. These filters include any set using the socket options <code>SO_ATTACH_FILTER</code>, <code>SO_ATTACH_BPF</code>, <code>SO_ATTACH_REUSEPORT_CBPF</code>, and <code>SO_ATTACH_REUSEPORT_EBPF</code>.</p>
<dd>The typical use case is for a privileged process to set up a raw socket (an operation that requires the <code>CAP_NET_RAW</code> capability), apply a restrictive filter, set the <code>SO_LOCK_FILTER</code> option, and then either drop its privileges or pass the socket file descriptor to an unprivileged process via a UNIX domain socket.</p>
<dd>Once the <code>SO_LOCK_FILTER</code> option has been enabled, attempts to change or remove the filter attached to a socket, or to disable the <code>SO_LOCK_FILTER</code> option will fail with the error <code>EPERM</code>.</p>
<dt><code>SO_MARK</code> (since Linux 2.6.25)</p>
<dd>Set the mark for each packet sent through this socket (similar to the netfilter MARK target but socket-based). Changing the mark can be used for mark-based routing without netfilter or for packet filtering. Setting this option requires the <code>CAP_NET_ADMIN</code> capability.</p>
<dt><code>SO_OOBINLINE</code></p>
<dd>If this option is enabled, out-of-band data is directly placed into the receive data stream. Otherwise, out-of-band data is passed only when the <code>MSG_OOB</code> flag is set during receiving.</p>
<dt><code>SO_PASSCRED</code></p>
<dd>Enable or disable the receiving of the <code>SCM_CREDENTIALS</code> control message. For more information see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7).</p>
<dt><code>SO_PASSSEC</code></p>
<dd>Enable or disable the receiving of the <code>SCM_SECURITY</code> control message. For more information see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7).</p>
<dt><code>SO_PEEK_OFF</code> (since Linux 3.4)</p>
<dd>This option, which is currently supported only for <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) sockets, sets the value of the &quot;peek offset&quot; for the <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) system call when used with <code>MSG_PEEK</code> flag.</p>
<dd>When this option is set to a negative value (it is set to -1 for all new sockets), traditional behavior is provided: <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) with the <code>MSG_PEEK</code> flag will peek data from the front of the queue.</p>
<dd>When the option is set to a value greater than or equal to zero, then the next peek at data queued in the socket will occur at the byte offset specified by the option value. At the same time, the &quot;peek offset&quot; will be incremented by the number of bytes that were peeked from the queue, so that a subsequent peek will return the next data in the queue.</p>
<dd>If data is removed from the front of the queue via a call to <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) (or similar) without the <code>MSG_PEEK</code> flag, the &quot;peek offset&quot; will be decreased by the number of bytes removed. In other words, receiving data without the <code>MSG_PEEK</code> flag will cause the &quot;peek offset&quot; to be adjusted to maintain the correct relative position in the queued data, so that a subsequent peek will retrieve the data that would have been retrieved had the data not been removed.</p>
<dd>For datagram sockets, if the &quot;peek offset&quot; points to the middle of a packet, the data returned will be marked with the <code>MSG_TRUNC</code> flag.</p>
<dd>The following example serves to illustrate the use of <code>SO_PEEK_OFF</code>. Suppose a stream socket has the following queued input data:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;aabbccddeeff</p>
<dd>The following sequence of <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2) calls would have the effect noted in the comments:</p>
<dd>int ov = 4; // Set peek offset to 4 setsockopt(fd, SOL_SOCKET, SO_PEEK_OFF, &amp;ov, sizeof(ov)); recv(fd, buf, 2, MSG_PEEK); // Peeks &quot;cc&quot;; offset set to 6 recv(fd, buf, 2, MSG_PEEK); // Peeks &quot;dd&quot;; offset set to 8 recv(fd, buf, 2, 0); // Reads &quot;aa&quot;; offset set to 6 recv(fd, buf, 2, MSG_PEEK); // Peeks &quot;ee&quot;; offset set to 8</p>
<dt><code>SO_PEERCRED</code></p>
<dd>Return the credentials of the peer process connected to this socket. For further details, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7).</p>
<dt><code>SO_PEERSEC</code> (since Linux 2.6.2)</p>
<dd>Return the security context of the peer socket connected to this socket. For further details, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) and <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>SO_PRIORITY</code></p>
<dd>Set the protocol-defined priority for all packets to be sent on this socket. Linux uses this value to order the networking queues: packets with a higher priority may be processed first depending on the selected device queueing discipline. Setting a priority outside the range 0 to 6 requires the <code>CAP_NET_ADMIN</code> capability.</p>
<dt><code>SO_PROTOCOL</code> (since Linux 2.6.32)</p>
<dd>Retrieves the socket protocol as an integer, returning a value such as <code>IPPROTO_SCTP</code>. See <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) for details. This socket option is read-only.</p>
<dt><code>SO_RCVBUF</code></p>
<dd>Sets or gets the maximum socket receive buffer in bytes. The kernel doubles this value (to allow space for bookkeeping overhead) when it is set using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), and this doubled value is returned by <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2). The default value is set by the <i>/proc/sys/net/core/rmem_default</i> file, and the maximum allowed value is set by the <i>/proc/sys/net/core/rmem_max</i> file. The minimum (doubled) value for this option is 256.</p>
<dt><code>SO_RCVBUFFORCE</code> (since Linux 2.6.14)</p>
<dd>Using this socket option, a privileged (<code>CAP_NET_ADMIN</code>) process can perform the same task as <code>SO_RCVBUF</code>, but the <i>rmem_max</i> limit can be overridden.</p>
<dt><code>SO_RCVLOWAT</code> and <code>SO_SNDLOWAT</code></p>
<dd>Specify the minimum number of bytes in the buffer until the socket layer will pass the data to the protocol (<code>SO_SNDLOWAT</code>) or the user on receiving (<code>SO_RCVLOWAT</code>). These two values are initialized to 1. <code>SO_SNDLOWAT</code> is not changeable on Linux (<code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) fails with the error <code>ENOPROTOOPT</code>). <code>SO_RCVLOWAT</code> is changeable only since Linux 2.4.</p>
<dd>Before Linux 2.6.28 <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) did not respect the <code>SO_RCVLOWAT</code> setting on Linux, and indicated a socket as readable when even a single byte of data was available. A subsequent read from the socket would then block until <code>SO_RCVLOWAT</code> bytes are available. Since Linux 2.6.28, <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) indicate a socket as readable only if at least <code>SO_RCVLOWAT</code> bytes are available.</p>
<dt><code>SO_RCVTIMEO</code> and <code>SO_SNDTIMEO</code></p>
<dd>Specify the receiving or sending timeouts until reporting an error. The argument is a <i>struct timeval</i>. If an input or output function blocks for this period of time, and data has been sent or received, the return value of that function will be the amount of data transferred; if no data has been transferred and the timeout has been reached, then -1 is returned with <i>errno</i> set to <code>EAGAIN</code> or <code>EWOULDBLOCK</code>, or <code>EINPROGRESS</code> (for <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2)) just as if the socket was specified to be nonblocking. If the timeout is set to zero (the default), then the operation will never timeout. Timeouts only have effect for system calls that perform socket I/O (e.g., <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2)); timeouts have no effect for <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), and so on.</p>
<dt><code>SO_REUSEADDR</code></p>
<dd>Indicates that the rules used in validating addresses supplied in a <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) call should allow reuse of local addresses. For <code>AF_INET</code> sockets this means that a socket may bind, except when there is an active listening socket bound to the address. When the listening socket is bound to <code>INADDR_ANY</code> with a specific port then it is not possible to bind to this port for any local address. Argument is an integer boolean flag.</p>
<dt><code>SO_REUSEPORT</code> (since Linux 3.9)</p>
<dd>Permits multiple <code>AF_INET</code> or <code>AF_INET6</code> sockets to be bound to an identical socket address. This option must be set on each socket (including the first socket) prior to calling <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) on the socket. To prevent port hijacking, all of the processes binding to the same address must have the same effective UID. This option can be employed with both TCP and UDP sockets.</p>
<dd>For TCP sockets, this option allows <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) load distribution in a multi-threaded server to be improved by using a distinct listener socket for each thread. This provides improved load distribution as compared to traditional techniques such using a single <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)ing thread that distributes connections, or having multiple threads that compete to <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2) from the same socket.</p>
<dd>For UDP sockets, the use of this option can provide better distribution of incoming datagrams to multiple processes (or threads) as compared to the traditional technique of having multiple processes compete to receive datagrams on the same socket.</p>
<dt><code>SO_RXQ_OVFL</code> (since Linux 2.6.33)</p>
<dd>Indicates that an unsigned 32-bit value ancillary message (cmsg) should be attached to received skbs indicating the number of packets dropped by the socket since its creation.</p>
<dt><code>SO_SELECT_ERR_QUEUE</code> (since Linux 3.10)</p>
<dd>When this option is set on a socket, an error condition on a socket causes notification not only via the <i>exceptfds</i> set of <code><a href="/docs/linux/man/2-select/">select</a></code>(2). Similarly, <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) also returns a <code>POLLPRI</code> whenever an <code>POLLERR</code> event is returned.</p>
<dd>Background: this option was added when waking up on an error condition occurred only via the <i>readfds</i> and <i>writefds</i> sets of <code><a href="/docs/linux/man/2-select/">select</a></code>(2). The option was added to allow monitoring for error conditions via the <i>exceptfds</i> argument without simultaneously having to receive notifications (via <i>readfds</i>) for regular data that can be read from the socket. After changes in Linux 4.16, the use of this flag to achieve the desired notifications is no longer necessary. This option is nevertheless retained for backwards compatibility.</p>
<dt><code>SO_SNDBUF</code></p>
<dd>Sets or gets the maximum socket send buffer in bytes. The kernel doubles this value (to allow space for bookkeeping overhead) when it is set using <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), and this doubled value is returned by <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2). The default value is set by the <i>/proc/sys/net/core/wmem_default</i> file and the maximum allowed value is set by the <i>/proc/sys/net/core/wmem_max</i> file. The minimum (doubled) value for this option is 2048.</p>
<dt><code>SO_SNDBUFFORCE</code> (since Linux 2.6.14)</p>
<dd>Using this socket option, a privileged (<code>CAP_NET_ADMIN</code>) process can perform the same task as <code>SO_SNDBUF</code>, but the <i>wmem_max</i> limit can be overridden.</p>
<dt><code>SO_TIMESTAMP</code></p>
<dd>Enable or disable the receiving of the <code>SO_TIMESTAMP</code> control message. The timestamp control message is sent with level <code>SOL_SOCKET</code> and a <i>cmsg_type</i> of <code>SCM_TIMESTAMP</code>. The <i>cmsg_data</i> field is a <i>struct timeval</i> indicating the reception time of the last packet passed to the user in this call. See <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3) for details on control messages.</p>
<dt><code>SO_TIMESTAMPNS</code> (since Linux 2.6.22)</p>
<dd>Enable or disable the receiving of the <code>SO_TIMESTAMPNS</code> control message. The timestamp control message is sent with level <code>SOL_SOCKET</code> and a <i>cmsg_type</i> of <code>SCM_TIMESTAMPNS</code>. The <i>cmsg_data</i> field is a <i>struct timespec</i> indicating the reception time of the last packet passed to the user in this call. The clock used for the timestamp is <code>CLOCK_REALTIME</code>. See <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3) for details on control messages.</p>
<dd>A socket cannot mix <code>SO_TIMESTAMP</code> and <code>SO_TIMESTAMPNS</code>: the two modes are mutually exclusive.</p>
<dt><code>SO_TYPE</code></p>
<dd>Gets the socket type as an integer (e.g., <code>SOCK_STREAM</code>). This socket option is read-only.</p>
<dt><code>SO_BUSY_POLL</code> (since Linux 3.11)</p>
<dd>Sets the approximate time in microseconds to busy poll on a blocking receive when there is no data. Increasing this value requires <code>CAP_NET_ADMIN</code>. The default for this option is controlled by the <i>/proc/sys/net/core/busy_read</i> file.</p>
<dd>The value in the <i>/proc/sys/net/core/busy_poll</i> file determines how long <code><a href="/docs/linux/man/2-select/">select</a></code>(2) and <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) will busy poll when they operate on sockets with <code>SO_BUSY_POLL</code> set and no events to report are found.</p>
<dd>In both cases, busy polling will only be done when the socket last received data from a network device that supports this option.</p>
<dd>While busy polling may improve latency of some applications, care must be taken when using it since this will increase both CPU utilization and power usage.</dl>
<h3>Signals</h3>
<p>When writing onto a connection-oriented socket that has been shut down (by the local or the remote end) <code>SIGPIPE</code> is sent to the writing process and <code>EPIPE</code> is returned. The signal is not sent when the write call specified the <code>MSG_NOSIGNAL</code> flag. When requested with the <code>FIOSETOWN</code> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) or <code>SIOCSPGRP</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code>SIGIO</code> is sent when an I/O event occurs. It is possible to use <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) or <code><a href="/docs/linux/man/2-select/">select</a></code>(2) in the signal handler to find out which socket the event occurred on. An alternative (in Linux 2.2) is to set a real-time signal using the <code>F_SETSIG</code> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2); the handler of the real time signal will be called with the file descriptor in the <i>si_fd</i> field of its <i>siginfo_t</i>. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for more information. Under some circumstances (e.g., multiple processes accessing a single socket), the condition that caused the <code>SIGIO</code> may have already disappeared when the process reacts to the signal. If this happens, the process should wait again because Linux will resend the signal later.</p>
<h3>/proc interfaces</h3>
<p>The core socket networking parameters can be accessed via files in the directory <i>/proc/sys/net/core/</i>.</p>
<dl>
<dt><i>rmem_default</i></p>
<dd>contains the default setting in bytes of the socket receive buffer.</p>
<dt><i>rmem_max</i></p>
<dd>contains the maximum socket receive buffer size in bytes which a user may set by using the <code>SO_RCVBUF</code> socket option.</p>
<dt><i>wmem_default</i></p>
<dd>contains the default setting in bytes of the socket send buffer.</p>
<dt><i>wmem_max</i></p>
<dd>contains the maximum socket send buffer size in bytes which a user may set by using the <code>SO_SNDBUF</code> socket option.</p>
<dt><i>message_cost</i> and <i>message_burst</i></p>
<dd>configure the token bucket filter used to load limit warning messages caused by external network events.</p>
<dt><i>netdev_max_backlog</i></p>
<dd>Maximum number of packets in the global input queue.</p>
<dt><i>optmem_max</i></p>
<dd>Maximum length of ancillary data and user control data like the iovecs per socket.</dl>
<h3>Ioctls</h3>
<p>These operations can be accessed using <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2): <i>error</i><code> = ioctl(</code><i>ip_socket</i><code>, </code><i>ioctl_type</i><code>, </code><i>&amp;value_result</i><code>);</code></p>
<dl>
<dt><code>SIOCGSTAMP</code></p>
<dd>Return a <i>struct timeval</i> with the receive timestamp of the last packet passed to the user. This is useful for accurate round trip time measurements. See <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) for a description of <i>struct timeval</i>. This ioctl should be used only if the socket options <code>SO_TIMESTAMP</code> and <code>SO_TIMESTAMPNS</code> are not set on the socket. Otherwise, it returns the timestamp of the last packet that was received while <code>SO_TIMESTAMP</code> and <code>SO_TIMESTAMPNS</code> were not set, or it fails if no such packet has been received, (i.e., <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) returns -1 with <i>errno</i> set to <code>ENOENT</code>).</p>
<dt><code>SIOCSPGRP</code></p>
<dd>Set the process or process group that is to receive <code>SIGIO</code> or <code>SIGURG</code> signals when I/O becomes possible or urgent data is available. The argument is a pointer to a <i>pid_t</i>. For further details, see the description of <code>F_SETOWN</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>FIOASYNC</code></p>
<dd>Change the <code>O_ASYNC</code> flag to enable or disable asynchronous I/O mode of the socket. Asynchronous I/O mode means that the <code>SIGIO</code> signal or the signal set with <code>F_SETSIG</code> is raised when a new I/O event occurs.</p>
<dd>Argument is an integer boolean flag. (This operation is synonymous with the use of <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to set the <code>O_ASYNC</code> flag.)</p>
<dt><code>SIOCGPGRP</code></p>
<dd>Get the current process or process group that receives <code>SIGIO</code> or <code>SIGURG</code> signals, or 0 when none is set.</dl>
<p> Valid <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) operations:</p>
<dl>
<dt><code>FIOGETOWN</code></p>
<dd>The same as the <code>SIOCGPGRP</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2).</p>
<dt><code>FIOSETOWN</code></p>
<dd>The same as the <code>SIOCSPGRP</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2).</dl>
<h2>Versions</h2>
<p><code>SO_BINDTODEVICE</code> was introduced in Linux 2.0.30. <code>SO_PASSCRED</code> is new in Linux 2.2. The <i>/proc</i> interfaces were introduced in Linux 2.2. <code>SO_RCVTIMEO</code> and <code>SO_SNDTIMEO</code> are supported since Linux 2.3.41. Earlier, timeouts were fixed to a protocol-specific setting, and could not be read or written.</p>
<h2>Notes</h2>
<p>Linux assumes that half of the send/receive buffer is used for internal kernel structures; thus the values in the corresponding <i>/proc</i> files are twice what can be observed on the wire. </p>
<p> Linux will allow port reuse only with the <code>SO_REUSEADDR</code> option when this option was set both in the previous program that performed a <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) to the port and in the program that wants to reuse the port. This differs from some implementations (e.g., FreeBSD) where only the later program needs to set the <code>SO_REUSEADDR</code> option. Typically this difference is invisible, since, for example, a server program is designed to always set this option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wireshark/">wireshark</a></code>(1), <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3), <code><a href="/docs/linux/man/7-address_families/">address_families</a></code>(7), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-ddp/">ddp</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7), <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
