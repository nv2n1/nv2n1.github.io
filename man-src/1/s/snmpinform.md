---

title: "snmpinform(1)"
name: "snmpinform"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpinform/"
description: "snmptrap, snmpinform – sends an SNMP notification to a manager"
---

<p> snmptrap, snmpinform &#8211; sends an SNMP notification to a manager</p>
<h2>SYNOPSIS</h2>
<p> <code>snmptrap -v 1</code> [COMMON OPTIONS] AGENT enterprise-oid agent generic-trap specific-trap uptime [OID TYPE VALUE]&#8230; </p>
<p> <code>snmptrap -v [2c|3]</code> [COMMON OPTIONS] [-Ci] AGENT uptime trap-oid [OID TYPE VALUE]&#8230; </p>
<p> <code>snmpinform -v [2c|3]</code> [COMMON OPTIONS] AGENT uptime trap-oid [OID TYPE VALUE]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmptrap</code> is an SNMP application that uses the SNMP TRAP operation to send information to a network manager. One or more object identifiers (OIDs) can be given as arguments on the command line. A type and a value must accompany each object identifier. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<p> When invoked as <code>snmpinform,</code> or when <code>-Ci</code> is added to the command line flags of snmptrap, it sends an INFORM-PDU, expecting a response from the trap receiver, retransmitting if required. Otherwise it sends an TRAP-PDU or TRAP2-PDU. </p>
<p> If any of the required version 1 parameters, <i>enterprise-oid</i>, <i>agent</i>, and <i>uptime</i> are specified as empty, it defaults to <i>1.3.6.1.4.1.3.1.1 (enterprises.cmu.1.1)</i>, <i>hostname</i>, and <i>host-uptime</i> respectively. </p>
<p> The <i>TYPE</i> is a single character, one of:</p>
<dl>
<dl>
<dt><code>i</code></dt>
<dd> INTEGER</dd>
<dt><code>u</code></dt>
<dd> UNSIGNED</dd>
<dt><code>c</code></dt>
<dd> COUNTER32</dd>
<dt><code>s</code></dt>
<dd> STRING</dd>
<dt><code>x</code></dt>
<dd> HEX STRING</dd>
<dt><code>d</code></dt>
<dd> DECIMAL STRING</dd>
<dt><code>n</code></dt>
<dd> NULLOBJ</dd>
<dt><code>o</code></dt>
<dd> OBJID</dd>
<dt><code>t</code></dt>
<dd> TIMETICKS</dd>
<dt><code>a</code></dt>
<dd> IPADDRESS</dd>
<dt><code>b</code></dt>
<dd> BITS</dd></dl>
</dl>
<p> which are handled in the same way as the <code>snmpset</code> command. </p>
<p> For example: </p>
<p> snmptrap -v 1 -c public manager enterprises.spider test-hub 3 0 &#8221; interfaces.iftable.ifentry.ifindex.1 i 1 </p>
<p> will send a generic linkUp trap to manager, for interface 1.</p>
<h2>OPTIONS</h2>
<p> <code>snmptrap</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) </i> manual page in addition to the <code>-Ci</code> option described above. Note that <code>snmptrap</code> REQUIRES an argument specifying the agent to query as described there.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpset/">snmpset</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
