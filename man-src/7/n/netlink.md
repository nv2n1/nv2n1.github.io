---
title: "netlink(7)"
name: "netlink"
section: "7"
letter: "n"
url: "/docs/linux/man/7-netlink/"
description: "netlink – communication between kernel and user space (AF_NETLINK)"
---

<p>netlink &#8211; communication between kernel and user space (AF_NETLINK)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;asm/types.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;linux/netlink.h&gt;

netlink_socket = socket(AF_NETLINK, socket_type, netlink_family);</code></pre>
<h2>Description</h2>
<p>Netlink is used to transfer information between the kernel and user-space processes. It consists of a standard sockets-based interface for user space processes and an internal kernel API for kernel modules. The internal kernel interface is not documented in this manual page. There is also an obsolete netlink interface via netlink character devices; this interface is not documented here and is provided only for backward compatibility. Netlink is a datagram-oriented service. Both <code>SOCK_RAW</code> and <code>SOCK_DGRAM</code> are valid values for <i>socket_type</i>. However, the netlink protocol does not distinguish between datagram and raw sockets. <i>netlink_family</i> selects the kernel module or netlink group to communicate with. The currently assigned netlink families are:</p>
<dl>
<dt><code>NETLINK_ROUTE</code></p>
<dd>Receives routing and link updates and may be used to modify the routing tables (both IPv4 and IPv6), IP addresses, link parameters, neighbor setups, queueing disciplines, traffic classes and packet classifiers (see <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7)).</p>
<dt><code>NETLINK_W1</code> (Linux 2.6.13 to 2.16.17)</p>
<dd>Messages from 1-wire subsystem.</p>
<dt><code>NETLINK_USERSOCK</code></p>
<dd>Reserved for user-mode socket protocols.</p>
<dt><code>NETLINK_FIREWALL</code> (up to and including Linux 3.4)</p>
<dd>Transport IPv4 packets from netfilter to user space. Used by <i>ip_queue</i> kernel module. After a long period of being declared obsolete (in favor of the more advanced <i>nfnetlink_queue</i> feature), <code>NETLINK_FIREWALL</code> was removed in Linux 3.5.</p>
<dt><code>NETLINK_SOCK_DIAG</code> (since Linux 3.3)</p>
<dd>Query information about sockets of various protocol families from the kernel (see <code><a href="/docs/linux/man/7-sock_diag/">sock_diag</a></code>(7)).</p>
<dt><code>NETLINK_INET_DIAG</code> (since Linux 2.6.14)</p>
<dd>An obsolete synonym for <code>NETLINK_SOCK_DIAG</code>.</p>
<dt><code>NETLINK_NFLOG</code> (up to and including Linux 3.16)</p>
<dd>Netfilter/iptables ULOG.</p>
<dt><code>NETLINK_XFRM</code></p>
<dd>IPsec.</p>
<dt><code>NETLINK_SELINUX</code> (since Linux 2.6.4)</p>
<dd>SELinux event notifications.</p>
<dt><code>NETLINK_ISCSI</code> (since Linux 2.6.15)</p>
<dd>Open-iSCSI.</p>
<dt><code>NETLINK_AUDIT</code> (since Linux 2.6.6)</p>
<dd>Auditing.</p>
<dt><code>NETLINK_FIB_LOOKUP</code> (since Linux 2.6.13)</p>
<dd>Access to FIB lookup from user space.</p>
<dt><code>NETLINK_CONNECTOR</code> (since Linux 2.6.14)</p>
<dd>Kernel connector. See <i>Documentation/driver-api/connector.rst</i> (or <i>/Documentation/connector/connector.*</i> in kernel 5.2 and earlier) in the Linux kernel source tree for further information.</p>
<dt><code>NETLINK_NETFILTER</code> (since Linux 2.6.14)</p>
<dd>Netfilter subsystem.</p>
<dt><code>NETLINK_SCSITRANSPORT</code> (since Linux 2.6.19)</p>
<dd>SCSI Transports.</p>
<dt><code>NETLINK_RDMA</code> (since Linux 3.0)</p>
<dd>Infiniband RDMA.</p>
<dt><code>NETLINK_IP6_FW</code> (up to and including Linux 3.4)</p>
<dd>Transport IPv6 packets from netfilter to user space. Used by <i>ip6_queue</i> kernel module.</p>
<dt><code>NETLINK_DNRTMSG</code></p>
<dd>DECnet routing messages.</p>
<dt><code>NETLINK_KOBJECT_UEVENT</code> (since Linux 2.6.10)</p>
<dd>Kernel messages to user space.</p>
<dt><code>NETLINK_GENERIC</code> (since Linux 2.6.15)</p>
<dd>Generic netlink family for simplified netlink usage.</p>
<dt><code>NETLINK_CRYPTO</code> (since Linux 3.2)</p>
<dd>Netlink interface to request information about ciphers registered with the kernel crypto API as well as allow configuration of the kernel crypto API.</dl>
<p> Netlink messages consist of a byte stream with one or multiple <i>nlmsghdr</i> headers and associated payload. The byte stream should be accessed only with the standard <code>NLMSG_*</code> macros. See <code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3) for further information. In multipart messages (multiple <i>nlmsghdr</i> headers with associated payload in one byte stream) the first and all following headers have the <code>NLM_F_MULTI</code> flag set, except for the last header which has the type <code>NLMSG_DONE</code>. After each <i>nlmsghdr</i> the payload follows. struct sockaddr_nl {<br />
    sa_family_t nl_family; /* AF_NETLINK */<br />
    unsigned short nl_pad; /* Zero */<br />
    pid_t nl_pid;          /* Port ID */<br />
    __u32 nl_groups;       /* Multicast groups mask */<br />
}; <i>nlmsg_type</i> can be one of the standard message types: <code>NLMSG_NOOP</code> message is to be ignored, <code>NLMSG_ERROR</code> message signals an error and the payload contains an <i>nlmsgerr</i> structure, <code>NLMSG_DONE</code> message terminates a multipart message. struct sockaddr_nl {<br />
    sa_family_t nl_family; /* AF_NETLINK */<br />
    unsigned short nl_pad; /* Zero */<br />
    pid_t nl_pid;          /* Port ID */<br />
    __u32 nl_groups;       /* Multicast groups mask */<br />
}; A netlink family usually specifies more message types, see the appropriate manual pages for that, for example, <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7) for <code>NETLINK_ROUTE</code>. </p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>Standard flag bits in <i>nlmsg_flags</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_REQUEST</code></td>
<td>Must be set on all request messages.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_MULTI</code></td>
<td> The message is part of a multipart message terminated by <code>NLMSG_DONE</code>.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_ACK</code></td>
<td>Request for an acknowledgment on success.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_ECHO</code></td>
<td>Echo this request.
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td COLSPAN=2>Additional flag bits for GET requests
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_ROOT</code></td>
<td>Return the complete table instead of a single entry.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_MATCH</code></td>
<td> Return all entries matching criteria passed in message content. Not implemented yet.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_ATOMIC</code></td>
<td>Return an atomic snapshot of the table.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_DUMP</code></td>
<td> Convenience macro; equivalent to<br />
 (NLM_F_ROOT|NLM_F_MATCH).
</td>
</tr>
</table>
<p> Note that <code>NLM_F_ATOMIC</code> requires the <code>CAP_NET_ADMIN</code> capability or an effective UID of 0. </p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>Additional flag bits for NEW requests
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_REPLACE</code></td>
<td>Replace existing matching object.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_EXCL</code></td>
<td>Don&#8217;t replace if the object already exists.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_CREATE</code></td>
<td>Create object if it doesn&#8217;t already exist.
</td>
</tr>
<tr VALIGN=top>
<td><code>NLM_F_APPEND</code></td>
<td>Add to the end of the object list.
</td>
</tr>
</table>
<p> <i>nlmsg_seq</i> and <i>nlmsg_pid</i> are used to track messages. <i>nlmsg_pid</i> shows the origin of the message. Note that there isn&#8217;t a 1:1 relationship between <i>nlmsg_pid</i> and the PID of the process if the message originated from a netlink socket. See the <code>ADDRESS FORMATS</code> section for further information. Both <i>nlmsg_seq</i> and <i>nlmsg_pid</i> are opaque to netlink core. Netlink is not a reliable protocol. It tries its best to deliver a message to its destination(s), but may drop messages when an out-of-memory condition or other error occurs. For reliable transfer the sender can request an acknowledgement from the receiver by setting the <code>NLM_F_ACK</code> flag. An acknowledgment is an <code>NLMSG_ERROR</code> packet with the error field set to 0. The application must generate acknowledgements for received messages itself. The kernel tries to send an <code>NLMSG_ERROR</code> message for every failed packet. A user process should follow this convention too. However, reliable transmissions from kernel to user are impossible in any case. The kernel can&#8217;t send a netlink message if the socket buffer is full: the message will be dropped and the kernel and the user-space process will no longer have the same view of kernel state. It is up to the application to detect when this happens (via the <code>ENOBUFS</code> error returned by <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2)) and resynchronize.</p>
<h3>Address formats</h3>
<p>The <i>sockaddr_nl</i> structure describes a netlink client in user space or in the kernel. A <i>sockaddr_nl</i> can be either unicast (only sent to one peer) or sent to netlink multicast groups (<i>nl_groups</i> not equal 0). struct sockaddr_nl {<br />
    sa_family_t nl_family; /* AF_NETLINK */<br />
    unsigned short nl_pad; /* Zero */<br />
    pid_t nl_pid;          /* Port ID */<br />
    __u32 nl_groups;       /* Multicast groups mask */<br />
}; <i>nl_pid</i> is the unicast address of netlink socket. It&#8217;s always 0 if the destination is in the kernel. For a user-space process, <i>nl_pid</i> is usually the PID of the process owning the destination socket. However, <i>nl_pid</i> identifies a netlink socket, not a process. If a process owns several netlink sockets, then <i>nl_pid</i> can be equal to the process ID only for at most one socket. There are two ways to assign <i>nl_pid</i> to a netlink socket. If the application sets <i>nl_pid</i> before calling <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), then it is up to the application to make sure that <i>nl_pid</i> is unique. If the application sets it to 0, the kernel takes care of assigning it. The kernel assigns the process ID to the first netlink socket the process opens and assigns a unique <i>nl_pid</i> to every netlink socket that the process subsequently creates. <i>nl_groups</i> is a bit mask with every bit representing a netlink group number. Each netlink family has a set of 32 multicast groups. When <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) is called on the socket, the <i>nl_groups</i> field in the <i>sockaddr_nl</i> should be set to a bit mask of the groups which it wishes to listen to. The default value for this field is zero which means that no multicasts will be received. A socket may multicast messages to any of the multicast groups by setting <i>nl_groups</i> to a bit mask of the groups it wishes to send to when it calls <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) or does a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2). Only processes with an effective UID of 0 or the <code>CAP_NET_ADMIN</code> capability may send or listen to a netlink multicast group. Since Linux 2.6.13, messages can&#8217;t be broadcast to multiple groups. Any replies to a message received for a multicast group should be sent back to the sending PID and the multicast group. Some Linux kernel subsystems may additionally allow other users to send and/or receive messages. As at Linux 3.0, the <code>NETLINK_KOBJECT_UEVENT</code>, <code>NETLINK_GENERIC</code>, <code>NETLINK_ROUTE</code>, and <code>NETLINK_SELINUX</code> groups allow other users to receive messages. No groups allow other users to send messages.</p>
<h3>Socket options</h3>
<p>To set or get a netlink socket option, call <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to write the option with the option level argument set to <code>SOL_NETLINK</code>. Unless otherwise noted, <i>optval</i> is a pointer to an <i>int</i>.</p>
<dl>
<dt><code>NETLINK_PKTINFO</code> (since Linux 2.6.14)</p>
<dd>Enable <code>nl_pktinfo</code> control messages for received packets to get the extended destination group number.</p>
<dt><code>NETLINK_ADD_MEMBERSHIP</code>,&nbsp;<code>NETLINK_DROP_MEMBERSHIP</code> (since Linux 2.6.14)</p>
<dd>Join/leave a group specified by <i>optval</i>.</p>
<dt><code>NETLINK_LIST_MEMBERSHIPS</code> (since Linux 4.2)</p>
<dd>Retrieve all groups a socket is a member of. <i>optval</i> is a pointer to <code>__u32</code> and <i>optlen</i> is the size of the array. The array is filled with the full membership set of the socket, and the required array size is returned in <i>optlen</i>.</p>
<dt><code>NETLINK_BROADCAST_ERROR</code> (since Linux 2.6.30)</p>
<dd>When not set, <code>netlink_broadcast()</code> only reports <code>ESRCH</code> errors and silently ignore <code>ENOBUFS</code> errors.</p>
<dt><code>NETLINK_NO_ENOBUFS</code> (since Linux 2.6.30)</p>
<dd>This flag can be used by unicast and broadcast listeners to avoid receiving <code>ENOBUFS</code> errors.</p>
<dt><code>NETLINK_LISTEN_ALL_NSID</code> (since Linux 4.2)</p>
<dd>When set, this socket will receive netlink notifications from all network namespaces that have an <i>nsid</i> assigned into the network namespace where the socket has been opened. The <i>nsid</i> is sent to user space via an ancillary data.</p>
<dt><code>NETLINK_CAP_ACK</code> (since Linux 4.2)</p>
<dd>The kernel may fail to allocate the necessary room for the acknowledgment message back to user space. This option trims off the payload of the original netlink message. The netlink message header is still included, so the user can guess from the sequence number which message triggered the acknowledgment.</dl>
<h2>Versions</h2>
<p>The socket interface to netlink first appeared Linux 2.2. </p>
<p> Linux 2.0 supported a more primitive device-based netlink interface (which is still available as a compatibility option). This obsolete interface is not described here.</p>
<h2>Notes</h2>
<p>It is often better to use netlink via <i>libnetlink</i> or <i>libnl</i> than via the low-level kernel interface.</p>
<h2>Bugs</h2>
<p>This manual page is not complete.</p>
<h2>Examples</h2>
<p>The following example creates a <code>NETLINK_ROUTE</code> netlink socket which will listen to the <code>RTMGRP_LINK</code> (network interface create/delete/up/down events) and <code>RTMGRP_IPV4_IFADDR</code> (IPv4 addresses add/delete events) multicast groups. struct sockaddr_nl sa;<br />
memset(&amp;sa, 0, sizeof(sa));<br />
sa.nl_family = AF_NETLINK;<br />
sa.nl_groups = RTMGRP_LINK | RTMGRP_IPV4_IFADDR;<br />
fd = socket(AF_NETLINK, SOCK_RAW, NETLINK_ROUTE);<br />
bind(fd, (struct sockaddr *)&amp;sa, sizeof(sa)); The next example demonstrates how to send a netlink message to the kernel (pid 0). Note that the application must take care of message sequence numbers in order to reliably track acknowledgements. struct nlmsghdr *nh; /* The nlmsghdr with payload to send */<br />
struct sockaddr_nl sa;<br />
struct iovec iov = {nh, nh-&gt;nlmsg_len};<br />
struct msghdr msg;<br />
msg = {&amp;sa, sizeof(sa), &amp;iov, 1, NULL, 0, 0};<br />
memset(&amp;sa, 0, sizeof(sa));<br />
sa.nl_family = AF_NETLINK;<br />
nh-&gt;nlmsg_pid = 0;<br />
nh-&gt;nlmsg_seq = ++sequence_number;<br />
/* Request an ack from kernel by setting NLM_F_ACK */<br />
nh-&gt;nlmsg_flags |= NLM_F_ACK; sendmsg(fd, &amp;msg, 0); And the last example is about reading netlink message. </p>
<pre><code>int len;
/* 8192 to avoid message truncation on platforms with
   page size &gt; 4096 */
struct nlmsghdr buf[8192 / sizeof(struct nlmsghdr)];
struct iovec iov = {buf, sizeof(buf)};
struct sockaddr_nl sa;
struct msghdr msg;
struct nlmsghdr *nh;
msg = {&amp;sa, sizeof(sa), &amp;iov, 1, NULL, 0, 0};
len = recvmsg(fd, &amp;msg, 0);
for (nh = (struct nlmsghdr *)buf; NLMSG_OK(nh, len);
     nh = NLMSG_NEXT(nh, len)) {
    /* The end of multipart message */
    if (nh-&gt;nlmsg_type == NLMSG_DONE)
        return;
    if (nh-&gt;nlmsg_type == NLMSG_ERROR)
        /* Do some error handling */
        ...
            /* Continue with parsing payload */
            ...
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3), <code><a href="/docs/linux/man/3-netlink/">netlink</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7), <code><a href="/docs/linux/man/7-sock_diag/">sock_diag</a></code>(7) </p>
<p> information about libnetlink </p>
<p> information about libnl </p>
<p> RFC 3549 &quot;Linux Netlink as an IP Services Protocol&quot;</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
