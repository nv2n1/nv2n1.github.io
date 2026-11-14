---
title: "snmpset(1)"
name: "snmpset"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpset/"
description: "snmpset – communicates with a network entity using SNMP SET requests"
---

<h2>NAME</h2>
<p> snmpset &#8211; communicates with a network entity using SNMP SET requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpset</code> [COMMON OPTIONS] AGENT OID TYPE VALUE [OID TYPE VALUE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpset</code> is an SNMP application that uses the SNMP SET request to set information on a network entity. One or more object identifiers (OIDs) must be given as arguments on the command line. A type and a value to be set must accompany each object identifier. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<p> The <i>TYPE</i> is a single character, one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>i</code></p>
<dd> INTEGER</p>
<dt><code>u</code></p>
<dd> UNSIGNED</p>
<dt><code>s</code></p>
<dd> STRING</p>
<dt><code>x</code></p>
<dd> HEX STRING</p>
<dt><code>d</code></p>
<dd> DECIMAL STRING</p>
<dt><code>n</code></p>
<dd> NULLOBJ</p>
<dt><code>o</code></p>
<dd> OBJID</p>
<dt><code>t</code></p>
<dd> TIMETICKS</p>
<dt><code>a</code></p>
<dd> IPADDRESS</p>
<dt><code>b</code></p>
<dd> BITS</dl>
</dl>
<p> Most of these will use the obvious corresponding ASN.1 type. &#8216;s&#8217;, &#8216;x&#8217;, &#8216;d&#8217; and &#8216;b&#8217; are all different ways of specifying an OCTET STRING value, and the &#8216;u&#8217; unsigned type is also used for handling Gauge32 values. </p>
<p> If you have the proper MIB file loaded, you can, in most cases, replace the type with an &#8216;=&#8217; sign. For an object of type OCTET STRING this will assume a string like the &#8216;s&#8217; type notation. For other types it will do &quot;The Right Thing&quot;. </p>
<p> For example: </p>
<p> snmpset -c private -v 1 test-hub system.sysContact.0 s dpz [at] noc.rutgers.edu ip.ipforwarding.0 = 2 </p>
<p> will set the variables sysContact.0 and ipForwarding.0: </p>
<p> system.sysContact.0 = STRING: &quot;dpz [at] noc.rutgers.edu&quot;<br />
 ip.ipForwarding.0 = INTEGER: <a href="/docs/linux/man/2-not-forwarding/">not-forwarding</a>(2) </p>
<p> If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint in what way the request was malformed.</p>
<h2>OPTIONS</h2>
<p> <code>snmpset</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. Note that <code>snmpset</code> REQUIRES an argument specifying the agent to query and at least one set of OID/type/value arguments, as described in there.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
