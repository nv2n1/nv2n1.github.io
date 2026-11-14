---
title: "ettercap(8)"
name: "ettercap"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ettercap/"
description: "ettercap NG-0.7.3 – A multipurpose sniffer/content filter for man in the middle attacks"
---

<p><code>ettercap NG-0.7.3 </code> &#8211; A multipurpose sniffer/content filter for man in the middle attacks </p>
<h2>***** Important Note ******</h2>
<p>Since ettercap NG (formerly 0.7.0), all the options have been changed. Even the target specification has been changed. <i>Please read carefully this man page.</i></p>
<h2>Synopsis</h2>
<p><code>ettercap</code> [<i>OPTIONS</i>] [<i>TARGET1</i>] [<i>TARGET2</i>] </p>
<p> <i>TARGET</i> is in the form <i>MAC/IPs/PORTs</i><br />
 where IPs and PORTs can be ranges (e.g. /192.168.0.1-30,40,50/20,22,25)</p>
<h2>Description</h2>
<p>Ettercap was born as a sniffer for switched LAN (and obviously even &quot;hubbed&quot; ones), but during the development process it has gained more and more features that have changed it to a powerful and flexible tool for man-in-the-middle attacks. It supports active and passive dissection of many protocols (even ciphered ones) and includes many features for network and host analysis (such as OS fingerprint). It has two main sniffing options: <i>UNIFIED</i>, this method sniffs all the packets that pass on the cable. You can choose to put or not the interface in promisc mode (-p option). The packet not directed to the host running ettercap will be forwarded automatically using layer 3 routing. So you can use a mitm attack launched from a different tool and let ettercap modify the packets and forward them for you.<br />
 The kernel ip_forwarding is always disabled by ettercap. This is done to prevent to forward a packet twice (one by ettercap and one by the kernel). This is an invasive behaviour on gateways. So we recommend you to use ettercap on the gateways ONLY with the UNOFFENSIVE MODE ENABLED. Since ettercap listens only on one network interface, launching it on the gateway in offensive mode will not allow packets to be rerouted back from the second interface. <i>BRIDGED</i>, it uses two network interfaces and forward the traffic from one to the other while performing sniffing and content filtering. This sniffing method is totally stealthy since there is no way to find that someone is in the middle on the cable. You can look at this method as a mitm attack at layer 1. You will be in the middle of the cable between two entities. Don&#8217;t use it on gateways or it will transform your gateway into a bridge. HINT: you can use the content filtering engine to drop packets that should not pass. This way ettercap will work as an inline IPS ;) You can also perform man in the middle attacks while using the unified sniffing. You can choose the mitm attack that you prefer. The mitm attack module is independent from the sniffing and filtering process, so you can launch several attacks at the same time or use your own tool for the attack. The crucial point is that the packets have to arrive to ettercap with the correct mac address and a different ip address (only these packets will be forwarded). The most relevant ettercap features are: <code>SSH1 support :</code> you can sniff User and Pass, and even the data of an SSH1 connection. ettercap is the first software capable to sniff an SSH connection in FULL-DUPLEX <code>SSL support :</code> you can sniff SSL secured data&#8230; a fake certificate is presented to the client and the session is decrypted. <code>Characters injection in an established connection :</code> you can inject characters to the server (emulating commands) or to the client (emulating replies) maintaining the connection alive !! <code>Packet filtering/dropping:</code> You can set up a filter script that searches for a particular string (even hex) in the TCP or UDP payload and replace it with yours or drop the entire packet. The filtering engine can match any field of the network protocols and modify whatever you want (see <a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)). <code>Remote traffic sniffing through tunnels and route mangling:</code> You can play with linux cooked interfaces or use the integrated plugin to sniff tunneled or route-mangled remote connections and perform mitm attacks on them. <code>Plug-ins support :</code> You can create your own plugin using the ettercap&#8217;s API. <code>Password collector for :</code> TELNET, FTP, POP, RLOGIN, SSH1, ICQ, SMB, MySQL, HTTP, NNTP, X11, NAPSTER, IRC, RIP, BGP, SOCKS 5, IMAP 4, VNC, LDAP, NFS, SNMP, HALF LIFE, QUAKE 3, MSN, YMSG (other protocols coming soon&#8230;) <code>Passive OS fingerprint:</code> you scan passively the lan (without sending any packet) and gather detailed info about the hosts in the LAN: Operating System, running services, open ports, IP, mac address and network adapter vendor. <code>Kill a connection:</code> from the connections list you can kill all the connections you want </p>
<h2>Target Specification</h2>
<p>There is no concept of SOURCE nor DEST. The two targets are intended to filter traffic coming from one to the other and vice-versa (since the connection is bidirectional). </p>
<p> <i>TARGET</i> is in the form <i>MAC/IPs/PORTs</i>. If you want you can omit any of its parts and this will represent an ANY in that part.<br />
 e.g.<br />
 &quot;//80&quot; means ANY mac address, ANY ip and ONLY port 80<br />
 &quot;/10.0.0.1/&quot; means ANY mac address, ONLY ip 10.0.0.1 and ANY port </p>
<p> <i>MAC</i> must be unique and in the form 00:11:22:33:44:55 </p>
<p> <i>IPs</i> is a range of IP in dotted notation. You can specify range with the &#8211; (hyphen) and single ip with , (comma). You can also use ; (semicolon) to indicate different ip addresses.<br />
 e.g.<br />
 &quot;10.0.0.1-5;10.0.1.33&quot; expands into ip 10.0.0.1, 2, 3, 4, 5 and 10.0.1.33 </p>
<p> <i>PORTs</i> is a range of PORTS. You can specify range with the &#8211; (hyphen) and single port with , (comma).<br />
 e.g.<br />
 &quot;20-25,80,110&quot; expands into ports 20, 21, 22, 23, 24, 25, 80 and 110 </p>
<p> <code>NOTE:</code><br />
 you can reverse the matching of the TARGET by adding the -R option to the command line. So if you want to sniff ALL the traffic BUT the one coming or going to 10.0.0.1 you can specify &quot;./ettercap -R /10.0.0.1/&quot; </p>
<p> <code>NOTE:</code><br />
 TARGETs are also responsible of the initial scan of the lan. You can use them to restrict the scan to only a subset of the hosts in the netmask. The result of the merging between the two targets will be scanned. remember that not specifying a target means &quot;no target&quot;, but specifying &quot;//&quot; means &quot;all the hosts in the subnet.</p>
<h2>Privileges Dropping</h2>
<p>ettercap needs root privileges to open the Link Layer sockets. After the initialization phase, the root privs are not needed anymore, so ettercap drops them to UID = 65535 (nobody). Since ettercap has to write (create) log files, it must be executed in a directory with the right permissions (e.g. /tmp/). If you want to drop privs to a different uid, you can export the environment variable EC_UID with the value of the uid you want to drop the privs to (e.g. export EC_UID=500) or set the correct parameter in the etter.conf file.</p>
<h2>Ssl Mitm Attack</h2>
<p>While performing the SSL mitm attack, ettercap substitutes the real ssl certificate with its own. The fake certificate is created on the fly and all the fields are filled according to the real cert presented by the server. Only the issuer is modified and signed with the private key contained in the &#8216;etter.sll.crt&#8217; file. If you want to use a different private key you have to regenerate this file. To regenerate the cert file use the following commands: </p>
<p> openssl genrsa -out etter.ssl.crt 1024<br />
 openssl req -new -key etter.ssl.crt -out tmp.csr<br />
 openssl x509 -req -days 1825 -in tmp.csr -signkey etter.ssl.crt -out tmp.new<br />
 cat tmp.new &gt;&gt; etter.ssl.crt<br />
 rm -f tmp.new tmp.csr NOTE: SSL mitm is not available (for now) in bridged mode.</p>
<h2>Options</h2>
<p>Options that make sense together can generally be combined. ettercap will warn the user about unsupported option combinations.</p>
<dl>
<dt><code>SNIFFING AND ATTACK OPTIONS</code></p>
<dd></dl>
<p> ettercap NG has a new unified sniffing method. This implies that ip_forwarding in the kernel is always disabled and the forwarding is done by ettercap. Every packet with destination mac address equal to the host&#8217;s mac address and destination ip address different for the one bound to the iface will be forwarded by ettercap. Before forwarding them, ettercap can content filter, sniff, log or drop them. It does not matter how these packets are hijacked, ettercap will process them. You can even use external programs to hijack packet.<br />
 You have full control of what ettercap should receive. You can use the internal mitm attacks, set the interface in promisc mode, use plugins or use every method you want. </p>
<p> IMPORTANT NOTE: if you run ettercap on a gateway, remember to re-enable the ip_forwarding after you have killed ettercap. Since ettercap drops its privileges, it cannot restore the ip_forwarding for you.</p>
<dl>
<dt><code>-M</code>, <code>&#8211;mitm &lt;METHOD:ARGS&gt;</code></p>
<dd>MITM attack<br />
 This option will activate the man in the middle attack. The mimt attack is totally independent from the sniffing. The aim of the attack is to hijack packets and redirect them to ettercap. The sniffing engine will forward them if necessary.<br />
 You can choose the mitm attack that you prefer and also combine some of them to perform different attacks at the same time.<br />
 If a mitm method requires some parameters you can specify them after the colon. (e.g. -M dhcp:ip_pool,netmask,etc ) </p>
<p> The following mitm attacks are available:</p>
<dl>
<dd>
<dl>
<dt><code>arp</code> ([remote],[oneway])</p>
<dd>This method implements the ARP poisoning mitm attack. ARP requests/replies are sent to the victims to poison their ARP cache. Once the cache has been poisoned the victims will send all packets to the attacker which, in turn, can modify and forward them to the real destination. </p>
<p> In silent mode (-z option) only the first target is selected, if you want to poison multiple target in silent mode use the -j option to load a list from a file. </p>
<p> You can select empty targets and they will be expanded as &#8216;ANY&#8217; (all the hosts in the LAN). The target list is joined with the hosts list (created by the arp scan) and the result is used to determine the victims of the attack. </p>
<p> The parameter &quot;remote&quot; is optional and you have to specify it if you want to sniff remote ip address poisoning a gateway. Indeed if you specify a victim and the gw in the TARGETS, ettercap will sniff only connection between them, but to enable ettercap to sniff connections that pass thru the gw, you have to use this parameter. </p>
<p> The parameter &quot;oneway&quot; will force ettercap to poison only from TARGET1 to TARGET2. Useful if you want to poison only the client and not the router (where an arp watcher can be in place). </p>
<p> Example: </p>
<p> the targets are: /10.0.0.1-5/ /10.0.0.15-20/<br />
 and the host list is: 10.0.0.1 10.0.0.3 10.0.0.16 10.0.0.18 </p>
<p> the associations between the victims will be:<br />
 1 and 16, 1 and 18, 3 and 16, 3 and 18 </p>
<p> if the targets overlap each other, the association with identical ip address will be skipped. </p>
<p> NOTE: if you manage to poison a client, you have to set correct routing table in the kernel specifying the GW. If your routing table is incorrect, the poisoned clients will not be able to navigate the Internet. </p>
<dt><code>icmp</code> (MAC/IP)</p>
<dd>This attack implements ICMP redirection. It sends a spoofed icmp redirect message to the hosts in the lan pretending to be a better route for internet. All connections to internet will be redirected to the attacker which, in turn, will forward them to the real gateway. The resulting attack is a HALF-DUPLEX mitm. Only the client is redirected, since the gateway will not accept redirect messages for a directly connected network. BE SURE TO NOT USE FILTERS THAT MODIFY THE PAYLOAD LENGTH. you can use a filter to modify packets, but the length must be the same since the tcp sequences cannot be updated in both ways.<br />
 You have to pass as argument the MAC and the IP address of the real gateway for the lan.<br />
 Obviously you have to be able to sniff all the traffic. If you are on a switch you have to use a different mitm attack such as arp poisoning. </p>
<p> NOTE: to restrict the redirection to a given target, specify it as a TARGET </p>
<p> Example: </p>
<p> -M icmp:00:11:22:33:44:55/10.0.0.1 </p>
<p> will redirect all the connections that pass thru that gateway. </p>
<dt><code>dhcp</code> (ip_pool/netmask/dns)</p>
<dd>This attack implements DHCP spoofing. It pretends to be a DHCP server and tries to win the race condition with the real one to force the client to accept the attacker&#8217;s reply. This way ettercap is able to manipulate the GW parameter and hijack all the outgoing traffic generated by the clients.<br />
 The resulting attack is a HALF-DUPLEX mitm. So be sure to use appropriate filters (see above in the ICMP section). </p>
<p> You have to pass the ip pool to be used, the netmask and the ip of the dns server. Since ettercap tries to win the race with the real server, it DOES NOT CHECK if the ip is already assigned. You have to specify an ip pool of FREE addresses to be used. The ip pool has the same form of the target specification. </p>
<p> If the client sends a dhcp request (suggesting an ip address) ettercap will ack on that ip and modify only the gw option. If the client makes a dhcp discovery, ettercap will use the first unused ip address of the list you have specified on command line. Every discovery consumes an ip address. When the list is over, ettercap stops offering new ip addresses and will reply only to dhcp requests.<br />
 If you don&#8217;t want to offer any ip address, but only change the router information of dhcp request/ack, you can specify an empty ip_pool. </p>
<p> BIG WARNING: if you specify a list of ip that are in use, you will mess your network! In general, use this attack carefully. It can really mess things up! When you stop the attack, all the victims will be still convinced that ettercap is the gateway until the lease expires&#8230; </p>
<p> Example: </p>
<p> -M dhcp:192.168.0.30,35,50-60/255.255.255.0/192.168.0.1<br />
 reply to DHCP offer and request. </p>
<p> -M dhcp:/255.255.255.0/192.168.0.1<br />
 reply only to DHCP request. </p>
<dt><code>port</code> ([remote],[tree])</p>
<dd>This attack implements Port Stealing. This technique is useful to sniff in a switched environment when ARP poisoning is not effective (for example where static mapped ARPs are used). </p>
<p> It floods the LAN (based on port_steal_delay option in etter.conf) with ARP packets. If you don&#8217;t specify the &quot;tree&quot; option, the destination MAC address of each &quot;stealing&quot; packet is the same as the attacker&#8217;s one (other NICs won&#8217;t see these packets), the source MAC address will be one of the MACs in the host list. This process &quot;steals&quot; the switch port of each victim host in the host list. Using low delays, packets destined to &quot;stolen&quot; MAC addresses will be received by the attacker, winning the race condition with the real port owner. When the attacker receives packets for &quot;stolen&quot; hosts, it stops the flooding process and performs an ARP request for the real destination of the packet. When it receives the ARP reply it&#8217;s sure that the victim has &quot;taken back&quot; his port, so ettercap can re-send the packet to the destination as is. Now we can re-start the flooding process waiting for new packets. </p>
<p> If you use the &quot;tree&quot; option, the destination MAC address of each stealing packet will be a bogus one, so these packets will be propagated to other switches (not only the directly connected one). This way you will be able to steal ports on other switches in the tree (if any), but you will generate a huge amount of traffic (according to port_steal_delay). The &quot;remote&quot; option has the same meaning as in &quot;arp&quot; mitm method. </p>
<p> When you stop the attack, ettercap will send an ARP request to each stolen host giving back their switch ports.<br />
 You can perform either HALF or FULL DUPLEX mitm according to target selection. </p>
<p> NOTE: Use this mitm method only on ethernet switches. Use it carefully, it could produce performances loss or general havoc. </p>
<p> NOTE: You can NOT use this method in only-mitm mode (-o flag), because it hooks the sniffing engine, and you can&#8217;t use interactive data injection. </p>
<p> NOTE: It could be dangerous to use it in conjunction with other mitm methods. </p>
<p> NOTE: This mitm method doesn&#8217;t work on Solaris and Windows because of the lipcap and libnet design and the lack of certain ioctl(). (We will feature this method on these OSes if someone will request it&#8230;) </p>
<p> Example: </p>
<p> The targets are: /10.0.0.1/ /10.0.0.15/<br />
 You will intercept and visualize traffic between 10.0.0.1 and 10.0.0.15, but you will receive all the traffic for 10.0.0.1 and 10.0.0.15 too. </p>
<p> The target is: /10.0.0.1/<br />
 You will intercept and visualize all the traffic for 10.0.0.1. </p>
</dl>
</dl>
<dt><code>-o</code>, <code>&#8211;only-mitm</code></p>
<dd>This options disables the sniffing thread and enables only the mitm attack. Useful if you want to use ettercap to perform mitm attacks and another sniffer (such as ethereal) to sniff the traffic. Keep in mind that the packets are not forwarded by ettercap. The kernel will be responsible for the forwarding. Remember to activate the &quot;ip forwarding&quot; feature in your kernel. </p>
<dt><code>-f</code>, <code>&#8211;pcapfilter &lt;FILTER&gt;</code></p>
<dd>Set a capturing filter in the pcap library. The format is the same as <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1). Remember that this kind of filter will not sniff packets out of the wire, so if you want to perform a mitm attack, ettercap will not be able to forward hijacked packets.<br />
 These filters are useful to decrease the network load impact into ettercap decoding module. </p>
<dt><code>-B</code>, <code>&#8211;bridge &lt;IFACE&gt;</code></p>
<dd>BRIDGED sniffing<br />
 You need two network interfaces. ettercap will forward form one to the other all the traffic it sees. It is useful for man in the middle at the physical layer. It is totally stealthy since it is passive and there is no way for an user to see the attacker.<br />
 You can content filter all the traffic as you were a transparent proxy for the &quot;cable&quot;. </p>
<dt><code>OFF LINE SNIFFING</code></p>
<dd>
<dt><code>-r</code>, <code>&#8211;read &lt;FILE&gt;</code></p>
<dd>OFF LINE sniffing<br />
 With this option enabled, ettercap will sniff packets from a pcap compatible file instead of capturing from the wire.<br />
 This is useful if you have a file dumped from tcpdump or ethereal and you want to make an analysis (search for passwords or passive fingerprint) on it.<br />
 Obviously you cannot use &quot;active&quot; sniffing (arp poisoning or bridging) while sniffing from a file.</p>
<dt><code>-w</code>, <code>&#8211;write &lt;FILE&gt;</code></p>
<dd>WRITE packet to a pcap file<br />
 This is useful if you have to use &quot;active&quot; sniffing (arp poison) on a switched LAN but you want to analyze the packets with tcpdump or ethereal. You can use this option to dump the packets to a file and then load it into your favourite application. </p>
<p> NOTE: dump file collect ALL the packets disregarding the TARGET. This is done because you may want to log even protocols not supported by ettercap, so you can analyze them with other tools. </p>
<p> TIP: you can use the -w option in conjunction with the -r one. This way you will be able to filter the payload of the dumped packets or decrypt WEP-encrypted WiFi traffic and dump them to another file. </p>
<dt><code>USER INTERFACES OPTIONS</code></p>
<dd>
<dt><code>-T</code>, <code>&#8211;text</code></p>
<dd>The text only interface, only printf ;)<br />
 It is quite interactive, press &#8216;h&#8217; in every moment to get help on what you can do. </p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Quiet mode. It can be used only in conjunction with the console interface. It does not print packet content. It is useful if you want to convert pcap file to ettercap log files. </p>
<p> example: </p>
<p> ettercap -Tq -L dumpfile -r pcapfile </p>
<dt><code>-s</code>, <code>&#8211;script &lt;COMMANDS&gt;</code></p>
<dd>With this option you can feed ettercap with command as they were typed on the keyboard by the user. This way you can use ettercap within your favourite scripts. There is a special command you can issue thru this command: s(x). this command will sleep for x seconds. </p>
<p> example: </p>
<p> ettercap -T -s &#8216;lq&#8217; will print the list of the hosts and exit<br />
 ettercap -T -s &#8216;s(300)olqq&#8217; will collect the infos for 5 minutes, print the list of the local profiles and exit </p>
<dt><code>-C</code>, <code>&#8211;curses</code></p>
<dd>Ncurses based GUI. See <a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8) for a full description. </p>
<dt><code>-G</code>, <code>&#8211;gtk</code></p>
<dd>The nice GTK2 interface (thanks Daten&#8230;). </p>
<dt><code>-D</code>, <code>&#8211;daemonize</code></p>
<dd>Daemonize ettercap. This option will detach ettercap from the current controlling terminal and set it as a daemon. You can combine this feature with the &quot;log&quot; option to log all the traffic in the background. If the daemon fails for any reason, it will create the file &quot;./ettercap_daemonized.log&quot; in which the error caught by ettercap will be reported. Furthermore, if you want to have a complete debug of the daemon process, you are encouraged to recompile ettercap in debug mode. </p>
<dt><code>GENERAL OPTIONS</code></p>
<dd>
<dt><code>-i</code>, <code>&#8211;iface &lt;IFACE&gt;</code></p>
<dd>Use this &lt;IFACE&gt; instead of the default one. The interface can be unconfigured (requires libnet &gt;= 1.1.2), but in this case you cannot use MITM attacks and you should set the unoffensive flag. </p>
<dt><code>-I</code>, <code>&#8211;iflist</code></p>
<dd>This option will print the list of all available network interfaces that can be used within ettercap. The option is particulary usefull under windows where the name of the interface is not so obvious as under *nix. </p>
<dt><code>-n</code>, <code>&#8211;netmask &lt;NETMASK&gt;</code></p>
<dd>Use this &lt;NETMASK&gt; instead of the one associated with the current iface. This option is useful if you have the NIC with an associated netmask of class B and you want to scan (with the arp scan) only a class C. </p>
<dt><code>-R</code>, <code>&#8211;reversed</code></p>
<dd>Reverse the matching in the TARGET selection. It means not(TARGET). All but the selected TARGET. </p>
<dt><code>-t</code>, <code>&#8211;proto &lt;PROTO&gt;</code></p>
<dd>Sniff only PROTO packets (default is TCP + UDP).<br />
 This is useful if you want to select a port via the TARGET specification but you want to differentiate between tcp or udp.<br />
 PROTO can be &quot;tcp&quot;, &quot;udp&quot; or &quot;all&quot; for both. </p>
<dt><code>-z</code>, <code>&#8211;silent</code></p>
<dd>Do not perform the initial ARP scan of the LAN. </p>
<p> NOTE: you will not have the hosts list, so you can&#8217;t use the multipoison feature. you can only select two hosts for an ARP poisoning attack, specifying them through the TARGETs </p>
<dt><code>-p</code>, <code>&#8211;nopromisc</code></p>
<dd>Usually, ettercap will put the interface in promisc mode to sniff all the traffic on the wire. If you want to sniff only your connections, use this flag to NOT enable the promisc mode. </p>
<dt><code>-u</code>, <code>&#8211;unoffensive</code></p>
<dd>Every time ettercap starts, it disables ip forwarding in the kernel and begins to forward packets itself. This option prevent to do that, so the responsibility of ip forwarding is left to the kernel.<br />
 This options is useful if you want to run multiple ettercap instances. You will have one instance (the one without the -u option) forwarding the packets, and all the other instances doing their work without forwarding them. Otherwise you will get packet duplicates.<br />
 It also disables the internal creation of the sessions for each connection. It increases performances, but you will not be able to modify packets on the fly.<br />
 If you want to use a mitm attack you have to use a separate instance.<br />
 You have to use this option if the interface is unconfigured (without an ip address.)<br />
 This is also useful if you want to run ettercap on the gateway. It will not disable the forwarding and the gateway will correctly route the packets. </p>
<dt><code>-j</code>, <code>&#8211;load-hosts &lt;FILENAME&gt;</code></p>
<dd>It can be used to load a hosts list from a file created by the -k option. (see below) </p>
<dt><code>-k</code>, <code>&#8211;save-hosts &lt;FILENAME&gt;</code></p>
<dd>Saves the hosts list to a file. Useful when you have many hosts and you don&#8217;t want to do an ARP storm at startup any time you use ettercap. Simply use this options and dump the list to a file, then to load the information from it use the -j &lt;filename&gt; option. </p>
<dt><code>-P</code>, <code>&#8211;plugin &lt;PLUGIN&gt;</code></p>
<dd>Run the selected PLUGIN. Many plugins need target specification, use TARGET as always.<br />
 In console mode (-C option), standalone plugins are executed and then the application exits. Hook plugins are activated and the normal sniffing is performed.<br />
 To have a list of the available external plugins use &quot;list&quot; (without quotes) as plugin name (e.g. ./ettercap -P list). </p>
<p> NOTE: you can also activate plugins directly from the interfaces (always press &quot;h&quot; to get the inline help) </p>
<p> More detailed info about plugins and about how to write your own are found in the man page <a href="/docs/linux/man/8-ettercap_plugin/">ettercap_plugin</a>(8) </p>
<dt><code>-F</code>, <code>&#8211;filter &lt;FILE&gt;</code></p>
<dd>Load the filter from the file &lt;FILE&gt;. The filter must be compiled with <a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8). The utility will compile the filter script and produce an ettercap-compliant binary filter file. Read the <a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8) man page for the list of functions you can use inside a filter script.<br />
 NOTE: these filters are different from those set with &#8211;pcapfilter. An ettercap filter is a content filter and can modify the payload of a packet before forwarding it. Pcap filter are used to capture only certain packets.<br />
 NOTE: you can use filters on pcapfile to modify them and save to another file, but in this case you have to pay attention on what you are doing, since ettercap will not recalculate checksums, nor split packets exceeding the mtu (snaplen) nor anything like that. </p>
<dt><code>-W</code>, <code>&#8211;wep-key &lt;KEY&gt;</code></p>
<dd>You can specify a WEP key to decrypt WiFi packets. Only the packets decrypted successfully will be passed to the decoders stack, the others will be skipped with a message.<br />
 The parameter has the following syntax: N:T:KEY. Where N is the bit length of the wep key (64, 128 or 256), T is the type of the string (&#8216;s&#8217; for string and &#8216;p&#8217; for passphrase). KEY can be a string or an escaped hex sequences. </p>
<p> example:<br />
 &#8211;wep-key 128:p:secret<br />
 &#8211;wep-key 128:s:ettercapwep0<br />
 &#8211;wep-key &#8217;64:s:&#8242; </p>
<dt><code>-a</code>, <code>&#8211;config &lt;CONFIG&gt;</code></p>
<dd>Loads an alternative config file instead of the default in /etc/etter.conf. This is useful if you have many preconfigured files for different situations. </p>
<dt><code>VISUALIZATION OPTIONS</code></p>
<dd>
<dt><code>-e</code>, <code>&#8211;regex &lt;REGEX&gt;</code></p>
<dd>Handle only packets that match the regex.<br />
 This option is useful in conjunction with -L. It logs only packets that match the posix regex REGEX.<br />
 It impacts even the visualization of the sniffed packets. If it is set only packets matching the regex will be displayed. </p>
<dt><code>-V</code>, <code>&#8211;visual &lt;FORMAT&gt;</code></p>
<dd>Use this option to set the visualization method for the packets to be displayed. </p>
<p> FORMAT may be one of the following: </p>
<dl>
<dd>
<dl>
<dt><code>hex</code></p>
<dd>Print the packets in hex format. </p>
<p> example: </p>
<p> the string &quot;HTTP/1.1 304 Not Modified&quot; becomes: </p>
<p> 0000: 4854 5450 2f31 2e31 2033 3034 204e 6f74 HTTP/1.1 304 Not<br />
 0010: 204d 6f64 6966 6965 64 Modified </p>
<dt><code>ascii</code></p>
<dd>Print only &quot;printable&quot; characters, the others are displayed as dots &#8216;.&#8217; </p>
<dt><code>text</code></p>
<dd>Print only the &quot;printable&quot; characters and skip the others. </p>
<dt><code>ebcdic</code></p>
<dd>Convert an EBCDIC text to ASCII. </p>
<dt><code>html</code></p>
<dd>Strip all the html tags from the text. A tag is every string between &lt; and &gt;. </p>
<p> example: </p>
<p> &lt;title&gt;This is the title&lt;/title&gt;, but the following &lt;string&gt; will not be displayed. </p>
<p> This is the title, but the following will not be displayed. </p>
<dt><code>utf8</code></p>
<dd>Print the packets in UTF-8 format. The encoding used while performing the conversion is declared in the <a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5) file. </p>
</dl>
</dl>
<dt><code>-d</code>, <code>&#8211;dns</code></p>
<dd>Resolve ip addresses into hostnames. </p>
<p> NOTE: this may seriously slow down ettercap while logging passive information. Every time a new host is found, a query to the dns is performed. Ettercap keeps a cache for already resolved host to increase the speed, but new hosts need a new query and the dns may take up to 2 or 3 seconds to respond for an unknown host. </p>
<p> HINT: ettercap collects the dns replies it sniffs in the resolution table, so even if you specify to not resolve the hostnames, some of them will be resolved because the reply was previously sniffed. think about it as a passive dns resolution for free&#8230; ;) </p>
<dt><code>-E</code>, <code>&#8211;ext-headers</code></p>
<dd>Print extended headers for every displayed packet. (e.g. mac addresses) </p>
<dt><code>-Q</code>, <code>&#8211;superquiet</code></p>
<dd>Super quiet mode. Do not print users and passwords as they are collected. Only store them in the profiles. It can be useful to run ettercap in text only mode but you don&#8217;t want to be flooded with dissectors messages. Useful when using plugins because the sniffing process is always active, it will print all the collected infos, with this option you can suppress these messages.<br />
 NOTE: this options automatically sets the -q option. </p>
<p> example: </p>
<p> ettercap -TzQP finger /192.168.0.1/22 </p>
<dt><code>LOGGING OPTIONS</code></p>
<dd>
<dt><code>-L</code>, <code>&#8211;log &lt;LOGFILE&gt;</code></p>
<dd>Log all the packets to binary files. These files can be parsed by <a href="/docs/linux/man/8-etterlog/">etterlog</a>(8) to extract human readable data. With this option, all packets sniffed by ettercap will be logged, together with all the passive info (host info + user &amp; pass) it can collect. Given a LOGFILE, ettercap will create LOGFILE.ecp (for packets) and LOGFILE.eci (for the infos). </p>
<p> NOTE: if you specify this option on command line you don&#8217;t have to take care of privileges since the log file is opened in the startup phase (with high privs). But if you enable the log option while ettercap is already started, you have to be in a directory where uid = 65535 or uid = EC_UID can write. </p>
<p> NOTE: the logfiles can be compressed with the deflate algorithm using the -c option. </p>
<dt><code>-l</code>, <code>&#8211;log-info &lt;LOGFILE&gt;</code></p>
<dd>Very similar to -L but it logs only passive information + users and passwords for each host. The file will be named LOGFILE.eci </p>
<dt><code>-m</code>, <code>&#8211;log-msg &lt;LOGFILE&gt;</code></p>
<dd>It stores in &lt;LOGFILE&gt; all the user messages printed by ettercap. This can be useful when you are using ettercap in daemon mode or if you want to track down all the messages. Indeed, some dissectors print messages but their information is not stored anywhere, so this is the only way to keep track of them. </p>
<dt><code>-c</code>, <code>&#8211;compress</code></p>
<dd>Compress the logfile with the gzip algorithm while it is dumped. <a href="/docs/linux/man/8-etterlog/">etterlog</a>(8) is capable of handling both compressed and uncompressed log files. </p>
<dt><code>-o</code>, <code>&#8211;only-local</code></p>
<dd>Stores profiles information belonging only to the LAN hosts. </p>
<p> NOTE: this option is effective only against the profiles collected in memory. While logging to a file ALL the hosts are logged. If you want to split them, use the related <a href="/docs/linux/man/8-etterlog/">etterlog</a>(8) option. </p>
<dt><code>-O</code>, <code>&#8211;only-remote</code></p>
<dd>Stores profiles information belonging only to remote hosts. </p>
<dt><code>STANDARD OPTIONS</code></p>
<dd>
<dt><code>-U</code>, <code>&#8211;update</code></p>
<dd>Connects to the ettercap website (ettercap.sf.net) and retrieve the latest databases used by ettercap.<br />
 If you want only to check if an update is available, prepend the -z option. The order does matter: ettercap -zU </p>
<p> <code>SECURITY NOTE: </code> The updates are not signed so an attacker may poison your DNS server and force the updateNG.php to feed ettercap with fake databases. This can harm to your system since it can overwrite any file containing the string &quot;Revision: &quot;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print the version and exit. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>prints the help screen with a short summary of the available options. </p>
</dl>
<h2>Examples</h2>
<p>Here are some examples of using ettercap.</p>
<dl>
<dt><code>ettercap -Tp</code></p>
<dd>Use the console interface and do not put the interface in promisc mode. You will see only your traffic.</p>
<dt><code>ettercap -Tzq</code></p>
<dd>Use the console interface, do not ARP scan the net and be quiet. The packet content will not be displayed, but user and passwords, as well as other messages, will be displayed.</p>
<dt><code>ettercap -T -j /tmp/victims -M arp /10.0.0.1-7/ /10.0.0.10-20/</code></p>
<dd>Will load the hosts list from /tmp/victims and perform an ARP poisoning attack against the two target. The list will be joined with the target and the resulting list is used for ARP poisoning.</p>
<dt><code>ettercap -T -M arp // //</code></p>
<dd>Perform the ARP poisoning attack against all the hosts in the LAN. BE CAREFUL !!</p>
<dt><code>ettercap -T -M arp:remote /192.168.1.1/ /192.168.1.2-10/</code></p>
<dd>Perform the ARP poisoning against the gateway and the host in the lan between 2 and 10. The &#8216;remote&#8217; option is needed to be able to sniff the remote traffic the hosts make through the gateway.</p>
<dt><code>ettercap -Tzq //110</code></p>
<dd>Sniff only the pop3 protocol from every hosts.</p>
<dt><code>ettercap -Tzq /10.0.0.1/21,22,23 </code></p>
<dd>Sniff telnet, ftp and ssh connections to 10.0.0.1.</p>
<dt><code>ettercap -P list</code></p>
<dd>Prints the list of all available plugins </p>
<h2>Authors</h2>
<p>Alberto Ornaghi (ALoR) &lt;alor [at] users.sf.net&gt;<br />
 Marco Valleri (NaGA) &lt;naga [at] antifork.org&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-etter-conf/">etter.conf</a>(5)</i> <i><a href="/docs/linux/man/8-ettercap_curses/">ettercap_curses</a>(8)</i> <i><a href="/docs/linux/man/8-ettercap_plugins/">ettercap_plugins</a>(8)</i> <i><a href="/docs/linux/man/8-etterlog/">etterlog</a>(8)</i> <i><a href="/docs/linux/man/8-etterfilter/">etterfilter</a>(8)</i> </p>
<h2>Availability</h2>
<p><a rel="nofollow" href="http://ettercap.sourceforge.net/download/">http://ettercap.sourceforge.net/download/</a></p>
<h2>Cvs</h2>
<p>cvs -d:pserver:anonymous [at] cvs.ettercap.sf.net:/cvsroot/ettercap login<br />
 cvs -d:pserver:anonymous [at] cvs.ettercap.sf.net:/cvsroot/ettercap co ettercap_ng</p>
<h2>Bugs</h2>
<p>Our software never has bugs.<br />
 It just develops random features. ;) <code>KNOWN-BUGS</code> &#8211; ettercap doesn&#8217;t handle fragmented packets&#8230; only the first segment will be displayed by the sniffer. However all the fragments are correctly forwarded. + please send bug-report, patches or suggestions to &lt;alor [at] users.sourceforge.net&gt; or visit <a rel="nofollow" href="http://ettercap.sourceforge.net/forum/">http://ettercap.sourceforge.net/forum/</a> and post it in the BUGS section. + to report a bug, follow the instructions in the README.BUGS file </p>
<h2>Philological History</h2>
<p>&quot;Even if blessed with a feeble intelligence, they are cruel and smart&#8230;&quot; this is the description of Ettercap, a monster of the RPG Advanced Dungeons &amp; Dragon. </p>
<p> The name &quot;ettercap&quot; was chosen because it has an assonance with &quot;ethercap&quot; which means &quot;ethernet capture&quot; (what ettercap actually does) and also because such monsters have a powerful poison&#8230; and you know, arp poisoning&#8230; ;)</p>
<h2>The Lord Of The (Token)Ring</h2>
<p>(the fellowship of the packet) </p>
<p> &quot;One Ring to link them all, One Ring to ping them, </p>
<p>&nbsp;<wbr>one Ring to bring them all and in the darkness sniff them.&quot;</p>
<h2>Last words</h2>
<p>&quot;Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning.&quot; &#8211; Rich Cook</p>
