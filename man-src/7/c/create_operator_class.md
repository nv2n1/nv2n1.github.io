---
title: "create_operator_class(7)"
name: "create_operator_class"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_operator_class/"
description: "CREATE OPERATOR CLASS – define a new operator class"
---

<p>CREATE OPERATOR CLASS &#8211; define a new operator class </p>
<h2>Synopsis</h2>
<pre>CREATE OPERATOR CLASS <i>name</i> [ DEFAULT ] FOR TYPE <i>data_type</i>
 USING <i>index_method</i> [ FAMILY <i>family_name</i> ] AS
 { OPERATOR <i>strategy_number</i> <i>operator_name</i> [ ( <i>op_type</i>, <i>op_type</i> ) ]
 | FUNCTION <i>support_number</i> [ ( <i>op_type</i> [ , <i>op_type</i> ] ) ] <i>funcname</i> ( <i>argument_type</i> [, ...] )
 | STORAGE <i>storage_type</i>
 } [, ... ]</pre>
<h2>Description</h2>
<p><code>CREATE OPERATOR CLASS</code> creates a new operator class. An operator class defines how a particular data type can be used with an index. The operator class specifies that certain operators will fill particular roles or &#8220;strategies&#8221; for this data type and this index method. The operator class also specifies the support procedures to be used by the index method when the operator class is selected for an index column. All the operators and functions used by an operator class must be defined before the operator class can be created. </p>
<p> If a schema name is given then the operator class is created in the specified schema. Otherwise it is created in the current schema. Two operator classes in the same schema can have the same name only if they are for different index methods. </p>
<p> The user who defines an operator class becomes its owner. Presently, the creating user must be a superuser. (This restriction is made because an erroneous operator class definition could confuse or even crash the server.) </p>
<p> <code>CREATE OPERATOR CLASS</code> does not presently check whether the operator class definition includes all the operators and functions required by the index method, nor whether the operators and functions form a self-consistent set. It is the user&#8217;s responsibility to define a valid operator class. </p>
<p> Related operator classes can be grouped into <i>operator families</i>. To add a new operator class to an existing family, specify the FAMILY option in <code>CREATE OPERATOR CLASS</code>. Without this option, the new class is placed into a family named the same as the new class (creating that family if it doesn&#8217;t already exist). </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the operator class to be created. The name can be schema-qualified.</p>
<dt><code>DEFAULT</code></p>
<dd>If present, the operator class will become the default operator class for its data type. At most one operator class can be the default for a specific data type and index method.</p>
<dt><i>data_type</i></p>
<dd>The column data type that this operator class is for.</p>
<dt><i>index_method</i></p>
<dd>The name of the index method this operator class is for.</p>
<dt><i>family_name</i></p>
<dd>The name of the existing operator family to add this operator class to. If not specified, a family named the same as the operator class is used (creating it, if it doesn&#8217;t already exist).</p>
<dt><i>strategy_number</i></p>
<dd>The index method&#8217;s strategy number for an operator associated with the operator class.</p>
<dt><i>operator_name</i></p>
<dd>The name (optionally schema-qualified) of an operator associated with the operator class.</p>
<dt><i>op_type</i></p>
<dd>In an OPERATOR clause, the operand data type(s) of the operator, or NONE to signify a left-unary or right-unary operator. The operand data types can be omitted in the normal case where they are the same as the operator class&#8217;s data type. </p>
<p> In a FUNCTION clause, the operand data type(s) the function is intended to support, if different from the input data type(s) of the function (for B-tree and hash indexes) or the class&#8217;s data type (for GIN and GiST indexes). These defaults are always correct, so there is no point in specifying <i>op_type</i> in a FUNCTION clause in <code>CREATE OPERATOR CLASS</code>, but the option is provided for consistency with the comparable syntax in <code>ALTER OPERATOR FAMILY</code>.</p>
<dt><i>support_number</i></p>
<dd>The index method&#8217;s support procedure number for a function associated with the operator class.</p>
<dt><i>funcname</i></p>
<dd>The name (optionally schema-qualified) of a function that is an index method support procedure for the operator class.</p>
<dt><i>argument_types</i></p>
<dd>The parameter data type(s) of the function.</p>
<dt><i>storage_type</i></p>
<dd>The data type actually stored in the index. Normally this is the same as the column data type, but some index methods (currently GIN and GiST) allow it to be different. The STORAGE clause must be omitted unless the index method allows a different type to be used.</dl>
<p> The OPERATOR, FUNCTION, and STORAGE clauses can appear in any order.</p>
<h2>Notes</h2>
<p>Because the index machinery does not check access permissions on functions before using them, including a function or operator in an operator class is tantamount to granting public execute permission on it. This is usually not an issue for the sorts of functions that are useful in an operator class. </p>
<p> The operators should not be defined by SQL functions. A SQL function is likely to be inlined into the calling query, which will prevent the optimizer from recognizing that the query matches an index. </p>
<p> Before PostgreSQL 8.4, the OPERATOR clause could include a RECHECK option. This is no longer supported because whether an index operator is &#8220;lossy&#8221; is now determined on-the-fly at runtime. This allows efficient handling of cases where an operator might or might not be lossy.</p>
<h2>Examples</h2>
<p>The following example command defines a GiST index operator class for the data type _int4 (array of <code>int4</code>). See <i>contrib/intarray/</i> for the complete example. </p>
<pre><code>CREATE OPERATOR CLASS gist__int_ops
    DEFAULT FOR TYPE _int4 USING gist AS
        OPERATOR 3 &amp;&amp;,
    OPERATOR 6 = (anyarray, anyarray),
             OPERATOR 7 @ &gt;,
             OPERATOR 8 &lt; @,
             OPERATOR 20 @ @(_int4, query_int),
             FUNCTION 1 g_int_consistent(internal, _int4, int, oid, internal),
             FUNCTION 2 g_int_union(internal, internal),
             FUNCTION 3 g_int_compress(internal),
             FUNCTION 4 g_int_decompress(internal),
             FUNCTION 5 g_int_penalty(internal, internal, internal),
             FUNCTION 6 g_int_picksplit(internal, internal),
             FUNCTION 7 g_int_same(_int4, _int4, internal);</code></pre>
<h2>Compatibility</h2>
<p><code>CREATE OPERATOR CLASS</code> is a PostgreSQL extension. There is no <code>CREATE OPERATOR CLASS</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER OPERATOR CLASS [<code><a href="/docs/linux/man/7-alter_operator_class/">alter_operator_class</a></code>(7)], DROP OPERATOR CLASS [<code><a href="/docs/linux/man/7-drop_operator_class/">drop_operator_class</a></code>(7)], CREATE OPERATOR FAMILY [<code><a href="/docs/linux/man/7-create_operator_family/">create_operator_family</a></code>(7)], ALTER OPERATOR FAMILY [<code><a href="/docs/linux/man/7-alter_operator_family/">alter_operator_family</a></code>(7)] </p>
