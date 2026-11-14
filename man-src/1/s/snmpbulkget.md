---
title: "snmpbulkget(1)"
name: "snmpbulkget"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpbulkget/"
description: "snmpbulkget – communicates with a network entity using SNMP GETBULK requests."
---

<h2>NAME</h2>
<p> snmpbulkget &#8211; communicates with a network entity using SNMP GETBULK requests.</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpbulkget</code> [COMMON OPTIONS] [-Cn &lt;num&gt;] [-Cr &lt;NUM&gt;] AGENT OID [OID]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpbulkget</code> is an SNMP application that uses the SNMP GETBULK request to query a network entity efficiently for information. One or more object identifiers (OIDs) may be given as arguments on the command line. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<p> If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint why the request was malformed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Cn</code><i>&lt;NUM&gt;</i></p>
<dd> Set the <i>non-repeaters</i> field in the GETBULK PDU. This specifies the number of supplied variables that should not be iterated over. The default is 0.</p>
<dt><code>-Cr</code><i>&lt;NUM&gt;</i></p>
<dd> Set the <i>max-repetitions</i> field in the GETBULK PDU. This specifies the maximum number of iterations over the repeating variables. The default is 10.</dl>
<p> In addition to these options, <code>snmpbulkget</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. Note that <code>snmpbulkget</code> REQUIRES an argument specifying the agent to query and at least one OID argument, as described there.</p>
<h2>EXAMPLE</h2>
<p> The command: </p>
<p> snmpbulkget -v2c -Cn1 -Cr5 -Os -c public zeus system ifTable </p>
<p> will retrieve the variable system.sysDescr.0 (which is the lexicographically next object to system) and the first 5 objects in the ifTable: </p>
<p> sysDescr.0 = STRING: &quot;SunOS zeus.net.cmu.edu 4.1.3_U1 1 sun4m&quot;<br />
 ifIndex.1 = INTEGER: 1<br />
 ifIndex.2 = INTEGER: 2<br />
 ifDescr.1 = STRING: &quot;lo0&quot;<br />
 et cetera.</p>
<h2>NOTE</h2>
<p> As the name implies, <code>snmpbulkget</code> utilizes the SNMP GETBULK message, which is not available in SNMPv1.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5), RFC 1905. </p>
<h2>Index</h2>
