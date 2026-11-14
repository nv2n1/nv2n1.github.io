---
title: "flow-import(1)"
name: "flow-import"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-import/"
description: "flow-import – Import flows into flow-tools from other NetFlow packages."
---

<h2>NAME</h2>
<p> flow-import &#8211; Import flows into flow-tools from other NetFlow packages.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-import</code> [ <code>-h</code> ] [ <code>-b</code><i> big|little</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> format</i> ] [ <code>-m</code><i> mask_fields</i> ] [ <code>-V</code><i> pdu_version</i> ] [ <code>-z</code><i> z_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-import</code> utility will convert data from cflowd and ASCII CSV files into flow-tools format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> format</i></p>
<dd> Export format. Supported formats are: </p>
<pre>
  0 cflowd
  2 ASCII CSV
  3 Cisco NFCollector
</pre>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-m</code><i> mask_fields</i></p>
<dd> Select fields for cflowd and ASCII formats. The <i>mask_fields</i> is built from a bitwise OR of the following: </p>
<pre>
    UNIX_SECS       0x0000000000000001LL
    UNIX_NSECS      0x0000000000000002LL
    SYSUPTIME       0x0000000000000004LL
    EXADDR          0x0000000000000008LL
    
    DFLOWS          0x0000000000000010LL
    DPKTS           0x0000000000000020LL
    DOCTETS         0x0000000000000040LL
    FIRST           0x0000000000000080LL
    
    LAST            0x0000000000000100LL
    ENGINE_TYPE     0x0000000000000200LL
    ENGINE_ID       0x0000000000000400LL
    
    SRCADDR         0x0000000000001000LL
    DSTADDR         0x0000000000002000LL
    SRC_PREFIX      0x0000000000004000LL
    DST_PREFIX      0x0000000000008000LL
    NEXTHOP         0x0000000000010000LL
    INPUT           0x0000000000020000LL
    OUTPUT          0x0000000000040000LL
    SRCPORT         0x0000000000080000LL
    
    DSTPORT         0x0000000000100000LL
    PROT            0x0000000000200000LL
    TOS             0x0000000000400000LL
    TCP_FLAGS       0x0000000000800000LL
    
    SRC_MASK        0x0000000001000000LL
    DST_MASK        0x0000000002000000LL
    SRC_AS          0x0000000004000000LL
    DST_AS          0x0000000008000000LL
    
    IN_ENCAPS       0x0000000010000000LL
    OUT_ENCAPS      0x0000000020000000LL
    PEER_NEXTHOP    0x0000000040000000LL
    ROUTER_SC       0x0000000080000000LL
    EXTRA_PKTS      0x0000000100000000LL
    MARKED_TOS      0x0000000200000000LL
</pre>
<p> The default value is all fields applicable to the <i>pdu_version</i>.</p>
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
<p> Convert the cflowd file <i>flows.cflowd</i> to the flow-tools file <i>flows</i>. Store as Version 5 with compression level 5. </p>
<p> <code>flow-import -V5 -z5 -f0 &lt; flows.cflowd &gt; flows</code></p>
<h2>EXAMPLES</h2>
<p> Convert the ASCII CSV data in flows.ascii to flow-tools format. The ASCII data must include all fields represented by 0xFF31EF in the order listed above. Store as Version 5 with no compression. </p>
<p> <code>flow-import -z0 -f2 -m0xFF31EF &lt; flows.ascii &gt; flows</code></p>
<h2>BUGS</h2>
<p> The pcap format is a hack.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
