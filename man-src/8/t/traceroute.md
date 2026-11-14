---
title: "traceroute(8)"
name: "traceroute"
section: "8"
letter: "t"
url: "/docs/linux/man/8-traceroute/"
description: "traceroute – print the route packets trace to network host"
---

<p>traceroute &#8211; print the route packets trace to network host</p>
<h2>Synopsis</h2>
<p><code>traceroute</code> [<code>-46dFITUnreAV</code>] [<code>-f first_ttl</code>] [<code>-g gate,&#8230;</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-i device</code>] [<code>-m max_ttl</code>] [<code>-p port</code>] [<code>-s src_addr</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-q nqueries</code>] [<code>-N squeries</code>] [<code>-t tos</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-l flow_label</code>] [<code>-w waittime</code>] [<code>-z sendwait</code>] [<code>-UL</code>] [<code>-D</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-P proto</code>] [<code>&#8211;sport=port</code>] [<code>-M method</code>] [<code>-O mod_options</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>&#8211;mtu</code>] [<code>&#8211;back</code>] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <code>host</code> [<code>packet_len</code>]<br />
 <code>traceroute6</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><i>traceroute</i> tracks the route packets taken from an IP network on their way to a given host. It utilizes the IP protocol&#8217;s time to live (TTL) field and attempts to elicit an ICMP TIME_EXCEEDED response from each gateway along the path to the host. </p>
<p> <i>traceroute6</i> is equivalent to <i>traceroute</i> <code>-6</code> </p>
<p> The only required parameter is the name or IP address of the destination <code>host</code>&nbsp;<wbr>. The optional <code>packet_len</code>`gth is the total size of the probing packet (default 60 bytes for IPv4 and 80 for IPv6). The specified size can be ignored in some situations or increased up to a minimal value. </p>
<p> This program attempts to trace the route an IP packet would follow to some internet host by launching probe packets with a small ttl (time to live) then listening for an ICMP &quot;time exceeded&quot; reply from a gateway. We start our probes with a ttl of one and increase by one until we get an ICMP &quot;port unreachable&quot; (or TCP reset), which means we got to the &quot;host&quot;, or hit a max (which defaults to 30 hops). Three probes (by default) are sent at each ttl setting and a line is printed showing the ttl, address of the gateway and round trip time of each probe. The address can be followed by additional information when requested. If the probe answers come from different gateways, the address of each responding system will be printed. If there is no response within a 5.0 seconds (default), an &quot;*&quot; (asterisk) is printed for that probe. </p>
<p> After the trip time, some additional annotation can be printed: <code>!H</code>, <code>!N</code>, or <code>!P</code> (host, network or protocol unreachable), <code>!S</code> (source route failed), <code>!F</code> (fragmentation needed), <code>!X</code> (communication administratively prohibited), <code>!V</code> (host precedence violation), <code>!C</code> (precedence cutoff in effect), or <code>!&lt;num&gt;</code> (ICMP unreachable code &lt;num&gt;). If almost all the probes result in some kind of unreachable, traceroute will give up and exit. </p>
<p> We don&#8217;t want the destination host to process the UDP probe packets, so the destination port is set to an unlikely value (you can change it with the <code>-p</code> flag). There is no such a problem for ICMP or TCP tracerouting (for TCP we use half-open technique, which prevents our probes to be seen by applications on the destination host). </p>
<p> In the modern network environment the traditional traceroute methods can not be always applicable, because of widespread use of firewalls. Such firewalls filter the &quot;unlikely&quot; UDP ports, or even ICMP echoes. To solve this, some additional tracerouting methods are implemented (including tcp), see <code>LIST OF AVAILABLE METHODS</code> below. Such methods try to use particular protocol and source/destination port, in order to bypass firewalls (to be seen by firewalls just as a start of allowed type of a network session).</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help info and exit.</p>
<dt><code>-4</code>, <code>-6</code></p>
<dd>Explicitly force IPv4 or IPv6 tracerouting. By default, the program will try to resolve the name given, and choose the appropriate protocol automatically. If resolving a host name returns both IPv4 and IPv6 addresses, <i>traceroute</i> will use IPv4.</p>
<dt><code>-I, &#8211;icmp</code></p>
<dd>Use ICMP ECHO for probes</p>
<dt><code>-T, &#8211;tcp</code></p>
<dd>Use TCP SYN for probes</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Enable socket level debugging (when the Linux kernel supports it)</p>
<dt><code>-F, &#8211;dont-fragment</code></p>
<dd>Do not fragment probe packets. (For IPv4 it also sets DF bit, which tells intermediate routers not to fragment remotely as well). </p>
<p> Varying the size of the probing packet by the <code>packet_len</code> command line parameter, you can manually obtain information about the MTU of individual network hops. The <code>&#8211;mtu</code> option (see below) tries to do this automatically. </p>
<p> Note, that non-fragmented features (like <code>-F</code> or <code>&#8211;mtu</code>) work properly since the Linux kernel 2.6.22 only. Before that version, IPv6 was always fragmented, IPv4 could use the once the discovered final mtu only (from the route cache), which can be less than the actual mtu of a device.</p>
<dt><code>-f</code><i> first_ttl</i><code>, &#8211;first=</code><i>first_ttl</i></p>
<dd>Specifies with what TTL to start. Defaults to 1.</p>
<dt><code>-g</code><i> gateway</i><code>, &#8211;gateway=</code><i>gateway</i></p>
<dd>Tells traceroute to add an IP source routing option to the outgoing packet that tells the network to route the packet through the specified <i>gateway</i> (most routers have disabled source routing for security reasons). In general, several <i>gateway</i>&#8216;s is allowed (comma separated). For IPv6, the form of <i>num</i><code>,</code><i>addr</i><code>,</code><i>addr&#8230;</i> is allowed, where <i>num</i> is a route header type (default is type 2). Note the type 0 route header is now deprecated (rfc5095).</p>
<dt><code>-i</code><i> interface</i><code>, &#8211;interface=</code><i>interface</i></p>
<dd>Specifies the interface through which <i>traceroute</i> should send packets. By default, the interface is selected according to the routing table.</p>
<dt><code>-m</code><i> max_ttl</i><code>, &#8211;max-hops=</code><i>max_ttl</i></p>
<dd>Specifies the maximum number of hops (max time-to-live value) <i>traceroute</i> will probe. The default is 30.</p>
<dt><code>-N</code><i> squeries</i><code>, &#8211;sim-queries=</code><i>squeries</i></p>
<dd>Specifies the number of probe packets sent out simultaneously. Sending several probes concurrently can speed up <i>traceroute</i> considerably. The default value is 16.<br />
 Note that some routers and hosts can use ICMP rate throttling. In such a situation specifying too large number can lead to loss of some responses.</p>
<dt><code>-n</code></p>
<dd>Do not try to map IP addresses to host names when displaying them.</p>
<dt><code>-p</code><i> port</i><code>, &#8211;port=</code><i>port</i></p>
<dd>For UDP tracing, specifies the destination port base <i>traceroute</i> will use (the destination port number will be incremented by each probe).<br />
 For ICMP tracing, specifies the initial ICMP sequence value (incremented by each probe too).<br />
 For TCP and others specifies just the (constant) destination port to connect.</p>
<dt><code>-t</code><i> tos</i><code>, &#8211;tos=</code><i>tos</i></p>
<dd>For IPv4, set the Type of Service (TOS) and Precedence value. Useful values are 16 (low delay) and 8 (high throughput). Note that in order to use some TOS precedence values, you have to be super user.<br />
 For IPv6, set the Traffic Control value.</p>
<dt><code>-l</code><i> flow_label</i><code>, &#8211;flowlabel=</code><i>flow_label</i></p>
<dd>Use specified flow_label for IPv6 packets.</p>
<dt><code>-w</code><i> waittime</i><code>, &#8211;wait=</code><i>waittime</i></p>
<dd>Set the time (in seconds) to wait for a response to a probe (default 5.0 sec).</p>
<dt><code>-q</code><i> nqueries</i><code>, &#8211;queries=</code><i>nqueries</i></p>
<dd>Sets the number of probe packets per hop. The default is 3.</p>
<dt><code>-r</code></p>
<dd>Bypass the normal routing tables and send directly to a host on an attached network. If the host is not on a directly-attached network, an error is returned. This option can be used to ping a local host through an interface that has no route through it.</p>
<dt><code>-s</code><i> source_addr</i><code>, &#8211;source=</code><i>source_addr</i></p>
<dd>Chooses an alternative source address. Note that you must select the address of one of the interfaces. By default, the address of the outgoing interface is used.</p>
<dt><code>-z</code><i> sendwait</i><code>, &#8211;sendwait=</code><i>sendwait</i></p>
<dd>Minimal time interval between probes (default 0). If the value is more than 10, then it specifies a number in milliseconds, else it is a number of seconds (float point values allowed too). Useful when some routers use rate-limit for ICMP messages.</p>
<dt><code>-e, &#8211;extensions</code></p>
<dd>Show ICMP extensions (rfc4884). The general form is <i>CLASS</i><code>/</code><i>TYPE</i><code>:</code> followed by a hexadecimal dump. The MPLS (rfc4950) is shown parsed, in a form: <code>MPLS:L=</code><i>label</i><code>,E=</code><i>exp_use</i><code>,S=</code><i>stack_bottom</i><code>,T=</code><i>TTL</i> (more objects separated by <code>/</code> ).</p>
<dt><code>-A, &#8211;as-path-lookups</code></p>
<dd>Perform AS path lookups in routing registries and print results directly after the corresponding addresses.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print the version and exit.
</dl>
<p> There are additional options intended for advanced usage (such as alternate trace methods etc.):</p>
<dl>
<dt><code>&#8211;sport</code>=<i>port</i></p>
<dd>Chooses the source port to use. Implies <code>-N 1</code>. Normally source ports (if applicable) are chosen by the system.</p>
<dt><code>&#8211;fwmark</code>=<i>mark</i></p>
<dd>Set the firewall mark for outgoing packets (since the Linux kernel 2.6.25).</p>
<dt><code>-M</code><i> method</i><code>, &#8211;module=</code><i>name</i></p>
<dd>Use specified method for traceroute operations. Default traditional udp method has name <i>default</i>, icmp (<code>-I</code>) and tcp (<code>-T</code>) have names <i>icmp</i> and <i>tcp</i> respectively.<br />
 Method-specific options can be passed by <code>-O&nbsp;<wbr></code>. Most methods have their simple shortcuts, (<code>-I </code>means<code> -M icmp</code>, etc).</p>
<dt><code>-O</code><i> option</i><code>, &#8211;options=</code><i>options</i></p>
<dd>Specifies some method-specific option. Several options are separated by comma (or use several <code>-O</code> on cmdline). Each method may have its own specific options, or many not have them at all. To print information about available options, use <code>-O help</code>.</p>
<dt><code>-U, &#8211;udp</code></p>
<dd>Use UDP to particular destination port for tracerouting (instead of increasing the port per each probe). Default port is 53 (dns).</p>
<dt><code>-UL</code></p>
<dd>Use UDPLITE for tracerouting (default port is 53).</p>
<dt><code>-D, &#8211;dccp</code></p>
<dd>Use DCCP Requests for probes.</p>
<dt><code>-P</code><i> protocol</i><code>, &#8211;protocol=</code><i>protocol</i></p>
<dd>Use raw packet of specified protocol for tracerouting. Default protocol is 253 (rfc3692).</p>
<dt><code>&#8211;mtu</code></p>
<dd>Discover MTU along the path being traced. Implies <code>-F -N 1</code>. New <i>mtu</i> is printed once in a form of <code>F=</code><i>NUM</i> at the first probe of a hop which requires such <i>mtu</i> to be reached. (Actually, the correspond &quot;frag needed&quot; icmp message normally is sent by the previous hop). </p>
<p> Note, that some routers might cache once the seen information on a fragmentation. Thus you can receive the final mtu from a closer hop. Try to specify an unusual <i>tos</i> by <code>-t</code> , this can help for one attempt (then it can be cached there as well).<br />
 See <code>-F</code> option for more info.</p>
<dt><code>&#8211;back</code></p>
<dd>Print the number of backward hops when it seems different with the forward direction. This number is guessed in assumption that remote hops send reply packets with initial ttl set to either 64, or 128 or 255 (which seems a common practice). It is printed as a negate value in a form of &#8216;-NUM&#8217; .</dl>
<h2>List Of Available Methods</h2>
<p>In general, a particular traceroute method may have to be chosen by <code>-M name</code>, but most of the methods have their simple cmdline switches (you can see them after the method name, if present).</p>
<h3>default</h3>
<p>The traditional, ancient method of tracerouting. Used by default. </p>
<p> Probe packets are udp datagrams with so-called &quot;unlikely&quot; destination ports. The &quot;unlikely&quot; port of the first probe is 33434, then for each next probe it is incremented by one. Since the ports are expected to be unused, the destination host normally returns &quot;icmp unreach port&quot; as a final response. (Nobody knows what happens when some application listens for such ports, though). </p>
<p> This method is allowed for unprivileged users.</p>
<h3>icmp &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr> -I</h3>
<p>Most usual method for now, which uses icmp echo packets for probes.<br />
 If you can <a href="/docs/linux/man/8-ping/">ping</a>(8) the destination host, icmp tracerouting is applicable as well. </p>
<p> This method may be allowed for unprivileged users since the kernel 3.0 (IPv4 only), which supports new <i>dgram icmp</i> (or <i></i><i>ping</i>) sockets. To allow such sockets, sysadmin should provide <i>net/ipv4/ping_group_range</i> sysctl range to match any group of the user.<br />
 Options:</p>
<dl>
<dt><code>raw</code></p>
<dd>Use only raw sockets (the traditional way).<br />
 This way is tried first by default (for compatibility reasons), then new dgram icmp sockets as fallback.</p>
<dt><code>dgram</code></p>
<dd>Use only dgram icmp sockets.</dl>
<h3>tcp &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr>-T</h3>
<p>Well-known modern method, intended to bypass firewalls.<br />
 Uses the constant destination port (default is 80, http). </p>
<p> If some filters are present in the network path, then most probably any &quot;unlikely&quot; udp ports (as for <i>default</i> method) or even icmp echoes (as for <i>icmp</i>) are filtered, and whole tracerouting will just stop at such a firewall. To bypass a network filter, we have to use only allowed protocol/port combinations. If we trace for some, say, mailserver, then more likely <code>-T -p 25</code> can reach it, even when <code>-I</code> can not. </p>
<p> This method uses well-known &quot;half-open technique&quot;, which prevents applications on the destination host from seeing our probes at all. Normally, a tcp syn is sent. For non-listened ports we receive tcp reset, and all is done. For active listening ports we receive tcp syn+ack, but answer by tcp reset (instead of expected tcp ack), this way the remote tcp session is dropped even without the application ever taking notice. </p>
<p> There is a couple of options for <i>tcp</i> method:</p>
<dl>
<dt><code>syn,ack,fin,rst,psh,urg,ece,cwr</code></p>
<dd>Sets specified tcp flags for probe packet, in any combination.</p>
<dt><code>flags</code>=<i>num</i></p>
<dd>Sets the flags field in the tcp header exactly to <i>num</i>.</p>
<dt><code>ecn</code></p>
<dd>Send syn packet with tcp flags ECE and CWR (for Explicit Congestion Notification, rfc3168).</p>
<dt><code>sack,timestamps,window_scaling</code></p>
<dd>Use the corresponding tcp header option in the outgoing probe packet.</p>
<dt><code>sysctl</code></p>
<dd>Use current sysctl <i></i>(<i>/proc/sys/net/*</i>) setting for the tcp header options above and <code>ecn</code>. Always set by default, if nothing else specified.</p>
<dt><code>mss</code>=<i>num</i></p>
<dd>Use value of <i>num</i> for maxseg tcp header option (when <code>syn</code>).</p>
<dt><code>info</code></p>
<dd>Print tcp flags of final tcp replies when the target host is reached. Allows to determine whether an application listens the port and other useful things.</dl>
<p> Default options is <code>syn,sysctl</code>.</p>
<h3>tcpconn</h3>
<p>An initial implementation of tcp method, simple using <a href="/docs/linux/man/2-connect/">connect</a>(2) call, which does full tcp session opening. Not recommended for normal use, because a destination application is always affected (and can be confused).</p>
<h3>udp &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr>-U</h3>
<p>Use udp datagram with constant destination port (default 53, dns).<br />
 Intended to bypass firewall as well. </p>
<p> Note, that unlike in <i>tcp</i> method, the correspond application on the destination host <code>always</code> receive our probes (with random data), and most can easily be confused by them. Most cases it will not respond to our packets though, so we will never see the final hop in the trace. (Fortunately, it seems that at least dns servers replies with something angry). </p>
<p> This method is allowed for unprivileged users.</p>
<h3>udplite &nbsp;<wbr> &nbsp;<wbr>-UL</h3>
<p>Use udplite datagram for probes (with constant destination port, default 53). </p>
<p> This method is allowed for unprivileged users.<br />
 Options:</p>
<dl>
<dt><code>coverage</code>=<i>num</i></p>
<dd>Set udplite send coverage to <i>num</i>.</dl>
<h3>dccp &nbsp;<wbr> &nbsp;<wbr>-D</h3>
<p>Use DCCP Request packets for probes (rfc4340). </p>
<p> This method uses the same &quot;half-open technique&quot; as used for TCP. The default destination port is 33434. </p>
<p> Options:</p>
<dl>
<dt><code>service</code>=<i>num</i></p>
<dd>Set DCCP service code to <i>num</i> (default is 1885957735).</dl>
<h3>raw &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr> &nbsp;<wbr>-P proto</h3>
<p>Send raw packet of protocol <i>proto</i>.<br />
 No protocol-specific headers are used, just IP header only.<br />
 Implies <code>-N 1</code>.<br />
 Options:</p>
<dl>
<dt><code>protocol</code>=<i>proto</i></p>
<dd>Use IP protocol <i>proto</i> (default 253).</dl>
<h2>Notes</h2>
<p>To speed up work, normally several probes are sent simultaneously. On the other hand, it creates a &quot;storm of packages&quot;, especially in the reply direction. Routers can throttle the rate of icmp responses, and some of replies can be lost. To avoid this, decrease the number of simultaneous probes, or even set it to 1 (like in initial traceroute implementation), i.e. <code>-N 1</code> </p>
<p> The final (target) host can drop some of the simultaneous probes, and might even answer only the latest ones. It can lead to extra &quot;looks like expired&quot; hops near the final hop. We use a smart algorithm to auto-detect such a situation, but if it cannot help in your case, just use <code>-N 1</code> too. </p>
<p> For even greater stability you can slow down the program&#8217;s work by <code>-z</code> option, for example use <code>-z 0.5</code> for half-second pause between probes. </p>
<p> If some hops report nothing for every method, the last chance to obtain something is to use <code>ping -R</code> command (IPv4, and for nearest 8 hops only).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ping/">ping</a></code>(8), <code><a href="/docs/linux/man/8-ping6/">ping6</a></code>(8), <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8) </p>
