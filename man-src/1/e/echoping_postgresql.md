---
title: "echoping_postgresql(1)"
name: "echoping_postgresql"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echoping_postgresql/"
description: "echoping_postgresql – echoping plugin which connects to a PostgreSQL RDBMS server"
---

<h2 class="name">NAME</h2>
<p> echoping_postgresql &#8211; echoping plugin which connects to a PostgreSQL RDBMS server </p>
<h2>SYNOPSIS</h2>
<p> <code>echoping</code> [echoping options] -m postgresql <code>hostname</code> [-c<i>conninfo]</i> [-e] [-r] [SQL-request]</p>
<h2>DESCRIPTION</h2>
<p> postgresql is an echoping plugin to connect to PostgreSQL RDBMS servers.</p>
<h2>ARGUMENTS</h2>
<p> <code>[SQL-request]</code> The request to the PostgreSQL server (in SQL). Only SELECT are supported. The default is &#8216;SELECT now()&#8217;.</p>
<dl>
<dt></dl>
<h2>OPTIONS</h2>
<dd>
<dl>
<dt><code>-c, &#8211;conninfo</code></p>
<dd> Connection information for the Postgresql server. Something like &#8216;dbname=bar&#8217;</p>
<dt><code>-r, &#8211;readall</code></p>
<dd> Read all the data sent by the Postgresql server</p>
<dt><code>-e, &#8211;connect-each-time</code></p>
<dd> (Re)connect to the Postgresql server at each iteration</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-echoping/">echoping</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> Stephane Bortzmeyer &lt;bortz [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
