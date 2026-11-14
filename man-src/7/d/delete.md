---
title: "delete(7)"
name: "delete"
section: "7"
letter: "d"
url: "/docs/linux/man/7-delete/"
description: "DELETE – delete rows of a table"
---

<p>DELETE &#8211; delete rows of a table </p>
<h2>Synopsis</h2>
<pre>DELETE FROM [ ONLY ] <i>table</i> [ [ AS ] <i>alias</i> ]
 [ USING <i>usinglist</i> ]
 [ WHERE <i>condition</i> | WHERE CURRENT OF <i>cursor_name</i> ]
 [ RETURNING * | <i>output_expression</i> [ [ AS ] <i>output_name</i> ] [, ...] ]</pre>
<h2>Description</h2>
<p><code>DELETE</code> deletes rows that satisfy the WHERE clause from the specified table. If the WHERE clause is absent, the effect is to delete all rows in the table. The result is a valid, but empty table. </p>
<dl>
<dd><code>Tip:</code> TRUNCATE [<code><a href="/docs/linux/man/7-truncate/">truncate</a></code>(7)] is a PostgreSQL extension that provides a faster mechanism to remove all rows from a table.</dl>
<p> By default, <code>DELETE</code> will delete rows in the specified table and all its child tables. If you wish to delete only from the specific table mentioned, you must use the ONLY clause. </p>
<p> There are two ways to delete rows in a table using information contained in other tables in the database: using sub-selects, or specifying additional tables in the USING clause. Which technique is more appropriate depends on the specific circumstances. </p>
<p> The optional RETURNING clause causes <code>DELETE</code> to compute and return value(s) based on each row actually deleted. Any expression using the table&#8217;s columns, and/or columns of other tables mentioned in USING, can be computed. The syntax of the RETURNING list is identical to that of the output list of <code>SELECT</code>. </p>
<p> You must have the DELETE privilege on the table to delete from it, as well as the SELECT privilege for any table in the USING clause or whose values are read in the <i>condition</i>.</p>
<h2>Parameters</h2>
<dl>
<dt><code>ONLY</code></p>
<dd>If specified, delete rows from the named table only. When not specified, any tables inheriting from the named table are also processed.</p>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of an existing table.</p>
<dt><i>alias</i></p>
<dd>A substitute name for the target table. When an alias is provided, it completely hides the actual name of the table. For example, given DELETE FROM foo AS f, the remainder of the <code>DELETE</code> statement must refer to this table as f not foo.</p>
<dt><i>usinglist</i></p>
<dd>A list of table expressions, allowing columns from other tables to appear in the WHERE condition. This is similar to the list of tables that can be specified in the FROM Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] of a <code>SELECT</code> statement; for example, an alias for the table name can be specified. Do not repeat the target table in the <i>usinglist</i>, unless you wish to set up a self-join.</p>
<dt><i>condition</i></p>
<dd>An expression that returns a value of type <code>boolean</code>. Only rows for which this expression returns true will be deleted.</p>
<dt><i>cursor_name</i></p>
<dd>The name of the cursor to use in a WHERE CURRENT OF condition. The row to be deleted is the one most recently fetched from this cursor. The cursor must be a non-grouping query on the <code>DELETE</code>&#8216;s target table. Note that WHERE CURRENT OF cannot be specified together with a Boolean condition. See DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)] for more information about using cursors with WHERE CURRENT OF.</p>
<dt><i>output_expression</i></p>
<dd>An expression to be computed and returned by the <code>DELETE</code> command after each row is deleted. The expression can use any column names of the <i>table</i> or table(s) listed in USING. Write * to return all columns.</p>
<dt><i>output_name</i></p>
<dd>A name to use for a returned column.</dl>
<h2>Outputs</h2>
<p>On successful completion, a <code>DELETE</code> command returns a command tag of the form </p>
<pre>DELETE <i>count</i></pre>
<p>The <i>count</i> is the number of rows deleted. If <i>count</i> is 0, no rows matched the <i>condition</i> (this is not considered an error). </p>
<p> If the <code>DELETE</code> command contains a RETURNING clause, the result will be similar to that of a <code>SELECT</code> statement containing the columns and values defined in the RETURNING list, computed over the row(s) deleted by the command.</p>
<h2>Notes</h2>
<p>PostgreSQL lets you reference columns of other tables in the WHERE condition by specifying the other tables in the USING clause. For example, to delete all films produced by a given producer, one can do: </p>
<pre>DELETE FROM films USING producers
 WHERE producer_id = producers.id AND producers.name = 'foo';</pre>
<p>What is essentially happening here is a join between <code>films</code> and <code>producers</code>, with all successfully joined <code>films</code> rows being marked for deletion. This syntax is not standard. A more standard way to do it is: </p>
<pre>DELETE FROM films
 WHERE producer_id IN (SELECT id FROM producers WHERE name = 'foo');</pre>
<p>In some cases the join style is easier to write or faster to execute than the sub-select style.</p>
<h2>Examples</h2>
<p>Delete all films but musicals: </p>
<pre>DELETE FROM films WHERE kind &lt;&gt; 'Musical';</pre>
<p>Clear the table films: </p>
<pre>DELETE FROM films;</pre>
<p>Delete completed tasks, returning full details of the deleted rows: </p>
<pre><code>DELETE FROM tasks WHERE status = 'DONE' RETURNING *;</code></pre>
<p> Delete the row of <code>tasks</code> on which the cursor c_tasks is currently positioned: </p>
<pre>DELETE FROM tasks WHERE CURRENT OF c_tasks;</pre>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard, except that the USING and RETURNING clauses are PostgreSQL extensions.</p>
