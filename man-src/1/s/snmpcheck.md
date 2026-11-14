---
title: "snmpcheck(1)"
name: "snmpcheck"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpcheck/"
description: "snmpcheck – enumerate information via SNMP protocol"
---

<h2>NAME</h2>
<p> snmpcheck &#8211; enumerate information via SNMP protocol</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpcheck</code> [<code>-OPTIONS </code>] <code>-t</code> <i>&lt;IP address&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> Like to snmpwalk, snmpcheck permits to enumerate information via SNMP protocol. It allows enumeration (hardware, software, network) of any devices with SNMP protocol support. It could be useful for penetration testing or systems monitoring. </p>
<p> Snmpcheck supports the following enumerations (in alfabetic order):</p>
<dl>
<dt>
<dd> contact, description, devices, domain, hardware and storage informations, hostname, IIS statistics, IP forwarding, listening UDP ports, location, motd, mountpoints, network interfaces, network services, processes, routing information, software components, system uptime, TCP connections, total memory, uptime, user accounts, detect write access (separate action by enumeration) </p>
</dl>
<p> Tested on GNU/Linux, *BSD and Windows (Cygwin and ActivePerl) systems. </p>
<p> Distributed under GPL license and based on &quot;Athena-2k&quot; script by jshaw. </p>
<h2>OPTIONS</h2>
<p> <code>-t </code><i>&lt;host&gt;</i> target host</p>
<dl>
<dt><code>-p </code><i>&lt;port&gt;</i></p>
<dd> SNMP port; default port is 161</p>
<dt><code>-c </code><i>&lt;community_string&gt;</i></p>
<dd> SNMP community; default is public</p>
<dt><code>-v </code><i>&lt;version&gt;</i></p>
<dd> SNMP version (1,2); default is 1</p>
<dt><code>-r </code><i>&lt;retries&gt;</i></p>
<dd> request retries; default is 0</p>
<dt><code>-T </code><i>&lt;timeout&gt;</i></p>
<dd> force timeout in seconds; default is 20. Max is 60</p>
<dt><code>-w</code></p>
<dd> detect write access (separate action by enumeration)</p>
<dt><code>-d</code></p>
<dd> disable &#8216;TCP connections&#8217; enumeration! &quot;TCP connections enumeration&quot; can be very long. Use -d flag to disable it.</p>
<dt><code>-D</code></p>
<dd> enable debug</p>
<dt><code>-h</code></p>
<dd> show help menu </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-snmpwalk/">snmpwalk</a></code>(1), <code><a href="/docs/linux/man/1-snmpget/">snmpget</a></code>(1), <code><a href="/docs/linux/man/1-onesixtyone/">onesixtyone</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (c) 2005-2011 by Matteo Cantoni &lt;matteo.cantoni [at] nothink.org&gt; </p>
<h2>Index</h2>
