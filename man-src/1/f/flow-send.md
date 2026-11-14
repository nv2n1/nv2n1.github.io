---
title: "flow-send(1)"
name: "flow-send"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-send/"
description: "flow-send – Transmit flow data with the NetFlow protocol."
---

<h2>NAME</h2>
<p> flow-send &#8211; Transmit flow data with the NetFlow protocol.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-send</code> [ <code>-h</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-m</code><i> privacy_mask</i> ] [ <code>-s</code> ] [ <code>-x</code><i> xmit_delay</i> ] [ <code>-V</code><i> pdu_version</i> ] <i>localip/remoteip/port</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-send</code> utility is used to transmit flows in NetFlow format to a collector specified by localip/remoteip/port.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-s</code></p>
<dd> Enable spoofing of source IP address.</p>
<dt><code>-m</code><i> privacy_mask</i></p>
<dd> Apply <i>privacy_mask</i> to the source and destination IP address of flows. For example a privacy_mask of 255.255.255.0 would convert flows with source/destination IP addresses 10.1.1.1 and 10.2.2.2 to 10.1.1.0 and 10.2.2.0 respectively.</p>
<dt><code>-V</code><i> pdu_version</i></p>
<dd> Use <i>pdu_version</i> format when transmitting. </p>
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
<p> Transmit all flows in the directory /flows/krc4 to the collector at 10.0.0.1 listening on port 9500. </p>
<p> <code>flow-cat /flows/krc4 | flow-send 0/10.0.0.1/9500</code> </p>
<p> Generate a test pattern of version 7 flows and send them to a collector at 10.0.0.1 listening on port 9500. </p>
<p> <code>flow-gen -V7 | flow-send 0/10.0.0.1/9500</code></p>
<h2>BUGS</h2>
<p> It is not currently possible to convert between the aggregated formats (8.x) and the non aggregated formats (1,5,6,7).</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
