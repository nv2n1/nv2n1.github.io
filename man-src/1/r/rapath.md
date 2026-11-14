---
title: "rapath(1)"
name: "rapath"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rapath/"
description: "rapath – print traceroute path information from argus(8) data."
---

<h2>NAME</h2>
<p> <code>rapath</code> &#8211; print traceroute path information from <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>rapath</code> [<code>-A</code>] [<code>-M [ aspath [dist] | asnode ] </code>] [<code>-m fields </code>] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rapath</code> reads <code>argus</code> data from an <i>argus-data</i> source, and generates the path information that can be formulated from flows that experience ICMP responses. When a packet cause the creation of an ICMP response, for whatever reason, the intermediate node that generates the ICMP packet is, by definition, on the path. Argus data perserves this intermediate node address, and <code>rapath</code> uses this information to generate path information, for arbitrary IP network traffic. <code>Rapath</code> is principally designed to recover traceroute.1 traffic, so that if a trace is done in the network, argus will pick it up and record the intermediate nodes and the RTT for the volleys. However the method is generalized such that it also picks up routing loop conditions, when they exist in the observed packet stream. </p>
<p> <code>Rapath</code> will generate argus flow records that have the src address, dst address and src ttl of the transmitted packet, aggregated so that the average duration, standard deviation, max and min rtt&#8217;s are preserved. The most accurate estimate of the actual Round-Trip Time (RTT) between a src IP address and an ICMP based intermediate node is the MinDur field. As the number of samples gets larger, the MinDur field approaches the theoretical best case minimum RTT. RTT&#8217;s above this value, will include variations in network and device delay. </p>
<p> When using the optional racluster.1 style flow descriptors, path information to and from CIDR based network addresses can be calculated, so that traces from and to multiple machines in the subnets can be grouped together. </p>
<p> The output of rapath can be piped into ranonymize.1, in order to share path performance information without divulging the actual addresses of intermidate routers. </p>
<h2>RAPATH SPECIFIC OPTIONS</h2>
<p> Rapath, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-A</code></p>
<dd> Draw a description of the path with a legend.</p>
<dt><code>-M</code><i> pathmodes</i></p>
<dd> Supported pathmodes are: </p>
<pre>
   <code>        node</code> - print a series of nodes that represent the path (default).
   <code>        addr</code> - print the IP addresses, instead of node labels.
  <code>aspath [dist] -</code> print the series of origin AS's along the path. Optional 'dist' adds the ttl range.
   <code>      asnode</code> - print the series of nodes, preceded with their AS's along the path.
</pre>
<dt><code>-m</code><i> fields</i></p>
<dd> Specify modifications to the default flow identifiers. Supported fields are: </p>
<pre><code>
srcid - the observation domain source identifier.saddr[/ len] - the source address, optionally as a CIDR address.daddr[/ len] - the destination address, optionally as a CIDR address.
</code></pre>
</dl>
<h2>INVOCATION</h2>
<p> A sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code>. This call reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and generates any path information, based on src and dst IP addresses, and writes the results to stdout. </p>
<p>% rapath &#8211; r inputfile<br />
               SrcId SrcAddr Dir DstAddr Inode sTtl Mean StdDev Max Min Trans 192.168.0.68 192.168.0.68-&gt;128.2.42.10 192.168.0.1 1 0.000686 0.000037 0.000764 0.000627 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 10.22.96.1 2 0.009329 0.002719 0.019935 0.007435 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 208.59.246.2 3 0.010686 0.002619 0.020175 0.007698 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 207.172.15.85 4 0.013988 0.007116 0.032652 0.008923 11 192.168.0.68 192.168.0.68-&gt;128.2.42.10 207.172.15.67 4 0.010188 0.000218 0.010676 0.009932 7 192.168.0.68 192.168.0.68-&gt;128.2.42.10 198.32.118.161 5 0.010865 0.003557 0.019436 0.007937 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 64.57.20.251 6 0.044649 0.008916 0.076137 0.039844 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 64.57.21.146 7 0.056345 0.003985 0.065643 0.053371 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 147.73.16.120 8 0.052594 0.003037 0.061770 0.050151 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.249 9 0.055147 0.002541 0.064620 0.053151 18 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.212 10 0.051835 0.000326 0.052362 0.051392 9 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.205 10 0.054236 0.000658 0.055198 0.053028 9<br />
 The output of rapath is an argus data stream, and can be written to a file, or piped to other programs for processing. The resulting stream is a clustered data stream ordered by the unique &quot; saddr -&gt; daddr &quot; paths. </p>
<p> The next sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out a graph of the path information using letters as index, with the node information provided as reference. </p>
<p>% rapath &#8211; Ar inputfile 192.168.0.68(192.168.0.68 ::128.2.42.10)A-&gt;B-&gt;C-&gt;<br />
{<br />
    D, E<br />
} -&gt; F-&gt;G-&gt;H-&gt;I-&gt;J-&gt;{K, L} Node SrcId SrcAddr Dir DstAddr Inode sTtl Mean StdDev Max Min Trans<br />
    A 192.168.0.68 192.168.0.68-&gt;128.2.42.10 192.168.0.1 1 0.000686 0.000037 0.000764 0.000627 18 B 192.168.0.68 192.168.0.68-&gt;128.2.42.10 10.22.96.1 2 0.009329 0.002719 0.019935 0.007435 18 C 192.168.0.68 192.168.0.68-&gt;128.2.42.10 208.59.246.2 3 0.010686 0.002619 0.020175 0.007698 18 D 192.168.0.68 192.168.0.68-&gt;128.2.42.10 207.172.15.85 4 0.013988 0.007116 0.032652 0.008923 11 E 192.168.0.68 192.168.0.68-&gt;128.2.42.10 207.172.15.67 4 0.010188 0.000218 0.010676 0.009932 7 F 192.168.0.68 192.168.0.68-&gt;128.2.42.10 198.32.118.161 5 0.010865 0.003557 0.019436 0.007937 18 G 192.168.0.68 192.168.0.68-&gt;128.2.42.10 64.57.20.251 6 0.044649 0.008916 0.076137 0.039844 18 H 192.168.0.68 192.168.0.68-&gt;128.2.42.10 64.57.21.146 7 0.056345 0.003985 0.065643 0.053371 18 I 192.168.0.68 192.168.0.68-&gt;128.2.42.10 147.73.16.120 8 0.052594 0.003037 0.061770 0.050151 18 J 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.249 9 0.055147 0.002541 0.064620 0.053151 18 K 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.212 10 0.051835 0.000326 0.052362 0.051392 9 L 192.168.0.68 192.168.0.68-&gt;128.2.42.10 128.2.255.205 10 0.054236 0.000658 0.055198 0.053028 9</p>
<p> the path. Because network paths can be divergent, due to routing changes, load balancing, or redirects, multiple nodes can be observed at the same distance along the path. <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> uses &#8216;{&#8216; and &#8216;}&#8217; to delimit the set of nodes that are observed at the same distance in the path. Letters in the path are references to inode addresses contained in the actual node records. </p>
<p> The next sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out just a graph of the path information in two sets of argus data; today&#8217;s and last month, to highlight how paths change. ASN information is added to the records, to show how <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> depicts ASN relationships, using a <code>-f <a href="/docs/linux/man/5-ralabel-conf/">ralabel.conf</a>(5)</code> option. </p>
<p> The -q option suppresses the default output of the actual argus record data compiled for each node along the path. The &#8216;[&#8216; and &#8216;]&#8217; (brackets) deliniate AS&#8217;s and will contain the set of nodes that were observed within the same AS. </p>
<p>% rapath &#8211; f ralabel.conf &#8211; qA &#8211; r inputfile 192.168.0.68(192.168.0.68 ::128.2.42.10)A-&gt;[B] -&gt; [C-&gt;{D, E}] -&gt; [F] -&gt; [G-&gt;H] -&gt; [I] -&gt; [J-&gt;{K, L}] % rapath &#8211; f ralabel.conf &#8211; qA &#8211; r inputfile.last.month 192.168.0.68(192.168.0.68 ::128.2.42.10)A-&gt;[B] -&gt; [C-&gt;D] -&gt; [E-&gt;F-&gt;G-&gt;{ H, I, J, K } -&gt; { L, M, N } -&gt; O-&gt;P] -&gt; [Q-&gt;{R, S}]</p>
<p> This next sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out a graph of the ASpath, the set of AS&#8217;s that the network path traversed. The -q option, again is used to suppress the output of the actual node information. Where there is no AS number, possibly due to a private network or an unregistered address space, letters are used to denote the node. </p>
<p>% rapath &#8211; f ralabel.conf &#8211; r inputfile &#8211; qA &#8211; M aspath 192.168.0.68(192.168.0.68 ::128.2.42.10)A-&gt;AS30496-&gt;AS6079-&gt;AS1257-&gt;AS11164-&gt;AS5050-&gt;AS9</p>
<p> This sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out a graph of the ASpath, suppressing the output of the actual node information (-q), and printing actual IP addresses, rather than node labels. </p>
<p>% rapath &#8211; f ralabel.conf &#8211; r inputfile &#8211; qA &#8211; M aspath addr 192.168.0.68(192.168.0.68 ::128.2.42.10)192.168.0.1-&gt;AS30496-&gt;AS6079-&gt;AS1257-&gt;AS11164-&gt;AS5050-&gt;AS9</p>
<p> This sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out a graph of the ASpath, with distance information, suppressing the output of the actual node information (-q). This is the aspath output, but with distances in TTL&#8217;s for each entry specified. </p>
<p>% rapath &#8211; f ralabel.conf &#8211; r inputfile &#8211; qA &#8211; M aspath dist addr 192.168.0.68(192.168.0.68 ::128.2.42.10)192.168.0.1 : 1-&gt;AS30496 : 2-&gt;AS6079 : 3 &#8211; 4-&gt;AS1257 : 5-&gt;AS11164 : 6 &#8211; 7-&gt;AS5050 : 8-&gt;AS9 : 9 &#8211; 10</p>
<p> This sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> prints out a graph of the AS nodal path, suppressing the output of the actual node information (-q). </p>
<p>% rapath &#8211; f ralabel.conf &#8211; r inputfile &#8211; qA &#8211; M asnode 192.168.0.68(192.168.0.68 ::128.2.42.10)AS30496 : [A-&gt;B]-&gt;AS6079 : [C-&gt;{D, E}]-&gt;AS1257 : [F] -&gt; AS11164 : [G-&gt;H]-&gt;AS5050 : [I] -&gt; AS9 : [J-&gt;{K, L}] % rapath &#8211; f ralabel.conf &#8211; r inputfile.last.month &#8211; qA &#8211; M asnode 192.168.0.68(192.168.0.68 ::128.2.42.10)A-&gt;AS30496 : [B] -&gt; AS6079 : [C-&gt;D]-&gt;AS3356 : [E-&gt;F-&gt;G-&gt;{ H, I, J, K } -&gt; { L, M, N } -&gt; O-&gt;P]-&gt;AS9 : [Q-&gt;{R, S}]</p>
<p> This sample invocation of <code><a href="/docs/linux/man/1-rapath/">rapath</a>(1)</code> demonstrates how to use CIDR address aggregation, using the -m option, to generate path performance data from a class B subnet, to a class C subnet. </p>
<pre><code>

% rapath - f ralabel.conf - r inputfile - A - m saddr / 16 daddr / 24 - srcid 192.168.0.68 192.168.0.68(192.168.0.0 / 16 ::128.2.42.0 / 24) A-&gt;[B] -&gt; [C-&gt;{D, E}] -&gt; [F] -&gt; [G-&gt;H] -&gt; [I] -&gt; [J-&gt;{K, L}] Node SrcId SrcAddr Dir DstAddr Inode sTtl Mean StdDev Max Min Trans
                                                                                                                                                                                                 A 192.168.0.68 192.168.0.0 /
                                                                                                                                                                                                 16 -&gt; 128.2.42.0 / 24 192.168.0.1 1 0.000686 0.000037 0.000764 0.000627 18 B 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 10.22.96.1 2 0.009329 0.002719 0.019935 0.007435 18 C 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 208.59.246.2 3 0.010686 0.002619 0.020175 0.007698 18 D 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 207.172.15.85 4 0.013988 0.007116 0.032652 0.008923 11 E 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 207.172.15.67 4 0.010188 0.000218 0.010676 0.009932 7 F 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 198.32.118.161 5 0.010865 0.003557 0.019436 0.007937 18 G 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 64.57.20.251 6 0.044649 0.008916 0.076137 0.039844 18 H 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 64.57.21.146 7 0.056345 0.003985 0.065643 0.053371 18 I 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 147.73.16.120 8 0.052594 0.003037 0.061770 0.050151 18 J 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 128.2.255.249 9 0.055147 0.002541 0.064620 0.053151 18 K 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 128.2.255.212 10 0.051835 0.000326 0.052362 0.051392 9 L 192.168.0.68 192.168.0.0 / 16 -&gt; 128.2.42.0 / 24 128.2.255.205 10 0.054236 0.000658 0.055198 0.053028 9
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/5-ralabel-conf/">ralabel.conf</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
