---
title: "snmptable(1)"
name: "snmptable"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmptable/"
description: "snmptable – retrieve an SNMP table and display it in tabular form"
---

<h2>NAME</h2>
<p> snmptable &#8211; retrieve an SNMP table and display it in tabular form</p>
<h2>SYNOPSIS</h2>
<p> <code>snmptable</code> [COMMON OPTIONS] [-Cb] [-CB] [-Ch] [-CH] [-Ci] [-Cf STRING] [-Cw WIDTH] AGENT TABLE-OID</p>
<h2>DESCRIPTION</h2>
<p> <code>snmptable</code> is an SNMP application that repeatedly uses the SNMP GETNEXT or GETBULK requests to query for information on a network entity. The parameter <i>TABLE-OID</i> must specify an SNMP table. </p>
<p> snmptable is an SNMP application that repeatedly uses the SNMP GETNEXT or GETBULK requests to query for information on a network entity. The parameter TABLE-OID must specify an SNMP table. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the gievn objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. In this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a full list of the possible formats for AGENT.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>COMMON OPTIONS</code></p>
<dd> Please see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a list of possible values for COMMON OPTIONS as well as their descriptions.</p>
<dt><code>-Cb</code></p>
<dd> Display only a brief heading. Any common prefix of the table field names will be deleted.</p>
<dt><code>-CB</code></p>
<dd> Do not use GETBULK requests to retrieve data, only GETNEXT.</p>
<dt><code>-Cc</code><i> CHARS</i></p>
<dd> Print table in columns of <i>CHARS</i> characters width.</p>
<dt><code>-Cf</code><i> STRING</i></p>
<dd> The string <i>STRING</i> is used to separate table columns. With this option, each table entry will be printed in compact form, just with the string given to separate the columns (useful if you want to import it into a database). Otherwise it is printed in nicely aligned columns.</p>
<dt><code>-Ch</code></p>
<dd> Display <i>only</i> the column headings.</p>
<dt><code>-CH</code></p>
<dd> Do not display the column headings.</p>
<dt><code>-Ci</code></p>
<dd> This option prepends the index of the entry to all printed lines.</p>
<dt><code>-Cl</code></p>
<dd> Left justify the data in each column.</p>
<dt><code>-Cr</code><i> REPEATERS</i></p>
<dd> For GETBULK requests, <i>REPEATERS</i> specifies the max-repeaters value to use. For GETNEXT requests, <i>REPEATERS</i> specifies the number of entries to retrieve at a time.</p>
<dt><code>-Cw</code><i> WIDTH</i></p>
<dd> Specifies the width of the lines when the table is printed. If the lines will be longer, the table will be printed in sections of at most <i>WIDTH </i> characters. If <i>WIDTH</i> is less than the length of the contents of a single column, then that single column will still be printed.</dl>
<p> Note that <code>snmptable</code> REQUIRES an argument specifying the agent to query and exactly one OID argument, as described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. This OID <code>must</code> be that of a MIB table object.</p>
<h2>EXAMPLES</h2>
<p> $ snmptable -v 2c -c public localhost at.atTable </p>
<p> SNMP table: at.atTable RFC1213-MIB::atTable </p>
<p> atIfIndex atPhysAddress atNetAddress<br />
&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>8:0:20:20:0:ab 130.225.243.33 </p>
<p> $ snmptable -v 2c -c public -Cf + localhost at.atTable </p>
<p> SNMP table: at.atTable </p>
<p> atIfIndex+atPhysAddress+atNetAddress 1+8:0:20:20:0:ab+130.225.243.33 </p>
<pre><code>
$ snmptable localhost - Cl - CB - Ci - OX - Cb - Cc 16 - Cw 64 ifTable SNMP table : ifTable Index Descr Type Mtu Speed PhysAddress AdminStatus OperStatus LastChange InOctets InUcastPkts InNUcastPkts InDiscards InErrors InUnknownProtos OutOctets OutUcastPkts OutNUcastPkts OutDiscards OutErrors OutQLen Specific index : [1] 1 lo softwareLoopbac 16436 10000000 up up
    ? 2837283786 3052466 ? 0 0 ? 2837283786 3052466 ? 0 0 0 zeroDotZero
                                                          index
                                                    : [2] 2 eth0 ethernetCsmacd 1500 10000000 0
                               : 5
                         : 5d
    : d1 : f7 : cf up up
                ? 2052604234 44252973
                ? 0 0
                ? 149778187 65897282
                ? 0 0 0 zeroDotZero
</code></pre>
<h2>BUGS</h2>
<p> The test for <i>TABLE-OID</i> actually specifying a table is rather heuristic. Note also that the test requires the defining MIB file to be loaded. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
