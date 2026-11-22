---

title: "ip(7)"
name: "ip"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ip/"
description: "ip – Linux IPv4 protocol implementation"
---

<p>ip &#8211; Linux IPv4 protocol implementation </p>

<p> <code>#include &lt;sys/socket.h&gt;</code> <br/>
 <code>#include &lt;netinet/in.h&gt;</code> <br/>
 <code>#include &lt;netinet/ip.h&gt; </code>/* superset of previous */ </p>
<p> <i>tcp_socket</i><code> = socket(AF_INET, SOCK_STREAM, 0);</code> <br/>
 <i>udp_socket</i><code> = socket(AF_INET, SOCK_DGRAM, 0);</code> <br/>
 <i>raw_socket</i><code> = socket(AF_INET, SOCK_RAW, </code><i>protocol</i><code>);</code>  </p>
<h2>DESCRIPTION</h2>
<p> Linux implements the Internet Protocol, version 4, described in RFC 791 and RFC 1122. <code>ip</code> contains a level 2 multicasting implementation conforming to RFC 1112. It also contains an IP router including a packet filter. </p>
<p>The programming interface is BSD-sockets compatible. For more information on sockets, see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7). </p>
<p>An IP socket is created using <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2): </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;socket(AF_INET, socket_type, protocol); </p>
<p>Valid socket types include <code>SOCK_STREAM</code> to open a stream socket, <code>SOCK_DGRAM</code> to open a datagram socket, and <code>SOCK_RAW</code> to open a <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7) socket to access the IP protocol directly. </p>
<p> <i>protocol</i> is the IP protocol in the IP header to be received or sent. Valid values for <i>protocol</i> include: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> 0 and <code>IPPROTO_TCP</code> for <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7) stream sockets; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> 0 and <code>IPPROTO_UDP</code> for <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7) datagram sockets; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>IPPROTO_SCTP</code> for <code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) stream sockets; and </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>IPPROTO_UDPLITE</code> for <code><a href="/docs/linux/man/7-udplite/">udplite</a></code>(7) datagram sockets. </p>
 </dd></dl>
<p>For <code>SOCK_RAW</code> you may specify a valid IANA IP protocol defined in RFC 1700 assigned numbers. </p>
<p>When a process wants to receive new incoming packets or connections, it should bind a socket to a local interface address using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). In this case, only one IP socket may be bound to any given local (address, port) pair. When <code>INADDR_ANY</code> is specified in the bind call, the socket will be bound to <i>all</i> local interfaces. When <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) is called on an unbound socket, the socket is automatically bound to a random free port with the local address set to <code>INADDR_ANY</code>. When <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) is called on an unbound socket, the socket is automatically bound to a random free port or to a usable shared port with the local address set to <code>INADDR_ANY</code>. </p>
<p>A TCP local socket address that has been bound is unavailable for some time after closing, unless the <code>SO_REUSEADDR</code> flag has been set. Care should be taken when using this flag as it makes TCP less reliable.  </p>
<h3>Address format</h3>
<p> An IP socket address is defined as a combination of an IP interface address and a 16-bit port number. The basic IP protocol does not supply port numbers, they are implemented by higher level protocols like <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7) and <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7). On raw sockets <i>sin_port</i> is set to the IP protocol. </p>
<p>struct sockaddr_in { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_family_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sin_family;&nbsp;/*&nbsp;address family: AF_INET&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in_port_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sin_port;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;port in network byte order&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr sin_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;internet address&nbsp;*/ }; </p>
<p>/* Internet address. */ struct in_addr { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;address in network byte order&nbsp;*/ }; </p>
<p> <i>sin_family</i> is always set to <code>AF_INET</code>. This is required; in Linux 2.2 most networking functions return <code>EINVAL</code> when this setting is missing. <i>sin_port</i> contains the port in network byte order. The port numbers below 1024 are called <i>privileged ports</i> (or sometimes: <i>reserved ports</i>). Only a privileged process (on Linux: a process that has the <code>CAP_NET_BIND_SERVICE</code> capability in the user namespace governing its network namespace) may <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) to these sockets. Note that the raw IPv4 protocol as such has no concept of a port, they are implemented only by higher protocols like <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7) and <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7). </p>
<p> <i>sin_addr</i> is the IP host address. The <i>s_addr</i> member of <i>struct in_addr</i> contains the host interface address in network byte order. <i>in_addr</i> should be assigned one of the <code>INADDR_*</code> values (e.g., <code>INADDR_LOOPBACK</code>) using <code><a href="/docs/linux/man/3-htonl/">htonl</a></code>(3) or set using the <code><a href="/docs/linux/man/3-inet_aton/">inet_aton</a></code>(3), <code><a href="/docs/linux/man/3-inet_addr/">inet_addr</a></code>(3), <code><a href="/docs/linux/man/3-inet_makeaddr/">inet_makeaddr</a></code>(3) library functions or directly with the name resolver (see <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3)). </p>
<p>IPv4 addresses are divided into unicast, broadcast, and multicast addresses. Unicast addresses specify a single interface of a host, broadcast addresses specify all hosts on a network, and multicast addresses address all hosts in a multicast group. Datagrams to broadcast addresses can be sent or received only when the <code>SO_BROADCAST</code> socket flag is set. In the current implementation, connection-oriented sockets are allowed to use only unicast addresses. </p>
<p>Note that the address and the port are always stored in network byte order. In particular, this means that you need to call <code><a href="/docs/linux/man/3-htons/">htons</a></code>(3) on the number that is assigned to a port. All address/port manipulation functions in the standard library work in network byte order. </p>
<p>There are several special addresses: <code>INADDR_LOOPBACK</code> (127.0.0.1) always refers to the local host via the loopback device; <code>INADDR_ANY</code> (0.0.0.0) means any address for binding; <code>INADDR_BROADCAST</code> (255.255.255.255) means any host and has the same effect on bind as <code>INADDR_ANY</code> for historical reasons.  </p>
<h3>Socket options</h3>
<p> IP supports some protocol-specific socket options that can be set with <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and read with <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2). The socket option level for IP is <code>IPPROTO_IP</code>. A boolean integer flag is zero when it is false, otherwise true. </p>
<p>When an invalid socket option is specified, <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) and <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) fail with the error <code>ENOPROTOOPT</code>. </p>
<dl>
<dt><code>IP_ADD_MEMBERSHIP</code> (since Linux 1.2) </dt>
<dd> <p> Join a multicast group. Argument is an <i>ip_mreqn</i> structure. </p>
 </dd></dl>
<p>struct ip_mreqn { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imr_multiaddr;&nbsp;/*&nbsp;IP multicast group <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imr_address;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;IP address of local <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;interface&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;imr_ifindex;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;interface index&nbsp;*/ }; </p>
<p> <i>imr_multiaddr</i> contains the address of the multicast group the application wants to join or leave. It must be a valid multicast address (or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) fails with the error <code>EINVAL</code>). <i>imr_address</i> is the address of the local interface with which the system should join the multicast group; if it is equal to <code>INADDR_ANY</code>, an appropriate interface is chosen by the system. <i>imr_ifindex</i> is the interface index of the interface that should join/leave the <i>imr_multiaddr</i> group, or 0 to indicate any interface. </p>
<dl>
<dd> <p> The <i>ip_mreqn</i> structure is available only since Linux 2.2. For compatibility, the old <i>ip_mreq</i> structure (present since Linux 1.2) is still supported; it differs from <i>ip_mreqn</i> only by not including the <i>imr_ifindex</i> field. (The kernel determines which structure is being passed based on the size passed in <i>optlen</i>.) </p>
 </dd>
<dd> <p> <code>IP_ADD_MEMBERSHIP</code> is valid only for <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2). </p>
 </dd>
<dt><code>IP_ADD_SOURCE_MEMBERSHIP</code> (since Linux 2.4.22 / 2.5.68) </dt>
<dd> <p> Join a multicast group and allow receiving data only from a specified source. Argument is an <i>ip_mreq_source</i> structure. </p>
 </dd></dl>
<p>struct ip_mreq_source { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imr_multiaddr;&nbsp;<wbr>&nbsp;/*&nbsp;IP multicast group <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imr_interface;&nbsp;<wbr>&nbsp;/*&nbsp;IP address of local <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;interface&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imr_sourceaddr;&nbsp;/*&nbsp;IP address of <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multicast source&nbsp;*/ }; </p>
<p>The <i>ip_mreq_source</i> structure is similar to <i>ip_mreqn</i> described under <code>IP_ADD_MEMBERSHIP</code>. The <i>imr_multiaddr</i> field contains the address of the multicast group the application wants to join or leave. The <i>imr_interface</i> field is the address of the local interface with which the system should join the multicast group. Finally, the <i>imr_sourceaddr</i> field contains the address of the source the application wants to receive data from. </p>
<dl>
<dd> <p> This option can be used multiple times to allow receiving data from more than one source. </p>
 </dd>
<dt><code>IP_BIND_ADDRESS_NO_PORT</code> (since Linux 4.2) </dt>
<dd> <p> Inform the kernel to not reserve an ephemeral port when using <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) with a port number of 0. The port will later be automatically chosen at <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) time, in a way that allows sharing a source port as long as the 4-tuple is unique. </p>
 </dd>
<dt><code>IP_BLOCK_SOURCE</code> (since Linux 2.4.22 / 2.5.68) </dt>
<dd> <p> Stop receiving multicast data from a specific source in a given group. This is valid only after the application has subscribed to the multicast group using either <code>IP_ADD_MEMBERSHIP</code> or <code>IP_ADD_SOURCE_MEMBERSHIP</code>. </p>
 </dd>
<dd> <p> Argument is an <i>ip_mreq_source</i> structure as described under <code>IP_ADD_SOURCE_MEMBERSHIP</code>. </p>
 </dd>
<dt><code>IP_DROP_MEMBERSHIP</code> (since Linux 1.2) </dt>
<dd> <p> Leave a multicast group. Argument is an <i>ip_mreqn</i> or <i>ip_mreq</i> structure similar to <code>IP_ADD_MEMBERSHIP</code>. </p>
 </dd>
<dt><code>IP_DROP_SOURCE_MEMBERSHIP</code> (since Linux 2.4.22 / 2.5.68) </dt>
<dd> <p> Leave a source-specific group---that is, stop receiving data from a given multicast group that come from a given source. If the application has subscribed to multiple sources within the same group, data from the remaining sources will still be delivered. To stop receiving data from all sources at once, use <code>IP_DROP_MEMBERSHIP</code>. </p>
 </dd>
<dd> <p> Argument is an <i>ip_mreq_source</i> structure as described under <code>IP_ADD_SOURCE_MEMBERSHIP</code>. </p>
 </dd>
<dt><code>IP_FREEBIND</code> (since Linux 2.4) </dt>
<dd> <p> If enabled, this boolean option allows binding to an IP address that is nonlocal or does not (yet) exist. This permits listening on a socket, without requiring the underlying network interface or the specified dynamic IP address to be up at the time that the application is trying to bind to it. This option is the per-socket equivalent of the <i>ip_nonlocal_bind</i> <i>/proc</i> interface described below. </p>
 </dd>
<dt><code>IP_HDRINCL</code> (since Linux 2.0) </dt>
<dd> <p> If enabled, the user supplies an IP header in front of the user data. Valid only for <code>SOCK_RAW</code> sockets; see <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7) for more information. When this flag is enabled, the values set by <code>IP_OPTIONS</code>, <code>IP_TTL</code>, and <code>IP_TOS</code> are ignored. </p>
 </dd>
<dt><code>IP_MSFILTER</code> (since Linux 2.4.22 / 2.5.68) </dt>
<dd> <p> This option provides access to the advanced full-state filtering API. Argument is an <i>ip_msfilter</i> structure. </p>
 </dd></dl>
<p>struct ip_msfilter { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imsf_multiaddr;&nbsp;/*&nbsp;IP multicast group <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imsf_interface;&nbsp;/*&nbsp;IP address of local <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;interface&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;imsf_fmode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Filter-mode&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;imsf_numsrc;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of sources in <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the following array&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr imsf_slist[1];&nbsp;<wbr>&nbsp;/*&nbsp;Array of source <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addresses&nbsp;*/ }; </p>
<p>There are two macros, <code>MCAST_INCLUDE</code> and <code>MCAST_EXCLUDE</code>, which can be used to specify the filtering mode. Additionally, the <code>IP_MSFILTER_SIZE</code>(n) macro exists to determine how much memory is needed to store <i>ip_msfilter</i> structure with <i>n</i> sources in the source list. </p>
<dl>
<dd> <p> For the full description of multicast source filtering refer to RFC 3376. </p>
 </dd>
<dt><code>IP_MTU</code> (since Linux 2.2) </dt>
<dd> <p> Retrieve the current known path MTU of the current socket. Returns an integer. </p>
 </dd>
<dd> <p> <code>IP_MTU</code> is valid only for <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) and can be employed only when the socket has been connected. </p>
 </dd>
<dt><code>IP_MTU_DISCOVER</code> (since Linux 2.2) </dt>
<dd> <p> Set or receive the Path MTU Discovery setting for a socket. When enabled, Linux will perform Path MTU Discovery as defined in RFC 1191 on <code>SOCK_STREAM</code> sockets. For non-<code>SOCK_STREAM</code> sockets, <code>IP_PMTUDISC_DO</code> forces the don&#8217;t-fragment flag to be set on all outgoing packets. It is the user&#8217;s responsibility to packetize the data in MTU-sized chunks and to do the retransmits if necessary. The kernel will reject (with <code>EMSGSIZE</code>) datagrams that are bigger than the known path MTU. <code>IP_PMTUDISC_WANT</code> will fragment a datagram if needed according to the path MTU, or will set the don&#8217;t-fragment flag otherwise. </p>
 </dd>
<dd> <p> The system-wide default can be toggled between <code>IP_PMTUDISC_WANT</code> and <code>IP_PMTUDISC_DONT</code> by writing (respectively, zero and nonzero values) to the <i>/proc/sys/net/ipv4/ip_no_pmtu_disc</i> file. </p>
<table>
<tr VALIGN=top>
<td>Path MTU discovery value</td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td>IP_PMTUDISC_WANT</td>
<td>Use per-route settings.
</td>
</tr>
<tr VALIGN=top>
<td>IP_PMTUDISC_DONT</td>
<td>Never do Path MTU Discovery.
</td>
</tr>
<tr VALIGN=top>
<td>IP_PMTUDISC_DO</td>
<td>Always do Path MTU Discovery.
</td>
</tr>
<tr VALIGN=top>
<td>IP_PMTUDISC_PROBE</td>
<td>Set DF but ignore Path MTU.
</td>
</tr>
</table>
<p>When PMTU discovery is enabled, the kernel automatically keeps track of the path MTU per destination host. When it is connected to a specific peer with <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), the currently known path MTU can be retrieved conveniently using the <code>IP_MTU</code> socket option (e.g., after an <code>EMSGSIZE</code> error occurred). The path MTU may change over time. For connectionless sockets with many destinations, the new MTU for a given destination can also be accessed using the error queue (see <code>IP_RECVERR</code>). A new error will be queued for every incoming MTU update. </p>
 </dd>
<dd> <p> While MTU discovery is in progress, initial packets from datagram sockets may be dropped. Applications using UDP should be aware of this and not take it into account for their packet retransmit strategy. </p>
 </dd>
<dd> <p> To bootstrap the path MTU discovery process on unconnected sockets, it is possible to start with a big datagram size (headers up to 64 kilobytes long) and let it shrink by updates of the path MTU. </p>
 </dd>
<dd> <p> To get an initial estimate of the path MTU, connect a datagram socket to the destination address using <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) and retrieve the MTU by calling <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) with the <code>IP_MTU</code> option. </p>
 </dd>
<dd> <p> It is possible to implement RFC 4821 MTU probing with <code>SOCK_DGRAM</code> or <code>SOCK_RAW</code> sockets by setting a value of <code>IP_PMTUDISC_PROBE</code> (available since Linux 2.6.22). This is also particularly useful for diagnostic tools such as <code><a href="/docs/linux/man/8-tracepath/">tracepath</a></code>(8) that wish to deliberately send probe packets larger than the observed Path MTU. </p>
 </dd>
<dt><code>IP_MULTICAST_ALL</code> (since Linux 2.6.31) </dt>
<dd> <p> This option can be used to modify the delivery policy of multicast messages to sockets bound to the wildcard <code>INADDR_ANY</code> address. The argument is a boolean integer (defaults to 1). If set to 1, the socket will receive messages from all the groups that have been joined globally on the whole system. Otherwise, it will deliver messages only from the groups that have been explicitly joined (for example via the <code>IP_ADD_MEMBERSHIP</code> option) on this particular socket. </p>
 </dd>
<dt><code>IP_MULTICAST_IF</code> (since Linux 1.2) </dt>
<dd> <p> Set the local device for a multicast socket. The argument for <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) is an <i>ip_mreqn</i> or (since Linux 3.5) <i>ip_mreq</i> structure similar to <code>IP_ADD_MEMBERSHIP</code>, or an <i>in_addr</i> structure. (The kernel determines which structure is being passed based on the size passed in <i>optlen</i>.) For <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), the argument is an <i>in_addr</i> structure. </p>
 </dd>
<dt><code>IP_MULTICAST_LOOP</code> (since Linux 1.2) </dt>
<dd> <p> Set or read a boolean integer argument that determines whether sent multicast packets should be looped back to the local sockets. </p>
 </dd>
<dt><code>IP_MULTICAST_TTL</code> (since Linux 1.2) </dt>
<dd> <p> Set or read the time-to-live value of outgoing multicast packets for this socket. It is very important for multicast packets to set the smallest TTL possible. The default is 1 which means that multicast packets don&#8217;t leave the local network unless the user program explicitly requests it. Argument is an integer. </p>
 </dd>
<dt><code>IP_NODEFRAG</code> (since Linux 2.6.36) </dt>
<dd> <p> If enabled (argument is nonzero), the reassembly of outgoing packets is disabled in the netfilter layer. The argument is an integer. </p>
 </dd>
<dd> <p> This option is valid only for <code>SOCK_RAW</code> sockets. </p>
 </dd>
<dt><code>IP_OPTIONS</code> (since Linux 2.0) </dt>
<dd> <p> Set or get the IP options to be sent with every packet from this socket. The arguments are a pointer to a memory buffer containing the options and the option length. The <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) call sets the IP options associated with a socket. The maximum option size for IPv4 is 40 bytes. See RFC 791 for the allowed options. When the initial connection request packet for a <code>SOCK_STREAM</code> socket contains IP options, the IP options will be set automatically to the options from the initial packet with routing headers reversed. Incoming packets are not allowed to change options after the connection is established. The processing of all incoming source routing options is disabled by default and can be enabled by using the <i>accept_source_route</i> <i>/proc</i> interface. Other options like timestamps are still handled. For datagram sockets, IP options can be set only by the local user. Calling <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) with <code>IP_OPTIONS</code> puts the current IP options used for sending into the supplied buffer. </p>
 </dd>
<dt><code>IP_PASSSEC</code> (since Linux 2.6.17) </dt>
<dd> <p> If labeled IPSEC or NetLabel is configured on the sending and receiving hosts, this option enables receiving of the security context of the peer socket in an ancillary message of type <code>SCM_SECURITY</code> retrieved using <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). This option is supported only for UDP sockets; for TCP or SCTP sockets, see the description of the <code>SO_PEERSEC</code> option below. </p>
 </dd>
<dd> <p> The value given as an argument to <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) and returned as the result of <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is an integer boolean flag. </p>
 </dd>
<dd> <p> The security context returned in the <code>SCM_SECURITY</code> ancillary message is of the same format as the one described under the <code>SO_PEERSEC</code> option below. </p>
 </dd>
<dd> <p> Note: the reuse of the <code>SCM_SECURITY</code> message type for the <code>IP_PASSSEC</code> socket option was likely a mistake, since other IP control messages use their own numbering scheme in the IP namespace and often use the socket option value as the message type. There is no conflict currently since the IP option with the same value as <code>SCM_SECURITY</code> is <code>IP_HDRINCL</code> and this is never used for a control message type. </p>
 </dd>
<dt><code>IP_PKTINFO</code> (since Linux 2.2) </dt>
<dd> <p> Pass an <code>IP_PKTINFO</code> ancillary message that contains a <i>pktinfo</i> structure that supplies some information about the incoming packet. This works only for datagram oriented sockets. The argument is a flag that tells the socket whether the <code>IP_PKTINFO</code> message should be passed or not. The message itself can be sent/retrieved only as a control message with a packet using <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). </p>
 </dd>
<dd> <p> struct in_pktinfo { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;ipi_ifindex;&nbsp;<wbr>&nbsp;/*&nbsp;Interface index&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr ipi_spec_dst;&nbsp;/*&nbsp;Local address&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct in_addr ipi_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Header Destination <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address&nbsp;*/ }; </p>
 </dd>
<dd> <p> <i>ipi_ifindex</i> is the unique index of the interface the packet was received on. <i>ipi_spec_dst</i> is the local address of the packet and <i>ipi_addr</i> is the destination address in the packet header. If <code>IP_PKTINFO</code> is passed to <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) and <i>ipi_spec_dst</i> is not zero, then it is used as the local source address for the routing table lookup and for setting up IP source route options. When <i>ipi_ifindex</i> is not zero, the primary local address of the interface specified by the index overwrites <i>ipi_spec_dst</i> for the routing table lookup. </p>
 </dd>
<dt><code>IP_RECVERR</code> (since Linux 2.2) </dt>
<dd> <p> Enable extended reliable error message passing. When enabled on a datagram socket, all generated errors will be queued in a per-socket error queue. When the user receives an error from a socket operation, the errors can be received by calling <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) with the <code>MSG_ERRQUEUE</code> flag set. The <i>sock_extended_err</i> structure describing the error will be passed in an ancillary message with the type <code>IP_RECVERR</code> and the level <code>IPPROTO_IP</code>. This is useful for reliable error handling on unconnected sockets. The received data portion of the error queue contains the error packet. </p>
 </dd>
<dd> <p> The <code>IP_RECVERR</code> control message contains a <i>sock_extended_err</i> structure: </p>
 </dd>
<dd> <p> #define SO_EE_ORIGIN_NONE 0 #define SO_EE_ORIGIN_LOCAL 1 #define SO_EE_ORIGIN_ICMP 2 #define SO_EE_ORIGIN_ICMP6 3 </p>
<p>struct sock_extended_err { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_errno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;error number&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_origin;&nbsp;<wbr>&nbsp;/*&nbsp;where the error originated&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;type&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;code&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;ee_pad; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_info;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;additional information&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ee_data;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;other data&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;More data may follow&nbsp;*/ }; </p>
<p>struct sockaddr *SO_EE_OFFENDER(struct sock_extended_err *); </p>
 </dd>
<dd> <p> <i>ee_errno</i> contains the <i>errno</i> number of the queued error. <i>ee_origin</i> is the origin code of where the error originated. The other fields are protocol-specific. The macro <code>SO_EE_OFFENDER</code> returns a pointer to the address of the network object where the error originated from given a pointer to the ancillary message. If this address is not known, the <i>sa_family</i> member of the <i>sockaddr</i> contains <code>AF_UNSPEC</code> and the other fields of the <i>sockaddr</i> are undefined. </p>
 </dd>
<dd> <p> IP uses the <i>sock_extended_err</i> structure as follows: <i>ee_origin</i> is set to <code>SO_EE_ORIGIN_ICMP</code> for errors received as an ICMP packet, or <code>SO_EE_ORIGIN_LOCAL</code> for locally generated errors. Unknown values should be ignored. <i>ee_type</i> and <i>ee_code</i> are set from the type and code fields of the ICMP header. <i>ee_info</i> contains the discovered MTU for <code>EMSGSIZE</code> errors. The message also contains the <i>sockaddr_in of the node</i> caused the error, which can be accessed with the <code>SO_EE_OFFENDER</code> macro. The <i>sin_family</i> field of the <code>SO_EE_OFFENDER</code> address is <code>AF_UNSPEC</code> when the source was unknown. When the error originated from the network, all IP options (<code>IP_OPTIONS</code>, <code>IP_TTL</code>, etc.) enabled on the socket and contained in the error packet are passed as control messages. The payload of the packet causing the error is returned as normal payload. Note that TCP has no error queue; <code>MSG_ERRQUEUE</code> is not permitted on <code>SOCK_STREAM</code> sockets. <code>IP_RECVERR</code> is valid for TCP, but all errors are returned by socket function return or <code>SO_ERROR</code> only. </p>
 </dd>
<dd> <p> For raw sockets, <code>IP_RECVERR</code> enables passing of all received ICMP errors to the application, otherwise errors are reported only on connected sockets </p>
 </dd>
<dd> <p> It sets or retrieves an integer boolean flag. <code>IP_RECVERR</code> defaults to off. </p>
 </dd>
<dt><code>IP_RECVOPTS</code> (since Linux 2.2) </dt>
<dd> <p> Pass all incoming IP options to the user in a <code>IP_OPTIONS</code> control message. The routing header and other options are already filled in for the local host. Not supported for <code>SOCK_STREAM</code> sockets. </p>
 </dd>
<dt><code>IP_RECVORIGDSTADDR</code> (since Linux 2.6.29) </dt>
<dd> <p> This boolean option enables the <code>IP_ORIGDSTADDR</code> ancillary message in <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), in which the kernel returns the original destination address of the datagram being received. The ancillary message contains a <i>struct sockaddr_in</i>. </p>
 </dd>
<dt><code>IP_RECVTOS</code> (since Linux 2.2) </dt>
<dd> <p> If enabled, the <code>IP_TOS</code> ancillary message is passed with incoming packets. It contains a byte which specifies the Type of Service/Precedence field of the packet header. Expects a boolean integer flag. </p>
 </dd>
<dt><code>IP_RECVTTL</code> (since Linux 2.2) </dt>
<dd> <p> When this flag is set, pass a <code>IP_TTL</code> control message with the time-to-live field of the received packet as a 32 bit integer. Not supported for <code>SOCK_STREAM</code> sockets. </p>
 </dd>
<dt><code>IP_RETOPTS</code> (since Linux 2.2) </dt>
<dd> <p> Identical to <code>IP_RECVOPTS</code>, but returns raw unprocessed options with timestamp and route record options not filled in for this hop. </p>
 </dd>
<dt><code>IP_ROUTER_ALERT</code> (since Linux 2.2) </dt>
<dd> <p> Pass all to-be forwarded packets with the IP Router Alert option set to this socket. Valid only for raw sockets. This is useful, for instance, for user-space RSVP daemons. The tapped packets are not forwarded by the kernel; it is the user&#8217;s responsibility to send them out again. Socket binding is ignored, such packets are filtered only by protocol. Expects an integer flag. </p>
 </dd>
<dt><code>IP_TOS</code> (since Linux 1.0) </dt>
<dd> <p> Set or receive the Type-Of-Service (TOS) field that is sent with every IP packet originating from this socket. It is used to prioritize packets on the network. TOS is a byte. There are some standard TOS flags defined: <code>IPTOS_LOWDELAY</code> to minimize delays for interactive traffic, <code>IPTOS_THROUGHPUT</code> to optimize throughput, <code>IPTOS_RELIABILITY</code> to optimize for reliability, <code>IPTOS_MINCOST</code> should be used for &quot;filler data&quot; where slow transmission doesn&#8217;t matter. At most one of these TOS values can be specified. Other bits are invalid and shall be cleared. Linux sends <code>IPTOS_LOWDELAY</code> datagrams first by default, but the exact behavior depends on the configured queueing discipline. Some high-priority levels may require superuser privileges (the <code>CAP_NET_ADMIN</code> capability). </p>
 </dd>
<dt><code>IP_TRANSPARENT</code> (since Linux 2.6.24) </dt>
<dd> <p> Setting this boolean option enables transparent proxying on this socket. This socket option allows the calling application to bind to a nonlocal IP address and operate both as a client and a server with the foreign address as the local endpoint. NOTE: this requires that routing be set up in a way that packets going to the foreign address are routed through the TProxy box (i.e., the system hosting the application that employs the <code>IP_TRANSPARENT</code> socket option). Enabling this socket option requires superuser privileges (the <code>CAP_NET_ADMIN</code> capability). </p>
 </dd>
<dd> <p> TProxy redirection with the iptables TPROXY target also requires that this option be set on the redirected socket. </p>
 </dd>
<dt><code>IP_TTL</code> (since Linux 1.0) </dt>
<dd> <p> Set or retrieve the current time-to-live field that is used in every packet sent from this socket. </p>
 </dd>
<dt><code>IP_UNBLOCK_SOURCE</code> (since Linux 2.4.22 / 2.5.68) </dt>
<dd> <p> Unblock previously blocked multicast source. Returns <code>EADDRNOTAVAIL</code> when given source is not being blocked. </p>
 </dd>
<dd> <p> Argument is an <i>ip_mreq_source</i> structure as described under <code>IP_ADD_SOURCE_MEMBERSHIP</code>. </p>
 </dd>
<dt><code>SO_PEERSEC</code> (since Linux 2.6.17) </dt>
<dd> <p> If labeled IPSEC or NetLabel is configured on both the sending and receiving hosts, this read-only socket option returns the security context of the peer socket connected to this socket. By default, this will be the same as the security context of the process that created the peer socket unless overridden by the policy or by a process with the required permissions. </p>
 </dd>
<dd> <p> The argument to <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) is a pointer to a buffer of the specified length in bytes into which the security context string will be copied. If the buffer length is less than the length of the security context string, then <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) returns -1, sets <i>errno</i> to <code>ERANGE</code>, and returns the required length via <i>optlen</i>. The caller should allocate at least <code>NAME_MAX</code> bytes for the buffer initially, although this is not guaranteed to be sufficient. Resizing the buffer to the returned length and retrying may be necessary. </p>
 </dd>
<dd> <p> The security context string may include a terminating null character in the returned length, but is not guaranteed to do so: a security context &quot;foo&quot; might be represented as either {&#8216;f&#8217;,&#8216;o&#8217;,&#8216;o&#8217;} of length 3 or {&#8216;f&#8217;,&#8216;o&#8217;,&#8216;o&#8217;,&#8216;\0&#8217;} of length 4, which are considered to be interchangeable. The string is printable, does not contain non-terminating null characters, and is in an unspecified encoding (in particular, it is not guaranteed to be ASCII or UTF-8). </p>
 </dd>
<dd> <p> The use of this option for sockets in the <code>AF_INET</code> address family is supported since Linux 2.6.17 for TCP sockets, and since Linux 4.17 for SCTP sockets. </p>
 </dd>
<dd> <p> For SELinux, NetLabel conveys only the MLS portion of the security context of the peer across the wire, defaulting the rest of the security context to the values defined in the policy for the netmsg initial security identifier (SID). However, NetLabel can be configured to pass full security contexts over loopback. Labeled IPSEC always passes full security contexts as part of establishing the security association (SA) and looks them up based on the association for each packet. </p>
 </dd></dl>
<h3>/proc interfaces</h3>
<p> The IP protocol supports a set of <i>/proc</i> interfaces to configure some global parameters. The parameters can be accessed by reading or writing files in the directory <i>/proc/sys/net/ipv4/</i>. Interfaces described as <i>Boolean</i> take an integer value, with a nonzero value (&quot;true&quot;) meaning that the corresponding option is enabled, and a zero value (&quot;false&quot;) meaning that the option is disabled. </p>
<dl>
<dt><i>ip_always_defrag</i> (Boolean; since Linux 2.2.13) </dt>
<dd> <p> [New with kernel 2.2.13; in earlier kernel versions this feature was controlled at compile time by the <code>CONFIG_IP_ALWAYS_DEFRAG</code> option; this option is not present in 2.4.x and later] </p>
 </dd>
<dd> <p> When this boolean flag is enabled (not equal 0), incoming fragments (parts of IP packets that arose when some host between origin and destination decided that the packets were too large and cut them into pieces) will be reassembled (defragmented) before being processed, even if they are about to be forwarded. </p>
 </dd>
<dd> <p> Enable only if running either a firewall that is the sole link to your network or a transparent proxy; never ever use it for a normal router or host. Otherwise, fragmented communication can be disturbed if the fragments travel over different links. Defragmentation also has a large memory and CPU time cost. </p>
 </dd>
<dd> <p> This is automagically turned on when masquerading or transparent proxying are configured. </p>
 </dd>
<dt><i>ip_autoconfig</i> (since Linux 2.2 to 2.6.17) </dt>
<dd> <p> Not documented. </p>
 </dd>
<dt><i>ip_default_ttl</i> (integer; default: 64; since Linux 2.2) </dt>
<dd> <p> Set the default time-to-live value of outgoing packets. This can be changed per socket with the <code>IP_TTL</code> option. </p>
 </dd>
<dt><i>ip_dynaddr</i> (Boolean; default: disabled; since Linux 2.0.31) </dt>
<dd> <p> Enable dynamic socket address and masquerading entry rewriting on interface address change. This is useful for dialup interface with changing IP addresses. 0 means no rewriting, 1 turns it on and 2 enables verbose mode. </p>
 </dd>
<dt><i>ip_forward</i> (Boolean; default: disabled; since Linux 1.2) </dt>
<dd> <p> Enable IP forwarding with a boolean flag. IP forwarding can be also set on a per-interface basis. </p>
 </dd>
<dt><i>ip_local_port_range</i> (since Linux 2.2) </dt>
<dd> <p> This file contains two integers that define the default local port range allocated to sockets that are not explicitly bound to a port number---that is, the range used for <i>ephemeral ports</i>. An ephemeral port is allocated to a socket in the following circumstances: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>*</dt>
<dd> <p> the port number in a socket address is specified as 0 when calling <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2); </p>
 </dd>
<dt>*</dt>
<dd> <p> <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) is called on a stream socket that was not previously bound; </p>
 </dd>
<dt>*</dt>
<dd> <p> <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) was called on a socket that was not previously bound; </p>
 </dd>
<dt>*</dt>
<dd> <p> <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) is called on a datagram socket that was not previously bound. </p>
 </dd></dl>
</dl>
<dd> <p> Allocation of ephemeral ports starts with the first number in <i>ip_local_port_range</i> and ends with the second number. If the range of ephemeral ports is exhausted, then the relevant system call returns an error (but see BUGS). </p>
 </dd>
<dd> <p> Note that the port range in <i>ip_local_port_range</i> should not conflict with the ports used by masquerading (although the case is handled). Also, arbitrary choices may cause problems with some firewall packet filters that make assumptions about the local ports in use. The first number should be at least greater than 1024, or better, greater than 4096, to avoid clashes with well known ports and to minimize firewall problems. </p>
 </dd>
<dt><i>ip_no_pmtu_disc</i> (Boolean; default: disabled; since Linux 2.2) </dt>
<dd> <p> If enabled, don&#8217;t do Path MTU Discovery for TCP sockets by default. Path MTU discovery may fail if misconfigured firewalls (that drop all ICMP packets) or misconfigured interfaces (e.g., a point-to-point link where the both ends don&#8217;t agree on the MTU) are on the path. It is better to fix the broken routers on the path than to turn off Path MTU Discovery globally, because not doing it incurs a high cost to the network. </p>
 </dd>
<dt><i>ip_nonlocal_bind</i> (Boolean; default: disabled; since Linux 2.4) </dt>
<dd> <p> If set, allows processes to <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) to nonlocal IP addresses, which can be quite useful, but may break some applications. </p>
 </dd>
<dt><i>ip6frag_time</i> (integer; default: 30) </dt>
<dd> <p> Time in seconds to keep an IPv6 fragment in memory. </p>
 </dd>
<dt><i>ip6frag_secret_interval</i> (integer; default: 600) </dt>
<dd> <p> Regeneration interval (in seconds) of the hash secret (or lifetime for the hash secret) for IPv6 fragments. </p>
 </dd>
<dt><i>ipfrag_high_thresh</i> (integer), <i>ipfrag_low_thresh</i> (integer) </dt>
<dd> <p> If the amount of queued IP fragments reaches <i>ipfrag_high_thresh</i>, the queue is pruned down to <i>ipfrag_low_thresh</i>. Contains an integer with the number of bytes. </p>
 </dd>
<dt><i>neigh/*</i></dt>
<dd> <p> See <code><a href="/docs/linux/man/7-arp/">arp</a></code>(7). </p>
 </dd></dl>
<h3>Ioctls</h3>
<p> All ioctls described in <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) apply to <code>ip</code>. </p>
<p>Ioctls to configure generic device parameters are described in <code><a href="/docs/linux/man/7-netdevice/">netdevice</a></code>(7).  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></dt>
<dd> <p> The user tried to execute an operation without the necessary permissions. These include: sending a packet to a broadcast address without having the <code>SO_BROADCAST</code> flag set; sending a packet via a <i>prohibit</i> route; modifying firewall settings without superuser privileges (the <code>CAP_NET_ADMIN</code> capability); binding to a privileged port without superuser privileges (the <code>CAP_NET_BIND_SERVICE</code> capability). </p>
 </dd>
<dt><code>EADDRINUSE</code></dt>
<dd> <p> Tried to bind to an address already in use. </p>
 </dd>
<dt><code>EADDRNOTAVAIL</code></dt>
<dd> <p> A nonexistent interface was requested or the requested source address was not local. </p>
 </dd>
<dt><code>EAGAIN</code></dt>
<dd> <p> Operation on a nonblocking socket would block. </p>
 </dd>
<dt><code>EALREADY</code></dt>
<dd> <p> A connection operation on a nonblocking socket is already in progress. </p>
 </dd>
<dt><code>ECONNABORTED</code></dt>
<dd> <p> A connection was closed during an <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2). </p>
 </dd>
<dt><code>EHOSTUNREACH</code></dt>
<dd> <p> No valid routing table entry matches the destination address. This error can be caused by an ICMP message from a remote router or for the local routing table. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> Invalid argument passed. For send operations this can be caused by sending to a <i>blackhole</i> route. </p>
 </dd>
<dt><code>EISCONN</code></dt>
<dd> <p> <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) was called on an already connected socket. </p>
 </dd>
<dt><code>EMSGSIZE</code></dt>
<dd> <p> Datagram is bigger than an MTU on the path and it cannot be fragmented. </p>
 </dd>
<dt><code>ENOBUFS</code>, <code>ENOMEM</code></dt>
<dd> <p> Not enough free memory. This often means that the memory allocation is limited by the socket buffer limits, not by the system memory, but this is not 100% consistent. </p>
 </dd>
<dt><code>ENOENT</code></dt>
<dd> <p> <code>SIOCGSTAMP</code> was called on a socket where no packet arrived. </p>
 </dd>
<dt><code>ENOPKG</code></dt>
<dd> <p> A kernel subsystem was not configured. </p>
 </dd>
<dt><code>ENOPROTOOPT</code> and <code>EOPNOTSUPP</code></dt>
<dd> <p> Invalid socket option passed. </p>
 </dd>
<dt><code>ENOTCONN</code></dt>
<dd> <p> The operation is defined only on a connected socket, but the socket wasn&#8217;t connected. </p>
 </dd>
<dt><code>EPERM</code></dt>
<dd> <p> User doesn&#8217;t have permission to set high priority, change configuration, or send signals to the requested process or group. </p>
 </dd>
<dt><code>EPIPE</code></dt>
<dd> <p> The connection was unexpectedly closed or shut down by the other end. </p>
 </dd>
<dt><code>ESOCKTNOSUPPORT</code></dt>
<dd> <p> The socket is not configured or an unknown socket type was requested. </p>
 </dd></dl>
<p>Other errors may be generated by the overlaying protocols; see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), and <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7).  </p>
<h2>NOTES</h2>
<p> <code>IP_FREEBIND</code>, <code>IP_MSFILTER</code>, <code>IP_MTU</code>, <code>IP_MTU_DISCOVER</code>, <code>IP_RECVORIGDSTADDR</code>, <code>IP_PASSSEC</code>, <code>IP_PKTINFO</code>, <code>IP_RECVERR</code>, <code>IP_ROUTER_ALERT</code>, and <code>IP_TRANSPARENT</code> are Linux-specific. </p>
<p>Be very careful with the <code>SO_BROADCAST</code> option - it is not privileged in Linux. It is easy to overload the network with careless broadcasts. For new application protocols it is better to use a multicast group instead of broadcasting. Broadcasting is discouraged. </p>
<p>Some other BSD sockets implementations provide <code>IP_RCVDSTADDR</code> and <code>IP_RECVIF</code> socket options to get the destination address and the interface of received datagrams. Linux has the more general <code>IP_PKTINFO</code> for the same task. </p>
<p>Some BSD sockets implementations also provide an <code>IP_RECVTTL</code> option, but an ancillary message with type <code>IP_RECVTTL</code> is passed with the incoming packet. This is different from the <code>IP_TTL</code> option used in Linux. </p>
<p>Using the <code>SOL_IP</code> socket options level isn&#8217;t portable; BSD-based stacks use the <code>IPPROTO_IP</code> level. </p>
<p> <code>INADDR_ANY</code> (0.0.0.0) and <code>INADDR_BROADCAST</code> (255.255.255.255) are byte-order-neutral. <br/>
&nbsp;This means <code><a href="/docs/linux/man/3-htonl/">htonl</a></code>(3) has no effect on them.  </p>
<h3>Compatibility</h3>
<p> For compatibility with Linux 2.0, the obsolete <code>socket(AF_INET, SOCK_PACKET, </code><i>protocol</i><code>)</code> syntax is still supported to open a <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7) socket. This is deprecated and should be replaced by <code>socket(AF_PACKET, SOCK_RAW, </code><i>protocol</i><code>)</code> instead. The main difference is the new <i>sockaddr_ll</i> address structure for generic link layer information instead of the old <code>sockaddr_pkt</code>.  </p>
<h2>BUGS</h2>
<p> There are too many inconsistent error values. </p>
<p>The error used to diagnose exhaustion of the ephemeral port range differs across the various system calls (<code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2)) that can assign ephemeral ports. </p>
<p>The ioctls to configure IP-specific interface options and ARP tables are not described. </p>
<p>Receiving the original destination address with <code>MSG_ERRQUEUE</code> in <i>msg_name</i> by <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) does not work in some 2.2 kernels.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/3-byteorder/">byteorder</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-icmp/">icmp</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-netdevice/">netdevice</a></code>(7), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<p>The kernel source file <i>Documentation/networking/ip-sysctl.txt</i>. </p>
<p>RFC 791 for the original IP specification. RFC 1122 for the IPv4 host requirements. RFC 1812 for the IPv4 router requirements.  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
