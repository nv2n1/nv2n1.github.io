---
title: "create_operator(7)"
name: "create_operator"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_operator/"
description: "CREATE OPERATOR – define a new operator"
---

<p>CREATE OPERATOR &#8211; define a new operator </p>
<h2>Synopsis</h2>
<pre>CREATE OPERATOR <i>name</i> (
 PROCEDURE = <i>funcname</i>
 [, LEFTARG = <i>lefttype</i> ] [, RIGHTARG = <i>righttype</i> ]
 [, COMMUTATOR = <i>com_op</i> ] [, NEGATOR = <i>neg_op</i> ]
 [, RESTRICT = <i>res_proc</i> ] [, JOIN = <i>join_proc</i> ]
 [, HASHES ] [, MERGES ]
)</pre>
<h2>Description</h2>
<p><code>CREATE OPERATOR</code> defines a new operator, <i>name</i>. The user who defines an operator becomes its owner. If a schema name is given then the operator is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> The operator name is a sequence of up to <code>NAMEDATALEN</code>-1 (63 by default) characters from the following list: </p>
<pre>+ - * / &lt; &gt; = ~ ! @ # % ^ &amp; | ` ?</pre>
<p>There are a few restrictions on your choice of name:</p>
<dl>
<dt>*</p>
<dd>&#8212; and /* cannot appear anywhere in an operator name, since they will be taken as the start of a comment.</p>
<dt>*</p>
<dd>A multicharacter operator name cannot end in + or -, unless the name also contains at least one of these characters: </p>
<pre>~ ! @ # % ^ &amp; | ` ?</pre>
<p>For example, @- is an allowed operator name, but *- is not. This restriction allows PostgreSQL to parse SQL-compliant commands without requiring spaces between tokens.</dl>
<p> The operator != is mapped to &lt;&gt; on input, so these two names are always equivalent. </p>
<p> At least one of LEFTARG and RIGHTARG must be defined. For binary operators, both must be defined. For right unary operators, only LEFTARG should be defined, while for left unary operators only RIGHTARG should be defined. </p>
<p> The <i>funcname</i> procedure must have been previously defined using <code>CREATE FUNCTION</code> and must be defined to accept the correct number of arguments (either one or two) of the indicated types. </p>
<p> The other clauses specify optional operator optimization clauses. Their meaning is detailed in in the documentation.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the operator to be defined. See above for allowable characters. The name can be schema-qualified, for example CREATE OPERATOR myschema.+ (&#8230;). If not, then the operator is created in the current schema. Two operators in the same schema can have the same name if they operate on different data types. This is called <i>overloading</i>.</p>
<dt><i>funcname</i></p>
<dd>The function used to implement this operator.</p>
<dt><i>lefttype</i></p>
<dd>The data type of the operator&#8217;s left operand, if any. This option would be omitted for a left-unary operator.</p>
<dt><i>righttype</i></p>
<dd>The data type of the operator&#8217;s right operand, if any. This option would be omitted for a right-unary operator.</p>
<dt><i>com_op</i></p>
<dd>The commutator of this operator.</p>
<dt><i>neg_op</i></p>
<dd>The negator of this operator.</p>
<dt><i>res_proc</i></p>
<dd>The restriction selectivity estimator function for this operator.</p>
<dt><i>join_proc</i></p>
<dd>The join selectivity estimator function for this operator.</p>
<dt><code>HASHES</code></p>
<dd>Indicates this operator can support a hash join.</p>
<dt><code>MERGES</code></p>
<dd>Indicates this operator can support a merge join.</dl>
<p> To give a schema-qualified operator name in <i>com_op</i> or the other optional arguments, use the OPERATOR() syntax, for example: </p>
<pre>COMMUTATOR = OPERATOR(myschema.===) ,</pre>
<h2>Notes</h2>
<p>Refer to in the documentation for further information. </p>
<p> The obsolete options SORT1, SORT2, LTCMP, and GTCMP were formerly used to specify the names of sort operators associated with a merge-joinable operator. This is no longer necessary, since information about associated operators is found by looking at B-tree operator families instead. If one of these options is given, it is ignored except for implicitly setting MERGES true. </p>
<p> Use DROP OPERATOR [<code><a href="/docs/linux/man/7-drop_operator/">drop_operator</a></code>(7)] to delete user-defined operators from a database. Use ALTER OPERATOR [<code><a href="/docs/linux/man/7-alter_operator/">alter_operator</a></code>(7)] to modify operators in a database.</p>
<h2>Examples</h2>
<p>The following command defines a new operator, area-equality, for the data type <code>box</code>: </p>
<pre><code>CREATE OPERATOR === (
LEFTARG = box,
RIGHTARG = box,
PROCEDURE = area_equal_procedure,
COMMUTATOR = ===,
NEGATOR = !==,
RESTRICT = area_restriction_procedure,
JOIN = area_join_procedure,
HASHES, MERGES
);</code></pre>
<h2>Compatibility</h2>
<p><code>CREATE OPERATOR</code> is a PostgreSQL extension. There are no provisions for user-defined operators in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER OPERATOR [<code><a href="/docs/linux/man/7-alter_operator/">alter_operator</a></code>(7)], CREATE OPERATOR CLASS [<code><a href="/docs/linux/man/7-create_operator_class/">create_operator_class</a></code>(7)], DROP OPERATOR [<code><a href="/docs/linux/man/7-drop_operator/">drop_operator</a></code>(7)] </p>
