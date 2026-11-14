---
title: "dhcrelay(8)"
name: "dhcrelay"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcrelay/"
description: "dhcrelay – Dynamic Host Configuration Protocol Relay Agent"
---

<p>dhcrelay &#8211; Dynamic Host Configuration Protocol Relay Agent</p>
<h2>Synopsis</h2>
<p><code>dhcrelay</code> [ <code>-4</code> ] [ <code>-dqaD</code> ] [ <code>-p</code> <i>port</i> ] [ <code>-c</code> <i>count</i> ] [ <code>-A</code> <i>length</i> ] [ <code>-pf</code> <i>pid-file</i> ] [ <code>&#8211;no-pid</code> ] [ <code>-m</code> <i>append</i> | <i>replace</i> | <i>forward</i> | <i>discard</i> ] [ <code>-i</code> <i>interface0</i> [ <code>&#8230;</code> <code>-i</code> <i>interfaceN </i> ] ] <i>server0</i> [ <i>&#8230;serverN</i> ] </p>
<p> <code>dhcrelay -6</code> [ <code>-dqI</code> ] [ <code>-p</code> <i>port</i> ] [ <code>-c</code> <i>count</i> ] [ <code>-pf</code> <i>pid-file</i> ] [ <code>&#8211;no-pid</code> ] <code>-l</code> <i>lower0</i> [ <code>&#8230;</code> <code>-l</code> <i>lowerN</i> ] <code>-u</code> <i>upper0 </i> [ <code>&#8230;</code> <code>-u</code> <i>upperN</i> ]</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP Relay Agent, dhcrelay, provides a means for relaying DHCP and BOOTP requests from a subnet to which no DHCP server is directly connected to one or more DHCP servers on other subnets. It supports both DHCPv4/BOOTP and DHCPv6 protocols.</p>
<h2>Operation</h2>
<p>The DHCP Relay Agent listens for DHCPv4 or DHCPv6 queries from clients or other relay agents on one or more interfaces, passing them along to &#8220;upstream&#8221; servers or relay agents as specified on the command line. When a reply is received from upstream, it is multicast or unicast back downstream to the source of the original request.</p>
<h2>Command Line</h2>
<p><i>Protocol selection options:</i></p>
<dl>
<dt>-6</p>
<dd>Run dhcrelay as a DHCPv6 relay agent. Incompatible with the <code>-4</code> option.</p>
<dt>-4</p>
<dd>Run dhcrelay as a DHCPv4/BOOTP relay agent. This is the default mode of operation, so the argument is not necessary, but may be specified for clarity. Incompatible with <code>-6</code>.</dl>
<p> <i>Specifying DHCPv4/BOOTP servers</i> </p>
<p> In DHCPv4 mode, a list of one or more server addresses must be specified on the command line, to which DHCP/BOOTP queries should be relayed. </p>
<p> <i>Options available for both DHCPv4 and DHCPv6:</i></p>
<dl>
<dt>-c COUNT</p>
<dd>Maximum hop count. When forwarding packets, dhcrelay discards packets which have reached a hop count of COUNT. Default is 10. Maximum is 255.</p>
<dt>-d</p>
<dd>Force dhcrelay to run as a foreground process. Useful when running dhcrelay under a debugger, or running out of inittab on System V systems.</p>
<dt>-p PORT</p>
<dd>Listen and transmit on port PORT. This is mostly useful for debugging purposes. Default is port 67 for DHCPv4/BOOTP, or port 547 for DHCPv6.</p>
<dt>-q</p>
<dd>Quiet mode. Prevents dhcrelay6 from printing its network configuration on startup.</p>
<dt>-pf pid-file</p>
<dd>Path to alternate pid file.</p>
<dt>&#8211;no-pid</p>
<dd>Option to disable writing pid files. By default the program will write a pid file.</dl>
<p> <i>Options available in DHCPv4 mode only:</i></p>
<dl>
<dt>-a</p>
<dd>Append an agent option field to each request before forwarding it to the server. Agent option fields in responses sent from servers to clients will be stripped before forwarding such responses back to the client. The agent option field will contain two agent options: the Circuit ID suboption and the Remote ID suboption. Currently, the Circuit ID will be the printable name of the interface on which the client request was received. The client supports inclusion of a Remote ID suboption as well, but this is not used by default.</p>
<dt>-A LENGTH</p>
<dd>Specify the maximum packet size to send to a DHCPv4/BOOTP server. This might be done to allow sufficient space for addition of relay agent options while still fitting into the Ethernet MTU size.</p>
<dt>-D</p>
<dd>Drop packets from upstream servers if they contain Relay Agent Information options that indicate they were generated in response to a query that came via a different relay agent. If this option is not specified, such packets will be relayed anyway.</p>
<dt>-i <i>ifname</i></p>
<dd>Listen for DHCPv4/BOOTP queries on interface <i>ifname</i>. Multiple interfaces may be specified by using more than one <code>-i</code> option. If no interfaces are specified on the command line, dhcrelay will identify all network interfaces, eliminating non-broadcast interfaces if possible, and attempt to listen on all of them.</p>
<dt>-m <i>append</i>|<i>replace</i>|<i>forward</i>|<i>discard</i></p>
<dd>Control the handling of incoming DHCPv4 packets which already contain relay agent options. If such a packet does not have <i>giaddr</i> set in its header, the DHCP standard requires that the packet be discarded. However, if <i>giaddr</i> is set, the relay agent may handle the situation in four ways: It may <i>append</i> its own set of relay options to the packet, leaving the supplied option field intact; it may <i>replace</i> the existing agent option field; it may <i>forward</i> the packet unchanged; or, it may <i>discard</i> it. </p>
<p> To use this option you must also enable the <code>-a</code> option.</dl>
<p> <i>Options available in DHCPv6 mode only:</i></p>
<dl>
<dt>-I</p>
<dd>Force use of the DHCPv6 Interface-ID option. This option is automatically sent when there are two or more downstream interfaces in use, to disambiguate between them. The <code>-I</code> option causes dhcrelay to send the option even if there is only one downstream interface.</p>
<dt>-l [<i>address%</i>]<i>ifname</i>[<i>#index</i>]</p>
<dd>Specifies the &#8220;lower&#8221; network interface for DHCPv6 relay mode: the interface on which queries will be received from clients or from other relay agents. At least one <code>-l</code> option must be included in the command line when running in DHCPv6 mode. The interface name <i>ifname</i> is a mandatory parameter. The link address can be specified by <i>address%</i>; if it isn&#8217;t, dhcrelay will use the first non-link-local address configured on the interface. The optional <i>#index</i> parameter specifies the interface index.</p>
<dt>-u [<i>address%</i>]<i>ifname</i></p>
<dd>Specifies the &#8220;upper&#8221; network interface for DHCPv6 relay mode: the interface to which queries from clients and other relay agents should be forwarded. At least one <code>-u</code> option must be included in the command line when running in DHCPv6 mode. The interface name <i>ifname</i> is a mandatory parameter. The destination unicast or multicast address can be specified by <i>address%</i>; if not specified, the relay agent will forward to the DHCPv6 <i>All_DHCP_Relay_Agents_and_Servers</i> multicast address.</dl>
<p> It is possible to specify the same interface with different addresses more than once, and even, when the system supports it, to use the same interface as both upper and lower interfaces.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), RFC3315, RFC2132, RFC2131.</p>
<h2>Bugs</h2>
<p>Using the same interface on both upper and lower sides may cause loops, so when running this way, the maximum hop count should be set to a low value. </p>
<p> The loopback interface is not (yet) recognized as a valid interface.</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhcrelay/">dhcrelay</a>(8)</code> To learn more about Internet Systems Consortium, see <code><a rel="nofollow" href="https://www.isc.org">https://www.isc.org</a></code></p>
