---
title: "nutop(8)"
name: "nutop"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nutop/"
description: "nutop – display top NUFW Users"
---

<p>nutop &#8211; display top NUFW Users</p>
<h2>Synopsis</h2>
<p><code>nutop</code> [ <code>-help</code> ] [ <code>-c </code><i>config file</i> ] [ <code>-delay </code><i>refresh delay (seconds)</i> ] [ <code>-line </code><i>number of lines to display</i> ] [ <code>-databasetype </code><i> mysql/pgsql</i> ] [ <code>-host </code><i>db host</i> ] [ <code>-user </code><i>db username</i> ] [ <code>-pass </code><i>db password</i> ] [ <code>-databasename </code><i>db database name</i> ] [ <code>-tablename </code><i>db table</i> ] [ <code>-port </code><i>db port</i> ] </p>
<h2>Description</h2>
<p>This manual page documents the <code>nutop</code> command. </p>
<p> Nutop is to be used by administrators willing to view users activity on a NuFW server, in real time. The display is designed to look a lot like the well known top command, as far as general layout is concerned. </p>
<p> The default configuration file (containing SQL connections parameters) is located at /etc/nufw/nutop.conf. If decided to customize it to their needs, care should be taken about file permissions on that file, as it might let any user of the system access to the NuFW connection tracking database. </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-help </code></p>
<dd>Issues usage details and exits.</p>
<dt><code>-c </code><i>config file</i></p>
<dd>Specifies config file to read SQL parameters from. Default is /etc/nufw/nutop.conf</p>
<dt><code>-delay </code><i>number</i></p>
<dd>Specifies a rate to refresh display. This parameter is interpeted as a number of seconds. Default is 2s.</p>
<dt><code>-line </code><i>number</i></p>
<dd>Number of lines to display. Default : 20</p>
<dt><code>-databasetype </code><i>mysql/pgsql</i></p>
<dd>Type of database to connect to. Default is mysql. This setting also sets the default port setting.</p>
<dt><code>-host </code><i>hostname/IP</i></p>
<dd>IP address or FQDN of database we connect to. Default value : 127.0.0.1</p>
<dt><code>-user </code><i>username</i></p>
<dd>Database username to connect as. Default is &quot;nutop&quot;</p>
<dt><code>-pass </code><i>password</i></p>
<dd>Password to use to connect to database.</p>
<dt><code>-databasename </code><i>name of database</i></p>
<dd>Name of database we connect to. Default is &quot;nulog&quot;</p>
<dt><code>-tablename </code><i>name of table</i></p>
<dd>Name of SQL table to use for queries. Default is &quot;ulog&quot;</p>
<dt><code>-port </code><i>TCP port</i></p>
<dd>TCP numeric port to use for database connection. Default is 3306 if databasetype is mysql, 5432 if pgsql.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nuauth/">nuauth</a>(8), <a href="/docs/linux/man/8-nufw/">nufw</a>(8)</p>
<h2>Author</h2>
<p>Nufw was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] inl.fr&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] inl.fr&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Vincent Deffontaines </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
