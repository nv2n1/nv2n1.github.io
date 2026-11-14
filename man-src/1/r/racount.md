---
title: "racount(1)"
name: "racount"
section: "1"
letter: "r"
url: "/docs/linux/man/1-racount/"
description: "racount – count things from an argus(8) data file/stream."
---

<h2>NAME</h2>
<p> <code>racount</code> &#8211; count things from an <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file/stream.</p>
<h2>SYNOPSIS</h2>
<p> <code>racount</code> <i>[-M addr proto] [</i><code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Racount</code> reads <code>argus</code> data from an <i>argus-file</i> list, and prints out various counts from the data in the file. Racount supports, by default, a single line output that provide total records and pkt and byte counts, broken down by source and destination. </p>
<h2>OPTIONS</h2>
<p> Racount, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. </p>
<p> <code>racount</code> specfic options are: </p>
<dl>
<dt><code>-M</code><i> modes</i></p>
<dd> Supported modes are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>proto</code></p>
<dd> Print a count breakdown on protocols seen. <code>racount</code> will report on IP protocols, ether protocols, arp, rarp and unknowwn. </p>
<dt><code>addr</code></p>
<dd> Print a summary report of the occurence of the various types of network addresses encountered. The current list of IANA standard network address types include:<br />
&nbsp;<wbr>IPv4 Unicast ThisNet, Reserved, LoopBack, LinkLocal, TestNet and Private<br />
&nbsp;<wbr>IPv4 Multicast Local, Internet, AdHoc, Reserved, SdpSap, Nasdaq, DisTrans, SrcSpec, Glop, Admin, OrgLocal and SiteLocal<br />
&nbsp;<wbr>IPv6 Loopback, LinkLocal, SiteLocal, Global, V4Compat, V4Mapped and Unspecified&nbsp;<wbr><br />
&nbsp;<wbr>IPv6 MulticastNodeLocal, MulticastLinkLocal, MulticastSiteLocal, MulticastOrgLocal and MulticastGlobal </p>
</dl>
</dl>
<h2>EXAMPLE INVOCATION</h2>
<p> This example runs <code>racount</code> against a single argus data file, generating the default output. </p>
<pre>
<font SIZE="-4">% racount -r argus.2012.02.13.17.20.00.out.gz
racount   records     total_pkts     src_pkts       dst_pkts       total_bytes        src_bytes          dst_bytes
    sum   336         21319          9266           12053          16954495           1329172            15625323          
</font></pre>
<p> This example runs <code>racount</code> against a directory containing argus data, generating a protocol breakdown as well as generating a network address summary. </p>
<pre>
<font SIZE="-4">% racount -M proto addr -r argus.2012.02.13.17.20.00.out.gz
racount   records     total_pkts     src_pkts       dst_pkts       total_bytes        src_bytes          dst_bytes
    sum   336         21319          9266           12053          16954495           1329172            15625323          
Protocol Summary
    udp   1           28             28             0              14692              14692              0                 
     ip   222         20751          8891           11860          16799531           1238670            15560861          
    udp   103         513            324            189            138274             74068              64206             
    udp   1           1              1              0              422                422                0                 
    arp   7           16             12             4              936                680                256               
Address Summary
  IPv4 Unicast              src 0           dst 40        
  IPv4 Unicast Private      src 6           dst 3         
  IPv6 LinkLocal            src 3           dst 0         
  IPv6 Multicast Link Local src 0           dst 3 
</font></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
<h2>Index</h2>
