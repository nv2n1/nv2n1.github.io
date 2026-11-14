---
title: "dnsreplay(1)"
name: "dnsreplay"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsreplay/"
description: "dnsreplay – A PowerDNS nameserver debugging tool"
---

<h2>NAME</h2>
<p> dnsreplay &#8211; A PowerDNS nameserver debugging tool</p>
<h2>SYNOPSIS</h2>
<p> <code>dnsreplay </code><i>[options]</i> <i>filename</i> <i>ip-address</i> <i>[port]</i></p>
<h2>DESCRIPTION</h2>
<p> This program takes recorded questions and answers and replays them to a specified nameserver and reporting afterwards which percentage of answers matched, were worse or better. </p>
<p> <i>filename</i> is expected to be an PCAP file. The queries are send to the DNS server specified as <i>ip-address</i> and <i>[port]</i>. <i>ip-address</i> is mandatory. If <i>[port]</i> is omitted, 53 will be used. dnsreplay compares the answers and some other metrics with the actual ones with those found in the dumpfile. </p>
<p> By default it only replay queries with recursion-desired flag set.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help | -h</code></p>
<dd>
 Show summary of options.</p>
<dt><code>&#8211;packet-limit </code><i>num</i></p>
<dd>
 Stop after replaying <i>num</i> packets. Default for <i>num</i> is 0, which means no limit.</p>
<dt><code>&#8211;quiet </code><i>flag</i></p>
<dd>
 If <i>flag</i> is set to 1. dnsreplay will not be very noisy with its output. This is the default.</p>
<dt><code>&#8211;recursive </code><i>flag</i></p>
<dd>
 If <i>flag</i> is set to 1. dnsreplay will only replay queries with recursion desired flag set. This is the default.</p>
<dt><code>&#8211;speedup </code><i>factor</i></p>
<dd>
 Replay queries with this speedup factor. Default is 1.</p>
<dt><code>&#8211;timeout-msec </code><i>time</i></p>
<dd>
 Wait at least this many milliseconds for a reply. Default is 500.</dl>
<h2>BUGS</h2>
<p> dnsreplay has no certain handling for timeouts. It handles around at most 65536 outstanding answers.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap/">pcap</a>(3PCAP), <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8), <a href="/docs/linux/man/8-dnswascher/">dnswascher</a>(8)</p>
<h2>AUTHORS</h2>
<p> This manpage was written by Joerg Jungermann (jj+debian At borkum.net) for the Debian Project and the PowerDNS versatile DNS server. </p>
<h2>Index</h2>
