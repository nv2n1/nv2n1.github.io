---
title: "flow-export(1)"
name: "flow-export"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-export/"
description: "flow-export – Export flow-tools files into other NetFlow packages."
---

<h2>NAME</h2>
<p> flow-export &#8211; Export flow-tools files into other NetFlow packages.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-export</code> [ <code>-h</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> format</i> ] [ <code>-m</code><i> mask_fields</i> ] [ <code>-u</code><i> user:password:host:port:name:table</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-export</code> utility will convert flow-tools flow files to ASCII CSV, cflowd, pcap, wire, mySQL, and PGSQL format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> format</i></p>
<dd> Export format. Supported formats are: 0 cflowd 1 pcap 2 ASCII CSV 3 MySQL 4 wire 5 PGSQL</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-m</code><i> mask_fields</i></p>
<dd> Select fields for MySQL, PostgresSQL, cflowd, and ASCII formats. The <i>mask_fields</i> is built from a bitwise OR of the following: </p>
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
<p> When exporting to cflowd format the <i>mask_fields</i> field is the cflowd mask which is defined as the following: </p>
<pre>
    ROUTERMASK         0x00000001
    SRCIPADDRMASK      0x00000002
    DSTIPADDRMASK      0x00000004
    INPUTIFINDEXMASK   0x00000008
    OUTPUTIFINDEXMASK  0x00000010
    SRCPORTMASK        0x00000020
    DSTPORTMASK        0x00000040
    PKTSMASK           0x00000080
    BYTESMASK          0x00000100
    IPNEXTHOPMASK      0x00000200
    STARTTIMEMASK      0x00000400
    ENDTIMEMASK        0x00000800
    PROTOCOLMASK       0x00001000
    TOSMASK            0x00002000
    SRCASMASK          0x00004000
    DSTASMASK          0x00008000
    SRCMASKLENMASK     0x00010000
    DSTMASKLENMASK     0x00020000
    TCPFLAGSMASK       0x00040000
    INPUTENCAPMASK     0x00080000
    OUTPUTENCAPMASK    0x00100000
    PEERNEXTHOPMASK    0x00200000
    ENGINETYPEMASK     0x00400000
    ENGINEIDMASK       0x00800000
    
    INDEX_V1_MASK      0x00043FFF
    INDEX_V5_MASK      0x00C7FFFF
    INDEX_V6_MASK      0x00FFFFFF
    INDEX_V7_MASK      0x00C7FFFF
    INDEX_V8_1_MASK    0x00C0CD99
    INDEX_V8_2_MASK    0x00C00DE1
    INDEX_V8_3_MASK    0x00C14D8B
    INDEX_V8_4_MASK    0x00C28D95
    INDEX_V8_5_MASK    0x00C3CD9F
</pre>
<p> The default value is all fields applicable to the the flow file, or the cflowd INDEX mask applicabable to the export format.</p>
<dt><code>-u</code><i> user:password:host:port:name:table</i></p>
<dd> Configure MySQL or PostgresSQL Access.</dl>
<h2>EXAMPLES</h2>
<p> Convert the flow-tools file <i>flows</i> to the cflowd file <i>flows.cflowd</i>. Include all fields. </p>
<p> <code>flow-export -f0 &lt; flows &gt; flows.cflowd</code></p>
<h2>EXAMPLES</h2>
<p> Convert the flow-tools file <i>flows</i> to the ASCII. Include the SRCADDR and DSTADDR fields. </p>
<p> <code>flow-export -f2 -m0x3000 &lt; flows &gt; flows.ascii</code></p>
<h2>EXAMPLES</h2>
<p> Export the flow-tools file <i>flows</i> to an MySQL Database. Include only SRCADDR, DSTADDR and DOCTETS. </p>
<p> <code>flow-export -f3 -mSRCADDR,DSTADDR,DOCTETS -u &quot;user:password:host:port:name:table&quot; &lt; flows </code></p>
<h2>BUGS</h2>
<p> The pcap format is a hack.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt; </p>
<p> Database Support: William Emmanuel Yu &lt;wyu [at] ateno.edu&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
