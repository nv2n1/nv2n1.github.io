---
title: "packet(7)"
name: "packet"
section: "7"
letter: "p"
url: "/docs/linux/man/7-packet/"
description: "packet – packet interface on device level"
---

<p>packet &#8211; packet interface on device level</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/if_packet.h&gt;
#include &lt;net/ethernet.h&gt; /* the L2 protocols */
#include &lt;sys/socket.h&gt;

packet_socket = socket(AF_PACKET, int socket_type, int protocol);</code></pre>
<h2>Description</h2>
<p>Packet sockets are used to receive or send raw packets at the device driver (OSI Layer 2) level. They allow the user to implement protocol modules in user space on top of the physical layer. The <i>socket_type</i> is either <code>SOCK_RAW</code> for raw packets including the link-level header or <code>SOCK_DGRAM</code> for cooked packets with the link-level header removed. The link-level header information is available in a common format in a <i>sockaddr_ll</i> structure. <i>protocol</i> is the IEEE 802.3 protocol number in network byte order. See the <i>&lt;linux/if_ether.h&gt;</i> include file for a list of allowed protocols. When protocol is set to <code>htons(ETH_P_ALL)</code>, then all protocols are received. All incoming packets of that protocol type will be passed to the packet socket before they are passed to the protocols implemented in the kernel. In order to create a packet socket, a process must have the <code>CAP_NET_RAW</code> capability in the user namespace that governs its network namespace. <code>SOCK_RAW</code> packets are passed to and from the device driver without any changes in the packet data. When receiving a packet, the address is still parsed and passed in a standard <i>sockaddr_ll</i> address structure. When transmitting a packet, the user-supplied buffer should contain the physical-layer header. That packet is then queued unmodified to the network driver of the interface defined by the destination address. Some device drivers always add other headers. <code>SOCK_RAW</code> is similar to but not compatible with the obsolete <code>AF_INET/SOCK_PACKET</code> of Linux 2.0. <code>SOCK_DGRAM</code> operates on a slightly higher level. The physical header is removed before the packet is passed to the user. Packets sent through a <code>SOCK_DGRAM</code> packet socket get a suitable physical-layer header based on the information in the <i>sockaddr_ll</i> destination address before they are queued. By default, all packets of the specified protocol type are passed to a packet socket. To get packets only from a specific interface use <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) specifying an address in a <i>struct sockaddr_ll</i> to bind the packet socket to an interface. Fields used for binding are <i>sll_family</i> (should be <code>AF_PACKET</code>), <i>sll_protocol</i>, and <i>sll_ifindex</i>. The <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) operation is not supported on packet sockets. When the <code>MSG_TRUNC</code> flag is passed to <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), or <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></code>(2), the real length of the packet on the wire is always returned, even when it is longer than the buffer.</p>
<h3>Address types</h3>
<p>The <i>sockaddr_ll</i> structure is a device-independent physical-layer address. struct sockaddr_ll {<br />
    unsigned short sll_family;   /* Always AF_PACKET */<br />
    unsigned short sll_protocol; /* Physical-layer protocol */<br />
    int sll_ifindex;             /* Interface number */<br />
    unsigned short sll_hatype;   /* ARP hardware type */<br />
    unsigned char sll_pkttype;   /* Packet type */<br />
    unsigned char sll_halen;     /* Length of address */<br />
    unsigned char sll_addr[8];   /* Physical-layer address */<br />
}; The fields of this structure are as follows:</p>
<dl>
<dt>*</p>
<dd><i>sll_protocol</i> is the standard ethernet protocol type in network byte order as defined in the <i>&lt;linux/if_ether.h&gt;</i> include file. It defaults to the socket&#8217;s protocol.</p>
<dt>*</p>
<dd><i>sll_ifindex</i> is the interface index of the interface (see <code><a href="/docs/linux/man/7-netdevice/">netdevice</a></code>(7)); 0 matches any interface (only permitted for binding). <i>sll_hatype</i> is an ARP type as defined in the <i>&lt;linux/if_arp.h&gt;</i> include file.</p>
<dt>*</p>
<dd><i>sll_pkttype</i> contains the packet type. Valid types are <code>PACKET_HOST</code> for a packet addressed to the local host, <code>PACKET_BROADCAST</code> for a physical-layer broadcast packet, <code>PACKET_MULTICAST</code> for a packet sent to a physical-layer multicast address, <code>PACKET_OTHERHOST</code> for a packet to some other host that has been caught by a device driver in promiscuous mode, and <code>PACKET_OUTGOING</code> for a packet originating from the local host that is looped back to a packet socket. These types make sense only for receiving.</p>
<dt>*</p>
<dd><i>sll_addr</i> and <i>sll_halen</i> contain the physical-layer (e.g., IEEE 802.3) address and its length. The exact interpretation depends on the device.</dl>
<p> When you send packets, it is enough to specify <i>sll_family</i>, <i>sll_addr</i>, <i>sll_halen</i>, <i>sll_ifindex</i>, and <i>sll_protocol</i>. The other fields should be 0. <i>sll_hatype</i> and <i>sll_pkttype</i> are set on received packets for your information.</p>
<h3>Socket options</h3>
<p>Packet socket options are configured by calling <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) with level <code>SOL_PACKET</code>.</p>
<dl>
<dt><code>PACKET_ADD_MEMBERSHIP</code></p>
<dd>
<dt><code>PACKET_DROP_MEMBERSHIP</code></p>
<dd>Packet sockets can be used to configure physical-layer multicasting and promiscuous mode. <code>PACKET_ADD_MEMBERSHIP</code> adds a binding and <code>PACKET_DROP_MEMBERSHIP</code> drops it. They both expect a <i>packet_mreq</i> structure as argument:</p>
<dd>struct packet_mreq {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mr_ifindex;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;interface index&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short mr_type;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;action&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short mr_alen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;address length&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char&nbsp;<wbr>&nbsp;mr_address[8];&nbsp;/*&nbsp;physical-layer address&nbsp;*/ };</p>
<dd><i>mr_ifindex</i> contains the interface index for the interface whose status should be changed. The <i>mr_type</i> field specifies which action to perform. <code>PACKET_MR_PROMISC</code> enables receiving all packets on a shared medium (often known as &quot;promiscuous mode&quot;), <code>PACKET_MR_MULTICAST</code> binds the socket to the physical-layer multicast group specified in <i>mr_address</i> and <i>mr_alen</i>, and <code>PACKET_MR_ALLMULTI</code> sets the socket up to receive all multicast packets arriving at the interface.</p>
<dd>In addition, the traditional ioctls <code>SIOCSIFFLAGS</code>, <code>SIOCADDMULTI</code>, <code>SIOCDELMULTI</code> can be used for the same purpose.</p>
<dt><code>PACKET_AUXDATA</code> (since Linux 2.6.21)</p>
<dd>If this binary option is enabled, the packet socket passes a metadata structure along with each packet in the <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) control field. The structure can be read with <code><a href="/docs/linux/man/3-cmsg/">cmsg</a></code>(3). It is defined as</p>
<dd>struct tpacket_auxdata {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 tp_status;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 tp_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;packet length&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 tp_snaplen;&nbsp;<wbr>&nbsp;/*&nbsp;captured length&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 tp_mac;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 tp_net;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 tp_vlan_tci;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u16 tp_vlan_tpid;&nbsp;/*&nbsp;Since Linux 3.14;&nbsp;earlier, these<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;were unused padding bytes&nbsp;*/ };</p>
<dt><code>PACKET_FANOUT</code> (since Linux 3.1)</p>
<dd>To scale processing across threads, packet sockets can form a fanout group. In this mode, each matching packet is enqueued onto only one socket in the group. A socket joins a fanout group by calling <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) with level <code>SOL_PACKET</code> and option <code>PACKET_FANOUT</code>. Each network namespace can have up to 65536 independent groups. A socket selects a group by encoding the ID in the first 16 bits of the integer option value. The first packet socket to join a group implicitly creates it. To successfully join an existing group, subsequent packet sockets must have the same protocol, device settings, fanout mode and flags (see below). Packet sockets can leave a fanout group only by closing the socket. The group is deleted when the last socket is closed.</p>
<dd>Fanout supports multiple algorithms to spread traffic between sockets, as follows:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>The default mode, <code>PACKET_FANOUT_HASH</code>, sends packets from the same flow to the same socket to maintain per-flow ordering. For each packet, it chooses a socket by taking the packet flow hash modulo the number of sockets in the group, where a flow hash is a hash over network-layer address and optional transport-layer port fields.</p>
<dt>*</p>
<dd>The load-balance mode <code>PACKET_FANOUT_LB</code> implements a round-robin algorithm.</p>
<dt>*</p>
<dd><code>PACKET_FANOUT_CPU</code> selects the socket based on the CPU that the packet arrived on.</p>
<dt>*</p>
<dd><code>PACKET_FANOUT_ROLLOVER</code> processes all data on a single socket, moving to the next when one becomes backlogged.</p>
<dt>*</p>
<dd><code>PACKET_FANOUT_RND</code> selects the socket using a pseudo-random number generator.</p>
<dt>*</p>
<dd><code>PACKET_FANOUT_QM</code> (available since Linux 3.14) selects the socket using the recorded queue_mapping of the received skb.</dl>
</dl>
<dd>Fanout modes can take additional options. IP fragmentation causes packets from the same flow to have different flow hashes. The flag <code>PACKET_FANOUT_FLAG_DEFRAG</code>, if set, causes packets to be defragmented before fanout is applied, to preserve order even in this case. Fanout mode and options are communicated in the second 16 bits of the integer option value. The flag <code>PACKET_FANOUT_FLAG_ROLLOVER</code> enables the roll over mechanism as a backup strategy: if the original fanout algorithm selects a backlogged socket, the packet rolls over to the next available one.</p>
<dt><code>PACKET_LOSS</code> (with <code>PACKET_TX_RING</code>)</p>
<dd>When a malformed packet is encountered on a transmit ring, the default is to reset its <i>tp_status</i> to <code>TP_STATUS_WRONG_FORMAT</code> and abort the transmission immediately. The malformed packet blocks itself and subsequently enqueued packets from being sent. The format error must be fixed, the associated <i>tp_status</i> reset to <code>TP_STATUS_SEND_REQUEST</code>, and the transmission process restarted via <code><a href="/docs/linux/man/2-send/">send</a></code>(2). However, if <code>PACKET_LOSS</code> is set, any malformed packet will be skipped, its <i>tp_status</i> reset to <code>TP_STATUS_AVAILABLE</code>, and the transmission process continued.</p>
<dt><code>PACKET_RESERVE</code> (with <code>PACKET_RX_RING</code>)</p>
<dd>By default, a packet receive ring writes packets immediately following the metadata structure and alignment padding. This integer option reserves additional headroom.</p>
<dt><code>PACKET_RX_RING</code></p>
<dd>Create a memory-mapped ring buffer for asynchronous packet reception. The packet socket reserves a contiguous region of application address space, lays it out into an array of packet slots and copies packets (up to <i>tp_snaplen</i>) into subsequent slots. Each packet is preceded by a metadata structure similar to <i>tpacket_auxdata</i>. The protocol fields encode the offset to the data from the start of the metadata header. <i>tp_net</i> stores the offset to the network layer. If the packet socket is of type <code>SOCK_DGRAM</code>, then <i>tp_mac</i> is the same. If it is of type <code>SOCK_RAW</code>, then that field stores the offset to the link-layer frame. Packet socket and application communicate the head and tail of the ring through the <i>tp_status</i> field. The packet socket owns all slots with <i>tp_status</i> equal to <code>TP_STATUS_KERNEL</code>. After filling a slot, it changes the status of the slot to transfer ownership to the application. During normal operation, the new <i>tp_status</i> value has at least the <code>TP_STATUS_USER</code> bit set to signal that a received packet has been stored. When the application has finished processing a packet, it transfers ownership of the slot back to the socket by setting <i>tp_status</i> equal to <code>TP_STATUS_KERNEL</code>.</p>
<dd>Packet sockets implement multiple variants of the packet ring. The implementation details are described in <i>Documentation/networking/packet_mmap.rst</i> in the Linux kernel source tree.</p>
<dt><code>PACKET_STATISTICS</code></p>
<dd>Retrieve packet socket statistics in the form of a structure</p>
<dd>struct tpacket_stats {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int tp_packets;&nbsp;<wbr>&nbsp;/*&nbsp;Total packet count&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int tp_drops;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Dropped packet count&nbsp;*/ };</p>
<dd>Receiving statistics resets the internal counters. The statistics structure differs when using a ring of variant <code>TPACKET_V3</code>.</p>
<dt><code>PACKET_TIMESTAMP</code> (with <code>PACKET_RX_RING</code>; since Linux 2.6.36)</p>
<dd>The packet receive ring always stores a timestamp in the metadata header. By default, this is a software generated timestamp generated when the packet is copied into the ring. This integer option selects the type of timestamp. Besides the default, it support the two hardware formats described in <i>Documentation/networking/timestamping.rst</i> in the Linux kernel source tree.</p>
<dt><code>PACKET_TX_RING</code> (since Linux 2.6.31)</p>
<dd>Create a memory-mapped ring buffer for packet transmission. This option is similar to <code>PACKET_RX_RING</code> and takes the same arguments. The application writes packets into slots with <i>tp_status</i> equal to <code>TP_STATUS_AVAILABLE</code> and schedules them for transmission by changing <i>tp_status</i> to <code>TP_STATUS_SEND_REQUEST</code>. When packets are ready to be transmitted, the application calls <code><a href="/docs/linux/man/2-send/">send</a></code>(2) or a variant thereof. The <i>buf</i> and <i>len</i> fields of this call are ignored. If an address is passed using <code><a href="/docs/linux/man/2-sendto/">sendto</a></code>(2) or <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), then that overrides the socket default. On successful transmission, the socket resets <i>tp_status</i> to <code>TP_STATUS_AVAILABLE</code>. It immediately aborts the transmission on error unless <code>PACKET_LOSS</code> is set.</p>
<dt><code>PACKET_VERSION</code> (with <code>PACKET_RX_RING</code>; since Linux 2.6.27)</p>
<dd>By default, <code>PACKET_RX_RING</code> creates a packet receive ring of variant <code>TPACKET_V1</code>. To create another variant, configure the desired variant by setting this integer option before creating the ring.</p>
<dt><code>PACKET_QDISC_BYPASS</code> (since Linux 3.14)</p>
<dd>By default, packets sent through packet sockets pass through the kernel&#8217;s qdisc (traffic control) layer, which is fine for the vast majority of use cases. For traffic generator appliances using packet sockets that intend to brute-force flood the network&#8212;for example, to test devices under load in a similar fashion to pktgen&#8212;this layer can be bypassed by setting this integer option to 1. A side effect is that packet buffering in the qdisc layer is avoided, which will lead to increased drops when network device transmit queues are busy; therefore, use at your own risk.</dl>
<h3>Ioctls</h3>
<p><code>SIOCGSTAMP</code> can be used to receive the timestamp of the last received packet. Argument is a <i>struct timeval</i> variable. In addition, all standard ioctls defined in <code><a href="/docs/linux/man/7-netdevice/">netdevice</a></code>(7) and <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) are valid on packet sockets.</p>
<h3>Error handling</h3>
<p>Packet sockets do no error handling other than errors occurred while passing the packet to the device driver. They don&#8217;t have the concept of a pending error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EADDRNOTAVAIL</code></p>
<dd>Unknown multicast group address passed.</p>
<dt><code>EFAULT</code></p>
<dd>User passed invalid memory address.</p>
<dt><code>EINVAL</code></p>
<dd>Invalid argument.</p>
<dt><code>EMSGSIZE</code></p>
<dd>Packet is bigger than interface MTU.</p>
<dt><code>ENETDOWN</code></p>
<dd>Interface is not up.</p>
<dt><code>ENOBUFS</code></p>
<dd>Not enough memory to allocate the packet.</p>
<dt><code>ENODEV</code></p>
<dd>Unknown device name or interface index specified in interface address.</p>
<dt><code>ENOENT</code></p>
<dd>No packet received.</p>
<dt><code>ENOTCONN</code></p>
<dd>No interface address passed.</p>
<dt><code>ENXIO</code></p>
<dd>Interface address contained an invalid interface index.</p>
<dt><code>EPERM</code></p>
<dd>User has insufficient privileges to carry out this operation.</dl>
<p> In addition, other errors may be generated by the low-level driver.</p>
<h2>Versions</h2>
<p><code>AF_PACKET</code> is a new feature in Linux 2.2. Earlier Linux versions supported only <code>SOCK_PACKET</code>. </p>
<h2>Notes</h2>
<p>For portable programs it is suggested to use <code>AF_PACKET</code> via <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3); although this covers only a subset of the <code>AF_PACKET</code> features. The <code>SOCK_DGRAM</code> packet sockets make no attempt to create or parse the IEEE 802.2 LLC header for a IEEE 802.3 frame. When <code>ETH_P_802_3</code> is specified as protocol for sending the kernel creates the 802.3 frame and fills out the length field; the user has to supply the LLC header to get a fully conforming packet. Incoming 802.3 packets are not multiplexed on the DSAP/SSAP protocol fields; instead they are supplied to the user as protocol <code>ETH_P_802_2</code> with the LLC header prefixed. It is thus not possible to bind to <code>ETH_P_802_3</code>; bind to <code>ETH_P_802_2</code> instead and do the protocol multiplex yourself. The default for sending is the standard Ethernet DIX encapsulation with the protocol filled in. Packet sockets are not subject to the input or output firewall chains.</p>
<h3>Compatibility</h3>
<p>In Linux 2.0, the only way to get a packet socket was with the call: socket(AF_INET, SOCK_PACKET, protocol) This is still supported, but deprecated and strongly discouraged. The main difference between the two methods is that <code>SOCK_PACKET</code> uses the old <i>struct sockaddr_pkt</i> to specify an interface, which doesn&#8217;t provide physical-layer independence. </p>
<pre><code>struct sockaddr_pkt {
    unsigned short spkt_family;
    unsigned char spkt_device[14];
    unsigned short spkt_protocol;
};</code></pre>
<p> <i>spkt_family</i> contains the device type, <i>spkt_protocol</i> is the IEEE 802.3 protocol type as defined in <i>&lt;sys/if_ether.h&gt;</i> and <i>spkt_device</i> is the device name as a null-terminated string, for example, eth0. This structure is obsolete and should not be used in new code.</p>
<h2>Bugs</h2>
<p>The IEEE 802.2/803.3 LLC handling could be considered as a bug. </p>
<p> Socket filters are not documented. </p>
<p> The <code>MSG_TRUNC</code> <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) extension is an ugly hack and should be replaced by a control message. There is currently no way to get the original destination address of packets via <code>SOCK_DGRAM</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) </p>
<p> RFC 894 for the standard IP Ethernet encapsulation. RFC 1700 for the IEEE 802.3 IP encapsulation. </p>
<p> The <i>&lt;linux/if_ether.h&gt;</i> include file for physical-layer protocols. </p>
<p> The Linux kernel source tree. <i>Documentation/networking/filter.rst</i> describes how to apply Berkeley Packet Filters to packet sockets. <i>tools/testing/selftests/net/psock_tpacket.c</i> contains example source code for all available versions of <code>PACKET_RX_RING</code> and <code>PACKET_TX_RING</code>.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
