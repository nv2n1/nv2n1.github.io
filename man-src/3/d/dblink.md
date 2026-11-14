---
title: "dblink(3)"
name: "dblink"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink/"
description: "dblink – executes a query in a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink &#8211; executes a query in a remote database </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink(text connname, text sql[, bool fail_on_error]) returns setof record
    dblink(text connstr, text sql[, bool fail_on_error]) returns setof record
    dblink(text sql[, bool fail_on_error]) returns setof record
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink</code> executes a query (usually a <code>SELECT</code>, but it can be any SQL statement that returns rows) in a remote database. </p>
<p> When two text arguments are given, the first one is first looked up as a persistent connection&#8217;s name; if found, the command is executed on that connection. If not found, the first argument is treated as a connection info string as for <code>dblink_connect</code>, and the indicated connection is made just for the duration of this command.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use; omit this parameter to use the unnamed connection.</dl>
<p> <i>connstr</i></p>
<dl>
<dt>
<dd> A connection info string, as previously described for <code>dblink_connect</code>.</dl>
<p> <i>sql</i></p>
<dl>
<dt>
<dd> The SQL query that you wish to execute in the remote database, for example select * from foo.</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function returns no rows.</dl>
<h2>RETURN VALUE</h2>
<p> The function returns the row(s) produced by the query. Since <code>dblink</code> can be used with any query, it is declared to return record, rather than specifying any particular set of columns. This means that you must specify the expected set of columns in the calling query &#8212; otherwise PostgreSQL would not know what to expect. Here is an example: </p>
<dl>
<dt>
<dd>
<pre>
SELECT *
    FROM dblink('dbname=mydb', 'select proname, prosrc from pg_proc')
      AS t1(proname name, prosrc text)
    WHERE proname LIKE 'bytea%';
</pre>
</dl>
<p> The &#8220;alias&#8221; part of the FROM clause must specify the column names and types that the function will return. (Specifying column names in an alias is actually standard SQL syntax, but specifying column types is a PostgreSQL extension.) This allows the system to understand what * should expand to, and what proname in the WHERE clause refers to, in advance of trying to execute the function. At run time, an error will be thrown if the actual query result from the remote database does not have the same number of columns shown in the FROM clause. The column names need not match, however, and <code>dblink</code> does not insist on exact type matches either. It will succeed so long as the returned data strings are valid input for the column type declared in the FROM clause.</p>
<h2>NOTES</h2>
<p> A convenient way to use <code>dblink</code> with predetermined queries is to create a view. This allows the column type information to be buried in the view, instead of having to spell it out in every query. For example, </p>
<dl>
<dt>
<dd>
CREATE VIEW myremote_pg_proc AS<br />
    SELECT *<br />
        FROM dblink(&#8216;dbname=postgres&#8217;, &#8216;select proname, prosrc from pg_proc&#8217;)<br />
            AS t1(proname name, prosrc text);<br />
SELECT *FROM myremote_pg_proc WHERE proname LIKE &#8216;bytea%&#8217;;
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT *FROM dblink('dbname=postgres', 'select proname, prosrc from pg_proc')
    AS t1(proname name, prosrc text) WHERE proname LIKE 'bytea%';
proname | prosrc-- -- -- -- -- --+-- -- -- -- -- --byteacat | byteacat byteaeq | byteaeq bytealt | bytealt byteale | byteale byteagt | byteagt byteage | byteage byteane | byteane byteacmp | byteacmp bytealike | bytealike byteanlike | byteanlike byteain | byteain byteaout | byteaout(12 rows) SELECT dblink_connect('dbname=postgres');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT *FROM dblink('select proname, prosrc from pg_proc')
        AS t1(proname name, prosrc text) WHERE proname LIKE 'bytea%';
proname | prosrc-- -- -- -- -- --+-- -- -- -- -- --byteacat | byteacat byteaeq | byteaeq bytealt | bytealt byteale | byteale byteagt | byteagt byteage | byteage byteane | byteane byteacmp | byteacmp bytealike | bytealike byteanlike | byteanlike byteain | byteain byteaout | byteaout(12 rows) SELECT dblink_connect('myconn', 'dbname=regression');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT *FROM dblink('myconn', 'select proname, prosrc from pg_proc')
        AS t1(proname name, prosrc text) WHERE proname LIKE 'bytea%';
proname | prosrc-- -- -- -- -- --+-- -- -- -- -- --bytearecv | bytearecv byteasend | byteasend byteale | byteale byteagt | byteagt byteage | byteage byteane | byteane byteacmp | byteacmp bytealike | bytealike byteanlike | byteanlike byteacat | byteacat byteaeq | byteaeq bytealt | bytealt byteain | byteain byteaout | byteaout(14 rows)
</code></pre>
</dl>
<h2>Index</h2>
