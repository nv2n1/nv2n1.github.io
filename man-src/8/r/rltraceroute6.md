---
title: "rltraceroute6(8)"
name: "rltraceroute6"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rltraceroute6/"
description: "rltraceroute6 – IPv6 traceroute tool tcptraceroute6 – TCP/IPv6 traceroute tool"
---

<p>rltraceroute6 &#8211; IPv6 traceroute tool tcptraceroute6 &#8211; TCP/IPv6 traceroute tool </p>
<h2>Synopsis</h2>
<p><code>traceroute6</code> [<code>-AdEILlnrSU</code>] [<code>-f min_hop</code>] [<code>-g hop</code>] [ <code>-i iface</code>] [<code>-m max_hop</code>] [<code>-p port</code>] [<code>-q attempts</code>] [ <code>-s source</code>] [<code>-t tclass</code>] [<code>-w wait</code>] [<code>-z delay_ms</code>] &lt; <code>hostname/address</code>&gt; [<code>packet length</code>] <code>tcptraceroute6</code> [<code>-AdEnrS</code>] [<code>-f min_hop</code>] [<code>-g hop</code>] [ <code>-i iface</code>] [<code>-l packet_size</code>] [<code>-m max_hop</code>] [<code>-p port</code>] [ <code>-q attempts</code>] [<code>-s source</code>] [<code>-t tclass</code>] [<code>-w wait</code>] [ <code>-z delay_ms</code>] &lt; <code>hostname/address</code>&gt; [<code>port</code>] </p>
<h2>Descripton</h2>
<p><code>rltraceroute6</code> is an IPv6 traceroute implementation. </p>
<p> It displays the list of hops along the network route between the local system and specified destination, by sending packets while incrementing their hop limit, until the final destination is reached. </p>
<p> By default, <code>rltraceroute6</code> sends UDP probe packets toward the destination (that&#8217;s the historical default). However, it can also send TCP packets, much like Michael C. Toren&#8217;s <code>tcptraceroute</code> does on IPv4 networks; <code>tcptraceroute6</code> sends TCP packets by default (and mimics tcptraceroute command line syntax). Finally, it can also send ICMPv6 Echo Request packets, like some other traceroute implementations (such as the one in Microsoft Windows); <code>tracert6</code> does this by default. </p>
<p> You must specify the name or address of the host toward which the network route should be determined. An optional additional parameter specifies either the probe packets length (for UDP and ICMP packets), or the destination port number/service name (for TCP packets). </p>
<p> Note that TCP destination port zero really is TCP port numbered 0 (which cannot be used via the standard higer-level TCP/IP programming interface).</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Send TCP/ACK probe packets. That&#8217;s very efficient against stateless firewalls (e.g. the official Linux kernel versions up to and including 2.4.31 and 2.6.14), and utterly helpless against stateful ones. Note that TCP/ACK probing cannot determine whether the destination TCP port is open or not. </p>
<dt><code>-d</code></p>
<dd>Enable socket debugging option (SO_DEBUG). Unless you are debugging the kernel, this is probably not going to have any actual effect. </p>
<dt><code>-E</code></p>
<dd>Send <i>ECN-setup</i> TCP/SYN probe packets (as per RFC 3168) rather than non-ECN-setup TCP/SYN probe packets. This has no effect unless command line optin -S is specified as well. </p>
<dt><code>-F</code></p>
<dd>This option is ignored for backward compatibility. IPv6 packets are never fragmented en route. </p>
<dt><code>-f</code></p>
<dd>Override the initial IPv6 packets hop limit (default: 1). </p>
<dt><code>-g</code></p>
<dd>Add an IPv6 route segment within an IPv6 Routing Header. This enables loose source routing. Currently, only &quot;Type 0&quot; routing header is supported. </p>
<dt><code>-h</code></p>
<dd>Display some help and exit. </p>
<dt><code>-I (rltraceroute6 only)</code></p>
<dd>Send ICMPv6 Echo requests (like ping6) as probe packets. That&#8217;s the default for tracert6. </p>
<dt><code>-i</code></p>
<dd>Only send packets through the specified interface. See also BUGS. </p>
<dt><code>-I (rltraceroute6 only)</code></p>
<dd>Send UDP-Lite (protocol 136) packets (with full checksum coverage) as probe packets instead of normal UDP (protocol 17). </p>
<dt><code>-l</code> (rltraceroute6 only)</p>
<dd>Print the hop limit of received packets. This is mostly used to detect asymmetric routing. </p>
<dt><code>-l</code> (tcptraceroute6 only)</p>
<dd>Specify the size (bytes) of sent packets. </p>
<dt><code>-m</code></p>
<dd>Override the maximum hop limit (maximum number of hops). The default is 30 hops which should be sufficient on the IPv6 Internet for some time. </p>
<dt><code>-N</code></p>
<dd>Try to resolve each hop&#8217;s IPv6 address to a host name. This is the default. This option is meant for backward compatibility with <a href="/docs/linux/man/8-tcptraceroute/">tcptraceroute</a>(8). </p>
<dt><code>-n</code></p>
<dd>Do not try to resolve each hop&#8217;s IPv6 address to a host name. That may speed up the traceroute significantly. </p>
<dt><code>-p</code></p>
<dd>For rltraceroute6, specify the base destination port number (default: 33434). rltraceroute6 assumes that packets toward this port up to this port plus the maximum hop limit are not in use by any program on the final destination and that they are not blocked by some firewall. The fact that this very assumption was not always correct, eventually lead to the development of the original IPv4 tcptraceroute by Michael Toren. </p>
<p> For tcptraceroute6, specify the source port number (default: auto). Note that source port number zero really means number zero, rather than some port number that would be automatically assigned, as is the case with usual softwares. </p>
<dt><code>-q</code></p>
<dd>Override the number of probes sent to each hop (default: 3). </p>
<dt><code>-r</code></p>
<dd>Do not route packets, i.e. do not send packets through a gateway that would be specified by the routing table. See also BUGS. </p>
<dt><code>-S</code></p>
<dd>Use TCP/SYN probe packets. That&#8217;s the default for tcptraceroute6. </p>
<dt><code>-s</code></p>
<dd>Specify the source address to use for probe packets explicitly. </p>
<dt><code>-S</code></p>
<dd>Use UDP probe packets. That&#8217;s the default for rltraceroute6. </p>
<dt><code>-t</code></p>
<dd>Specify the traffic class (DSCP) for probe packets. See also BUGS. </p>
<dt><code>-U (rltraceroute6 only)</code></p>
<dd>Send UDP probe packets. That&#8217;s the default. </p>
<dt><code>-V</code></p>
<dd>Display program version and license and exit. </p>
<dt><code>-w</code></p>
<dd>Override the delay (in seconds) to wait for response once a given probe packet was sent (default: 5 seconds). </p>
<dt><code>-x</code></p>
<dd>This option is ignored for seamless migration from IPv4 traceroute. The IPv6 header has no checksum field. </p>
<dt><code>-z</code></p>
<dd>Specify a milliseconds delay to wait between each probe with identical hop limit. This can be useful to work-around ICMPv6 rate limitation on some hosts. </p>
</dl>
<h2>Diagnostics</h2>
<p>If a response is received, the round-trip time is printed. In addition, specific symbols denote certain errors: </p>
<dl>
<dt><code>*</code> No response</p>
<dd>No valid response received before the timeout delay (see -w option). </p>
<dt><code>!N</code> No route to destination</p>
<dd>There is no entry for the destination network in the routing table. </p>
<dt><code>!A</code> Communication with destination administratively prohibited</p>
<dd>A firewall explicitly rejected the traffic. </p>
<dt><code>!S</code> Beyond scope of source address</p>
<dd>The address scope of the source address is too small to reach the destination address. At the time of writing, this can only happen when using a link-local source address to reach a global scope destination. (Note: some IPv4 traceroute implementations use !S for source route error which is completely different) </p>
<dt><code>!H</code> Address unreachable</p>
<dd>The host address is not reachable for some other reasons, particularly a link-layer failure (e.g. Neighbor discovery failure). </p>
<dt><code>!P</code> Unrecognized Next Header type encountered</p>
<dd>The destination does not implement the layer-4 protocol used. You should retry with ICMPv6 Echo Requests (-I command line option) which MUST be supported by any IPv6 node. </p>
</dl>
<h2>Security</h2>
<p>rltraceroute6 should be <i>setuid</i> <i>root</i> to allow use by non privileged users. It will drop its root privileges before any attempt is made to send or receive data from the network so as to reduce the possible impact of a security vulnerability.</p>
<h2>Bugs</h2>
<p>However useful they might be, -i and -r options are ignored by the official Linux kernel at the time of writing this manpage, and hence do not work as documented. Support for option -t was broken until Linux kernel version 2.6.18. Usage of Routing Header, with option -g, triggers an OOPS on Linux kernel versions below 2.6.17.12. Receiving TCP/SYN-ACK packets does not work on FreeBSD at all. This severely limits the usefulness of tcptraceroute6 on FreeBSD. Packet length takes the IPv6 header and, if present, extension headers into account. rltraceroute6 versions before 0.7.4 used it as IPv6 payload length instead, i.e. did not include the layer-3 headers in the computation. Linux iputils traceroute6 does not even include the UDP header. On the whole, the packet length semantic is very inconsistent among IPv6 traceroute implementations. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-ipv6/">ipv6</a>(7), <a href="/docs/linux/man/8-traceroute/">traceroute</a>(8), <a href="/docs/linux/man/8-tcptraceroute/">tcptraceroute</a>(8), <a href="/docs/linux/man/8-traceroute6/">traceroute6</a>(8) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/ndisc6/">http://www.remlab.net/ndisc6/</a></p>
