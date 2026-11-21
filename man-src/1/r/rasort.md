---

title: "rasort(1)"
name: "rasort"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasort/"
description: "rasort – sort argus(8) data file."
---

<p> <code>rasort</code> &#8211; sort <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file.</p>
<h2>SYNOPSIS</h2>
<p> <code>rasort</code> [[<code>-M</code> <i>sortmode</i>] [<code>-m</code> <i>sort fields</i>] &#8230;] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rasort</code> reads <code>argus</code> data from an <i>argus-data</i> source, sorts the records based on the criteria specified on the command line, and outputs a valid <i>argus-stream</i>.</p>
<h2>OPTIONS</h2>
<p> Rasort, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-rasort/">rasort</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-M replace</code></dt>
<dd> Replace the existing file(s) with the sorted output(s). </dd>
<dt><code>-m</code><i> field [field &#8230;]</i></dt>
<dd> Supported sort fields are:</dd></dl>
<dl>
<dl>
<dt><code>stime</code></dt>
<dd> record start time &lt;default&gt;</dd>
<dt><code>ltime</code></dt>
<dd> record last time.</dd>
<dt><code>trans</code></dt>
<dd> aggregation record count.</dd>
<dt><code>dur</code></dt>
<dd> record total duration.</dd>
<dt><code>avgdur</code></dt>
<dd> record average duration.</dd>
<dt><code>mindur</code></dt>
<dd> record minimum duration.</dd>
<dt><code>maxdur</code></dt>
<dd> record maximum duration.</dd>
<dt><code>smac</code></dt>
<dd> source MAC addr.</dd>
<dt><code>dmac</code></dt>
<dd> destination MAC addr.</dd>
<dt><code>soui</code></dt>
<dd> oui portion of the source MAC addr.</dd>
<dt><code>doui</code></dt>
<dd> oui portion of the destination MAC addr.</dd>
<dt><code>saddr[/cidr]</code></dt>
<dd> source IP addr, with optional cidr specification for IPv4 addresses.</dd>
<dt><code>daddr[/cidr]</code></dt>
<dd> destination IP addr, with optional cidr specification for IPv4 addresses.</dd>
<dt><code>proto</code></dt>
<dd> transaction protocol.</dd>
<dt><code>sport</code></dt>
<dd> source port number.</dd>
<dt><code>dport</code></dt>
<dd> destination port number.</dd>
<dt><code>stos</code></dt>
<dd> source TOS byte value.</dd>
<dt><code>dtos</code></dt>
<dd> destination TOS byte value.</dd>
<dt><code>sttl</code></dt>
<dd> src -&gt; dst TTL value.</dd>
<dt><code>dttl</code></dt>
<dd> dst -&gt; src TTL value.</dd>
<dt><code>bytes</code></dt>
<dd> total transaction bytes.</dd>
<dt><code>sbytes</code></dt>
<dd> src -&gt; dst transaction bytes.</dd>
<dt><code>dbytes</code></dt>
<dd> dst -&gt; src transaction bytes.</dd>
<dt><code>pkts</code></dt>
<dd> total transaction packet count.</dd>
<dt><code>spkts</code></dt>
<dd> src -&gt; dst packet count.</dd>
<dt><code>dpkts</code></dt>
<dd> dst -&gt; src packet count.</dd>
<dt><code>load</code></dt>
<dd> bits per second.</dd>
<dt><code>sload</code></dt>
<dd> source bits per second.</dd>
<dt><code>dload</code></dt>
<dd> destination bits per second.</dd>
<dt><code>loss</code></dt>
<dd> pkts retransmitted or dropped.</dd>
<dt><code>sloss</code></dt>
<dd> source pkts retransmitted or dropped.</dd>
<dt><code>dloss</code></dt>
<dd> destination pkts retransmitted or dropped.</dd>
<dt><code>ploss</code></dt>
<dd> percent pkts retransmitted or dropped.</dd>
<dt><code>sploss</code></dt>
<dd> percent source pkts retransmitted or dropped.</dd>
<dt><code>dploss</code></dt>
<dd> percent destination pkts retransmitted or dropped.</dd>
<dt><code>rate</code></dt>
<dd> pkts per second.</dd>
<dt><code>srate</code></dt>
<dd> source pkts per second.</dd>
<dt><code>drate</code></dt>
<dd> destination pkts per second.</dd>
<dt><code>tranref</code></dt>
<dd> argus transaction reference number.</dd>
<dt><code>seq</code></dt>
<dd> argus sequence number.</dd>
<dt><code>smpls</code></dt>
<dd> source MPLS identifier.</dd>
<dt><code>dmpls</code></dt>
<dd> destination MPLS identifier.</dd>
<dt><code>svlan</code></dt>
<dd> source VLAN identifier.</dd>
<dt><code>dvlan</code></dt>
<dd> destination VLAN identifier.</dd>
<dt><code>srcid</code></dt>
<dd> argus source identifier.</dd>
<dt><code>stcpb</code></dt>
<dd> source TCP base sequence number.</dd>
<dt><code>dtcpb</code></dt>
<dd> destination TCP base sequence number.</dd>
<dt><code>tcprtt</code></dt>
<dd> TCP connection setup round-trip time.</dd>
<dt><code>smeansz</code></dt>
<dd> source mean packet size</dd>
<dt><code>dmeansz</code></dt>
<dd> destination mean packet size</dd>
<dt><code>sco</code></dt>
<dd> source country code</dd>
<dt><code>dco</code></dt>
<dd> destination country code</dd>
<dt><code>sas</code></dt>
<dd> source autonomous system number</dd>
<dt><code>das</code></dt>
<dd> destination autonomous system number </dd>
</dl>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-rasort/">rasort</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and sorts the IP protocol based <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data, first by the destination IP address, then by the service (destination) port number and then by the source IP address, and writes the results to stdout. For most services, this arranges <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> formatted data by server, service, and then by client.</p>
<dl>
<dt><code>rasort</code> -r inputfile -m daddr dport saddr &#8211; ip</dt>
<dd>
</dd></dl>
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
