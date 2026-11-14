---
title: "radzap(1)"
name: "radzap"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radzap/"
description: "radzap – remove rogue entries from the active sessions database"
---

<h2>NAME</h2>
<p> radzap &#8211; remove rogue entries from the active sessions database</p>
<h2>SYNOPSIS</h2>
<p> <code>radzap</code> [<code>-d</code> <i>raddb_directory</i>] [<code>-h</code>] [<code>-N</code> <i>nas_ip_address</i>] [<code>-P</code> <i>nas_port</i>] [<code>-u</code> <i>user</i>] [<code>-U</code> <i>user</i>] [<code>-x</code>] <i>server[:port] secret</i></p>
<h2>DESCRIPTION</h2>
<p> The FreeRadius server can be configured to maintain an active session database in a file called <i>radutmp</i>. Commands like <code><a href="/docs/linux/man/1-radwho/">radwho</a></code>(1) use this database. Sometimes that database can get out of sync, and then it might contain rogue entries. <code>radzap</code> can clean up this database. </p>
<p> As of FreeRADIUS 1.1.0, <code>radzap</code> is a simple shell-script wrapper around <code><a href="/docs/linux/man/1-radwho/">radwho</a></code>(1) and <code><a href="/docs/linux/man/1-radclient/">radclient</a></code>(1). </p>
<p> The sessions are &quot;zapped&quot; by sending an Accounting-Request packet which contains the information necessary for the server to delete the session record. <code>radzap</code> sends a packet to the server, rather than writing to <i>radutmp</i> directly, because session records may also be maintained in SQL.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d&nbsp;<wbr><i>raddb_directory</i></p>
<dd> The directory that contains the RADIUS configuration files. <code>radzap</code> reads <i>radiusd.conf</i> to determine the location of the <i>radutmp</i> file.</p>
<dt>-h</p>
<dd> Print usage help information.</p>
<dt>-N&nbsp;<wbr><i>nas_ip_address</i></p>
<dd> Zap the entries which match the given NAS IP address.</p>
<dt>-P&nbsp;<wbr><i>nas_port</i></p>
<dd> Zap the entries which match the given NAS port.</p>
<dt>-u&nbsp;<wbr><i>user</i></p>
<dd> Zap the entries which match the given username (case insensitive).</p>
<dt>-U&nbsp;<wbr><i>user</i></p>
<dd> Zap the entries which match the given username (case sensitive).</p>
<dt>-x</p>
<dd> Enable debugging output.</p>
<dt>server[:port]</p>
<dd> The hostname or IP address of the remote server. Optionally a UDP port can be specified. If no UDP port is specified, it is looked up in <i>/etc/services</i>. The service name looked for is <code>radacct</code> for accounting packets, and <code>radius</code> for all other requests. If a service is not found in <i>/etc/services</i>, 1813 and 1812 are used respectively.</p>
<dt>secret</p>
<dd> The shared secret for this client. It needs to be defined on the radius server side too, for the IP address you are sending the radius packets from.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-radwho/">radwho</a>(1), <a href="/docs/linux/man/1-radclient/">radclient</a>(1), <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5).</p>
<h2>AUTHOR</h2>
<p> Alan DeKok &lt;aland [at] ox.org&gt; </p>
<h2>Index</h2>
