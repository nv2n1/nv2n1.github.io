---
title: "ping(8)"
name: "ping"
section: "8"
letter: "p"
url: "/docs/linux/man/8-ping/"
description: "ping – send ICMP ECHO_REQUEST to network hosts"
---

<p>ping &#8211; send ICMP ECHO_REQUEST to network hosts</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ping</code> [<code>-aAbBdDfhLnOqrRUvV46</code>] [<code>-c&nbsp;</code><i>count</i>] [<code>-F&nbsp;</code><i>flowlabel</i>] [<code>-i&nbsp;</code><i>interval</i>] [<code>-I&nbsp;</code><i>interface</i>] [<code>-l&nbsp;</code><i>preload</i>] [<code>-m&nbsp;</code><i>mark</i>] [<code>-M&nbsp;</code><i>pmtudisc_option</i>] [<code>-N&nbsp;</code><i>nodeinfo_option</i>] [<code>-w&nbsp;</code><i>deadline</i>] [<code>-W&nbsp;</code><i>timeout</i>] [<code>-p&nbsp;</code><i>pattern</i>] [<code>-Q&nbsp;</code><i>tos</i>] [<code>-s&nbsp;</code><i>packetsize</i>] [<code>-S&nbsp;</code><i>sndbuf</i>] [<code>-t&nbsp;</code><i>ttl</i>] [<code>-T&nbsp;</code><i>timestamp option</i>] [hop&#8230;] {destination}</dl>
<h2>Description</h2>
<p><code>ping</code></p>
<dd>uses the ICMP protocol&#8217;s mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway. ECHO_REQUEST datagrams (&#8220;pings&#8221;) have an IP and ICMP header, followed by a struct timeval and then an arbitrary number of &#8220;pad&#8221; bytes used to fill out the packet. </p>
<p> <code>ping</code> works with both IPv4 and IPv6. Using only one of them explicitly can be enforced by specifying <code>-4</code> or <code>-6</code>. </p>
<p> <code>ping</code> can also send IPv6 Node Information Queries (RFC4620). Intermediate <i>hop</i>s may not be allowed, because IPv6 source routing was deprecated (RFC5095).</p>
<h2>Options</h2>
<p><code>-4</code></p>
<dl>
<dd>Use IPv4 only.</dl>
<p> <code>-6</code></p>
<dl>
<dd>Use IPv6 only.</dl>
<p> <code>-a</code></p>
<dl>
<dd>Audible ping.</dl>
<p> <code>-A</code></p>
<dl>
<dd>Adaptive ping. Interpacket interval adapts to round-trip time, so that effectively not more than one (or more, if preload is set) unanswered probe is present in the network. Minimal interval is 200msec unless super-user. On networks with low RTT this mode is essentially equivalent to flood mode.</dl>
<p> <code>-b</code></p>
<dl>
<dd>Allow pinging a broadcast address.</dl>
<p> <code>-B</code></p>
<dl>
<dd>Do not allow <code>ping</code> to change source address of probes. The address is bound to one selected when <code>ping</code> starts.</dl>
<p> <code>-c</code> <i>count</i></p>
<dl>
<dd>Stop after sending <i>count</i> ECHO_REQUEST packets. With <i>deadline</i> option, <code>ping</code> waits for <i>count</i> ECHO_REPLY packets, until the timeout expires.</dl>
<p> <code>-d</code></p>
<dl>
<dd>Set the SO_DEBUG option on the socket being used. Essentially, this socket option is not used by Linux kernel.</dl>
<p> <code>-D</code></p>
<dl>
<dd>Print timestamp (unix time + microseconds as in gettimeofday) before each line.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Flood ping. For every ECHO_REQUEST sent a period &#8220;.&#8221; is printed, while for every ECHO_REPLY received a backspace is printed. This provides a rapid display of how many packets are being dropped. If interval is not given, it sets interval to zero and outputs packets as fast as they come back or one hundred times per second, whichever is more. Only the super-user may use this option with zero interval.</dl>
<p> <code>-F</code> <i>flow label</i></p>
<dl>
<dd>IPv6 only. Allocate and set 20 bit flow label (in hex) on echo request packets. If value is zero, kernel allocates random flow label.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Show help.</dl>
<p> <code>-i</code> <i>interval</i></p>
<dl>
<dd>Wait <i>interval</i> seconds between sending each packet. Real number allowed with dot as a decimal separator (regardless locale setup). The default is to wait for one second between each packet normally, or not to wait in flood mode. Only super-user may set interval to values less than 2 ms.</dl>
<p> <code>-I</code> <i>interface</i></p>
<dl>
<dd><i>interface</i> is either an address, an interface name or a VRF name. If <i>interface</i> is an address, it sets source address to specified interface address. If <i>interface</i> is an interface name, it sets source interface to specified interface. If <i>interface</i> is a VRF name, each packet is routed using the corresponding routing table; in this case, the <code>-I</code> option can be repeated to specify a source address. NOTE: For IPv6, when doing ping to a link-local scope address, link specification (by the &#8216;%&#8217;-notation in <i>destination</i>, or by this option) can be used but it is no longer required.</dl>
<p> <code>-l</code> <i>preload</i></p>
<dl>
<dd>If <i>preload</i> is specified, <code>ping</code> sends that many packets not waiting for reply. Only the super-user may select preload more than 3.</dl>
<p> <code>-L</code></p>
<dl>
<dd>Suppress loopback of multicast packets. This flag only applies if the ping destination is a multicast address.</dl>
<p> <code>-m</code> <i>mark</i></p>
<dl>
<dd>use <i>mark</i> to tag the packets going out. This is useful for variety of reasons within the kernel such as using policy routing to select specific outbound processing.</dl>
<p> <code>-M</code> <i>pmtudisc_opt</i></p>
<dl>
<dd>Select Path MTU Discovery strategy. <i>pmtudisc_option</i> may be either <i>do</i> (prohibit fragmentation, even local one), <i>want</i> (do PMTU discovery, fragment locally when packet size is large), or <i>dont</i> (do not set DF flag).</dl>
<p> <code>-N</code> <i>nodeinfo_option</i></p>
<dl>
<dd>IPv6 only. Send ICMPv6 Node Information Queries (RFC4620), instead of Echo Request. CAP_NET_RAW capability is required. </p>
<p> <code>help</code></p>
<dl>
<dd>Show help for NI support.</dl>
<p> <code>name</code></p>
<dl>
<dd>Queries for Node Names.</dl>
<p> <code>ipv6</code></p>
<dl>
<dd>Queries for IPv6 Addresses. There are several IPv6 specific flags. </p>
<p> <code>ipv6-global</code></p>
<dl>
<dd>Request IPv6 global-scope addresses.</dl>
<p> <code>ipv6-sitelocal</code></p>
<dl>
<dd>Request IPv6 site-local addresses.</dl>
<p> <code>ipv6-linklocal</code></p>
<dl>
<dd>Request IPv6 link-local addresses.</dl>
<p> <code>ipv6-all</code></p>
<dl>
<dd>Request IPv6 addresses on other interfaces.</dl>
</dl>
<p> <code>ipv4</code></p>
<dl>
<dd>Queries for IPv4 Addresses. There is one IPv4 specific flag. </p>
<p> <code>ipv4-all</code></p>
<dl>
<dd>Request IPv4 addresses on other interfaces.</dl>
</dl>
<p> <code>subject-ipv6=</code><i>ipv6addr</i></p>
<dl>
<dd>IPv6 subject address.</dl>
<p> <code>subject-ipv4=</code><i>ipv4addr</i></p>
<dl>
<dd>IPv4 subject address.</dl>
<p> <code>subject-name=</code><i>nodename</i></p>
<dl>
<dd>Subject name. If it contains more than one dot, fully-qualified domain name is assumed.</dl>
<p> <code>subject-fqdn=</code><i>nodename</i></p>
<dl>
<dd>Subject name. Fully-qualified domain name is always assumed.</dl>
</dl>
<p> <code>-n</code></p>
<dl>
<dd>Numeric output only. No attempt will be made to lookup symbolic names for host addresses.</dl>
<p> <code>-O</code></p>
<dl>
<dd>Report outstanding ICMP ECHO reply before sending next packet. This is useful together with the timestamp <code>-D</code> to log output to a diagnostic file and search for missing answers.</dl>
<p> <code>-p</code> <i>pattern</i></p>
<dl>
<dd>You may specify up to 16 &#8220;pad&#8221; bytes to fill out the packet you send. This is useful for diagnosing data-dependent problems in a network. For example, <code>-p ff</code> will cause the sent packet to be filled with all ones.</dl>
<p> <code>-q</code></p>
<dl>
<dd>Quiet output. Nothing is displayed except the summary lines at startup time and when finished.</dl>
<p> <code>-Q</code> <i>tos</i></p>
<dl>
<dd>Set Quality of Service -related bits in ICMP datagrams. <i>tos</i> can be decimal (<code>ping</code> only) or hex number. </p>
<p> In RFC2474, these fields are interpreted as 8-bit Differentiated Services (DS), consisting of: bits 0-1 (2 lowest bits) of separate data, and bits 2-7 (highest 6 bits) of Differentiated Services Codepoint (DSCP). In RFC2481 and RFC3168, bits 0-1 are used for ECN. </p>
<p> Historically (RFC1349, obsoleted by RFC2474), these were interpreted as: bit 0 (lowest bit) for reserved (currently being redefined as congestion control), 1-4 for Type of Service and bits 5-7 (highest bits) for Precedence.</dl>
<p> <code>-r</code></p>
<dl>
<dd>Bypass the normal routing tables and send directly to a host on an attached interface. If the host is not on a directly-attached network, an error is returned. This option can be used to ping a local host through an interface that has no route through it provided the option <code>-I</code> is also used.</dl>
<p> <code>-R</code></p>
<dl>
<dd><code>ping</code> only. Record route. Includes the RECORD_ROUTE option in the ECHO_REQUEST packet and displays the route buffer on returned packets. Note that the IP header is only large enough for nine such routes. Many hosts ignore or discard this option.</dl>
<p> <code>-s</code> <i>packetsize</i></p>
<dl>
<dd>Specifies the number of data bytes to be sent. The default is 56, which translates into 64 ICMP data bytes when combined with the 8 bytes of ICMP header data.</dl>
<p> <code>-S</code> <i>sndbuf</i></p>
<dl>
<dd>Set socket sndbuf. If not specified, it is selected to buffer not more than one packet.</dl>
<p> <code>-t</code> <i>ttl</i></p>
<dl>
<dd><code>ping</code> only. Set the IP Time to Live.</dl>
<p> <code>-T</code> <i>timestamp option</i></p>
<dl>
<dd>Set special IP timestamp options. <i>timestamp option</i> may be either <i>tsonly</i> (only timestamps), <i>tsandaddr</i> (timestamps and addresses) or <i>tsprespec host1 [host2 [host3 [host4]]]</i> (timestamp prespecified hops).</dl>
<p> <code>-U</code></p>
<dl>
<dd>Print full user-to-user latency (the old behaviour). Normally <code>ping</code> prints network round trip time, which can be different f.e. due to DNS failures.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Verbose output. Do not suppress DUP replies when pinging multicast address.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Show version and exit.</dl>
<p> <code>-w</code> <i>deadline</i></p>
<dl>
<dd>Specify a timeout, in seconds, before <code>ping</code> exits regardless of how many packets have been sent or received. In this case <code>ping</code> does not stop after <i>count</i> packet are sent, it waits either for <i>deadline</i> expire or until <i>count</i> probes are answered or for some error notification from network.</dl>
<p> <code>-W</code> <i>timeout</i></p>
<dl>
<dd>Time to wait for a response, in seconds. The option affects only timeout in absence of any responses, otherwise <code>ping</code> waits for two RTTs. Real number allowed with dot as a decimal separator (regardless locale setup). 0 means infinite timeout.</dl>
<p> When using <code>ping</code> for fault isolation, it should first be run on the local host, to verify that the local network interface is up and running. Then, hosts and gateways further and further away should be &#8220;pinged&#8221;. Round-trip times and packet loss statistics are computed. If duplicate packets are received, they are not included in the packet loss calculation, although the round trip time of these packets is used in calculating the minimum/average/maximum/mdev round-trip time numbers. </p>
<p> Population standard deviation (mdev), essentially an average of how far each ping RTT is from the mean RTT. The higher mdev is, the more variable the RTT is (over time). With a high RTT variability, you will have speed issues with bulk transfers (they will take longer than is strictly speaking necessary, as the variability will eventually cause the sender to wait for ACKs) and you will have middling to poor VoIP quality. </p>
<p> When the specified number of packets have been sent (and received) or if the program is terminated with a SIGINT, a brief summary is displayed. Shorter current statistics can be obtained without termination of process with signal SIGQUIT. </p>
<p> If <code>ping</code> does not receive any reply packets at all it will exit with code 1. If a packet <i>count</i> and <i>deadline</i> are both specified, and fewer than <i>count</i> packets are received by the time the <i>deadline</i> has arrived, it will also exit with code 1. On other error it exits with code 2. Otherwise it exits with code 0. This makes it possible to use the exit code to see if a host is alive or not. </p>
<p> This program is intended for use in network testing, measurement and management. Because of the load it can impose on the network, it is unwise to use <code>ping</code> during normal operations or from automated scripts.</p>
<h2>Icmp Packet Details</h2>
<p>An IP header without options is 20 bytes. An ICMP ECHO_REQUEST packet contains an additional 8 bytes worth of ICMP header followed by an arbitrary amount of data. When a <i>packetsize</i> is given, this indicates the size of this extra piece of data (the default is 56). Thus the amount of data received inside of an IP packet of type ICMP ECHO_REPLY will always be 8 bytes more than the requested data space (the ICMP header). </p>
<p> If the data space is at least of size of struct timeval <code>ping</code> uses the beginning bytes of this space to include a timestamp which it uses in the computation of round trip times. If the data space is shorter, no round trip times are given.</p>
<h2>Duplicate And Damaged Packets</h2>
<p><code>ping</code> will report duplicate and damaged packets. Duplicate packets should never occur, and seem to be caused by inappropriate link-level retransmissions. Duplicates may occur in many situations and are rarely (if ever) a good sign, although the presence of low levels of duplicates may not always be cause for alarm. </p>
<p> Damaged packets are obviously serious cause for alarm and often indicate broken hardware somewhere in the <code>ping</code> packet&#8217;s path (in the network or in the hosts).</p>
<h2>Trying Different Data Patterns</h2>
<p>The (inter)network layer should never treat packets differently depending on the data contained in the data portion. Unfortunately, data-dependent problems have been known to sneak into networks and remain undetected for long periods of time. In many cases the particular pattern that will have problems is something that doesn&#8217;t have sufficient &#8220;transitions&#8221;, such as all ones or all zeros, or a pattern right at the edge, such as almost all zeros. It isn&#8217;t necessarily enough to specify a data pattern of all zeros (for example) on the command line because the pattern that is of interest is at the data link level, and the relationship between what you type and what the controllers transmit can be complicated. </p>
<p> This means that if you have a data-dependent problem you will probably have to do a lot of testing to find it. If you are lucky, you may manage to find a file that either can&#8217;t be sent across your network or that takes much longer to transfer than other similar length files. You can then examine this file for repeated patterns that you can test using the <code>-p</code> option of <code>ping</code>.</p>
<h2>Ttl Details</h2>
<p>The TTL value of an IP packet represents the maximum number of IP routers that the packet can go through before being thrown away. In current practice you can expect each router in the Internet to decrement the TTL field by exactly one. </p>
<p> The TCP/IP specification states that the TTL field for TCP packets should be set to 60, but many systems use smaller values (4.3 BSD uses 30, 4.2 used 15). </p>
<p> The maximum possible value of this field is 255, and most Unix systems set the TTL field of ICMP ECHO_REQUEST packets to 255. This is why you will find you can &#8220;ping&#8221; some hosts, but not reach them with <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1) or <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1). </p>
<p> In normal operation ping prints the TTL value from the packet it receives. When a remote system receives a ping packet, it can do one of three things with the TTL field in its response: </p>
<dl>
<dd>&bull; Not change it; this is what Berkeley Unix systems did before the 4.3BSD Tahoe release. In this case the TTL value in the received packet will be 255 minus the number of routers in the round-trip path.</dl>
<dl>
<dd>&bull; Set it to 255; this is what current Berkeley Unix systems do. In this case the TTL value in the received packet will be 255 minus the number of routers in the path <code>from</code> the remote system <code>to</code> the <code>ping</code>ing host.</dl>
<dl>
<dd>&bull; Set it to some other value. Some machines use the same value for ICMP packets that they use for TCP packets, for example either 30 or 60. Others may use completely wild values.</dl>
<h2>Bugs</h2>
<dl>
<dd>&bull; Many Hosts and Gateways ignore the RECORD_ROUTE option.</dl>
<dl>
<dd>&bull; The maximum IP header length is too small for options like RECORD_ROUTE to be completely useful. There&#8217;s not much that can be done about this, however.</dl>
<dl>
<dd>&bull; Flood pinging is not recommended in general, and flood pinging the broadcast address should only be done under very controlled conditions.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ss/">ss</a></code>(8).</p>
<h2>History</h2>
<p>The <code>ping</code> command appeared in 4.3BSD. </p>
<p> The version described here is its descendant specific to Linux. </p>
<p> As of version s20150815, the <code>ping6</code> binary doesn&#8217;t exist anymore. It has been merged into <code>ping</code>. Creating a symlink named <code>ping6</code> pointing to <code>ping</code> will result in the same functionality as before.</p>
<h2>Security</h2>
<p><code>ping</code> requires CAP_NET_RAW capability to be executed 1) if the program is used for non-echo queries (See <code>-N</code> option), or 2) if kernel does not support non-raw ICMP sockets, or 3) if the user is not allowed to create an ICMP echo socket. The program may be used as set-uid root.</p>
<h2>Availability</h2>
<p><code>ping</code> is part of <i>iputils</i> package.</p>
