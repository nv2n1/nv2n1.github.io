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
<dt><code>-c</code> <i>expressionlist</i></p>
<dd> Count occurrences of matching expressions </p>
<dt><code>-f</code> <i>expression</i></p>
<dd> Filter: only process packets that match the expression </p>
<dt><code>-h</code></p>
<dd> Show usage </p>
<dt><code>-p</code></p>
<dd> Show the total number of correct DNS packets, and percentage of -u and -c values (of the total of matching on the -f filter. if no filter is given, percentages are on all correct dns packets) </p>
<dt><code>-of</code> <i>file</i></p>
<dd> Write all packets that match the -f flag to file, as pcap data. </p>
<dt><code>-ofh</code> <i>file</i></p>
<dd> Write all packets that match the -f flag to file, in hexadecimal format, readable by drill. </p>
<dt><code>-s</code></p>
<dd> Show possible match names </p>
<dt><code>-s</code> <i>matchname</i></p>
<dd> show possible match operators and values for name </p>
<dt><code>-sf</code></p>
<dd> Only evaluate packets (in representation format) that match the -f filter. If no -f was given, evaluate all correct dns packets. </p>
<dt><code>-u</code> <i>matchnamelist</i></p>
<dd> Count every occurence of every value of the matchname (for instance, count all packetsizes, see EXAMPLES in <a href="/docs/linux/man/1-ldns-dpa/">ldns-dpa</a>(1) ). </p>
<dt><code>-ua</code></p>
<dd> For every matchname in -u, show the average value of all matches. Behaviour for match types that do not have an integer value is undefined. </p>
<dt><code>-uac</code></p>
<dd> For every matchname in -u, show the average number of times this value was encountered. </p>
<dt><code>-um</code> <i>number</i></p>
<dd> Only show the results from -u for values that occurred more than &lt;number&gt; times. </p>
<dt><code>-v</code> <i>level</i></p>
<dd> Set verbosity to level (1-5, 5 being the highest). Mostly used for debugging. </p>
<dt><code>-notip</code> <i>file</i></p>
<dd> Write packets that were not recognized as IP packets to file (as pcap data). </p>
<dt><code>-baddns</code> <i>file</i></p>
<dd> Write dns packets that were too mangled to parse to file (as pcap data). </p>
<dt><code>-version</code></p>
<dd> Show version and exit </p>
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
<dt>ldns-dpa -u packetsize -p test.tr</p>
<dd> Count all different packetsizes in test.tr and show the precentages. </p>
<dt>ldns-dpa -f &quot;edns=1&amp;qr=0&quot; -of edns.tr test.tr</p>
<dd> Filter out all edns enable queries in test.tr and put them in edns.tr </p>
<dt>ldns-dpa -f edns=1 -c tc=1 -u rcode test.tr</p>
<dd> For all edns packets, count the number of truncated packets and all their rcodes in test.tr. </p>
<dt>ldns-dpa -c tc=1,qr=0,qr=1,opcode=QUERY test.tr</p>
<dd> For all packets, count the number of truncated packets, the number of packets with qr=0, the number of packets with qr=1 and the number of queries in test.tr. </p>
<dt>ldns-dpa -u packetsize -ua test.tr</p>
<dd> Show all packet sizes and the average packet size per packet. </p>
<dt>ldns-dpa -u srcaddress -uac test.tr</p>
<dd> Show all packet source addresses and the average number of packets sent from this address. </p>
<dt>sudo tcpdump -i eth0 -s 0 -U -w &#8211; port 53 | ldns-dpa -f qr=0 -sf</p>
<dd> Print all query packets seen on the specified interface. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Jelte Jansen for NLnetLabs. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;jelte [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
