---
title: "dblink_build_sql_delete(3)"
name: "dblink_build_sql_delete"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_build_sql_delete/"
description: "dblink_build_sql_delete – builds a DELETE statement using supplied values for primary key field values"
---

<h2 class="name">NAME</h2>
<p> dblink_build_sql_delete &#8211; builds a DELETE statement using supplied values for primary key field values </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_build_sql_delete(text relname,
                        int2vector primary_key_attnums,
                        integer num_primary_key_atts,
                        text[] tgt_pk_att_vals_array) returns text
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_build_sql_delete</code> can be useful in doing selective replication of a local table to a remote database. It builds a SQL <code>DELETE</code> command that will delete the row with the given primary key values.</p>
<h2>ARGUMENTS</h2>
<p> <i>relname</i></p>
<dl>
<dt>
<dd> Name of a local relation, for example foo or myschema.mytab. Include double quotes if the name is mixed-case or contains special characters, for example &quot;FooBar&quot;; without quotes, the string will be folded to lower case.</dl>
<p> <i>primary_key_attnums</i></p>
<dl>
<dt>
<dd> Attribute numbers (1-based) of the primary key fields, for example 1 2.</dl>
<p> <i>num_primary_key_atts</i></p>
<dl>
<dt>
<dd> The number of primary key fields.</dl>
<p> <i>tgt_pk_att_vals_array</i></p>
<dl>
<dt>
<dd> Values of the primary key fields to be used in the resulting <code>DELETE</code> command. Each field is represented in text form.</dl>
<h2>RETURN VALUE</h2>
<p> Returns the requested SQL statement as text.</p>
<h2>NOTES</h2>
<p> As of PostgreSQL 9.0, the attribute numbers in <i>primary_key_attnums</i> are interpreted as logical column numbers, corresponding to the column&#8217;s position in SELECT * FROM relname. Previous versions interpreted the numbers as physical column positions. There is a difference if any column(s) to the left of the indicated column have been dropped during the lifetime of the table.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_build_sql_delete('"MyFoo"', '1 2', 2, '{"1", "b"}');
dblink_build_sql_delete-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -DELETE FROM "MyFoo" WHERE f1 = '1' AND f2 = 'b'(1 row)
</code></pre>
</dl>
<h2>Index</h2>
