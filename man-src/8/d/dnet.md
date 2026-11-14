---
title: "dnet(8)"
name: "dnet"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnet/"
description: "dnet – dumb networking library test program"
---

<p><code>dnet</code> &#8211; dumb networking library test program</p>
<h2>Synopsis</h2>
<p><code>dnet </code><i>command args </i>[&#8230;]</p>
<h2>Description</h2>
<p><code>dnet Ar command Ar args Op &#8230;</code> is a simple test program for the <a href="/docs/linux/man/3-dnet/">dnet</a>(3) library. It can be used to compose and transmit network datagrams as a Unix-style filter (e.g. reading from or writing to files and pipes) or modify the local system network configuration (including the ARP cache, firewall ruleset, network interfaces, and routing table).</p>
<h3>Payload generation commands</h3>
<dl>
<dt><code>addr </code><i>address </i>[&#8230;]</p>
<dd>Convert the <i>address</i> (specified as a hostname, IP address, or MAC address) into its binary representation on standard output.</p>
<dt><code>hex </code><i>string </i>[&#8230;]</p>
<dd>Convert the C-style escaped <i>string</i> (shellcode, for instance) into its binary representation on standard output.</p>
<dt><code>rand </code><i>len</i></p>
<dd>Write <i>len</i> random bytes to standard output.</dl>
<h3>Packet encapsulation commands</h3>
<dl>
<dt> <code>eth</code> [<code>type </code><i>type </i> ] [<code>src </code><i>mac</i> ] [<code>dst </code><i>mac</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with an Ethernet header on standard output. The Ethernet <i>type</i> may be specified as `arp&#8217; , `ip&#8217; , or as a hex, octal, or decimal number.</p>
<dt> <code>arp</code> [<code>op </code><i>op</i> ] [<code>sha </code><i>mac</i> ] [<code>spa </code><i>host</i> ] [<code>tha </code><i>mac</i> ] [<code>tpa </code><i>host</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with an ARP header on standard output. The ARP <i>op</i> may be specified as `req&#8217; , `rep&#8217; , `revreq&#8217; , `revrep&#8217; , or as a hex, octal, or decimal number.</p>
<dt> <code>ip</code> [<code>tos </code><i>num</i> ] [<code>id </code><i>num</i> ] [<code>off </code><i>offset</i> ] [<code>ttl </code><i>num</i> ] [<code>proto </code><i>protocol</i> ] [<code>src </code><i>host</i> ] -words [<code>dst </code><i>dst</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with an IP header on standard output. The fragmentation <i>offset</i> may be specified as a decimal number (optionally concatenated with `+&#8217; to indicate more fragments) or as a hex number. The <i>protocol</i> may be specified by name, or as a hex, octal, or decimal number.</p>
<dt> <code>icmp</code> [<code>type </code><i>num</i> ] [<code>code </code><i>num</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with an ICMP header on standard output.</p>
<dt> <code>tcp</code> [<code>sport </code><i>port</i> ] [<code>dport </code><i>port</i> ] [<code>flags </code><i>flags</i> ] [<code>seq </code><i>num</i> ] [<code>ack </code><i>num</i> ] [<code>win </code><i>num</i> ] [<code>urp </code><i>num</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with a TCP header on standard output. A <i>port</i> may be specified by name or hex, octal, or decimal number. The TCP <i>flags</i> may be specified as some combination of the characters in the set `SAFRPU&#8217; or as a hex number.</p>
<dt> <code>udp</code> [<code>sport </code><i>port</i> ] [<code>dport </code><i>port</i> ]</p>
<dd>
<dd>Prepend the data read from standard input with a UDP header on standard output. A <i>port</i> may be specified by name or hex, octal, or decimal number.</dl>
<h3>Packet transmission commands</h3>
<dl>
<dt><code>send </code>[<i>device</i> ]</p>
<dd>Read a packet from standard input and send it over the network. If no <i>device</i> is specified, the packet is assumed to be an IP datagram and routed to its destination. Otherwise, the packet is assumed to be an Ethernet frame and is transmitted on the specified interface.</dl>
<h3>Kernel interface commands</h3>
<dl>
<dt><code>arp show</code></p>
<dd>Display the kernel ARP cache.</p>
<dt><code>arp get </code><i>host</i></p>
<dd>Display the kernel ARP entry for <i>host</i></p>
<dt><code>arp add </code><i>host mac</i></p>
<dd>Add an ARP entry mapping the <i>mac</i> address for <i>host</i></p>
<dt><code>arp delete </code><i>host</i></p>
<dd>Delete the ARP entry for <i>host</i></p>
<dt><code>fw show</code></p>
<dd>Display the kernel firewall ruleset.</p>
<dt> <code>fw add | delete</code> <i>action direction device </i> <i>protocol </i> <i>src </i>[: <i>port[-max]</i> ] <i>dst </i>[: <i>port[-max]</i> ] [<i>type </i>[/code] ]</p>
<dd>
<dd>Add a rule to or delete a rule from the active firewall ruleset. The <i>action</i> must be either `allow&#8217; or `block&#8217; The direction must be either `in&#8217; or `out&#8217; The <i>device</i> may specify an interface name, or `any&#8217; The <i>protocol</i> may be specified by name, or as a decimal number. For TCP and UDP protocols, a <i>port</i> (or range, if specified with a <i>max</i> value) may be specified in decimal and appended to the source and/or destination address. For ICMP, a <i>type</i> (and optional <i>code</i> may be specified in decimal.</p>
<dt><code>intf show</code></p>
<dd>Display the configuration of all network interfaces.</p>
<dt><code>intf get </code><i>device</i></p>
<dd>Display the configuration for the interface specified by <i>device</i></p>
<dt> <code>intf set</code> <i>device</i> [<code>alias </code><i>host</i> ] [<code>dst </code><i>host</i> ] [<code>inet </code><i>host</i> ] [<code>link </code><i>mac</i> ] [<code>up | down</code> ] [<code>arp | noarp</code> ]</p>
<dd>
<dd>Configure the interface specified by <i>device</i></p>
<dt><code>route show</code></p>
<dd>Display the kernel routing table.</p>
<dt><code>route get </code><i>dst</i></p>
<dd>Display the route for the destination <i>dst</i> specified as a hostname, IP address, or network prefix in CIDR notation.</p>
<dt><code>route add </code><i>dst gw</i></p>
<dd>Add a route for the destination <i>dst</i> through the gateway <i>gw</i></p>
<dt><code>route delete </code><i>dst</i></p>
<dd>Delete the route for the destination <i>dst</i></dl>
<h2>Examples</h2>
<p>Send a UDP datagram containing random shellcode: </p>
<blockquote>
<pre>dnet hex &quot;�^�v1��F�&quot; \
&quot;F���N�V̀&quot; \
&quot;1ۉ�@̀�����/bin/sh&quot; | \
dnet udp sport 555 dport 666 | \
dnet ip proto udp src 1.2.3.4 dst 5.6.7.8 | dnet send</pre>
</blockquote>
<p> Save an ARP request in a file and send it twice: </p>
<blockquote>
<pre>dnet arp op req sha 0:d:e:a:d:0 spa 10.0.0.3 tpa 10.0.0.4 | \
dnet eth type arp src 0:d:e:a:d:0 dst ff:ff:ff:ff:ff:ff &gt; arp.pkt
dnet send fxp0 &lt; arp.pkt
dnet send fxp0 &lt; arp.pkt</pre>
</blockquote>
<p> Send a fragmented ping packet: </p>
<blockquote>
<pre># Create ping packet with IP header, to set ICMP checksum
echo &quot;monkey monkey monkey monkey&quot; | dnet icmp type 8 code 0 | \
dnet ip proto icmp src 1.2.3.4 dst 5.6.7.8 &gt; ping.pkt
# Chop off IP header
dd if=ping.pkt of=ping.data bs=20 skip=1
# Fragment IP payload
split -b 24 ping.data p.
# Send fragments
dnet ip id 1 off 0+ proto icmp src 1.2.3.4 dst 5.6.7.8 &lt; p.aa | \
dnet send
dnet ip id 1 off 24 proto icmp src 1.2.3.4 dst 5.6.7.8 &lt; p.ab | \
dnet send</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-dnet/">dnet</a>(3)</p>
<h2>Authors</h2>
<p>Dug Song Aq dugsong [at] monkey.org</p>
