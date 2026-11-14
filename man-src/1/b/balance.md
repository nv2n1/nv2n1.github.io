---
title: "balance(1)"
name: "balance"
section: "1"
letter: "b"
url: "/docs/linux/man/1-balance/"
description: "balance 3.42 – A simple TCP proxy with load balancing and failover mechanisms."
---

<h2>NAME</h2>
<p> balance 3.42 &#8211; A simple TCP proxy with load balancing and failover mechanisms.</p>
<h2>SYNOPSIS</h2>
<p> <code>balance </code> [ <code>-b addr</code> ] [ <code>-B addr</code> ] [ <code>-t sec</code> ] [ <code>-T sec</code> ] [ <code>-adfpHM</code> ] port host1[:port1[:maxc]] [!|%] [ &#8230; hostn[:portn[:maxc]]] </p>
<p> <code>balance</code> [ <code>-b addr </code> ] <code>-i</code> [ <code>-d</code> ] [ <code>-M</code> ] port </p>
<p> <code>balance</code> [ <code>-b addr</code> ] <code>-c cmd</code> [ <code>-d</code> ] [ <code>-M</code> ] port</p>
<h2>DESCRIPTION</h2>
<p> <i>Balance</i> is a simple, generic &quot;userland&quot; TCP proxy, which allows simple round-robin load balancing and graceful failover between several destination servers. </p>
<p> <i>Balance </i> supports IPv6 on the listening side which makes it a very useful tool for IPv6 migration of IPv4 only services and servers. </p>
<p> <i>Balance </i> is available at <a rel="nofollow" href="http://balance.sourceforge.net.">http://balance.sourceforge.net.</a> </p>
<p> <i>Definitions:</i> A possible destination consisting of a host address and a port is called a &quot;channel&quot;. A channel is member of a &quot;channel group&quot;. Channels are numbered in a group starting with 0. Groups are numbered starting with 0, which is the initial default group. </p>
<p> <i>Balance</i> accepts connections on the given port and forwards them to the supplied channels. At least one channel (in the default group) must be specified. If there are two or more channels specified in a group <i>balance</i> performs a simple round-robin load balancing between the channels. </p>
<p> <i>Balance</i> allows the definition of further channel groups. The connection scheme works as follows: <i>balance</i> tries first to establish a connection to a channel in the first group (0), performing the standard round-robin load balancing scheme. If no channel in this group is available, <i>balance</i> proceeds with the next higher channel group. Groups are simply separated with a &quot;!&quot; at the command line at startup and can be controlled interactively with the &quot;group&quot; command. </p>
<p> A &quot;%&quot; instead of a &quot;!&quot; as a group separator declares the previous group to be of type &quot;hash&quot;. This means that instead of a round-robin algorithm, a hash distribution based on the client ip address is used to determine the destination channel. This allows connecting one client always to the same server (e.g. balancing http sessions to a single server). </p>
<p> Hosts may be specified either by hostname or by IP address. Ports may be specified either by name (as listed in /etc/services) or numerically. If no port is specified in a destination, the destination port defaults to the source port that <i>balance</i> controls. </p>
<p> <i>Balance </i> allows the specification of the maximum number of connections per channel. This parameter can be optionally added after the port specification separated by a colon (&quot;:&quot;). If a maximum number of connections is specified a channel will only be used for this maximum number of simultaneous connections. A maxc value of 0 denotes an unlimited number of connections. This is the initial default value of a channel. </p>
<p> The maximum number of groups and channels <i>balance</i> can handle is specified at compile time and is initially 16 channels in 16 groups. </p>
<p> Failover to another destination (a &quot;channel&quot;) occurs if the connection is refused on the current channel or if the connect timeout is reached trying to establish a connection. If all possible destinations (channels) currently fail, the client connection to balance is closed. </p>
<p> <i>Balance</i> accepts the following options:</p>
<dl>
<dt><code>a</code></p>
<dd> Enable autodisable option: A channel needs to be manually re-enabled after a failure.</p>
<dt><code>b</code></p>
<dd> Bindhost: <i>Balance</i> binds to the specified host (or address) for listen() instead to INADDR_ANY.</p>
<dt><code>B</code></p>
<dd> Bindhost: <i>Balance</i> binds to the specified host (or address) for outgoing connections (the connection will be initiated from this address).</p>
<dt><code>c</code></p>
<dd> Command: allows to send a command to the balance master process (see interactive mode)</p>
<dt><code>d</code></p>
<dd> Debug: <i>Balance</i> outputs debugging and tracing information messages on stderr.</p>
<dt><code>H</code></p>
<dd> Hashfailover: <i>Balance</i> does failover to next node even if hash is used.</p>
<dt><code>F</code></p>
<dd> Foreground: tells <i>balance </i> to stay in foreground. This might be useful for testing and debugging since <i>balance </i> can be stopped in that mode using ^C (or other interrupt character).</p>
<dt><code>M</code></p>
<dd> Use memory mapping for IPC instead of shared memory</p>
<dt><code>i</code></p>
<dd> Interactive Control: <i>Balance</i> connects to the running instance defined by local port and bind address via shared memory and allows to control the behaviour of it using a command line interface. The access permission using this interface are determined by the access restrictions of the shared memory segment in effect. <i>help or ?</i> prints out a short command overview, <i>create</i> allows to establish a new destination definition (channel) consisting of host and port in the current group, <i>disable</i> disables a channel in the current group, <i>enable</i> enables a channel again in the current group, <i>group</i> changes the current group in interactive mode where all following commands are targeted, <i>hash</i> changes the current group to be of type &quot;Hash&quot;, <i>help </i> prints out online help informations, <i>kill</i> shuts down the master process and exits interactive mode, <i>maxc &lt;channel&gt; &lt;maxc&gt;</i> sets the maximum number of connection ot the channel (0 means infinite), <i>mrtg-bytes &lt;group&gt; &lt;channel&gt;</i> prints out the bytes received/sent in MRTG compatible format (intended to be called with -c automatically by MRTG), <i>mrtg-conns &lt;group&gt; &lt;channel&gt;</i> prints out the total connections in MRTG compatible format (intended to be called with -c automatically by MRTG), <i>quit</i> exits the interactive mode, <i>reset</i> resets the byte counters of a channel, <i>rr</i> changes the current group to be of type &quot;Round Robin&quot;, <i>show </i> shows an overview and the status of all channels including the incoming and outgoing transfer volume in bytes. The output is sorted by groups. Additionally the current connections (c) and the maximum allowed connections (maxc) are printed, <i>version</i> prints out the version and MAXGROUPS and MAXCHANNELS constants at compile time.</p>
<dt><code>p</code></p>
<dd> Packetdump: <i>Balance</i> shows all incoming and outgoing data on stdout using a simple always readable external representation of data. This might be useful for debugging and protocol analysis.</p>
<dt><code>t</code></p>
<dd> Connect Timeout: the default timeout trying to establish a connection to any destination can be changed using this option. The default timeout after which a destination is regarded to be currently inaccessible is 5 seconds.</p>
<dt><code>T</code></p>
<dd> Select Timeout: Timeout for select(), default = 0 (never). This feature is currently untested.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>$ balance smtp host1.test.net host2.test.net</code></p>
<dd> Connection to the local SMTP port will be forwarded alterating to the SMTP port on host1 and host2. <i>Balance</i> runs automatically in background.</dl>
<dl>
<dt><code>$ balance -b 2001:DB8::1 80 10.1.1.1 10.1.1.2 </code></p>
<dd> <i>Balance</i> binds on port 80 of the local IPv6 IP address 2001:DB8::1 and distributes connections to the IPv4 addresses 10.1.1.1 and 10.1.1.2.</dl>
<dl>
<dt><code>$ balance -fp imap mailserver</code></p>
<dd> Connections to the local IMAP port will always be forwarded to the host &quot;mailserver&quot;. <i>Balance</i> stays in foreground and all data is printed in readable format on stdout.</dl>
<dl>
<dt><code>$ balance -f 8888 host1 10.1.1.1:8000</code></p>
<dd> Connections to the local port 8888 are forwarded alternating to host1, port 8888 and the host 10.1.1.1, port 8000. <i>Balance</i> stays in foreground connected to the &quot;controlling tty&quot;.</dl>
<dl>
<dt><code>$ balance imap mailserver1::16 ! mailserver2</code></p>
<dd> Two groups are specified, each containing one channel member. First up to 16 simultaneous connections are forwarded to &quot;mailserver1&quot;. As soon as they are consumed, <i>balance </i> proceeds with the next group (1) which will consume all remaining connections forwarding them to the imap ort on &quot;mailserver2&quot;.</dl>
<dl>
<dt><code>$ balance pop3 host1 host2 host3 ! failover1</code></p>
<dd> <i>Balance</i> does round robin load balancing for the three hosts in the default group 0 for pop3 services. If all three hosts in group 0 fail, all connections are then forwarded to the host &quot;failover1&quot;.</dl>
<dl>
<dt><code>$ balance telnet target.munich.net::1</code></p>
<dd> Here <i>balance</i> is used to restrict all connections to exactly one at a time forwarding the telnet port.</dl>
<dl>
<dt><code>$ balance 8888 localhost::12 ! localhost::4 ! localhost::2 localhost::2 ! localhost:25</code></p>
<dd> This is a simple test, forming 5 groups where balance is self referencing its own services 20 times. This is simply a test which definitely can be tried at home.</dl>
<h2>BUGS</h2>
<p> In case that <i>balance</i> is not able to forward the connection to any destination the inital connection to balance is always first accepted and then closed again immediately. This is not in every case the behaviour that would have been seen directly on the destination host.</p>
<h2>AUTHOR</h2>
<p> Thomas Obermair, Inlab Software GmbH (obermair [at] acm.org) </p>
<p> Copyright (c) 2000-2007,2008 by Thomas Obermair (obermair [at] acm.org) and Inlab Software GmbH (<a rel="nofollow" href="http://www.inlab.de">http://www.inlab.de</a>), Gruenwald, Germany. All rights reserved. </p>
<p> Balance is released under the GNU GENERAL PUBLIC LICENSE, see the file COPYING in the source code distribution. </p>
<h2>Index</h2>
