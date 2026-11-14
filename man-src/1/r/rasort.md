---
title: "rasort(1)"
name: "rasort"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasort/"
description: "rasort – sort argus(8) data file."
---

<h2>NAME</h2>
<p> <code>rasort</code> &#8211; sort <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasort</code> [[<code>-M</code> <i>sortmode</i>] [<code>-m</code> <i>sort fields</i>] &#8230;] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rasort</code> reads <code>argus</code> data from an <i>argus-data</i> source, sorts the records based on the criteria specified on the command line, and outputs a valid <i>argus-stream</i>.</p>
<h2>OPTIONS</h2>
<p> Rasort, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-rasort/">rasort</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-M replace</code></p>
<dd> Replace the existing file(s) with the sorted output(s). </p>
<dt><code>-m</code><i> field [field &#8230;]</i></p>
<dd> Supported sort fields are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>stime</code></p>
<dd> record start time &lt;default&gt;</p>
<dt><code>ltime</code></p>
<dd> record last time.</p>
<dt><code>trans</code></p>
<dd> aggregation record count.</p>
<dt><code>dur</code></p>
<dd> record total duration.</p>
<dt><code>avgdur</code></p>
<dd> record average duration.</p>
<dt><code>mindur</code></p>
<dd> record minimum duration.</p>
<dt><code>maxdur</code></p>
<dd> record maximum duration.</p>
<dt><code>smac</code></p>
<dd> source MAC addr.</p>
<dt><code>dmac</code></p>
<dd> destination MAC addr.</p>
<dt><code>soui</code></p>
<dd> oui portion of the source MAC addr.</p>
<dt><code>doui</code></p>
<dd> oui portion of the destination MAC addr.</p>
<dt><code>saddr[/cidr]</code></p>
<dd> source IP addr, with optional cidr specification for IPv4 addresses.</p>
<dt><code>daddr[/cidr]</code></p>
<dd> destination IP addr, with optional cidr specification for IPv4 addresses.</p>
<dt><code>proto</code></p>
<dd> transaction protocol.</p>
<dt><code>sport</code></p>
<dd> source port number.</p>
<dt><code>dport</code></p>
<dd> destination port number.</p>
<dt><code>stos</code></p>
<dd> source TOS byte value.</p>
<dt><code>dtos</code></p>
<dd> destination TOS byte value.</p>
<dt><code>sttl</code></p>
<dd> src -&gt; dst TTL value.</p>
<dt><code>dttl</code></p>
<dd> dst -&gt; src TTL value.</p>
<dt><code>bytes</code></p>
<dd> total transaction bytes.</p>
<dt><code>sbytes</code></p>
<dd> src -&gt; dst transaction bytes.</p>
<dt><code>dbytes</code></p>
<dd> dst -&gt; src transaction bytes.</p>
<dt><code>pkts</code></p>
<dd> total transaction packet count.</p>
<dt><code>spkts</code></p>
<dd> src -&gt; dst packet count.</p>
<dt><code>dpkts</code></p>
<dd> dst -&gt; src packet count.</p>
<dt><code>load</code></p>
<dd> bits per second.</p>
<dt><code>sload</code></p>
<dd> source bits per second.</p>
<dt><code>dload</code></p>
<dd> destination bits per second.</p>
<dt><code>loss</code></p>
<dd> pkts retransmitted or dropped.</p>
<dt><code>sloss</code></p>
<dd> source pkts retransmitted or dropped.</p>
<dt><code>dloss</code></p>
<dd> destination pkts retransmitted or dropped.</p>
<dt><code>ploss</code></p>
<dd> percent pkts retransmitted or dropped.</p>
<dt><code>sploss</code></p>
<dd> percent source pkts retransmitted or dropped.</p>
<dt><code>dploss</code></p>
<dd> percent destination pkts retransmitted or dropped.</p>
<dt><code>rate</code></p>
<dd> pkts per second.</p>
<dt><code>srate</code></p>
<dd> source pkts per second.</p>
<dt><code>drate</code></p>
<dd> destination pkts per second.</p>
<dt><code>tranref</code></p>
<dd> argus transaction reference number.</p>
<dt><code>seq</code></p>
<dd> argus sequence number.</p>
<dt><code>smpls</code></p>
<dd> source MPLS identifier.</p>
<dt><code>dmpls</code></p>
<dd> destination MPLS identifier.</p>
<dt><code>svlan</code></p>
<dd> source VLAN identifier.</p>
<dt><code>dvlan</code></p>
<dd> destination VLAN identifier.</p>
<dt><code>srcid</code></p>
<dd> argus source identifier.</p>
<dt><code>stcpb</code></p>
<dd> source TCP base sequence number.</p>
<dt><code>dtcpb</code></p>
<dd> destination TCP base sequence number.</p>
<dt><code>tcprtt</code></p>
<dd> TCP connection setup round-trip time.</p>
<dt><code>smeansz</code></p>
<dd> source mean packet size</p>
<dt><code>dmeansz</code></p>
<dd> destination mean packet size</p>
<dt><code>sco</code></p>
<dd> source country code</p>
<dt><code>dco</code></p>
<dd> destination country code</p>
<dt><code>sas</code></p>
<dd> source autonomous system number</p>
<dt><code>das</code></p>
<dd> destination autonomous system number </p>
</dl>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-rasort/">rasort</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and sorts the IP protocol based <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data, first by the destination IP address, then by the service (destination) port number and then by the source IP address, and writes the results to stdout. For most services, this arranges <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> formatted data by server, service, and then by client.</p>
<dl>
<dt><code>rasort</code> -r inputfile -m daddr dport saddr &#8211; ip</p>
<dd>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
