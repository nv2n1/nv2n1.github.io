---
title: "alter_operator_family(7)"
name: "alter_operator_family"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_operator_family/"
description: "ALTER OPERATOR FAMILY – change the definition of an operator family"
---

<p>ALTER OPERATOR FAMILY &#8211; change the definition of an operator family </p>
<h2>Synopsis</h2>
<pre>ALTER OPERATOR FAMILY <i>name</i> USING <i>index_method</i> ADD
 { OPERATOR <i>strategy_number</i> <i>operator_name</i> ( <i>op_type</i>, <i>op_type</i> )
 | FUNCTION <i>support_number</i> [ ( <i>op_type</i> [ , <i>op_type</i> ] ) ] <i>funcname</i> ( <i>argument_type</i> [, ...] )
 } [, ... ]
ALTER OPERATOR FAMILY <i>name</i> USING <i>index_method</i> DROP
 { OPERATOR <i>strategy_number</i> ( <i>op_type</i> [ , <i>op_type</i> ] )
 | FUNCTION <i>support_number</i> ( <i>op_type</i> [ , <i>op_type</i> ] )
 } [, ... ]
ALTER OPERATOR FAMILY <i>name</i> USING <i>index_method</i> RENAME TO <i>newname</i>
ALTER OPERATOR FAMILY <i>name</i> USING <i>index_method</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER OPERATOR FAMILY</code> changes the definition of an operator family. You can add operators and support functions to the family, remove them from the family, or change the family&#8217;s name or owner. </p>
<p> When operators and support functions are added to a family with <code>ALTER OPERATOR FAMILY</code>, they are not part of any specific operator class within the family, but are just &#8220;loose&#8221; within the family. This indicates that these operators and functions are compatible with the family&#8217;s semantics, but are not required for correct functioning of any specific index. (Operators and functions that are so required should be declared as part of an operator class, instead; see CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)].) PostgreSQL will allow loose members of a family to be dropped from the family at any time, but members of an operator class cannot be dropped without dropping the whole class and any indexes that depend on it. Typically, single-data-type operators and functions are part of operator classes because they are needed to support an index on that specific data type, while cross-data-type operators and functions are made loose members of the family. </p>
<p> You must be a superuser to use <code>ALTER OPERATOR FAMILY</code>. (This restriction is made because an erroneous operator family definition could confuse or even crash the server.) </p>
<p> <code>ALTER OPERATOR FAMILY</code> does not presently check whether the operator family definition includes all the operators and functions required by the index method, nor whether the operators and functions form a self-consistent set. It is the user&#8217;s responsibility to define a valid operator family. </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing operator family.</p>
<dt><i>index_method</i></p>
<dd>The name of the index method this operator family is for.</p>
<dt><i>strategy_number</i></p>
<dd>The index method&#8217;s strategy number for an operator associated with the operator family.</p>
<dt><i>operator_name</i></p>
<dd>The name (optionally schema-qualified) of an operator associated with the operator family.</p>
<dt><i>op_type</i></p>
<dd>In an OPERATOR clause, the operand data type(s) of the operator, or NONE to signify a left-unary or right-unary operator. Unlike the comparable syntax in <code>CREATE OPERATOR CLASS</code>, the operand data types must always be specified. </p>
<p> In an ADD FUNCTION clause, the operand data type(s) the function is intended to support, if different from the input data type(s) of the function. For B-tree and hash indexes it is not necessary to specify <i>op_type</i> since the function&#8217;s input data type(s) are always the correct ones to use. For GIN and GiST indexes it is necessary to specify the input data type the function is to be used with. </p>
<p> In a DROP FUNCTION clause, the operand data type(s) the function is intended to support must be specified.</p>
<dt><i>support_number</i></p>
<dd>The index method&#8217;s support procedure number for a function associated with the operator family.</p>
<dt><i>funcname</i></p>
<dd>The name (optionally schema-qualified) of a function that is an index method support procedure for the operator family.</p>
<dt><i>argument_types</i></p>
<dd>The parameter data type(s) of the function.</p>
<dt><i>newname</i></p>
<dd>The new name of the operator family.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the operator family.</dl>
<p> The OPERATOR and FUNCTION clauses can appear in any order.</p>
<h2>Notes</h2>
<p>Notice that the DROP syntax only specifies the &#8220;slot&#8221; in the operator family, by strategy or support number and input data type(s). The name of the operator or function occupying the slot is not mentioned. Also, for DROP FUNCTION the type(s) to specify are the input data type(s) the function is intended to support; for GIN and GiST indexes this might have nothing to do with the actual input argument types of the function. </p>
<p> Because the index machinery does not check access permissions on functions before using them, including a function or operator in an operator family is tantamount to granting public execute permission on it. This is usually not an issue for the sorts of functions that are useful in an operator family. </p>
<p> The operators should not be defined by SQL functions. A SQL function is likely to be inlined into the calling query, which will prevent the optimizer from recognizing that the query matches an index. </p>
<p> Before PostgreSQL 8.4, the OPERATOR clause could include a RECHECK option. This is no longer supported because whether an index operator is &#8220;lossy&#8221; is now determined on-the-fly at runtime. This allows efficient handling of cases where an operator might or might not be lossy.</p>
<h2>Examples</h2>
<p>The following example command adds cross-data-type operators and support functions to an operator family that already contains B-tree operator classes for data types <code>int4</code> and <code>int2</code>. </p>
<pre><code>ALTER OPERATOR FAMILY integer_ops USING btree ADD

-- int4 vs int2
OPERATOR 1 &lt; (int4, int2) ,
OPERATOR 2 &lt;= (int4, int2) ,
OPERATOR 3 = (int4, int2) ,
OPERATOR 4 &gt;= (int4, int2) ,
OPERATOR 5 &gt; (int4, int2) ,
FUNCTION 1 btint42cmp(int4, int2) ,

-- int2 vs int4
OPERATOR 1 &lt; (int2, int4) ,
OPERATOR 2 &lt;= (int2, int4) ,
OPERATOR 3 = (int2, int4) ,
OPERATOR 4 &gt;= (int2, int4) ,
OPERATOR 5 &gt; (int2, int4) ,
FUNCTION 1 btint24cmp(int2, int4) ;</code></pre>
<p> To remove these entries again: </p>
<pre>ALTER OPERATOR FAMILY integer_ops USING btree DROP
 -- int4 vs int2
 OPERATOR 1 (int4, int2) ,
 OPERATOR 2 (int4, int2) ,
 OPERATOR 3 (int4, int2) ,
 OPERATOR 4 (int4, int2) ,
 OPERATOR 5 (int4, int2) ,
 FUNCTION 1 (int4, int2) ,
 -- int2 vs int4
 OPERATOR 1 (int2, int4) ,
 OPERATOR 2 (int2, int4) ,
 OPERATOR 3 (int2, int4) ,
 OPERATOR 4 (int2, int4) ,
 OPERATOR 5 (int2, int4) ,
 FUNCTION 1 (int2, int4) ;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER OPERATOR FAMILY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE OPERATOR FAMILY [<code><a href="/docs/linux/man/7-create_operator_family/">create_operator_family</a></code>(7)], DROP OPERATOR FAMILY [<code><a href="/docs/linux/man/7-drop_operator_family/">drop_operator_family</a></code>(7)], CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], ALTER OPERATOR CLASS [<code><a href="/docs/linux/man/7-alter_operator_class/">alter_operator_class</a></code>(7)], DROP OPERATOR CLASS [<code><a href="/docs/linux/man/7-drop_operator_class/">drop_operator_class</a></code>(7)] </p>
