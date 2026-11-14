---
title: "insert(7)"
name: "insert"
section: "7"
letter: "i"
url: "/docs/linux/man/7-insert/"
description: "INSERT – create new rows in a table"
---

<p>INSERT &#8211; create new rows in a table </p>
<h2>Synopsis</h2>
<pre>INSERT INTO <i>table</i> [ ( <i>column</i> [, ...] ) ]
 { DEFAULT VALUES | VALUES ( { <i>expression</i> | DEFAULT } [, ...] ) [, ...] | <i>query</i> }
 [ RETURNING * | <i>output_expression</i> [ [ AS ] <i>output_name</i> ] [, ...] ]</pre>
<h2>Description</h2>
<p><code>INSERT</code> inserts new rows into a table. One can insert one or more rows specified by value expressions, or zero or more rows resulting from a query. </p>
<p> The target column names can be listed in any order. If no list of column names is given at all, the default is all the columns of the table in their declared order; or the first <i>N</i> column names, if there are only <i>N</i> columns supplied by the VALUES clause or <i>query</i>. The values supplied by the VALUES clause or <i>query</i> are associated with the explicit or implicit column list left-to-right. </p>
<p> Each column not present in the explicit or implicit column list will be filled with a default value, either its declared default value or null if there is none. </p>
<p> If the expression for any column is not of the correct data type, automatic type conversion will be attempted. </p>
<p> The optional RETURNING clause causes <code>INSERT</code> to compute and return value(s) based on each row actually inserted. This is primarily useful for obtaining values that were supplied by defaults, such as a serial sequence number. However, any expression using the table&#8217;s columns is allowed. The syntax of the RETURNING list is identical to that of the output list of <code>SELECT</code>. </p>
<p> You must have INSERT privilege on a table in order to insert into it. If a column list is specified, you only need INSERT privilege on the listed columns. Use of the RETURNING clause requires SELECT privilege on all columns mentioned in RETURNING. If you use the <i>query</i> clause to insert rows from a query, you of course need to have SELECT privilege on any table or column used in the query.</p>
<h2>Parameters</h2>
<dl>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of an existing table.</p>
<dt><i>column</i></p>
<dd>The name of a column in <i>table</i>. The column name can be qualified with a subfield name or array subscript, if needed. (Inserting into only some fields of a composite column leaves the other fields null.)</p>
<dt><code>DEFAULT VALUES</code></p>
<dd>All columns will be filled with their default values.</p>
<dt><i>expression</i></p>
<dd>An expression or value to assign to the corresponding <i>column</i>.</p>
<dt><code>DEFAULT</code></p>
<dd>The corresponding <i>column</i> will be filled with its default value.</p>
<dt><i>query</i></p>
<dd>A query (<code>SELECT</code> statement) that supplies the rows to be inserted. Refer to the SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] statement for a description of the syntax.</p>
<dt><i>output_expression</i></p>
<dd>An expression to be computed and returned by the <code>INSERT</code> command after each row is inserted. The expression can use any column names of the <i>table</i>. Write * to return all columns of the inserted row(s).</p>
<dt><i>output_name</i></p>
<dd>A name to use for a returned column.</dl>
<h2>Outputs</h2>
<p>On successful completion, an <code>INSERT</code> command returns a command tag of the form </p>
<pre>INSERT <i>oid</i> <i>count</i></pre>
<p>The <i>count</i> is the number of rows inserted. If <i>count</i> is exactly one, and the target table has OIDs, then <i>oid</i> is the OID assigned to the inserted row. Otherwise <i>oid</i> is zero. </p>
<p> If the <code>INSERT</code> command contains a RETURNING clause, the result will be similar to that of a <code>SELECT</code> statement containing the columns and values defined in the RETURNING list, computed over the row(s) inserted by the command.</p>
<h2>Examples</h2>
<p>Insert a single row into table films: </p>
<pre>INSERT INTO films VALUES
 ('UA502', 'Bananas', 105, '1971-07-13', 'Comedy', '82 minutes');</pre>
<p>In this example, the len column is omitted and therefore it will have the default value: </p>
<pre>INSERT INTO films (code, title, did, date_prod, kind)
 VALUES ('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');</pre>
<p>This example uses the DEFAULT clause for the date columns rather than specifying a value: </p>
<pre>INSERT INTO films VALUES
 ('UA502', 'Bananas', 105, DEFAULT, 'Comedy', '82 minutes');
INSERT INTO films (code, title, did, date_prod, kind)
 VALUES ('T_601', 'Yojimbo', 106, DEFAULT, 'Drama');</pre>
<p>To insert a row consisting entirely of default values: </p>
<pre>INSERT INTO films DEFAULT VALUES;</pre>
<p>To insert multiple rows using the multirow <code>VALUES</code> syntax: </p>
<pre>INSERT INTO films (code, title, did, date_prod, kind) VALUES
 ('B6717', 'Tampopo', 110, '1985-02-10', 'Comedy'),
 ('HG120', 'The Dinner Game', 140, DEFAULT, 'Comedy');</pre>
<p>This example inserts some rows into table films from a table tmp_films with the same column layout as films: </p>
<pre>INSERT INTO films SELECT * FROM tmp_films WHERE date_prod &lt; '2004-05-07';</pre>
<p>This example inserts into array columns: </p>
<pre>-- Create an empty 3x3 gameboard for noughts-and-crosses
INSERT INTO tictactoe (game, board[1:3][1:3])
 VALUES (1, '&#123;&#123;&quot; &quot;,&quot; &quot;,&quot; &quot;},{&quot; &quot;,&quot; &quot;,&quot; &quot;},{&quot; &quot;,&quot; &quot;,&quot; &quot;}}');
-- The subscripts in the above example aren't really needed
INSERT INTO tictactoe (game, board)
 VALUES (2, '&#123;&#123;X,&quot; &quot;,&quot; &quot;},{&quot; &quot;,O,&quot; &quot;},{&quot; &quot;,X,&quot; &quot;}}');</pre>
<p>Insert a single row into table distributors, returning the sequence number generated by the DEFAULT clause: </p>
<pre>INSERT INTO distributors (did, dname) VALUES (DEFAULT, 'XYZ Widgets')
 RETURNING did;</pre>
<h2>Compatibility</h2>
<p><code>INSERT</code> conforms to the SQL standard, except that the RETURNING clause is a PostgreSQL extension. Also, the case in which a column name list is omitted, but not all the columns are filled from the VALUES clause or <i>query</i>, is disallowed by the standard. </p>
<p> Possible limitations of the <i>query</i> clause are documented under SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)].</p>
