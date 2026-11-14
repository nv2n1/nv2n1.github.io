---
title: "dblink_get_connections(3)"
name: "dblink_get_connections"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_get_connections/"
description: "dblink_get_connections – returns the names of all open named dblink connections"
---

<h2 class="name">NAME</h2>
<p> dblink_get_connections &#8211; returns the names of all open named dblink connections </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_get_connections() returns text[]
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_get_connections</code> returns an array of the names of all open named dblink connections.</p>
<h2>RETURN VALUE</h2>
<p> Returns a text array of connection names, or NULL if none.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
SELECT dblink_get_connections();
</pre>
</dl>
<h2>Index</h2>
