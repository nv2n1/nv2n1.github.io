---
title: "rastrip(1)"
name: "rastrip"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rastrip/"
description: "rastrip – strip argus(8) data file."
---

<h2>NAME</h2>
<p> <code>rastrip</code> &#8211; strip <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file.</p>
<h2>SYNOPSIS</h2>
<p> <code>rastrip</code> [<code>-M</code> [replace] [+|-]<i>dsr</i> [-M &#8230;]] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rastrip</code> reads <code>argus</code> data from an <i>argus-data</i> source, strips the records based on the criteria specified on the command line, and outputs a valid <i>argus-stream</i>. This is useful to reduce the size of argus data files. Rastrip always removes argus management transactions, thus having the same effect as a &#8216;not man&#8217; filter expression.</p>
<h2>OPTIONS</h2>
<p> Rastrip, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-rastrip/">rastrip</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-M [+|-]dsr</code></p>
<dd> Strip specified dsr (data set record). </p>
<p> Supported dsrs are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>flow</code></p>
<dd> flow key data (proto, saddr, sport, dir, daddr, dport)</p>
<dt><code>time</code></p>
<dd> time stamp fields (stime, ltime).</p>
<dt><code>metric</code></p>
<dd> basic ([s|d]bytes, [s|d]pkts, [s|d]rate, [s|d]load)</p>
<dt><code>agr</code></p>
<dd> aggregation stats (trans, avgdur, mindur, maxdur, stdev).</p>
<dt><code>net</code></p>
<dd> network objects (tcp, esp, rtp, icmp data).</p>
<dt><code>vlan</code></p>
<dd> VLAN tag data</p>
<dt><code>mpls</code></p>
<dd> MPLS label data</p>
<dt><code>jitter</code></p>
<dd> Jitter data ([s|d]jit, [s|d]intpkt)</p>
<dt><code>ipattr</code></p>
<dd> IP attributes ([s|d]ipid, [s|d]tos, [s|d]dsb, [s|d]ttl)</p>
<dt><code>suser</code></p>
<dd> src user captured data bytes (suser)</p>
<dt><code>duser</code></p>
<dd> dst captured user data bytes (duser)</p>
<dt><code>mac</code></p>
<dd> MAC addresses (smac, dmac)</p>
<dt><code>icmp</code></p>
<dd> ICMP specific data (icmpmap, inode)</p>
<dt><code>encaps</code></p>
<dd> Flow encapsulation type indications</dl>
</dl>
<p> In the default mode, without the -M option, rastrip removes the following default set of dsrs: encaps, agr, vlan, mpls, mac, icmp, ipattr, jitter, suser, duser </p>
<dl>
<dt><code>-M replace</code></p>
<dd> Replace the existing file with the newly striped file. </p>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-rastrip/">rastrip</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and strips the default dsr set but keeps MAC addresses and writes the result to <code>outputfile</code>: </p>
<p> <code>rastrip -M +mac -r inputfile -w outputfile</code> </p>
<p> This call removes only captured user data and timings and writes the result to stdout: </p>
<p> <code>rastrip -M -suser -M -duser -M -time -r inputfile</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
