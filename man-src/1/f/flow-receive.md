---
title: "flow-receive(1)"
name: "flow-receive"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-receive/"
description: "flow-receive – Receive flow data with the NetFlow protocol."
---

<h2>NAME</h2>
<p> flow-receive &#8211; Receive flow data with the NetFlow protocol.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-receive</code> [ <code>-h</code> ] [ <code>-b</code><i> big|little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-o</code><i> output_file</i> ] [ <code>-S</code><i> stat_interval</i> ] [ <code>-V</code><i> pdu_version</i> ] [ <code>-z</code><i> z_level</i> ] <i>localip/remoteip/port</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-receive</code> utility is used to receive flows in NetFlow format. When the <i>remoteip</i> is configured only flows from that exporter will be processed, this is the most secure and recommended configuration. When the <i>localip</i> is configured <code>flow-receive</code> will only process flows sent to the <i> localip</i> IP address. If <i>remoteip</i> is 0 (not configured) flows from any source IP address are accepted. Multiple non aggregated PDU versions may be accepted at once to support Cisco&#8217;s Catalyst 6500 NetFlow implementation which exports from both the supervisor and MSFC with the same IP address and same port but different export versions. In this case the exports will be stored in the format specified by the -V flag or whichever export type is received first.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-o</code><i> file</i></p>
<dd> Write to <i>file</i> instead of the standard out.</p>
<dt><code>-S</code><i> stat_interval</i></p>
<dd> When configured <code>flow-receive</code> will emit a timestamped message on stderr every <i>stat_interval</i> minutes indicating counters such as the number of flows received, packets processed, and lost flows.</p>
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
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dl>
<h2>EXAMPLES</h2>
<p> Listen on port 9800 on any local interface for exports from IP address 10.0.0.1, store the exports in <i>flows</i> </p>
<p> <code>flow-receive</code> 0/10.0.0.1/9800 &gt; <i>flows</i> </p>
<p> Listen on port 9800 on any local interface from any IP address, display the received flows with flow-print. </p>
<p> <code>flow-receive</code> 0/0/9800 | <code>flow-print</code></p>
<h2>BUGS</h2>
<p> It is not currently possible to convert between the aggregated formats (8.x) and the non aggregated formats (1,5,6,7).</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
