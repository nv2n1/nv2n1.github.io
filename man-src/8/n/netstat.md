---
title: "netstat(8)"
name: "netstat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netstat/"
description: "netstat – Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships"
---

<p>netstat &#8211; Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships</p>
<h2>Synopsis</h2>
<p><code>netstat </code> [<i>address_family_options</i>] [<code>&#8211;tcp</code>|<code>-t</code>] [<code>&#8211;udp</code>|<code>-u</code>] [<code>&#8211;udplite</code>|<code>-U</code>] [<code>&#8211;sctp</code>|<code>-S</code>] [<code>&#8211;raw</code>|<code>-w</code>] [<code>&#8211;l2cap</code>|<code>-2</code>] [<code>&#8211;rfcomm</code>|<code>-f</code>] [<code>&#8211;listening</code>|<code>-l</code>] [<code>&#8211;all</code>|<code>-a</code>] [<code>&#8211;numeric</code>|<code>-n</code>] [<code>&#8211;numeric-hosts</code>] [<code>&#8211;numeric-ports</code>] [<code>&#8211;numeric-users</code>] [<code>&#8211;symbolic</code>|<code>-N</code>] [<code>&#8211;extend</code>|<code>-e</code>[<code>&#8211;extend</code>|<code>-e]</code>] [<code>&#8211;timers</code>|<code>-o</code>] [<code>&#8211;program</code>|<code>-p</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;continuous</code>|<code>-c]</code> [<code>&#8211;wide</code>|<code>-W</code>] <code>netstat </code> {<code>&#8211;route</code>|<code>-r</code>} [<i>address_family_options</i>] [<code>&#8211;extend</code>|<code>-e</code>[<code>&#8211;extend</code>|<code>-e]</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;numeric</code>|<code>-n</code>] [<code>&#8211;numeric-hosts</code>] [<code>&#8211;numeric-ports</code>] [<code>&#8211;numeric-users</code>] [<code>&#8211;continuous</code>|<code>-c</code>] <code>netstat</code> {<code>&#8211;interfaces</code>|<code>-i</code>} [<code>&#8211;all</code>|<code>-a</code>] [<code>&#8211;extend</code>|<code>-e</code>[<code>&#8211;extend</code>|<code>-e]</code>] [<code>&#8211;verbose</code>|<code>-v</code>] [<code>&#8211;program</code>|<code>-p</code>] [<code>&#8211;numeric</code>|<code>-n</code>] [<code>&#8211;numeric-hosts</code>] [<code>&#8211;numeric-ports</code>] [<code>&#8211;numeric-users</code>] [<code>&#8211;continuous</code>|<code>-c</code>] <code>netstat</code> {<code>&#8211;groups</code>|<code>-g</code>} [<code>&#8211;numeric</code>|<code>-n</code>] [<code>&#8211;numeric-hosts</code>] [<code>&#8211;numeric-ports</code>] [<code>&#8211;numeric-users</code>] [<code>&#8211;continuous</code>|<code>-c</code>] <code>netstat</code> {<code>&#8211;masquerade</code>|<code>-M</code>} [<code>&#8211;extend</code>|<code>-e</code>] [<code>&#8211;numeric</code>|<code>-n</code>] [<code>&#8211;numeric-hosts</code>] [<code>&#8211;numeric-ports</code>] [<code>&#8211;numeric-users</code>] [<code>&#8211;continuous</code>|<code>-c</code>] <code>netstat</code> {<code>&#8211;statistics</code>|<code>-s</code>} [<code>&#8211;tcp</code>|<code>-t</code>] [<code>&#8211;udp</code>|<code>-u</code>] [<code>&#8211;udplite</code>|<code>-U</code>] [<code>&#8211;sctp</code>|<code>-S</code>] [<code>&#8211;raw</code>|<code>-w</code>] <code>netstat </code> {<code>&#8211;version</code>|<code>-V</code>} <code>netstat </code> {<code>&#8211;help</code>|<code>-h</code>} <i>address_family_options</i>: [<code>-4</code>|<code>&#8211;inet</code>] [<code>-6</code>|<code>&#8211;inet6</code>] [<code>&#8211;protocol=</code>{<code>inet</code>,<code>inet6</code>,<code>unix</code>,<code>ipx</code>,<code>ax25</code>,<code>netrom</code>,<code>ddp</code>,<code>bluetooth</code>, &#8230; } ] [<code>&#8211;unix</code>|<code>-x</code>] [<code>&#8211;inet</code>|<code>&#8211;ip</code>|<code>&#8211;tcpip</code>] [<code>&#8211;ax25</code>] [<code>&#8211;x25</code>] [<code>&#8211;rose</code>] [<code>&#8211;ash</code>] [<code>&#8211;bluetooth</code>] [<code>&#8211;ipx</code>] [<code>&#8211;netrom</code>] [<code>&#8211;ddp</code>|<code>&#8211;appletalk</code>] [<code>&#8211;econet</code>|<code>&#8211;ec</code>] </p>
<h2>Notes</h2>
<p>This program is mostly obsolete. Replacement for <code>netstat</code> is <code>ss</code>. Replacement for <code>netstat -r</code> is <code>ip route</code>. Replacement for <code>netstat -i</code> is <code>ip -s link</code>. Replacement for <code>netstat -g</code> is <code>ip maddr</code>. </p>
<h2>Description</h2>
<p><code>Netstat</code> prints information about the Linux networking subsystem. The type of information printed is controlled by the first argument, as follows:</p>
<h3>(none)</h3>
<p>By default, <code>netstat </code> displays a list of open sockets. If you don&#8217;t specify any address families, then the active sockets of all configured address families will be printed.</p>
<h3>&#8211;route, -r</h3>
<p>Display the kernel routing tables. See the description in <code><a href="/docs/linux/man/8-route/">route</a></code>(8) for details. <code>netstat -r </code> and <code>route -e </code> produce the same output.</p>
<h3>&#8211;groups, -g</h3>
<p>Display multicast group membership information for IPv4 and IPv6.</p>
<h3>&#8211;interfaces, -i</h3>
<p>Display a table of all network interfaces.</p>
<h3>&#8211;masquerade, -M</h3>
<p>Display a list of masqueraded connections.</p>
<h3>&#8211;statistics, -s</h3>
<p>Display summary statistics for each protocol.</p>
<h2>Options</h2>
<h3>&#8211;verbose, -v</h3>
<p>Tell the user what is going on by being verbose. Especially print some useful information about unconfigured address families.</p>
<h3>&#8211;wide, -W</h3>
<p>Do not truncate IP addresses by using output as wide as needed. This is optional for now to not break existing scripts.</p>
<h3>&#8211;numeric, -n</h3>
<p>Show numerical addresses instead of trying to determine symbolic host, port or user names.</p>
<h3>&#8211;numeric-hosts</h3>
<p>shows numerical host addresses but does not affect the resolution of port or user names.</p>
<h3>&#8211;numeric-ports</h3>
<p>shows numerical port numbers but does not affect the resolution of host or user names.</p>
<h3>&#8211;numeric-users</h3>
<p>shows numerical user IDs but does not affect the resolution of host or port names.</p>
<h3>&#8211;protocol=</code><i>family</i>, <code>-A</h3>
<p>Specifies the address families (perhaps better described as low level protocols) for which connections are to be shown. </code><i>family </i> is a comma (&#8216;,&#8217;) separated list of address family keywords like <code>inet</code>, <code>inet6</code>, <code>unix</code>, <code>ipx</code>, <code>ax25</code>, <code>netrom</code>, <code>econet</code>, <code>ddp</code>, and <code>bluetooth</code>. This has the same effect as using the <code>&#8211;inet</code>|<code>-4</code>, <code>&#8211;inet6</code>|<code>-6</code>, <code>&#8211;unix</code>|<code>-x</code>, <code>&#8211;ipx</code>, <code>&#8211;ax25</code>, <code>&#8211;netrom</code>, <code>&#8211;ddp</code>, and <code>&#8211;bluetooth</code> options. </p>
<p> The address family <code>inet</code> (Iv4) includes raw, udp, udplite and tcp protocol sockets. </p>
<p> The address family <code>bluetooth</code> (Iv4) includes l2cap and rfcomm protocol sockets.</p>
<h3>-c, &#8211;continuous</h3>
<p>This will cause <code>netstat</code> to print the selected information every second continuously.</p>
<h3>-e, &#8211;extend</h3>
<p>Display additional information. Use this option twice for maximum detail.</p>
<h3>-o, &#8211;timers</h3>
<p>Include information related to networking timers.</p>
<h3>-p, &#8211;program</h3>
<p>Show the PID and name of the program to which each socket belongs.</p>
<h3>-l, &#8211;listening</h3>
<p>Show only listening sockets. (These are omitted by default.)</p>
<h3>-a, &#8211;all</h3>
<p>Show both listening and non-listening sockets. With the <code>&#8211;interfaces</code> option, show interfaces that are not up</p>
<h3>-F</h3>
<p>Print routing information from the FIB. (This is the default.)</p>
<h3>-C</h3>
<p>Print routing information from the route cache.</p>
<h2>Output</h2>
<h3>Active Internet connections (TCP, UDP, UDPLite, raw)</h3>
<h3>Proto</h3>
<p>The protocol (tcp, udp, udpl, raw) used by the socket.</p>
<h3>Recv-Q</h3>
<p>Established: The count of bytes not copied by the user program connected to this socket. Listening: Since Kernel 2.6.18 this column contains the current syn backlog.</p>
<h3>Send-Q</h3>
<p>Established: The count of bytes not acknowledged by the remote host. Listening: Since Kernel 2.6.18 this column contains the maximum size of the syn backlog.</p>
<h3>Local Address</h3>
<p>Address and port number of the local end of the socket. Unless the <code>&#8211;numeric</code> (<code>-n</code>) option is specified, the socket address is resolved to its canonical host name (FQDN), and the port number is translated into the corresponding service name.</p>
<h3>Foreign Address</h3>
<p>Address and port number of the remote end of the socket. Analogous to &quot;Local Address&quot;.</p>
<h3>State</h3>
<p>The state of the socket. Since there are no states in raw mode and usually no states used in UDP and UDPLite, this column may be left blank. Normally this can be one of several values:</p>
<dl>
<dt><i>ESTABLISHED</i></p>
<dd>The socket has an established connection.</p>
<dt><i>SYN_SENT</i></p>
<dd>The socket is actively attempting to establish a connection.</p>
<dt><i>SYN_RECV</i></p>
<dd>A connection request has been received from the network.</p>
<dt><i>FIN_WAIT1</i></p>
<dd>The socket is closed, and the connection is shutting down.</p>
<dt><i>FIN_WAIT2</i></p>
<dd>Connection is closed, and the socket is waiting for a shutdown from the remote end.</p>
<dt><i>TIME_WAIT</i></p>
<dd>The socket is waiting after close to handle packets still in the network.</p>
<dt><i>CLOSE</i></p>
<dd>The socket is not being used.</p>
<dt><i>CLOSE_WAIT</i></p>
<dd>The remote end has shut down, waiting for the socket to close.</p>
<dt><i>LAST_ACK</i></p>
<dd>The remote end has shut down, and the socket is closed. Waiting for acknowledgement.</p>
<dt><i>LISTEN</i></p>
<dd>The socket is listening for incoming connections. Such sockets are not included in the output unless you specify the <code>&#8211;listening</code> (<code>-l</code>) or <code>&#8211;all</code> (<code>-a</code>) option.</p>
<dt><i>CLOSING</i></p>
<dd>Both sockets are shut down but we still don&#8217;t have all our data sent.</p>
<dt><i>UNKNOWN</i></p>
<dd>The state of the socket is unknown.</dl>
<h3>User</h3>
<p>The username or the user id (UID) of the owner of the socket.</p>
<h3>PID/Program name</h3>
<p>Slash-separated pair of the process id (PID) and process name of the process that owns the socket. <code>&#8211;program</code> causes this column to be included. You will also need <i>superuser</i> privileges to see this information on sockets you don&#8217;t own. This identification information is not yet available for IPX sockets.</p>
<h3>Timer</h3>
<p>(this needs to be written)</p>
<h3>Active UNIX domain Sockets</h3>
<h3>Proto</h3>
<p>The protocol (usually unix) used by the socket.</p>
<h3>RefCnt</h3>
<p>The reference count (i.e. attached processes via this socket).</p>
<h3>Flags</h3>
<p>The flags displayed is SO_ACCEPTON (displayed as <code>ACC</code>), SO_WAITDATA (<code>W</code>) or SO_NOSPACE (<code>N</code>). SO_ACCECPTON is used on unconnected sockets if their corresponding processes are waiting for a connect request. The other flags are not of normal interest.</p>
<h3>Type</h3>
<p>There are several types of socket access:</p>
<dl>
<dt><i>SOCK_DGRAM</i></p>
<dd>The socket is used in Datagram (connectionless) mode.</p>
<dt><i>SOCK_STREAM</i></p>
<dd>This is a stream (connection) socket.</p>
<dt><i>SOCK_RAW</i></p>
<dd>The socket is used as a raw socket.</p>
<dt><i>SOCK_RDM</i></p>
<dd>This one serves reliably-delivered messages.</p>
<dt><i>SOCK_SEQPACKET</i></p>
<dd>This is a sequential packet socket.</p>
<dt><i>SOCK_PACKET</i></p>
<dd>Raw interface access socket.</p>
<dt><i>UNKNOWN</i></p>
<dd>Who ever knows what the future will bring us &#8211; just fill in here :-)</dl>
<h3>State</h3>
<p>This field will contain one of the following Keywords:</p>
<dl>
<dt><i>FREE</i></p>
<dd>The socket is not allocated</p>
<dt><i>LISTENING </i></p>
<dd>The socket is listening for a connection request. Such sockets are only included in the output if you specify the <code>&#8211;listening</code> (<code>-l</code>) or <code>&#8211;all</code> (<code>-a</code>) option.</p>
<dt><i>CONNECTING</i></p>
<dd>The socket is about to establish a connection.</p>
<dt><i>CONNECTED</i></p>
<dd>The socket is connected.</p>
<dt><i>DISCONNECTING</i></p>
<dd>The socket is disconnecting.</p>
<dt><i>(empty)</i></p>
<dd>The socket is not connected to another one.</p>
<dt><i>UNKNOWN</i></p>
<dd>This state should never happen.</dl>
<h3>PID/Program name</h3>
<p>Process ID (PID) and process name of the process that has the socket open. More info available in <code>Active Internet connections</code> section written above.</p>
<h3>Path</h3>
<p>This is the path name as which the corresponding processes attached to the socket.</p>
<h3>Active IPX sockets</h3>
<p>(this needs to be done by somebody who knows it)</p>
<h3>Active NET/ROM sockets</h3>
<p>(this needs to be done by somebody who knows it)</p>
<h3>Active AX.25 sockets</h3>
<p>(this needs to be done by somebody who knows it)</p>
<h2>Files</h2>
<p><i>/etc/services</i> &#8212; The services translation file </p>
<p> <i>/proc</i> &#8212; Mount point for the proc filesystem, which gives access to kernel status information via the following files. </p>
<p> <i>/proc/net/dev</i> &#8212; device information </p>
<p> <i>/proc/net/raw</i> &#8212; raw socket information </p>
<p> <i>/proc/net/tcp</i> &#8212; TCP socket information </p>
<p> <i>/proc/net/udp</i> &#8212; UDP socket information </p>
<p> <i>/proc/net/udplite</i> &#8212; UDPLite socket information </p>
<p> <i>/proc/net/igmp</i> &#8212; IGMP multicast information </p>
<p> <i>/proc/net/unix</i> &#8212; Unix domain socket information </p>
<p> <i>/proc/net/ipx</i> &#8212; IPX socket information </p>
<p> <i>/proc/net/ax25</i> &#8212; AX25 socket information </p>
<p> <i>/proc/net/appletalk</i> &#8212; DDP (appletalk) socket information </p>
<p> <i>/proc/net/nr</i> &#8212; NET/ROM socket information </p>
<p> <i>/proc/net/route</i> &#8212; IP routing information </p>
<p> <i>/proc/net/ax25_route</i> &#8212; AX25 routing information </p>
<p> <i>/proc/net/ipx_route</i> &#8212; IPX routing information </p>
<p> <i>/proc/net/nr_nodes</i> &#8212; NET/ROM nodelist </p>
<p> <i>/proc/net/nr_neigh</i> &#8212; NET/ROM neighbours </p>
<p> <i>/proc/net/ip_masquerade</i> &#8212; masqueraded connections </p>
<p> <i>/sys/kernel/debug/bluetooth/l2cap</i> &#8212; Bluetooth L2CAP information </p>
<p> <i>/sys/kernel/debug/bluetooth/rfcomm</i> &#8212; Bluetooth serial connections </p>
<p> <i>/proc/net/snmp</i> &#8212; statistics</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-route/">route</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) <code><a href="/docs/linux/man/8-ss/">ss</a></code>(8) <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Bugs</h2>
<p>Occasionally strange information may appear if a socket changes as it is viewed. This is unlikely to occur. </p>
<h2>Authors</h2>
<p>The netstat user interface was written by Fred Baumgarten &lt;dc6iq [at] insu1.etec.uni-karlsruhe.de&gt;, the man page basically by Matt Welsh &lt;mdw [at] tc.cornell.edu&gt;. It was updated by Alan Cox &lt;Alan.Cox [at] linux.org&gt;, updated again by Tuan Hoang &lt;tqhoang [at] bigfoot.com&gt;. The man page and the command included in the net-tools package is totally rewritten by Bernd Eckenfels &lt;ecki [at] linux.de&gt;. UDPLite options were added by Brian Micek &lt;bmicek [at] gmail.com&gt;</p>
