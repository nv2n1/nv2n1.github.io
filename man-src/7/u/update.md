---
title: "update(7)"
name: "update"
section: "7"
letter: "u"
url: "/docs/linux/man/7-update/"
description: "UPDATE – update rows of a table"
---

<p>UPDATE &#8211; update rows of a table </p>
<h2>Synopsis</h2>
<pre>UPDATE [ ONLY ] <i>table</i> [ [ AS ] <i>alias</i> ]
 SET { <i>column</i> = { <i>expression</i> | DEFAULT } |
 ( <i>column</i> [, ...] ) = ( { <i>expression</i> | DEFAULT } [, ...] ) } [, ...]
 [ FROM <i>fromlist</i> ]
 [ WHERE <i>condition</i> | WHERE CURRENT OF <i>cursor_name</i> ]
 [ RETURNING * | <i>output_expression</i> [ [ AS ] <i>output_name</i> ] [, ...] ]</pre>
<h2>Description</h2>
<p><code>UPDATE</code> changes the values of the specified columns in all rows that satisfy the condition. Only the columns to be modified need be mentioned in the SET clause; columns not explicitly modified retain their previous values. </p>
<p> By default, <code>UPDATE</code> will update rows in the specified table and all its subtables. If you wish to only update the specific table mentioned, you must use the ONLY clause. </p>
<p> There are two ways to modify a table using information contained in other tables in the database: using sub-selects, or specifying additional tables in the FROM clause. Which technique is more appropriate depends on the specific circumstances. </p>
<p> The optional RETURNING clause causes <code>UPDATE</code> to compute and return value(s) based on each row actually updated. Any expression using the table&#8217;s columns, and/or columns of other tables mentioned in FROM, can be computed. The new (post-update) values of the table&#8217;s columns are used. The syntax of the RETURNING list is identical to that of the output list of <code>SELECT</code>. </p>
<p> You must have the UPDATE privilege on the table, or at least on the column(s) that are listed to be updated. You must also have the SELECT privilege on any column whose values are read in the <i>expressions</i> or <i>condition</i>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of the table to update.</p>
<dt><i>alias</i></p>
<dd>A substitute name for the target table. When an alias is provided, it completely hides the actual name of the table. For example, given UPDATE foo AS f, the remainder of the <code>UPDATE</code> statement must refer to this table as f not foo.</p>
<dt><i>column</i></p>
<dd>The name of a column in <i>table</i>. The column name can be qualified with a subfield name or array subscript, if needed. Do not include the table&#8217;s name in the specification of a target column &#8212; for example, UPDATE tab SET tab.col = 1 is invalid.</p>
<dt><i>expression</i></p>
<dd>An expression to assign to the column. The expression can use the old values of this and other columns in the table.</p>
<dt><code>DEFAULT</code></p>
<dd>Set the column to its default value (which will be NULL if no specific default expression has been assigned to it).</p>
<dt><i>fromlist</i></p>
<dd>A list of table expressions, allowing columns from other tables to appear in the WHERE condition and the update expressions. This is similar to the list of tables that can be specified in the FROM Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] of a <code>SELECT</code> statement. Note that the target table must not appear in the <i>fromlist</i>, unless you intend a self-join (in which case it must appear with an alias in the <i>fromlist</i>).</p>
<dt><i>condition</i></p>
<dd>An expression that returns a value of type <code>boolean</code>. Only rows for which this expression returns true will be updated.</p>
<dt><i>cursor_name</i></p>
<dd>The name of the cursor to use in a WHERE CURRENT OF condition. The row to be updated is the one most recently fetched from this cursor. The cursor must be a non-grouping query on the <code>UPDATE</code>&#8216;s target table. Note that WHERE CURRENT OF cannot be specified together with a Boolean condition. See DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)] for more information about using cursors with WHERE CURRENT OF.</p>
<dt><i>output_expression</i></p>
<dd>An expression to be computed and returned by the <code>UPDATE</code> command after each row is updated. The expression can use any column names of the <i>table</i> or table(s) listed in FROM. Write * to return all columns.</p>
<dt><i>output_name</i></p>
<dd>A name to use for a returned column.</dl>
<h2>Outputs</h2>
<p>On successful completion, an <code>UPDATE</code> command returns a command tag of the form </p>
<pre>UPDATE <i>count</i></pre>
<p>The <i>count</i> is the number of rows updated. If <i>count</i> is 0, no rows matched the <i>condition</i> (this is not considered an error). </p>
<p> If the <code>UPDATE</code> command contains a RETURNING clause, the result will be similar to that of a <code>SELECT</code> statement containing the columns and values defined in the RETURNING list, computed over the row(s) updated by the command.</p>
<h2>Notes</h2>
<p>When a FROM clause is present, what essentially happens is that the target table is joined to the tables mentioned in the <i>fromlist</i>, and each output row of the join represents an update operation for the target table. When using FROM you should ensure that the join produces at most one output row for each row to be modified. In other words, a target row shouldn&#8217;t join to more than one row from the other table(s). If it does, then only one of the join rows will be used to update the target row, but which one will be used is not readily predictable. </p>
<p> Because of this indeterminacy, referencing other tables only within sub-selects is safer, though often harder to read and slower than using a join.</p>
<h2>Examples</h2>
<p>Change the word Drama to Dramatic in the column <code>kind</code> of the table <code>films</code>: </p>
<pre><code>UPDATE films SET kind = 'Dramatic' WHERE CURRENT OF c_films;</code></pre>
<p> Adjust temperature entries and reset precipitation to its default value in one row of the table <code>weather</code>: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Perform the same operation and return the updated entries: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Use the alternative column-list syntax to do the same update: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Increment the sales count of the salesperson who manages the account for Acme Corporation, using the FROM clause syntax: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Perform the same operation, using a sub-select in the WHERE clause: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Attempt to insert a new stock item along with the quantity of stock. If the item already exists, instead update the stock count of the existing item. To do this without failing the entire transaction, use savepoints: UPDATE films SET kind = &#8216;Dramatic&#8217; WHERE CURRENT OF c_films; Change the <code>kind</code> column of the table <code>films</code> in the row on which the cursor c_films is currently positioned: </p>
<pre><code>UPDATE films SET kind = 'Dramatic' WHERE CURRENT OF c_films;</code></pre>
<h2>Compatibility</h2>
<p>This command conforms to the SQL standard, except that the FROM and RETURNING clauses are PostgreSQL extensions. </p>
<p> According to the standard, the column-list syntax should allow a list of columns to be assigned from a single row-valued expression, such as a sub-select: </p>
<pre>UPDATE accounts SET (contact_last_name, contact_first_name) =
 (SELECT last_name, first_name FROM salesmen
 WHERE salesmen.id = accounts.sales_id);</pre>
<p>This is not currently implemented &#8212; the source must be a list of independent expressions. </p>
<p> Some other database systems offer a FROM option in which the target table is supposed to be listed again within FROM. That is not how PostgreSQL interprets FROM. Be careful when porting applications that use this extension.</p>
