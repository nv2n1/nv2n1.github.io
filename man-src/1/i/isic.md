---
title: "isic(1)"
name: "isic"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isic/"
description: "ISIC – IP Stack Integrity Checker"
---

<h2>NAME</h2>
<p> ISIC &#8211; IP Stack Integrity Checker</p>
<h2>SYNOPSIS</h2>
<p> <code>esic -i</code> <i>&lt;interface&gt;</i> <code>[&#8230;]</code><br />
 <code>isic -s </code> <i>&lt;source ip&gt; </i> <code>-d </code> <i>&lt;destination ip&gt; </i> <code>[&#8230;]</code><br />
 <code>tcpsic -s </code> <i>&lt;source ip&gt;[,port]</i> <code>-d </code> <i>&lt;destination ip&gt;[,port]</i> <code>[&#8230;]</code><br />
 <code>udpsic -s </code> <i>&lt;source ip&gt;[,port]</i> <code>-d </code> <i>&lt;destination ip&gt;[,port]</i> <code>[&#8230;]</code><br />
 <code>icmpsic -s </code> <i>&lt;source ip&gt;</i> <code>-d </code> <i>&lt;destination ip&gt;</i> <code>[&#8230;]</code><br />
 <code>multisic -s</code> <i>&lt;source ip&gt;[,port]</i> <code>-d</code> <i>&lt;destination ip&gt;[,port]</i> <code>-i</code> <i>&lt;interface&gt;</i> <code>[&#8230;]</code><br />
 <code>isic6 -s </code> <i>&lt;source ip&gt;</i> <code>-d </code> <i>&lt;destination ip&gt;</i> <code>[&#8230;]</code><br />
 <code>tcpsic6 -s </code> <i>&lt;source ip&gt;[,port]</i> <code>-d </code> <i>&lt;destination ip&gt;[,port]</i> <code>[&#8230;]</code><br />
 <code>udpsic6 -s </code> <i>&lt;source ip&gt;[,port]</i> <code>-d </code> <i>&lt;destination ip&gt;[,port]</i> <code>[&#8230;]</code><br />
 <code>imcpsic6 -s </code> <i>&lt;source ip&gt;</i> <code>-d </code> <i>&lt;destination ip&gt;</i> <code>[&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ISIC</code> is a suite of utilities to exercise the stability of an IP Stack and its component stacks (TCP, UDP, ICMP et. al.) It generates piles of pseudo random packets of the target protocol. The packets are given tendancies to conform to. For example 50% of the packets generated can have IP Options, and 25% of the packets can be IP fragments&#8230; But the percentages are arbitrary and most of the packet fields have a configurable tendancy. </p>
<p> The packets are then sent against the target machine to either penetrate its firewall rules or find bugs in the IP stack. ISIC also contains an utility (esic) that generates raw Ethernet frames to examine hardware implementations, and the &quot;multisic&quot; tool to check multicast code integrity. </p>
<p> Starting from version <i>0.07</i>, ISIC includes utilities (*sic6) to test IPv6 protocol stack. These would of course need IPv6 enabled in the system as a prerequisite.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt>-c &lt;# of packets&gt;</p>
<dd> For esic only, number of packets to send. It is equivlent to -p option used by other utilities. The default is <i>2^32</i>.</p>
<dt>-d &lt;destination MAC/IP&gt;</p>
<dd> Optional for esic, required for all others. For esic, this specifies destination MAC address, and the default will be broadcast address <i>ff:ff:ff:ff:ff:ff</i>. For all others, this specifies destination IP address. Use &quot;-d rand&quot; to send packets to random destination MAC/IP address. For multisic, &quot;-d rand&quot; will make destination IP address picked from the list [224, 225, 232, 233, 234, 235, 236, 237, 238, 239] randomly.</p>
<dt>-i &lt;interface&gt;</p>
<dd> Required by esic and multisic. This specifies the interface for outgoing packets.</p>
<dt>-k &lt;num&gt;</p>
<dd> This specifies the number of skipped packets. This option is useful for identifying the exact packet(s) causing the problem. Default is <i>0</i>.</p>
<dt>-l &lt;length&gt;</p>
<dd> For esic only, the maximum length of packet generated. Default is maximum ethernet frame size <i>1500</i>. Length greater than default value will be rejected.</p>
<dt>-m &lt;num&gt;</p>
<dd> For esic, this is the number of packets between printout, default to <i>1000</i>. For all others, this specifies the maximum speed of traffic generation, unit is kB/s</p>
<dt>-p &lt;num&gt;</p>
<dd> For esic, this specifies upper layer protocol number in the ethernet header, and default to type IP <i>0x0800</i>. For all others this is the number of packets to send, default is <i>2^32</i>. Note esic uses -c instead for this purpose.</p>
<dt>-r &lt;random seed&gt;</p>
<dd> Specify the random seed, default to current process id.</p>
<dt>-s &lt;source MAC/IP&gt;</p>
<dd> Optional for esic, required for all others. For esic, this specifies source MAC address, and the default will be the MAC address of given interface. For all others, this specifies source IP address. Use &quot;-s rand&quot; to set source MAC/IP address to random value.</p>
<dt>-x &lt;num&gt;</p>
<dd> Available to all but esic. Send each packet &lt;num&gt; times, the default value is <i>1</i>.</p>
<dt>-v</p>
<dd> Print out the current version of ISIC test suite.</p>
<dt>-z &lt;source MAC&gt;</p>
<dd> Optional for multisic. This specifies source MAC address for outgoing multicast packets, and the default will be the MAC address of given interface. Use &quot;-z rand&quot; to set source MAC address to random value.</p>
<dt>-D</p>
<dd> Available to all but esic, this turns on the debugging printout. Caution: the program will print out information of every generated packet, the entire output will be huge. </p>
</dl>
<h2>PERCENTAGE OPTIONS</h2>
<p> These options are defined to all but esic. All percentage options have default value of <i>10</i>.</p>
<dl>
<dt>-i</p>
<dd> Available for icmpsic and icmpsic6 only, the percentage of ICMP packets with bad ICMP checksum.</p>
<dt>-t</p>
<dd> Available for tcpsic and tcpsic6 only, the percentage of TCP packets with bad TCP checksum.</p>
<dt>-u</p>
<dd> Available for tcpsic and tcpsic6 only, the percentage of TCP packets with urgent flag set.</p>
<dt>-F</p>
<dd> The percentage of fragmented packets. Note for *sic6, this is the percentage of IPv6 packets with random fragment extension header.</p>
<dt>-I</p>
<dd>
&nbsp;<wbr>For&nbsp;<wbr>*sic6, this is the percentage of IPv6 packets with random destination option header. For isic, this specifies the percentage of packets with random IP header length. For tcpsic, udpsic and icmpsic, this is the percentage of packets with random IP option.</p>
<dt>-T</p>
<dd> Available for tcpsic and tcpsic6 only, the percentage of TCP options in the TCP header.</p>
<dt>-U</p>
<dd> Available for udpsic and udpsic6 only, the percentage of UDP packets with bad UDP checksum.</p>
<dt>-V</p>
<dd> Avialable for isic, tcpsic, udpsic, icmpsic and isic6, this is the percentage of packets with bad IP version value in the header. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>esic -i eth0 -s 01:02:34:56:07:89 -p rand -m 5000</p>
<dd>
<dt>
<dd>
<dl>
<dt>
<dd> This will generate ethernet frames with random protocol number in the ethernet header, and send out through eth0 interface. In the frames, the source MAC address is fixed 01:02:34:56:07:89, destination will be the default broadcast MAC address. There will be a printout line for every 5000 frames.</dl>
<dt>isic -s rand -d 10.11.12.13 -F 50 -p 100 -k 20 -r 10</p>
<dd>
<dt>
<dd>
<dl>
<dt>
<dd> This asks isic to generate 100 IP packets with randsom source address and fixed destination address 10.11.12.13. The random seed is set to 10. half of packets will be fragments. When sending out, first 20 packets will be skipped, isic will start from the 21st packet.</dl>
<dt>tcpsic -s 1.2.3.4,69 -d 21.22.23.24 -x 2 -m 1000 -T 30 -t 50</p>
<dd>
<dt>
<dd>
<dl>
<dt>
<dd> This advises tcpsic to generate TCP packets with source address 1.2.3,4 and source TCP port 69, and destination address 21.22.23.24 and random destination TCP port. Each packet will be sent out twice, and the overall maximum speed is 1000kB/s. Of all the TCP packets generated, 30% of packets will have random TCP options, and 50% will have bad TCP checksum.</dl>
<dt>multisic -s rand -d 224.0.0.5 -i eth2 -p 50000 -F 50 -z ff:ff:ff:ff:ff:ff</p>
<dd>
<dt>
<dd>
<dl>
<dt>
<dd> This lets multisic to send 50000 UDP packets to multicast address 224.0.0.5 with random source address and source/destination UDP ports. The egress interface is forced to be eth2. 50% of outgoing packets will have fragments. And the source MAC address is set to ff:ff:ff:ff:ff:ff.</dl>
<dt>udpsic6 -s rand -d 2001:1:2:3:4::2,161 -p 1000000 -I 90 -U 20</p>
<dd>
<dt>
<dd>
<dl>
<dt>
<dd> This lets udpsic6 to send 1 million IPv6 UDP packets with random source address and source UDP port, to destination address 2001:1:2:3:4::2 and UDP port 161 (SNMP port). 90% of outgoing packets will have random IPv6 destination option header, and 20% of total packets will include incorrect UDP checksum.</dl>
</dl>
<h2>AUTHOR</h2>
<p> Shu Xiao &lt;sxiao [at] cisco.com&gt;</p>
<h2>SEE ALSO</h2>
<p> Libnet (<a rel="nofollow" href="http://www.packetfactory.net/projects/libnet)">http://www.packetfactory.net/projects/libnet)</a><br />
 ISIC online (<a rel="nofollow" href="http://www.packetfactory.net/projects/ISIC)">http://www.packetfactory.net/projects/ISIC)</a> or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(<a rel="nofollow" href="http://isic.sourceforge.net)">http://isic.sourceforge.net)</a><br />
 ip6sic (<a rel="nofollow" href="http://ip6sic.sourceforge.net)">http://ip6sic.sourceforge.net)</a> </p>
<h2>Index</h2>
