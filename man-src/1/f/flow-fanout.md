---
title: "flow-fanout(1)"
name: "flow-fanout"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-fanout/"
description: "flow-fanout – Fanout (replicate) flow exports to many destinations."
---

<h2>NAME</h2>
<p> flow-fanout &#8211; Fanout (replicate) flow exports to many destinations.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-fanout</code> [ <code>-h</code> ] [ <code>-A</code><i> AS0_substitution</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> filter_fname</i> ] [ <code>-F</code><i> filter_definition</i> ] [ <code>-m</code><i> privacy_mask</i> ] [ <code>-p</code><i> pidfile</i> ] [ <code>-s</code> ] [ <code>-S</code><i> stat_interval</i> ] [ <code>-V</code><i> pdu_version</i> ] [ <code>-x</code><i> xmit_delay</i> ] <i>localip/remoteip/port</i> <i>localip/remoteip/port</i><i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-fanout</code> utility will replicate flows arriving on localip/remoteip/port to destination(s) specified by localip/remoteip/port. </p>
<p> Flows processed by multiple exporters will be mixed into a single output stream. This functionality appeared to support Cisco Catalyst exports and may have other uses. </p>
<p> A SIGQUIT or SIGTERM signal will cause <code>flow-fanout</code> to exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code><i> AS0_substitution</i></p>
<dd> Cisco&#8217;s NetFlow exports represent the local autonomous system as 0 instead of the real value. This option can be used to replace the 0 in the export with the a configured value. Unfortunately under certain configurations AS 0 can also represent a cache miss or non forwarded traffic so use with caution.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> filter_fname</i></p>
<dd> Filter list filename. Defaults to <i>/etc/flow-tools/cfg/filter</i>.</p>
<dt><code>-F</code><i> filter_definition</i></p>
<dd> Select the active definition. Defaults to default.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-m</code><i> privacy_mask</i></p>
<dd> Apply <i>privacy_mask</i> to the source and destination IP address of flows. For example a privacy_mask of 255.255.255.0 would convert flows with source/destination IP addresses 10.1.1.1 and 10.2.2.2 to 10.1.1.0 and 10.2.2.0 respectively.</p>
<dt><code>-p</code><i> pidfile</i></p>
<dd> Configure the process ID file. Use &#8211; to disable pid file creation.</p>
<dt><code>-s</code></p>
<dd> Spoof the source IP address. If the IP address is 0 then it is replaced with the exporter source IP.</p>
<dt><code>-S</code><i> stat_interval</i></p>
<dd> When configured <code>flow-fanout</code> will emit a timestamped message on stderr every <i>stat_interval</i> minutes indicating counters such as the number of flows received, packets processed, and lost flows.</p>
<dt><code>-V</code><i> pdu_version</i></p>
<dd> Use <i>pdu_version</i> format output. </p>
<pre>
    1    NetFlow version 1 (No sequence numbers, AS, or mask)
    5    NetFlow version 5
    6    NetFlow version 6 (5+ Encapsulation size)
    7    NetFlow version 7 (Catalyst switches)
    8.1  NetFlow AS Aggregation
    8.2  NetFlow Proto Port Aggregation
    8.3  NetFlow Source Prefix Aggregation
    8.4  NetFlow Destination Prefix Aggregation
    8.5  NetFlow Prefix Aggregation
    8.6  NetFlow Destination (Catalyst switches)
    8.7  NetFlow Source Destination (Catalyst switches)
    8.8  NetFlow Full Flow (Catalyst switches)
    8.9  NetFlow ToS AS Aggregation
    8.10 NetFlow ToS Proto Port Aggregation
    8.11 NetFlow ToS Source Prefix Aggregation
    8.12 NetFlow ToS Destination Prefix Aggregation
    8.13 NetFlow ToS Prefix Aggregation
    8.14 NetFlow ToS Prefix Port Aggregation
    1005 Flow-Tools tagged version 5
</pre>
<dt><code>-x</code><i> xmit_delay</i></p>
<dd> Configure a microsecond transmit delay between packets. This may be necessary in some configurations to prevent a transmit buffer overrun.</dl>
<h2>EXAMPLES</h2>
<p> Replicate flows arriving to local IP address 10.0.0.1 from the router exporting with IP address 10.1.1.1 on port 9500 to localhost port 9500 and 10.5.5.5 port 9200. The exports sent to 10.5.5.5 will be sent with a source IP address of 10.0.0.5 which must be a valid local IP address. </p>
<p> <code>flow-fanout 10.0.0.1/10.1.1.1/9500 0/0/9500 10.0.0.5/10.5.5.5/9200</code></p>
<h2>BUGS</h2>
<p> NetFlow exports do not contain the exporter IP address inside the payload so the original exporter IP address (typically a router) will be lost when using <code>flow-fanout</code>. A work around for this protocol limitation is to use local IP aliases and the <i>localip</i> option. When the spoofing option is used multiple exporters with different IP addresses will share the same sequence number but will have the original source IP. Fixing this requires per source : destination sequence number mapping. It is much easier to just use multiple instances of flow-fanout running on different ports.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
