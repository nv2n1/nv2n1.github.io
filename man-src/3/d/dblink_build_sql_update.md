---
title: "dblink_build_sql_update(3)"
name: "dblink_build_sql_update"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_build_sql_update/"
description: "dblink_build_sql_update – builds an UPDATE statement using a local tuple, replacing the primary key field values with alternative supplied values"
---

<h2 class="name">NAME</h2>
<p> dblink_build_sql_update &#8211; builds an UPDATE statement using a local tuple, replacing the primary key field values with alternative supplied values </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink_build_sql_update(text relname,
                        int2vector primary_key_attnums,
                        integer num_primary_key_atts,
                        text[] src_pk_att_vals_array,
                        text[] tgt_pk_att_vals_array) returns text
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_build_sql_update</code> can be useful in doing selective replication of a local table to a remote database. It selects a row from the local table based on primary key, and then builds a SQL <code>UPDATE</code> command that will duplicate that row, but with the primary key values replaced by the values in the last argument. (To make an exact copy of the row, just specify the same values for the last two arguments.) The <code>UPDATE</code> command always assigns all fields of the row &#8212; the main difference between this and <code>dblink_build_sql_insert</code> is that it&#8217;s assumed that the target row already exists in the remote table.</p>
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
<p> <i>src_pk_att_vals_array</i></p>
<dl>
<dt>
<dd> Values of the primary key fields to be used to look up the local tuple. Each field is represented in text form. An error is thrown if there is no local row with these primary key values.</dl>
<p> <i>tgt_pk_att_vals_array</i></p>
<dl>
<dt>
<dd> Values of the primary key fields to be placed in the resulting <code>UPDATE</code> command. Each field is represented in text form.</dl>
<h2>RETURN VALUE</h2>
<p> Returns the requested SQL statement as text.</p>
<h2>NOTES</h2>
<p> As of PostgreSQL 9.0, the attribute numbers in <i>primary_key_attnums</i> are interpreted as logical column numbers, corresponding to the column&#8217;s position in SELECT * FROM relname. Previous versions interpreted the numbers as physical column positions. There is a difference if any column(s) to the left of the indicated column have been dropped during the lifetime of the table.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_build_sql_update('foo', '1 2', 2, '{"1", "a"}', '{"1", "b"}');
dblink_build_sql_update-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -UPDATE foo SET f1 = '1', f2 = 'b', f3 = '1' WHERE f1 = '1' AND f2 = 'b'(1 row)
</code></pre>
</dl>
<h2>Index</h2>
