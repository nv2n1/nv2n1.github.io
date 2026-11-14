---
title: "node(8)"
name: "node"
section: "8"
letter: "n"
url: "/docs/linux/man/8-node/"
description: "node – Node front end for AX.25, NET/ROM, Rose and TCP"
---

<p>node &#8211; Node front end for AX.25, NET/ROM, Rose and TCP</p>
<h2>Synopsis</h2>
<p><code>node [-c]</code></p>
<h2>Description</h2>
<p><code>Node</code> is a simple node front end, modelled after the node shells of TheNet and G8BPQ nodes.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>Enable compression. With this option it is assumed that the incoming call is using Zlib based compression (modified Lempel-Ziv 1977). Currently no negotiation is done so the caller must be aware of this. You probably want to set up a separate AX.25, NET/ROM or ROSE callsign in ax25d.conf or a separate TCP port in inetd.conf to listen to compressed connects. </p>
<p> At the moment I know only two implementations compatible with this compression method, namely LinuxNode and Clussed.</dl>
<h2>Node Commands</h2>
<p>The following commands are supported for users of <code>node:</code></p>
<dl>
<dt><code>?</code></p>
<dd>Give short list of available commands.</p>
<dt><code>Bye</code></p>
<dd>Disconnect user from the node.</p>
<dt><code>Connect &lt;port&gt; &lt;call&gt; [via &lt;call1&gt; &#8230;] [d|s] For AX.25</code></p>
<dd>
<dt><code>Connect &lt;call | alias&gt; [d|s] For NET/ROM</code></p>
<dd>
<dt><code>Connect &lt;call&gt; &lt;address&gt; [&lt;digi&gt;] [d|s] For ROSE</code></p>
<dd>Initiate an AX.25, NET/ROM or ROSE connection to a remote host. If only one argument is supplied then the connection is assumed to be a NET/ROM connection and the argument specifies the callsign of alias of a NET/ROM node. If more than one argument is supplied and the second parameter is composed of numeric characters only then the connection is assumed to be a ROSE connection. Any other combination is assumed to be an AX.25 connection with the first argument being the AX25 port to use for the connection. </p>
<p> For a ROSE connection the &lt;address&gt; part must be exactly six or ten digits. If only six digits are supplied, the DNIC (first four digits) default to the local DNIC. The local DNIC is assumed to be that of the first configured Rose port in /etc/ax25/rsports. </p>
<p> The user may optionally supply as the last argument a single character which modifies the default behaviour on disconnection of the connection. If a single `s&#8217; is entered as the last argument, then when the remote host disconnects you will be returned to this node. If a single `d&#8217; is entered as the last argument, you will be disconnected from this node too. The Default behaviour (neither `s&#8217; nor `d&#8217; entered) is configured in the node configuration file and depends on the sysop preference.</p>
<dt><code>Escape [&lt;escape string&gt;]</code></p>
<dd>Override the sysop configured default escape character setting. If the Escape command is given without an argument then the current escape character setting is returned to the user. The escape string may be specified using any of the well known codings:</p>
<dd><code>&lt;char&gt;</code> to enter the escape character in its binary form.</p>
<dd><code>^C</code> to enter the escape character as a control character value.</p>
<dd><code>NNN</code> to set the escape character to a Decimal value.</p>
<dd><code>0xNN</code> to set the escape character to a HexaDecimal value.</p>
<dd><code>0NNN</code> to set the escape character to an Octal value.</p>
<dd><code>off</code> to disable the escape character.</p>
<dt><code>Finger [&lt;username&gt;][@&lt;hostname&gt;]</code></p>
<dd>Retrieve information about users of a system. If the user name is omitted, shows the users currently logged on the host. If the hostname is omitted, defaults to the local host.</p>
<dt><code>Help [&lt;command&gt;]</code></p>
<dd>Give help for the specified command or this text if no command is specified. Commands can not be abbreviated. Use the &quot;?&quot; command to retrieve a list of available commands.</p>
<dt><code>HOst &lt;hostname&gt; | &lt;ip address&gt;</code></p>
<dd>Give the Domain Name Service host name information about &lt;hostname&gt; or &lt;ip address&gt;.</p>
<dt><code>Info</code></p>
<dd>Display the version information and the contents of the /etc/ax25/node.info file, which should describe any aspects of your system that you would like to brag about.</p>
<dt><code>Links [* | &lt;call&gt;]</code></p>
<dd>Give a list of active AX.25 connections to and from the local host. With an optional argument * list also AX.25 sockets in state listening. A callsign as argument gives a list of all connections with &lt;call&gt; as source or destination address.</p>
<dt><code>Mheard &lt;portname&gt;</code></p>
<dd>Give a list of heard AX.25 stations on the specified port.</p>
<dt><code>NLinks</code></p>
<dd>Give a list of active NET/ROM connections to and from the local host.</p>
<dt><code>Nodes [* | &lt;node&gt;]</code></p>
<dd>Show the NET/ROM node table of the local host. The nodes on this list can be reached using the Connect command without knowing the actual network path used (assuming the network is OK). </p>
<p> The optional argument &#8216;*&#8217; toggles verbose mode, showing the Obsolescence counter, relative path quality and the port and neighbour node used to reach each node. You can also specify a node callsign to get the verbose information for a single node. In that case a &quot;which&quot; field that tells what route the kernel will use to reach the node is also shown.</p>
<dt><code>Ports</code></p>
<dd>Show the available AX.25 ports. Shown are the port name and a short description for the port. The port name is used when using the Connect command to connect to an user or service not running NET/ROM (eg. not visible in the Nodes list).</p>
<dt><code>PIng &lt;host&gt; [&lt;size&gt;]</code></p>
<dd>Check if a host can be reached trough the network by sending an ICMP Echo Request packet to the host and waiting for it to reply. If a reply is received the round-trip-time (RTT) between the local and remote hosts is shown. </p>
<p> If an optional length is specified the data portion of the packet is filled with length number of bytes.</p>
<dt><code>Routes</code></p>
<dd>Show the NET/ROM neighbour table of the local host (ie. the nodes which the local node directly talks with). These nodes are used to reach the other nodes on the node table.</p>
<dt><code>Status</code></p>
<dd>Give some more or less useful information about the system.</p>
<dt><code>Telnet &lt;host&gt; [&lt;port&gt;] [&lt;string&gt;] [d|s]</code></p>
<dd>Initiate a telnet session to a remote host using TCP/IP. By default, the telnet command connects to the TCP port 23 (allocated for telnet). You can specify another TCP port or a TCP port name. </p>
<p> If an optional third argument &lt;string&gt; is given, that string, followed by a CRLF is sent to the remote host right after the connection is established. This is mainly useful for command aliases. </p>
<p> If a single `s&#8217; is entered as the last parameter, then when the remote host disconnects you will be returned to this node. If a single `d&#8217; is entered as the last parameter, you will be disconnected from this node too. Default behaviour (neither `s&#8217; nor `d&#8217; entered) depends on sysop configuration.</p>
<dt><code>TAlk &lt;user&gt; &lt;message&gt;</code></p>
<dd>Send a message to another user of the node. The user in question must be in idle state (ie. not connected/connecting anywhere or running a program). </p>
<p> If the user has an SSID other than zero, the SSID must be specified. If multiple users are logged in with the same callsign/SSID pair, those who are in idle state, get the message.</p>
<dt><code>Users</code></p>
<dd>Show a list of users currently connected to the local node, where the users are coming from, and what are they doing at the moment.</p>
<dt><code>ZConnect</code></p>
<dd>Initiate a compressed AX.25, NET/ROM or ROSE connection. The command arguments are the same as in <code>Connect</code> command. Note that the other end must be expecting a compressed connection (a LinuxNode started with the -c command line option). No negotiation of compression is done.</p>
<dt><code>ZTelnet</code></p>
<dd>Initiate a compressed telnet session. The command arguments are the same as in <code>Telnet</code> command. Note that the other end must be expecting a compressed connection (a LinuxNode started with the -c command line option). No negotiation of compression is done.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/ax25/node.conf</code></p>
<dd>LinuxNode configuration file. </p>
<dt><code>/etc/ax25/node.perms</code></p>
<dd>LinuxNode permissions file. </p>
<dt><code>/etc/ax25/node.motd</code></p>
<dd>LinuxNode message of the day file. </p>
<dt><code>/etc/ax25/node.info</code></p>
<dd>The response to the &#8216;info&#8217; command. This file should be edited to reflect the local configuration. </p>
<dt><code>/var/ax25/node/loggedin</code></p>
<dd>Database of current users. </p>
<dt><code>/var/ax25/mheard/mheard.dat</code></p>
<dd>Information about AX.25 stations heard. </p>
<dt><code>/usr/lib/ax25/node/help/*.hlp</code></p>
<dd>The online help files.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-node-conf/">node.conf</a></code>(5), <code><a href="/docs/linux/man/5-node-perms/">node.perms</a></code>(5), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/8-ax25d/">ax25d</a></code>(8), <code><a href="/docs/linux/man/8-mheardd/">mheardd</a></code>(8).</p>
<h2>Author</h2>
<p>Tomi Manninen OH2BNS &lt;tpmannin [at] cc.hut.fi&gt;<br />
 Alan Cox GW4PTS &lt;gw4pts [at] gw4pts.ampr.org&gt;</p>
