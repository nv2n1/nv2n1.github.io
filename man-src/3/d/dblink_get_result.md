---
title: "dblink_get_result(3)"
name: "dblink_get_result"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dblink_get_result/"
description: "dblink_get_result – gets an async query result"
---

<h2 class="name">NAME</h2>
<p> dblink_get_result &#8211; gets an async query result </p>
<h2>SYNOPSIS</h2>
<pre>
dblink_get_result(text connname [, bool fail_on_error]) returns setof record
</pre>
<h2>DESCRIPTION</h2>
<p> <code>dblink_get_result</code> collects the results of an asynchronous query previously sent with <code>dblink_send_query</code>. If the query is not already completed, <code>dblink_get_result</code> will wait until it is.</p>
<h2>ARGUMENTS</h2>
<p> <i>connname</i></p>
<dl>
<dt>
<dd> Name of the connection to use.</dl>
<p> <i>fail_on_error</i></p>
<dl>
<dt>
<dd> If true (the default when omitted) then an error thrown on the remote side of the connection causes an error to also be thrown locally. If false, the remote error is locally reported as a NOTICE, and the function returns no rows.</dl>
<h2>RETURN VALUE</h2>
<p> For an async query (that is, a SQL statement returning rows), the function returns the row(s) produced by the query. To use this function, you will need to specify the expected set of columns, as previously discussed for <code>dblink</code>. </p>
<p> For an async command (that is, a SQL statement not returning rows), the function returns a single row with a single text column containing the command&#8217;s status string. It is still necessary to specify that the result will have a single text column in the calling FROM clause.</p>
<h2>NOTES</h2>
<p> This function <i>must</i> be called if <code>dblink_send_query</code> returned 1. It must be called once for each query sent, and one additional time to obtain an empty set result, before the connection can be used again. </p>
<p> When using <code>dblink_send_query</code> and <code>dblink_get_result</code>, dblink fetches the entire remote query result before returning any of it to the local query processor. If the query returns a large number of rows, this can result in transient memory bloat in the local session. It may be better to open such a query as a cursor with <code>dblink_open</code> and then fetch a manageable number of rows at a time. Alternatively, use plain <code>dblink()</code>, which avoids memory bloat by spooling large result sets to disk.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
contrib_regression = #SELECT dblink_connect('dtest1', 'dbname=contrib_regression');
dblink_connect-- -- -- -- -- -- -- --OK(1 row)
    contrib_regression = #SELECT * FROM
                             contrib_regression
                         - #dblink_send_query('dtest1', 'select * from foo where f1 &lt; 3') AS t1;
t1-- --1(1 row)
    contrib_regression = #SELECT * FROM dblink_get_result('dtest1') AS t1(f1 int, f2 text, f3 text[]);
f1 | f2 | f3-- --+-- --+-- -- -- -- -- --0 | a |
{
    a0, b0, c0
}
1 | b |
{
    a1, b1, c1
}
2 | c | {a2, b2, c2}(3 rows)contrib_regression = #SELECT * FROM dblink_get_result('dtest1') AS t1(f1 int, f2 text, f3 text[]);
f1 | f2 | f3-- --+-- --+-- --(0 rows)contrib_regression = #SELECT * FROM
                                                              contrib_regression
                                                          - #dblink_send_query('dtest1', 'select * from foo where f1 &lt; 3; select * from foo where f1 &gt; 6') AS t1;
t1-- --1(1 row)
    contrib_regression = #SELECT * FROM dblink_get_result('dtest1') AS t1(f1 int, f2 text, f3 text[]);
f1 | f2 | f3-- --+-- --+-- -- -- -- -- --0 | a |
{
    a0, b0, c0
}
1 | b |
{
    a1, b1, c1
}
2 | c | {a2, b2, c2}(3 rows)contrib_regression = #SELECT * FROM dblink_get_result('dtest1') AS t1(f1 int, f2 text, f3 text[]);
f1 | f2 | f3-- --+-- --+-- -- -- -- -- -- -- -7 | h |
{
    a7, b7, c7
}
8 | i |
{
    a8, b8, c8
}
9 | j |
{
    a9, b9, c9
}
10 | k | {a10, b10, c10}(4 rows)contrib_regression = #SELECT * FROM dblink_get_result('dtest1') AS t1(f1 int, f2 text, f3 text[]);
f1 | f2 | f3-- --+-- --+-- --(0 rows)
</code></pre>
</dl>
<h2>Index</h2>
