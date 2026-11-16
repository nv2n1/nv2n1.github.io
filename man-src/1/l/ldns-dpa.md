---
title: "ldns-dpa(1)"
name: "ldns-dpa"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-dpa/"
description: "dpa – DNS Packet Analyzer. Analyze DNS packets in ip trace files"
---

<h2>NAME</h2>
<p> dpa &#8211; DNS Packet Analyzer. Analyze DNS packets in ip trace files</p>
<h2>SYNOPSIS</h2>
<p> <code>dpa</code> [ <i>OPTION</i> ] <i>TRACEFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>dpa</code> is used to analyze dns packets in trace files. It has 3 main options: count, filter, and count uniques (i.e. count all different occurences). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>expressionlist</i></dt>
<dd> Count occurrences of matching expressions </dd>
<dt><code>-f</code> <i>expression</i></dt>
<dd> Filter: only process packets that match the expression </dd>
<dt><code>-h</code></dt>
<dd> Show usage </dd>
<dt><code>-p</code></dt>
<dd> Show the total number of correct DNS packets, and percentage of -u and -c values (of the total of matching on the -f filter. if no filter is given, percentages are on all correct dns packets) </dd>
<dt><code>-of</code> <i>file</i></dt>
<dd> Write all packets that match the -f flag to file, as pcap data. </dd>
<dt><code>-ofh</code> <i>file</i></dt>
<dd> Write all packets that match the -f flag to file, in hexadecimal format, readable by drill. </dd>
<dt><code>-s</code></dt>
<dd> Show possible match names </dd>
<dt><code>-s</code> <i>matchname</i></dt>
<dd> show possible match operators and values for name </dd>
<dt><code>-sf</code></dt>
<dd> Only evaluate packets (in representation format) that match the -f filter. If no -f was given, evaluate all correct dns packets. </dd>
<dt><code>-u</code> <i>matchnamelist</i></dt>
<dd> Count every occurence of every value of the matchname (for instance, count all packetsizes, see EXAMPLES in <a href="/docs/linux/man/1-ldns-dpa/">ldns-dpa</a>(1) ). </dd>
<dt><code>-ua</code></dt>
<dd> For every matchname in -u, show the average value of all matches. Behaviour for match types that do not have an integer value is undefined. </dd>
<dt><code>-uac</code></dt>
<dd> For every matchname in -u, show the average number of times this value was encountered. </dd>
<dt><code>-um</code> <i>number</i></dt>
<dd> Only show the results from -u for values that occurred more than &lt;number&gt; times. </dd>
<dt><code>-v</code> <i>level</i></dt>
<dd> Set verbosity to level (1-5, 5 being the highest). Mostly used for debugging. </dd>
<dt><code>-notip</code> <i>file</i></dt>
<dd> Write packets that were not recognized as IP packets to file (as pcap data). </dd>
<dt><code>-baddns</code> <i>file</i></dt>
<dd> Write dns packets that were too mangled to parse to file (as pcap data). </dd>
<dt><code>-version</code></dt>
<dd> Show version and exit </dd>
</dl>
<h2>LIST AND MATCHES</h2>
<p> A &lt;matchnamelist&gt; is a comma separated list of match names (use -s to see possible match names). A &lt;expressionlist&gt; is a comma separated list of expressions. </p>
<p> An expression has the following form: &lt;expr&gt;: (&lt;expr&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;expr&gt;&nbsp;<wbr>|&nbsp;<wbr>&lt;expr&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;expr&gt;&nbsp;<wbr>&amp;&nbsp;<wbr>&lt;expr&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;match&gt; </p>
<p> &lt;match&gt;: &lt;matchname&gt; &lt;operator&gt; &lt;value&gt; </p>
<p> &lt;operator&gt;: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>equal to &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>!=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>not equal to &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&gt;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>greater than &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>lesser than &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&gt;=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>greater than or equal to &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>lesser than or equal to &lt;value&gt;<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>~=<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>contains &lt;value&gt;</p>
<p> See the -s option for possible matchnames, operators and values. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>ldns-dpa -u packetsize -p test.tr</dt>
<dd> Count all different packetsizes in test.tr and show the precentages. </dd>
<dt>ldns-dpa -f &quot;edns=1&amp;qr=0&quot; -of edns.tr test.tr</dt>
<dd> Filter out all edns enable queries in test.tr and put them in edns.tr </dd>
<dt>ldns-dpa -f edns=1 -c tc=1 -u rcode test.tr</dt>
<dd> For all edns packets, count the number of truncated packets and all their rcodes in test.tr. </dd>
<dt>ldns-dpa -c tc=1,qr=0,qr=1,opcode=QUERY test.tr</dt>
<dd> For all packets, count the number of truncated packets, the number of packets with qr=0, the number of packets with qr=1 and the number of queries in test.tr. </dd>
<dt>ldns-dpa -u packetsize -ua test.tr</dt>
<dd> Show all packet sizes and the average packet size per packet. </dd>
<dt>ldns-dpa -u srcaddress -uac test.tr</dt>
<dd> Show all packet source addresses and the average number of packets sent from this address. </dd>
<dt>sudo tcpdump -i eth0 -s 0 -U -w &#8211; port 53 | ldns-dpa -f qr=0 -sf</dt>
<dd> Print all query packets seen on the specified interface. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by Jelte Jansen for NLnetLabs. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;jelte [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
