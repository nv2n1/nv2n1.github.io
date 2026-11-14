---
title: "dblink_send_query(3)"
name: "dblink_send_query"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_send_query/"
description: "dblink_send_query – sends an async query to a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_send_query &#8211; sends an async query to a remote database </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_send_query(text connname, text sql) returns int
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_send_query</code> sends a query to be executed asynchronously, that is, without immediately waiting for the result. There must not be an async query already in progress on the connection. </p>
<p> After successfully dispatching an async query, completion status can be checked with <code>dblink_is_busy</code>, and the results are ultimately collected with <code>dblink_get_result</code>. It is also possible to attempt to cancel an active async query using <code>dblink_cancel_query</code>.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use.</dl>
<p> <i>sql</i></p>
<dl>
<dt>
<dd> The SQL statement that you wish to execute in the remote database, for example select * from pg_class.</dl>
<h2>RETURN VALUE</h2>
<p> Returns 1 if the query was successfully dispatched, 0 otherwise.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
SELECT dblink_send_query('dtest1', 'SELECT * FROM foo WHERE f1 &lt; 3');
</pre>
</dl>
<h2>Index</h2>
