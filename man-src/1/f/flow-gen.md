---
title: "flow-gen(1)"
name: "flow-gen"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-gen/"
description: "flow-gen – Generate test flows"
---

<h2>NAME</h2>
<p> flow-gen &#8211; Generate test flows</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-gen</code> [ <code>-h</code> ] [ <code>-b</code><i> big</i><code>|</code><i>little</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-n</code><i> count</i> ] [ <code>-V</code><i> version</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-gen</code> utility generates a test pattern of flows in any of the currently supported export versions typically for debugging purposes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-n</code><i> count</i></p>
<dd> Generate count flows. Default 1000.</p>
<dt><code>-V</code><i> version</i></p>
<dd> Generate version type exports. Supported versions are: </p>
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
<p> Generate a test pattern of 1000 version 5 flows and send them in the Cisco NetFlow packet format to 10.0.0.1 port 9500. </p>
<p> <code>flow-gen -V5 | flow-send 0/10.0.0.1/9500</code></p>
<h2>BUGS</h2>
<p> The test pattern may change between releases.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
