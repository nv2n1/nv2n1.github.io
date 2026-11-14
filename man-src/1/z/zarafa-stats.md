---
title: "zarafa-stats(1)"
name: "zarafa-stats"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-stats/"
description: "zarafa-stats – Dump zarafa statistics tables."
---

<h2 class="name">NAME</h2>
<p> zarafa-stats &#8211; Dump zarafa statistics tables. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-stats</code> <i>TABLE</i></dl>
<h2>DESCRIPTION</h2>
<dd>This program dumps a statistics table that the zarafa-server program collects. The Zarafa server must be running for <code>zarafa-stats</code> to work. </p>
<p> If no table, or an invalid table is given, an error message is printed.</p>
<h2>TABLES</h2>
<p> There are four tables the zarafa-stats program can dump: </p>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Dump the system table. This table contains information about connections, SQL and cache statistics.</dl>
<p> <code>&#8211;session</code></p>
<dl>
<dt>
<dd> Dump the session table. This table contains information about user sessions and SOAP functions.</dl>
<p> <code>&#8211;users</code></p>
<dl>
<dt>
<dd> Dump the user table. This table contains information about users and user settings.</dl>
<p> <code>&#8211;company</code></p>
<dl>
<dt>
<dd> Dump the company table. This table contains information about companies and their properties. This table is only available on multi-tenancy enabled servers.</dl>
<p> <code>&#8211;servers</code></p>
<dl>
<dt>
<dd> Dump the servers table. This is only available in multiserver mode. Each server shows access methods and configured ports.</dl>
<p> <code>&#8211;top</code></p>
<dl>
<dt>
<dd> Shows a top-like view of all connected clients to the server, showing versions, users, programs, ip-adres, cpu-usage, and other statistical information. </p>
<p> Use 1-9 to enable/disable some columns. Use a-g to sort on a column, press the same letter again to reverse the sorting. Press &lt;ESC&gt; to quit the application.</dl>
<p> <code>&#8211;user</code>, <code>-u</code> <i>username</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server using this name in stead of SYSTEM.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-admin/">zarafa-admin</a></code>(1) </p>
<h2>Index</h2>
