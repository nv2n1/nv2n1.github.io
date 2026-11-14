---
title: "security_label(7)"
name: "security_label"
section: "7"
letter: "s"
url: "/docs/linux/man/7-security_label/"
description: "SECURITY_LABEL – define or change a security label applied to an object"
---

<p>SECURITY_LABEL &#8211; define or change a security label applied to an object</p>
<h2>Synopsis</h2>
<pre>SECURITY LABEL [ FOR <i>provider</i> ] ON
{
 TABLE <i>object_name</i> |
 COLUMN <i>table_name</i>.<i>column_name</i> |
 AGGREGATE <i>agg_name</i> (<i>agg_type</i> [, ...] ) |
 DATABASE <i>object_name</i> |
 DOMAIN <i>object_name</i> |
 FOREIGN TABLE <i>object_name</i>
 FUNCTION <i>function_name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] ) |
 LARGE OBJECT <i>large_object_oid</i> |
 [ PROCEDURAL ] LANGUAGE <i>object_name</i> |
 ROLE <i>object_name</i> |
 SCHEMA <i>object_name</i> |
 SEQUENCE <i>object_name</i> |
 TABLESPACE <i>object_name</i> |
 TYPE <i>object_name</i> |
 VIEW <i>object_name</i>
} IS '<i>label</i>'</pre>
<h2>Description</h2>
<p><code>SECURITY LABEL</code> applies a security label to a database object. An arbitrary number of security labels, one per label provider, can be associated with a given database object. Label providers are loadable modules which register themselves by using the function <code>register_label_provider</code>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>register_label_provider</code> is not an SQL function; it can only be called from C code loaded into the backend.  The label provider determines whether a given label is valid and whether it is permissible to assign that label to a given object. The meaning of a given label is likewise at the discretion of the label provider. PostgreSQL places no restrictions on whether or how a label provider must interpret security labels; it merely provides a mechanism for storing them. In practice, this facility is intended to allow integration with label-based mandatory access control (MAC) systems such as SE-Linux. Such systems make all access control decisions based on object labels, rather than traditional discretionary access control (DAC) concepts such as users and groups.</p>
<h2>Parameters</h2>
<p><i>object_name</i>, <i>table_name.column_name</i>, <i>agg_name</i>, <i>function_name</i></p>
<dl>
<dd>The name of the object to be labeled. Names of tables, aggregates, domains, foreign tables, functions, sequences, types, and views can be schema-qualified.</dl>
<p> <i>provider</i></p>
<dl>
<dd>The name of the provider with which this label is to be associated. The named provider must be loaded and must consent to the proposed labeling operation. If exactly one provider is loaded, the provider name may be omitted for brevity.</dl>
<p> <i>arg_type</i></p>
<dl>
<dd>An input data type on which the aggregate function operates. To reference a zero-argument aggregate function, write * in place of the list of input data types.</dl>
<p> <i>argmode</i></p>
<dl>
<dd>The mode of a function argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Note that <code>SECURITY LABEL ON FUNCTION</code> does not actually pay any attention to OUT arguments, since only the input arguments are needed to determine the function&#8217;s identity. So it is sufficient to list the IN, INOUT, and VARIADIC arguments.</dl>
<p> <i>argname</i></p>
<dl>
<dd>The name of a function argument. Note that <code>SECURITY LABEL ON FUNCTION</code> does not actually pay any attention to argument names, since only the argument data types are needed to determine the function&#8217;s identity.</dl>
<p> <i>argtype</i></p>
<dl>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any.</dl>
<p> <i>large_object_oid</i></p>
<dl>
<dd>The OID of the large object.</dl>
<p> PROCEDURAL</p>
<dl>
<dd>This is a noise word.</dl>
<p> <i>label</i></p>
<dl>
<dd>The new security label, written as a string literal; or NULL to drop the security label.</dl>
<h2>Examples</h2>
<p>The following example shows how the security label of a table might be changed. </p>
<dl>
<dd>
<pre>SECURITY LABEL FOR selinux ON TABLE mytable IS 'system_u:object_r:sepgsql_table_t:s0';</pre>
</dl>
<h2>Compatibility</h2>
<p>There is no <code>SECURITY LABEL</code> command in the SQL standard.</p>
<h2>See Also</h2>
<p>sepgsql, dummy_seclabel </p>
