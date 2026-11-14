---
title: "arp-scan(1)"
name: "arp-scan"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arp-scan/"
description: "arp-scan – The ARP scanner"
---

<h2 class="name">NAME</h2>
<p> arp-scan &#8211; The ARP scanner </p>
<h2>SYNOPSIS</h2>
<p> <code>arp-scan</code> [<i>options</i>]<i> </i>[<i>hosts</i>&#8230;] </p>
<p> Target hosts must be specified on the command line unless the <code>&#8211;file</code> option is given, in which case the targets are read from the specified file instead, or the <code>&#8211;localnet</code> option is used, in which case the targets are generated from the network interface IP address and netmask. </p>
<p> You will need to be root, or <code>arp-scan</code> must be SUID root, in order to run <code>arp-scan</code>, because the functions that it uses to read and write packets require root privilege. </p>
<p> The target hosts can be specified as IP addresses or hostnames. You can also specify the target as <code>IPnetwork/bits</code> (e.g. 192.168.1.0/24) to specify all hosts in the given network (network and broadcast addresses included), <code>IPstart-IPend</code> (e.g. 192.168.1.3-192.168.1.27) to specify all hosts in the inclusive range, or <code>IPnetwork:NetMask</code> (e.g. 192.168.1.0:255.255.255.0) to specify all hosts in the given network and mask.</p>
<h2>DESCRIPTION</h2>
<p> <code>arp-scan</code> sends ARP packets to hosts on the local network and displays any responses that are received. The network interface to use can be specified with the <code>&#8211;interface</code> option. If this option is not present, <code>arp-scan</code> will search the system interface list for the lowest numbered, configured up interface (excluding loopback). By default, the ARP packets are sent to the Ethernet broadcast address, ff:ff:ff:ff:ff:ff, but that can be changed with the <code>&#8211;destaddr</code> option. </p>
<p> The target hosts to scan may be specified in one of three ways: by specifying the targets on the command line; by specifying a file containing the targets with the <code>&#8211;file</code> option; or by specifying the <code>&#8211;localnet</code> option which causes all possible hosts on the network attached to the interface (as defined by the interface address and mask) to be scanned. For hosts specified on the command line, or with the <code>&#8211;file</code> option, you can use either IP addresses or hostnames. You can also use network specifications <code>IPnetwork/bits</code>, <code>IPstart-IPend</code>, or <code>IPnetwork:NetMask</code>. </p>
<p> The list of target hosts is stored in memory. Each host in this list uses 28 bytes of memory, so scanning a Class-B network (65,536 hosts) requires about 1.75MB of memory for the list, and scanning a Class-A (16,777,216 hosts) requires about 448MB. </p>
<p> <code>arp-scan</code> supports Ethernet and 802.11 wireless networks. It could also support token ring and FDDI, but they have not been tested. It does not support serial links such as PPP or SLIP, because ARP is not supported on them. </p>
<p> The ARP protocol is a layer-2 (datalink layer) protocol that is used to determine a host&#8217;s layer-2 address given its layer-3 (network layer) address. ARP was designed to work with any layer-2 and layer-3 address format, but the most common use is to map IP addresses to Ethernet hardware addresses, and this is what <code>arp-scan</code> supports. ARP only operates on the local network, and cannot be routed. Although the ARP protocol makes use of IP addresses, it is not an IP-based protocol and <code>arp-scan</code> can be used on an interface that is not configured for IP. </p>
<p> ARP is only used by IPv4 hosts. IPv6 uses NDP (neighbour discovery protocol) instead, which is a different protocol and is not supported by <code>arp-scan</code>. </p>
<p> One ARP packet is sent for each for each target host, with the target protocol address (the ar$tpa field) set to the IP address of this host. If a host does not respond, then the ARP packet will be re-sent once more. The maximum number of retries can be changed with the <code>&#8211;retry</code> option. Reducing the number of retries will reduce the scanning time at the possible risk of missing some results due to packet loss. </p>
<p> You can specify the bandwidth that <code>arp-scan</code> will use for the outgoing ARP packets with the <code>&#8211;bandwidth</code> option. By default, it uses a bandwidth of 256000 bits per second. Increasing the bandwidth will reduce the scanning time, but setting the bandwidth too high may result in an ARP storm which can disrupt network operation. Also, setting the bandwidth too high can send packets faster than the network interface can transmit them, which will eventually fill the kernel&#8217;s transmit buffer resulting in the error message: <i>No buffer space available</i>. Another way to specify the outgoing ARP packet rate is with the <code>&#8211;interval</code> option, which is an alternative way to modify the same underlying parameter. </p>
<p> The time taken to perform a single-pass scan (i.e. with <code>&#8211;retry=1</code>) is given by: </p>
<pre>
time = n*i + t + o
</pre>
<p> Where <i>n</i> is the number of hosts in the list, <i>i</i> is the time interval between packets (specified with <code>&#8211;interval</code>, or calculated from <code>&#8211;bandwidth</code>), <i>t</i> is the timeout value (specified with <code>&#8211;timeout</code>) and <i>o</i> is the overhead time taken to load the targets into the list and read the MAC/Vendor mapping files. For small lists of hosts, the timeout value will dominate, but for large lists the packet interval is the most important value. </p>
<p> With 65,536 hosts, the default bandwidth of 256,000 bits/second (which results in a packet interval of 2ms), the default timeout of 500ms, and a single pass ( <code>&#8211;retry=1</code>), and assuming an overhead of 1 second, the scan would take 65536*0.002 + 0.5 + 1 = 132.57 seconds, or about 2 minutes 13 seconds. </p>
<p> Any part of the outgoing ARP packet may be modified through the use of the various <code>&#8211;arpXXX</code> options. The use of some of these options may make the outgoing ARP packet non RFC compliant. Different operating systems handle the various non standard ARP packets in different ways, and this may be used to fingerprint these systems. See <code><a href="/docs/linux/man/1-arp-fingerprint/">arp-fingerprint</a></code>(1) for information about a script which uses these options to fingerprint the target operating system. </p>
<p> The table below summarises the options that change the outgoing ARP packet. In this table, the <i>Field</i> column gives the ARP packet field name from RFC 826, <i>Bits</i> specifies the number of bits in the field, <i>Option</i> shows the <code>arp-scan</code> option to modify this field, and <i>Notes </i> gives the default value and any other notes. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4><code>Outgoing ARP Packet Options</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Field</code></td>
<td><code>Bits</code></td>
<td><code>Option</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ar$hrd</td>
<td>16</td>
<td>&#8211;arphrd</td>
<td>Default is 1 (ARPHRD_ETHER)
</td>
</tr>
<tr VALIGN=top>
<td>ar$pro</td>
<td>16</td>
<td>&#8211;arppro</td>
<td>Default is 0x0800
</td>
</tr>
<tr VALIGN=top>
<td>ar$hln</td>
<td>8</td>
<td>&#8211;arphln</td>
<td>Default is 6 (ETH_ALEN)
</td>
</tr>
<tr VALIGN=top>
<td>ar$pln</td>
<td>8</td>
<td>&#8211;arppln</td>
<td>Default is 4 (IPv4)
</td>
</tr>
<tr VALIGN=top>
<td>ar$op</td>
<td>16</td>
<td>&#8211;arpop</td>
<td>Default is 1 (ARPOP_REQUEST)
</td>
</tr>
<tr VALIGN=top>
<td>ar$sha</td>
<td>48</td>
<td>&#8211;arpsha</td>
<td>Default is interface h/w address
</td>
</tr>
<tr VALIGN=top>
<td>ar$spa</td>
<td>32</td>
<td>&#8211;arpspa</td>
<td>Default is interface IP address
</td>
</tr>
<tr VALIGN=top>
<td>ar$tha</td>
<td>48</td>
<td>&#8211;arptha</td>
<td>Default is zero (00:00:00:00:00:00)
</td>
</tr>
<tr VALIGN=top>
<td>ar$tpa</td>
<td>32</td>
<td>None</td>
<td>Set to the target host IP address
</td>
</tr>
</table>
</table>
<p> The most commonly used outgoing ARP packet option is <code>&#8211;arpspa</code>, which sets the source IP address in the ARP packet. This option allows the outgoing ARP packet to use a different source IP address from the outgoing interface address. With this option it is possible to use <code>arp-scan</code> on an interface with no IP address configured, which can be useful if you want to ensure that the testing host does not interact with the network being tested. </p>
<p> <code>Warning: Setting ar$spa to the destination IP address can disrupt some</code> <code>operating systems, as they assume there is an IP address clash if they</code> <code>receive an ARP request for their own address.</code> </p>
<p> It is also possible to change the values in the Ethernet frame header that precedes the ARP packet in the outgoing packets. The table below summarises the options that change values in the Ethernet frame header. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4><code>Outgoing Ethernet Frame Options</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Field</code></td>
<td><code>Bits</code></td>
<td><code>Option</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Dest Address</td>
<td>48</td>
<td>&#8211;destaddr</td>
<td>Default is ff:ff:ff:ff:ff:ff
</td>
</tr>
<tr VALIGN=top>
<td>Source Address</td>
<td>48</td>
<td>&#8211;srcaddr</td>
<td>Default is interface address
</td>
</tr>
<tr VALIGN=top>
<td>Protocol Type</td>
<td>16</td>
<td>&#8211;prototype</td>
<td>Default is 0x0806
</td>
</tr>
</table>
</table>
<p> The most commonly used outgoing Ethernet frame option is <code>&#8211;destaddr</code>, which sets the destination Ethernet address for the ARP packet. <code>&#8211;prototype</code> is not often used, because it will cause the packet to be interpreted as a different Ethernet protocol. </p>
<p> Any ARP responses that are received are displayed in the following format: </p>
<table>
<tr VALIGN=top>
<td>&lt;IP Address&gt;</td>
<td>&lt;Hardware Address&gt;</td>
<td>&lt;Vendor Details&gt;
</td>
</tr>
</table>
<p> Where <code>IP Address</code> is the IP address of the responding target, <code>Hardware Address</code> is its Ethernet hardware address (also known as the MAC address) and <code>Vendor Details</code> are the vendor details, decoded from the hardware address. The output fields are separated by a single tab character. </p>
<p> The responses are displayed in the order they are received, which is not always the same order as the requests were sent because some hosts may respond faster than others. </p>
<p> The vendor decoding uses the files <i>ieee-oui.txt</i>, <i>ieee-iab.txt </i> and <i>mac-vendor.txt</i>, which are supplied with <code>arp-scan</code>. The <i>ieee-oui.txt</i> and <i>ieee-iab.txt</i> files are generated from the OUI and IAB data on the IEEE website at <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/ieee-oui.txt">http://standards.ieee.org/regauth/oui/ieee-oui.txt</a></i> and <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/iab.txt">http://standards.ieee.org/regauth/oui/iab.txt</a></i>. The Perl scripts <code>get-oui</code> and <code>get-iab</code>, which are included in the <code>arp-scan</code> package, can be used to update these files with the latest data from the IEEE website. The <i>mac-vendor.txt</i> file contains other MAC to Vendor mappings that are not covered by the IEEE OUI and IAB files, and can be used to add custom mappings. </p>
<p> Almost all hosts that support IP will respond to <code>arp-scan</code> if they receive an ARP packet with the target protocol address (ar$tpa) set to their IP address. This includes firewalls and other hosts with IP filtering that drop all IP traffic from the testing system. For this reason, <code>arp-scan</code> is a useful tool to quickly determine all the active IP hosts on a given Ethernet network segment.</p>
<h2>OPTIONS</h2>
<p> Where an option takes a value, that value is specified as a letter in angle brackets. The letter indicates the type of data that is expected:</p>
<dl>
<dt><code>&lt;s&gt;</code></p>
<dd> A character string, e.g. &#8211;file=hostlist.txt.</p>
<dt><code>&lt;i&gt;</code></p>
<dd> An integer, which can be specified as a decimal number or as a hexadecimal number if preceeded with 0x, e.g. &#8211;arppro=2048 or &#8211;arpro=0x0800.</p>
<dt><code>&lt;f&gt;</code></p>
<dd> A floating point decimal number, e.g. &#8211;backoff=1.5.</p>
<dt><code>&lt;m&gt;</code></p>
<dd> An Ethernet MAC address, which can be specified either in the format 01:23:45:67:89:ab, or as 01-23-45-67-89-ab. The alphabetic hex characters may be either upper or lower case. E.g. &#8211;arpsha=01:23:45:67:89:ab.</p>
<dt><code>&lt;a&gt;</code></p>
<dd> An IPv4 address, e.g. &#8211;arpspa=10.0.0.1</p>
<dt><code>&lt;h&gt;</code></p>
<dd> Binary data specified as a hexadecimal string, which should not include a leading 0x. The alphabetic hex characters may be either upper or lower case. E.g. &#8211;padding=aaaaaaaaaaaa</p>
<dt><code>&lt;x&gt;</code></p>
<dd> Something else. See the description of the option for details.</p>
<dt><code>&#8211;help or -h</code></p>
<dd> Display this usage message and exit.</p>
<dt><code>&#8211;file=&lt;s&gt; or -f &lt;s&gt;</code></p>
<dd> Read hostnames or addresses from the specified file instead of from the command line. One name or IP address per line. Use &quot;-&quot; for standard input.</p>
<dt><code>&#8211;localnet or -l</code></p>
<dd> Generate addresses from network interface configuration. Use the network interface IP address and network mask to generate the list of target host addresses. The list will include the network and broadcast addresses, so an interface address of 10.0.0.1 with netmask 255.255.255.0 would generate 256 target hosts from 10.0.0.0 to 10.0.0.255 inclusive. If you use this option, you cannot specify the &#8211;file option or specify any target hosts on the command line. The interface specifications are taken from the interface that arp-scan will use, which can be changed with the &#8211;interface option.</p>
<dt><code>&#8211;retry=&lt;i&gt; or -r &lt;i&gt;</code></p>
<dd> Set total number of attempts per host to &lt;i&gt;, default=2.</p>
<dt><code>&#8211;timeout=&lt;i&gt; or -t &lt;i&gt;</code></p>
<dd> Set initial per host timeout to &lt;i&gt; ms, default=500. This timeout is for the first packet sent to each host. subsequent timeouts are multiplied by the backoff factor which is set with &#8211;backoff.</p>
<dt><code>&#8211;interval=&lt;x&gt; or -i &lt;x&gt;</code></p>
<dd> Set minimum packet interval to &lt;x&gt;. This controls the outgoing bandwidth usage by limiting the rate at which packets can be sent. The packet interval will be no smaller than this number. If you want to use up to a given bandwidth, then it is easier to use the &#8211;bandwidth option instead. The interval specified is in milliseconds by default, or in microseconds if &quot;u&quot; is appended to the value.</p>
<dt><code>&#8211;bandwidth=&lt;x&gt; or -B &lt;x&gt;</code></p>
<dd> Set desired outbound bandwidth to &lt;x&gt;, default=256000. The value is in bits per second by default. If you append &quot;K&quot; to the value, then the units are kilobits per sec; and if you append &quot;M&quot; to the value, the units are megabits per second. The &quot;K&quot; and &quot;M&quot; suffixes represent the decimal, not binary, multiples. So 64K is 64000, not 65536. You cannot specify both &#8211;interval and &#8211;bandwidth because they are just different ways to change the same underlying parameter.</p>
<dt><code>&#8211;backoff=&lt;f&gt; or -b &lt;f&gt;</code></p>
<dd> Set timeout backoff factor to &lt;f&gt;, default=1.50. The per-host timeout is multiplied by this factor after each timeout. So, if the number of retries is 3, the initial per-host timeout is 500ms and the backoff factor is 1.5, then the first timeout will be 500ms, the second 750ms and the third 1125ms.</p>
<dt><code>&#8211;verbose or -v</code></p>
<dd> Display verbose progress messages. Use more than once for greater effect:</p>
<dt>
<dd> 1 &#8211; Display the network address and mask used when the &#8211;localnet option is specified, display any nonzero packet padding, display packets received from unknown hosts, and show when each pass through the list completes.</p>
<dt>
<dd> 2 &#8211; Show each packet sent and received, when entries are removed from the list, the pcap filter string, and counts of MAC/Vendor mapping entries.</p>
<dt>
<dd> 3 &#8211; Display the host list before scanning starts.</p>
<dt><code>&#8211;version or -V</code></p>
<dd> Display program version and exit.</p>
<dt><code>&#8211;random or -R</code></p>
<dd> Randomise the host list. This option randomises the order of the hosts in the host list, so the ARP packets are sent to the hosts in a random order. It uses the Knuth shuffle algorithm.</p>
<dt><code>&#8211;randomseed=&lt;i&gt;</code></p>
<dd> Use &lt;i&gt; to seed the pseudo random number generator. This option seeds the PRNG with the specified number, which can be useful if you want to ensure that the random host list is reproducable. By default, the PRNG is seeded with an unpredictable value. This option is only effective in conjunction with the &#8211;random (-R) option.</p>
<dt><code>&#8211;numeric or -N</code></p>
<dd> IP addresses only, no hostnames. With this option, all hosts must be specified as IP addresses. Hostnames are not permitted. No DNS lookups will be performed.</p>
<dt><code>&#8211;snap=&lt;i&gt; or -n &lt;i&gt;</code></p>
<dd> Set the pcap snap length to &lt;i&gt;. Default=64. This specifies the frame capture length. This length includes the data-link header. The default is normally sufficient.</p>
<dt><code>&#8211;interface=&lt;s&gt; or -I &lt;s&gt;</code></p>
<dd> Use network interface &lt;s&gt;. If this option is not specified, arp-scan will search the system interface list for the lowest numbered, configured up interface (excluding loopback). The interface specified must support ARP.</p>
<dt><code>&#8211;quiet or -q</code></p>
<dd> Only display minimal output. No protocol decoding. If this option is specified, then only the IP address and MAC address are displayed for each responding host. No protocol decoding is performed and the OUI mapping files are not used.</p>
<dt><code>&#8211;plain or -x</code></p>
<dd> Display plain output showing only responding hosts. This option supresses the printing of the header and footer text, and only displays one line for each responding host. Useful if the output will be parsed by a script.</p>
<dt><code>&#8211;ignoredups or -g</code></p>
<dd> Don&#8217;t display duplicate packets. By default, duplicate packets are displayed and are flagged with &quot;(DUP: n)&quot;.</p>
<dt><code>&#8211;ouifile=&lt;s&gt; or -O &lt;s&gt;</code></p>
<dd> Use IEEE Ethernet OUI to vendor mapping file &lt;s&gt;. If this option is not specified, the default filename is ieee-oui.txt in the current directory. If that is not found, then the file /usr/local/share/arp-scan/ieee-oui.txt is used.</p>
<dt><code>&#8211;iabfile=&lt;s&gt; or -O &lt;s&gt;</code></p>
<dd> Use IEEE Ethernet IAB to vendor mapping file &lt;s&gt;. If this option is not specified, the default filename is ieee-iab.txt in the current directory. If that is not found, then the file /usr/local/share/arp-scan/ieee-iab.txt is used.</p>
<dt><code>&#8211;macfile=&lt;s&gt; or -O &lt;s&gt;</code></p>
<dd> Use custom Ethernet MAC to vendor mapping file &lt;s&gt;. If this option is not specified, the default filename is mac-vendor.txt in the current directory. If that is not found, then the file /usr/local/share/arp-scan/mac-vendor.txt is used.</p>
<dt><code>&#8211;srcaddr=&lt;m&gt; or -S &lt;m&gt;</code></p>
<dd> Set the source Ethernet MAC address to &lt;m&gt;. This sets the 48-bit hardware address in the Ethernet frame header for outgoing ARP packets. It does not change the hardware address in the ARP packet, see &#8211;arpsha for details on how to change that address. The default is the Ethernet address of the outgoing interface.</p>
<dt><code>&#8211;destaddr=&lt;m&gt; or -T &lt;m&gt;</code></p>
<dd> Send the packets to Ethernet MAC address &lt;m&gt; This sets the 48-bit destination address in the Ethernet frame header. The default is the broadcast address ff:ff:ff:ff:ff:ff. Most operating systems will also respond if the ARP request is sent to their MAC address, or to a multicast address that they are listening on.</p>
<dt><code>&#8211;arpsha=&lt;m&gt; or -u &lt;m&gt;</code></p>
<dd> Use &lt;m&gt; as the ARP source Ethernet address This sets the 48-bit ar$sha field in the ARP packet It does not change the hardware address in the frame header, see &#8211;srcaddr for details on how to change that address. The default is the Ethernet address of the outgoing interface.</p>
<dt><code>&#8211;arptha=&lt;m&gt; or -w &lt;m&gt;</code></p>
<dd> Use &lt;m&gt; as the ARP target Ethernet address This sets the 48-bit ar$tha field in the ARP packet The default is zero, because this field is not used for ARP request packets.</p>
<dt><code>&#8211;prototype=&lt;i&gt; or -y &lt;i&gt;</code></p>
<dd> Set the Ethernet protocol type to &lt;i&gt;, default=0x0806. This sets the 16-bit protocol type field in the Ethernet frame header. Setting this to a non-default value will result in the packet being ignored by the target, or sent to the wrong protocol stack.</p>
<dt><code>&#8211;arphrd=&lt;i&gt; or -H &lt;i&gt;</code></p>
<dd> Use &lt;i&gt; for the ARP hardware type, default=1. This sets the 16-bit ar$hrd field in the ARP packet. The normal value is 1 (ARPHRD_ETHER). Most, but not all, operating systems will also respond to 6 (ARPHRD_IEEE802). A few systems respond to any value.</p>
<dt><code>&#8211;arppro=&lt;i&gt; or -p &lt;i&gt;</code></p>
<dd> Use &lt;i&gt; for the ARP protocol type, default=0x0800. This sets the 16-bit ar$pro field in the ARP packet. Most operating systems only respond to 0x0800 (IPv4) but some will respond to other values as well.</p>
<dt><code>&#8211;arphln=&lt;i&gt; or -a &lt;i&gt;</code></p>
<dd> Set the hardware address length to &lt;i&gt;, default=6. This sets the 8-bit ar$hln field in the ARP packet. It sets the claimed length of the hardware address in the ARP packet. Setting it to any value other than the default will make the packet non RFC compliant. Some operating systems may still respond to it though. Note that the actual lengths of the ar$sha and ar$tha fields in the ARP packet are not changed by this option; it only changes the ar$hln field.</p>
<dt><code>&#8211;arppln=&lt;i&gt; or -P &lt;i&gt;</code></p>
<dd> Set the protocol address length to &lt;i&gt;, default=4. This sets the 8-bit ar$pln field in the ARP packet. It sets the claimed length of the protocol address in the ARP packet. Setting it to any value other than the default will make the packet non RFC compliant. Some operating systems may still respond to it though. Note that the actual lengths of the ar$spa and ar$tpa fields in the ARP packet are not changed by this option; it only changes the ar$pln field.</p>
<dt><code>&#8211;arpop=&lt;i&gt; or -o &lt;i&gt;</code></p>
<dd> Use &lt;i&gt; for the ARP operation, default=1. This sets the 16-bit ar$op field in the ARP packet. Most operating systems will only respond to the value 1 (ARPOP_REQUEST). However, some systems will respond to other values as well.</p>
<dt><code>&#8211;arpspa=&lt;a&gt; or -s &lt;a&gt;</code></p>
<dd> Use &lt;a&gt; as the source IP address. The address should be specified in dotted quad format; or the literal string &quot;dest&quot;, which sets the source address to be the same as the target host address. This sets the 32-bit ar$spa field in the ARP packet. Some operating systems check this, and will only respond if the source address is within the network of the receiving interface. Others don&#8217;t care, and will respond to any source address. By default, the outgoing interface address is used.</p>
<dt>
<dd> WARNING: Setting ar$spa to the destination IP address can disrupt some operating systems, as they assume there is an IP address clash if they receive an ARP request for their own address.</p>
<dt><code>&#8211;padding=&lt;h&gt; or -A &lt;h&gt;</code></p>
<dd> Specify padding after packet data. Set the padding data to hex value &lt;h&gt;. This data is appended to the end of the ARP packet, after the data. Most, if not all, operating systems will ignore any padding. The default is no padding, although the Ethernet driver on the sending system may pad the packet to the minimum Ethernet frame length.</p>
<dt><code>&#8211;llc or -L</code></p>
<dd> Use RFC 1042 LLC framing with SNAP. This option causes the outgoing ARP packets to use IEEE 802.2 framing with a SNAP header as described in RFC 1042. The default is to use Ethernet-II framing. arp-scan will decode and display received ARP packets in either Ethernet-II or IEEE 802.2 formats irrespective of this option.</p>
<dt><code>&#8211;vlan=&lt;i&gt; or -Q &lt;i&gt;</code></p>
<dd> Use 802.1Q tagging with VLAN id &lt;i&gt;. This option causes the outgoing ARP packets to use 802.1Q VLAN tagging with a VLAN ID of &lt;i&gt;, which should be in the range 0 to 4095 inclusive. arp-scan will always decode and display received ARP packets in 802.1Q format irrespective of this option.</p>
<dt><code>&#8211;pcapsavefile=&lt;s&gt; or -W &lt;s&gt;</code></p>
<dd> Write received packets to pcap savefile &lt;s&gt;. This option causes received ARP responses to be written to the specified pcap savefile as well as being decoded and displayed. This savefile can be analysed with programs that understand the pcap file format, such as &quot;tcpdump&quot; and &quot;wireshark&quot;.</p>
<dt><code>&#8211;rtt or -D</code></p>
<dd> Display the packet round-trip time.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/local/share/arp-scan/ieee-oui.txt</i></p>
<dd> List of IEEE OUI (Organisationally Unique Identifier) to vendor mappings.</p>
<dt><i>/usr/local/share/arp-scan/ieee-iab.txt</i></p>
<dd> List of IEEE IAB (Individual Address Block) to vendor mappings.</p>
<dt><i>/usr/local/share/arp-scan/mac-vendor.txt</i></p>
<dd> List of other Ethernet MAC to vendor mappings.</dl>
<h2>EXAMPLES</h2>
<p> The example below shows <code>arp-scan</code> being used to scan the network <i>192.168.0.0/24</i> using the network interface <i>eth0</i>. </p>
<pre>
$ arp-scan --interface=eth0 192.168.0.0/24
Interface: eth0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.4 with 256 hosts (<a rel="nofollow" href="http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/)">http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/)</a>
192.168.0.1     00:c0:9f:09:b8:db       QUANTA COMPUTER, INC.
192.168.0.3     00:02:b3:bb:66:98       Intel Corporation
192.168.0.5     00:02:a5:90:c3:e6       Compaq Computer Corporation
192.168.0.6     00:c0:9f:0b:91:d1       QUANTA COMPUTER, INC.
192.168.0.12    00:02:b3:46:0d:4c       Intel Corporation
192.168.0.13    00:02:a5:de:c2:17       Compaq Computer Corporation
192.168.0.87    00:0b:db:b2:fa:60       Dell ESG PCBA Test
192.168.0.90    00:02:b3:06:d7:9b       Intel Corporation
192.168.0.105   00:13:72:09:ad:76       Dell Inc.
192.168.0.153   00:10:db:26:4d:52       Juniper Networks, Inc.
192.168.0.191   00:01:e6:57:8b:68       Hewlett-Packard Company
192.168.0.251   00:04:27:6a:5d:a1       Cisco Systems, Inc.
192.168.0.196   00:30:c1:5e:58:7d       HEWLETT-PACKARD
13 packets received by filter, 0 packets dropped by kernel
Ending arp-scan: 256 hosts scanned in 3.386 seconds (75.61 hosts/sec).  13 responded
</pre>
<p> This next example shows <code>arp-scan</code> being used to scan the local network after configuring the network interface with DHCP using <i>pump</i>. </p>
<pre>
# pump
# ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 00:D0:B7:0B:DD:C7
          inet addr:10.0.84.178  Bcast:10.0.84.183  Mask:255.255.255.248
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:46335 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1542776 errors:0 dropped:0 overruns:0 carrier:0
          collisions:1644 txqueuelen:1000
          RX bytes:6184146 (5.8 MiB)  TX bytes:348887835 (332.7 MiB)
# arp-scan --localnet
Interface: eth0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.4 with 8 hosts (<a rel="nofollow" href="http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/)">http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/)</a>
10.0.84.179     00:02:b3:63:c7:57       Intel Corporation
10.0.84.177     00:d0:41:08:be:e8       AMIGO TECHNOLOGY CO., LTD.
10.0.84.180     00:02:b3:bd:82:9b       Intel Corporation
10.0.84.181     00:02:b3:1f:73:da       Intel Corporation
4 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.4: 8 hosts scanned in 0.820 seconds (9.76 hosts/sec).  4 responded
</pre>
<h2>AUTHOR</h2>
<p> Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-get-oui/">get-oui</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-get-iab/">get-iab</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-arp-fingerprint/">arp-fingerprint</a></code>(1) </p>
<p> <code>RFC 826</code> &#8211; An Ethernet Address Resolution Protocol </p>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The arp-scan wiki page. </p>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/">http://www.nta-monitor.com/tools-resources/security-tools/arp-scan/</a></i> The arp-scan homepage. </p>
<h2>Index</h2>
