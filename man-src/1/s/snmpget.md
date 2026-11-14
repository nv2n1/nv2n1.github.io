---
title: "snmpget(1)"
name: "snmpget"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpget/"
description: "snmpget – communicates with a network entity using SNMP GET requests"
---

<h2>NAME</h2>
<p> snmpget &#8211; communicates with a network entity using SNMP GET requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpget</code> [COMMON OPTIONS] [-Cf] AGENT OID [OID]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpget</code> is an SNMP application that uses the SNMP GET request to query for information on a network entity. One or more object identifiers (OIDs) may be given as arguments on the command line. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-Cf</code></p>
<dd> If <code>-Cf</code> is <i>not</i> specified, some applications (<code>snmpdelta</code>, <code>snmpget</code>, <code>snmpgetnext</code> and <code>snmpstatus</code>) will try to fix errors returned by the agent that you were talking to and resend the request. The only time this is really useful is if you specified a OID that didn&#8217;t exist in your request and you&#8217;re using SNMPv1 which requires &quot;all or nothing&quot; kinds of requests.</dl>
<p> In addition to this option, <code>snmpget</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. Note that <code>snmpget</code> REQUIRES an argument specifying the agent to query and at least one OID argument, as described there.</p>
<h2>EXAMPLES</h2>
<p> The command: </p>
<p>&nbsp;<wbr>snmpget -c public zeus system.sysDescr.0 </p>
<p> will retrieve the variable system.sysDescr.0 from the host <code>zeus </code> using the community string <code>public</code> : </p>
<p>&nbsp;<wbr>system.sysDescr.0&nbsp;<wbr>=&nbsp;<wbr>&quot;SunOS zeus.net.cmu.edu 4.1.3_U1 1 sun4m&quot; </p>
<p> If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint in what way the request was malformed. If there were other variables in the request, the request will be resent without the bad variable. </p>
<p> Here is another example. The -c and -v options are defined in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. (Note that system.sysUpTime is an incomplete OID, as it needs the .0 index appended to it): </p>
<pre>
    snmpget -v1 -Cf -c public localhost system.sysUpTime system.sysContact.0
</pre>
<p> This example will return the following: </p>
<pre>
    Error in packet
    Reason: (noSuchName) There is no such variable name in this MIB.
    This name doesn't exist: system.sysUpTime
</pre>
<p> Similarly, the command: </p>
<pre>
    snmpget -v1 -c public localhost system.sysUpTime system.sysContact.0
</pre>
<p> Will return: </p>
<pre>
    Error in packet
    Reason: (noSuchName) There is no such variable name in this MIB.
    This name doesn't exist: system.sysUpTime
    system.sysContact.0 = STRING: root [at] localhost
</pre>
<p> With the <code>-Cf</code> flag specified the application will not try to fix the PDU for you.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpwalk/">snmpwalk</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
