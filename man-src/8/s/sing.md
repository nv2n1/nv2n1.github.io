---
title: "sing(8)"
name: "sing"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sing/"
description: "sing – Send ICMP Nasty Garbage packets to network hosts"
---

<p><code>sing </code> &#8211; <code>S</code>end <code>I</code>CMP <code>N</code>asty <code>G</code>arbage packets to network hosts</p>
<h2>Synopsis</h2>
<p><code>sing</code> [<code>-hVRnvqGQOBU</code>] [<code>-c</code> <i>count</i>] [<code>-T</code> <i>wait</i>] [<code>-p</code> <i>pattern</i>] [<code>-s</code> <i>datasize</i>] [<code>-F</code> <i>bytes</i>] [<code>-i</code> <i>interface</i>] [<code>-S</code> <i>spoof</i>] [<code>-t</code> <i>ttl</i>] [<code>-TOS</code> <i>tos</i>] [<code>-l</code> <i>preload</i>] [<code>-M</code> <i>os</i>] [<code>-L</code> <i>logfile</i>] [<code>-MAC</code> <i>hw_addr</i>] [<code>-x</code> <i>code</i>] [<i>type</i>] <i>host</i></p>
<h2>Description</h2>
<p><code>sing</code> is a tool that sends ICMP packets fully customized from command line. The main purpose is to replace the niceful <code>ping</code> command with certain enhancenments as the ability to send/read IP spoofed packets, send MAC spoofed packets, send in addition to the ECHO REQUEST type sent by default, many other ICMP types as <code>Echo Reply</code>, <code>Address Mask Request</code>, <code>Timestamp</code>, <code>Information Request</code>,<code>Router Solicitation</code> and <code>Router Advertisement</code>. </p>
<p> It supports also the following ICMP error types: <code>Redirect</code>, <code>Source Quench</code>, <code>Time Exceeded</code>, <code>Destination Unreachable</code> and <code>Parameter Problem</code>. </p>
<p> It can do a little fingerprinting, see the <code>FINGERPRINTING TECHNIQUES</code> section to read more details about. </p>
<p> It can emulate certain OOSS sending <code>Echo Request</code> or <code>Echo Reply</code> packets. See the <code>MIMIC TECHNIQUES</code> section for a more accurate information. </p>
<p> The host destination can also be specified as a list of gateways (including destination) breaked by the &#8216;<code>%</code>&#8216; symbol meaning the use of a <code>Strict Source Routing IP Option</code> (v.g. router1<code>%</code>router2<code>%</code>router3<code>%</code>host) or the &#8216;<code>@</code>&#8216; symbol meaning the use of a <code>Loose Source Routing IP Option</code> (v.g. router1<code>@</code>router2<code>@</code>router3<code>@</code>host). </p>
<p> A long number of examples is given at the <code>EXAMPLES</code> section of this page that shows a real use of this program.</p>
<h2>Most Common Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Help screen.</p>
<dt><code>-V</code>, <code>&#8211;Version</code></p>
<dd>Program version.</p>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>-B</code></p>
<dd>Send a <code>B</code>ad ICMP Checksum on Information types.</p>
<dt><code>-c</code> <i>count</i></p>
<dd>Stop after sending (and receiving) <i>count</i> packets. Information types only.</p>
<dt><code>-F</code> <i>bytes</i></p>
<dd>Fragment the entire ICMP packet with <i>bytes</i> size by fragment. Not used on Solaris systems.</p>
<dt><code>-G</code></p>
<dd>Set the IP header Don&#8217;t Fragment flag. Not used on Solaris systems.</p>
<dt><code>-i</code> <i>interface</i></p>
<dd>Interface (name or IP address) where listen on for replies.</p>
<dt><code>-l</code> <i>preload</i></p>
<dd>If <i>preload</i> is specified, <code>sing</code> sends that many packets as fast as possible before falling into its normal mode of behavior. Only the super-user may use this option. Information types only.</p>
<dt><code>-L</code> <i>logfile</i></p>
<dd>Save the current session to the file <i>logfile</i>. If <i>logfile</i> exists the data will be appended at end.</p>
<dt><code>-M</code> <i>os</i></p>
<dd>Do mimic of the <i>os</i> specified when sending an <i>Echo Request</i> or <i>Echo Reply</i>. <i>os</i> can be <i>win</i>, <i>unix</i>, <i>linux</i>, <i>cisco</i>, <i>solaris</i> or <i>shiva</i>.</p>
<dt><code>-MAC</code> <i>hw_address</i></p>
<dd>Do MAC spoofing using the MAC <i>hw_address</i> (maybe to surpass filtered switches). Be aware of using on an interface with a datalink type different of Ethernet. The MAC address must be on hexadecimal form and must be delimited by &#8216;<code>:</code>&#8216; (Example: 00:FF:AC:33:1:B). This option made use of the libnet library to acces the network link layer. Only the super-user can use this option.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t use name resolution.</p>
<dt><code>-O</code></p>
<dd>Do fingerprinting to discover the target OS.</p>
<dt><code>-p</code> <i>pattern</i></p>
<dd>You may specify a <i>pattern</i> of bytes to fill out the packet you send. This is useful for diagnosing data-dependent problems in a network. For example, `-p INPACK&#8221; will cause the sent packet to be filled with the word INPACK.</p>
<dt><code>-q</code></p>
<dd>Quiet output. Nothing is displayed except the summary lines at startup time and when finished.</p>
<dt><code>-Q</code></p>
<dd>Totally quiet output. Absolutly nothing is displayed. Useful to use within shell scripts.</p>
<dt><code>-R</code></p>
<dd>Use Record Route IP Header Option on the ICMP packet.</p>
<dt><code>-s</code> <i>bytes</i>|<i>max</i></p>
<dd>Number of garbage bytes that will be sent on any ICMP packet. With <i>max</i> the maximum possible will be sent.</p>
<dt><code>-S</code> <i>address</i></p>
<dd>IP address to be used as the source of the ICMP packet. This force the use of the libpcap routines that puts your network interface into promiscuous mode to be able to read the replies. Only the super-user may use this option.</p>
<dt><code>-t</code> <i>ttl</i></p>
<dd>Set the IP Time To Live field to <i>ttl</i> value.</p>
<dt><code>-T</code> <i>wait</i></p>
<dd>Wait <i>wait</i> seconds <i>between sending each packet</i>. The default is to wait for one second between each packet.</p>
<dt><code>-TOS</code> <i>tos</i></p>
<dd>Set the IP Type Of Service field to <i>tos</i> value.</p>
<dt><code>-U</code></p>
<dd>Set the IP header Unused bit flag. Be aware on *BSD systems because the kernel set to 0 the IP header flags when using the Reserved Bit so <i>SING</i> must revert to promiscuous mode to be able to read the response with libpcap. Not used on Solaris systems.</p>
<dt><code>-x</code>, <code>&#8211;xcode</code> <i>code</i>|<i>num</i>|<i>max</i></p>
<dd>ICMP code to send. Code <i>code</i> valid for Destination Unreachable (<code>-du</code>), Redirect (<code>-red</code>) and Time Exceeded (<code>-tx</code>) types. Numerical code can be specified for the ICMP types that doesn&#8217;t have (Echo Request, Information Request, Address Mask Request, Router Solicitation, Router Advertisement, Source Quench, Parameter Problem and Timestamp). Using <i>max</i> an ICMP code greater than the admited ones will be sent. See the <code>ICMP CODES</code> section for a long list of <i>code</i> types.</dl>
<h2>Icmp Types</h2>
<p>The <code>type</code> can be any of the following below:</p>
<dl>
<dt><code>-echo</code>, <code>&#8211;echo_request</code></p>
<dd>Echo Request. Request sent to a host to receive an echo reply. This is the type sent by default. This ICMP type is <code>information</code>.</p>
<dt><code>-tstamp</code>, <code>&#8211;timestamp</code></p>
<dd>Timestamp. Host request to receive the time of another host. This ICMP type is <code>information</code>.</p>
<dt><code>-mask</code>, <code>&#8211;mask_req</code></p>
<dd>Address Mask Request. Used to find out a host network mask. This ICMP type is <code>information</code>.</p>
<dt><code>-info</code>, <code>&#8211;info_req</code></p>
<dd>Information Request. Host request to receive an Info Reply from another host. This ICMP type is <code>information</code>.</p>
<dt><code>-du</code>, <code>&#8211;dest_unreach</code></p>
<dd>Destination Unreach. IP packet couldn&#8217;t be given. This ICMP type is <code>error</code>.</p>
<dt><code>-sq</code>, <code>&#8211;src_quench</code></p>
<dd>Source Quench. IP packet is not given due a net congestion. This ICMP type is <code>error</code>.</p>
<dt><code>-red</code>, <code>&#8211;redirect</code></p>
<dd>Redirect. Request to forward IP packets through another router. This ICMP type is <code>error</code>.</p>
<dt><code>-rta</code>, <code>&#8211;router_advert</code> <code>address</code>[<code>/preference</code>]</p>
<dd>Router Advertisement. Router trasmits one or more routers with address <code>address</code> and preference <code>preference</code>. If this is ommited, default preference 0 is given. This ICMP type is <code>information</code>.</p>
<dt><code>-rts</code>, <code>&#8211;router_solicit</code></p>
<dd>Router Solicitation. Host requeriment for a message of one or more routers. Like the previous, is a part of the messages exchange Router Discovery and this ICMP type is <code>information</code>.</p>
<dt><code>-tx</code>, <code>&#8211;time_exc</code></p>
<dd>Time Exceeded. Time Exceeded for an IP packet. This ICMP type is <code>error</code>.</p>
<dt><code>-param</code>, <code>&#8211;param_problem</code></p>
<dd>Parameter Problem. Erroneous value on a variable of IP header. This ICMP type is <code>error</code>.</p>
<dt><code>-reply</code></p>
<dd>Echo Reply. Response to a Echo Request. This ICMP type is <code>information</code>.</dl>
<h2>Less Common Options</h2>
<p>The <code>options</code> can be any of the following:</p>
<dl>
<dt><code>-lt</code>, <code>&#8211;lifetime</code> <i>secs</i></p>
<dd>Lifetime in seconds of the router announcement. Only valid with Router Advertisement (<code>-rta</code>) type. 1800 seconds by default (30&#8242;).</p>
<dt><code>-gw</code>, <code>&#8211;gateway</code> <i>address</i></p>
<dd>Route gateway address on an ICMP Redirect (<code>-red</code>). By default will be the spoof address (<code>-S</code>), if it has been specified, or the outgoing IP address if it has not been specified.</p>
<dt><code>-dest</code>, <code>&#8211;route_dest</code> <i>address</i></p>
<dd>Route destination address on an ICMP Redirect (<code>-red</code>). This is a required option when sending an ICMP Redirect.</p>
<dt><code>-orig</code>, <code>&#8211;orig_host</code> <i>address</i></p>
<dd>Original host within the IP header sent in the 64 bits data field of an ICMP <code>error</code>. By default will be the same as the IP of the host that sends the ICMP packet.</p>
<dt><code>-psrc</code>, <code>&#8211;port_src</code> <i>port</i></p>
<dd>Source port (tcp or udp) within the IP header sent in the 64 bits data field of an ICMP <code>error</code>. 0 by default.</p>
<dt><code>-pdst</code>, <code>&#8211;port_dst</code> <i>port</i></p>
<dd>Destination port (tcp or udp) within the IP header sent in the 64 bits data field of an ICMP <code>error</code>. 0 by default.</p>
<dt><code>-prot</code>, <code>&#8211;protocol</code> <i>name</i>|<i>number</i></p>
<dd>Protocol to be used within the IP header sent in the 64 bits data field of an ICMP <code>error</code>. Must be a name from the <code>/etc/protocols</code> or a protocol number. Only <code>tcp</code>,<code> udp</code> and <code>icmp</code> are fully implemented, with other protocols the remaining of the 64 bits field are fulfilled with 0xFF. TCP by default.</p>
<dt><code>-id</code> <i>identificator</i></p>
<dd>ICMP id to be used with ICMP of Information types. Do not be confused with the <code>-ip_id</code> option!.</p>
<dt><code>-seq</code> <i>sequence</i></p>
<dd>Echo sequence number to be used with <code>Echo Request</code> or <code>Echo Reply</code> types. Do not be confused with the <code>-ip_seq</code> option!.</p>
<dt><code>-ip_id</code> <i>identificator</i></p>
<dd>Echo identificator within the IP header sent in the 64 bits data field of an ICMP <code>error</code> when the IP header protocol of the 64 bits data field (<code>-prot</code>) is icmp. 0 by default.</p>
<dt><code>-ip_seq</code> <i>sequence</i></p>
<dd>Echo sequence number within the IP header sent in the 64 bits data field of an ICMP <code>error</code> when the IP header protocol of the 64 bits data field (<code>-prot</code>) is icmp. 0 by default.</p>
<dt><code>-ptr</code>, <code>&#8211;pointer</code> <i>byte</i></p>
<dd>Pointer to erroneus byte <code>byte</code> on an ICMP packet showing a parameter problem. Valid only on Parameter Problem type (<code>-param</code>).</dl>
<h2>Icmp Codes</h2>
<p>Valid <code>codes</code> used with Destination Unreach, Redirect and Time Exceeded types are,</p>
<dl>
<dt>&#8211; Used with <code>Destination Unreach</code> type (<code>-du</code>):</p>
<dd></dl>
<p> <code>net-unreach</code> (Net Unreachable) The destination net is unreachable. </p>
<p> <code>host-unreach</code> (Host Unreachable) The destination host is unreachable. </p>
<p> <code>prot-unreach</code> (Protocol Unreachable) desired protocol is unreachable to destination host. </p>
<p> <code>port-unreach</code> (Port Unreachable) desired port is unreachable to destination host. </p>
<p> <code>frag-needed</code> (Fragmentation Needed and Don&#8217;t Fragment was Set) Shows that IP packet had to be fragmented because of its size but the sender did not allowed it because the DF (DON&#8217;T FRAGMENT) flag was set. </p>
<p> <code>sroute-fail</code> (Source Route Failed) could&#8217;nt follow the route indicated on IP packet. </p>
<p> <code>net-unknown</code> (Destination Network Unknown) Destination network is unknown. </p>
<p> <code>host-unknown</code> (Destination Host Unknown) Destination host unknown but network is. </p>
<p> <code>host-isolated</code> (Source Host Isolated) Can&#8217;t reach destination host. </p>
<p> <code>net-ano</code> (Communication with Destination Network is Administratively Prohibited) access network is denied through firewall or similar on receiver side. </p>
<p> <code>host-ano</code> (Communication with Destination Host is Administratively Prohibited) access host is denied through firewall or similar on receiver side. </p>
<p> <code>net-unr-tos</code> (Destination Network Unreachable for Type of Service) indicates on destination network that the Type Of Service (TOS) applied for is not allowed. </p>
<p> <code>host-unr-tos</code> (Destination Host Unreachable for Type of Service) shows that destination host is unreachable with applied TOS. </p>
<p> <code>com-admin-prohib</code> (Communication Administratively Prohibited) a router can&#8217;t forward a packet because of administrative filter. </p>
<p> <code>host-precedence-viol</code> (Host Precedence Violation) IP packet precedence is not allowed. </p>
<p> <code>precedence-cutoff</code> (Precedence cutoff in effect) a smaller IP packet precedence has tried to be sent over the minimal impossed by network manager. </p>
<dl>
<dt>&#8211; To be used with <code>Redirect</code> type (<code>-red</code>):</p>
<dd></dl>
<p> <code>net</code> (Redirect Datagram for the Network) shows that destination is a network. </p>
<p> <code>host</code> (Redirect Datagram for the Host) shows that destination is a host. </p>
<p> <code>serv-net</code> (Redirect Datagram for the Type Of Service and Network) destination is a type of service and network. </p>
<p> <code>serv-host</code> (Redirect Datagram for the Type Of Service and Host) destination is a type of service and host. </p>
<p> and</p>
<dl>
<dt>&#8211; to be used with <code>Time Exceeded</code> type (<code>-tx</code>):</p>
<dd></dl>
<p> <code>ttl</code> (Time to Live exceeded in Transit) time is over on an IP packet header packet. </p>
<p> <code>frag</code> (Fragment Reassembly Time Exceeded) could not reassembly all the IP packet fragments.</p>
<h2>Fingerprinting Techniques</h2>
<p>With the <code>-O</code> option <code>SING</code> can use little techniques of remote OS fingerprinting. To distinguish between Window$ boxes and the rest of the world <code>Ofir Arkin</code> has discovered a simple method: Sending an ICMP code that is not 0 within an ICMP Echo Request, a Window$ box respond with a 0 code while the rest of the boxes would leave the code field unchanged. See the <code>SEE ALSO</code> section. </p>
<p> With Solaris systems <code>SING</code> use a method discovered by me: Sending a fragmented Addres Mask Request any Solaris system (tested from 2.5.1 to Solaris8 Intel &amp; SPARC) respond with an Address Mask of 0&#8217;s. Last update!: Some people have noticed that HP-UX v11.0 respond the same way. </p>
<p> See the <code>EXAMPLES</code> section for examples.</p>
<h2>Mimic Techniques</h2>
<p>With the <code>-M</code> option <code>SING</code> can try to emulate certain OS. At the moment Window$98/Window$NT4 (<code>win</code> value), UNIX (<code>unix</code> value), Linux (<code>linux</code> value), Cisco (<code>cisco</code> value), Solaris (<code>solaris</code> value) or Shiva (<code>shiva</code> value) are the only accepted values. To emulate them <code>SING</code> changes its normal behaviour about the IP header flags, the TTL, the initial ICMP sequence number, the ICMP id and the ICMP data that each OS send. These techniques are aplied only when using <code>Echo Request</code> or <code>Echo Reply</code> types.</p>
<h2>Return Values</h2>
<p><code>sing</code> can be easily used within shell scripts. Program returns the following values to the shell:</p>
<h2>Examples</h2>
<p>&#8211; Testing if <a rel="nofollow" href="http://www.solarisbox.xx">www.solarisbox.xx</a> is running the Solaris OS. Supposed no filter methods: <code>sing -mask -O <a rel="nofollow" href="http://www.solarisbox.xx">www.solarisbox.xx</a></code> &#8211; Testing if <a rel="nofollow" href="http://www.winbox.xx">www.winbox.xx</a> is running the Window$ OS: <code>sing -O <a rel="nofollow" href="http://www.winbox.xx">www.winbox.xx</a></code> &#8211; Send Echos with garbage size of 32 bytes and fragments of 8 bytes to host <a rel="nofollow" href="http://www.provatina.xx">www.provatina.xx</a>: <code>sing -s</code> 32 <code>-F</code> 8 <code><a rel="nofollow" href="http://www.provatina.xx">www.provatina.xx</a></code> &#8211; Send Echos with data pattern IsSiNg and fragments of 8 bytes to the host <a rel="nofollow" href="http://www.provatina.xx">www.provatina.xx</a> using Loose Source Routing via router1.xx and router2.xx: <code>sing -p</code> IsSiNg <code>-F</code> 8 <code>router1.xx [at] router2.xx@<a rel="nofollow" href="http://www.provatina.xx">www.provatina.xx</a></code> &#8211; Send an ICMP packet Timestamp to host sepultura.hell. We spoof as host 10.2.3.1: <code>sing -tstamp -S</code> 10.2.3.1 <code>sepultura.hell</code> &#8211; Send an ICMP packet Router Solicitation to 10.13.1.0: <code>sing -rts </code> <code>10.13.1.0</code> &#8211; Send an ICMP Router Advertisement to host death.es, saying that the routers to use are: router1.xtc with preference 20, router2.xtc with preference 50 and router3.xtc with default preference (0). We spoof as fatherouter.xtc: <code>sing -rta</code> router1.xtc/20 <code>-rta</code> router2.xtc/50 <code>-rta</code> router3.xtc <code>-S</code> fatherouter.xtc <code>death.es</code> &#8211; In response to a packet send with TCP source port 100 and destination on port 90, we want to send and ICMP Redirect to dwdwah.xx to modify its routing table with the following data: 10.12.12.12 as a gateway to the host death.es masking the packet source as if it was sent from infect.comx host:<br />
&nbsp;<wbr>&nbsp;<wbr> <code>sing -red -S</code> infect.comx <code>-gw</code> 10.12.12.12 <code>-dest</code> death.es <code>-x</code> host <code>-prot</code> tcp <code>-psrc</code> 100 <code>-pdst</code> 90 <code>dwdwah.xx</code> &#8211; In response to an ICMP packet Echo Request sent with Echo Request id 100 and Echo Request sequence number 90, we want to send an ICMP Redirect to the host araya.xx to modify its routing table with the following data: the host pizza.death as a gateway to the host death.es, masking the packet source as if it was sent from infect.comx host. <code>sing -red -S</code> infect.comx <code>-gw</code> pizza.death <code>-dest</code> death.es <code>-x</code> host <code>-prot</code> icmp <code>-ip_id</code> 100 <code>-ip_seq</code> 90 <code>araya.xx</code> &#8211; We want to send an ICMP packet Destination Unreach to the host 10.2.3.4 saying that our TCP port number 20 connected with its TCP port 2100, is unreachable. We mask ourselves as host 10.1.1.1: <code>sing -du -S</code> 10.1.1.1 <code>-x</code> port-unreach <code>-prot</code> tcp <code>-psrc</code> 2100 <code>-pdst</code> 20 <code>10.2.3.4</code> &#8211; We want to send an ICMP packet Destination Unreach to host 10.2.3.4 saying that the host inferno.hell and its TCP port 69, connected with his port TCP 666 in unreachable. We mask ourselves as gateway router.comx: <code>sing -du -S</code> router.comx <code>-x</code> host-unreach <code>-prot</code> tcp <code>-psrc</code> 666 <code>-pdst</code> 69 <code>-orig</code> inferno.hell <code>10.2.3.4</code> &#8211; We want to send a packet ICMP Source Quench to host ldg02.hell in response to a packet destinated to host ldg00 with UDP protocol, source port 100 and destination port 200. We mask ourselves as gateway 10.10.10.1: <code>sing -sq -S</code> 10.10.10.1 <code>-prot</code> udp <code>-psrc</code> 100 <code>-pdst</code> 200 <code>-orig</code> ldg00 <code>ldg02.hell</code> &#8211; We want to send an ICMP packet Time Exceeded to host ldg02.hell in response to a packet destinated to host ldg00 with UDP protocol, source port 100 and destination port 200. We mask as gateway ldg04.hell: <code>sing -tx -S</code> ldg04.hell <code>-x</code> frag <code>-prot</code> udp <code>-psrc</code> 100 <code>-pdst</code> 200 <code>-orig</code> ldg00 <code>ldg02.hell</code> &#8211; We want to send an ICMP packet Address Mask Request and wait 10 seconds between sending each packet. We mask the packet with source address of 10.2.3.4 and we send it to the address 10.0.1.255: <code>sing -mask -S</code> 10.2.3.4 <code>-T</code> 10 <code>10.0.1.255</code> &#8211; We want to send an ICMP packet Information Request to host deep.hell: <code>sing -info </code> <code>deep.hell</code> &#8211; We want to send an ICMP packet Echo Request to host black.hell with the data pattern &#8216;MyNameIsGump&#8217;: <code>sing -p</code> MyNameIsGump <code>black.hell</code> &#8211; We want to send ICMP packet Echo Request to 10.12.0.255 with the following data pattern: D E A T H (blanks included). We will mask the source address as 192.168.0.255: <code>sing -S</code> 192.168.0.255 <code>-p</code> &#8216;D E A T H&#8217; <code>10.12.0.255</code> &#8211; We want to send an ICMP packet Destination Unreach to host destination.death but sending it with an ICMP code bigger to the legal ones adding also 60K of garbage data: <code>sing -du -x</code> max <code>-s</code> 60000 <code>destination.death</code> &#8211; We send an ICMP Parameter Problem to host misery.es saying that the packet sent from the host dump.xorg with udp protocol, source port 13 and destination port 53, has an error on the IP header byte 13. We will also add all garbage bytes as possible: <code>sing -S</code> dump.xorg <code>-param -ptr</code> 13 <code>-prot</code> udp <code>-psrc</code> 13 <code>-pdest</code> 53 <code>-s</code> max <code>misery.es</code> &#8211; We want to send an ICMP packet Timestamp to host <a rel="nofollow" href="http://www.danz.hell">www.danz.hell</a> with code 38 instead of code (0) as usual: <code>sing -tstamp -x</code> 38 <code><a rel="nofollow" href="http://www.danz.hell">www.danz.hell</a></code> &#8211; Same as above without code 38 and using Loose Source Routing between the routers cisco, 10.13.1.1 and wakeup.man: <code>sing -tstamp cisco [at] 10.13.1.1@wakeup.man [at] www.danz.hell</code> &#8211; Same as above using Strict Source Routing between the gateways: <code>sing -tstamp cisco%10.13.1.1%wakeup.man%<a rel="nofollow" href="http://www.danz.hell">www.danz.hell</a></code> &#8211; Using Record Route IP Option to see the route that takes to <a href="ftp://ftp.target.xx">ftp.target.xx</a>: <code>sing -R <a href="ftp://ftp.target.xx">ftp.target.xx</a></code> </p>
<h2>See Also</h2>
<p>Postel, John, &quot;Internet Control Message Protocol &#8211; DARPA Internet Program Protocol Specification&quot;, <code>RFC 792</code>, USC/Information Sciences Institute, September 1981. Mogul, Jeffrey and John Postel, &quot;Internet Standard Subnetting Procedure&quot;, <code>RFC 950</code>, Stanford, USC/Information Sciences Institute, August 1985. Braden, Robert, &quot;Requeriments for Internet Hosts &#8211; Communication Layers&quot;, <code>RFC 1122</code>, USC/Information Sciences Institute, October 1989. Deering, Stephen, &quot;ICMP Router Discovery Messages&quot;, <code>RFC 1256</code>, Xerox PARC, September 1991. Baker, Fred, &quot;Requeriments for IP Version 4 Routers&quot;, <code>RFC 1812</code>, Cisco Systems, June 1995. Arkin, Ofir, &quot;ICMP usage in scanning&quot;, <code><a rel="nofollow" href="http://www.sys-security.com/archive/papers/ICMP_Scanning.pdf">http://www.sys-security.com/archive/papers/ICMP_Scanning.pdf</a></code>, Sys-Security Group, July 2000. The <code>Linux source code</code>, everything referent to network code and to ICMP protocol. </p>
<h2>Author</h2>
<p>The original <code>ping</code> command was written by Mike Muuss. </p>
<p> <code>sing</code> is original from Alfredo Andres Omella, Slay &lt;aandres [at] s21sec.com&gt;</p>
