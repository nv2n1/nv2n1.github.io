---
title: "dibbler-relay(8)"
name: "dibbler-relay"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dibbler-relay/"
description: "dibbler-relay – a portable DHCPv6 relay"
---

<p>dibbler-relay &#8211; a portable DHCPv6 relay</p>
<h2>Description</h2>
<p><code>dibbler-relay</code> is a portable implementation of the DHCPv6 relay. DHCPv6 relays are proxies, which allow one server to support links, which server is not directly connected to. There are ports available for Linux 2.4/2.6 systems as well as MS Windows XP and 2003. They are freely available under <code>GNU GPL </code> version 2 (or later) license. </p>
<h2>Synopsis</h2>
<p><code>dibbler-relay</code> [ run | start | stop | status ] </p>
<h2>Options</h2>
<p><i>run</i> &#8211; starts relay in the console. Relay can be closed using ctrl-c. </p>
<p> <i>start </i> &#8211; starts relay in daemon mode. </p>
<p> <i>stop</i> &#8211; stops running relay. </p>
<p> <i>status</i> &#8211; shows status of the relay.</p>
<h2>Examples</h2>
<p>Relay forwards DHCPv6 messages between interfaces. Messages from client are encapsulated and forwarded as RELAY_FORW messages. Replies from server are received as RELAY_REPL message. After decapsulation, they are being sent back to clients. It is vital to inform server, where this relayed message was received. DHCPv6 does this using interface-id option. This identifier must be unique. Otherwise relays will get confused when they will receive reply from server. Note that this id does not need to be alligned with system interface id (ifindex). Think about it as &quot;ethernet segment identifier&quot; if you are using Ethernet network or as &quot;bss identifier&quot; if you are using 802.11 network. Let&#8217;s assume this case: relay has 2 interfaces: eth0 and eth1. Clients are located on the eth1 network. Relay should receive data on that interface using well-known ALL_DHCP_RELAYS_AND_SERVER multicast address (ff02::1:2). Relay also listens on its global address 2000::123. Packets received on the eth1 should be forwarded on the eth0 interface, also using multicast address: </p>
<pre>log-level 8
log-mode short
iface eth0 {
 server multicast yes
}
iface eth1 {
 client multicast yes
 client unicast 2000::123
 interface-id 1000
}</pre>
<p>Here is another exmaple. This time messages should be forwarded from eth1 and eth3 to the eth0 interface (using multicast) and to the eth2 interface (using server&#8217;s global address 2000::546). Also clients must use multicasts (the default approach): </p>
<pre>iface eth0 {
 server multicast yes
}
iface eth2 {
 server unicast 2000::456
}
iface eth1 {
 client multicast yes 
 interface-id 1000
}
iface eth3 {
 client multicast yes 
 interface-id 1001
}</pre>
<h2>Files</h2>
<p>All files are created in the /var/lib/dibbler directory. During operation, Dibbler saves various file in that directory. Dibbler relay reads /etc/dibbler/relay.conf file. Log file is named client.log.</p>
<h2>Standards</h2>
<p>This implementation aims at conformance to the following standards: </p>
<p> <i>RFC 3315 </i> DHCP for IPv6 </p>
<p> <i>RFC 3736</i> Stateless DHCPv6</p>
<h2>Bugs</h2>
<p>Bugs are tracked with bugzilla, available at <i><a rel="nofollow" href="http://klub.com.pl/bugzilla/">http://klub.com.pl/bugzilla/</a></i>. If you belive you have found a bug, don&#8217;t hesitate to report it. </p>
<h2>Author</h2>
<p>Dibbler was developed as master thesis on the Technical University of Gdansk by Tomasz Mrugalski and Marek Senderski. Currently Marek has not enough free time, so this project is being developed by Tomasz Mrugalski. Author can be reached at thomson [at] klub.com.pl.</p>
<h2>See Also</h2>
<p>There are <a href="/docs/linux/man/8-dibbler-server/">dibbler-server</a>(8) and <a href="/docs/linux/man/8-dibbler-client/">dibbler-client</a>(8) manual pages available. You are also advised to take a look at project website located at <i><a rel="nofollow" href="http://klub.com.pl/dhcpv6/">http://klub.com.pl/dhcpv6/</a></i>. As far as authors know, this is the only Windows DHCPv6 stateful implementation available and the only one with relay support. It is also one of two freely available under Linux. The other Linux implementation is available at <i><a rel="nofollow" href="http://dhcpv6.sourceforge.net">http://dhcpv6.sourceforge.net</a></i>, but it is rather outdated and seems not being actively developed. </p>
