---
title: "snmpgetnext(1)"
name: "snmpgetnext"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpgetnext/"
description: "snmpgetnext – communicates with a network entity using SNMP GETNEXT requests"
---

<h2>NAME</h2>
<p> snmpgetnext &#8211; communicates with a network entity using SNMP GETNEXT requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpgetnext</code> [COMMON OPTIONS] [-Cf] AGENT OID [OID]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpget</code> is an SNMP application that uses the SNMP GETNEXT request to query for information on a network entity. One or more object identifiers (OIDs) may be given as arguments on the command line. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. For each one, the variable that is lexicographically &quot;next&quot; in the remote entity&#8217;s MIB will be returned. </p>
<p> For example: </p>
<p> snmpgetnext -c public zeus interfaces.ifTable.ifEntry.ifType.1 </p>
<p> will retrieve the variable interfaces.ifTable.ifEntry.ifType.2: </p>
<p> interfaces.ifTable.ifEntry.ifType.2 = softwareLoopback(24) </p>
<p> If the network entity has an error processing the request packet, an error message will be shown, helping to pinpoint in what way the request was malformed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Cf</code></p>
<dd> If <code>-Cf</code> is <i>not</i> specified, some applications (<code>snmpdelta</code>, <code>snmpget</code>, <code>snmpgetnext</code> and <code>snmpstatus</code>) will try to fix errors returned by the agent that you were talking to and resend the request. The only time this is really useful is if you specified a OID that didn&#8217;t exist in your request and you&#8217;re using SNMPv1 which requires &quot;all or nothing&quot; kinds of requests.</dl>
<p> In addition to this option, <code>snmpgetnext</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. Note that <code>snmpgetnext</code> REQUIRES an argument specifying the agent to query and at least one OID argument, as described there.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpget/">snmpget</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
