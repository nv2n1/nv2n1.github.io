---
title: "tc-cake(8)"
name: "tc-cake"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-cake/"
description: "CAKE – Common Applications Kept Enhanced (CAKE)"
---

<p>CAKE &#8211; Common Applications Kept Enhanced (CAKE)</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; cake</code><br />
 [ <code>bandwidth</code> RATE | <code>unlimited*</code> | <code>autorate-ingress</code> ]<br />
 [ <code>rtt</code> TIME | <code>datacentre</code> | <code>lan</code> | <code>metro</code> | <code>regional</code> | <code>internet*</code> | <code>oceanic</code> | <code>satellite</code> | <code>interplanetary</code> ]<br />
 [ <code>besteffort</code> | <code>diffserv8</code> | <code>diffserv4</code> | <code>diffserv3*</code> ]<br />
 [ <code>flowblind</code> | <code>srchost</code> | <code>dsthost</code> | <code>hosts</code> | <code>flows</code> | <code>dual-srchost</code> | <code>dual-dsthost</code> | <code>triple-isolate*</code> ]<br />
 [ <code>nat</code> | <code>nonat*</code> ]<br />
 [ <code>wash</code> | <code>nowash*</code> ]<br />
 [ <code>split-gso*</code> | <code>no-split-gso</code> ]<br />
 [ <code>ack-filter</code> | <code>ack-filter-aggressive</code> | <code>no-ack-filter*</code> ]<br />
 [ <code>memlimit</code> LIMIT ]<br />
 [ <code>fwmark</code> MASK ]<br />
 [ <code>ptm</code> | <code>atm</code> | <code>noatm*</code> ]<br />
 [ <code>overhead</code> N | <code>conservative</code> | <code>raw*</code> ]<br />
 [ <code>mpu</code> N ]<br />
 [ <code>ingress</code> | <code>egress*</code> ]<br />
 (* marks defaults) </p>
<h2>Description</h2>
<p>CAKE (Common Applications Kept Enhanced) is a shaping-capable queue discipline which uses both AQM and FQ. It combines COBALT, which is an AQM algorithm combining Codel and BLUE, a shaper which operates in deficit mode, and a variant of DRR++ for flow isolation. 8-way set-associative hashing is used to virtually eliminate hash collisions. Priority queuing is available through a simplified diffserv implementation. Overhead compensation for various encapsulation schemes is tightly integrated. All settings are optional; the default settings are chosen to be sensible in most common deployments. Most people will only need to set the <code>bandwidth</code> parameter to get useful results, but reading the <code>Overhead Compensation</code> and <code>Round Trip Time</code> sections is strongly encouraged. </p>
<h2>Shaper Parameters</h2>
<p>CAKE uses a deficit-mode shaper, which does not exhibit the initial burst typical of token-bucket shapers. It will automatically burst precisely as much as required to maintain the configured throughput. As such, it is very straightforward to configure. </p>
<p> <code>unlimited</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>No limit on the bandwidth.</p>
<p> <code>bandwidth</code> RATE<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set the shaper bandwidth. See<br />
 <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> or examples below for details of the RATE value. </p>
<p> <code>autorate-ingress</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Automatic capacity estimation based on traffic arriving at this qdisc.<br />
 This is most likely to be useful with cellular links, which tend to change quality randomly. A <code>bandwidth</code> parameter can be used in conjunction to specify an initial estimate. The shaper will periodically be set to a bandwidth slightly below the estimated rate. This estimator cannot estimate the bandwidth of links downstream of itself.</p>
<h2>Overhead Compensation Parameters</h2>
<p>The size of each packet on the wire may differ from that seen by Linux. The following parameters allow CAKE to compensate for this difference by internally considering each packet to be bigger than Linux informs it. To assist users who are not expert network engineers, keywords have been provided to represent a number of common link technologies.</p>
<h3>Manual Overhead Specification</h3>
<p><code>overhead</code> BYTES<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Adds BYTES to the size of each packet. BYTES may be negative; values<br />
 between -64 and 256 (inclusive) are accepted. </p>
<p> <code>mpu</code> BYTES<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Rounds each packet (including overhead) up to a minimum length<br />
 BYTES. BYTES may not be negative; values between 0 and 256 (inclusive) are accepted. </p>
<p> <code>atm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compensates for ATM cell framing, which is normally found on ADSL links.<br />
 This is performed after the <code>overhead</code> parameter above. ATM uses fixed 53-byte cells, each of which can carry 48 bytes payload. </p>
<p> <code>ptm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compensates for PTM encoding, which is normally found on VDSL2 links and<br />
 uses a 64b/65b encoding scheme. It is even more efficient to simply derate the specified shaper bandwidth by a factor of 64/65 or 0.984. See ITU G.992.3 Annex N and IEEE 802.3 Section 61.3 for details. </p>
<p> <code>noatm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disables ATM and PTM compensation.</p>
<h3>Failsafe Overhead Keywords</h3>
<p>These two keywords are provided for quick-and-dirty setup. Use them if you can&#8217;t be bothered to read the rest of this section. </p>
<p> <code>raw</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Turns off all overhead compensation in CAKE. The packet size reported<br />
 by Linux will be used directly. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Other overhead keywords may be added after &quot;raw&quot;. The effect of this is<br />
 to make the overhead compensation operate relative to the reported packet size, not the underlying IP packet size. </p>
<p> <code>conservative</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Compensates for more overhead than is likely to occur on any<br />
 widely-deployed link technology.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 48 atm.</code></p>
<h3>ADSL Overhead Keywords</h3>
<p>Most ADSL modems have a way to check which framing scheme is in use. Often this is also specified in the settings document provided by the ISP. The keywords in this section are intended to correspond with these sources of information. All of them implicitly set the <code>atm</code> flag. </p>
<p> <code>pppoa-vcmux</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 10 atm</code> </p>
<p> <code>pppoa-llc</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 14 atm</code> </p>
<p> <code>pppoe-vcmux</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 32 atm</code> </p>
<p> <code>pppoe-llcsnap</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 40 atm</code> </p>
<p> <code>bridged-vcmux</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 24 atm</code> </p>
<p> <code>bridged-llcsnap</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 32 atm</code> </p>
<p> <code>ipoa-vcmux</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 8 atm</code> </p>
<p> <code>ipoa-llcsnap</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 16 atm</code> </p>
<p> See also the Ethernet Correction Factors section below.</p>
<h3>VDSL2 Overhead Keywords</h3>
<p>ATM was dropped from VDSL2 in favour of PTM, which is a much more straightforward framing scheme. Some ISPs retained PPPoE for compatibility with their existing back-end systems. </p>
<p> <code>pppoe-ptm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 30 ptm</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PPPoE: 2B PPP + 6B PPPoE +</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>ETHERNET: 6B dest MAC + 6B src MAC + 2B ethertype + 4B Frame Check Sequence +</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PTM: 1B Start of Frame (S) + 1B End of Frame (Ck) + 2B TC-CRC (PTM-FCS)</p>
<p> <code>bridged-ptm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 22 ptm</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>ETHERNET: 6B dest MAC + 6B src MAC + 2B ethertype + 4B Frame Check Sequence +</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PTM: 1B Start of Frame (S) + 1B End of Frame (Ck) + 2B TC-CRC (PTM-FCS)</p>
<p> See also the Ethernet Correction Factors section below.</p>
<h3>DOCSIS Cable Overhead Keyword</h3>
<p>DOCSIS is the universal standard for providing Internet service over cable-TV infrastructure. </p>
<p> In this case, the actual on-wire overhead is less important than the packet size the head-end equipment uses for shaping and metering. This is specified to be an Ethernet frame including the CRC (aka FCS). </p>
<p> <code>docsis</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 18 mpu 64 noatm</code></p>
<h3>Ethernet Overhead Keywords</h3>
<p><code>ethernet</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Accounts for Ethernet&#8217;s preamble, inter-frame gap, and Frame Check<br />
 Sequence. Use this keyword when the bottleneck being shaped for is an actual Ethernet cable.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Equivalent to<br />
 <code>overhead 38 mpu 84 noatm</code> </p>
<p> <code>ether-vlan</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Adds 4 bytes to the overhead compensation, accounting for an IEEE 802.1Q<br />
 VLAN header appended to the Ethernet frame header. NB: Some ISPs use one or even two of these within PPPoE; this keyword may be repeated as necessary to express this.</p>
<h2>Round Trip Time Parameters</h2>
<p>Active Queue Management (AQM) consists of embedding congestion signals in the packet flow, which receivers use to instruct senders to slow down when the queue is persistently occupied. CAKE uses ECN signalling when available, and packet drops otherwise, according to a combination of the Codel and BLUE AQM algorithms called COBALT. </p>
<p> Very short latencies require a very rapid AQM response to adequately control latency. However, such a rapid response tends to impair throughput when the actual RTT is relatively long. CAKE allows specifying the RTT it assumes for tuning various parameters. Actual RTTs within an order of magnitude of this will generally work well for both throughput and latency management. </p>
<p> At the &#8216;lan&#8217; setting and below, the time constants are similar in magnitude to the jitter in the Linux kernel itself, so congestion might be signalled prematurely. The flows will then become sparse and total throughput reduced, leaving little or no back-pressure for the fairness logic to work against. Use the &quot;metro&quot; setting for local lans unless you have a custom kernel. </p>
<p> <code>rtt</code> TIME<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Manually specify an RTT.</p>
<p> <code>datacentre</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For extremely high-performance 10GigE+ networks only. Equivalent to<br />
 <code>rtt 100us.</code> </p>
<p> <code>lan</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For pure Ethernet (not Wi-Fi) networks, at home or in the office. Don&#8217;t<br />
 use this when shaping for an Internet access link. Equivalent to <code>rtt 1ms.</code> </p>
<p> <code>metro</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For traffic mostly within a single city. Equivalent to<br />
 <code>rtt 10ms.</code> </p>
<p> <code>regional</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For traffic mostly within a European-sized country. Equivalent to<br />
 <code>rtt 30ms.</code> </p>
<p> <code>internet</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>This is suitable for most Internet traffic. Equivalent to<br />
 <code>rtt 100ms.</code> </p>
<p> <code>oceanic</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For Internet traffic with generally above-average latency, such as that<br />
 suffered by Australasian residents. Equivalent to <code>rtt 300ms.</code> </p>
<p> <code>satellite</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>For traffic via geostationary satellites. Equivalent to<br />
 <code>rtt 1000ms.</code> </p>
<p> <code>interplanetary</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>So named because Jupiter is about 1 light-hour from Earth. Use this to<br />
 (almost) completely disable AQM actions. Equivalent to <code>rtt 3600s.</code></p>
<h2>Flow Isolation Parameters</h2>
<p>With flow isolation enabled, CAKE places packets from different flows into different queues, each of which carries its own AQM state. Packets from each queue are then delivered fairly, according to a DRR++ algorithm which minimizes latency for &quot;sparse&quot; flows. CAKE uses a set-associative hashing algorithm to minimize flow collisions. </p>
<p> These keywords specify whether fairness based on source address, destination address, individual flows, or any combination of those is desired. </p>
<p> <code>flowblind</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disables flow isolation; all traffic passes through a single queue for<br />
 each tin. </p>
<p> <code>srchost</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined only by source address. Could be useful on the egress<br />
 path of an ISP backhaul. </p>
<p> <code>dsthost</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined only by destination address. Could be useful on the<br />
 ingress path of an ISP backhaul. </p>
<p> <code>hosts</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined by source-destination host pairs. This is host<br />
 isolation, rather than flow isolation. </p>
<p> <code>flows</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined by the entire 5-tuple of source address, destination<br />
 address, transport protocol, source port and destination port. This is the type of flow isolation performed by SFQ and fq_codel. </p>
<p> <code>dual-srchost</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined by the 5-tuple, and fairness is applied first over<br />
 source addresses, then over individual flows. Good for use on egress traffic from a LAN to the internet, where it&#8217;ll prevent any one LAN host from monopolising the uplink, regardless of the number of flows they use. </p>
<p> <code>dual-dsthost</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined by the 5-tuple, and fairness is applied first over<br />
 destination addresses, then over individual flows. Good for use on ingress traffic to a LAN from the internet, where it&#8217;ll prevent any one LAN host from monopolising the downlink, regardless of the number of flows they use. </p>
<p> <code>triple-isolate</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Flows are defined by the 5-tuple, and fairness is applied over source<br />
 *and* destination addresses intelligently (ie. not merely by host-pairs), and also over individual flows. Use this if you&#8217;re not certain whether to use dual-srchost or dual-dsthost; it&#8217;ll do both jobs at once, preventing any one host on *either* side of the link from monopolising it with a large number of flows. </p>
<p> <code>nat</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Instructs Cake to perform a NAT lookup before applying flow-isolation<br />
 rules, to determine the true addresses and port numbers of the packet, to improve fairness between hosts &quot;inside&quot; the NAT. This has no practical effect in &quot;flowblind&quot; or &quot;flows&quot; modes, or if NAT is performed on a different host. </p>
<p> <code>nonat</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Cake will not perform a NAT lookup. Flow isolation will be performed<br />
 using the addresses and port numbers directly visible to the interface Cake is attached to.</p>
<h2>Priority Queue Parameters</h2>
<p>CAKE can divide traffic into &quot;tins&quot; based on the Diffserv field. Each tin has its own independent set of flow-isolation queues, and is serviced based on a WRR algorithm. To avoid perverse Diffserv marking incentives, tin weights have a &quot;priority sharing&quot; value when bandwidth used by that tin is below a threshold, and a lower &quot;bandwidth sharing&quot; value when above. Bandwidth is compared against the threshold using the same algorithm as the deficit-mode shaper. </p>
<p> Detailed customisation of tin parameters is not provided. The following presets perform all necessary tuning, relative to the current shaper bandwidth and RTT settings. </p>
<p> <code>besteffort</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disables priority queuing by placing all traffic in one tin.</p>
<p> <code>precedence</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Enables legacy interpretation of TOS &quot;Precedence&quot; field. Use of this<br />
 preset on the modern Internet is firmly discouraged. </p>
<p> <code>diffserv4</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Provides a general-purpose Diffserv implementation with four tins:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Bulk (CS1, LE in kernel v5.9+), 6.25% threshold, generally low priority.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Best Effort (general), 100% threshold.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Video (AF4x, AF3x, CS3, AF2x, CS2, TOS4, TOS1), 50% threshold.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Voice (CS7, CS6, EF, VA, CS5, CS4), 25% threshold.</p>
<p> <code>diffserv3</code> (default)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Provides a simple, general-purpose Diffserv implementation with three tins:</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Bulk (CS1, LE in kernel v5.9+), 6.25% threshold, generally low priority.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Best Effort (general), 100% threshold.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Voice (CS7, CS6, EF, VA, TOS4), 25% threshold, reduced Codel interval.</p>
<p> <code>fwmark</code> MASK<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>This options turns on fwmark-based overriding of CAKE&#8217;s tin selection.<br />
 If set, the option specifies a bitmask that will be applied to the fwmark associated with each packet. If the result of this masking is non-zero, the result will be right-shifted by the number of least-significant unset bits in the mask value, and the result will be used as a the tin number for that packet. This can be used to set policies in a firewall script that will override CAKE&#8217;s built-in tin selection.</p>
<h2>Other Parameters</h2>
<p><code>memlimit</code> LIMIT<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Limit the memory consumed by Cake to LIMIT bytes. Note that this does<br />
 not translate directly to queue size (so do not size this based on bandwidth delay product considerations, but rather on worst case acceptable memory consumption), as there is some overhead in the data structures containing the packets, especially for small packets. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>By default, the limit is calculated based on the bandwidth and RTT<br />
 settings. </p>
<p> <code>wash</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Traffic entering your diffserv domain is frequently mis-marked in<br />
 transit from the perspective of your network, and traffic exiting yours may be mis-marked from the perspective of the transiting provider. </p>
<p> Apply the wash option to clear all extra diffserv (but not ECN bits), after priority queuing has taken place. </p>
<p> If you are shaping inbound, and cannot trust the diffserv markings (as is the case for Comcast Cable, among others), it is best to use a single queue &quot;besteffort&quot; mode with wash. </p>
<p> <code>split-gso</code> </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>This option controls whether CAKE will split General Segmentation<br />
 Offload (GSO) super-packets into their on-the-wire components and dequeue them individually. </p>
<p> Super-packets are created by the networking stack to improve efficiency. However, because they are larger they take longer to dequeue, which translates to higher latency for competing flows, especially at lower bandwidths. CAKE defaults to splitting GSO packets to achieve the lowest possible latency. At link speeds higher than 10 Gbps, setting the no-split-gso parameter can increase the maximum achievable throughput by retaining the full GSO packets.</p>
<h2>Overriding Classification With Tc Filters</h2>
<p>CAKE supports overriding of its internal classification of packets through the tc filter mechanism. Packets can be assigned to different priority tins by setting the <code>priority</code> field on the skb, and the flow hashing can be overridden by setting the <code>classid</code> parameter. </p>
<p> <code>Tin override</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;To assign a priority tin, the major number of the priority field needs to match the qdisc handle of the cake instance; if it does, the minor number will be interpreted as the tin index. For example, to classify all ICMP packets as &#8216;bulk&#8217;, the following filter can be used: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;tc qdisc replace dev eth0 handle 1: root cake diffserv3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;tc filter add dev eth0 parent 1: protocol ip prio 1&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 match icmp type 0 0 action skbedit priority 1:1 </p>
<p> <code>Flow hash override</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;To override flow hashing, the classid can be set. CAKE will interpret the major number of the classid as the host hash used in host isolation mode, and the minor number as the flow hash used for flow-based queueing. One or both of those can be set, and will be used if the relevant flow isolation parameter is set (i.e., the major number will be ignored if CAKE is not configured in hosts mode, and the minor number will be ignored if CAKE is not configured in flows mode). </p>
<p> This example will assign all ICMP packets to the first queue: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;tc qdisc replace dev eth0 handle 1: root cake<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;tc filter add dev eth0 parent 1: protocol ip prio 1&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 match icmp type 0 0 classid 0:1 </p>
<p> If only one of the host and flow overrides is set, CAKE will compute the other hash from the packet as normal. Note, however, that the host isolation mode works by assigning a host ID to the flow queue; so if overriding both host and flow, the same flow cannot have more than one host assigned. In addition, it is not possible to assign different source and destination host IDs through the override mechanism; if a host ID is assigned, it will be used as both source and destination host.</p>
<h2>Examples</h2>
<p># tc qdisc delete root dev eth0<br />
 # tc qdisc add root dev eth0 cake bandwidth 100Mbit ethernet<br />
 # tc -s qdisc show dev eth0<br />
 qdisc cake 1: root refcnt 2 bandwidth 100Mbit diffserv3 triple-isolate rtt 100.0ms noatm overhead 38 mpu 84<br />
&nbsp;Sent 0 bytes 0 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;backlog 0b 0p requeues 0<br />
&nbsp;memory used: 0b of 5000000b<br />
&nbsp;capacity estimate: 100Mbit<br />
&nbsp;min/max network layer size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;65535&nbsp;/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;min/max overhead-adjusted size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;65535&nbsp;/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;average network hdr offset:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bulk&nbsp;<wbr>&nbsp;Best Effort&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Voice<br />
&nbsp;<wbr>&nbsp;thresh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6250Kbit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100Mbit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;25Mbit<br />
&nbsp;<wbr>&nbsp;target&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms<br />
&nbsp;<wbr>&nbsp;interval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms<br />
&nbsp;<wbr>&nbsp;pk_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us<br />
&nbsp;<wbr>&nbsp;av_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us<br />
&nbsp;<wbr>&nbsp;sp_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0us<br />
&nbsp;<wbr>&nbsp;pkts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;way_inds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;way_miss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;way_cols&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;drops&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;marks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;ack_drop&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;sp_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;bk_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;un_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;max_len&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;quantum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;300&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1514&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;762 After some use:<br />
 # tc -s qdisc show dev eth0 qdisc cake 1: root refcnt 2 bandwidth 100Mbit diffserv3 triple-isolate rtt 100.0ms noatm overhead 38 mpu 84<br />
&nbsp;Sent 44709231 bytes 31931 pkt&nbsp;(dropped 45, overlimits 93782 requeues 0)<br />
&nbsp;backlog 33308b 22p requeues 0<br />
&nbsp;memory used: 292352b of 5000000b<br />
&nbsp;capacity estimate: 100Mbit<br />
&nbsp;min/max network layer size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;28&nbsp;/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1500<br />
&nbsp;min/max overhead-adjusted size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;84&nbsp;/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1538<br />
&nbsp;average network hdr offset:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;14<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bulk&nbsp;<wbr>&nbsp;Best Effort&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Voice<br />
&nbsp;<wbr>&nbsp;thresh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6250Kbit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100Mbit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;25Mbit<br />
&nbsp;<wbr>&nbsp;target&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms<br />
&nbsp;<wbr>&nbsp;interval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100.0ms<br />
&nbsp;<wbr>&nbsp;pk_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8.7ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6.9ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.0ms<br />
&nbsp;<wbr>&nbsp;av_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4.9ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5.3ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3.8ms<br />
&nbsp;<wbr>&nbsp;sp_delay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;727us&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1.4ms&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;511us<br />
&nbsp;<wbr>&nbsp;pkts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2590&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;21271&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8137<br />
&nbsp;<wbr>&nbsp;bytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3081804&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;30302659&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;11426206<br />
&nbsp;<wbr>&nbsp;way_inds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;46&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;way_miss&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;17&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4<br />
&nbsp;<wbr>&nbsp;way_cols&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;drops&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;20&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;10<br />
&nbsp;<wbr>&nbsp;marks&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;ack_drop&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;sp_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;bk_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1<br />
&nbsp;<wbr>&nbsp;un_flows&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;max_len&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1514&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1514&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1514<br />
&nbsp;<wbr>&nbsp;quantum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;300&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1514&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;762 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-codel/">tc-codel</a></code>(8), <code><a href="/docs/linux/man/8-tc-fq_codel/">tc-fq_codel</a></code>(8), <code><a href="/docs/linux/man/8-tc-htb/">tc-htb</a></code>(8) </p>
<h2>Authors</h2>
<p>Cake&#8217;s principal author is Jonathan Morton, with contributions from Tony Ambardar, Kevin Darbyshire-Bryant, Toke Høiland-Jørgensen, Sebastian Moeller, Ryan Mounce, Dean Scarff, Nils Andreas Svee, and Dave Täht. </p>
<p> This manual page was written by Loganaden Velvindron. Please report corrections to the Linux Networking mailing list &lt;netdev [at] vger.kernel.org&gt;.</p>
