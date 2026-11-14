---
title: "agentxtrap(1)"
name: "agentxtrap"
section: "1"
letter: "a"
url: "/docs/linux/man/1-agentxtrap/"
description: "agentxtrap – send an AgentX NotifyPDU to an AgentX master agent"
---

<h2>NAME</h2>
<p> agentxtrap &#8211; send an AgentX NotifyPDU to an AgentX master agent</p>
<h2>SYNOPSIS</h2>
<p> <code>agentxtrap</code> [<i>OPTIONS</i>]<i> trap-oid </i>[<i>OID TYPE VALUE</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>agentxtrap</code> issues an AgentX NotifyPDU to a master agent. One or more object identifiers (OIDs) can be given as arguments on the command line. A type and a value must accompany each object identifier. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> contextName</i></p>
<dd> if the <code>-c</code> option is present then the notification is sent in the nondefault name context.</p>
<dt><code>-U</code><i> uptime</i></p>
<dd> if the <code>-U</code> option is present then that value, parsed as centiseconds, is taken to be the sysUpTime field of the application.</p>
<dt><code>-x</code><i> ADDRESS</i></p>
<dd> if the <code>-x</code> option is present then contact the AgentX master at ADDRESS and not the default one.</dl>
<p> Additionally all the options described in <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> under the <code>MIB PARSING OPTIONS</code>, <code>LOGGING OPTIONS</code> and <code>INPUT OPTIONS</code> headers as well as the <code>-d</code>, <code>-D</code>, <code>-m</code> and <code>-M</code> options are supported. </p>
<p> In <i>OID TYPE VALUE</i> the parsing of the <i>VALUE</i> field is controlled by the <i>TYPE</i> field. The possible values for the <i>TYPE</i> field is one of the following characters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>=</code></p>
<dd> Let <i>OID</i> decide how <i>VALUE</i> should be interpreted</p>
<dt><code>i</code></p>
<dd> INTEGER</p>
<dt><code>u</code></p>
<dd> Unsigned</p>
<dt><code>c</code></p>
<dd> Counter32</p>
<dt><code>s</code></p>
<dd> OCTET STRING of chaacters</p>
<dt><code>x</code></p>
<dd> OCTET STRING, entered as a sequence of optionally space separated hexadecimal digit pairs</p>
<dt><code>d</code></p>
<dd> OCTET STRING, entered as a sequence of space separated decimal digits in the range 0 &#8211; 255</p>
<dt><code>n</code></p>
<dd> NULL</p>
<dt><code>o</code></p>
<dd> OBJECT IDENTIFIER</p>
<dt><code>t</code></p>
<dd> TimeTicks</p>
<dt><code>a</code></p>
<dd> IpAddress</p>
<dt><code>b</code></p>
<dd> BITS</dl>
</dl>
<p> which are handled in the same way as the <code>snmpset</code> command. </p>
<h2>EXAMPLES</h2>
<p> To send a generic linkUp trap to the manager for interface 1 the following command can be used: </p>
<p> agentxtrap netSnmp.0.3 ifindex.1 i 1 </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpset/">snmpset</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5), RFC 2741 </p>
<h2>Index</h2>
