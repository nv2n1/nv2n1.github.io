---
title: "flow-print(1)"
name: "flow-print"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-print/"
description: "flow-print – Display flows in formatted ASCII."
---

<h2>NAME</h2>
<p> flow-print &#8211; Display flows in formatted ASCII.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-print</code> [ <code>-hlnpw</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> format</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-print</code> utility will display flow data in ASCII using pre-defined formats selectable with -f. </p>
<pre><code>
Some of the less descriptive column headers are defined below
Header     Description
-------------------------------
Sif           Source Interface ifIndex.
DiF           Destination Interface ifIndex.
Pr            Protocol.
P             Protocol.
SrcP          Source Port.
DstP          Destination Port.
Pkts          Packets.
Octets        Octets (Bytes).
Active        Time in ms the flow was active.
B/Pk          Bytes per Packet.
Ts            Type of Service.
Fl            Flags, for TCP the cumulative or of the TCP control bits.
srcAS         Source AS.
dstAS         Destination AS.
Start         Start time of the flow.
End           End time of the flow.
router_sc     V7 IP address of router producing shorcuts.
peer_nexthop  V6 IP address of peer next hop IP address.
encap i/o     Version 6 only.  Encapsulation size in/out
duration      Time in ms the flow was active.
input         Input Interface ifIndex.
output        Output Interface ifIndex.
flows         Number of aggregated flows.
mTos          V8.x ToS of pkts that exceeded the contract.
xpackets      V8.x Packets that exceed the contract.
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> format</i></p>
<dd> Select format. The default is appropriate for the export type of the flow data. Available formats are: </p>
<pre>
    0 1 line, interfaces, hex ports
    1 2 line (includes timing and flags)
    2 2 line candidate TCP syn attack flows
    3 1 line, no interfaces, decimal ports
    4 1 line with AS number
    5 1 line, 132 column
    6 show ip accounting emulation
    7 1 line, 132 column +router_id
    8 1 line, 132 column +encapsulation
    9 1 line with tag values
   10 AS aggregation
   11 Protocol Port aggregation
   12 Source Prefix aggregation
   13 Destination Prefix aggregation
   14 Prefix aggregation
   15 Destination aggregation (Catalyst)
   16 Source Destination aggregation (Catalyst)
   17 Full Flow (Catalyst)
   18 ToS AS Aggregation
   19 ToS Proto Port aggregation
   20 ToS Source Prefix aggregation
   21 ToS Destination Prefix aggregation
   22 ToS Prefix Aggregation
   23 ToS Prefix Port aggregation
   24 Full (Catalyst)
</pre>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-l</code></p>
<dd> Unbuffer output.</p>
<dt><code>-n</code></p>
<dd> Use symbolic names where appropriate.</p>
<dt><code>-p</code></p>
<dd> Display header information.</p>
<dt><code>-w</code></p>
<dd> Wide output.</dl>
<h2>EXAMPLES</h2>
<p> Display flows in <i>flowfile</i> </p>
<p> <code>flow-print &lt; flowfile</code></p>
<h2>FILES</h2>
<p> Configuration files: Symbols &#8211; <i>/etc/flow-tools/sym/*</i>.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
