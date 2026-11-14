---
title: "icmp(7)"
name: "icmp"
section: "7"
letter: "i"
url: "/docs/linux/man/7-icmp/"
description: "icmp – Linux IPv4 ICMP kernel module."
---

<p>icmp &#8211; Linux IPv4 ICMP kernel module.</p>
<h2>Description</h2>
<p>This kernel protocol module implements the Internet Control Message Protocol defined in RFC 792. It is used to signal error conditions and for diagnosis. The user doesn&#8217;t interact directly with this module; instead it communicates with the other protocols in the kernel and these pass the ICMP errors to the application layers. The kernel ICMP module also answers ICMP requests. </p>
<p> A user protocol may receive ICMP packets for all local sockets by opening a raw socket with the protocol <code>IPPROTO_ICMP</code>. See <code><a href="/docs/linux/man/7-raw/">raw</a></code>(7) for more information. The types of ICMP packets passed to the socket can be filtered using the <code>ICMP_FILTER</code> socket option. ICMP packets are always processed by the kernel too, even when passed to a user socket. </p>
<p> Linux limits the rate of ICMP error packets to each destination. <code>ICMP_REDIRECT</code> and <code>ICMP_DEST_UNREACH</code> are also limited by the destination route of the incoming packets.</p>
<h3>/proc interfaces</h3>
<p>ICMP supports a set of <i>/proc</i> interfaces to configure some global IP parameters. The parameters can be accessed by reading or writing files in the directory <i>/proc/sys/net/ipv4/</i>. Most of these parameters are rate limitations for specific ICMP types. Linux 2.2 uses a token bucket filter to limit ICMPs. The value is the timeout in jiffies until the token bucket filter is cleared after a burst. A jiffy is a system dependent unit, usually 10ms on i386 and about 1ms on alpha and ia64.</p>
<dl>
<dt><i>icmp_destunreach_rate</i> (Linux 2.2 to 2.4.9)</p>
<dd>Maximum rate to send ICMP Destination Unreachable packets. This limits the rate at which packets are sent to any individual route or destination. The limit does not affect sending of <code>ICMP_FRAG_NEEDED</code> packets needed for path MTU discovery.</p>
<dt><i>icmp_echo_ignore_all</i> (since Linux 2.2)</p>
<dd>If this value is nonzero, Linux will ignore all <code>ICMP_ECHO</code> requests.</p>
<dt><i>icmp_echo_ignore_broadcasts</i> (since Linux 2.2)</p>
<dd>If this value is nonzero, Linux will ignore all <code>ICMP_ECHO</code> packets sent to broadcast addresses.</p>
<dt><i>icmp_echoreply_rate</i> (Linux 2.2 to 2.4.9)</p>
<dd>Maximum rate for sending <code>ICMP_ECHOREPLY</code> packets in response to <code>ICMP_ECHOREQUEST</code> packets.</p>
<dt><i>icmp_errors_use_inbound_ifaddr</i> (Boolean; default: disabled; since Linux 2.6.12)</p>
<dd>If disabled, ICMP error messages are sent with the primary address of the exiting interface.</p>
<dd>If enabled, the message will be sent with the primary address of the interface that received the packet that caused the ICMP error. This is the behavior that many network administrators will expect from a router. And it can make debugging complicated network layouts much easier.</p>
<dd>Note that if no primary address exists for the interface selected, then the primary address of the first non-loopback interface that has one will be used regardless of this setting.</p>
<dt><i>icmp_ignore_bogus_error_responses</i> (Boolean; default: disabled; since Linux 2.2)</p>
<dd>Some routers violate RFC1122 by sending bogus responses to broadcast frames. Such violations are normally logged via a kernel warning. If this parameter is enabled, the kernel will not give such warnings, which will avoid log file clutter.</p>
<dt><i>icmp_paramprob_rate</i> (Linux 2.2 to 2.4.9)</p>
<dd>Maximum rate for sending <code>ICMP_PARAMETERPROB</code> packets. These packets are sent when a packet arrives with an invalid IP header.</p>
<dt><i>icmp_ratelimit</i> (integer; default: 1000; since Linux 2.4.10)</p>
<dd>Limit the maximum rates for sending ICMP packets whose type matches <i>icmp_ratemask</i> (see below) to specific targets. 0 to disable any limiting, otherwise the minimum space between responses in milliseconds.</p>
<dt><i>icmp_ratemask</i> (integer; default: see below; since Linux 2.4.10)</p>
<dd>Mask made of ICMP types for which rates are being limited.</p>
<dd>Significant bits: IHGFEDCBA9876543210<br />
 Default mask: 0000001100000011000 (0x1818)</p>
<dd>Bit definitions (see the Linux kernel source file <i>include/linux/icmp.h</i>):</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>0 Echo Reply</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>3 Destination Unreachable *</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>4 Source Quench *</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>5 Redirect</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>8 Echo Request</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>B Time Exceeded *</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>C Parameter Problem *</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>D Timestamp Request</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>E Timestamp Reply</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>F Info Request</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>G Info Reply</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>H Address Mask Request</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>I Address Mask Reply</td>
<td>
</td>
</tr>
</table>
</dl>
</dl>
<p> The bits marked with an asterisk are rate limited by default (see the default mask above).</p>
<dl>
<dt><i>icmp_timeexceed_rate</i> (Linux 2.2 to 2.4.9)</p>
<dd>Maximum rate for sending <code>ICMP_TIME_EXCEEDED</code> packets. These packets are sent to prevent loops when a packet has crossed too many hops.</p>
<dt><i>ping_group_range</i> (two integers; default: see below; since Linux 2.6.39)</p>
<dd>Range of the group IDs (minimum and maximum group IDs, inclusive) that are allowed to create ICMP Echo sockets. The default is &quot;1 0&quot;, which means no group is allowed to create ICMP Echo sockets.</dl>
<h2>Versions</h2>
<p>Support for the <code>ICMP_ADDRESS</code> request was removed in 2.2. </p>
<p> Support for <code>ICMP_SOURCE_QUENCH</code> was removed in Linux 2.2.</p>
<h2>Notes</h2>
<p>As many other implementations don&#8217;t support <code>IPPROTO_ICMP</code> raw sockets, this feature should not be relied on in portable programs. </p>
<p> <code>ICMP_REDIRECT</code> packets are not sent when Linux is not acting as a router. They are also accepted only from the old gateway defined in the routing table and the redirect routes are expired after some time. </p>
<p> The 64-bit timestamp returned by <code>ICMP_TIMESTAMP</code> is in milliseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). </p>
<p> Linux ICMP internally uses a raw socket to send ICMPs. This raw socket may appear in <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8) output with a zero inode.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/8-rdisc/">rdisc</a></code>(8) </p>
<p> RFC 792 for a description of the ICMP protocol.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
