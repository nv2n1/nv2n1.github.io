---
title: "trafgen(8)"
name: "trafgen"
section: "8"
letter: "t"
url: "/docs/linux/man/8-trafgen/"
description: "trafgen – a fast, multithreaded network packet generator"
---

<p>trafgen &#8211; a fast, multithreaded network packet generator </p>
<h2>Synopsis</h2>
<p><code>trafgen</code> [<i>options</i>] </p>
<h2>Description</h2>
<p>trafgen is a fast, zero-copy network traffic generator for debugging, performance evaluation, and fuzz-testing. trafgen utilizes the <a href="/docs/linux/man/7-packet/">packet</a>(7) socket interface of Linux which postpones complete control over packet data and packet headers into the user space. It has a powerful packet configuration language, which is rather low-level and not limited to particular protocols. Thus, trafgen can be used for many purposes. Its only limitation is that it cannot mimic full streams resp. sessions. However, it is very useful for various kinds of load testing in order to analyze and subsequently improve systems behaviour under DoS attack scenarios, for instance. trafgen is Linux specific, meaning there is no support for other operating systems, same as <a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a>(8), thus we can keep the code footprint quite minimal and to the point. trafgen makes use of <a href="/docs/linux/man/7-packet/">packet</a>(7) socket&#8217;s TX_RING interface of the Linux kernel, which is a <a href="/docs/linux/man/2-mmap/">mmap</a>(2)&#8217;ed ring buffer shared between user and kernel space. By default, trafgen starts as many processes as available CPUs, pins each of them to their respective CPU and sets up the ring buffer each in their own process space after having compiled a list of packets to transmit. Thus, this is likely the fastest one can get out of the box in terms of transmission performance from user space, without having to load unsupported or non-mainline third-party kernel modules. On Gigabit Ethernet, trafgen has a comparable performance to pktgen, the built-in Linux kernel traffic generator, except that trafgen is more flexible in terms of packet configuration possibilities. On 10-Gigabit-per-second Ethernet, trafgen might be slower than pktgen due to the user/kernel space overhead but still has a fairly high performance for out of the box kernels. trafgen has the potential to do fuzz testing, meaning a packet configuration can be built with random numbers on all or certain packet offsets that are freshly generated each time a packet is sent out. With a built-in IPv4 ping, trafgen can send out an ICMP probe after each packet injection to the remote host in order to test if it is still responsive/alive. Assuming there is no answer from the remote host after a certain threshold of probes, the machine is considered dead and the last sent packet is printed together with the random seed that was used by trafgen. You might not really get lucky fuzz-testing the Linux kernel, but presumably there are buggy closed-source embedded systems or network driver&#8217;s firmware files that are prone to bugs, where trafgen could help in finding them. trafgen&#8217;s configuration language is quite powerful, also due to the fact, that it supports C preprocessor macros. A stddef.h is being shipped with trafgen for this purpose, so that well known defines from Linux kernel or network programming can be reused. After a configuration file has passed the C preprocessor stage, it is processed by the trafgen packet compiler. The language itself supports a couple of features that are useful when assembling packets, such as built-in runtime checksum support for IP, UDP and TCP. Also it has an expression evaluator where arithmetic (basic operations, bit operations, bit shifting, &#8230;) on constant expressions is being reduced to a single constant on compile time. Other features are &#8221;fill&#8221; macros, where a packet can be filled with n bytes by a constant, a compile-time random number or run-time random number (as mentioned with fuzz testing). Also, <a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a>(8) is able to convert a pcap file into a trafgen configuration file, thus such a configuration can then be further tweaked for a given scenario. </p>
<h2>Options</h2>
<h3>-i &lt;cfg|-&gt;, -c &lt;cfg|i&gt;, &#8211;in &lt;cfg|-&gt;, &#8211;conf &lt;cfg|-&gt;</h3>
<p>Defines the input configuration file that can either be passed as a normal plain text file or via stdin (&#8221;-&#8221;). Note that currently, if a configuration is passed through stdin, only 1 CPU will be used.</p>
<h3>-o &lt;dev&gt;, -d &lt;dev&gt;, &#8211;out &lt;dev&gt;, &#8211;dev &lt;dev&gt;</h3>
<p>Defines the outgoing networking device such as eth0, wlan0 and others.</p>
<h3>-p, &#8211;cpp</h3>
<p>Pass the packet configuration to the C preprocessor before reading it into trafgen. This allows #define and #include directives (e.g. to include definitions from system headers) to be used in the trafgen configuration file.</p>
<h3>-J, &#8211;jumbo-support</h3>
<p>By default trafgen&#8217;s ring buffer frames are of a fixed size of 2048 bytes. This means that if you&#8217;re expecting jumbo frames or even super jumbo frames to pass your line, then you will need to enable support for that with the help of this option. However, this has the disadvantage of a performance regression and a bigger memory footprint for the ring buffer.</p>
<h3>-R, &#8211;rfraw</h3>
<p>In case the output networking device is a wireless device, it is possible with trafgen to turn this into monitor mode and create a mon&lt;X&gt; device that trafgen will be transmitting on instead of wlan&lt;X&gt;, for instance. This enables trafgen to inject raw 802.11 frames.</p>
<h3>-s &lt;ipv4&gt;, &#8211;smoke-test &lt;ipv4&gt;</h3>
<p>In case this option is enabled, trafgen will perform a smoke test. In other words, it will probe the remote end, specified by an &lt;ipv4&gt; address, that is being &#8221;attacked&#8221; with trafgen network traffic, if it is still alive and responsive. That means, after each transmitted packet that has been configured, trafgen sends out ICMP echo requests and waits for an answer before it continues. In case the remote end stays unresponsive, trafgen assumes that the machine has crashed and will print out the content of the last packet as a trafgen packet configuration and the random seed that has been used in order to reproduce a possible bug. This might be useful when testing proprietary embedded devices. It is recommended to have a direct link between the host running trafgen and the host being attacked by trafgen.</p>
<h3>-n &lt;0|uint&gt;, &#8211;num &lt;0|uint&gt;</h3>
<p>Process a number of packets and then exit. If the number of packets is 0, then this is equivalent to infinite packets resp. processing until interrupted. Otherwise, a number given as an unsigned integer will limit processing.</p>
<h3>-r, &#8211;rand</h3>
<p>Randomize the packet selection of the configuration file. By default, if more than one packet is defined in a packet configuration, packets are scheduled for transmission in a round robin fashion. With this option, they are selected randomly instread.</p>
<h3>-P &lt;uint&gt;, &#8211;cpus &lt;uint&gt;</h3>
<p>Specify the number of processes trafgen shall <a href="/docs/linux/man/2-fork/">fork</a>(2) off. By default trafgen will start as many processes as CPUs that are online and pin them to each, respectively. Allowed value must be within interval [1,CPUs].</p>
<h3>-t &lt;uint&gt;, &#8211;gap &lt;uint&gt;</h3>
<p>Specify a static inter-packet timegap in micro-seconds. If this option is given, then instead of <a href="/docs/linux/man/7-packet/">packet</a>(7)&#8217;s TX_RING interface, trafgen will use <a href="/docs/linux/man/2-sendto/">sendto</a>(2) I/O for network packets, even if the &lt;uint&gt; argument is 0. This option is useful for a couple of reasons: i) comparison between <a href="/docs/linux/man/2-sendto/">sendto</a>(2) and TX_RING performance, ii) low-traffic packet probing for a given interval, iii) ping-like debugging with specific payload patterns. Furthermore, the TX_RING interface does not cope with interpacket gaps.</p>
<h3>-S &lt;size&gt;, &#8211;ring-size &lt;size&gt;</h3>
<p>Manually define the TX_RING resp. TX_RING size in &#8221;&lt;num&gt;KiB/MiB/GiB&#8221;. On default the size is being determined based on the network connectivity rate.</p>
<h3>-k &lt;uint&gt;, &#8211;kernel-pull &lt;uint&gt;</h3>
<p>Manually define the interval in micro-seconds where the kernel should be triggered to batch process the ring buffer frames. By default, it is every 10us, but it can manually be prolonged, for instance..</p>
<h3>-E &lt;uint&gt;, &#8211;seed &lt;uint&gt;</h3>
<p>Manually set the seed for pseudo random number generator (PRNG) in trafgen. By default, a random seed from /dev/urandom is used to feed glibc&#8217;s PRNG. If that fails, it falls back to the unix timestamp. It can be useful to set the seed manually in order to be able to reproduce a trafgen session, e.g. after fuzz testing.</p>
<h3>-u &lt;uid&gt;, &#8211;user &lt;uid&gt; resp. -g &lt;gid&gt;, &#8211;group &lt;gid&gt;</h3>
<p>After ring setup, drop privileges to a non-root user/group combination.</p>
<h3>-V, &#8211;verbose</h3>
<p>Let trafgen be more talkative and let it print the parsed configuration and some ring buffer statistics.</p>
<h3>-e, &#8211;example</h3>
<p>Show a built-in packet configuration example. This might be a good starting point for an initial packet configuration scenario.</p>
<h3>-C, &#8211;no-cpu-stats</h3>
<p>Do not print CPU time statistics on exit.</p>
<h3>-v, &#8211;version</h3>
<p>Show version information and exit.</p>
<h3>-h, &#8211;help</h3>
<p>Show user help and exit.</p>
<h2>Syntax</h2>
<p>trafgen&#8217;s packet configuration syntax is fairly simple. The very basic things one needs to know is that a configuration file is a simple plain text file where packets are defined. It can contain one or more packets. Packets are enclosed by opening &#8216;{&#8216; and closing &#8216;}&#8217; braces, for example: </p>
<p>{&nbsp;<wbr>/*&nbsp;<wbr>packet 1 content goes here &#8230;&nbsp;<wbr>*/&nbsp;<wbr>}<br />
{&nbsp;<wbr>/*&nbsp;<wbr>packet 2 content goes here &#8230;&nbsp;<wbr>*/&nbsp;<wbr>} </p>
<p> When trafgen is started using multiple CPUs (default), then each of those packets will be scheduled for transmission on all CPUs by default. However, it is possible to tell trafgen to schedule a packet only on a particular CPU: </p>
<p><a href="/docs/linux/man/1-cpu/">cpu</a>(1):&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>packet 1 content goes here &#8230;&nbsp;<wbr>*/&nbsp;<wbr>}<br />
cpu(2-3):&nbsp;<wbr>{&nbsp;<wbr>/*&nbsp;<wbr>packet 2 content goes here &#8230;&nbsp;<wbr>*/&nbsp;<wbr>} </p>
<p> Thus, in case we have a 4 core machine with CPU0-CPU3, packet 1 will be scheduled only on CPU1, packet 2 on CPU2 and CPU3. When using trafgen with &#8211;num option, then these constraints will still be valid and the packet is fairly distributed among those CPUs. </p>
<p> Packet content is delimited either by a comma or whitespace, or both: </p>
<p>{&nbsp;<wbr>0xca, 0xfe, 0xba 0xbe&nbsp;<wbr>} </p>
<p> Packet content can be of the following: </p>
<p>hex bytes:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0xca, xff<br />
decimal:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>42<br />
binary:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0b11110000, b11110000<br />
octal:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>011<br />
character:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8216;a&#8217;<br />
string:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;hello world&quot;<br />
shellcode:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;1ۍC�̀1�&quot; </p>
<p> Thus, a quite useless packet packet configuration might look like this (one can verify this when running this with trafgen in combination with -V): </p>
<p>{&nbsp;<wbr>0xca, 42, 0b11110000, 011,&nbsp;<wbr>&#8216;a&#8217;,&nbsp;<wbr>&quot;hello world&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;1ۍC�̀1�&quot;&nbsp;<wbr>} </p>
<p> There are a couple of helper functions in trafgen&#8217;s language to make life easier to write configurations: </p>
<p> i) Fill with garbage functions: </p>
<p>byte fill function:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fill(&lt;content&gt;,&nbsp;<wbr>&lt;times&gt;): fill(0xca, 128)<br />
compile-time random:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rnd(&lt;times&gt;): rnd(128), rnd()<br />
runtime random numbers:&nbsp;<wbr>&nbsp;<wbr>drnd(&lt;times&gt;): drnd(128), drnd()<br />
compile-time counter:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>seqinc(&lt;start-val&gt;,&nbsp;<wbr>&lt;increment&gt;,&nbsp;<wbr>&lt;times&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>seqdec(&lt;start-val&gt;,&nbsp;<wbr>&lt;decrement&gt;,&nbsp;<wbr>&lt;times&gt;)<br />
runtime counter&nbsp;<wbr>(1byte): dinc(&lt;min-val&gt;,&nbsp;<wbr>&lt;max-val&gt;,&nbsp;<wbr>&lt;increment&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ddec(&lt;min-val&gt;,&nbsp;<wbr>&lt;max-val&gt;,&nbsp;<wbr>&lt;decrement&gt;) </p>
<p> ii) Checksum helper functions (packet offsets start with 0): </p>
<p>IP/ICMP checksum:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>csumip/csumicmp(&lt;off-from&gt;,&nbsp;<wbr>&lt;off-to&gt;)<br />
UDP checksum:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>csumudp(&lt;off-iphdr&gt;,&nbsp;<wbr>&lt;off-udpdr&gt;)<br />
TCP checksum:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>csumtcp(&lt;off-iphdr&gt;,&nbsp;<wbr>&lt;off-tcphdr&gt;) </p>
<p> iii) Multibyte functions, compile-time expression evaluation: </p>
<p>const8(&lt;content&gt;), c8(&lt;content&gt;), const16(&lt;content&gt;), c16(&lt;content&gt;),<br />
const32(&lt;content&gt;), c32(&lt;content&gt;), const64(&lt;content&gt;), c64(&lt;content&gt;) </p>
<p>These functions write their result in network byte order into the packet configuration, e.g. const16(0xaa) will result in &#8221;00 aa&#8221;. Within c*() functions, it is possible to do some arithmetics: -,+,*,/,%,&amp;,|,&lt;&lt;,&gt;&gt;,^ E.g. const16((((1&lt;&lt;8)+0x32)|0b110)*2) will be evaluated to &#8221;02 6c&#8221;. </p>
<p> Furthermore, there are two types of comments in trafgen configuration files: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1. Multi-line C-style comments:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>put comment here&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>2. Single-line Shell-style comments:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>put comment here </p>
<p> Next to all of this, a configuration can be passed through the C preprocessor before the trafgen compiler gets to see it with option &#8211;cpp. To give you a taste of a more advanced example, run &#8221;trafgen -e&#8221;, fields are commented: </p>
<p>/*&nbsp;<wbr>Note: dynamic elements make trafgen slower!&nbsp;<wbr>*/<br />
#include&nbsp;<wbr>&lt;stddef.h&gt; </p>
<p>{<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>MAC Destination&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>fill(0xff, ETH_ALEN),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>MAC Source&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>0x00, 0x02, 0xb3,&nbsp;<wbr><a href="/docs/linux/man/3-drnd/">drnd</a>(3),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Protocol&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c16(ETH_P_IP),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Version, IHL, TOS&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>0b01000101, 0,<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Total Len&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c16(59),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Ident&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/2-drnd/">drnd</a>(2),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Flags, Frag Off&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>0b01000000, 0,<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 TTL&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>64,<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Proto TCP&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>0x06,<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>IPv4 Checksum&nbsp;<wbr>(IP header from, to)&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>csumip(14, 33),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Source IP&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/4-drnd/">drnd</a>(4),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Dest IP&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/4-drnd/">drnd</a>(4),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Source Port&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/2-drnd/">drnd</a>(2),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Dest Port&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c16(80),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Sequence Number&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/4-drnd/">drnd</a>(4),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Ackn. Number&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c32(0),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Header length&nbsp;<wbr>+&nbsp;<wbr>TCP SYN/ECN Flag&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c16((8&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>12)&nbsp;<wbr>| TCP_FLAG_SYN | TCP_FLAG_ECE)<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Window Size&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>c16(16),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Checksum&nbsp;<wbr>(offset IP, offset TCP)&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>csumtcp(14, 34),<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>TCP Options&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>0x00, 0x00, 0x01, 0x01, 0x08, 0x0a, 0x06,<br />
&nbsp;<wbr>&nbsp;<wbr>0x91, 0x68, 0x7d, 0x06, 0x91, 0x68, 0x6f,<br />
&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Data blob&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;gotcha!&quot;,<br />
} </p>
<p> Another real-world example by Jesper Dangaard Brouer [1]: </p>
<p>{<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8212; ethernet header &#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>0x00, 0x1b, 0x21, 0x3c, 0x9d, 0xf8,&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>mac destination<br />
&nbsp;<wbr>&nbsp;<wbr>0x90, 0xe2, 0xba, 0x0a, 0x56, 0xb4,&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>mac source<br />
&nbsp;<wbr>&nbsp;<wbr>const16(0x0800),&nbsp;<wbr>#&nbsp;<wbr>protocol<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8212; ip header &#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipv4 version&nbsp;<wbr>(4-bit)&nbsp;<wbr>+&nbsp;<wbr>ihl&nbsp;<wbr>(4-bit), tos<br />
&nbsp;<wbr>&nbsp;<wbr>0b01000101, 0,<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipv4 total len<br />
&nbsp;<wbr>&nbsp;<wbr>const16(40),<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>id&nbsp;<wbr>(note: runtime dynamic random)<br />
&nbsp;<wbr>&nbsp;<wbr><a href="/docs/linux/man/2-drnd/">drnd</a>(2),<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipv4 3-bit flags&nbsp;<wbr>+&nbsp;<wbr>13-bit fragment offset<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>001&nbsp;<wbr>=&nbsp;<wbr>more fragments<br />
&nbsp;<wbr>&nbsp;<wbr>0b00100000, 0,<br />
&nbsp;<wbr>&nbsp;<wbr>64,&nbsp;<wbr>#&nbsp;<wbr>ttl<br />
&nbsp;<wbr>&nbsp;<wbr>17,&nbsp;<wbr>#&nbsp;<wbr>proto udp<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>dynamic ip checksum&nbsp;<wbr>(note: offsets are zero indexed)<br />
&nbsp;<wbr>&nbsp;<wbr>csumip(14, 33),<br />
&nbsp;<wbr>&nbsp;<wbr>192, 168, 51, 1,&nbsp;<wbr>#&nbsp;<wbr>source ip<br />
&nbsp;<wbr>&nbsp;<wbr>192, 168, 51, 2,&nbsp;<wbr>#&nbsp;<wbr>dest ip<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&#8212; udp header &#8212;<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>as this is a fragment the below stuff does not matter too much<br />
&nbsp;<wbr>&nbsp;<wbr>const16(48054),&nbsp;<wbr>#&nbsp;<wbr>src port<br />
&nbsp;<wbr>&nbsp;<wbr>const16(43514),&nbsp;<wbr>#&nbsp;<wbr>dst port<br />
&nbsp;<wbr>&nbsp;<wbr>const16(20),&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>udp length<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>udp checksum can be dyn calc via csumudp(offset ip, offset tcp)<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>which is csumudp(14, 34), but for udp its allowed to be zero<br />
&nbsp;<wbr>&nbsp;<wbr>const16(0),<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>payload<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;A&#8217;,&nbsp;<wbr>&nbsp;<wbr>fill(0x41, 11),<br />
} </p>
<p>[1]&nbsp;<wbr><a rel="nofollow" href="http://thread.gmane.org/gmane.linux.network/257155">http://thread.gmane.org/gmane.linux.network/257155</a></p>
<h2>Usage Example</h2>
<h3>trafgen &#8211;dev eth0 &#8211;conf trafgen.cfg</h3>
<p>This is the most simple and, probably, the most common use of trafgen. It will generate traffic defined in the configuration file &#8221;trafgen.cfg&#8221; and transmit this via the &#8221;eth0&#8221; networking device. All online CPUs are used.</p>
<h3>trafgen -e | trafgen -i &#8211; -o lo &#8211;cpp -n 1</h3>
<p>This is an example where we send one packet of the built-in example through the loopback device. The example configuration is passed via stdin and also through the C preprocessor before trafgen&#8217;s packet compiler will see it.</p>
<h3>trafgen &#8211;dev eth0 &#8211;conf fuzzing.cfg &#8211;smoke-test 10.0.0.1</h3>
<p>Read the &#8221;fuzzing.cfg&#8221; packet configuration file (which contains drnd() calls) and send out the generated packets to the &#8221;eth0&#8221; device. After each sent packet, ping probe the attacked host with address 10.0.0.1 to check if it&#8217;s still alive. This also means, that we utilize 1 CPU only, and do not use the TX_RING, but <a href="/docs/linux/man/2-sendto/">sendto</a>(2) packet I/O due to &#8221;slow mode&#8221;.</p>
<h3>trafgen &#8211;dev wlan0 &#8211;rfraw &#8211;conf beacon-test.txf -V &#8211;cpus 2</h3>
<p>As an output device &#8221;wlan0&#8221; is used and put into monitoring mode, thus we are going to transmit raw 802.11 frames through the air. Use the use only 2 CPUs.</p>
<h3>trafgen &#8211;dev em1 &#8211;conf frag_dos.cfg &#8211;rand &#8211;gap 1000</h3>
<p>Use trafgen in <a href="/docs/linux/man/2-sendto/">sendto</a>(2) mode instead of TX_RING mode and sleep after each sent packet a static timegap for 1000us. Generate packets from &#8221;frag_dos.cfg&#8221; and select next packets to send randomly instead of a round-robin fashion. The output device for packets is &#8221;em1&#8221;.</p>
<h3>trafgen &#8211;dev eth0 &#8211;conf icmp.cfg &#8211;rand &#8211;num 1400000 -k1000</h3>
<p>Send only 1400000 packets using the &#8221;icmp.cfg&#8221; configuration file and then exit trafgen. Select packets randomly from that file for transmission and send them out via &#8221;eth0&#8221;. Also, trigger the kernel every 1000us for batching the ring frames from user space (default is 10us).</p>
<h3>trafgen &#8211;dev eth0 &#8211;conf tcp_syn.cfg -u `id -u bob` -g `id -g bob`</h3>
<p>Send out packets generated from the configuration file &#8221;tcp_syn.cfg&#8221; via the &#8221;eth0&#8221; networking device. After setting up the ring for transmission, drop credentials to the non-root user/group bob/bob.</p>
<h2>Note</h2>
<p>trafgen can saturate a Gigabit Ethernet link without problems. As always, of course, this depends on your hardware as well. Not everywhere where it says Gigabit Ethernet on the box, will you reach almost physical line rate! Please also read the <a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a>(8) man page, section NOTE for further details about tuning your system e.g. with <a href="/docs/linux/man/8-tuned/">tuned</a>(8). </p>
<p> If you intend to use trafgen on a 10-Gbit/s Ethernet NIC, make sure you are using a multiqueue <a href="/docs/linux/man/8-tc/">tc</a>(8) discipline, and make sure that the packets you generate with trafgen will have a good distribution among tx_hashes so that you&#8217;ll actually make use of multiqueues. </p>
<p> For introducing bit errors, delays with random variation and more, there is no built-in option in trafgen. Rather, one should reuse existing methods for that which integrate nicely with trafgen, such as <a href="/docs/linux/man/8-tc/">tc</a>(8) with its different disciplines, i.e. netem. </p>
<p> For more complex packet configurations, it is recommended to use high-level scripting for generating trafgen packet configurations in a more automated way, i.e. also to create different traffic distributions that are common for industrial benchmarking: </p>
<p>&nbsp;<wbr>Traffic model&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Distribution </p>
<p>&nbsp;<wbr>IMIX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64:7,&nbsp;<wbr>&nbsp;<wbr>570:4,&nbsp;<wbr>&nbsp;<wbr>1518:1<br />
&nbsp;<wbr>Tolly&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64:55,&nbsp;<wbr>&nbsp;<wbr>78:5,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>576:17, 1518:23<br />
&nbsp;<wbr>Cisco&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64:7,&nbsp;<wbr>&nbsp;<wbr>594:4,&nbsp;<wbr>&nbsp;<wbr>1518:1<br />
&nbsp;<wbr>RPR Trimodal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64:60, 512:20, 1518:20<br />
&nbsp;<wbr>RPR Quadrimodal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64:50, 512:15, 1518:15, 9218:20 </p>
<p> The low-level nature of trafgen makes trafgen rather protocol independent and therefore useful in many scenarios when stress testing is needed, for instance. However, if a traffic generator with higher level packet descriptions is desired, netsniff-ng&#8217;s <a href="/docs/linux/man/8-mausezahn/">mausezahn</a>(8) can be of good use as well. </p>
<p> For smoke/fuzz testing with trafgen, it is recommended to have a direct link between the host you want to analyze (&#8221;victim&#8221; machine) and the host you run trafgen on (&#8221;attacker&#8221; machine). If the ICMP reply from the victim fails, we assume that probably its kernel crashed, thus we print the last sent packet togther with the seed and quit probing. It might be very unlikely to find such a ping-of-death on modern Linux systems. However, there might be a good chance to find it on some proprietary (e.g. embedded) systems or buggy driver firmwares that are in the wild. Also, fuzz testing can be done on raw 802.11 frames, of course. In case you find a ping-of-death, please mention that you were using trafgen in your commit message of the fix!</p>
<h2>Bugs</h2>
<p>For old trafgen versions only, there could occur kernel crashes: we have fixed this bug in the mainline and stable kernels under commit 7f5c3e3a8 (&#8221;af_packet: remove BUG statement in tpacket_destruct_skb&#8221;) and also in trafgen. Probably the best is if you upgrade trafgen to the latest version. </p>
<h2>Legal</h2>
<p>trafgen is licensed under the GNU GPL version 2.0.</p>
<h2>History</h2>
<p><code>trafgen</code> was originally written for the netsniff-ng toolkit by Daniel Borkmann. It is currently maintained by Tobias Klauser &lt;tklauser [at] distanz.ch&gt; and Daniel Borkmann &lt;dborkma [at] tik.ee.ethz.ch&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netsniff-ng/">netsniff-ng</a></code>(8), <code><a href="/docs/linux/man/8-mausezahn/">mausezahn</a></code>(8), <code><a href="/docs/linux/man/8-ifpps/">ifpps</a></code>(8), <code><a href="/docs/linux/man/8-bpfc/">bpfc</a></code>(8), <code><a href="/docs/linux/man/8-flowtop/">flowtop</a></code>(8), <code><a href="/docs/linux/man/8-astraceroute/">astraceroute</a></code>(8), <code><a href="/docs/linux/man/8-curvetun/">curvetun</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage was written by Daniel Borkmann.</p>
<h2>Colophon</h2>
<p>This page is part of the Linux netsniff-ng toolkit project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://netsniff-ng.org/.">http://netsniff-ng.org/.</a> </p>
