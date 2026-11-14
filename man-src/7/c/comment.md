---
title: "comment(7)"
name: "comment"
section: "7"
letter: "c"
url: "/docs/linux/man/7-comment/"
description: "COMMENT – define or change the comment of an object"
---

<p>COMMENT &#8211; define or change the comment of an object </p>
<h2>Synopsis</h2>
<pre>COMMENT ON
{
 TABLE <i>object_name</i> |
 COLUMN <i>table_name</i>.<i>column_name</i> |
 AGGREGATE <i>agg_name</i> (<i>agg_type</i> [, ...] ) |
 CAST (<i>sourcetype</i> AS <i>targettype</i>) |
 CONSTRAINT <i>constraint_name</i> ON <i>table_name</i> |
 CONVERSION <i>object_name</i> |
 DATABASE <i>object_name</i> |
 DOMAIN <i>object_name</i> |
 FUNCTION <i>func_name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] ) |
 INDEX <i>object_name</i> |
 LARGE OBJECT <i>large_object_oid</i> |
 OPERATOR <i>op</i> (<i>leftoperand_type</i>, <i>rightoperand_type</i>) |
 OPERATOR CLASS <i>object_name</i> USING <i>index_method</i> |
 OPERATOR FAMILY <i>object_name</i> USING <i>index_method</i> |
 [ PROCEDURAL ] LANGUAGE <i>object_name</i> |
 ROLE <i>object_name</i> |
 RULE <i>rule_name</i> ON <i>table_name</i> |
 SCHEMA <i>object_name</i> |
 SEQUENCE <i>object_name</i> |
 TABLESPACE <i>object_name</i> |
 TEXT SEARCH CONFIGURATION <i>object_name</i> |
 TEXT SEARCH DICTIONARY <i>object_name</i> |
 TEXT SEARCH PARSER <i>object_name</i> |
 TEXT SEARCH TEMPLATE <i>object_name</i> |
 TRIGGER <i>trigger_name</i> ON <i>table_name</i> |
 TYPE <i>object_name</i> |
 VIEW <i>object_name</i>
} IS <i>'text'</i></pre>
<h2>Description</h2>
<p><code>COMMENT</code> stores a comment about a database object. </p>
<p> To modify a comment, issue a new <code>COMMENT</code> command for the same object. Only one comment string is stored for each object. To remove a comment, write NULL in place of the text string. Comments are automatically dropped when the object is dropped. </p>
<p> Comments can be viewed using <code>psql</code>&#8216;s <code>\d</code> family of commands. Other user interfaces to retrieve comments can be built atop the same built-in functions that <code>psql</code> uses, namely <code>obj_description</code>, <code>col_description</code>, and <code>shobj_description</code> (see in the documentation).</p>
<h2>Parameters</h2>
<dl>
<dt><i>object_name</i></p>
<dd>
<dt><i>table_name.column_name</i></p>
<dd>
<dt><i>agg_name</i></p>
<dd>
<dt><i>constraint_name</i></p>
<dd>
<dt><i>func_name</i></p>
<dd>
<dt><i>op</i></p>
<dd>
<dt><i>rule_name</i></p>
<dd>
<dt><i>trigger_name</i></p>
<dd>The name of the object to be commented. Names of tables, aggregates, domains, functions, indexes, operators, operator classes, operator families, sequences, text search objects, types, and views can be schema-qualified.</p>
<dt><i>agg_type</i></p>
<dd>An input data type on which the aggregate function operates. To reference a zero-argument aggregate function, write * in place of the list of input data types.</p>
<dt><i>sourcetype</i></p>
<dd>The name of the source data type of the cast.</p>
<dt><i>targettype</i></p>
<dd>The name of the target data type of the cast.</p>
<dt><i>argmode</i></p>
<dd>The mode of a function argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Note that <code>COMMENT ON FUNCTION</code> does not actually pay any attention to OUT arguments, since only the input arguments are needed to determine the function&#8217;s identity. So it is sufficient to list the IN, INOUT, and VARIADIC arguments.</p>
<dt><i>argname</i></p>
<dd>The name of a function argument. Note that <code>COMMENT ON FUNCTION</code> does not actually pay any attention to argument names, since only the argument data types are needed to determine the function&#8217;s identity.</p>
<dt><i>argtype</i></p>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any.</p>
<dt><i>large_object_oid</i></p>
<dd>The OID of the large object.</p>
<dt><code>PROCEDURAL</code></p>
<dd>This is a noise word.</p>
<dt><i>text</i></p>
<dd>The new comment, written as a string literal; or NULL to drop the comment.</dl>
<h2>Notes</h2>
<p>There is presently no security mechanism for comments: any user connected to a database can see all the comments for objects in that database (although only superusers can change comments for objects that they don&#8217;t own). For shared objects such as databases, roles, and tablespaces comments are stored globally and any user connected to any database can see all the comments for shared objects. Therefore, don&#8217;t put security-critical information in comments.</p>
<h2>Examples</h2>
<p>Attach a comment to the table mytable: </p>
<pre>COMMENT ON TABLE mytable IS 'This is my table.';</pre>
<p>Remove it again: </p>
<pre>COMMENT ON TABLE mytable IS NULL;</pre>
<p>Some more examples: </p>
<pre>COMMENT ON AGGREGATE my_aggregate (double precision) IS 'Computes sample variance';
COMMENT ON CAST (text AS int4) IS 'Allow casts from text to int4';
COMMENT ON COLUMN my_table.my_column IS 'Employee ID number';
COMMENT ON CONVERSION my_conv IS 'Conversion to UTF8';
COMMENT ON DATABASE my_database IS 'Development Database';
COMMENT ON DOMAIN my_domain IS 'Email Address Domain';
COMMENT ON FUNCTION my_function (timestamp) IS 'Returns Roman Numeral';
COMMENT ON INDEX my_index IS 'Enforces uniqueness on employee ID';
COMMENT ON LANGUAGE plpython IS 'Python support for stored procedures';
COMMENT ON LARGE OBJECT 346344 IS 'Planning document';
COMMENT ON OPERATOR ^ (text, text) IS 'Performs intersection of two texts';
COMMENT ON OPERATOR - (NONE, text) IS 'This is a prefix operator on text';
COMMENT ON OPERATOR CLASS int4ops USING btree IS '4 byte integer operators for btrees';
COMMENT ON OPERATOR FAMILY integer_ops USING btree IS 'all integer operators for btrees';
COMMENT ON ROLE my_role IS 'Administration group for finance tables';
COMMENT ON RULE my_rule ON my_table IS 'Logs updates of employee records';
COMMENT ON SCHEMA my_schema IS 'Departmental data';
COMMENT ON SEQUENCE my_sequence IS 'Used to generate primary keys';
COMMENT ON TABLE my_schema.my_table IS 'Employee Information';
COMMENT ON TABLESPACE my_tablespace IS 'Tablespace for indexes';
COMMENT ON TEXT SEARCH CONFIGURATION my_config IS 'Special word filtering';
COMMENT ON TEXT SEARCH DICTIONARY swedish IS 'Snowball stemmer for swedish language';
COMMENT ON TEXT SEARCH PARSER my_parser IS 'Splits text into words';
COMMENT ON TEXT SEARCH TEMPLATE snowball IS 'Snowball stemmer';
COMMENT ON TRIGGER my_trigger ON my_table IS 'Used for RI';
COMMENT ON TYPE complex IS 'Complex number data type';
COMMENT ON VIEW my_view IS 'View of departmental costs';</pre>
<h2>Compatibility</h2>
<p>There is no <code>COMMENT</code> command in the SQL standard.</p>
