---
title: "dblink_exec(3)"
name: "dblink_exec"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_exec/"
description: "dblink_exec – executes a command in a remote database"
---

<h2 class="name">NAME</h2>
<p> dblink_exec &#8211; executes a command in a remote database </p>
<h2>SYNOPSIS</h2>
<pre><code>
dblink_exec(text connname, text sql[, bool fail_on_error]) returns text
    dblink_exec(text connstr, text sql[, bool fail_on_error]) returns text
    dblink_exec(text sql[, bool fail_on_error]) returns text
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_exec</code> executes a command (that is, any SQL statement that doesn&#8217;t return rows) in a remote database. </p>
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
<dd> The SQL command that you wish to execute in the remote database, for example insert into foo values(0,&#8217;a&#8217;,'{&quot;a0&quot;,&quot;b0&quot;,&quot;c0&quot;}&#8217;).</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function&#8217;s return value is set to ERROR.</dl>
<h2>RETURN VALUE</h2>
<p> Returns status, either the command&#8217;s status string or ERROR.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
SELECT dblink_connect('dbname=dblink_test_standby');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_exec('insert into foo values(21,' 'z' ',' '{"a0","b0","c0"}' ');');
dblink_exec-- -- -- -- -- -- -- -- -INSERT 943366 1(1 row)
    SELECT dblink_connect('myconn', 'dbname=regression');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    SELECT dblink_exec('myconn', 'insert into foo values(21,' 'z' ',' '{"a0","b0","c0"}' ');');
dblink_exec-- -- -- -- -- -- -- -- --INSERT 6432584 1(1 row)
    SELECT dblink_exec('myconn', 'insert into pg_class values (' 'foo' ')', false);
NOTICE : sql error
             DETAIL : ERROR : null value in column "relnamespace" violates not -null constraint
                                  dblink_exec-- -- -- -- -- -- -ERROR(1 row)
</code></pre>
</dl>
<h2>Index</h2>
