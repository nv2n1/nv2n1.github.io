---
title: "batctl(8)"
name: "batctl"
section: "8"
letter: "b"
url: "/docs/linux/man/8-batctl/"
description: "batctl – B.A.T.M.A.N. advanced control and management tool"
---

<p>batctl &#8211; B.A.T.M.A.N. advanced control and management tool</p>
<h2>Synopsis</h2>
<p><code>batctl [</code><i>options</i>]&nbsp;<wbr><i>command</i>|<i>debug table</i>&nbsp;<wbr>[<i>parameters</i>]</p>
<h2>Description</h2>
<p>batctl offers a convenient way to configure the batman-adv kernel module as well as displaying debug information such as originator tables, translation tables and the debug log. In combination with a bat-hosts file batctl allows the use of host names instead of MAC addresses. B.A.T.M.A.N. advanced operates on layer 2. Thus all hosts participating in the virtual switched network are transparently connected together for all protocols above layer 2. Therefore the common diagnosis tools do not work as expected. To overcome these problems batctl contains the commands <code>ping</code>, <code>traceroute</code>, <code>tcpdump</code> which provide similar functionality to the normal <code><a href="/docs/linux/man/1-ping/">ping</a></code>(1), <code><a href="/docs/linux/man/1-traceroute/">traceroute</a></code>(1), <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1) commands, but modified to layer 2 behaviour or using the B.A.T.M.A.N. advanced protocol. For similar reasons, <code>throughputmeter</code>, a command to test network performances, is also included. </p>
<h2>Options</h2>
<dl>
<dt><i></i><code>options:</code></p>
<dd>-m specify mesh interface or VLAN created on top of a mesh interface (default &#8216;bat0&#8217;)<br />
 -h print general batctl help<br />
 -v print batctl version and batman-adv version (if the module is loaded) </p>
<dt><i></i><code>commands:</code></p>
<dd>
<dt><code>interface</code>|<code>if</code> [<code>add</code>|<code>del iface(s)</code>]</p>
<dd>If no parameter is given or the first parameter is neither &quot;add&quot; nor &quot;del&quot; the current interface settings are displayed. In order to add or delete interfaces specify &quot;add&quot; or &quot;del&quot; as first argument and append the interface names you wish to add or delete. Multiple interfaces can be specified. </p>
<dt><code>orig_interval</code>|<code>it</code> [<code>interval</code>]</p>
<dd>If no parameter is given the current originator interval setting is displayed otherwise the parameter is used to set the originator interval. The interval is in units of milliseconds. </p>
<dt><code>ap_isolation</code>|<code>ap</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current ap isolation setting is displayed. Otherwise the parameter is used to enable or disable ap isolation. This command can be used in conjunction with &quot;-m&quot; option to target per VLAN configurations. </p>
<dt><code>bridge_loop_avoidance</code>|<code>bl</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current bridge loop avoidance setting is displayed. Otherwise the parameter is used to enable or disable the bridge loop avoidance. Bridge loop avoidance support has to be enabled when compiling the module otherwise this option won&#8217;t be available. </p>
<dt><code>distributed_arp_table</code>|<code>dat</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current distributed arp table setting is displayed. Otherwise the parameter is used to enable or disable the distributed arp table. </p>
<dt><code>aggregation</code>|<code>ag</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current aggregation setting is displayed. Otherwise the parameter is used to enable or disable OGM packet aggregation. </p>
<dt><code>bonding</code>|<code>b</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current bonding mode setting is displayed. Otherwise the parameter is used to enable or disable the bonding mode. </p>
<dt><code>fragmentation</code>|<code>f</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current fragmentation mode setting is displayed. Otherwise the parameter is used to enable or disable fragmentation. </p>
<dt><code>network_coding</code>|<code>nc</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current network coding mode setting is displayed. Otherwise the parameter is used to enable or disable network coding. </p>
<dt><code>multicast_mode</code>|<code>mm</code> [<code>0</code>|<code>1</code>]</p>
<dd>If no parameter is given the current multicast mode setting is displayed. Otherwise the parameter is used to enable or disable multicast optimizations (i.e. disabling means always sending own multicast frames via classic flooding). </p>
<dt><code>loglevel</code>|<code>ll</code> [<code>level</code>[ <code>level</code>[ <code>level</code>]] <code>&#8230;</code>]</p>
<dd>If no parameter is given the current log level settings are displayed otherwise the parameter(s) is/are used to set the log level. Level &#8216;none&#8217; disables all verbose logging. Level &#8216;batman&#8217; enables messages related to routing / flooding / broadcasting. Level &#8216;routes&#8217; enables messages related to routes being added / changed / deleted. Level &#8216;tt&#8217; enables messages related to translation table operations. Level &#8216;bla&#8217; enables messages related to the bridge loop avoidance. Level &#8216;dat&#8217; enables messages related to ARP snooping and the Distributed Arp Table. Level &#8216;nc&#8217; enables messages related to network coding. Level &#8216;mcast&#8217; enables messages related to multicast optimizations. Level &#8216;all&#8217; enables all messages. The messages are sent to the batman-adv debug log. Use <code>batctl log</code> to retrieve it. Make sure to have debugging output enabled when compiling the module otherwise the output as well as the loglevel options won&#8217;t be available. </p>
<dt><code>log</code>|<code>l</code> [<code>-n</code>]</p>
<dd>batctl will read the batman-adv debug log which has to be compiled into the kernel module. If &quot;-n&quot; is given batctl will not replace the MAC addresses with bat-host names in the output. </p>
<dt><code>gw_mode|gw</code> [<code>off</code>|<code>client</code>|<code>server</code>] [<code>sel_class|bandwidth</code>]</p>
<dd>If no parameter is given the current gateway mode is displayed otherwise the parameter is used to set the gateway mode. The second (optional) argument specifies the selection class (if &#8216;client&#8217; was the first argument) or the gateway bandwidth (if &#8216;server&#8217; was the first argument). If the node is a server this parameter is used to inform other nodes in the network about this node&#8217;s internet connection bandwidth. Just enter any number (optionally followed by &quot;kbit&quot; or &quot;mbit&quot;) and the batman-adv module will propagate the entered value in the mesh. Use &quot;/&quot; to separate the down- and upload rates. You can omit the upload rate and the module will assume an upload of download / 5.</p>
<dl>
<dd>default: 10000 -&gt; 10.0/2.0 MBit</dl>
<dl>
<dd>examples: 5000 -&gt; 5.0/1.0 MBit</dl>
<dl>
<dd>&nbsp;<wbr>5000kbit<br />
&nbsp;<wbr>5mbit<br />
&nbsp;<wbr>5mbit/1024<br />
&nbsp;<wbr>5mbit/1024kbit<br />
&nbsp;<wbr>5mbit/1mbit</dl>
<dl>
<dd>If the node is a gateway client the parameter will decide which criteria to consider when the batman-adv module has to choose between different internet connections announced by the aforementioned servers.</dl>
<dl>
<dd>default: 20 -&gt; late switch (TQ 20)</dl>
<dl>
<dd>examples: 1 -&gt; fast connection</p>
<dl>
<dd>consider the gateway&#8217;s advertised throughput as well as the link quality towards the gateway and stick with the selection until the gateway disappears</dl>
</dl>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>2 -&gt;&nbsp;<wbr>stable connection</p>
<dl>
<dd>chooses the gateway with the best link quality and sticks with it (ignore the advertised throughput)</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>3 -&gt;&nbsp;<wbr>fast switch connection</p>
<dl>
<dd>chooses the gateway with the best link quality but switches to another gateway as soon as a better one is found</dl>
<p>&nbsp;<wbr>XX -&gt;&nbsp;<wbr>late switch connection</p>
<dl>
<dd>chooses the gateway with the best link quality but switches to another gateway as soon as a better one is found which is at least XX TQ better than the currently selected gateway (XX has to be a number between 3 and 256).</dl>
</dl>
<dt><code>routing_algo</code>|<code>ra</code> [<code>algorithm</code>]</p>
<dd>If no parameter is given the current routing algorithm configuration as well as supported routing algorithms are displayed. Otherwise the parameter is used to select the routing algorithm for the following batX interface to be created. </p>
<dt><code>isolation_mark</code>|<code>mark</code></p>
<dd>If no parameter is given the current isolation mark value is displayed. Otherwise the parameter is used to set or unset the isolation mark used by the Extended Isolation feature.<br />
 The input is supposed to be of the form $value/$mask, where $value can be any 32bit long integer (expressed in decimal or hex base) and $mask is a generic bitmask (expressed in hex base) that selects the bits to take into consideration from $value. It is also possible to enter the input using only $value and in this case the full bitmask is used by default. </p>
<p> Example 1: 0x00000001/0xffffffff<br />
 Example 2: 0x00040000/0xffff0000<br />
 Example 3: 16 or 0x0F </p>
</dl>
<p> <i></i><code>debug tables:</code></p>
<dl>
<dd>The batman-adv kernel module comes with a variety of debug tables containing various information about the state of the mesh seen by each individual node. These tables are exported via debugfs and easily accessible via batctl. You will need debugfs support compiled into your kernel and preferably have mounted the debugfs to a well-known mountpoint. If debugfs is not mounted batctl will attempt to do this step for you. </p>
<p> All of the debug tables support the following options:</p>
<dl>
<dd>-w refresh the list every second or add a number to let it refresh at a custom interval in seconds (with optional decimal places)</dl>
<dl>
<dd>-n do not replace the MAC addresses with bat-host names in the output</dl>
<dl>
<dd>-H do not show the header of the debug table</dl>
<dl>
<dd>The originator table also supports the &quot;-t&quot; filter option to remove all originators from the output that have not been seen for the specified amount of seconds (with optional decimal places). It furthermore supports the &quot;-i&quot; parameter to specify an interface for which the originator table should be printed. If this parameter is not supplied, the default originator table is printed. </p>
<p> The local and global translation tables also support the &quot;-u&quot; and &quot;-m&quot; option to only display unicast or multicast translation table announcements respectively. </p>
<p> List of debug tables:</p>
<dl>
<dd>&#8211; neighbors|n</dl>
<dl>
<dd>&#8211; originators|o</dl>
<dl>
<dd>&#8211; gateways|gwl</dl>
<dl>
<dd>&#8211; translocal|tl</dl>
<dl>
<dd>&#8211; transglobal|tg</dl>
<dl>
<dd>&#8211; claimtable|cl (compile time option)</dl>
<dl>
<dd>&#8211; backbonetable|bbt (compile time option)</dl>
<dl>
<dd>&#8211; dat_cache|dc (compile time option)</dl>
<dl>
<dd>&#8211; nc_nodes|nn (compile time option)</dl>
<dl>
<dd>&#8211; mcast_flags|mf (compile time option)</dl>
</dl>
<dt><code>translate</code>|<code>t</code> <code>MAC_address</code>|<code>bat-host_name</code>|<code>host_name</code>|<code>IP_address</code></p>
<dd>Translates a destination (hostname, IP, MAC, bat_host-name) to the originator mac address responsible for it. </p>
<dt><code>statistics</code>|<code>s</code></p>
<dd>Retrieve traffic counters from batman-adv kernel module. The output may vary depending on which features have been compiled into the kernel module.<br />
 Each module subsystem has its own counters which are indicated by their prefixes:</p>
<dl>
<dd>mgmt &#8211; mesh protocol counters</dl>
<dl>
<dd>tt &#8211; translation table counters</dl>
<dl>
<dd>All counters without a prefix concern payload (pure user data) traffic.</dl>
<dt><code>ping</code>|<code>p</code> [<code>-c count</code>][<code>-i interval</code>][<code>-t time</code>][<code>-R</code>][<code>-T</code>] <code>MAC_address</code>|<code>bat-host_name</code>|<code>host_name</code>|<code>IP_address</code></p>
<dd>Layer 2 ping of a MAC address or bat-host name. batctl will try to find the bat-host name if the given parameter was not a MAC address. It can also try to guess the MAC address using an IPv4/IPv6 address or a hostname when the IPv4/IPv6 address was configured on top of the batman-adv interface of the destination device and both source and destination devices are in the same IP subnet. The &quot;-c&quot; option tells batctl how man pings should be sent before the program exits. Without the &quot;-c&quot; option batctl will continue pinging without end. Use CTRL + C to stop it. With &quot;-i&quot; and &quot;-t&quot; you can set the default interval between pings and the timeout time for replies, both in seconds. When run with &quot;-R&quot;, the route taken by the ping messages will be recorded. With &quot;-T&quot; you can disable the automatic translation of a client MAC address to the originator address which is responsible for this client. </p>
<dt><code>traceroute</code>|<code>tr</code> [<code>-n</code>][<code>-T</code>] <code>MAC_address</code>|<code>bat-host_name</code>|<code>host_name</code>|<code>IP_address</code></p>
<dd>Layer 2 traceroute to a MAC address or bat-host name. batctl will try to find the bat-host name if the given parameter was not a MAC address. It can also try to guess the MAC address using an IPv4/IPv6 address or a hostname when the IPv4/IPv6 address was configured on top of the batman-adv interface of the destination device and both source and destination devices are in the same IP subnet. batctl will send 3 packets to each host and display the response time. If &quot;-n&quot; is given batctl will not replace the MAC addresses with bat-host names in the output. With &quot;-T&quot; you can disable the automatic translation of a client MAC address to the originator address which is responsible for this client. </p>
<dt><code>tcpdump</code>|<code>td</code> [<code>-c</code>][<code>-n</code>][<code>-p filter</code>][<code>-x filter</code>] <code>interface &#8230;</code></p>
<dd>batctl will display all packets that are seen on the given interface(s). A variety of options to filter the output are available: To only print packets that match the compatibility number of batctl specify the &quot;-c&quot; (compat filter) option. If &quot;-n&quot; is given batctl will not replace the MAC addresses with bat-host names in the output. To filter the shown packet types you can either use &quot;-p&quot; (dump only specified packet types) or &quot;-x&quot; (dump all packet types except specified). The following packet types are available:</p>
<dl>
<dd>1 &#8211; batman ogm packets</dl>
<dl>
<dd>2 &#8211; batman icmp packets</dl>
<dl>
<dd>4 &#8211; batman unicast packets</dl>
<dl>
<dd>8 &#8211; batman broadcast packets</dl>
<dl>
<dd>16 &#8211; batman unicast tvlv packets</dl>
<dl>
<dd>32 &#8211; batman fragmented packets</dl>
<dl>
<dd>64 &#8211; batman tt / roaming packets</dl>
<dl>
<dd>128 &#8211; non batman packets</dl>
<dl>
<dd>Example: batctl td &lt;interface&gt; -p 129 -&gt; only display batman ogm packets and non batman packets</dl>
<dt><code>bisect_iv</code> [<code>-l MAC</code>][<code>-t MAC</code>][<code>-r MAC</code>][<code>-s min</code> [<code>&#8211; max</code>]][<code>-o MAC</code>][<code>-n</code>] <code>logfile1</code> [<code>logfile2</code> &#8230; <code>logfileN</code>]</p>
<dd>Analyses the B.A.T.M.A.N. IV logfiles to build a small internal database of all sent sequence numbers and routing table changes. This database can then be analyzed in a number of different ways. With &quot;-l&quot; the database can be used to search for routing loops. Use &quot;-t&quot; to trace OGMs of a host throughout the network. Use &quot;-r&quot; to display routing tables of the nodes. The option &quot;-s&quot; can be used to limit the output to a range of sequence numbers, between min and max, or to one specific sequence number, min. Furthermore using &quot;-o&quot; you can filter the output to a specified originator. If &quot;-n&quot; is given batctl will not replace the MAC addresses with bat-host names in the output. </p>
<dt><code>throughputmeter</code>|<code>tp</code> <code>MAC</code></p>
<dd>This command starts a throughput test entirely controlled by batman module in kernel space: the computational resources needed to align memory and copy data between user and kernel space that are required by other user space tools may represent a bootleneck on some low profile device. </p>
<p> The test consist of the transfer of 14 MB of data between the two nodes. The protocol used to transfer the data is somehow similar to TCP, but simpler: some TCP features are still missing, thus protocol performances could be worst. Since a fixed amount of data is transferred the experiment duration depends on the network conditions. The experiment can be interrupted with CTRL + C. At the end of a successful experiment the throughput in KBytes per second is returned, togheter with the experiment duration in millisecond and the amount of bytes transferred. If too many packets are lost or the specified MAC address is not reachable, a message notifing the error is returned instead of the result.
</dl>
<h2>Files</h2>
<dl>
<dt><i></i><code>bat-hosts</code></p>
<dd>This file is similar to the /etc/hosts file. You can write one MAC address and one host name per line. batctl will search for bat-hosts in /etc, your home directory and the current directory. The found data is used to match MAC address to your provided host name or replace MAC addresses in debug output and logs. Host names are much easier to remember than MAC addresses.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ping/">ping</a></code>(1), <code><a href="/docs/linux/man/1-traceroute/">traceroute</a></code>(1), <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1), <code><a href="/docs/linux/man/1-dmesg/">dmesg</a></code>(1), <code><a href="/docs/linux/man/1-dot/">dot</a></code>(1)</p>
<h2>Author</h2>
<p>batctl was written by Andreas Langer &lt;an.langer [at] gmx.de&gt; and Marek Lindner &lt;mareklindner [at] neomailbox.ch&gt;. </p>
<p> This manual page was written by Simon Wunderlich &lt;sw [at] simonwunderlich.de&gt;, Marek Lindner &lt;mareklindner [at] neomailbox.ch&gt; and Andrew Lunn &lt;andrew [at] lunn.ch&gt;</p>
