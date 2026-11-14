---
title: "mausezahn(1)"
name: "mausezahn"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mausezahn/"
description: "mausezahn – a fast versatile packet generator"
---

<h2 class="name">NAME</h2>
<p> mausezahn &#8211; a fast versatile packet generator </p>
<h2>SYNOPSIS</h2>
<p> <code>mausezahn</code> [<i>options</i>]<i>&lt;arg_string&gt; | &lt;hex_string&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>Mausezahn</code> is a free fast traffic generator written in C which allows you to send nearly every possible and impossible packet.<br />
 Mausezahn can also be used for example as didactical tool in network labs or for security audits including penetration and DoS testing. As traffic generator Mausezahn is for example used test IP multicast or VoIP networks. Speeds close to the Ethernet limit are reachable (depending on the HW platform). </p>
<h2>USAGE</h2>
<p> Mausezahn supports two modes, <code>raw-layer-2</code> mode, where every single byte to be sent can be specified, and <code>higher-layer</code> mode, where packet builder interfaces are used (using the <i>-t</i> option).<br />
 To use the <code>raw-layer-2</code> mode, simply specify the desired frame as hexadecimal sequence (the <i>hex_string</i>), such as </p>
<p> mausezahn eth0 &quot;00:ab:cd:ef:00 00:00:00:00:00:01 08:00 ca:fe:ba:be&quot; </p>
<p> The spaces within the byte string are optional and separate the Ethernet fields (destination and source address, type field, and a short payload). The only additional options supported are <i>-a</i>, <i>-b</i>, <i>-c</i>, and <i>-p</i>. The frame length MUST be greater or equal 15 bytes.<br />
 The <code>higher-layer</code> mode is enabled using the <i>-t &lt;packet_type&gt;</i> option. This option activates a packet builder and besides the <i>packet_type</i> an optional <i>arg_string</i> can be specified. The <i>arg_string</i> contains packet-specific parameters, such as TCP flags, port numbers, etc. </p>
<p> Note that Mausezahn requires root privileges. Please see the Mausezahn User&#8217;s Guide for more details or use Mausezahn&#8217;s command line help.</p>
<h2>OPTIONS</h2>
<p> Mausezahn has a built-in context specific help. Simply append the keyword <code>help</code> to the configuration options.<br />
 The most important options are:</p>
<dl>
<dt><code>-v</code></p>
<dd> Verbose mode.</p>
<dt><code>-q</code></p>
<dd> Quiet mode (only warnings and errors are displayed).</p>
<dt><code>-c &lt;count&gt;</code></p>
<dd> Send the packet count times (default: 1, infinite: 0).</p>
<dt><code>-d &lt;delay&gt;</code></p>
<dd> Apply delay between transmissions. The delay value can be specified in usec (default, no additional unit needed), or in msec (e. g. 100m or 100msec), or in seconds (e. g. 100s or 100sec).</p>
<dt><code>-p &lt;lenght&gt;</code></p>
<dd> Pad the raw frame to specified length (using zero bytes). Note that for raw layer 2 frames the specified length defines the whole frame length, while for higher layer packets the number of additional padding bytes are specified.</p>
<dt><code>-a &lt;Src_MAC|keyword&gt;</code></p>
<dd> Use specified source mac address (use hex notation such as 00:00:aa:bb:cc:dd). By default the interface MAC address will be used. The keywords <i>rand</i> and <i>own</i> refer to a random MAC address (only unicast addresses are created) and the own address, respectively. You can also use the keywords mentioned below (although broadcast-type source addresses are officially invalid).</p>
<dt><code>-b &lt;Dst_MAC|keyword&gt;</code></p>
<dd> Use specified destination mac address. By default a broadcast is sent in raw layer 2 mode or the destination hosts/gateways interface MAC address in normal (IP) mode. You can use the same keywords as mentioned above as well as <i>bc</i> (or <i>bcast</i>), <i>cisco</i>, and <i>stp</i>. Please note that for the destination MAC address the <i>rand</i> keyword is supported but creates a random address only once, even when you send multiple packets.</p>
<dt><code>-A &lt;Src_IP|range|rand&gt;</code></p>
<dd> Use specified source IP address (default is own interface IP). Optionally the keyword <i>rand</i> can again be used for a random source IP address or a range can be specified, such as 192.168.1.1-192.168.1.100 or 10.1.0.0/16. Also a DNS name can be specified for which Mausezahn tries to determine the corresponding IP address automatically.</p>
<dt><code>-B &lt;Dst_IP|range&gt;</code></p>
<dd> Use specified destination IP address (default is broadcast i. e. 255.255.255.255). As with the source address (see above) you can also specify a range or a DNS name.</p>
<dt><code>-t &lt;packet_type&gt;</code></p>
<dd> Create the specified packet type using the built-in packet builder. Currently supported packet types are: <i>arp</i>, <i>bpdu</i>, <i>ip</i>, <i>udp</i>, <i>tcp</i>, <i>rtp</i>, and <i>dns</i>. There is currently also a limited support for ICMP. Enter <i>-t help</i> to verify which packet builders your actual Mausezahn version supports. Also, for any particular packet type, for example <i>tcp</i> enter <i>mausezahn -t tcp help</i> to receive a context specific help.</p>
<dt><code>-T &lt;packet_type&gt;</code></p>
<dd> Make this Mausezahn instance the receiving station. Currently (version 0.30) only <i>rtp</i> is an option here and provides precise jitter measurements. For this purpose start another Mausezahn instance on the sending station and the local receiving station will output jitter statistics. See <i>mausezahn -T rtp help</i> for a detailed help.</p>
<dt><code>-Q &lt;[CoS:]vlan&gt; [, &lt;[CoS:]vlan&gt;, &#8230;]</code></p>
<dd> Specify 802.1Q VLAN tag and optional Class of Service. An arbitrary number of VLAN tags can be specified (that is you can simulate QinQ or even QinQinQinQ&#8230;). Multiple tags must be separated via a comma or a period (e. g. &quot;5:10,20,2:30&quot;). VLAN tags are not supported for ARP and BPDU packets (in which case you could specify the whole frame in hex using the raw layer 2 interface of Mausezahn).</p>
<dt><code>-M &lt;label[:cos[:ttl]][bos]&gt; [, &lt;label&#8230;&gt;] </code></p>
<dd> Specify a MPLS label or even a MPLS label stack. Optionally for each label the experimental bits (usually the Class of Service, CoS) and the Time To Live (TTL) can be specified. And if you are really crazy you can set/unset the Bottom of Stack (BoS) bit at each label using the <i>S</i> (set) and <i>s</i> (unset) option. By default the BoS is set automatically and correctly. Any other setting will lead to invalid frames. Enter <i>-M help</i> for detailed instructions and examples.</p>
<dt><code>-P &lt;ASCII_payload&gt;</code></p>
<dd> Specify a cleartext payload. Alternatively each packet type supports a hexadecimal specification of the payload (see for example <i>-t udp help</i>).
</dl>
<h2>COMBINATION OF RANGES</h2>
<p> When multiple ranges are specified, e. g. destination port ranges AND destination address ranges, then <code>all</code> possible combinations of ports and addresses are used for packet generation. This can lead to a very huge number of frames. </p>
<h2>DISCLAIMER AND WARNING</h2>
<p> Mausezahn has been designed as fast traffic generator so you quickly can overwhelm a LAN segment with myriads of packets. And because Mausezahn should also support security audits it is easily possible to create malicious packets, SYN floods, specify port and address ranges, DNS and ARP poisoning, etc.<br />
 Therefore, don&#8217;t use this tool when you are not aware of possible consequences or have only little knowledge about networks and data communication. If you abuse Mausezahn for unallowed attacks and get caught, or damage something of your own, then this is completely your fault. </p>
<h2>EXAMPLES</h2>
<p> Send BPDU frames for VLAN 5 as used with Cisco&#8217;s PVST+ type of STP. Per default Mausezahn assumes that you want to become the root bridge: </p>
<p> # mausezahn eth0 -c 0 -d 2s -t bpdu vlan=5 </p>
<p> Perform a CAM table overflow attack: </p>
<p> # mausezahn eth0 -c 128000 -a rand -p 64 </p>
<p> Perform a SYN flood attack to another VLAN using a VLAN hopping attack. This only works if you are connected to the same VLAN which is configured as native VLAN on the trunk. We assume that the victim VLAN is VLAN 100 and the native VLAN is VLAN 5. Also lets attack every host in VLAN 100 which use a IP prefix of 10.100.100.0/24: </p>
<p> # mausezahn eth0 -c 0 -Q 5,100 -t tcp flags=syn -p 20 </p>
<p> Send IP multicast packets to the multicast group 230.1.1.1 using a UDP header with destination port 32000. Send one frame every 10 msec: </p>
<p> # mausezahn eth0 -c 0 -d 10msec -B 230.1.1.1 -t udp dp=32000 -P &quot;Multicast test packet&quot; </p>
<p> Send UDP packets to the destination host target.anynetwork.foo using all possible destionation ports and send every packet with all possible source addresses of the range 172.30.0.0/16; pad with 1000 bytes and repeat this 10 times: </p>
<p> # mausezahn eth0 -c 10 -A 172.30.0.0/16 -B target.anynetwork.foo -t udp dp=1-65535 -p 1000 </p>
<h2>AUTHOR</h2>
<p> Herbert Haas<br />
 Visit <a rel="nofollow" href="http://www.perihel.at">www.perihel.at</a>/sec/mz/ for Mausezahn news and additional information. </p>
<p> This manual page has been written by Vivek Shah &lt;boni.vivek at gmail.com&gt; for the Fedora project. </p>
<h2>Index</h2>
