---
title: "table(7)"
name: "table"
section: "7"
letter: "t"
url: "/docs/linux/man/7-table/"
description: "SELECT, TABLE, WITH – retrieve rows from a table or view"
---

<p>SELECT, TABLE, WITH &#8211; retrieve rows from a table or view </p>
<h2>Synopsis</h2>
<pre>[ WITH [ RECURSIVE ] <i>with_query</i> [, ...] ]
SELECT [ ALL | DISTINCT [ ON ( <i>expression</i> [, ...] ) ] ]
 * | <i>expression</i> [ [ AS ] <i>output_name</i> ] [, ...]
 [ FROM <i>from_item</i> [, ...] ]
 [ WHERE <i>condition</i> ]
 [ GROUP BY <i>expression</i> [, ...] ]
 [ HAVING <i>condition</i> [, ...] ]
 [ WINDOW <i>window_name</i> AS ( <i>window_definition</i> ) [, ...] ]
 [ { UNION | INTERSECT | EXCEPT } [ ALL ] <i>select</i> ]
 [ ORDER BY <i>expression</i> [ ASC | DESC | USING <i>operator</i> ] [ NULLS { FIRST | LAST } ] [, ...] ]
 [ LIMIT { <i>count</i> | ALL } ]
 [ OFFSET <i>start</i> [ ROW | ROWS ] ]
 [ FETCH { FIRST | NEXT } [ <i>count</i> ] { ROW | ROWS } ONLY ]
 [ FOR { UPDATE | SHARE } [ OF <i>table_name</i> [, ...] ] [ NOWAIT ] [...] ]
where <i>from_item</i> can be one of:
 [ ONLY ] <i>table_name</i> [ * ] [ [ AS ] <i>alias</i> [ ( <i>column_alias</i> [, ...] ) ] ]
 ( <i>select</i> ) [ AS ] <i>alias</i> [ ( <i>column_alias</i> [, ...] ) ]
 <i>with_query_name</i> [ [ AS ] <i>alias</i> [ ( <i>column_alias</i> [, ...] ) ] ]
 <i>function_name</i> ( [ <i>argument</i> [, ...] ] ) [ AS ] <i>alias</i> [ ( <i>column_alias</i> [, ...] | <i>column_definition</i> [, ...] ) ]
 <i>function_name</i> ( [ <i>argument</i> [, ...] ] ) AS ( <i>column_definition</i> [, ...] )
 <i>from_item</i> [ NATURAL ] <i>join_type</i> <i>from_item</i> [ ON <i>join_condition</i> | USING ( <i>join_column</i> [, ...] ) ]
and <i>with_query</i> is:
 <i>with_query_name</i> [ ( <i>column_name</i> [, ...] ) ] AS ( <i>select</i> )
TABLE { [ ONLY ] <i>table_name</i> [ * ] | <i>with_query_name</i> }</pre>
<h2>Description</h2>
<p><code>SELECT</code> retrieves rows from zero or more tables. The general processing of <code>SELECT</code> is as follows:</p>
<dl>
<dt>1.</p>
<dd>All queries in the WITH list are computed. These effectively serve as temporary tables that can be referenced in the FROM list. A WITH query that is referenced more than once in FROM is computed only once. (See WITH Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>2.</p>
<dd>All elements in the FROM list are computed. (Each element in the FROM list is a real or virtual table.) If more than one element is specified in the FROM list, they are cross-joined together. (See FROM Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>3.</p>
<dd>If the WHERE clause is specified, all rows that do not satisfy the condition are eliminated from the output. (See WHERE Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>4.</p>
<dd>If the GROUP BY clause is specified, the output is divided into groups of rows that match on one or more values. If the HAVING clause is present, it eliminates groups that do not satisfy the given condition. (See GROUP BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] and HAVING Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>5.</p>
<dd>The actual output rows are computed using the <code>SELECT</code> output expressions for each selected row. (See SELECT List [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>6.</p>
<dd>Using the operators UNION, INTERSECT, and EXCEPT, the output of more than one <code>SELECT</code> statement can be combined to form a single result set. The UNION operator returns all rows that are in one or both of the result sets. The INTERSECT operator returns all rows that are strictly in both result sets. The EXCEPT operator returns the rows that are in the first result set but not in the second. In all three cases, duplicate rows are eliminated unless ALL is specified. (See UNION Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], INTERSECT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], and EXCEPT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>7.</p>
<dd>If the ORDER BY clause is specified, the returned rows are sorted in the specified order. If ORDER BY is not given, the rows are returned in whatever order the system finds fastest to produce. (See ORDER BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>8.</p>
<dd>DISTINCT eliminates duplicate rows from the result. DISTINCT ON eliminates rows that match on all the specified expressions. ALL (the default) will return all candidate rows, including duplicates. (See DISTINCT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>9.</p>
<dd>If the LIMIT (or FETCH FIRST) or OFFSET clause is specified, the <code>SELECT</code> statement only returns a subset of the result rows. (See LIMIT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</p>
<dt>10.</p>
<dd>If FOR UPDATE or FOR SHARE is specified, the <code>SELECT</code> statement locks the selected rows against concurrent updates. (See FOR UPDATE/FOR SHARE Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] below.)</dl>
<p> You must have SELECT privilege on each column used in a <code>SELECT</code> command. The use of FOR UPDATE or FOR SHARE requires UPDATE privilege as well (for at least one column of each table so selected).</p>
<h2>Parameters</h2>
<h3>With Clause</h3>
<p>The WITH clause allows you to specify one or more subqueries that can be referenced by name in the primary query. The subqueries effectively act as temporary tables or views for the duration of the primary query. </p>
<p> A name (without schema qualification) must be specified for each WITH query. Optionally, a list of column names can be specified; if this is omitted, the column names are inferred from the subquery. </p>
<p> If RECURSIVE is specified, it allows a subquery to reference itself by name. Such a subquery must have the form </p>
<pre><i>non_recursive_term</i> UNION [ ALL ] <i>recursive_term</i></pre>
<p>where the recursive self-reference must appear on the right-hand side of the UNION. Only one recursive self-reference is permitted per query. </p>
<p> Another effect of RECURSIVE is that WITH queries need not be ordered: a query can reference another one that is later in the list. (However, circular references, or mutual recursion, are not implemented.) Without RECURSIVE, WITH queries can only reference sibling WITH queries that are earlier in the WITH list. </p>
<p> A useful property of WITH queries is that they are evaluated only once per execution of the primary query, even if the primary query refers to them more than once. </p>
<p> See in the documentation for additional information.</p>
<h3>From Clause</h3>
<p>The FROM clause specifies one or more source tables for the <code>SELECT</code>. If multiple sources are specified, the result is the Cartesian product (cross join) of all the sources. But usually qualification conditions are added to restrict the returned rows to a small subset of the Cartesian product. </p>
<p> The FROM clause can contain the following elements:</p>
<dl>
<dt><i>table_name</i></p>
<dd>The name (optionally schema-qualified) of an existing table or view. If ONLY is specified, only that table is scanned. If ONLY is not specified, the table and any descendant tables are scanned.</p>
<dt><i>alias</i></p>
<dd>A substitute name for the FROM item containing the alias. An alias is used for brevity or to eliminate ambiguity for self-joins (where the same table is scanned multiple times). When an alias is provided, it completely hides the actual name of the table or function; for example given FROM foo AS f, the remainder of the <code>SELECT</code> must refer to this FROM item as f not foo. If an alias is written, a column alias list can also be written to provide substitute names for one or more columns of the table.</p>
<dt><i>select</i></p>
<dd>A sub-<code>SELECT</code> can appear in the FROM clause. This acts as though its output were created as a temporary table for the duration of this single <code>SELECT</code> command. Note that the sub-<code>SELECT</code> must be surrounded by parentheses, and an alias <code>must</code> be provided for it. A VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] command can also be used here.</p>
<dt><i>with_query_name</i></p>
<dd>A WITH query is referenced by writing its name, just as though the query&#8217;s name were a table name. (In fact, the WITH query hides any real table of the same name for the purposes of the primary query. If necessary, you can refer to a real table of the same name by schema-qualifying the table&#8217;s name.) An alias can be provided in the same way as for a table.</p>
<dt><i>function_name</i></p>
<dd>Function calls can appear in the FROM clause. (This is especially useful for functions that return result sets, but any function can be used.) This acts as though its output were created as a temporary table for the duration of this single <code>SELECT</code> command. An alias can also be used. If an alias is written, a column alias list can also be written to provide substitute names for one or more attributes of the function&#8217;s composite return type. If the function has been defined as returning the <code>record</code> data type, then an alias or the key word AS must be present, followed by a column definition list in the form ( <i>column_name</i> <i>data_type</i> [, &#8230; ] ). The column definition list must match the actual number and types of columns returned by the function.</p>
<dt><i>join_type</i></p>
<dd>One of</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>[ INNER ] JOIN</p>
<dt>*</p>
<dd>LEFT [ OUTER ] JOIN</p>
<dt>*</p>
<dd>RIGHT [ OUTER ] JOIN</p>
<dt>*</p>
<dd>FULL [ OUTER ] JOIN</p>
<dt>*</p>
<dd>CROSS JOIN</dl>
</dl>
</dl>
<p> For the INNER and OUTER join types, a join condition must be specified, namely exactly one of NATURAL, ON <i>join_condition</i>, or USING (<i>join_column</i> [, &#8230;]). See below for the meaning. For CROSS JOIN, none of these clauses can appear. </p>
<p> A JOIN clause combines two FROM items. Use parentheses if necessary to determine the order of nesting. In the absence of parentheses, JOINs nest left-to-right. In any case JOIN binds more tightly than the commas separating FROM items. </p>
<p> CROSS JOIN and INNER JOIN produce a simple Cartesian product, the same result as you get from listing the two items at the top level of FROM, but restricted by the join condition (if any). CROSS JOIN is equivalent to INNER JOIN ON (TRUE), that is, no rows are removed by qualification. These join types are just a notational convenience, since they do nothing you couldn&#8217;t do with plain FROM and WHERE. </p>
<p> LEFT OUTER JOIN returns all rows in the qualified Cartesian product (i.e., all combined rows that pass its join condition), plus one copy of each row in the left-hand table for which there was no right-hand row that passed the join condition. This left-hand row is extended to the full width of the joined table by inserting null values for the right-hand columns. Note that only the JOIN clause&#8217;s own condition is considered while deciding which rows have matches. Outer conditions are applied afterwards. </p>
<p> Conversely, RIGHT OUTER JOIN returns all the joined rows, plus one row for each unmatched right-hand row (extended with nulls on the left). This is just a notational convenience, since you could convert it to a LEFT OUTER JOIN by switching the left and right inputs. </p>
<p> FULL OUTER JOIN returns all the joined rows, plus one row for each unmatched left-hand row (extended with nulls on the right), plus one row for each unmatched right-hand row (extended with nulls on the left).</p>
<dl>
<dt><code>ON </code><i>join_condition</i></p>
<dd><i>join_condition</i> is an expression resulting in a value of type <code>boolean</code> (similar to a WHERE clause) that specifies which rows in a join are considered to match.</p>
<dt><code>USING ( </code><i>join_column</i><code> [, &#8230;] )</code></p>
<dd>A clause of the form USING ( a, b, &#8230; ) is shorthand for ON left_table.a = right_table.a AND left_table.b = right_table.b &#8230;. Also, USING implies that only one of each pair of equivalent columns will be included in the join output, not both.</p>
<dt><code>NATURAL</code></p>
<dd>NATURAL is shorthand for a USING list that mentions all columns in the two tables that have the same names.</dl>
<h3>Where Clause</h3>
<p>The optional WHERE clause has the general form </p>
<pre>WHERE <i>condition</i></pre>
<p>where <i>condition</i> is any expression that evaluates to a result of type <code>boolean</code>. Any row that does not satisfy this condition will be eliminated from the output. A row satisfies the condition if it returns true when the actual row values are substituted for any variable references.</p>
<h3>Group By Clause</h3>
<p>The optional GROUP BY clause has the general form </p>
<pre>GROUP BY <i>expression</i> [, ...]</pre>
<p>GROUP BY will condense into a single row all selected rows that share the same values for the grouped expressions. <i>expression</i> can be an input column name, or the name or ordinal number of an output column (<code>SELECT</code> list item), or an arbitrary expression formed from input-column values. In case of ambiguity, a GROUP BY name will be interpreted as an input-column name rather than an output column name. </p>
<p> Aggregate functions, if any are used, are computed across all rows making up each group, producing a separate value for each group (whereas without GROUP BY, an aggregate produces a single value computed across all the selected rows). When GROUP BY is present, it is not valid for the <code>SELECT</code> list expressions to refer to ungrouped columns except within aggregate functions, since there would be more than one possible value to return for an ungrouped column.</p>
<h3>Having Clause</h3>
<p>The optional HAVING clause has the general form </p>
<pre>HAVING <i>condition</i></pre>
<p>where <i>condition</i> is the same as specified for the WHERE clause. </p>
<p> HAVING eliminates group rows that do not satisfy the condition. HAVING is different from WHERE: WHERE filters individual rows before the application of GROUP BY, while HAVING filters group rows created by GROUP BY. Each column referenced in <i>condition</i> must unambiguously reference a grouping column, unless the reference appears within an aggregate function. </p>
<p> The presence of HAVING turns a query into a grouped query even if there is no GROUP BY clause. This is the same as what happens when the query contains aggregate functions but no GROUP BY clause. All the selected rows are considered to form a single group, and the <code>SELECT</code> list and HAVING clause can only reference table columns from within aggregate functions. Such a query will emit a single row if the HAVING condition is true, zero rows if it is not true.</p>
<h3>Window Clause</h3>
<p>The optional WINDOW clause has the general form </p>
<pre>WINDOW <i>window_name</i> AS ( <i>window_definition</i> ) [, ...]</pre>
<p>where <i>window_name</i> is a name that can be referenced from subsequent window definitions or OVER clauses, and <i>window_definition</i> is </p>
<pre>[ <i>existing_window_name</i> ]
[ PARTITION BY <i>expression</i> [, ...] ]
[ ORDER BY <i>expression</i> [ ASC | DESC | USING <i>operator</i> ] [ NULLS { FIRST | LAST } ] [, ...] ]
[ <i>frame_clause</i> ]</pre>
<p>If an <i>existing_window_name</i> is specified it must refer to an earlier entry in the WINDOW list; the new window copies its partitioning clause from that entry, as well as its ordering clause if any. In this case the new window cannot specify its own PARTITION BY clause, and it can specify ORDER BY only if the copied window does not have one. The new window always uses its own frame clause; the copied window must not specify a frame clause. </p>
<p> The elements of the PARTITION BY list are interpreted in much the same fashion as elements of a GROUP BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], except that they are always simple expressions and never the name or number of an output column. Another difference is that these expressions can contain aggregate function calls, which are not allowed in a regular GROUP BY clause. They are allowed here because windowing occurs after grouping and aggregation. </p>
<p> Similarly, the elements of the ORDER BY list are interpreted in much the same fashion as elements of an ORDER BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], except that the expressions are always taken as simple expressions and never the name or number of an output column. </p>
<p> The optional <i>frame_clause</i> defines the <i>window frame</i> for window functions that depend on the frame (not all do). It can be one of </p>
<pre>RANGE UNBOUNDED PRECEDING
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
ROWS UNBOUNDED PRECEDING
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING</pre>
<p>The first two are equivalent and are also the default: they set the frame to be all rows from the partition start up through the current row&#8217;s last peer in the ORDER BY ordering (which means all rows if there is no ORDER BY). The options RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING and ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING are also equivalent: they always select all rows in the partition. Lastly, ROWS UNBOUNDED PRECEDING or its verbose equivalent ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW select all rows up through the current row (regardless of duplicates). Beware that this option can produce implementation-dependent results if the ORDER BY ordering does not order the rows uniquely. </p>
<p> The purpose of a WINDOW clause is to specify the behavior of <i>window functions</i> appearing in the query&#8217;s SELECT List [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] or ORDER BY Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)]. These functions can reference the WINDOW clause entries by name in their OVER clauses. A WINDOW clause entry does not have to be referenced anywhere, however; if it is not used in the query it is simply ignored. It is possible to use window functions without any WINDOW clause at all, since a window function call can specify its window definition directly in its OVER clause. However, the WINDOW clause saves typing when the same window definition is needed for more than one window function. </p>
<p> Window functions are described in detail in in the documentation, in the documentation, and in the documentation.</p>
<h3>Select List</h3>
<p>The <code>SELECT</code> list (between the key words SELECT and FROM) specifies expressions that form the output rows of the <code>SELECT</code> statement. The expressions can (and usually do) refer to columns computed in the FROM clause. </p>
<p> Just as in a table, every output column of a <code>SELECT</code> has a name. In a simple <code>SELECT</code> this name is just used to label the column for display, but when the <code>SELECT</code> is a sub-query of a larger query, the name is seen by the larger query as the column name of the virtual table produced by the sub-query. To specify the name to use for an output column, write AS <i>output_name</i> after the column&#8217;s expression. (You can omit AS, but only if the desired output name does not match any PostgreSQL keyword (see in the documentation). For protection against possible future keyword additions, it is recommended that you always either write AS or double-quote the output name.) If you do not specify a column name, a name is chosen automatically by PostgreSQL. If the column&#8217;s expression is a simple column reference then the chosen name is the same as that column&#8217;s name; in more complex cases a generated name looking like ?column<i>N</i>? is usually chosen. </p>
<p> An output column&#8217;s name can be used to refer to the column&#8217;s value in ORDER BY and GROUP BY clauses, but not in the WHERE or HAVING clauses; there you must write out the expression instead. </p>
<p> Instead of an expression, * can be written in the output list as a shorthand for all the columns of the selected rows. Also, you can write <i>table_name</i>.* as a shorthand for the columns coming from just that table. In these cases it is not possible to specify new names with AS; the output column names will be the same as the table columns&#8217; names.</p>
<h3>Union Clause</h3>
<p>The UNION clause has this general form: </p>
<pre><i>select_statement</i> UNION [ ALL ] <i>select_statement</i></pre>
<p><i>select_statement</i> is any <code>SELECT</code> statement without an ORDER BY, LIMIT, FOR UPDATE, or FOR SHARE clause. (ORDER BY and LIMIT can be attached to a subexpression if it is enclosed in parentheses. Without parentheses, these clauses will be taken to apply to the result of the UNION, not to its right-hand input expression.) </p>
<p> The UNION operator computes the set union of the rows returned by the involved <code>SELECT</code> statements. A row is in the set union of two result sets if it appears in at least one of the result sets. The two <code>SELECT</code> statements that represent the direct operands of the UNION must produce the same number of columns, and corresponding columns must be of compatible data types. </p>
<p> The result of UNION does not contain any duplicate rows unless the ALL option is specified. ALL prevents elimination of duplicates. (Therefore, UNION ALL is usually significantly quicker than UNION; use ALL when you can.) </p>
<p> Multiple UNION operators in the same <code>SELECT</code> statement are evaluated left to right, unless otherwise indicated by parentheses. </p>
<p> Currently, FOR UPDATE and FOR SHARE cannot be specified either for a UNION result or for any input of a UNION.</p>
<h3>Intersect Clause</h3>
<p>The INTERSECT clause has this general form: </p>
<pre><i>select_statement</i> INTERSECT [ ALL ] <i>select_statement</i></pre>
<p><i>select_statement</i> is any <code>SELECT</code> statement without an ORDER BY, LIMIT, FOR UPDATE, or FOR SHARE clause. </p>
<p> The INTERSECT operator computes the set intersection of the rows returned by the involved <code>SELECT</code> statements. A row is in the intersection of two result sets if it appears in both result sets. </p>
<p> The result of INTERSECT does not contain any duplicate rows unless the ALL option is specified. With ALL, a row that has <i>m</i> duplicates in the left table and <i>n</i> duplicates in the right table will appear min(<i>m</i>,<i>n</i>) times in the result set. </p>
<p> Multiple INTERSECT operators in the same <code>SELECT</code> statement are evaluated left to right, unless parentheses dictate otherwise. INTERSECT binds more tightly than UNION. That is, A UNION B INTERSECT C will be read as A UNION (B INTERSECT C). </p>
<p> Currently, FOR UPDATE and FOR SHARE cannot be specified either for an INTERSECT result or for any input of an INTERSECT.</p>
<h3>Except Clause</h3>
<p>The EXCEPT clause has this general form: </p>
<pre><i>select_statement</i> EXCEPT [ ALL ] <i>select_statement</i></pre>
<p><i>select_statement</i> is any <code>SELECT</code> statement without an ORDER BY, LIMIT, FOR UPDATE, or FOR SHARE clause. </p>
<p> The EXCEPT operator computes the set of rows that are in the result of the left <code>SELECT</code> statement but not in the result of the right one. </p>
<p> The result of EXCEPT does not contain any duplicate rows unless the ALL option is specified. With ALL, a row that has <i>m</i> duplicates in the left table and <i>n</i> duplicates in the right table will appear max(<i>m</i>&#8211;<i>n</i>,0) times in the result set. </p>
<p> Multiple EXCEPT operators in the same <code>SELECT</code> statement are evaluated left to right, unless parentheses dictate otherwise. EXCEPT binds at the same level as UNION. </p>
<p> Currently, FOR UPDATE and FOR SHARE cannot be specified either for an EXCEPT result or for any input of an EXCEPT.</p>
<h3>Order By Clause</h3>
<p>The optional ORDER BY clause has this general form: </p>
<pre>ORDER BY <i>expression</i> [ ASC | DESC | USING <i>operator</i> ] [ NULLS { FIRST | LAST } ] [, ...]</pre>
<p>The ORDER BY clause causes the result rows to be sorted according to the specified expression(s). If two rows are equal according to the leftmost expression, they are compared according to the next expression and so on. If they are equal according to all specified expressions, they are returned in an implementation-dependent order. </p>
<p> Each <i>expression</i> can be the name or ordinal number of an output column (<code>SELECT</code> list item), or it can be an arbitrary expression formed from input-column values. </p>
<p> The ordinal number refers to the ordinal (left-to-right) position of the output column. This feature makes it possible to define an ordering on the basis of a column that does not have a unique name. This is never absolutely necessary because it is always possible to assign a name to an output column using the AS clause. </p>
<p> It is also possible to use arbitrary expressions in the ORDER BY clause, including columns that do not appear in the <code>SELECT</code> output list. Thus the following statement is valid: </p>
<pre>SELECT name FROM distributors ORDER BY code;</pre>
<p>A limitation of this feature is that an ORDER BY clause applying to the result of a UNION, INTERSECT, or EXCEPT clause can only specify an output column name or number, not an expression. </p>
<p> If an ORDER BY expression is a simple name that matches both an output column name and an input column name, ORDER BY will interpret it as the output column name. This is the opposite of the choice that GROUP BY will make in the same situation. This inconsistency is made to be compatible with the SQL standard. </p>
<p> Optionally one can add the key word ASC (ascending) or DESC (descending) after any expression in the ORDER BY clause. If not specified, ASC is assumed by default. Alternatively, a specific ordering operator name can be specified in the USING clause. An ordering operator must be a less-than or greater-than member of some B-tree operator family. ASC is usually equivalent to USING &lt; and DESC is usually equivalent to USING &gt;. (But the creator of a user-defined data type can define exactly what the default sort ordering is, and it might correspond to operators with other names.) </p>
<p> If NULLS LAST is specified, null values sort after all non-null values; if NULLS FIRST is specified, null values sort before all non-null values. If neither is specified, the default behavior is NULLS LAST when ASC is specified or implied, and NULLS FIRST when DESC is specified (thus, the default is to act as though nulls are larger than non-nulls). When USING is specified, the default nulls ordering depends on whether the operator is a less-than or greater-than operator. </p>
<p> Note that ordering options apply only to the expression they follow; for example ORDER BY x, y DESC does not mean the same thing as ORDER BY x DESC, y DESC. </p>
<p> Character-string data is sorted according to the locale-specific collation order that was established when the database was created.</p>
<h3>Distinct Clause</h3>
<p>If DISTINCT is specified, all duplicate rows are removed from the result set (one row is kept from each group of duplicates). ALL specifies the opposite: all rows are kept; that is the default. </p>
<p> DISTINCT ON ( <i>expression</i> [, &#8230;] ) keeps only the first row of each set of rows where the given expressions evaluate to equal. The DISTINCT ON expressions are interpreted using the same rules as for ORDER BY (see above). Note that the &#8220;first row&#8221; of each set is unpredictable unless ORDER BY is used to ensure that the desired row appears first. For example: </p>
<pre>SELECT DISTINCT ON (location) location, time, report
 FROM weather_reports
 ORDER BY location, time DESC;</pre>
<p>retrieves the most recent weather report for each location. But if we had not used ORDER BY to force descending order of time values for each location, we&#8217;d have gotten a report from an unpredictable time for each location. </p>
<p> The DISTINCT ON expression(s) must match the leftmost ORDER BY expression(s). The ORDER BY clause will normally contain additional expression(s) that determine the desired precedence of rows within each DISTINCT ON group.</p>
<h3>Limit Clause</h3>
<p>The LIMIT clause consists of two independent sub-clauses: </p>
<pre>LIMIT { <i>count</i> | ALL }
OFFSET <i>start</i></pre>
<p><i>count</i> specifies the maximum number of rows to return, while <i>start</i> specifies the number of rows to skip before starting to return rows. When both are specified, <i>start</i> rows are skipped before starting to count the <i>count</i> rows to be returned. </p>
<p> If the <i>count</i> expression evaluates to NULL, it is treated as LIMIT ALL, i.e., no limit. If <i>start</i> evaluates to NULL, it is treated the same as OFFSET 0. </p>
<p> SQL:2008 introduced a different syntax to achieve the same thing, which PostgreSQL also supports. It is: </p>
<pre>OFFSET <i>start</i> { ROW | ROWS }
FETCH { FIRST | NEXT } [ <i>count</i> ] { ROW | ROWS } ONLY</pre>
<p>Both clauses are optional, but if present the OFFSET clause must come before the FETCH clause. ROW and ROWS as well as FIRST and NEXT are noise words that don&#8217;t influence the effects of these clauses. In this syntax, when using expressions other than simple constants for <i>start</i> or <i>count</i>, parentheses will be necessary in most cases. If <i>count</i> is omitted in FETCH, it defaults to 1. </p>
<p> When using LIMIT, it is a good idea to use an ORDER BY clause that constrains the result rows into a unique order. Otherwise you will get an unpredictable subset of the query&#8217;s rows &#8212; you might be asking for the tenth through twentieth rows, but tenth through twentieth in what ordering? You don&#8217;t know what ordering unless you specify ORDER BY. </p>
<p> The query planner takes LIMIT into account when generating a query plan, so you are very likely to get different plans (yielding different row orders) depending on what you use for LIMIT and OFFSET. Thus, using different LIMIT/OFFSET values to select different subsets of a query result <code>will give inconsistent results</code> unless you enforce a predictable result ordering with ORDER BY. This is not a bug; it is an inherent consequence of the fact that SQL does not promise to deliver the results of a query in any particular order unless ORDER BY is used to constrain the order. </p>
<p> It is even possible for repeated executions of the same LIMIT query to return different subsets of the rows of a table, if there is not an ORDER BY to enforce selection of a deterministic subset. Again, this is not a bug; determinism of the results is simply not guaranteed in such a case.</p>
<h3>For Update/For Share Clause</h3>
<p>The FOR UPDATE clause has this form: </p>
<pre>FOR UPDATE [ OF <i>table_name</i> [, ...] ] [ NOWAIT ]</pre>
<p>The closely related FOR SHARE clause has this form: </p>
<pre>FOR SHARE [ OF <i>table_name</i> [, ...] ] [ NOWAIT ]</pre>
<p>FOR UPDATE causes the rows retrieved by the <code>SELECT</code> statement to be locked as though for update. This prevents them from being modified or deleted by other transactions until the current transaction ends. That is, other transactions that attempt <code>UPDATE</code>, <code>DELETE</code>, or <code>SELECT FOR UPDATE</code> of these rows will be blocked until the current transaction ends. Also, if an <code>UPDATE</code>, <code>DELETE</code>, or <code>SELECT FOR UPDATE</code> from another transaction has already locked a selected row or rows, <code>SELECT FOR UPDATE</code> will wait for the other transaction to complete, and will then lock and return the updated row (or no row, if the row was deleted). For further discussion see in the documentation. </p>
<p> To prevent the operation from waiting for other transactions to commit, use the NOWAIT option. <code>SELECT FOR UPDATE NOWAIT</code> reports an error, rather than waiting, if a selected row cannot be locked immediately. Note that NOWAIT applies only to the row-level lock(s) &#8212; the required ROW SHARE table-level lock is still taken in the ordinary way (see in the documentation). You can use the NOWAIT option of LOCK [<code><a href="/docs/linux/man/7-lock/">lock</a></code>(7)] if you need to acquire the table-level lock without waiting. </p>
<p> FOR SHARE behaves similarly, except that it acquires a shared rather than exclusive lock on each retrieved row. A shared lock blocks other transactions from performing <code>UPDATE</code>, <code>DELETE</code>, or <code>SELECT FOR UPDATE</code> on these rows, but it does not prevent them from performing <code>SELECT FOR SHARE</code>. </p>
<p> If specific tables are named in FOR UPDATE or FOR SHARE, then only rows coming from those tables are locked; any other tables used in the <code>SELECT</code> are simply read as usual. A FOR UPDATE or FOR SHARE clause without a table list affects all tables used in the command. If FOR UPDATE or FOR SHARE is applied to a view or sub-query, it affects all tables used in the view or sub-query. However, FOR UPDATE/FOR SHARE do not apply to WITH queries referenced by the primary query. If you want row locking to occur within a WITH query, specify FOR UPDATE or FOR SHARE within the WITH query. </p>
<p> Multiple FOR UPDATE and FOR SHARE clauses can be written if it is necessary to specify different locking behavior for different tables. If the same table is mentioned (or implicitly affected) by both FOR UPDATE and FOR SHARE clauses, then it is processed as FOR UPDATE. Similarly, a table is processed as NOWAIT if that is specified in any of the clauses affecting it. </p>
<p> FOR UPDATE and FOR SHARE cannot be used in contexts where returned rows cannot be clearly identified with individual table rows; for example they cannot be used with aggregation. </p>
<dl>
<dd><code>Caution:</code> Avoid locking a row and then modifying it within a later savepoint or <code>PL/pgSQL</code> exception block. A subsequent rollback would cause the lock to be lost. For example: </p>
<pre>BEGIN;
SELECT * FROM mytable WHERE key = 1 FOR UPDATE;
SAVEPOINT s;
UPDATE mytable SET ... WHERE key = 1;
ROLLBACK TO s;</pre>
<p>After the <code>ROLLBACK</code>, the row is effectively unlocked, rather than returned to its pre-savepoint state of being locked but not modified. This hazard occurs if a row locked in the current transaction is updated or deleted, or if a shared lock is upgraded to exclusive: in all these cases, the former lock state is forgotten. If the transaction is then rolled back to a state between the original locking command and the subsequent change, the row will appear not to be locked at all. This is an implementation deficiency which will be addressed in a future release of PostgreSQL.</dl>
<dl>
<dd><code>Caution:</code> It is possible for a <code>SELECT</code> command using both LIMIT and FOR UPDATE/SHARE clauses to return fewer rows than specified by LIMIT. This is because LIMIT is applied first. The command selects the specified number of rows, but might then block trying to obtain a lock on one or more of them. Once the SELECT unblocks, the row might have been deleted or updated so that it does not meet the query WHERE condition anymore, in which case it will not be returned.</dl>
<dl>
<dd><code>Caution:</code> Similarly, it is possible for a <code>SELECT</code> command using ORDER BY and FOR UPDATE/SHARE to return rows out of order. This is because ORDER BY is applied first. The command orders the result, but might then block trying to obtain a lock on one or more of the rows. Once the SELECT unblocks, one of the ordered columns might have been modified and be returned out of order. A workaround is to perform <code>SELECT &#8230; FOR UPDATE/SHARE</code> and then <code>SELECT &#8230; ORDER BY</code>.</dl>
<h3>Table Command</h3>
<p>The command </p>
<pre>TABLE <i>name</i></pre>
<p>is completely equivalent to </p>
<pre>SELECT * FROM <i>name</i></pre>
<p>It can be used as a top-level command or as a space-saving syntax variant in parts of complex queries.</p>
<h2>Examples</h2>
<p>To join the table films with the table distributors: </p>
<pre>SELECT f.title, f.did, d.name, f.date_prod, f.kind
 FROM distributors d, films f
 WHERE f.did = d.did
 title | did | name | date_prod | kind
-------------------+-----+--------------+------------+----------
 The Third Man | 101 | British Lion | 1949-12-23 | Drama
 The African Queen | 101 | British Lion | 1951-08-11 | Romantic
 ...</pre>
<p>To sum the column len of all films and group the results by kind: </p>
<pre>SELECT kind, sum(len) AS total FROM films GROUP BY kind;
 kind | total
----------+-------
 Action | 07:34
 Comedy | 02:58
 Drama | 14:28
 Musical | 06:42
 Romantic | 04:38</pre>
<p>To sum the column len of all films, group the results by kind and show those group totals that are less than 5 hours: </p>
<pre>SELECT kind, sum(len) AS total
 FROM films
 GROUP BY kind
 HAVING sum(len) &lt; interval '5 hours';
 kind | total
----------+-------
 Comedy | 02:58
 Romantic | 04:38</pre>
<p>The following two examples are identical ways of sorting the individual results according to the contents of the second column (name): </p>
<pre>SELECT * FROM distributors ORDER BY name;
SELECT * FROM distributors ORDER BY 2;
 did | name
-----+------------------
 109 | 20th Century Fox
 110 | Bavaria Atelier
 101 | British Lion
 107 | Columbia
 102 | Jean Luc Godard
 113 | Luso films
 104 | Mosfilm
 103 | Paramount
 106 | Toho
 105 | United Artists
 111 | Walt Disney
 112 | Warner Bros.
 108 | Westward</pre>
<p>The next example shows how to obtain the union of the tables distributors and actors, restricting the results to those that begin with the letter W in each table. Only distinct rows are wanted, so the key word ALL is omitted. </p>
<pre>distributors: actors:
 did | name id | name
-----+-------------- ----+----------------
 108 | Westward 1 | Woody Allen
 111 | Walt Disney 2 | Warren Beatty
 112 | Warner Bros. 3 | Walter Matthau
 ... ...
SELECT distributors.name
 FROM distributors
 WHERE distributors.name LIKE 'W%'
UNION
SELECT actors.name
 FROM actors
 WHERE actors.name LIKE 'W%';
 name
----------------
 Walt Disney
 Walter Matthau
 Warner Bros.
 Warren Beatty
 Westward
 Woody Allen</pre>
<p>This example shows how to use a function in the FROM clause, both with and without a column definition list: </p>
<pre>CREATE FUNCTION distributors(int) RETURNS SETOF distributors AS $$
 SELECT * FROM distributors WHERE did = $1;
$$ LANGUAGE SQL;
SELECT * FROM distributors(111);
 did | name
-----+-------------
 111 | Walt Disney
CREATE FUNCTION distributors_2(int) RETURNS SETOF record AS $$
 SELECT * FROM distributors WHERE did = $1;
$$ LANGUAGE SQL;
SELECT * FROM distributors_2(111) AS (f1 int, f2 text);
 f1 | f2
-----+-------------
 111 | Walt Disney</pre>
<p>This example shows how to use a simple WITH clause: </p>
<pre>WITH t AS (
 SELECT random() as x FROM generate_series(1, 3)
 )
SELECT * FROM t
UNION ALL
SELECT * FROM t
 x 
--------------------
 0.534150459803641
 0.520092216785997
 0.0735620250925422
 0.534150459803641
 0.520092216785997
 0.0735620250925422</pre>
<p>Notice that the WITH query was evaluated only once, so that we got two sets of the same three random values. This example uses WITH RECURSIVE to find all subordinates (direct or indirect) of the employee Mary, and their level of indirectness, from a table that shows only direct subordinates: </p>
<pre><code>WITH RECURSIVE employee_recursive(distance, employee_name, manager_name) AS(
    SELECT 1, employee_name, manager_name FROM employee WHERE manager_name = 'Mary' UNION ALL SELECT er.distance + 1, e.employee_name, e.manager_name FROM employee_recursive er, employee e WHERE er.employee_name = e.manager_name)
    SELECT distance,
    employee_name FROM employee_recursive;

Notice the typical form of recursive queries:
an initial condition, followed by UNION,
followed by the recursive part of the query. Be sure that the
recursive part of the query will eventually return no tuples, or
else the query will loop indefinitely. (See in the documentation
for more examples.)</code></pre>
<h2>Compatibility</h2>
<p>Of course, the <code>SELECT</code> statement is compatible with the SQL standard. But there are some extensions and some missing features.</p>
<h3>Omitted From Clauses</h3>
<p>PostgreSQL allows one to omit the FROM clause. It has a straightforward use to compute the results of simple expressions: </p>
<pre>SELECT 2+2;
 ?column?
----------
 4</pre>
<p>Some other SQL databases cannot do this except by introducing a dummy one-row table from which to do the <code>SELECT</code>. </p>
<p> Note that if a FROM clause is not specified, the query cannot reference any database tables. For example, the following query is invalid: </p>
<pre>SELECT distributors.* WHERE distributors.name = 'Westward';</pre>
<p>PostgreSQL releases prior to 8.1 would accept queries of this form, and add an implicit entry to the query&#8217;s FROM clause for each table referenced by the query. This is no longer the default behavior, because it does not comply with the SQL standard, and is considered by many to be error-prone. For compatibility with applications that rely on this behavior the add_missing_from configuration variable can be enabled.</p>
<h3>Omitting The As Key Word</h3>
<p>In the SQL standard, the optional key word AS can be omitted before an output column name whenever the new column name is a valid column name (that is, not the same as any reserved keyword). PostgreSQL is slightly more restrictive: AS is required if the new column name matches any keyword at all, reserved or not. Recommended practice is to use AS or double-quote output column names, to prevent any possible conflict against future keyword additions. </p>
<p> In FROM items, both the standard and PostgreSQL allow AS to be omitted before an alias that is an unreserved keyword. But this is impractical for output column names, because of syntactic ambiguities.</p>
<h3>Only And Parentheses</h3>
<p>The SQL standard requires parentheses around the table name after ONLY, as in SELECT * FROM ONLY (tab1), ONLY (tab2) WHERE &#8230;. PostgreSQL supports that as well, but the parentheses are optional. (This point applies equally to all SQL commands supporting the ONLY option.)</p>
<h3>Namespace Available To Group By And Order By</h3>
<p>In the SQL-92 standard, an ORDER BY clause can only use output column names or numbers, while a GROUP BY clause can only use expressions based on input column names. PostgreSQL extends each of these clauses to allow the other choice as well (but it uses the standard&#8217;s interpretation if there is ambiguity). PostgreSQL also allows both clauses to specify arbitrary expressions. Note that names appearing in an expression will always be taken as input-column names, not as output-column names. </p>
<p> SQL:1999 and later use a slightly different definition which is not entirely upward compatible with SQL-92. In most cases, however, PostgreSQL will interpret an ORDER BY or GROUP BY expression the same way SQL:1999 does.</p>
<h3>Window Clause Restrictions</h3>
<p>The SQL standard provides additional options for the window <i>frame_clause</i>. PostgreSQL currently supports only the options listed above.</p>
<h3>Limit And Offset</h3>
<p>The clauses LIMIT and OFFSET are PostgreSQL-specific syntax, also used by MySQL. The SQL:2008 standard has introduced the clauses OFFSET &#8230; FETCH {FIRST|NEXT} &#8230; for the same functionality, as shown above in LIMIT Clause [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)], and this syntax is also used by IBM DB2. (Applications written for Oracle frequently use a workaround involving the automatically generated rownum column, not available in PostgreSQL, to implement the effects of these clauses.)</p>
<h3>Nonstandard Clauses</h3>
<p>The clause DISTINCT ON is not defined in the SQL standard.</p>
