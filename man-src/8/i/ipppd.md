---
title: "ipppd(8)"
name: "ipppd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipppd/"
description: "ipppd – (ISDN) Point to Point Protocol daemon"
---

<p>ipppd &#8211; (ISDN) Point to Point Protocol daemon</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/ipppd</code> [ <i>options</i> ] [ <i>device</i> ]</p>
<h2>Description</h2>
<p>The Point-to-Point Protocol (PPP) provides a method for transmitting datagrams over serial point-to-point links. PPP is composed of three parts: a method for encapsulating datagrams over serial links, an extensible Link Control Protocol (LCP), and a family of Network Control Protocols (NCP) for establishing and configuring different network-layer protocols. </p>
<p> The encapsulation scheme is provided by driver code in the kernel. <i>ipppd</i> provides the basic LCP, authentication support, and an NCP for establishing and configuring the Internet Protocol (IP) (called the IP Control Protocol, IPCP).</p>
<h2>NOTES for (ISDN) IPPPD</h2>
<p>This special (ISDN) PPP daemon is a modified version of pppd and provides synchronous PPP for ISDN connections. </p>
<p> If you need asynchronous PPP over ISDN lines use pppd instead with the ISDN character devices, see <code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4). </p>
<p> The <i>ipppd </i> can handle multiple devices. This is necessary to link several connections together to one bundle. <i>ipppd </i> should be started once. It opens the devices and waits for connections. If the connections is closed <i>ipppd</i> reopens the device automatically (the device, that&#8217;s it &#8230; not the link to the remote). So you shouldn&#8217;t kill the ipppd to close a link. Instead, trigger a hangup on the netdevice layer by &#8216;isdnctrl hangup &lt;device&gt;&#8217;. </p>
<p> The facility to configure the daemon via file /etc/ppp/ioptions.&lt;devname&gt; is disabled. The &#8216;file&#8217; option or the command line may be used for individual configuration. </p>
<p> Do not set the permissions of the program to &#8216;setuid to root on execution&#8217;. Call the daemon as root instead. No common user should have the need to call the daemon!</p>
<h2>Options</h2>
<dl>
<dt><i>&lt;device&gt;</i></p>
<dd>Communicate over the named device. The string &quot;/dev/&quot; is prepended if necessary. If no device name is given, or if the name of the controlling terminal is given, <i>ipppd</i> will use the controlling terminal, and will not fork to put itself in the background.</p>
<dt><i>&lt;local_IP_address&gt;</i><code>:</code><i>&lt;remote_IP_address&gt;</i></p>
<dd>Set the local and/or remote interface IP addresses. Either one may be omitted. The IP addresses can be specified with a host name or in decimal dot notation (e.g. 150.234.56.78). The default local address is the (first) IP address of the system (unless the <code>noipdefault</code> option is given). The remote address will be obtained from the peer if not specified in any option. Thus, in simple cases, this option is not required. If a local and/or remote IP address is specified with this option, <i>ipppd</i> will not accept a different value from the peer in the IPCP negotiation, unless the <code>ipcp-accept-local</code> and/or <code>ipcp-accept-remote</code> options are given, respectively.</p>
<dt><code>active-filter </code><i>filter-expression</i></p>
<dd>Specifies a packet filter to be applied to data packets to determine which packets are to be regarded as link activity, and therefore reset the idle timer, or cause the link to be brought up in demand-dialling mode. This option is useful in conjunction with the <code>idle</code> option if there are packets being sent or received regularly over the link (for example, routing information packets) which would otherwise prevent the link from ever appearing to be idle. The <i>filter-expression</i> syntax is as described for <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1), except that qualifiers which are inappropriate for a PPP link, such as <code>ether</code> and <code>arp</code>, are not permitted. Generally the filter expression should be enclosed in single-quotes to prevent whitespace in the expression from being interpreted by the shell. This option is currently only available if both the kernel and ipppd were compiled with IPPP_FILTER defined.</p>
<dt><code>-ac</code></p>
<dd>Disable Address/Control compression negotiation (use default, i.e. address/control field compression disabled).</p>
<dt><code>-all</code></p>
<dd>Don&#8217;t request or allow negotiation of any options for LCP and IPCP (use default values).</p>
<dt><code>auth</code></p>
<dd>Require the peer to authenticate itself before allowing network packets to be sent or received.</p>
<dt><code>bsdcomp </code><i>nr,nt</i></p>
<dd>Request that the peer compress packets that it sends, using the BSD-Compress scheme, with a maximum code size of <i>nr</i> bits, and agree to compress packets sent to the peer with a maximum code size of <i>nt</i> bits. If <i>nt</i> is not specified, it defaults to the value given for <i>nr</i>. Values in the range 9 to 15 may be used for <i>nr</i> and <i>nt</i>; larger values give better compression but consume more kernel memory for compression dictionaries. Alternatively, a value of 0 for <i>nr</i> or <i>nt</i> disables compression in the corresponding direction.</p>
<dt><code>-bsdcomp</code></p>
<dd>Disables compression; <i>ipppd</i> will not request or agree to compress packets using the BSD-Compress scheme.</p>
<dt><code>callback </code><i>&lt;string&gt;</i></p>
<dd>Request the peer to call back at the location given in &lt;string&gt;. Usually this is a phone number, but it may be interpreted differently (or ignored) depending on the <code>callback-type</code> option. If &lt;string&gt; is the empty string, <i>ipppd</i> automatically tries to negotiate a callback type that does not need a location to be specified.</p>
<dt><code>callback-delay </code><i>&lt;n&gt;</i></p>
<dd>Callback delay for CBCP in seconds. If callback is negotiated using CBCP, request that the peer waits at least &lt;n&gt; seconds before calling back. Ignored if callback is negotiated as specified in RFC 1570. Legal range is 0..255, default is 5.</p>
<dt><code>callback-cbcp</code></p>
<dd>Enable callback negotiation via CBCB (default).</p>
<dt><code>-callback-cbcp</code></p>
<dd>Disable callback negotiation via CBCB.</p>
<dt><code>no-callback-cbcp</code></p>
<dd>Disable callback negotiation via CBCB.</p>
<dt><code>callback-cbcp-preferred</code></p>
<dd>If both CBCP and RFC 1570 style callback negotiation is enabled, CBCP is preferred (default)</p>
<dt><code>callback-rfc1570-preferred</code></p>
<dd>If both CBCP and RFC 1570 style callback negotiation is enabled, RFC 1570 style is preferred.</p>
<dt><code>callback-rfc1570</code></p>
<dd>Enable RFC 1570 style callback negotiation (default).</p>
<dt><code>-callback-rfc1570</code></p>
<dd>Disable RFC 1570 style callback negotiation.</p>
<dt><code>no-callback-rfc1570</code></p>
<dd>Disable RFC 1570 style callback negotiation (default).</p>
<dt><code>callback-type </code><i>&lt;n&gt;</i></p>
<dd>Specifies how to interpret the location identifier given as parameter of the <code>callback</code> option. Legal values are 0..4. A value of 0 means that only callback types should be negotiated that need no extra location id. No location id is sent to the peer in this case. For RFC 1570 style callback negotiation, the values 1..4 indicate how the peer should interpret the location identifier: 1 &#8211; id is a system specific dial string, 2 &#8211; id is used for database lookup by the peer, 3 &#8211; id is a phone number, and 4 id is a name. For CBCP callback negotiation, the location id is always interpreted as a phone number.</p>
<dt><code>-ccp</code></p>
<dd>Necessary for a few netblazers on the remote side.</p>
<dt><code>noccp</code></p>
<dd>same as <code>-ccp</code></p>
<dt><code>+chap</code></p>
<dd>Require the peer to authenticate itself using CHAP [Cryptographic Handshake Authentication Protocol] authentication.</p>
<dt><code>-chap</code></p>
<dd>Don&#8217;t agree to authenticate using CHAP.</p>
<dt><code>chap-interval </code><i>&lt;n&gt;</i></p>
<dd>If this option is given, <i>ipppd</i> will rechallenge the peer every &lt;n&gt; seconds.</p>
<dt><code>chap-max-challenge </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of CHAP challenge transmissions to &lt;n&gt; (default 10).</p>
<dt><code>chap-restart </code><i>&lt;n&gt;</i></p>
<dd>Set the CHAP restart interval (retransmission timeout for challenges) to &lt;n&gt; seconds (default 3).</p>
<dt><code>debug</code></p>
<dd>Increase debugging level (same as <code>-d</code>). If this option is given, <i>ipppd</i> will log the contents of all control packets sent or received in a readable form. The packets are logged through syslog with facility <i>daemon</i> and level <i>debug</i>. This information can be directed to a file by setting up /etc/syslog.conf appropriately (see <a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5)).</p>
<dt><code>-d</code></p>
<dd>Increase debugging level (same as the <code>debug</code> option).</p>
<dt><code>defaultroute</code></p>
<dd>Add a default route to the system routing tables, using the peer as the gateway, when IPCP negotiation is successfully completed. This entry is removed when the PPP connection is broken.</p>
<dt><code>-defaultroute</code></p>
<dd>Disable the <code>defaultroute</code> option. The system administrator who wishes to prevent users from creating default routes with <i>ipppd</i> can do so by placing this option in the /etc/ppp/ioptions file.</p>
<dt><code>deldefaultroute</code></p>
<dd>Replace default route if it already exists. Together with the option <code>defaultroute</code>, this will replace any existing default route by a new one through this ipppd&#8217;s interface when it comes up.</p>
<dt><code>-detach</code></p>
<dd>Don&#8217;t fork to become a background process (otherwise <i>ipppd</i> will do so if a serial device other than its controlling terminal is specified).</p>
<dt><code>domain </code><i>&lt;d&gt;</i></p>
<dd>Append the domain name &lt;d&gt; to the local host name for authentication purposes. For example, if gethostname() returns the name porsche, but the fully qualified domain name is porsche.Quotron.COM, you would use the domain option to set the domain name to Quotron.COM.</p>
<dt><code>file </code><i>&lt;f&gt;</i></p>
<dd>Read options from file &lt;f&gt; (the format is described below).</p>
<dt><code>-ip</code></p>
<dd>Disable IP address negotiation. If this option is used, the remote IP address must be specified with an option on the command line or in an options file.</p>
<dt><code>+ip-protocol</code></p>
<dd>Enable the IPCP and IP protocols. This is the default condition. This option is only needed if the default setting is -ip-protocol.</p>
<dt><code>-ip-protocol</code></p>
<dd>Disable the IPCP and IP protocols. This should only be used if you know that you are using a client which only understands IPX and you don&#8217;t want to confuse the client with the IPCP protocol.</p>
<dt><code>+ipx-protocol</code></p>
<dd>Enable the IPXCP and IPX protocols. This is the default condition if your kernel supports IPX. This option is only needed if the default setting is -ipx-protocol. If your kernel does not support IPX then this option will have no effect.</p>
<dt><code>-ipx-protocol</code></p>
<dd>Disable the IPXCP and IPX protocols. This should only be used if you know that you are using a client which only understands IP and you don&#8217;t want to confuse the client with the IPXCP protocol.</p>
<dt><code>ipcp-accept-local</code></p>
<dd>With this option, <i>ipppd</i> will accept the peer&#8217;s idea of our local IP address, even if the local IP address was specified in an option.</p>
<dt><code>ipcp-accept-remote</code></p>
<dd>With this option, <i>ipppd</i> will accept the peer&#8217;s idea of its (remote) IP address, even if the remote IP address was specified in an option.</p>
<dt><code>ipcp-max-configure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPCP configure-request transmissions to &lt;n&gt; (default 10).</p>
<dt><code>ipcp-max-failure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPCP configure-NAKs returned before starting to send configure-Rejects instead to &lt;n&gt; (default 10).</p>
<dt><code>ipcp-max-terminate </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPCP terminate-request transmissions to &lt;n&gt; (default 3).</p>
<dt><code>ipcp-restart </code><i>&lt;n&gt;</i></p>
<dd>Set the IPCP restart interval (retransmission timeout) to &lt;n&gt; seconds (default 3).</p>
<dt><code>ipparam </code><i>string</i></p>
<dd>Provides an extra parameter to the ip-up and ip-down scripts. If this option is given, the <i>string</i> supplied is given as the 6th parameter to those scripts.</p>
<dt><code>ipx-network </code><i>&lt;n&gt;</i></p>
<dd>Set the IPX network number in the IPXCP configure request frame to &lt;n&gt;. There is no valid default. If this option is not specified then the network number is obtained from the peer. If the peer does not have the network number, the IPX protocol will not be started. This is a hexadecimal number and is entered without any leading sequence such as 0x. It is related to the <i>ipxcp-accept-network</i> option.</p>
<dt><code>ipx-node </code><i>&lt;n&gt;:&lt;m&gt;</i></p>
<dd>Set the IPX node numbers. The two node numbers are separated from each other with a colon character. The first number &lt;n&gt; is the local node number. The second number &lt;m&gt; is the peer&#8217;s node number. Each node number is a hexadecimal number, to the maximum of ten significant digits. The node numbers on the ipx-network must be unique. There is no valid default. If this option is not specified then the node number is obtained from the peer. This option is a related to the <i>ipxcp-accept-local</i> and <i>ipxcp-accept-remote</i> options.</p>
<dt><code>ipx-router-name </code><i>&lt;string&gt;</i></p>
<dd>Set the name of the router. This is a string and is sent to the peer as information data.</p>
<dt><code>ipx-routing </code><i>&lt;n&gt;</i></p>
<dd>Set the routing protocol to be received by this option. Use a comma-separated list if you want to specify more than one protocol. The &#8216;<i>none</i>&#8216; option (0) may be specified as the only instance of ipx-routing. The values may be <i>0</i> for <i>NONE</i>, <i>2</i> for <i>RIP/SAP</i>, and <i>4</i> for <i>NLSP</i>.</p>
<dt><code>ipxcp-accept-local</code></p>
<dd>Accept the peer&#8217;s NAK for the node number specified in the ipx-node option. If a node number was specified, and non-zero, the default is to insist that the value be used. If you include this option then you will permit the peer to override the entry of the node number.</p>
<dt><code>ipxcp-accept-network</code></p>
<dd>Accept the peer&#8217;s NAK for the network number specified in the ipx-network option. If a network number was specified, and non-zero, the default is to insist that the value be used. If you include this option then you will permit the peer to override the entry of the node number.</p>
<dt><code>ipxcp-accept-remote</code></p>
<dd>Use the peer&#8217;s network number specified in the configure request frame. If a node number was specified for the peer and this option was not specified, the peer will be forced to use the value which you have specified.</p>
<dt><code>ipxcp-max-configure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPXCP configure request frames which the system will send to &lt;n&gt;. The default is 10.</p>
<dt><code>ipxcp-max-failure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPXCP NAK frames which the local system will send before it rejects the options. The default value is 3.</p>
<dt><code>ipxcp-max-terminate </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of IPXCP terminate request frames before the local system considers that the peer is not listening to them. The default value is 3.</p>
<dt><code>kdebug </code><i>n</i></p>
<dd>Enable debugging code in the kernel-level PPP driver. The argument <i>n</i> is a number which is the sum of the following values: 1 to enable general debug messages, 2 to request that the contents of received packets be printed, and 4 to request that the contents of transmitted packets be printed.</p>
<dt><code>lcp-echo-failure </code><i>&lt;n&gt;</i></p>
<dd>If this option is given, <i>ipppd</i> will presume the peer to be dead if <i>n</i> LCP echo-requests are sent without receiving a valid LCP echo-reply. If this happens, <i>ipppd</i> will terminate the connection. Use of this option requires a non-zero value for the <code>lcp-echo-interval</code> parameter. This option can be used to enable <i>ipppd</i> to terminate after the physical connection has been broken (e.g., the line hung up) in situations where no hardware modem control lines are available.</p>
<dt><code>lcp-echo-interval </code><i>&lt;n&gt;</i></p>
<dd>If this option is given, <i>ipppd</i> will send an LCP echo-request frame to the peer every <i>n</i> seconds. With Linux, the echo-request is sent when no packets have been received from the peer for <i>n</i> seconds. Normally the peer should respond to the echo-request by sending an echo-reply. This option can be used with the <code>lcp-echo-failure</code> option to detect that the peer is no longer connected.</p>
<dt><code>lcp-max-configure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of LCP configure-request transmissions to &lt;n&gt; (default 10).</p>
<dt><code>lcp-max-failure </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of LCP configure-NAKs returned before starting to send configure-Rejects instead to &lt;n&gt; (default 10).</p>
<dt><code>lcp-max-terminate </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of LCP terminate-request transmissions to &lt;n&gt; (default 3).</p>
<dt><code>lcp-restart </code><i>&lt;n&gt;</i></p>
<dd>Set the LCP restart interval (retransmission timeout) to &lt;n&gt; seconds (default 3).</p>
<dt><code>lock</code></p>
<dd>Specifies that <i>ipppd</i> should create a UUCP-style lock file for the serial device to ensure exclusive access to the device.</p>
<dt><code>login</code></p>
<dd>Use the system password database for authenticating the peer using PAP, and record the user in the system wtmp file.</p>
<dt><code>-mn</code></p>
<dd>Disable magic number negotiation. With this option, <i>ipppd</i> cannot detect a looped-back line.</p>
<dt><code>+mp</code></p>
<dd>enables MPPP negotiation</p>
<dt><code>mru </code><i>&lt;n&gt;</i></p>
<dd>Set the MRU [Maximum Receive Unit] value to &lt;n&gt; for negotiation. <i>ipppd</i> will ask the peer to send packets of no more than &lt;n&gt; bytes. The minimum MRU value is 128. The default MRU value is 1500. A value of 296 is recommended for slow links (40 bytes for TCP/IP header + 256 bytes of data).</p>
<dt><code>-mru</code></p>
<dd>Disable MRU [Maximum Receive Unit] negotiation. With this option, <i>ipppd</i> will use the default MRU value of 1500 bytes.</p>
<dt><code>ms-dns </code><i>&lt;n&gt;</i></p>
<dd>This option sets the IP address or addresses for the Domain Name Server. It is used by Microsoft Windows clients. The primary DNS address is specified by the first instance of the ms-dns option. The secondary is specified by the second instance.</p>
<dt><code>ms-get-dns</code></p>
<dd>Implements the client side of RFC1877. If <i>ipppd</i> is acting as a client to a server that implements RFC1877 such as one intended to be used with Microsoft Windows clients, this option allows <i>ipppd</i> to obtain one or two DNS (Domain Name Server) addresses from the server. It does not do anything with these addresses except put them in the environment (MS_DNS1 MS_DNS2) that is passed to scripts. For compatibility with the async pppd, DNS1 DNS2 environment variables are also set. A sample resolv.conf is created in /etc/ppp/resolv.conf. The /etc/ppp/ip-up script should use this information to perform whatever adjustment is necessary. Note: RFC1877 is a horrible protocol layering violation, the correct approach would be to use DHCP after the IPCP phase.</p>
<dt><code>ms-get-wins</code></p>
<dd>As ms-get-dns but for WINS (Windows Internet Name Services) server addresses. Environment variables are MS_WINS1 and MS_WINS2.</p>
<dt><code>mtu </code><i>&lt;n&gt;</i></p>
<dd>Set the MTU [Maximum Transmit Unit] value to <i>&lt;n&gt;</i>. Unless the peer requests a smaller value via MRU negotiation, <i>ipppd</i> will request that the kernel networking code send data packets of no more than <i>n</i> bytes through the PPP network interface.</p>
<dt><code>name </code><i>&lt;n&gt;</i></p>
<dd>Set the name of the local system for authentication purposes to &lt;n&gt;.</p>
<dt><code>netmask </code><i>&lt;n&gt;</i></p>
<dd>Set the interface netmask to &lt;n&gt;, a 32 bit netmask in &quot;decimal dot&quot; notation (e.g. 255.255.255.0). If this option is given, the value specified is ORed with the default netmask. The default netmask is chosen based on the negotiated remote IP address; it is the appropriate network mask for the class of the remote IP address, ORed with the netmasks for any non point-to-point network interfaces in the system which are on the same network.</p>
<dt><code>noipdefault</code></p>
<dd>Disables the default behaviour when no local IP address is specified, which is to determine (if possible) the local IP address from the hostname. With this option, the peer will have to supply the local IP address during IPCP negotiation (unless it specified explicitly on the command line or in an options file).</p>
<dt><code>passive</code></p>
<dd>Enables the &quot;passive&quot; option in the LCP. With this option, <i>ipppd</i> will attempt to initiate a connection; if no reply is received from the peer, <i>ipppd</i> will then just wait passively for a valid LCP packet from the peer (instead of exiting, as it does without this option).</p>
<dt><code>-p</code></p>
<dd>Same as the <code>passive</code> option.</p>
<dt><code>+pap</code></p>
<dd>Require the peer to authenticate itself using PAP.</p>
<dt><code>-pap</code></p>
<dd>Don&#8217;t agree to authenticate using PAP.</p>
<dt><code>papcrypt</code></p>
<dd>Indicates that all secrets in the /etc/ppp/pap-secrets file which are used for checking the identity of the peer are encrypted, and thus <i>ipppd </i> should not accept a password which (before encryption) is identical to the secret from the /etc/ppp/pap-secrets file.</p>
<dt><code>pap-max-authreq </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum number of PAP authenticate-request transmissions to &lt;n&gt; (default 10).</p>
<dt><code>pap-restart </code><i>&lt;n&gt;</i></p>
<dd>Set the PAP restart interval (retransmission timeout) to &lt;n&gt; seconds (default 3).</p>
<dt><code>pap-timeout </code><i>&lt;n&gt;</i></p>
<dd>Set the maximum time that <i>ipppd</i> will wait for the peer to authenticate itself with PAP to &lt;n&gt; seconds (0 means no limit).</p>
<dt><code>pass-filter </code><i>filter-expression</i></p>
<dd>Specifies a packet filter to applied to data packets being sent or received to determine which packets should be allowed to pass. Packets which are rejected by the filter are silently discarded. This option can be used to prevent specific network daemons (such as routed) using up link bandwidth, or to provide a basic firewall capability. The <i>filter-expression</i> syntax is as described for <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1), except that qualifiers which are inappropriate for a PPP link, such as <code>ether</code> and <code>arp</code>, are not permitted. Generally the filter expression should be enclosed in single-quotes to prevent whitespace in the expression from being interpreted by the shell. Note that it is possible to apply different constraints to incoming and outgoing packets using the <code>inbound</code> and <code>outbound</code> qualifiers. This option is currently only available if both the kernel and ipppd were compiled with IPPP_FILTER defined.</p>
<dt><code>-pc</code></p>
<dd>Disable protocol field compression negotiation (use default, i.e. protocol field compression disabled).</p>
<dt><code>pidfile &lt;filename&gt;</code></p>
<dd>Use &lt;filename&gt; instead of <i>/var/run/ipppd.pid</i></p>
<dt><code>pred1comp</code></p>
<dd>Attempt to request that the peer send the local system frames which have been compressed by the Predictor-1 compression. The compression protocols must be loaded or this option will be ignored.</p>
<dt><code>-pred1comp</code></p>
<dd>Do not accept Predictor-1 compression, even if the peer wants to send this type of compression and support has been defined in the kernel.</p>
<dt><code>proxyarp</code></p>
<dd>Add an entry to this system&#8217;s ARP [Address Resolution Protocol] table with the IP address of the peer and the Ethernet address of this system.</p>
<dt><code>-proxyarp</code></p>
<dd>Disable the <code>proxyarp</code> option. The system administrator who wishes to prevent users from creating proxy ARP entries with <i>ipppd</i> can do so by placing this option in the /etc/ppp/ioptions file.</p>
<dt><code>remotename </code><i>&lt;n&gt;</i></p>
<dd>Set the assumed name of the remote system for authentication purposes to &lt;n&gt;.</p>
<dt><code>set_userip</code></p>
<dd>You may define valid IPs in <i>/etc/ppp/useriptab</i></p>
<dt><code>silent</code></p>
<dd>With this option, <i>ipppd</i> will not transmit LCP packets to initiate a connection until a valid LCP packet is received from the peer (as for the `passive&#8217; option with ancient versions of <i>ipppd</i>).</p>
<dt><code>+ua </code><i>&lt;p&gt;</i></p>
<dd>Agree to authenticate using PAP [Password Authentication Protocol] if requested by the peer, and use the data in file &lt;p&gt; for the user and password to send to the peer. The file contains the remote user name, followed by a newline, followed by the remote password, followed by a newline. This option is obsolescent.</p>
<dt><code>usefirstip</code></p>
<dd>Gets the remote address from the first entry in the auth file (if there is an IP address entry). This address should be a full IP address not an address from a masked area. Ipppd calls &#8216;gethostbyname()&#8217; and negotiates the result. IP from auth file will overwrite the remote address gotten from the interface. &#8216;usefirstip&#8217; is UNTESTED!</p>
<dt><code>usehostname</code></p>
<dd>Enforce the use of the hostname as the name of the local system for authentication purposes (overrides the <code>name</code> option).</p>
<dt><code>usepeerdns</code></p>
<dd>Same as <code>ms-get-dns</code> for compatibility with async pppd.</p>
<dt><code>user </code><i>&lt;u&gt;</i></p>
<dd>Set the user name to use for authenticating this machine with the peer using PAP to &lt;u&gt;.</p>
<dt><code>useifip</code></p>
<dd>will get (if not set to 0.0.0.0) the IP address for the negotiation from the attached network-interface. (also: <i>ipppd</i> will try to negotiate &#8216;pointopoint&#8217; IP as remote IP) interface address -&gt; local IP pointopoint address -&gt; remote IP</p>
<dt><code>-vj</code></p>
<dd>Disable negotiation of Van Jacobson style TCP/IP header compression (use default, i.e. no compression).</p>
<dt><code>-vjccomp</code></p>
<dd>Disable the connection-ID compression option in Van Jacobson style TCP/IP header compression. With this option, <i>ipppd</i> will not omit the connection-ID byte from Van Jacobson compressed TCP/IP headers, nor ask the peer to do so.</p>
<dt><code>vj-max-slots </code><i>n</i></p>
<dd>Sets the number of connection slots to be used by the Van Jacobson TCP/IP header compression and decompression code to <i>n</i>, which must be between 2 and 16 (inclusive).</dl>
<h2>Options Files</h2>
<p>Options can be taken from files as well as the command line. <i>ipppd</i> reads options from the file /etc/ppp/ioptions before looking at the command line. An options file is parsed into a series of words, delimited by whitespace. Whitespace can be included in a word by enclosing the word in quotes (&quot;). A backslash (\) quotes the following character. A hash (#) starts a comment, which continues until the end of the line.</p>
<h2>Authentication</h2>
<p><i>ipppd</i> provides system administrators with sufficient access control that PPP access to a server machine can be provided to legitimate users without fear of compromising the security of the server or the network it&#8217;s on. In part this is provided by the /etc/ppp/ioptions file, where the administrator can place options to require authentication whenever <i>ipppd</i> is run, and in part by the PAP and CHAP secrets files, where the administrator can restrict the set of IP addresses which individual users may use. </p>
<p> The default behaviour of <i>ipppd</i> is to agree to authenticate if requested, and to not require authentication from the peer. However, <i>ipppd</i> will not agree to authenticate itself with a particular protocol if it has no secrets which could be used to do so. </p>
<p> Authentication is based on secrets, which are selected from secrets files (/etc/ppp/pap-secrets for PAP, /etc/ppp/chap-secrets for CHAP). Both secrets files have the same format, and both can store secrets for several combinations of server (authenticating peer) and client (peer being authenticated). Note that <i>ipppd</i> can be both a server and client, and that different protocols can be used in the two directions if desired. </p>
<p> A secrets file is parsed into words as for a options file. A secret is specified by a line containing at least 3 words, in the order client name, server name, secret. Any following words on the same line are taken to be a list of acceptable IP addresses for that client. If there are only 3 words on the line, it is assumed that any IP address is OK; to disallow all IP addresses, use &quot;-&quot;. If the secret starts with an `@&#8217;, what follows is assumed to be the name of a file from which to read the secret. A &quot;*&quot; as the client or server name matches any name. When selecting a secret, <i>ipppd</i> takes the best match, i.e. the match with the fewest wildcards. </p>
<p> Thus a secrets file contains both secrets for use in authenticating other hosts, plus secrets which we use for authenticating ourselves to others. Which secret to use is chosen based on the names of the host (the `local name&#8217;) and its peer (the `remote name&#8217;). The local name is set as follows:</p>
<dl>
<dt>if the <code>usehostname</code> option is given,</p>
<dd>then the local name is the hostname of this machine (with the domain appended, if given)</p>
<dt>else if the <code>name</code> option is given,</p>
<dd>then use the argument of the first <code>name</code> option seen</p>
<dt>else if the local IP address is specified with a hostname,</p>
<dd>then use that name</p>
<dt>else use the hostname of this machine (with the domain appended, if given)</p>
<dd></dl>
<p> When authenticating ourselves using PAP, there is also a `username&#8217; which is the local name by default, but can be set with the <code>user</code> option or the <code>+ua</code> option. </p>
<p> The remote name is set as follows:</p>
<dl>
<dt>if the <code>remotename</code> option is given,</p>
<dd>then use the argument of the last <code>remotename</code> option seen</p>
<dt>else if the remote IP address is specified with a hostname,</p>
<dd>then use that host name</p>
<dt>else the remote name is the null string &quot;&quot;.</p>
<dd></dl>
<p> Secrets are selected from the PAP secrets file as follows:</p>
<dl>
<dt>*</p>
<dd>For authenticating the peer, look for a secret with client == username specified in the PAP authenticate-request, and server == local name.</p>
<dt>*</p>
<dd>For authenticating ourselves to the peer, look for a secret with client == our username, server == remote name.</dl>
<p> When authenticating the peer with PAP, a secret of &quot;&quot; matches any password supplied by the peer. If the password doesn&#8217;t match the secret, the password is encrypted using crypt() and checked against the secret again; thus secrets for authenticating the peer can be stored in encrypted form. If the <code>papcrypt</code> option is given, the first (unencrypted) comparison is omitted, for better security. </p>
<p> If the <code>login</code> option was specified, the username and password are also checked against the system password database. Thus, the system administrator can set up the pap-secrets file to allow PPP access only to certain users, and to restrict the set of IP addresses that each user can use. Typically, when using the <code>login</code> option, the secret in /etc/ppp/pap-secrets would be &quot;&quot;, to avoid the need to have the same secret in two places. </p>
<p> Secrets are selected from the CHAP secrets file as follows:</p>
<dl>
<dt>*</p>
<dd>For authenticating the peer, look for a secret with client == name specified in the CHAP-Response message, and server == local name.</p>
<dt>*</p>
<dd>For authenticating ourselves to the peer, look for a secret with client == local name, and server == name specified in the CHAP-Challenge message.</dl>
<p> Authentication must be satisfactorily completed before IPCP (or any other Network Control Protocol) can be started. If authentication fails, <i>ipppd</i> will terminated the link (by closing LCP). If IPCP negotiates an unacceptable IP address for the remote host, IPCP will be closed. IP packets can only be sent or received when IPCP is open. </p>
<p> In some cases it is desirable to allow some hosts which can&#8217;t authenticate themselves to connect and use one of a restricted set of IP addresses, even when the local host generally requires authentication. If the peer refuses to authenticate itself when requested, <i>ipppd</i> takes that as equivalent to authenticating with PAP using the empty string for the username and password. Thus, by adding a line to the pap-secrets file which specifies the empty string for the client and password, it is possible to allow restricted access to hosts which refuse to authenticate themselves.</p>
<h2>Routing</h2>
<p>When IPCP negotiation is completed successfully, <i>ipppd</i> will inform the kernel of the local and remote IP addresses for the ppp interface. This is sufficient to create a host route to the remote end of the link, which will enable the peers to exchange IP packets. Communication with other machines generally requires further modification to routing tables and/or ARP (Address Resolution Protocol) tables. In some cases this will be done automatically through the actions of the <i>routed</i> or <i>gated</i> daemons, but in most cases some further intervention is required. </p>
<p> Sometimes it is desirable to add a default route through the remote host, as in the case of a machine whose only connection to the Internet is through the ppp interface. The <code>defaultroute</code> option causes <i>ipppd</i> to create such a default route when IPCP comes up, and delete it when the link is terminated. </p>
<p> In some cases it is desirable to use proxy ARP, for example on a server machine connected to a LAN, in order to allow other hosts to communicate with the remote host. The <code>proxyarp</code> option causes <i>ipppd</i> to look for a network interface on the same subnet as the remote host (an interface supporting broadcast and ARP, which is up and not a point-to-point or loopback interface). If found, <i>ipppd</i> creates a permanent, published ARP entry with the IP address of the remote host and the hardware address of the network interface found.</p>
<h2>Diagnostics</h2>
<p>Messages are sent to the syslog daemon using facility LOG_DAEMON. (This can be overriden by recompiling <i>ipppd</i> with the macro LOG_PPP defined as the desired facility.) In order to see the error and debug messages, you will need to edit your /etc/syslog.conf file to direct the messages to the desired output device or file. </p>
<p> The <code>debug</code> option causes the contents of all control packets sent or received to be logged, that is, all LCP, PAP, CHAP or IPCP packets. This can be useful if the PPP negotiation does not succeed. If debugging is enabled at compile time, the <code>debug</code> option also causes other debugging messages to be logged. </p>
<p> Debugging can also be enabled or disabled by sending a SIGUSR1 to the <i>ipppd</i> process. This signal acts as a toggle.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/run/ipppd.pid </code></p>
<dd>Process-ID for <i>ipppd</i> process on ppp interface unit <i>n</i>.</p>
<dt><code>/etc/ppp/ip-up</code></p>
<dd>A program or script which is executed when the link is available for sending and receiving IP packets (that is, IPCP has come up). It is executed with the parameters</p>
<dd><i>interface-name tty-device speed local-IP-address remote-IP-address</i></p>
<dd>and with its standard input, output and error streams redirected to <code>/dev/null</code>.</p>
<dd>This program or script is executed with the same real and effective user-ID as <i>ipppd</i>, that is, at least the effective user-ID and possibly the real user-ID will be <code>root</code>. This is so that it can be used to manipulate routes, run privileged daemons (e.g. <code>sendmail</code>), etc. Be careful that the contents of the /etc/ppp/ip-up and /etc/ppp/ip-down scripts do not compromise your system&#8217;s security.</p>
<dt><code>/etc/ppp/ip-down</code></p>
<dd>A program or script which is executed when the link is no longer available for sending and receiving IP packets. This script can be used for undoing the effects of the /etc/ppp/ip-up script. It is invoked with the same parameters as the ip-up script, and the same security considerations apply, since it is executed with the same effective and real user-IDs as <i>ipppd</i>.</p>
<dt><code>/etc/ppp/ipx-up</code></p>
<dd>A program or script which is executed when the link is available for sending and receiving IPX packets (that is, IPXCP has come up). It is executed with the parameters</p>
<dd><i>interface-name tty-device speed network-number local-IPX-node-address remote-IPX-node-address local-IPX-routing-protocol remote-IPX-routing-protocol local-IPX-router-name remote-IPX-router-name ipparam ipppd-pid</i></p>
<dd>and with its standard input, output and error streams redirected to <code>/dev/null</code>. </p>
<dd>The local-IPX-routing-protocol and remote-IPX-routing-protocol field may be one of the following:</p>
<dd>NONE to indicate that there is no routing protocol<br />
 RIP to indicate that RIP/SAP should be used<br />
 NLSP to indicate that Novell NLSP should be used<br />
 RIP NLSP to indicate that both RIP/SAP and NLSP should be used </p>
<dd>This program or script is executed with the same real and effective user-ID as <i>ipppd</i>, that is, at least the effective user-ID and possibly the real user-ID will be <code>root</code>. This is so that it can be used to manipulate routes, run privileged daemons (e.g. <code>ripd</code>), etc. Be careful that the contents of the /etc/ppp/ipx-up and /etc/ppp/ipx-down scripts do not compromise your system&#8217;s security.</p>
<dt><code>/etc/ppp/ipx-down</code></p>
<dd>A program or script which is executed when the link is no longer available for sending and receiving IPX packets. This script can be used for undoing the effects of the /etc/ppp/ipx-up script. It is invoked with the same parameters as the ipx-up script, and the same security considerations apply, since it is executed with the same effective and real user-IDs as <i>ipppd</i>.</p>
<dt><code>/etc/ppp/auth-up</code></p>
<dd>This program or script is executed after successful authentication with the following parameters: <i>interface name,</i> <i>authentication user name,</i> <i>username of ipppd,</i> <i>devicename,</i> <i>speed,</i> <i>remote number</i></p>
<dt><code>/etc/ppp/auth-down</code></p>
<dd>This program or script is executed after a disconnection with the following parameters: <i>interface name,</i> <i>authentication user name,</i> <i>username of ipppd,</i> <i>devicename,</i> <i>speed,</i> <i>remote number</i></p>
<dt><code>/etc/ppp/auth-fail</code></p>
<dd>This program or script is executed after a authentication failure with the following parameters: <i>interface name,</i> <i>authentication user name,</i> <i>username of ipppd,</i> <i>devicename,</i> <i>speed,</i> <i>remote number,</i> <i>failure reason</i><br />
&nbsp;<wbr>Valid reasons are:&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>Timeout during pap auth<br />
&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>pap protocol rejected<br />
&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>pap secrets invalid<br />
&nbsp;<wbr>&nbsp;<wbr>9&nbsp;<wbr>=&nbsp;<wbr>Timeout during chap auth<br />
&nbsp;<wbr>10&nbsp;<wbr>=&nbsp;<wbr>chap protocol rejected<br />
&nbsp;<wbr>11&nbsp;<wbr>=&nbsp;<wbr>chap secrets invalid</p>
<dt><code>/etc/ppp/pap-secrets</code></p>
<dd>Usernames, passwords and IP addresses for PAP authentication.</p>
<dt><code>/etc/ppp/chap-secrets</code></p>
<dd>Names, secrets and IP addresses for CHAP authentication.</p>
<dt><code>/etc/ppp/ioptions</code></p>
<dd>System default options for <i>ipppd,</i> read before user default options or command-line options.</dl>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4), <code><a href="/docs/linux/man/8-isdnctrl/">isdnctrl</a></code>(8), <code><a href="/docs/linux/man/8-ipppstats/">ipppstats</a></code>(8),</p>
<dd>
<dt><code>RFC1144</code></p>
<dd>Jacobson, V. <i>Compressing TCP/IP headers for low-speed serial links.</i> 1990 February.</p>
<dt><code>RFC1321</code></p>
<dd>Rivest, R. <i>The MD5 Message-Digest Algorithm.</i> 1992 April.</p>
<dt><code>RFC1332</code></p>
<dd>McGregor, G. <i>PPP Internet Protocol Control Protocol (IPCP).</i> 1992 May.</p>
<dt><code>RFC1334</code></p>
<dd>Lloyd, B.; Simpson, W.A. <i>PPP authentication protocols.</i> 1992 October.</p>
<dt><code>RFC1548</code></p>
<dd>Simpson, W.A. <i>The Point-to-Point Protocol (PPP).</i> 1993 December.</p>
<dt><code>RFC1549</code></p>
<dd>Simpson, W.A. <i>PPP in HDLC Framing.</i> 1993 December</dl>
<h2>Notes</h2>
<p>The following signals have the specified effect when sent to the <i>ipppd</i> process.</p>
<dl>
<dt><code>SIGINT, SIGTERM</code></p>
<dd>These signals cause <code>ipppd</code> to terminate the link (by closing LCP), restore the serial device settings, and exit.</p>
<dt><code>SIGHUP</code></p>
<dd>This signal causes <code>ipppd</code> to terminate the link, restore the serial device settings, and close the serial device. If the <code>persist</code> option has been specified, <code>ipppd</code> will try to reopen the serial device and start another connection. Otherwise <code>ipppd</code> will exit.</p>
<dt><code>SIGUSR2</code></p>
<dd>This signal causes <code>ipppd</code> to renegotiate compression. This can be useful to re-enable compression after it has been disabled as a result of a fatal decompression error. With the BSD Compress scheme, fatal decompression errors generally indicate a bug in one or other implementation.</dl>
<h2>Authors</h2>
<p>Originally written by Drew Perkins, Brad Clements, Karl Fox, Greg Christy, Brad Parker, Paul Mackerras &lt;paulus [at] cs.anu.edu.au&gt; for (original) pppd. </p>
<p> Changes for ipppd by Klaus Franken &lt;kfr [at] suse.de&gt; and Michael Hipp &lt;Michael.Hipp [at] student.uni-tuebingen.de&gt;. </p>
<p> Removal of pppd specific options and polish by Frank Elsner &lt;Elsner [at] zrz.TU-Berlin.DE&gt;.</p>
