---
title: "dblink_fetch(3)"
name: "dblink_fetch"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_fetch/"
description: "dblink_fetch – returns rows from an open cursor in a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_fetch &#8211; returns rows from an open cursor in a remote database </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink_fetch(text cursorname, int howmany[, bool fail_on_error]) returns setof record
    dblink_fetch(text connname, text cursorname, int howmany[, bool fail_on_error]) returns setof record
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_fetch</code> fetches rows from a cursor previously established by <code>dblink_open</code>.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use; omit this parameter to use the unnamed connection.</dl>
<p> <i>cursorname</i></p>
<dl>
<dt>
<dd> The name of the cursor to fetch from.</dl>
<p> <i>howmany</i></p>
<dl>
<dt>
<dd> The maximum number of rows to retrieve. The next <i>howmany</i> rows are fetched, starting at the current cursor position, moving forward. Once the cursor has reached its end, no more rows are produced.</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function returns no rows.</dl>
<h2>RETURN VALUE</h2>
<p> The function returns the row(s) fetched from the cursor. To use this function, you will need to specify the expected set of columns, as previously discussed for <code>dblink</code>.</p>
<h2>NOTES</h2>
<p> On a mismatch between the number of return columns specified in the FROM clause, and the actual number of columns returned by the remote cursor, an error will be thrown. In this event, the remote cursor is still advanced by as many rows as it would have been if the error had not occurred. The same is true for any other error occurring in the local query after the remote <code>FETCH</code> has been done.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_connect('dbname=postgres');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_open('foo', 'select proname, prosrc from pg_proc where proname like ' 'bytea%''');
dblink_open-- -- -- -- -- -- -OK(1 row)
    SELECT *FROM dblink_fetch('foo', 5) AS(funcname name, source text);
funcname | source-- -- -- -- --+-- -- -- -- --byteacat | byteacat byteacmp | byteacmp byteaeq | byteaeq byteage | byteage byteagt | byteagt(5 rows) SELECT *FROM dblink_fetch('foo', 5) AS(funcname name, source text);
funcname | source-- -- -- -- -- -+-- -- -- -- -- -byteain | byteain byteale | byteale bytealike | bytealike bytealt | bytealt byteane | byteane(5 rows) SELECT *FROM dblink_fetch('foo', 5) AS(funcname name, source text);
funcname | source-- -- -- -- -- --+-- -- -- -- -- --byteanlike | byteanlike byteaout | byteaout(2 rows) SELECT *FROM dblink_fetch('foo', 5) AS(funcname name, source text);
funcname | source-- -- -- -- --+-- -- -- --(0 rows)
</code></pre>
</dl>
<h2>Index</h2>
