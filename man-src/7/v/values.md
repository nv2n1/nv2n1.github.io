---
title: "values(7)"
name: "values"
section: "7"
letter: "v"
url: "/docs/linux/man/7-values/"
description: "VALUES – compute a set of rows"
---

<p>VALUES &#8211; compute a set of rows </p>
<h2>Synopsis</h2>
<pre>VALUES ( <i>expression</i> [, ...] ) [, ...]
 [ ORDER BY <i>sort_expression</i> [ ASC | DESC | USING <i>operator</i> ] [, ...] ]
 [ LIMIT { <i>count</i> | ALL } ]
 [ OFFSET <i>start</i> [ ROW | ROWS ] ]
 [ FETCH { FIRST | NEXT } [ <i>count</i> ] { ROW | ROWS } ONLY ]</pre>
<h2>Description</h2>
<p><code>VALUES</code> computes a row value or set of row values specified by value expressions. It is most commonly used to generate a &#8220;constant table&#8221; within a larger command, but it can be used on its own. </p>
<p> When more than one row is specified, all the rows must have the same number of elements. The data types of the resulting table&#8217;s columns are determined by combining the explicit or inferred types of the expressions appearing in that column, using the same rules as for UNION (see in the documentation). </p>
<p> Within larger commands, <code>VALUES</code> is syntactically allowed anywhere that <code>SELECT</code> is. Because it is treated like a <code>SELECT</code> by the grammar, it is possible to use the ORDER BY, LIMIT (or equivalently FETCH FIRST), and OFFSET clauses with a <code>VALUES</code> command.</p>
<h2>Parameters</h2>
<dl>
<dt><i>expression</i></p>
<dd>A constant or expression to compute and insert at the indicated place in the resulting table (set of rows). In a <code>VALUES</code> list appearing at the top level of an <code>INSERT</code>, an <i>expression</i> can be replaced by DEFAULT to indicate that the destination column&#8217;s default value should be inserted. DEFAULT cannot be used when <code>VALUES</code> appears in other contexts.</p>
<dt><i>sort_expression</i></p>
<dd>An expression or integer constant indicating how to sort the result rows. This expression can refer to the columns of the <code>VALUES</code> result as column1, column2, etc. For more details see ORDER BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
<dt><i>operator</i></p>
<dd>A sorting operator. For details see ORDER BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
<dt><i>count</i></p>
<dd>The maximum number of rows to return. For details see LIMIT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
<dt><i>start</i></p>
<dd>The number of rows to skip before starting to return rows. For details see LIMIT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</dl>
<h2>Notes</h2>
<p><code>VALUES</code> lists with very large numbers of rows should be avoided, as you might encounter out-of-memory failures or poor performance. <code>VALUES</code> appearing within <code>INSERT</code> is a special case (because the desired column types are known from the <code>INSERT</code>&#8216;s target table, and need not be inferred by scanning the <code>VALUES</code> list), so it can handle larger lists than are practical in other contexts.</p>
<h2>Examples</h2>
<p>A bare <code>VALUES</code> command: </p>
<pre>VALUES (1, 'one'), (2, 'two'), (3, 'three');</pre>
<p>This will return a table of two columns and three rows. It&#8217;s effectively equivalent to: </p>
<pre>SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';</pre>
<p>More usually, <code>VALUES</code> is used within a larger SQL command. The most common use is in <code>INSERT</code>: </p>
<pre>INSERT INTO films (code, title, did, date_prod, kind)
 VALUES ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');</pre>
<p>In the context of <code>INSERT</code>, entries of a <code>VALUES</code> list can be DEFAULT to indicate that the column default should be used here instead of specifying a value: </p>
<pre>INSERT INTO films VALUES
 ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 minutes'),
 ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama', DEFAULT);</pre>
<p><code>VALUES</code> can also be used where a sub-<code>SELECT</code> might be written, for example in a FROM clause: </p>
<pre>SELECT f.*
 FROM films f, (VALUES('MGM', 'Horror'), ('UA', 'Sci-Fi')) AS t (studio, kind)
 WHERE f.studio = t.studio AND f.kind = t.kind;
UPDATE employees SET salary = salary * v.increase
 FROM (VALUES(1, 200000, 1.2), (2, 400000, 1.4)) AS v (depno, target, increase)
 WHERE employees.depno = v.depno AND employees.sales &gt;= v.target;</pre>
<p>Note that an AS clause is required when <code>VALUES</code> is used in a FROM clause, just as is true for <code>SELECT</code>. It is not required that the AS clause specify names for all the columns, but it&#8217;s good practice to do so. (The default column names for <code>VALUES</code> are column1, column2, etc in PostgreSQL, but these names might be different in other database systems.) When <code>VALUES</code> is used in <code>INSERT</code>, the values are all automatically coerced to the data type of the corresponding destination column. When it&#8217;s used in other contexts, it might be necessary to specify the correct data type. If the entries are all quoted literal constants, coercing the first is sufficient to determine the assumed type for all: </p>
<pre>SELECT * FROM machines
WHERE ip_address IN (VALUES('192.168.0.1'::inet), ('192.168.0.10'), ('192.168.1.43'));</pre>
<dl>
<dd><code>Tip:</code> For simple IN tests, it&#8217;s better to rely on the list-of-scalars form of IN than to write a <code>VALUES</code> query as shown above. The list of scalars method requires less writing and is often more efficient.</dl>
<h2>Compatibility</h2>
<p><code>VALUES</code> conforms to the SQL standard. LIMIT and OFFSET are PostgreSQL extensions; see also under SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
<h2>See Also</h2>
<p>INSERT [<code><a href="/docs/linux/man/7-insert/">insert</a></code>(7)], SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] </p>
