---
title: "ip(7)"
name: "ip"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ip/"
description: "ip – Linux IPv4 protocol implementation"
---

<p>ip &#8211; Linux IPv4 protocol implementation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;


#include &lt;netinet/in.h&gt;


#include &lt;netinet/ip.h&gt;        /* superset of previous */
tcp_socket = socket(AF_INET, SOCK_STREAM, 0);


udp_socket = socket(AF_INET, SOCK_DGRAM, 0);


raw_socket = socket(AF_INET, SOCK_RAW, protocol);</code></pre>
<h2>Description</h2>
<p>Linux implements the Internet Protocol, version 4, described in RFC 791 and RFC 1122. <code>ip</code> contains a level 2 multicasting implementation conforming to RFC 1112. It also contains an IP router including a packet filter. The programming interface is BSD-sockets compatible. For more information on sockets, see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). An IP socket is created using <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2): struct sock_extended_err {<br />
    uint32_t ee_errno; /* error number */<br />
    uint8_t ee_origin; /* where the error originated */<br />
    uint8_t ee_type;   /* type */<br />
    uint8_t ee_code;   /* code */<br />
    uint8_t ee_pad;<br />
    uint32_t ee_info; /* additional information */<br />
    uint32_t ee_data; /* other data */<br />
    /* More data may follow */<br />
};<br />
struct sockaddr *SO_EE_OFFENDER(struct sock_extended_err *);</p>
<p>ee_errno</p>
<p>contains the<br />
errno</p>
<p>number of the queued error.<br />
ee_origin</p>
<p>is the origin code of where the error originated.<br />
The other fields are protocol-specific.<br />
The macro<br />
SO_EE_OFFENDER</p>
<p>returns a pointer to the address of the network object<br />
where the error originated from given a pointer to the ancillary message.<br />
If this address is not known, the<br />
sa_family</p>
<p>member of the<br />
sockaddr</p>
<p>contains<br />
AF_UNSPEC</p>
<p>and the other fields of the<br />
sockaddr</p>
<p>are undefined.</p>
<p>IP uses the<br />
sock_extended_err</p>
<p>structure as follows:<br />
ee_origin</p>
<p>is set to<br />
SO_EE_ORIGIN_ICMP</p>
<p>for errors received as an ICMP packet, or<br />
SO_EE_ORIGIN_LOCAL</p>
<p>for locally generated errors.<br />
Unknown values should be ignored.<br />
ee_type</p>
<p>and<br />
ee_code</p>
<p>are set from the type and code fields of the ICMP header.<br />
ee_info</p>
<p>contains the discovered MTU for<br />
EMSGSIZE</p>
<p>errors.<br />
The message also contains the<br />
sockaddr_in of the node</p>
<p>caused the error, which can be accessed with the<br />
SO_EE_OFFENDER</p>
<p>macro.<br />
The<br />
sin_family</p>
<p>field of the<br />
SO_EE_OFFENDER</p>
<p>address is<br />
AF_UNSPEC</p>
<p>when the source was unknown.<br />
When the error originated from the network, all IP options<br />
(IP_OPTIONS, IP_TTL,</p>
<p>etc.) enabled on the socket and contained in the<br />
error packet are passed as control messages.<br />
The payload of the packet causing the error is returned as normal payload.</p>
<p>Note that TCP has no error queue;<br />
MSG_ERRQUEUE</p>
<p>is not permitted on<br />
SOCK_STREAM</p>
<p>sockets.<br />
IP_RECVERR</p>
<p>is valid for TCP, but all errors are returned by socket function return or<br />
SO_ERROR</p>
<p>only.</p>
<p>For raw sockets,<br />
IP_RECVERR</p>
<p>enables passing of all received ICMP errors to the<br />
application, otherwise errors are reported only on connected sockets</p>
<p>It sets or retrieves an integer boolean flag.<br />
IP_RECVERR</p>
<p>defaults to off.<br />
IP_RECVOPTS (since Linux 2.2)</p>
<p>Pass all incoming IP options to the user in a<br />
IP_OPTIONS</p>
<p>control message.<br />
The routing header and other options are already filled in<br />
for the local host.<br />
Not supported for<br />
SOCK_STREAM</p>
<p>sockets.<br />
IP_RECVORIGDSTADDR (since Linux 2.6.29)</p>
<p>This boolean option enables the<br />
IP_ORIGDSTADDR</p>
<p>ancillary message in<br />
recvmsg(2),</p>
<p>in which the kernel returns the original destination address<br />
of the datagram being received.<br />
The ancillary message contains a<br />
struct sockaddr_in.</p>
<p>IP_RECVTOS (since Linux 2.2)</p>
<p>If enabled, the<br />
IP_TOS</p>
<p>ancillary message is passed with incoming packets.<br />
It contains a byte which specifies the Type of Service/Precedence<br />
field of the packet header.<br />
Expects a boolean integer flag.<br />
IP_RECVTTL (since Linux 2.2)</p>
<p>When this flag is set, pass a<br />
IP_TTL</p>
<p>control message with the time-to-live<br />
field of the received packet as a 32 bit integer.<br />
Not supported for<br />
SOCK_STREAM</p>
<p>sockets.<br />
IP_RETOPTS (since Linux 2.2)</p>
<p>Identical to<br />
IP_RECVOPTS,</p>
<p>but returns raw unprocessed options with timestamp and route record<br />
options not filled in for this hop.<br />
IP_ROUTER_ALERT (since Linux 2.2)</p>
<p>Pass all to-be forwarded packets with the<br />
IP Router Alert option set to this socket.<br />
Valid only for raw sockets.<br />
This is useful, for instance, for user-space RSVP daemons.<br />
The tapped packets are not forwarded by the kernel; it is<br />
the user&#8217;s responsibility to send them out again.<br />
Socket binding is ignored,<br />
such packets are filtered only by protocol.<br />
Expects an integer flag.<br />
IP_TOS (since Linux 1.0)</p>
<p>Set or receive the Type-Of-Service (TOS) field that is sent<br />
with every IP packet originating from this socket.<br />
It is used to prioritize packets on the network.<br />
TOS is a byte.<br />
There are some standard TOS flags defined:<br />
IPTOS_LOWDELAY</p>
<p>to minimize delays for interactive traffic,<br />
IPTOS_THROUGHPUT</p>
<p>to optimize throughput,<br />
IPTOS_RELIABILITY</p>
<p>to optimize for reliability,<br />
IPTOS_MINCOST</p>
<p>should be used for &quot;filler data&quot; where slow transmission doesn&#8217;t matter.<br />
At most one of these TOS values can be specified.<br />
Other bits are invalid and shall be cleared.<br />
Linux sends<br />
IPTOS_LOWDELAY</p>
<p>datagrams first by default,<br />
but the exact behavior depends on the configured queueing discipline.</p>
<p>Some high-priority levels may require superuser privileges (the<br />
CAP_NET_ADMIN</p>
<p>capability).</p>
<p>IP_TRANSPARENT (since Linux 2.6.24)</p>
<p>Setting this boolean option enables transparent proxying on this socket.<br />
This socket option allows<br />
the calling application to bind to a nonlocal IP address and operate<br />
both as a client and a server with the foreign address as the local endpoint.<br />
NOTE: this requires that routing be set up in a way that<br />
packets going to the foreign address are routed through the TProxy box<br />
(i.e., the system hosting the application that employs the<br />
IP_TRANSPARENT</p>
<p>socket option)<br />
.Enabling this socket option requires superuser privileges(the<br />
                                                               CAP_NET_ADMIN</p>
<p>                                                                   capability).</p>
<p>TProxy redirection with the iptables TPROXY target also requires that<br />
this option be set on the redirected socket.<br />
IP_TTL (since Linux 1.0)</p>
<p>Set or retrieve the current time-to-live field that is used in every packet<br />
sent from this socket.<br />
IP_UNBLOCK_SOURCE (since Linux 2.4.22 / 2.5.68)</p>
<p>Unblock previously blocked multicast source.<br />
Returns<br />
EADDRNOTAVAIL</p>
<p>when given source is not being blocked.</p>
<p>Argument is an<br />
ip_mreq_source</p>
<p>structure as described under<br />
IP_ADD_SOURCE_MEMBERSHIP.</p>
<p>SO_PEERSEC (since Linux 2.6.17)</p>
<p>If labeled IPSEC or NetLabel is configured on both the sending and<br />
receiving hosts, this read-only socket option returns the security<br />
context of the peer socket connected to this socket.<br />
By default,<br />
this will be the same as the security context of the process that created<br />
the peer socket unless overridden by the policy or by a process with<br />
the required permissions.</p>
<p>The argument to<br />
getsockopt(2)</p>
<p>is a pointer to a buffer of the specified length in bytes<br />
into which the security context string will be copied.<br />
If the buffer length is less than the length of the security<br />
context string, then<br />
getsockopt(2)</p>
<p>returns -1, sets<br />
errno</p>
<p>to<br />
ERANGE,</p>
<p>and returns the required length via<br />
optlen.</p>
<p>The caller should allocate at least<br />
NAME_MAX</p>
<p>bytes for the buffer initially, although this is not guaranteed<br />
to be sufficient.<br />
Resizing the buffer to the returned length<br />
and retrying may be necessary.</p>
<p>The security context string may include a terminating null character<br />
in the returned length, but is not guaranteed to do so: a security<br />
context &quot;foo&quot; might be represented as either {&#8216;f&#8217;,&#8217;o&#8217;,&#8217;o&#8217;} of length 3<br />
or {&#8216;f&#8217;,&#8217;o&#8217;,&#8217;o&#8217;,&#8217;
