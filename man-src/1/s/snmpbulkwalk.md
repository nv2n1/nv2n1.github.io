---
title: "snmpbulkwalk(1)"
name: "snmpbulkwalk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpbulkwalk/"
description: "snmpbulkwalk – retrieve a subtree of management values using SNMP GETBULK requests"
---

<h2>NAME</h2>
<p> snmpbulkwalk &#8211; retrieve a subtree of management values using SNMP GETBULK requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpbulkwalk</code> [APPLICATION OPTIONS] [COMMON OPTIONS] AGENT [OID]</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpbulkwalk</code> is an SNMP application that uses SNMP GETBULK requests to query a network entity efficiently for a tree of information. </p>
<p> An object identifier (OID) may be given on the command line. This OID specifies which portion of the object identifier space will be searched using GETBULK requests. All variables in the subtree below the given OID are queried and their values presented to the user. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. If no OID argument is present, <code>snmpbulkwalk</code> will search MIB-2. </p>
<p> If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint why the request was malformed. </p>
<p> If the tree search causes attempts to search beyond the end of the MIB, the message &quot;End of MIB&quot; will be displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Cc</code></p>
<dd> Do not check whether the returned OIDs are increasing. Some agents (LaserJets are an example) return OIDs out of order, but can complete the walk anyway. Other agents return OIDs that are out of order and can cause <code>snmpbulkwalk</code> to loop indefinitely. By default, <code>snmpbulkwalk</code> tries to detect this behavior and warns you when it hits an agent acting illegally. Use <code>-Cc</code> to turn off this behaviour.</p>
<dt><code>-Ci</code></p>
<dd> Include the given OID in the search range. Normally <code>snmpbulkwalk</code> uses GETBULK requests starting with the OID you specified and returns all results in the MIB tree after that OID. Sometimes, you may wish to include the OID specified on the command line in the printed results if it is a valid OID in the tree itself. This option lets you do this.</p>
<dt><code>-Cn</code><i>&lt;NUM&gt;</i></p>
<dd> Set the <i>non-repeaters</i> field in the GETBULK PDUs. This specifies the number of supplied variables that should not be iterated over. The default is 0.</p>
<dt><code>-Cp</code></p>
<dd> Upon completion of the walk, print the number of variables found.</p>
<dt><code>-Cr</code><i>&lt;NUM&gt;</i></p>
<dd> Set the <i>max-repetitions</i> field in the GETBULK PDUs. This specifies the maximum number of iterations over the repeating variables. The default is 10.</dl>
<p> In addition to these options, <code>snmpbulkwalk</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. Note that <code>snmpbulkget</code> REQUIRES an argument specifying the agent to query and at most one OID argument, as described above.</p>
<h2>EXAMPLE</h2>
<p> The command: </p>
<p> snmpbulkwalk -v2c -Os -c public zeus system </p>
<p> will retrieve all of the variables under system: </p>
<p> sysDescr.0 = STRING: &quot;SunOS zeus.net.cmu.edu 4.1.3_U1 1 sun4m&quot;<br />
 sysObjectID.0 = OID: enterprises.hp.nm.hpsystem.10.1.1<br />
 sysUpTime.0 = Timeticks: (155274552) 17 days, 23:19:05<br />
 sysContact.0 = STRING: &quot;&quot;<br />
 sysName.0 = STRING: &quot;zeus.net.cmu.edu&quot;<br />
 sysLocation.0 = STRING: &quot;&quot;<br />
 sysServices.0 = INTEGER: 72 </p>
<p> In contrast to <code>snmpwalk</code>, this information will typically be gathered in a single transaction with the agent, rather than one transaction per variable found. <code>snmpbulkwalk</code> is thus more efficient in terms of network utilisation, which may be especially important when retrieving large tables.</p>
<h2>NOTE</h2>
<p> As the name implies, <code>snmpbulkwalk</code> utilizes the SNMP GETBULK message, which is not available in SNMP v1.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
