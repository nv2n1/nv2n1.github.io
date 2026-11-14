---
title: "alter_extension(7)"
name: "alter_extension"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_extension/"
description: "ALTER_EXTENSION – change the definition of an extension"
---

<p>ALTER_EXTENSION &#8211; change the definition of an extension</p>
<h2>Synopsis</h2>
<pre>ALTER EXTENSION <i>name</i> UPDATE [ TO <i>new_version</i> ]
ALTER EXTENSION <i>name</i> SET SCHEMA <i>new_schema</i>
ALTER EXTENSION <i>name</i> ADD <i>member_object</i>
ALTER EXTENSION <i>name</i> DROP <i>member_object</i>
where <i>member_object</i> is:
 AGGREGATE <i>agg_name</i> (<i>agg_type</i> [, ...] ) |
 CAST (<i>source_type</i> AS <i>target_type</i>) |
 COLLATION <i>object_name</i> |
 CONVERSION <i>object_name</i> |
 DOMAIN <i>object_name</i> |
 FOREIGN DATA WRAPPER <i>object_name</i> |
 FOREIGN TABLE <i>object_name</i> |
 FUNCTION <i>function_name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] ) |
 OPERATOR <i>operator_name</i> (<i>left_type</i>, <i>right_type</i>) |
 OPERATOR CLASS <i>object_name</i> USING <i>index_method</i> |
 OPERATOR FAMILY <i>object_name</i> USING <i>index_method</i> |
 [ PROCEDURAL ] LANGUAGE <i>object_name</i> |
 SCHEMA <i>object_name</i> |
 SEQUENCE <i>object_name</i> |
 SERVER <i>object_name</i> |
 TABLE <i>object_name</i> |
 TEXT SEARCH CONFIGURATION <i>object_name</i> |
 TEXT SEARCH DICTIONARY <i>object_name</i> |
 TEXT SEARCH PARSER <i>object_name</i> |
 TEXT SEARCH TEMPLATE <i>object_name</i> |
 TYPE <i>object_name</i> |
 VIEW <i>object_name</i></pre>
<h2>Description</h2>
<p><code>ALTER EXTENSION</code> changes the definition of an installed extension. There are several subforms: </p>
<p> UPDATE</p>
<dl>
<dd>This form updates the extension to a newer version. The extension must supply a suitable update script (or series of scripts) that can modify the currently-installed version into the requested version.</dl>
<p> SET SCHEMA</p>
<dl>
<dd>This form moves the extension&#8217;s objects into another schema. The extension has to be relocatable for this command to succeed.</dl>
<p> ADD <i>member_object</i></p>
<dl>
<dd>This form adds an existing object to the extension. This is mainly useful in extension update scripts. The object will subsequently be treated as a member of the extension; notably, it can only be dropped by dropping the extension.</dl>
<p> DROP <i>member_object</i></p>
<dl>
<dd>This form removes a member object from the extension. This is mainly useful in extension update scripts. The object is not dropped, only disassociated from the extension.</dl>
<p> See Section 35.15, &#8220;Packaging Related Objects into an Extension&#8221;, in the documentation for more information about these operations. </p>
<p> You must own the extension to use <code>ALTER EXTENSION</code>. The ADD/DROP forms require ownership of the added/dropped object as well.</p>
<h2>Parameters</h2>
<p><i>name</i></p>
<dl>
<dd>The name of an installed extension.</dl>
<p> <i>new_version</i></p>
<dl>
<dd>The desired new version of the extension. This can be written as either an identifier or a string literal. If not specified, <code>ALTER EXTENSION UPDATE</code> attempts to update to whatever is shown as the default version in the extension&#8217;s control file.</dl>
<p> <i>new_schema</i></p>
<dl>
<dd>The new schema for the extension.</dl>
<p> <i>object_name</i>, <i>agg_name</i>, <i>function_name</i>, <i>operator_name</i></p>
<dl>
<dd>The name of an object to be added to or removed from the extension. Names of tables, aggregates, domains, foreign tables, functions, operators, operator classes, operator families, sequences, text search objects, types, and views can be schema-qualified.</dl>
<p> <i>agg_type</i></p>
<dl>
<dd>An input data type on which the aggregate function operates. To reference a zero-argument aggregate function, write * in place of the list of input data types.</dl>
<p> <i>source_type</i></p>
<dl>
<dd>The name of the source data type of the cast.</dl>
<p> <i>target_type</i></p>
<dl>
<dd>The name of the target data type of the cast.</dl>
<p> <i>argmode</i></p>
<dl>
<dd>The mode of a function argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Note that <code>ALTER EXTENSION</code> does not actually pay any attention to OUT arguments, since only the input arguments are needed to determine the function&#8217;s identity. So it is sufficient to list the IN, INOUT, and VARIADIC arguments.</dl>
<p> <i>argname</i></p>
<dl>
<dd>The name of a function argument. Note that <code>ALTER EXTENSION</code> does not actually pay any attention to argument names, since only the argument data types are needed to determine the function&#8217;s identity.</dl>
<p> <i>argtype</i></p>
<dl>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any.</dl>
<p> <i>left_type</i>, <i>right_type</i></p>
<dl>
<dd>The data type(s) of the operator&#8217;s arguments (optionally schema-qualified). Write NONE for the missing argument of a prefix or postfix operator.</dl>
<p> PROCEDURAL</p>
<dl>
<dd>This is a noise word.</dl>
<h2>Examples</h2>
<p>To update the hstore extension to version 2.0: </p>
<dl>
<dd>
<pre>ALTER EXTENSION hstore UPDATE TO '2.0';</pre>
</dl>
<p> To change the schema of the hstore extension to utils: </p>
<dl>
<dd>
<pre>ALTER EXTENSION hstore SET SCHEMA utils;</pre>
</dl>
<p> To add an existing function to the hstore extension: </p>
<dl>
<dd>
<pre>ALTER EXTENSION hstore ADD FUNCTION populate_record(anyelement, hstore);</pre>
</dl>
<h2>Compatibility</h2>
<p><code>ALTER EXTENSION</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE EXTENSION (<code><a href="/docs/linux/man/7-create_extension/">CREATE_EXTENSION</a></code>(7)), DROP EXTENSION (<code><a href="/docs/linux/man/7-drop_extension/">DROP_EXTENSION</a></code>(7)) </p>
