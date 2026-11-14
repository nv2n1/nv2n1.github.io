---
title: "ip6sic(1)"
name: "ip6sic"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ip6sic/"
description: "ip6sic – flood a node with IPv6 frames in an attempt to cause great havoc"
---

<h2 class="name">NAME</h2>
<p> <code>ip6sic</code> &#8211; flood a node with IPv6 frames in an attempt to cause great havoc </p>
<h2>SYNOPSIS</h2>
<p> <code>ip6sic</code> [<code>-bDhHtv</code>] [<code>-i</code> intf] [<code>-d</code> dst addr] [<code>-s</code> src addr] [<code>-e</code> num hdrs] [<code>-p</code> num pkts] [<code>-r</code> seed] [<code>-w</code> pcap file] [<code>-y</code> max payload] [<code>-f</code> fragment pct] [<code>-T</code> TCP pct] [<code>-U</code> UDP pct] [<code>-I</code> ICMP pct] [<code>-c</code> checksum pct] [<code>-4</code> IPv4 tunnel pct] [<code>-6</code> IPv6 tunnel pct] </p>
<h2>DESCRIPTION</h2>
<p> <code>ip6sic</code> sends IPv6 network traffic according to the options supplied on the command line. It supports tunneling, tcp, udp, and icmp payloads, fragments, and checksumming. </p>
<dl>
<dt><code>-h</code></p>
<dd> Show help information. </p>
<dt><code>-D</code></p>
<dd> Enable debugging. </p>
<dt><code>-v</code></p>
<dd> Show the version. </p>
<dt><code>-b</code></p>
<dd> Don&#8217;t show the progress indicator. </p>
<dt><code>-H</code></p>
<dd> Dump each packet in hex after sending it (useful for debugging). </p>
<dt><code>-t</code></p>
<dd> Dump each packet in the tcpdump-style interpreted format to stdout. (requires libtcpdump) Note: All other text is printed to stderr, which allows one to redirect the tcpdump-style output separately. </p>
<dt><code>-s src addr</code></p>
<dd> Set the source IPv6 address. If a domain name is given, <code>ip6sic</code> will use getaddrinfo to resolve it to an IPv6 address. If no IPv6 address is found, it will create an IPv4-mapped IPv6 address. Random addresses, the default, can be specified with<code>and</code>. </p>
<dt><code>-d dst addr</code></p>
<dd> Set the destination IPv6 address. If a domain name is given, <code>ip6sic</code> will use getaddrinfo to resolve it to an IPv6 address. If no IPv6 address is found, it will create an IPv4-mapped IPv6 address. Random addresses, the default, can be specified with<code>and</code>. </p>
<dt><code>-i intf</code></p>
<dd> Set the outgoing interface. </p>
<dt><code>-p num pkts</code></p>
<dd> Set the number of packets <code>ip6sic</code> will create and send. if this option is not given, or -1 is given, <code>ip6sic</code> will send an infinite amount of packets. </p>
<dt><code>-r seed</code></p>
<dd> Set the randomization seed. This is useful for duplicating runs. </p>
<dt><code>-w pcap file</code></p>
<dd> Save every packet created to <code><br />
 cap file</code> using libpcap. Note that this does not stop <code>ip6sic</code> from writing packets to the wire. </p>
<dt><code>-y max payload</code></p>
<dd> Set the maximum number of bytes in the payload, including the ethernet header. This is useful the the specified interface has a non-standard MTU. </p>
<dt><code>-f percent</code></p>
<dd> Set the percentage of packets which should have an IPv6 fragment header. The value given should be between 0 and 100. If 100 is specified, then all packets created will have an IPv6 fragment header. </p>
<dt><code>-T percent</code></p>
<dd> Set the percentage of packets with a random TCP payload. </p>
<dt><code>-U percent</code></p>
<dd> Set the percentage of packets with a random UDP payload. </p>
<dt><code>-I percent</code></p>
<dd> Set the percentage of packets with a random ICMPv6 payload. Note that this will be an (IPv4) ICMP payload if -4 is specified. </p>
<dt><code>-c percent</code></p>
<dd> Set the percentage of packets which will have a valid TCP, UDP, ICMP, and IP checksum. </p>
<dt><code>-4 percent</code></p>
<dd> Set the percentage of packets to have an IPv4 header following the initial IPv6 header. The IPv6 header&#8217;s &#8216;nxt&#8217; byte will be set to IPPROTO_IPIP (for IP tunneling). Higher layer header options can also be specifed in conjunction with this option. </p>
<dt><code>-6 percent</code></p>
<dd> Set the percentage of packets to have an IPv6 header following the initial IPv6 header. The IPv6 header&#8217;s &#8216;nxt&#8217; byte will be set to IPPROTO_IPV6 (for IPv6 tunneling). Higher layer header options can also be specifed in conjunction with this option. </p>
</dl>
<h2>SEE ALSO</h2>
<p> isic &#8211; the IP Stack Integrity Checker libdnet &#8211; a cross-platform networking library</p>
<h2>AUTHOR</h2>
<p> Greg Taleck, taleck [at] oz.net </p>
<h2>Index</h2>
