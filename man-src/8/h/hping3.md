---
title: "hping3(8)"
name: "hping3"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hping3/"
description: "hping3 – send (almost) arbitrary TCP/IP packets to network hosts"
---

<p>hping3 &#8211; send (almost) arbitrary TCP/IP packets to network hosts</p>
<h2>Synopsis</h2>
<p><code>hping3</code> [ <code>-hvnqVDzZ012WrfxykQbFSRPAUXYjJBuTG</code> ] [ <code>-c</code> <i>count</i> ] [ <code>-i</code> <i>wait</i> ] [ <code>&#8211;fast</code> ] [ <code>-I</code> <i>interface</i> ] [ <code>-9</code> <i>signature</i> ] [ <code>-a</code> <i>host</i> ] [ <code>-t</code> <i>ttl</i> ] [ <code>-N</code> <i>ip id</i> ] [ <code>-H</code> <i>ip protocol</i> ] [ <code>-g</code> <i>fragoff</i> ] [ <code>-m</code> <i>mtu</i> ] [ <code>-o</code> <i>tos</i> ] [ <code>-C</code> <i>icmp type</i> ] [ <code>-K</code> <i>icmp code</i> ] [ <code>-s</code> <i>source port</i> ] [ <code>-p[+][+]</code> <i>dest port</i> ] [ <code>-w</code> <i>tcp window</i> ] [ <code>-O</code> <i>tcp offset</i> ] [ <code>-M</code> <i>tcp sequence number</i> ] [ <code>-L</code> <i>tcp ack</i> ] [ <code>-d</code> <i>data size</i> ] [ <code>-E</code> <i>filename</i> ] [ <code>-e</code> <i>signature</i> ] [ <code>&#8211;icmp-ipver</code> <i>version</i> ] [ <code>&#8211;icmp-iphlen</code> <i>length</i> ] [ <code>&#8211;icmp-iplen</code> <i>length</i> ] [ <code>&#8211;icmp-ipid</code> <i>id</i> ] [ <code>&#8211;icmp-ipproto</code> <i>protocol</i> ] [ <code>&#8211;icmp-cksum</code> <i>checksum</i> ] [ <code>&#8211;icmp-ts</code> ] [ <code>&#8211;icmp-addr</code> ] [ <code>&#8211;tcpexitcode</code> ] [ <code>&#8211;tcp-timestamp</code> ] [ <code>&#8211;tr-stop</code> ] [ <code>&#8211;tr-keep-ttl</code> ] [ <code>&#8211;tr-no-rtt</code> ] [ <code>&#8211;rand-dest</code> ] [ <code>&#8211;rand-source</code> ] [ <code>&#8211;beep</code> ] hostname</p>
<h2>Description</h2>
<p>hping3 is a network tool able to send custom TCP/IP packets and to display target replies like ping program does with ICMP replies. hping3 handle fragmentation, arbitrary packets body and size and can be used in order to transfer files encapsulated under supported protocols. Using hping3 you are able to perform at least the following stuff: </p>
<p>&nbsp;<wbr>&#8211; Test firewall rules<br />
&nbsp;<wbr>&#8211; Advanced port scanning<br />
&nbsp;<wbr>&#8211; Test net performance using different protocols,<br />
packet size, TOS&nbsp;<wbr>(type of service)&nbsp;<wbr>and fragmentation.<br />
&nbsp;<wbr>&#8211; Path MTU discovery<br />
&nbsp;<wbr>&#8211; Transferring files between even really fascist firewall<br />
rules.<br />
&nbsp;<wbr>&#8211; Traceroute-like under different protocols.<br />
&nbsp;<wbr>&#8211; Firewalk-like usage.<br />
&nbsp;<wbr>&#8211; Remote OS fingerprinting.<br />
&nbsp;<wbr>&#8211; TCP/IP stack auditing.<br />
&nbsp;<wbr>&#8211; A lot of others. </p>
<p> <i>It&#8217;s also a good didactic tool to learn TCP/IP</i>. hping3 is developed and maintained by antirez [at] invece.org and is licensed under GPL version 2. Development is open so you can send me patches, suggestion and affronts without inhibitions.</p>
<h2>Hping Site</h2>
<p>primary site at <code><a rel="nofollow" href="http://www.hping.org">http://www.hping.org</a></code>. You can found both the stable release and the instruction to download the latest source code at <a rel="nofollow" href="http://www.hping.org/download.html">http://www.hping.org/download.html</a></p>
<h2>Base Options</h2>
<dl>
<dt><i>-h &#8211;help</i></dt>
<dd>Show an help screen on standard output, so you can pipe to less.</dd>
<dt><i>-v &#8211;version</i></dt>
<dd>Show version information and API used to access to data link layer, <i>linux sock packet</i> or <i>libpcap.</i></dd>
<dt><i>-c &#8211;count count</i></dt>
<dd>Stop after sending (and receiving) <i>count</i> response packets. After last packet was send hping3 wait COUNTREACHED_TIMEOUT seconds target host replies. You are able to tune COUNTREACHED_TIMEOUT editing hping3.h</dd>
<dt><i>-i &#8211;interval</i></dt>
<dd>Wait the specified number of seconds or micro seconds between sending each packet. &#8211;interval X set <i>wait</i> to X seconds, &#8211;interval uX set <i>wait</i> to X micro seconds. The default is to wait one second between each packet. Using hping3 to transfer files tune this option is really important in order to increase transfer rate. Even using hping3 to perform idle/spoofing scanning you should tune this option, see <code>HPING3-HOWTO</code> for more information.</dd>
<dt><i>&#8211;fast</i></dt>
<dd>Alias for -i u10000. Hping will send 10 packets for second.</dd>
<dt><i>&#8211;faster</i></dt>
<dd>Alias for -i u1. Faster then &#8211;fast ;) (but not as fast as your computer can send packets due to the signal-driven design).</dd>
<dt><i>&#8211;flood</i></dt>
<dd>Sent packets as fast as possible, without taking care to show incoming replies. This is ways faster than to specify the -i u0 option.</dd>
<dt><i>-n &#8211;numeric</i></dt>
<dd>Numeric output only, No attempt will be made to lookup symbolic names for host addresses.</dd>
<dt><i>-q &#8211;quiet</i></dt>
<dd>Quiet output. Nothing is displayed except the summary lines at startup time and when finished.</dd>
<dt><i>-I &#8211;interface interface name</i></dt>
<dd>By default on linux and BSD systems hping3 uses default routing interface. In other systems or when there is no default route hping3 uses the first non-loopback interface. However you are able to force hping3 to use the interface you need using this option. Note: you don&#8217;t need to specify the whole name, for example -I et will match eth0 ethernet0 myet1 et cetera. If no interfaces match hping3 will try to use lo.</dd>
<dt><i>-V &#8211;verbose</i></dt>
<dd>Enable verbose output. TCP replies will be shown as follows: </dd>
<p> len=46 ip=192.168.1.1 flags=RA DF seq=0 ttl=255 id=0 win=0 rtt=0.4 ms tos=0 iplen=40 seq=0 ack=1380893504 sum=2010 urp=0</p>
<dt><i>-D &#8211;debug</i></dt>
<dd>Enable debug mode, it&#8217;s useful when you experience some problem with hping3. When debug mode is enabled you will get more information about <code>interface detection, data link layer access, interface settings, options</code> <code>parsing, fragmentation, HCMP protocol</code> and other stuff.</dd>
<dt><i>-z &#8211;bind</i></dt>
<dd>Bind CTRL+Z to <code>time to live (TTL)</code> so you will able to increment/decrement ttl of outgoing packets pressing CTRL+Z once or twice.</dd>
<dt><i>-Z &#8211;unbind</i></dt>
<dd>Unbind CTRL+Z so you will able to stop hping3.</dd>
<dt><i>&#8211;beep</i></dt>
<dd>Beep for every matching received packet (but not for ICMP errors).</dd></dl>
<h2>Protocol Selection</h2>
<p>Default protocol is TCP, by default hping3 will send tcp headers to target host&#8217;s port 0 with a winsize of 64 without any tcp flag on. Often this is the best way to do an &#8216;hide ping&#8217;, useful when target is behind a firewall that drop ICMP. Moreover a tcp null-flag to port 0 has a good probability of not being logged.</p>
<dl>
<dt><i>-0 &#8211;rawip</i></dt>
<dd>RAW IP mode, in this mode hping3 will send IP header with data appended with &#8211;signature and/or &#8211;file, see also &#8211;ipproto that allows you to set the ip protocol field.</dd>
<dt><i>-1 &#8211;icmp</i></dt>
<dd>ICMP mode, by default hping3 will send ICMP echo-request, you can set other ICMP type/code using <code>&#8211;icmptype &#8211;icmpcode</code> options.</dd>
<dt><i>-2 &#8211;udp</i></dt>
<dd>UDP mode, by default hping3 will send udp to target host&#8217;s port 0. UDP header tunable options are the following: <code>&#8211;baseport, &#8211;destport, &#8211;keep.</code></dd>
<dt><i>-8 &#8211;scan</i></dt>
<dd>Scan mode, the option expects an argument that describes groups of ports to scan. port groups are comma separated: a number describes just a single port, so 1,2,3 means port 1, 2 and 3. ranges are specified using a start-end notation, like 1-1000, that tell hping to scan ports between 1 and 1000 (included). the special word <code>all</code> is an alias for 0-65535, while the special word <code>known</code> includes all the ports listed in /etc/services.<br />
 Groups can be combined, so the following command line will scan ports between 1 and 1000 AND port 8888 AND ports listed in /etc/services: <code>hping &#8211;scan 1-1000,8888,known -S target.host.com</code><br />
 Groups can be negated (subtracted) using a ! character as prefix, so the following command line will scan all the ports NOT listed in /etc/services in the range 1-1024: <code>hping &#8211;scan &#8216;1-1024,!known&#8217; -S target.host.com</code><br />
 Keep in mind that while hping seems much more like a port scanner in this mode, most of the hping switches are still honored, so for example to perform a SYN scan you need to specify the <code>-S</code> option, you can change the TCP windows size, TTL, control the IP fragmentation as usually, and so on. The only real difference is that the standard hping behaviors are encapsulated into a scanning algorithm.<br />
 <code>Tech note</code>: The scan mode uses a two-processes design, with shared memory for synchronization. The scanning algorithm is still not optimal, but already quite fast.<br />
 <code>Hint</code>: unlike most scanners, hping shows some interesting info about received packets, the IP ID, TCP win, TTL, and so on, don&#8217;t forget to look at this additional information when you perform a scan! Sometimes they shows interesting details.</dd>
<dt><i>-9 &#8211;listen signature</i></dt>
<dd>HPING3 listen mode, using this option hping3 waits for packet that contain <i>signature</i> and dump from <i>signature</i> end to packet&#8217;s end. For example if hping3 &#8211;listen TEST reads a packet that contain <code>234-09sdflkjs45-TESThello_world</code> it will display <code>hello_world</code>.</dd></dl>
<h2>Ip Related Options</h2>
<dl>
<dt><i>-a &#8211;spoof hostname</i></dt>
<dd>Use this option in order to set a fake IP source address, this option ensures that target will not gain your real address. However replies will be sent to spoofed address, so you will can&#8217;t see them. In order to see how it&#8217;s possible to perform spoofed/idle scanning see the <code>HPING3-HOWTO</code>.</dd>
<dt><i>&#8211;rand-source</i></dt>
<dd>This option enables the <code>random source mode</code>. hping will send packets with random source address. It is interesting to use this option to stress firewall state tables, and other per-ip basis dynamic tables inside the TCP/IP stacks and firewall software.</dd>
<dt><i>&#8211;rand-dest</i></dt>
<dd>This option enables the <code>random destination mode</code>. hping will send the packets to random addresses obtained following the rule you specify as the target host. You need to specify a numerical IP address as target host like <code>10.0.0.x</code>. All the occurrences of <code>x</code> will be replaced with a random number in the range 0-255. So to obtain Internet IP addresses in the whole IPv4 space use something like <code>hping x.x.x.x &#8211;rand-dest</code>. If you are not sure about what kind of addresses your rule is generating try to use the <code>&#8211;debug</code> switch to display every new destination address generated. When this option is turned on, matching packets will be accept from all the destinations.<br />
 <code>Warning</code>: when this option is enabled hping can&#8217;t detect the right outgoing interface for the packets, so you should use the <code>&#8211;interface</code> option to select the desired outgoing interface.</dd>
<dt><i>-t &#8211;ttl time to live</i></dt>
<dd>Using this option you can set <code>TTL (time to live)</code> of outgoing packets, it&#8217;s likely that you will use this with <code>&#8211;traceroute</code> or <code>&#8211;bind</code> options. If in doubt try `<code>hping3 some.host.com -t 1 &#8211;traceroute</code>&#8216;.</dd>
<dt><i>-N &#8211;id</i></dt>
<dd>Set ip-&gt;id field. Default id is random but if fragmentation is turned on and id isn&#8217;t specified it will be <code>getpid() &amp; 0xFF</code>, to implement a better solution is in TODO list.</dd>
<dt><i>-H &#8211;ipproto</i></dt>
<dd>Set the ip protocol in RAW IP mode.</dd>
<dt><i>-W &#8211;winid</i></dt>
<dd>id from Windows* systems before Win2k has different byte ordering, if this option is enable hping3 will properly display id replies from those Windows.</dd>
<dt><i>-r &#8211;rel</i></dt>
<dd>Display id increments instead of id. See the <code>HPING3-HOWTO</code> for more information. Increments aren&#8217;t computed as id[N]-id[N-1] but using packet loss compensation. See relid.c for more information.</dd>
<dt><i>-f &#8211;frag</i></dt>
<dd>Split packets in more fragments, this may be useful in order to test IP stacks fragmentation performance and to test if some packet filter is so weak that can be passed using tiny fragments (anachronistic). Default &#8216;virtual mtu&#8217; is 16 bytes. see also <i>&#8211;mtu</i> option.</dd>
<dt><i>-x &#8211;morefrag</i></dt>
<dd>Set more fragments IP flag, use this option if you want that target host send an <code>ICMP time-exceeded during reassembly</code>.</dd>
<dt><i>-y &#8211;dontfrag</i></dt>
<dd>Set don&#8217;t fragment IP flag, this can be used to perform <code>MTU path discovery</code>.</dd>
<dt><i>-g &#8211;fragoff fragment offset value</i></dt>
<dd>Set the fragment offset.</dd>
<dt><i>-m &#8211;mtu mtu value</i></dt>
<dd>Set different &#8216;virtual mtu&#8217; than 16 when fragmentation is enabled. If packets size is greater that &#8216;virtual mtu&#8217; fragmentation is automatically turned on.</dd>
<dt><i>-o &#8211;tos hex_tos</i></dt>
<dd>Set <code>Type Of Service (TOS)</code>, for more information try <code>&#8211;tos help</code>.</dd>
<dt><i>-G &#8211;rroute</i></dt>
<dd>Record route. Includes the RECORD_ROUTE option in each packet sent and displays the route buffer of returned packets. Note that the IP header is only large enough for nine such routes. Many hosts ignore or discard this option. Also note that using hping you are able to use record route even if target host filter ICMP. Record route is an IP option, not an ICMP option, so you can use record route option even in TCP and UDP mode.</dd></dl>
<h2>Icmp Related Options</h2>
<dl>
<dt><i>-C &#8211;icmptype type</i></dt>
<dd>Set icmp type, default is <code>ICMP echo request</code> (implies &#8211;icmp).</dd>
<dt><i>-K &#8211;icmpcode code</i></dt>
<dd>Set icmp code, default is 0 (implies &#8211;icmp).</dd>
<dt><i>&#8211;icmp-ipver</i></dt>
<dd>Set IP version of IP header contained into ICMP data, default is 4.</dd>
<dt><i>&#8211;icmp-iphlen</i></dt>
<dd>Set IP header length of IP header contained into ICMP data, default is 5 (5 words of 32 bits).</dd>
<dt><i>&#8211;icmp-iplen</i></dt>
<dd>Set IP packet length of IP header contained into ICMP data, default is the real length.</dd>
<dt><i>&#8211;icmp-ipid</i></dt>
<dd>Set IP id of IP header contained into ICMP data, default is random.</dd>
<dt><i>&#8211;icmp-ipproto</i></dt>
<dd>Set IP protocol of IP header contained into ICMP data, default is TCP.</dd>
<dt><i>&#8211;icmp-cksum</i></dt>
<dd>Set ICMP checksum, for default is the valid checksum.</dd>
<dt><i>&#8211;icmp-ts</i></dt>
<dd>Alias for &#8211;icmptype 13 (to send ICMP timestamp requests).</dd>
<dt><i>&#8211;icmp-addr</i></dt>
<dd>Alias for &#8211;icmptype 17 (to send ICMP address mask requests).</dd></dl>
<h2>Tcp/Udp Related Options</h2>
<dl>
<dt><i>-s &#8211;baseport source port</i></dt>
<dd>hping3 uses source port in order to guess replies sequence number. It starts with a base source port number, and increase this number for each packet sent. When packet is received sequence number can be computed as <i>replies.dest.port &#8211; base.source.port</i>. Default base source port is random, using this option you are able to set different number. If you need that source port not be increased for each sent packet use the <i>-k &#8211;keep</i> option.</dd>
<dt><i>-p &#8211;destport [+][+]dest port</i></dt>
<dd>Set destination port, default is 0. If &#8216;+&#8217; character precedes dest port number (i.e. +1024) destination port will be increased for each reply received. If double &#8216;+&#8217; precedes dest port number (i.e. ++1024), destination port will be increased for each packet sent. By default destination port can be modified interactively using <code>CTRL+z</code>.</dd>
<dt><i>&#8211;keep</i></dt>
<dd>keep still source port, see <i>&#8211;baseport</i> for more information.</dd>
<dt><i>-w &#8211;win</i></dt>
<dd>Set TCP window size. Default is 64.</dd>
<dt><i>-O &#8211;tcpoff</i></dt>
<dd>Set fake tcp data offset. Normal data offset is tcphdrlen / 4.</dd>
<dt><i>-M &#8211;setseq</i></dt>
<dd>Set the TCP sequence number.</dd>
<dt><i>-L &#8211;setack</i></dt>
<dd>Set the TCP ack.</dd>
<dt><i>-Q &#8211;seqnum</i></dt>
<dd>This option can be used in order to collect sequence numbers generated by target host. This can be useful when you need to analyze whether TCP sequence number is predictable. Output example: </dd>
<p> <code>#hping3 win98 &#8211;seqnum -p 139 -S -i u1 -I eth0</code> </p>
<pre>HPING uaz (eth0 192.168.4.41): S set, 40 headers + 0 data bytes
2361294848 +2361294848
2411626496 +50331648
2545844224 +134217728
2713616384 +167772160
2881388544 +167772160
3049160704 +167772160
3216932864 +167772160
3384705024 +167772160
3552477184 +167772160
3720249344 +167772160
3888021504 +167772160
4055793664 +167772160
4223565824 +167772160</pre>
<p>The first column reports the sequence number, the second difference between current and last sequence number. As you can see target host&#8217;s sequence numbers are predictable.</p>
<dt><i>-b &#8211;badcksum</i></dt>
<dd>Send packets with a bad UDP/TCP checksum.</dd>
<dt><i>&#8211;tcp-timestamp</i></dt>
<dd>Enable the TCP timestamp option, and try to guess the timestamp update frequency and the remote system uptime.</dd>
<dt><i>-F &#8211;fin</i></dt>
<dd>Set FIN tcp flag.</dd>
<dt><i>-S &#8211;syn</i></dt>
<dd>Set SYN tcp flag.</dd>
<dt><i>-R &#8211;rst</i></dt>
<dd>Set RST tcp flag.</dd>
<dt><i>-P &#8211;push</i></dt>
<dd>Set PUSH tcp flag.</dd>
<dt><i>-A &#8211;ack</i></dt>
<dd>Set ACK tcp flag.</dd>
<dt><i>-U &#8211;urg</i></dt>
<dd>Set URG tcp flag.</dd>
<dt><i>-X &#8211;xmas</i></dt>
<dd>Set Xmas tcp flag.</dd>
<dt><i>-Y &#8211;ymas</i></dt>
<dd>Set Ymas tcp flag.</dd></dl>
<h2>Common Options</h2>
<dl>
<dt><i>-d &#8211;data data size</i></dt>
<dd>Set packet body size. Warning, using &#8211;data 40 hping3 will not generate 0 byte packets but protocol_header+40 bytes. hping3 will display packet size information as first line output, like this: <code>HPING <a rel="nofollow" href="http://www.yahoo.com">www.yahoo.com</a> (ppp0 204.71.200.67): NO FLAGS are set, 40 headers + 40 data bytes</code></dd>
<dt><i>-E &#8211;file filename</i></dt>
<dd>Use <code>filename</code> contents to fill packet&#8217;s data.</dd>
<dt><i>-e &#8211;sign signature</i></dt>
<dd>Fill first <i>signature length</i> bytes of data with <i>signature</i>. If the <i>signature length</i> is bigger than data size an error message will be displayed. If you don&#8217;t specify the data size hping will use the signature size as data size. This option can be used safely with <i>&#8211;file filename</i> option, remainder data space will be filled using <i>filename</i>.</dd>
<dt><i>-j &#8211;dump</i></dt>
<dd>Dump received packets in hex.</dd>
<dt><i>-J &#8211;print</i></dt>
<dd>Dump received packets&#8217; printable characters.</dd>
<dt><i>-B &#8211;safe</i></dt>
<dd>Enable safe protocol, using this option lost packets in file transfers will be resent. For example in order to send file /etc/passwd from host A to host B you may use the following: </dd>
<pre><i>[host_a]</i>
<code># hping3 host_b --udp -p 53 -d 100 --sign signature --safe --file /etc/passwd</code>
<i>[host_b]</i>
<code># hping3 host_a --listen signature --safe --icmp</code></pre>
<dt><i>-u &#8211;end</i></dt>
<dd>If you are using <i>&#8211;file filename</i> option, tell you when EOF has been reached. Moreover prevent that other end accept more packets. Please, for more information see the <code>HPING3-HOWTO</code>.</dd>
<dt><i>-T &#8211;traceroute</i></dt>
<dd>Traceroute mode. Using this option hping3 will increase ttl for each <code>ICMP time to live 0 during transit</code> received. Try <code>hping3 host &#8211;traceroute</code>. This option implies &#8211;bind and &#8211;ttl 1. You can override the ttl of 1 using the &#8211;ttl option. Since 2.0.0 stable it prints RTT information.</dd>
<dt><i>&#8211;tr-keep-ttl</i></dt>
<dd>Keep the TTL fixed in traceroute mode, so you can monitor just one hop in the route. For example, to monitor how the 5th hop changes or how its RTT changes you can try <code>hping3 host &#8211;traceroute &#8211;ttl 5 &#8211;tr-keep-ttl</code>.</dd>
<dt><i>&#8211;tr-stop</i></dt>
<dd>If this option is specified hping will exit once the first packet that isn&#8217;t an ICMP time exceeded is received. This better emulates the traceroute behavior.</dd>
<dt><i>&#8211;tr-no-rtt</i></dt>
<dd>Don&#8217;t show RTT information in traceroute mode. The ICMP time exceeded RTT information aren&#8217;t even calculated if this option is set.</dd>
<dt><i>&#8211;tcpexitcode</i></dt>
<dd>Exit with last received packet tcp-&gt;th_flag as exit code. Useful for scripts that need, for example, to known if the port 999 of some host reply with SYN/ACK or with RST in response to SYN, i.e. the service is up or down.</dd></dl>
<h2>Tcp Output Format</h2>
<p>The standard TCP output format is the following: </p>
<p> len=46 ip=192.168.1.1 flags=RA DF seq=0 ttl=255 id=0 win=0 rtt=0.4 ms </p>
<p> <code>len</code> is the size, in bytes, of the data captured from the data link layer excluding the data link header size. This may not match the IP datagram size due to low level transport layer padding. </p>
<p> <code>ip</code> is the source ip address. </p>
<p> <code>flags</code> are the TCP flags, R for RESET, S for SYN, A for ACK, F for FIN, P for PUSH, U for URGENT, X for not standard 0x40, Y for not standard 0x80. </p>
<p> If the reply contains <code>DF</code> the IP header has the don&#8217;t fragment bit set. </p>
<p> <code>seq</code> is the sequence number of the packet, obtained using the source port for TCP/UDP packets, the sequence field for ICMP packets. </p>
<p> <code>id</code> is the IP ID field. </p>
<p> <code>win</code> is the TCP window size. </p>
<p> <code>rtt</code> is the round trip time in milliseconds. </p>
<p> If you run hping using the <code>-V</code> command line switch it will display additional information about the packet, example: </p>
<p> len=46 ip=192.168.1.1 flags=RA DF seq=0 ttl=255 id=0 win=0 rtt=0.4 ms tos=0 iplen=40 seq=0 ack=1223672061 sum=e61d urp=0 </p>
<p> <code>tos</code> is the type of service field of the IP header. </p>
<p> <code>iplen</code> is the IP total len field. </p>
<p> <code>seq and ack</code> are the sequence and acknowledge 32bit numbers in the TCP header. </p>
<p> <code>sum</code> is the TCP header checksum value. </p>
<p> <code>urp</code> is the TCP urgent pointer value.</p>
<h2>Udp Output Format</h2>
<p>The standard output format is: </p>
<p> len=46 ip=192.168.1.1 seq=0 ttl=64 id=0 rtt=6.0 ms </p>
<p> The field meaning is just the same as the TCP output meaning of the same fields.</p>
<h2>Icmp Output Format</h2>
<p>An example of ICMP output is: </p>
<p> ICMP Port Unreachable from ip=192.168.1.1 name=nano.marmoc.net </p>
<p> It is very simple to understand. It starts with the string &quot;ICMP&quot; followed by the description of the ICMP error, Port Unreachable in the example. The ip field is the IP source address of the IP datagram containing the ICMP error, the name field is just the numerical address resolved to a name (a dns PTR request) or UNKNOWN if the resolution failed. </p>
<p> The ICMP Time exceeded during transit or reassembly format is a bit different: </p>
<p> TTL 0 during transit from ip=192.168.1.1 name=nano.marmoc.net </p>
<p> TTL 0 during reassembly from ip=192.70.106.25 name=UNKNOWN </p>
<p> The only difference is the description of the error, it starts with TTL 0.</p>
<h2>Author</h2>
<p>Salvatore Sanfilippo &lt;antirez [at] invece.org&gt;, with the help of the people mentioned in AUTHORS file and at <a rel="nofollow" href="http://www.hping.org/authors.html">http://www.hping.org/authors.html</a></p>
<h2>Bugs</h2>
<p>Even using the &#8211;end and &#8211;safe options to transfer files the final packet will be padded with 0x00 bytes. </p>
<p> Data is read without care about alignment, but alignment is enforced in the data structures. This will not be a problem under i386 but, while usually the TCP/IP headers are naturally aligned, may create problems with different processors and bogus packets if there is some unaligned access around the code (hopefully none). </p>
<p> On solaris hping does not work on the loopback interface. This seems a solaris problem, as stated in the tcpdump-workers mailing list, so the libpcap can&#8217;t do nothing to handle it properly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ping/">ping</a>(8), <a href="/docs/linux/man/8-traceroute/">traceroute</a>(8), <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8), <a href="/docs/linux/man/1-nmap/">nmap</a>(1) </p>
