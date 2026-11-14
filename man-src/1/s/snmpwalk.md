---
title: "snmpwalk(1)"
name: "snmpwalk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpwalk/"
description: "snmpwalk – retrieve a subtree of management values using SNMP GETNEXT requests"
---

<h2>NAME</h2>
<p> snmpwalk &#8211; retrieve a subtree of management values using SNMP GETNEXT requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpwalk</code> [APPLICATION OPTIONS] [COMMON OPTIONS] AGENT [OID]</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpwalk</code> is an SNMP application that uses SNMP GETNEXT requests to query a network entity for a tree of information. </p>
<p> An object identifier (OID) may be given on the command line. This OID specifies which portion of the object identifier space will be searched using GETNEXT requests. All variables in the subtree below the given OID are queried and their values presented to the user. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<p> If no OID argument is present, <code>snmpwalk</code> will search the subtree rooted at SNMPv2-SMI::mib-2 (including any MIB object values from other MIB modules, that are defined as lying within this subtree). If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint why the request was malformed. </p>
<p> If the tree search causes attempts to search beyond the end of the MIB, the message &quot;End of MIB&quot; will be displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Cc</code></p>
<dd> Do not check whether the returned OIDs are increasing. Some agents (LaserJets are an example) return OIDs out of order, but can complete the walk anyway. Other agents return OIDs that are out of order and can cause <code>snmpwalk</code> to loop indefinitely. By default, <code>snmpwalk</code> tries to detect this behavior and warns you when it hits an agent acting illegally. Use <code>-Cc</code> to turn off this check.</p>
<dt><code>-CE {OID}</code></p>
<dd> End the walk at the specified OID, rather than a simple subtree. This can be used to walk a partial subtree, selected columns of a table, or even two or more tables within a single command.</p>
<dt><code>-Ci</code></p>
<dd> Include the given OID in the search range. Normally <code>snmpwalk</code> uses GETNEXT requests starting with the OID you specified and returns all results in the MIB subtree rooted at that OID. Sometimes, you may wish to include the OID specified on the command line in the printed results if it is a valid OID in the tree itself. This option lets you do this explicitly.</p>
<dt><code>-CI</code></p>
<dd> In fact, the given OID will be retrieved automatically if the main subtree walk returns no useable values. This allows a walk of a single instance to behave as generally expected, and return the specified instance value. This option turns off this final GET request, so a walk of a single instance will return nothing.</p>
<dt><code>-Cp</code></p>
<dd> Upon completion of the walk, print the number of variables found.</p>
<dt><code>-Ct</code></p>
<dd> Upon completion of the walk, print the total wall-clock time it took to collect the data (in seconds). Note that the timer is started just before the beginning of the data request series and stopped just after it finishes. Most importantly, this means that it does not include snmp library initialization, shutdown, argument processing, and any other overhead.</dl>
<p> In addition to these options, <code>snmpwalk</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page.</p>
<h2>EXAMPLES</h2>
<p> Note that <code>snmpbulkget</code> REQUIRES an argument specifying the agent to query and at most one OID argument, as described there. The command: </p>
<p> snmpwalk -Os -c public -v 1 zeus system </p>
<p> will retrieve all of the variables under system: </p>
<p> sysDescr.0 = STRING: &quot;SunOS zeus.net.cmu.edu 4.1.3_U1 1 sun4m&quot;<br />
 sysObjectID.0 = OID: enterprises.hp.nm.hpsystem.10.1.1<br />
 sysUpTime.0 = Timeticks: (155274552) 17 days, 23:19:05<br />
 sysContact.0 = STRING: &quot;&quot;<br />
 sysName.0 = STRING: &quot;zeus.net.cmu.edu&quot;<br />
 sysLocation.0 = STRING: &quot;&quot;<br />
 sysServices.0 = INTEGER: 72<br />
 (plus the contents of the sysORTable). </p>
<p> The command: </p>
<p> snmpwalk -Os -c public -v 1 -CE sysORTable zeus system </p>
<p> will retrieve the scalar values, but omit the sysORTable.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpbulkwalk/">snmpbulkwalk</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
