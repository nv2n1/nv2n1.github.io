---
title: "zone2sqlite(1)"
name: "zone2sqlite"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zone2sqlite/"
description: "zone2sqlite – Load BIND 9 zone file into SQLite database"
---

<h2>NAME</h2>
<p> zone2sqlite &#8211; Load BIND 9 zone file into SQLite database</p>
<h2>SYNOPSIS</h2>
<p> <code>zone2sqlite zone zonefile dbfile dbtable</code></p>
<h2>DESCRIPTION</h2>
<p> zone2sqlite parses DNS zone file and creates database for use with SQLite BIND SDB driver. </p>
<p> <code>zone</code></p>
<dl>
<dt>
<dd> Zone origin, eg &quot;mydomain.net.&quot;</dl>
<p> <code>zonefile</code></p>
<dl>
<dt>
<dd> Master zone database file, eg. mydomain.net.zone</dl>
<p> <code>dbfile</code></p>
<dl>
<dt>
<dd> Name of SQLite database file</dl>
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
