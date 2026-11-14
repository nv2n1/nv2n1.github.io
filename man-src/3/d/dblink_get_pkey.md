---
title: "dblink_get_pkey(3)"
name: "dblink_get_pkey"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_get_pkey/"
description: "dblink_get_pkey – returns the positions and field names of a relation’s primary key fields"
---

<h2 class="name">NAME</h2>
<p> dblink_get_pkey &#8211; returns the positions and field names of a relation&#8217;s primary key fields </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_get_pkey(text relname) returns setof dblink_pkey_results
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_get_pkey</code> provides information about the primary key of a relation in the local database. This is sometimes useful in generating queries to be sent to remote databases.</p>
<h2>ARGUMENTS</h2>
<p> <i>relname</i></p>
<dl>
<dt>
<dd> Name of a local relation, for example foo or myschema.mytab. Include double quotes if the name is mixed-case or contains special characters, for example &quot;FooBar&quot;; without quotes, the string will be folded to lower case.</dl>
<h2>RETURN VALUE</h2>
<p> Returns one row for each primary key field, or no rows if the relation has no primary key. The result row type is defined as </p>
<dl>
<dt>
<dd>
<pre><code>
CREATE TYPE dblink_pkey_results AS(position int, colname text);
</code></pre>
</dl>
<p> The position column simply runs from 1 to <i>N</i>; it is the number of the field within the primary key, not the number within the table&#8217;s columns.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
CREATE TABLE foobar(
    f1 int,
    f2 int,
    f3 int,
    PRIMARY KEY(f1, f2, f3));
CREATE TABLE
    SELECT *FROM dblink_get_pkey('foobar');
position | colname-- -- -- -- --+-- -- -- -- -1 | f1 2 | f2 3 | f3(3 rows)
</code></pre>
</dl>
<h2>Index</h2>
