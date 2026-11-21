---

title: "snmpcheck(1)"
name: "snmpcheck"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpcheck/"
description: "snmpcheck – enumerate information via SNMP protocol"
---

<p> snmpcheck &#8211; enumerate information via SNMP protocol</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpcheck</code> [<code>-OPTIONS </code>] <code>-t</code> <i>&lt;IP address&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> Like to snmpwalk, snmpcheck permits to enumerate information via SNMP protocol. It allows enumeration (hardware, software, network) of any devices with SNMP protocol support. It could be useful for penetration testing or systems monitoring. </p>
<p> Snmpcheck supports the following enumerations (in alfabetic order):</p>
<dl>
<dt>
</dt><dd> contact, description, devices, domain, hardware and storage informations, hostname, IIS statistics, IP forwarding, listening UDP ports, location, motd, mountpoints, network interfaces, network services, processes, routing information, software components, system uptime, TCP connections, total memory, uptime, user accounts, detect write access (separate action by enumeration) </dd>
</dl>
<p> Tested on GNU/Linux, *BSD and Windows (Cygwin and ActivePerl) systems. </p>
<p> Distributed under GPL license and based on &quot;Athena-2k&quot; script by jshaw. </p>
<h2>OPTIONS</h2>
<p> <code>-t </code><i>&lt;host&gt;</i> target host</p>
<dl>
<dt><code>-p </code><i>&lt;port&gt;</i></dt>
<dd> SNMP port; default port is 161</dd>
<dt><code>-c </code><i>&lt;community_string&gt;</i></dt>
<dd> SNMP community; default is public</dd>
<dt><code>-v </code><i>&lt;version&gt;</i></dt>
<dd> SNMP version (1,2); default is 1</dd>
<dt><code>-r </code><i>&lt;retries&gt;</i></dt>
<dd> request retries; default is 0</dd>
<dt><code>-T </code><i>&lt;timeout&gt;</i></dt>
<dd> force timeout in seconds; default is 20. Max is 60</dd>
<dt><code>-w</code></dt>
<dd> detect write access (separate action by enumeration)</dd>
<dt><code>-d</code></dt>
<dd> disable &#8216;TCP connections&#8217; enumeration! &quot;TCP connections enumeration&quot; can be very long. Use -d flag to disable it.</dd>
<dt><code>-D</code></dt>
<dd> enable debug</dd>
<dt><code>-h</code></dt>
<dd> show help menu </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-snmpwalk/">snmpwalk</a></code>(1), <code><a href="/docs/linux/man/1-snmpget/">snmpget</a></code>(1), <code>onesixtyone</code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (c) 2005-2011 by Matteo Cantoni &lt;matteo.cantoni [at] nothink.org&gt; </p>
