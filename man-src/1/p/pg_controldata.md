---
title: "pg_controldata(1)"
name: "pg_controldata"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_controldata/"
description: "pg_controldata – display control information of a PostgreSQL database cluster"
---

<h2 class="name">NAME</h2>
<p> pg_controldata &#8211; display control information of a PostgreSQL database cluster </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_controldata</code> [<i>option</i>] [<i>datadir</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pg_controldata</code></p>
<dd>prints information initialized during <code>initdb</code>, such as the catalog version. It also shows information about write-ahead logging and checkpoint processing. This information is cluster-wide, and not specific to any one database. </p>
<p> This utility can only be run by the user who initialized the cluster because it requires read access to the data directory. You can specify the data directory on the command line, or use the environment variable <code>PGDATA</code>. This utility supports the options <code>-V</code> and <code>&#8211;version</code>, which print the pg_controldata version and exit. It also supports options <code>-?</code> and <code>&#8211;help</code>, which output the supported arguments.</p>
<h2>ENVIRONMENT</h2>
<p> <code>PGDATA</code></p>
<dl>
<dt>
<dd> Default data directory location</dl>
<h2>Index</h2>
