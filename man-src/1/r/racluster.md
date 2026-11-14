---
title: "racluster(1)"
name: "racluster"
section: "1"
letter: "r"
url: "/docs/linux/man/1-racluster/"
description: "racluster – aggregate argus(8) data files."
---

<h2>NAME</h2>
<p> <code>racluster</code> &#8211; aggregate <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data files.</p>
<h2>SYNOPSIS</h2>
<p> <code>racluster</code> [<code>-f</code> <i>conf</i>] [<code>-m</code> <i>agr(s)</i>] [<code>-M</code> <i>mode(s)</i>] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Racluster</code> reads <code>argus</code> data from an <i>argus-data</i> source, and clusters/merges the records based on the flow key criteria specified either on the command line, or in a racluster configuration file, and outputs a valid <i>argus-stream</i>. This tool is primarily used for data mining, data management and report generation. </p>
<p> The default action is to merge status records from the same flow and argus probe, providing in some cases huge data reduction with limited loss of flow information. Racluster provides the ability to modify the flow model key, either using the &quot;-m&quot; option, or in the racluster.conf file, allowing records to be clustered based on any number of attributes. This supports the development of important reports, such as MPLS LSP usage statistics, DiffServe flow marking policy verification, VLAN group behavior, IP distance related measurements, routing loop detection, traceroute path data recovery, and complex availability/reachability reports, to name just a few useful applications. </p>
<p> Please see racluster.5 for detailed information regarding racluster configuration. </p>
<h2>OPTIONS</h2>
<p> Racluster, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression, and the ability to specify the output style, format and contents for printing data. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-racluster/">racluster</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-m</code><i> aggregation object</i></p>
<dd> Supported aggregation objects are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> use a null flow key.</p>
<dt><code>srcid</code></p>
<dd> argus source identifier.</p>
<dt><code>smac</code></p>
<dd> source mac(ether) addr.</p>
<dt><code>dmac</code></p>
<dd> destination mac(ether) addr.</p>
<dt><code>soui</code></p>
<dd> oui portion of the source mac(ether) addr.</p>
<dt><code>doui</code></p>
<dd> oui portion of the destination mac(ether) addr.</p>
<dt><code>smpls</code></p>
<dd> source mpls label.</p>
<dt><code>dmpls</code></p>
<dd> destination label addr.</p>
<dt><code>svlan</code></p>
<dd> source vlan label.</p>
<dt><code>dvlan</code></p>
<dd> destination vlan addr.</p>
<dt><code>saddr/[l|m]</code></p>
<dd> source IP addr/[cidr len | m.a.s.k].</p>
<dt><code>daddr/[l|m]</code></p>
<dd> destination IP addr/[cidr len | m.a.s.k].</p>
<dt><code>matrix/l</code></p>
<dd> sorted src and dst IP addr/cidr len.</p>
<dt><code>proto</code></p>
<dd> transaction protocol.</p>
<dt><code>sport</code></p>
<dd> source port number. Implies use of &#8216;proto&#8217;.</p>
<dt><code>dport</code></p>
<dd> destination port number. Implies use of &#8216;proto&#8217;.</p>
<dt><code>stos</code></p>
<dd> source TOS byte value.</p>
<dt><code>dtos</code></p>
<dd> destination TOS byte value.</p>
<dt><code>sttl</code></p>
<dd> src -&gt; dst TTL value.</p>
<dt><code>dttl</code></p>
<dd> dst -&gt; src TTL value.</p>
<dt><code>stcpb</code></p>
<dd> src -&gt; dst TCP base sequence number.</p>
<dt><code>dtcpb</code></p>
<dd> dst -&gt; src TCP base sequence number.</p>
<dt><code>inode[/l|m]]</code></p>
<dd> intermediate node IP addr/[cidr len | m.a.s.k], source of ICMP mapped events.</p>
<dt><code>sco</code></p>
<dd> source ARIN country code, if present.</p>
<dt><code>dco</code></p>
<dd> destination ARIN country code, if present.</p>
<dt><code>sas</code></p>
<dd> source node origin AS number, if available.</p>
<dt><code>das</code></p>
<dd> destination node origin AS number, if available.</p>
<dt><code>ias</code></p>
<dd> intermediate node origin AS number, if available. </p>
<dt></dl>
</dl>
<dd>
<dl>
<dt><code>-M</code><i> modes</i></p>
<dd> Supported modes are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>correct</code></p>
<dd> Attempt to correct the direction of flows by also searching the reverse flow key, if a match isn&#8217;t found in the cache. This mode is on by default when using the default full 5-tuple flow key definitions.</p>
<dt><code>nocorrect</code></p>
<dd> Turn off flow correction for direction. This mode is used by default if the flow key has been changed.</p>
<dt><code>norep</code></p>
<dd> Do not generate an aggregate statistic for each flow. This is used primarily when the output represents a single object. Primarily used when merging status records to generate single flows that represent single transactions.</p>
<dt><code>rmon</code></p>
<dd> Generate data suitable for producing RMON types of metrics.</p>
<dt><code>ind</code></p>
<dd> Process each input file independantly, so that after the end of each inputfile, racluster flushes its output.</p>
<dt><code>replace</code></p>
<dd> Replace each inputfile contents, with the aggregated output. The initial file compression status is maintained</dl>
</dl>
<dl>
<dt><code>-V</code></p>
<dd> Verbose operation, printing a line of output for each input file processed. Very useful when using the ra() -R option. </p>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-racluster/">racluster</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and aggregates the TCP protocol based <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data. By default, <code><a href="/docs/linux/man/1-racluster/">racluster</a>(1)</code> merges using the standard 5-tuple flow key. This method is used to merge multiple status records into a single flow record per transaction. </p>
<pre><code>
% ra - r argus.tcp .2012.02.13.12.20.00 StartTime Dur Trans Flgs Proto SrcAddr Sport Dir DstAddr Dport TotPkts State 12 : 23 : 07.268 0.997 1 e i tcp 192.168.0.68.59016-&gt;208.59.201.75.http 298 CON 12 : 23 : 08.294 1.000 1 e tcp 192.168.0.68.59016-&gt;208.59.201.75.http 111 CON 12 : 23 : 09.294 0.991 1 e d tcp 192.168.0.68.59016-&gt;208.59.201.75.http 637 CON 12 : 23 : 10.331 0.330 1 e tcp 192.168.0.68.59016-&gt;208.59.201.75.http 89 CON 12 : 23 : 32.183 0.010 1 e tcp 192.168.0.68.59016-&gt;208.59.201.75.http 3 FIN % racluster - r argus.tcp .2012.02.13.12.20.00 StartTime Dur Trans Flgs Proto SrcAddr Sport Dir DstAddr Dport TotPkts State 12 : 23 : 07.268 24.925 5 e d tcp 192.168.0.68.59016-&gt;208.59.201.75.http 1138 FIN
</code></pre>
<p> A sample invocation of <code><a href="/docs/linux/man/1-racluster/">racluster</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and aggregates the TCP protocol based <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data, based on the source and destination address matrix and the protocol. It reports the metrics as a percent of the total. </p>
<pre><code>

% racluster - r argus .2012.02.13.17.20.00 - m saddr / 16 daddr proto - %
                                                                            -s stime dur trans proto saddr dir daddr pkts state -
    tcp and port https
            StartTime Dur pTrans Proto SrcAddr Dir DstAddr pTotPkts State 17 : 49 : 54.225 8.101 33.333 tcp 192.168.0.0 /
        16-&gt;17.154.66.18 23.372 FIN 17 : 48 : 42.607 179.761 13.333 tcp 192.168.0.0 / 16-&gt;17.172.224.25 31.052 FIN 17 : 50 : 01.113 0.803 6.667 tcp 192.168.0.0 / 16-&gt;17.250.248.161 5.676 FIN 17 : 49 : 54.525 1.153 6.667 tcp 192.168.0.0 / 16-&gt;64.12.173.137 5.509 FIN 17 : 50 : 35.411 101.133 26.667 tcp 192.168.0.0 / 16-&gt;184.28.150.87 19.199 RST 17 : 49 : 56.061 73.415 6.667 tcp 192.168.0.0 / 16-&gt;205.188.8.47 11.018 RST 17 : 49 : 55.677 0.434 6.667 tcp 192.168.0.0 / 16-&gt;205.188.101.10 4.174 FIN
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-racluster/">racluster</a>(5),</code> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
