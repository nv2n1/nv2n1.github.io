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
<p> <code>agentxtrap</code> [<i>OPTIONS</i>]<i> trap-oid </i>[<i>OID TYPE VALUE</i>&#8230;]</p>
<p> <code>agentxtrap</code> issues an AgentX NotifyPDU to a master agent. One or more object identifiers (OIDs) can be given as arguments on the command line. A type and a value must accompany each object identifier. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> contextName</i></dt>
<dd> if the <code>-c</code> option is present then the notification is sent in the nondefault name context.</dd>
<dt><code>-U</code><i> uptime</i></dt>
<dd> if the <code>-U</code> option is present then that value, parsed as centiseconds, is taken to be the sysUpTime field of the application.</dd>
<dt><code>-x</code><i> ADDRESS</i></dt>
<dd> if the <code>-x</code> option is present then contact the AgentX master at ADDRESS and not the default one.</dd></dl>
<p> Additionally all the options described in <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> under the <code>MIB PARSING OPTIONS</code>, <code>LOGGING OPTIONS</code> and <code>INPUT OPTIONS</code> headers as well as the <code>-d</code>, <code>-D</code>, <code>-m</code> and <code>-M</code> options are supported. </p>
<p> In <i>OID TYPE VALUE</i> the parsing of the <i>VALUE</i> field is controlled by the <i>TYPE</i> field. The possible values for the <i>TYPE</i> field is one of the following characters:</p>
<dl>
<dl>
<dt><code>=</code></dt>
<dd> Let <i>OID</i> decide how <i>VALUE</i> should be interpreted</dd>
<dt><code>i</code></dt>
<dd> INTEGER</dd>
<dt><code>u</code></dt>
<dd> Unsigned</dd>
<dt><code>c</code></dt>
<dd> Counter32</dd>
<dt><code>s</code></dt>
<dd> OCTET STRING of chaacters</dd>
<dt><code>x</code></dt>
<dd> OCTET STRING, entered as a sequence of optionally space separated hexadecimal digit pairs</dd>
<dt><code>d</code></dt>
<dd> OCTET STRING, entered as a sequence of space separated decimal digits in the range 0 &#8211; 255</dd>
<dt><code>n</code></dt>
<dd> NULL</dd>
<dt><code>o</code></dt>
<dd> OBJECT IDENTIFIER</dd>
<dt><code>t</code></dt>
<dd> TimeTicks</dd>
<dt><code>a</code></dt>
<dd> IpAddress</dd>
<dt><code>b</code></dt>
<dd> BITS</dd></dl>
</dl>
<p> which are handled in the same way as the <code>snmpset</code> command. </p>
<h2>EXAMPLES</h2>
<p> To send a generic linkUp trap to the manager for interface 1 the following command can be used: </p>
<p> agentxtrap netSnmp.0.3 ifindex.1 i 1 </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpset/">snmpset</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5), RFC 2741 </p>
