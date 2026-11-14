---
title: "netsniff-ng(8)"
name: "netsniff-ng"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netsniff-ng/"
description: "netsniff-ng – the packet sniffing beast"
---

<p>netsniff-ng &#8211; the packet sniffing beast </p>
<h2>Synopsis</h2>
<p><code>netsniff-ng</code> { [<i>options</i>] [<i>filter-expression</i>] } </p>
<h2>Description</h2>
<p>netsniff-ng is a fast, minimal tool to analyze network packets, capture pcap files, replay pcap files, and redirect traffic between interfaces with the help of zero-copy <a href="/docs/linux/man/7-packet/">packet</a>(7) sockets. netsniff-ng uses both Linux specific RX_RING and TX_RING interfaces to perform zero-copy. This is to avoid copy and system call overhead between kernel and user address space. When we started working on netsniff-ng, the <a href="/docs/linux/man/3-pcap/">pcap</a>(3) library did not use this zero-copy facility. netsniff-ng is Linux specific, meaning there is no support for other operating systems. Therefore we can keep the code footprint quite minimal and to the point. Linux <a href="/docs/linux/man/7-packet/">packet</a>(7) sockets and its RX_RING and TX_RING interfaces bypass the normal packet processing path through the networking stack. This is the fastest capturing or transmission performance one can get from user space out of the box, without having to load unsupported or non-mainline third-party kernel modules. We explicitly refuse to build netsniff-ng on top of ntop/PF_RING. Not because we do not like it (we do find it interesting), but because of the fact that it is not part of the mainline kernel. Therefore, the ntop project has to maintain and sync out-of-tree drivers to adapt them to their DNA. Eventually, we went for untainted Linux kernel, since its code has a higher rate of review, maintenance, security and bug fixes. netsniff-ng also supports early packet filtering in the kernel. It has support for low-level and high-level packet filters that are translated into Berkeley Packet Filter instructions. netsniff-ng can capture pcap files in several different pcap formats that are interoperable with other tools. It has different pcap I/O methods supported (scatter-gather, <a href="/docs/linux/man/2-mmap/">mmap</a>(2), <a href="/docs/linux/man/2-read/">read</a>(2), and <a href="/docs/linux/man/2-write/">write</a>(2)) for efficient to-disc capturing. netsniff-ng is also able to rotate pcap files based on data size or time intervals, thus, making it a useful backend tool for subsequent traffic analysis. netsniff-ng itself also supports analysis, replaying, and dumping of raw 802.11 frames. For online or offline analysis, netsniff-ng has a built-in packet dissector for the current 802.3 (Ethernet), 802.11* (WLAN), ARP, MPLS, 802.1Q (VLAN), 802.1QinQ, LLDP, IPv4, IPv6, ICMPv4, ICMPv6, IGMP, TCP and UDP, including GeoIP location analysis. Since netsniff-ng does not establish any state or perform reassembly during packet dissection, its memory footprint is quite low, thus, making netsniff-ng quite efficient for offline analysis of large pcap files as well. Note that netsniff-ng is currently not multithreaded. However, this does not prevent you from starting multiple netsniff-ng instances that are pinned to different, non-overlapping CPUs and f.e. have different BPF filters attached. Likely that at some point in time your harddisc might become a bottleneck assuming you do not rotate such pcaps in ram (and from there periodically scheduled move to slower medias). You can then use <a href="/docs/linux/man/1-mergecap/">mergecap</a>(1) to transform all pcaps into a single large pcap. Thus, netsniff-ng then works multithreaded eventually. netsniff-ng can also be used to debug netlink traffic. </p>
<h2>Options</h2>
<h3>-i &lt;dev|pcap|-&gt;, -d &lt;dev|pcap|-&gt;, &#8211;in &lt;dev|pcap|-&gt;, &#8211;dev &lt;dev|pcap|-&gt;</h3>
<p>Defines an input device. This can either be a networking device, a pcap file or stdin (&#8220;-&#8220;). In case of a pcap file, the pcap type (&#8220;-D&#8221; option) is determined automatically by the pcap file magic. In case of stdin, it is assumed that the input stream is a pcap file.</p>
<h3>-o &lt;dev|pcap|dir|cfg|-&gt;, &#8211;out &lt;dev|pcap|dir|cfg|-&gt;</h3>
<p>Defines the output device. This can either be a networking device, a pcap file, a folder, a <a href="/docs/linux/man/8-trafgen/">trafgen</a>(8) configuration file or stdout (&#8220;-&#8220;). In the case of a pcap file that should not have the default pcap type (0xa1b2c3d4), the additional option &#8220;-T&#8221; must be provided. If a directory is given, then, instead of a single pcap file, multiple pcap files are generated with rotation based on maximum file size or a given interval (&#8220;-F&#8221; option). A trafgen configuration file can currently only be specified if the input device is a pcap file. If stdout is given as a device, then a trafgen configuration will be written to stdout if the input device is a pcap file, or a pcap file if the input device is a networking device.</p>
<h3>-C &lt;id&gt;, &#8211;fanout-group &lt;id&gt;</h3>
<p>If multiple netsniff-ng instances are being started that all have the same packet fanout group id, then the ingress network traffic being captured is being distributed/load-balanced among these group participants. This gives a much better scaling than running multiple netsniff-ng processes without a fanout group parameter in parallel, but only with a BPF filter attached as a packet would otherwise need to be delivered to all such capturing processes, instead of only once to such a fanout member. Naturally, each fanout member can have its own BPF filters attached.</p>
<h3>-K &lt;hash|lb|cpu|rnd|roll|qm&gt;, &#8211;fanout-type &lt;hash|lb|cpu|rnd|roll|qm&gt;</h3>
<p>This parameter specifies the fanout discipline, in other words, how the captured network traffic is dispatched to the fanout group members. Options are to distribute traffic by the packet hash (&#8220;hash&#8221;), in a round-robin manner (&#8220;lb&#8221;), by CPU the packet arrived on (&#8220;cpu&#8221;), by random (&#8220;rnd&#8221;), by rolling over sockets (&#8220;roll&#8221;) which means if one socket&#8217;s queue is full, we move on to the next one, or by NIC hardware queue mapping (&#8220;qm&#8221;).</p>
<h3>-L &lt;defrag|roll&gt;, &#8211;fanout-opts &lt;defrag|roll&gt;</h3>
<p>Defines some auxillary fanout options to be used in addition to a given fanout type. These options apply to any fanout type. In case of &#8220;defrag&#8221;, the kernel is being told to defragment packets before delivering to user space, and &#8220;roll&#8221; provides the same roll-over option as the &#8220;roll&#8221; fanout type, so that on any different fanout type being used (e.g. &#8220;qm&#8221;) the socket may temporarily roll over to the next fanout group member in case the original one&#8217;s queue is full.</p>
<h3>-f, &#8211;filter &lt;bpf-file|expr&gt;</h3>
<p>Specifies to not dump all traffic, but to filter the network packet haystack. As a filter, either a <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) compiled file can be passed as a parameter or a <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)-like filter expression in quotes. For details regarding the bpf-file have a look at <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8), for details regarding a <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)-like filter have a look at section &#8220;filter example&#8221; or at <a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a>(7). A filter expression may also be passed to netsniff-ng without option &#8220;-f&#8221; in case there is no subsequent option following after the command-line filter expression.</p>
<h3>-t, &#8211;type &lt;type&gt;</h3>
<p>This defines some sort of filtering mechanisms in terms of addressing. Possible values for type are &#8220;host&#8221; (to us), &#8220;broadcast&#8221; (to all), &#8220;multicast&#8221; (to group), &#8220;others&#8221; (promiscuous mode) or &#8220;outgoing&#8221; (from us).</p>
<h3>-F, &#8211;interval &lt;size|time&gt;</h3>
<p>If the output device is a folder, with &#8220;-F&#8221;, it is possible to define the pcap file rotation interval either in terms of size or time. Thus, when the interval limit has been reached, a new pcap file will be started. As size parameter, the following values are accepted &#8220;&lt;num&gt;KiB/MiB/GiB&#8221;; As time parameter, it can be &#8220;&lt;num&gt;s/sec/min/hrs&#8221;.</p>
<h3>-J, &#8211;jumbo-support</h3>
<p>By default, in pcap replay or redirect mode, netsniff-ng&#8217;s ring buffer frames are a fixed size of 2048 bytes. This means that if you are expecting jumbo frames or even super jumbo frames to pass through your network, then you need to enable support for that by using this option. However, this has the disadvantage of performance degradation and a bigger memory footprint for the ring buffer. Note that this doesn&#8217;t affect (pcap) capturing mode, since tpacket in version 3 is used!</p>
<h3>-R, &#8211;rfraw</h3>
<p>In case the input or output networking device is a wireless device, it is possible with netsniff-ng to turn this into monitor mode and create a mon&lt;X&gt; device that netsniff-ng will be listening on instead of wlan&lt;X&gt;, for instance. This enables netsniff-ng to analyze, dump, or even replay raw 802.11 frames.</p>
<h3>-n &lt;0|uint&gt;, &#8211;num &lt;0|uint&gt;</h3>
<p>Process a number of packets and then exit. If the number of packets is 0, then this is equivalent to infinite packets resp. processing until interrupted. Otherwise, a number given as an unsigned integer will limit processing.</p>
<h3>-P &lt;name&gt;, &#8211;prefix &lt;name&gt;</h3>
<p>When dumping pcap files into a folder, a file name prefix can be defined with this option. If not otherwise specified, the default prefix is &#8220;dump-&#8221; followed by a Unix timestamp. Use &#8220;&#8211;prefex &quot;&quot;&#8221; to set filename as seconds since the Unix Epoch e.g. 1369179203.pcap</p>
<h3>-T &lt;pcap-magic&gt;, &#8211;magic &lt;pcap-magic&gt;</h3>
<p>Specify a pcap type for storage. Different pcap types with their various meta data capabilities are shown with option &#8220;-D&#8221;. If not otherwise specified, the pcap-magic 0xa1b2c3d4, also known as a standard tcpdump-capable pcap format, is used. Pcap files with swapped endianness are also supported.</p>
<h3>-D, &#8211;dump-pcap-types</h3>
<p>Dump all available pcap types with their capabilities and magic numbers that can be used with option &#8220;-T&#8221; to stdout and exit.</p>
<h3>-B, &#8211;dump-bpf</h3>
<p>If a Berkeley Packet Filter is given, for example via option &#8220;-f&#8221;, then dump the BPF disassembly to stdout during ring setup. This only serves for informative or verification purposes.</p>
<h3>-r, &#8211;rand</h3>
<p>If the input and output device are both networking devices, then this option will randomize packet order in the output ring buffer.</p>
<h3>-M, &#8211;no-promisc</h3>
<p>The networking interface will not be put into promiscuous mode. By default, promiscuous mode is turned on.</p>
<h3>-A, &#8211;no-sock-mem</h3>
<p>On startup and shutdown, netsniff-ng tries to increase socket read and write buffers if appropriate. This option will prevent netsniff-ng from doing so.</p>
<h3>-m, &#8211;mmap</h3>
<p>Use <a href="/docs/linux/man/2-mmap/">mmap</a>(2) as pcap file I/O. This is the default when replaying pcap files.</p>
<h3>-G, &#8211;sg</h3>
<p>Use scatter-gather as pcap file I/O. This is the default when capturing pcap files.</p>
<h3>-c, &#8211;clrw</h3>
<p>Use slower <a href="/docs/linux/man/2-read/">read</a>(2) and <a href="/docs/linux/man/2-write/">write</a>(2) I/O. This is not the default case anywhere, but in some situations it could be preferred as it has a lower latency on write-back to disc.</p>
<h3>-S &lt;size&gt;, &#8211;ring-size &lt;size&gt;</h3>
<p>Manually define the RX_RING resp. TX_RING size in &#8220;&lt;num&gt;KiB/MiB/GiB&#8221;. By default, the size is determined based on the network connectivity rate.</p>
<h3>-k &lt;uint&gt;, &#8211;kernel-pull &lt;uint&gt;</h3>
<p>Manually define the interval in micro-seconds where the kernel should be triggered to batch process the ring buffer frames. By default, it is every 10us, but it can manually be prolonged, for instance.</p>
<h3>-b &lt;cpu&gt;, &#8211;bind-cpu &lt;cpu&gt;</h3>
<p>Pin netsniff-ng to a specific CPU and also pin resp. migrate the NIC&#8217;s IRQ CPU affinity to this CPU. This option should be preferred in combination with &#8220;-s&#8221; in case a middle to high packet rate is expected.</p>
<h3>-u &lt;uid&gt;, &#8211;user &lt;uid&gt; resp. -g &lt;gid&gt;, &#8211;group &lt;gid&gt;</h3>
<p>After ring setup drop privileges to a non-root user/group combination.</p>
<h3>-H, &#8211;prio-high</h3>
<p>Set this process as a high priority process in order to achieve a higher scheduling rate resp. CPU time. This is however not the default setting, since it could lead to starvation of other processes, for example low priority kernel threads.</p>
<h3>-Q, &#8211;notouch-irq</h3>
<p>Do not reassign the NIC&#8217;s IRQ CPU affinity settings.</p>
<h3>-s, &#8211;silent</h3>
<p>Do not enter the packet dissector at all and do not print any packet information to the terminal. Just shut up and be silent. This option should be preferred in combination with pcap recording or replay, since it will not flood your terminal which causes a significant performance degradation.</p>
<h3>-q, &#8211;less</h3>
<p>Print a less verbose one-line information for each packet to the terminal.</p>
<h3>-X, &#8211;hex</h3>
<p>Only dump packets in hex format to the terminal.</p>
<h3>-l, &#8211;ascii</h3>
<p>Only display ASCII printable characters.</p>
<h3>-U, &#8211;update</h3>
<p>If geographical IP location is used, the built-in database update mechanism will be invoked to get Maxmind&#8217;s latest database. To configure search locations for databases, the file /etc/netsniff-ng/geoip.conf contains possible addresses. Thus, to save bandwidth or for mirroring of Maxmind&#8217;s databases (to bypass their traffic limit policy), different hosts or IP addresses can be placed into geoip.conf, separated by a newline.</p>
<h3>-V, &#8211;verbose</h3>
<p>Be more verbose during startup i.e. show detailed ring setup information.</p>
<h3>-v, &#8211;version</h3>
<p>Show version information and exit.</p>
<h3>-h, &#8211;help</h3>
<p>Show user help and exit.</p>
<h2>Usage Example</h2>
<h3>netsniff-ng</h3>
<p>The most simple command is to just run &#8220;netsniff-ng&#8221;. This will start listening on all available networking devices in promiscuous mode and dump the packet dissector output to the terminal. No files will be recorded.</p>
<h3>netsniff-ng &#8211;in eth0 &#8211;out dump.pcap -s -T 0xa1e2cb12 -b 0 tcp or udp</h3>
<p>Capture TCP or UDP traffic from the networking device eth0 into the pcap file named dump.pcap, which has netsniff-ng specific pcap extensions (see &#8220;netsniff-ng -D&#8221; for capabilities). Also, do not print the content to the terminal and pin the process and NIC IRQ affinity to CPU 0. The pcap write method is scatter-gather I/O.</p>
<h3>netsniff-ng &#8211;in wlan0 &#8211;rfraw &#8211;out dump.pcap &#8211;silent &#8211;bind-cpu 0</h3>
<p>Put the wlan0 device into monitoring mode and capture all raw 802.11 frames into the file dump.pcap. Do not dissect and print the content to the terminal and pin the process and NIC IRQ affinity to CPU 0. The pcap write method is scatter-gather I/O.</p>
<h3>netsniff-ng &#8211;in dump.pcap &#8211;mmap &#8211;out eth0 -k1000 &#8211;silent &#8211;bind-cpu 0</h3>
<p>Replay the pcap file dump.pcap which is read through <a href="/docs/linux/man/2-mmap/">mmap</a>(2) I/O and send the packets out via the eth0 networking device. Do not dissect and print the content to the terminal and pin the process and NIC IRQ affinity to CPU 0. Also, trigger the kernel every 1000us to traverse the TX_RING instead of every 10us. Note that the pcap magic type is detected automatically from the pcap file header.</p>
<h3>netsniff-ng &#8211;in eth0 &#8211;out eth1 &#8211;silent &#8211;bind-cpu 0 &#8211;type host -r</h3>
<p>Redirect network traffic from the networking device eth0 to eth1 for traffic that is destined for our host, thus ignore broadcast, multicast and promiscuous traffic. Randomize the order of packets for the outgoing device and do not print any packet contents to the terminal. Also, pin the process and NIC IRQ affinity to CPU 0.</p>
<h3>netsniff-ng &#8211;in team0 &#8211;out /opt/probe/ -s -m &#8211;interval 100MiB -b 0</h3>
<p>Capture on an aggregated team0 networking device and dump packets into multiple pcap files that are split into 100MiB each. Use <a href="/docs/linux/man/2-mmap/">mmap</a>(2) I/O as a pcap write method, support for super jumbo frames is built-in (does not need to be configured here), and do not print the captured data to the terminal. Pin netsniff-ng and NIC IRQ affinity to CPU 0. The default pcap magic type is 0xa1b2c3d4 (tcpdump-capable pcap).</p>
<h3>netsniff-ng &#8211;in vlan0 &#8211;out dump.pcap -c -u `id -u bob` -g `id -g bob`</h3>
<p>Capture network traffic on device wlan0 into a pcap file called dump.pcap by using normal <a href="/docs/linux/man/2-read/">read</a>(2), <a href="/docs/linux/man/2-write/">write</a>(2) I/O for the pcap file (slower but less latency). Also, after setting up the RX_RING for capture, drop privileges from root to the user and group &#8220;bob&#8221;. Invoke the packet dissector and print packet contents to the terminal for further analysis.</p>
<h3>netsniff-ng &#8211;in any &#8211;filter http.bpf -B &#8211;ascii -V</h3>
<p>Capture from all available networking interfaces and install a low-level filter that was previously compiled by <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) into http.bpf in order to filter HTTP traffic. Super jumbo frame support is automatically enabled and only print human readable packet data to the terminal, and also be more verbose during setup phase. Moreover, dump a BPF disassembly of http.bpf.</p>
<h3>netsniff-ng &#8211;in dump.pcap &#8211;out dump.cfg &#8211;silent</h3>
<p>Convert the pcap file dump.pcap into a <a href="/docs/linux/man/8-trafgen/">trafgen</a>(8) configuration file dump.cfg. Do not print pcap contents to the terminal.</p>
<h3>netsniff-ng -i dump.pcap -f beacon.bpf -o &#8211;</h3>
<p>Convert the pcap file dump.pcap into a <a href="/docs/linux/man/8-trafgen/">trafgen</a>(8) configuration file and write it to stdout. However, do not dump all of its content, but only the one that passes the low-level filter for raw 802.11 from beacon.bpf. The BPF engine here is invoked in user space inside of netsniff-ng, so Linux extensions are not available.</p>
<h3>cat foo.pcap | netsniff-ng -i &#8211; -o &#8211;</h3>
<p>Read a pcap file from stdin and convert it into a <a href="/docs/linux/man/8-trafgen/">trafgen</a>(8) configuration file to stdout.</p>
<h3>modprobe nlmon</h3>
<h3>ip link add type nlmon</h3>
<h3>ip link set nlmon0 up</h3>
<h3>netsniff-ng -i nlmon0 -o dump.pcap -s</h3>
<h3>ip link set nlmon0 down</h3>
<h3>ip link del dev nlmon0</h3>
<h3>rmmod nlmon</h3>
<p>In this example, netlink traffic is being captured. If not already done, a netlink monitoring device needs to be set up before it can be used to capture netlink socket buffers (iproute2&#8217;s <a href="/docs/linux/man/1-ip/">ip</a>(1) commands are given for nlmon device setup and teardown). netsniff-ng can then make use of the nlmon device as an input device. In this example a pcap file with netlink traffic is being recorded.</p>
<h3>netsniff-ng &#8211;fanout-group 1 &#8211;fanout-type cpu &#8211;fanout-opts defrag &#8211;bind-cpu 0 &#8211;notouch-irq &#8211;silent &#8211;in em1 &#8211;out /var/cap/cpu0/ &#8211;interval 120sec</h3>
<h3>netsniff-ng &#8211;fanout-group 1 &#8211;fanout-type cpu &#8211;fanout-opts defrag &#8211;bind-cpu 1 &#8211;notouch-irq &#8211;silent &#8211;in em1 &#8211;out /var/cap/cpu1/ &#8211;interval 120sec</h3>
<p>Starts two netsniff-ng fanout instances. Both are assigned into the same fanout group membership and traffic is splitted among them by incoming cpu. Furthermore, the kernel is supposed to defragment possible incoming fragments. First instance is assigned to CPU 0 and the second one to CPU 1, IRQ bindings are not altered as they might have been adapted to this scenario by the user a-priori, and traffic is captured on interface em1, and written out in 120 second intervals as pcap files into /var/cap/cpu0/. Tools like <a href="/docs/linux/man/1-mergecap/">mergecap</a>(1) will be able to merge the cpu0/1 split back together if needed.</p>
<h2>Config Files</h2>
<p>Files under /etc/netsniff-ng/ can be modified to extend netsniff-ng&#8217;s functionality: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>oui.conf &#8211; OUI/MAC vendor database<br />
&nbsp;<wbr>*&nbsp;<wbr>ether.conf &#8211; Ethernet type descriptions<br />
&nbsp;<wbr>*&nbsp;<wbr>tcp.conf &#8211; TCP port/services map<br />
&nbsp;<wbr>*&nbsp;<wbr>udp.conf &#8211; UDP port/services map<br />
&nbsp;<wbr>*&nbsp;<wbr>geoip.conf &#8211; GeoIP database mirrors</p>
<h2>Filter Example</h2>
<p>netsniff-ng supports both, low-level and high-level filters that are attached to its <a href="/docs/linux/man/7-packet/">packet</a>(7) socket. Low-level filters are described in the <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) man page. </p>
<p> Low-level filters can be used with netsniff-ng in the following way: </p>
<p>&nbsp;<wbr>1. bpfc foo&nbsp;<wbr>&gt;&nbsp;<wbr>bar<br />
&nbsp;<wbr>2. netsniff-ng -f bar </p>
<p> Here, foo is the bpfc program that will be translated into a netsniff-ng readable &#8220;opcodes&#8221; file and passed to netsniff-ng through the -f option. </p>
<p> Similarly, high-level filter can be either passed through the -f option, e.g. -f &quot;tcp or udp&quot; or at the end of all options without the &#8220;-f&#8221;. </p>
<p> The filter syntax is the same as in <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8), which is described in the man page <a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a>(7). Just to quote some examples from <a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a>(7):</p>
<h3>host sundown</h3>
<p>To select all packets arriving at or departing from sundown.</p>
<h3>host helios and hot or ace )</h3>
<p>To select traffic between helios and either hot or ace.</p>
<h3>ip host ace and not helios</h3>
<p>To select all IP packets between ace and any host except helios.</p>
<h3>net ucb-ether</h3>
<p>To select all traffic between local hosts and hosts at Berkeley.</p>
<h3>gateway snup and (port ftp or ftp-data)</h3>
<p>To select all FTP traffic through Internet gateway snup.</p>
<h3>ip and not net localnet</h3>
<p>To select traffic neither sourced from, nor destined for, local hosts. If you have a gateway to another network, this traffic should never make it onto your local network.</p>
<h3>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst net localnet</h3>
<p>To select the start and end packets (the SYN and FIN packets) of each TCP conversation that involve a non-local host.</p>
<h3>tcp port 80 and (((ip[2:2] &#8211; ((ip[0]&amp;0xf)&lt;&lt;2)) &#8211; ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)</h3>
<p>To select all IPv4 HTTP packets to and from port 80, that is to say, print only packets that contain data, not, for example, SYN and FIN packets and ACK-only packets. (IPv6 is left as an exercise for the reader.)</p>
<h3>gateway snup and ip[2:2] &gt; 576</h3>
<p>To select IP packets longer than 576 bytes sent through gateway snup.</p>
<h3>ether[0] &amp; 1 = 0 and ip[16] &gt;= 224</h3>
<p>To select IP broadcast or multicast packets that were not sent via Ethernet broadcast or multicast.</p>
<h3>icmp[icmptype] != icmp-echo and icmp[icmptype] != icmp-echoreply</h3>
<p>To select all ICMP packets that are not echo requests or replies (that is to say, not &quot;ping&quot; packets).</p>
<h2>Pcap Formats:</h2>
<p>netsniff-ng supports a couple of pcap formats, visible through &#8220;netsniff-ng -D&#8221;:</p>
<h3>tcpdump-capable pcap (default)</h3>
<p>Pcap magic number is encoded as 0xa1b2c3d4 resp. 0xd4c3b2a1. As packet meta data this format contains the timeval in microseconds, the original packet length and the captured packet length.</p>
<h3>tcpdump-capable pcap with ns resolution</h3>
<p>Pcap magic number is encoded as 0xa1b23c4d resp. 0x4d3cb2a1. As packet meta data this format contains the timeval in nanoseconds, the original packet length and the captured packet length.</p>
<h3>Alexey Kuznetzov&#8217;s pcap</h3>
<p>Pcap magic number is encoded as 0xa1b2cd34 resp. 0x34cdb2a1. As packet meta data this format contains the timeval in microseconds, the original packet length, the captured packet length, the interface index (sll_ifindex), the packet&#8217;s protocol (sll_protocol), and the packet type (sll_pkttype).</p>
<h3>netsniff-ng pcap</h3>
<p>Pcap magic number is encoded as 0xa1e2cb12 resp. 0x12cbe2a1. As packet meta data this format contains the timeval in nanoseconds, the original packet length, the captured packet length, the timestamp hw/sw source, the interface index (sll_ifindex), the packet&#8217;s protocol (sll_protocol), the packet type (sll_pkttype) and the hardware type (sll_hatype). </p>
<p> For further implementation details or format support in your application, have a look at pcap_io.h.</p>
<h2>Note</h2>
<p>For introducing bit errors, delays with random variation and more while replaying pcaps, make use of <a href="/docs/linux/man/8-tc/">tc</a>(8) with its disciplines such as netem. </p>
<p> netsniff-ng does only some basic, architecture generic tuning on startup. If you are considering to do high performance capturing, you need to carefully tune your machine, both hardware and software. Simply letting netsniff-ng run without thinking about your underlying system might not necessarily give you the desired performance. Note that tuning your system is always a tradeoff and fine-grained balancing act (throughput versus latency). You should know what you are doing! </p>
<p> One recommendation for software-based tuning is <a href="/docs/linux/man/8-tuned/">tuned</a>(8). Besides that, there are many other things to consider. Just to throw you a few things that you might want to look at: NAPI networking drivers, tickless kernel, I/OAT DMA engine, Direct Cache Access, RAM-based file systems, multi-queues, and many more things. Also, you might want to read the kernel&#8217;s Documentation/networking/scaling.txt file regarding technologies such as RSS, RPS, RFS, aRFS and XPS. Also check your <a href="/docs/linux/man/8-ethtool/">ethtool</a>(8) settings, for example regarding offloading or Ethernet pause frames. </p>
<p> Moreover, to get a deeper understanding of netsniff-ng internals and how it interacts with the Linux kernel, the kernel documentation under Documentation/networking/{packet_mmap.txt, filter.txt, multiqueue.txt} might be of interest. </p>
<p> How do you sniff in a switched environment? I rudely refer to dSniff&#8217;s documentation that says: </p>
<p> The easiest route is simply to impersonate the local gateway, stealing client traffic en route to some remote destination. Of course, the traffic must be forwarded by your attacking machine, either by enabling kernel IP forwarding or with a userland program that accomplishes the same (fragrouter -B1). </p>
<p> Several people have reportedly destroyed connectivity on their LAN to the outside world by ARP spoofing the gateway, and forgetting to enable IP forwarding on the attacking machine. Do not do this. You have been warned. </p>
<p> A safer option than ARP spoofing would be to use a &quot;port mirror&quot; function if your switch hardware supports it and if you have access to the switch. </p>
<p> If you do not need to dump all possible traffic, you have to consider running netsniff-ng with a BPF filter for the ingress path. For that purpose, read the <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) man page. </p>
<p> Also, to aggregate multiple NICs that you want to capture on, you should consider using team devices, further explained in libteam resp. <a href="/docs/linux/man/8-teamd/">teamd</a>(8). </p>
<p> The following netsniff-ng pcap magic numbers are compatible with other tools, at least tcpdump or Wireshark: </p>
<p>&nbsp;<wbr>0xa1b2c3d4&nbsp;<wbr>(tcpdump-capable pcap)<br />
&nbsp;<wbr>0xa1b23c4d&nbsp;<wbr>(tcpdump-capable pcap with ns resolution)<br />
&nbsp;<wbr>0xa1b2cd34&nbsp;<wbr>(Alexey Kuznetzov&#8217;s pcap) </p>
<p> Pcap files with different meta data endianness are supported by netsniff-ng as well.</p>
<h2>Bugs</h2>
<p>When replaying pcap files, the timing information from the pcap packet header is currently ignored. Also, when replaying pcap files, demultiplexing traffic among multiple networking interfaces does not work. Currently, it is only sent via the interface that is given by the &#8211;out parameter. When performing traffic capture on the Ethernet interface, the pcap file is created and packets are received but without a 802.1Q header. When one uses tshark, all headers are visible, but netsniff-ng removes 802.1Q headers. Is that normal behavior? Yes and no. The way VLAN headers are handled in PF_PACKET sockets by the kernel is somewhat &#8220;problematic&#8221; [1]. The problem in the Linux kernel is that some drivers already handle VLANs, others do not. Those who handle it can have different implementations, such as hardware acceleration and so on. So in some cases the VLAN tag is even stripped before entering the protocol stack, in some cases probably not. The bottom line is that a &quot;hack&quot; was introduced in PF_PACKET so that a VLAN ID is visible in some helper data structure that is accessible from the RX_RING. Then it gets really messy in the user space to artificially put the VLAN header back into the right place. Not to mention the resulting performance implications on all of <a href="/docs/linux/man/3-libpcap/">libpcap</a>(3) tools since parts of the packet need to be copied for reassembly via <a href="/docs/linux/man/3-memmove/">memmove</a>(3). A user reported the following, just to demonstrate this mess: some tests were made with two machines, and it seems that results depend on the driver &#8230;<br />
&nbsp;<wbr>AR8131:<br />
ethtool -k eth0 gives&nbsp;<wbr>&quot;rx-vlan-offload: on&quot;<br />
&#8211; wireshark gets the vlan header<br />
&#8211; netsniff-ng doesn&#8217;t get the vlan header<br />
ethtool -K eth0 rxvlan off<br />
&#8211; wireshark gets a QinQ header even though noone sent QinQ<br />
&#8211; netsniff-ng gets the vlan header<br />
&nbsp;<wbr>RTL8111/8168B:<br />
ethtool -k eth0 gives&nbsp;<wbr>&quot;rx-vlan-offload: on&quot;<br />
&#8211; wireshark gets the vlan header<br />
&#8211; netsniff-ng doesn&#8217;t get the vlan header<br />
ethtool -K eth0 rxvlan off<br />
&#8211; wireshark gets the vlan header<br />
&#8211; netsniff-ng doesn&#8217;t get the vlan header Even if we agreed on doing the same workaround as libpcap, we still will not be able to see QinQ, for instance, due to the fact that only one VLAN tag is stored in the kernel helper data structure. We think that there should be a good consensus on the kernel space side about what gets transferred to userland first. Update (28.11.2012): the Linux kernel and also <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) has built-in support for hardware accelerated VLAN filtering, even though tags might not be visible in the payload itself as reported here. However, the filtering for VLANs works reliable if your NIC supports it. See <a href="/docs/linux/man/8-bpfc/">bpfc</a>(8) for an example.<br />
[1]&nbsp;<wbr><a rel="nofollow" href="http://lkml.indiana.edu/hypermail/linux/kernel/0710.3/3816.html">http://lkml.indiana.edu/hypermail/linux/kernel/0710.3/3816.html</a> </p>
<h2>Legal</h2>
<p>netsniff-ng is licensed under the GNU GPL version 2.0.</p>
<h2>History</h2>
<p><code>netsniff-ng</code> was originally written for the netsniff-ng toolkit by Daniel Borkmann. Bigger contributions were made by Emmanuel Roullit, Markus Amend, Tobias Klauser and Christoph Jaeger. It is currently maintained by Tobias Klauser &lt;tklauser [at] distanz.ch&gt; and Daniel Borkmann &lt;dborkma [at] tik.ee.ethz.ch&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-trafgen/">trafgen</a></code>(8), <code><a href="/docs/linux/man/8-mausezahn/">mausezahn</a></code>(8), <code><a href="/docs/linux/man/8-ifpps/">ifpps</a></code>(8), <code><a href="/docs/linux/man/8-bpfc/">bpfc</a></code>(8), <code><a href="/docs/linux/man/8-flowtop/">flowtop</a></code>(8), <code><a href="/docs/linux/man/8-astraceroute/">astraceroute</a></code>(8), <code><a href="/docs/linux/man/8-curvetun/">curvetun</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage was written by Daniel Borkmann.</p>
<h2>Colophon</h2>
<p>This page is part of the Linux netsniff-ng toolkit project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://netsniff-ng.org/.">http://netsniff-ng.org/.</a> </p>
