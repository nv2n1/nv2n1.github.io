---
title: "zonetodb(1)"
name: "zonetodb"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zonetodb/"
description: "zonetodb – Generate a PostgreSQL table from a zone."
---

<h2>NAME</h2>
<p> zonetodb &#8211; Generate a PostgreSQL table from a zone.</p>
<h2>SYNOPSIS</h2>
<p> <code>zonetodb origin file dbname dbtable</code></p>
<h2>DESCRIPTION</h2>
<p> zonetodb parses DNS zone file and creates table in selected database for use with PostgreSQL BIND SDB driver. </p>
<p> <code>zone</code></p>
<dl>
<dt>
<dd> Zone origin, eg &quot;pgdb.net.&quot;</dl>
<p> <code>file</code></p>
<dl>
<dt>
<dd> Master zone database file, eg. pgdb.net.db</dl>
<p> <code>dbname</code></p>
<dl>
<dt>
<dd> Name of PostgreSQL database (database must exist)</dl>
<p> <code>dbtable</code></p>
<dl>
<dt>
<dd> Name of table in database</dl>
<h2>EXIT STATUS</h2>
<p> Exits with 0 on success or 1 on failure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-named/">named</a>(8)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007-2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
