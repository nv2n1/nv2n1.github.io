---
title: "dblink_open(3)"
name: "dblink_open"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_open/"
description: "dblink_open – opens a cursor in a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_open &#8211; opens a cursor in a remote database </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink_open(text cursorname, text sql[, bool fail_on_error]) returns text
    dblink_open(text connname, text cursorname, text sql[, bool fail_on_error]) returns text
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_open()</code> opens a cursor in a remote database. The cursor can subsequently be manipulated with <code>dblink_fetch()</code> and <code>dblink_close()</code>.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use; omit this parameter to use the unnamed connection.</dl>
<p> <i>cursorname</i></p>
<dl>
<dt>
<dd> The name to assign to this cursor.</dl>
<p> <i>sql</i></p>
<dl>
<dt>
<dd> The <code>SELECT</code> statement that you wish to execute in the remote database, for example select * from pg_class.</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function&#8217;s return value is set to ERROR.</dl>
<h2>RETURN VALUE</h2>
<p> Returns status, either OK or ERROR.</p>
<h2>NOTES</h2>
<p> Since a cursor can only persist within a transaction, <code>dblink_open</code> starts an explicit transaction block (<code>BEGIN</code>) on the remote side, if the remote side was not already within a transaction. This transaction will be closed again when the matching <code>dblink_close</code> is executed. Note that if you use <code>dblink_exec</code> to change data between <code>dblink_open</code> and <code>dblink_close</code>, and then an error occurs or you use <code>dblink_disconnect</code> before <code>dblink_close</code>, your change <i>will be lost</i> because the transaction will be aborted.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_connect('dbname=postgres');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_open('foo', 'select proname, prosrc from pg_proc');
dblink_open-- -- -- -- -- -- -OK(1 row)
</code></pre>
</dl>
<h2>Index</h2>
