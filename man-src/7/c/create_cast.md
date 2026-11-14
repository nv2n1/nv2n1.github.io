---
title: "create_cast(7)"
name: "create_cast"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_cast/"
description: "CREATE CAST – define a new cast"
---

<p>CREATE CAST &#8211; define a new cast </p>
<h2>Synopsis</h2>
<pre>CREATE CAST (<i>sourcetype</i> AS <i>targettype</i>)
 WITH FUNCTION <i>funcname</i> (<i>argtypes</i>)
 [ AS ASSIGNMENT | AS IMPLICIT ]
CREATE CAST (<i>sourcetype</i> AS <i>targettype</i>)
 WITHOUT FUNCTION
 [ AS ASSIGNMENT | AS IMPLICIT ]
CREATE CAST (<i>sourcetype</i> AS <i>targettype</i>)
 WITH INOUT
 [ AS ASSIGNMENT | AS IMPLICIT ]</pre>
<h2>Description</h2>
<p><code>CREATE CAST</code> defines a new cast. A cast specifies how to perform a conversion between two data types. For example: </p>
<pre>SELECT CAST(42 AS float8);</pre>
<p>converts the integer constant 42 to type <code>float8</code> by invoking a previously specified function, in this case float8(int4). (If no suitable cast has been defined, the conversion fails.) </p>
<p> Two types can be <i>binary coercible</i>, which means that the conversion can be performed &#8220;for free&#8221; without invoking any function. This requires that corresponding values use the same internal representation. For instance, the types <code>text</code> and <code>varchar</code> are binary coercible both ways. Binary coercibility is not necessarily a symmetric relationship. For example, the cast from <code>xml</code> to <code>text</code> can be performed for free in the present implementation, but the reverse direction requires a function that performs at least a syntax check. (Two types that are binary coercible both ways are also referred to as binary compatible.) </p>
<p> You can define a cast as an <i>I/O conversion cast</i> using the WITH INOUT syntax. An I/O conversion cast is performed by invoking the output function of the source data type, and passing the result to the input function of the target data type. </p>
<p> By default, a cast can be invoked only by an explicit cast request, that is an explicit CAST(<i>x</i> AS <i>typename</i>) or <i>x</i>::<i>typename</i> construct. </p>
<p> If the cast is marked AS ASSIGNMENT then it can be invoked implicitly when assigning a value to a column of the target data type. For example, supposing that foo.f1 is a column of type <code>text</code>, then: </p>
<pre>INSERT INTO foo (f1) VALUES (42);</pre>
<p>will be allowed if the cast from type <code>integer</code> to type <code>text</code> is marked AS ASSIGNMENT, otherwise not. (We generally use the term <i>assignment cast</i> to describe this kind of cast.) </p>
<p> If the cast is marked AS IMPLICIT then it can be invoked implicitly in any context, whether assignment or internally in an expression. (We generally use the term <i>implicit cast</i> to describe this kind of cast.) For example, consider this query: </p>
<pre>SELECT 2 + 4.0;</pre>
<p>The parser initially marks the constants as being of type <code>integer</code> and <code>numeric</code> respectively. There is no <code>integer</code> + <code>numeric</code> operator in the system catalogs, but there is a <code>numeric</code> + <code>numeric</code> operator. The query will therefore succeed if a cast from <code>integer</code> to <code>numeric</code> is available and is marked AS IMPLICIT &#8212; which in fact it is. The parser will apply the implicit cast and resolve the query as if it had been written </p>
<pre>SELECT CAST ( 2 AS numeric ) + 4.0;</pre>
<p>Now, the catalogs also provide a cast from <code>numeric</code> to <code>integer</code>. If that cast were marked AS IMPLICIT &#8212; which it is not &#8212; then the parser would be faced with choosing between the above interpretation and the alternative of casting the <code>numeric</code> constant to <code>integer</code> and applying the <code>integer</code> + <code>integer</code> operator. Lacking any knowledge of which choice to prefer, it would give up and declare the query ambiguous. The fact that only one of the two casts is implicit is the way in which we teach the parser to prefer resolution of a mixed <code>numeric</code>-and-<code>integer</code> expression as <code>numeric</code>; there is no built-in knowledge about that. </p>
<p> It is wise to be conservative about marking casts as implicit. An overabundance of implicit casting paths can cause PostgreSQL to choose surprising interpretations of commands, or to be unable to resolve commands at all because there are multiple possible interpretations. A good rule of thumb is to make a cast implicitly invokable only for information-preserving transformations between types in the same general type category. For example, the cast from <code>int2</code> to <code>int4</code> can reasonably be implicit, but the cast from <code>float8</code> to <code>int4</code> should probably be assignment-only. Cross-type-category casts, such as <code>text</code> to <code>int4</code>, are best made explicit-only. </p>
<dl>
<dd><code>Note:</code> Sometimes it is necessary for usability or standards-compliance reasons to provide multiple implicit casts among a set of types, resulting in ambiguity that cannot be avoided as above. The parser has a fallback heuristic based on <i>type categories</i> and <i>preferred types</i> that can help to provide desired behavior in such cases. See CREATE TYPE [<code><a href="/docs/linux/man/7-create_type/">create_type</a></code>(7)] for more information.</dl>
<p> To be able to create a cast, you must own the source or the target data type. To create a binary-coercible cast, you must be superuser. (This restriction is made because an erroneous binary-coercible cast conversion can easily crash the server.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>sourcetype</i></p>
<dd>The name of the source data type of the cast.</p>
<dt><i>targettype</i></p>
<dd>The name of the target data type of the cast.</p>
<dt><i>funcname</i><code>(</code><i>argtypes</i><code>)</code></p>
<dd>The function used to perform the cast. The function name can be schema-qualified. If it is not, the function will be looked up in the schema search path. The function&#8217;s result data type must match the target type of the cast. Its arguments are discussed below.</p>
<dt><code>WITHOUT FUNCTION</code></p>
<dd>Indicates that the source type is binary-coercible to the target type, so no function is required to perform the cast.</p>
<dt><code>WITH INOUT</code></p>
<dd>Indicates that the cast is an I/O conversion cast, performed by invoking the output function of the source data type, and passing the result to the input function of the target data type.</p>
<dt><code>AS ASSIGNMENT</code></p>
<dd>Indicates that the cast can be invoked implicitly in assignment contexts.</p>
<dt><code>AS IMPLICIT</code></p>
<dd>Indicates that the cast can be invoked implicitly in any context.</dl>
<p> Cast implementation functions can have one to three arguments. The first argument type must be identical to or binary-coercible from the cast&#8217;s source type. The second argument, if present, must be type <code>integer</code>; it receives the type modifier associated with the destination type, or -1 if there is none. The third argument, if present, must be type <code>boolean</code>; it receives true if the cast is an explicit cast, false otherwise. (Bizarrely, the SQL standard demands different behaviors for explicit and implicit casts in some cases. This argument is supplied for functions that must implement such casts. It is not recommended that you design your own data types so that this matters.) </p>
<p> The return type of a cast function must be identical to or binary-coercible to the cast&#8217;s target type. </p>
<p> Ordinarily a cast must have different source and target data types. However, it is allowed to declare a cast with identical source and target types if it has a cast implementation function with more than one argument. This is used to represent type-specific length coercion functions in the system catalogs. The named function is used to coerce a value of the type to the type modifier value given by its second argument. </p>
<p> When a cast has different source and target types and a function that takes more than one argument, it represents converting from one type to another and applying a length coercion in a single step. When no such entry is available, coercion to a type that uses a type modifier involves two steps, one to convert between data types and a second to apply the modifier.</p>
<h2>Notes</h2>
<p>Use DROP CAST [<code><a href="/docs/linux/man/7-drop_cast/">drop_cast</a></code>(7)] to remove user-defined casts. Remember that if you want to be able to convert types both ways you need to declare casts both ways explicitly. It is normally not necessary to create casts between user-defined types and the standard string types (<code>text</code>, <code>varchar</code>, and <code>char(</code><i>n</i><code>)</code>, as well as user-defined types that are defined to be in the string category). PostgreSQL provides automatic I/O conversion casts for that. The automatic casts to string types are treated as assignment casts, while the automatic casts from string types are explicit-only. You can override this behavior by declaring your own cast to replace an automatic cast, but usually the only reason to do so is if you want the conversion to be more easily invokable than the standard assignment-only or explicit-only setting. Another possible reason is that you want the conversion to behave differently from the type&#8217;s I/O function; but that is sufficiently surprising that you should think twice about whether it&#8217;s a good idea. (A small number of the built-in types do indeed have different behaviors for conversions, mostly because of requirements of the SQL standard.) Prior to PostgreSQL 7.3, every function that had the same name as a data type, returned that data type, and took one argument of a different type was automatically a cast function. This convention has been abandoned in face of the introduction of schemas and to be able to represent binary-coercible casts in the system catalogs. The built-in cast functions still follow this naming scheme, but they have to be shown as casts in the system catalog <code>pg_cast</code> as well. While not required, it is recommended that you continue to follow this old convention of naming cast implementation functions after the target data type. Many users are used to being able to cast data types using a function-style notation, that is <i>typename</i>(<i>x</i>). This notation is in fact nothing more nor less than a call of the cast implementation function; it is not specially treated as a cast. If your conversion functions are not named to support this convention then you will have surprised users. Since PostgreSQL allows overloading of the same function name with different argument types, there is no difficulty in having multiple conversion functions from different types that all use the target type&#8217;s name.</p>
<dl>
<dd><code>Note:</code> Actually the preceding paragraph is an oversimplification: there are two cases in which a function-call construct will be treated as a cast request without having matched it to an actual function. If a function call <i>name</i>(<i>x</i>) does not exactly match any existing function, but <i>name</i> is the name of a data type and <code>pg_cast</code> provides a binary-coercible cast to this type from the type of <i>x</i>, then the call will be construed as a binary-coercible cast. This exception is made so that binary-coercible casts can be invoked using functional syntax, even though they lack any function. Likewise, if there is no <code>pg_cast</code> entry but the cast would be to or from a string type, the call will be construed as an I/O conversion cast. This exception allows I/O conversion casts to be invoked using functional syntax.</dl>
<h2>Examples</h2>
<p>To create an assignment cast from type <code>bigint</code> to type <code>int4</code> using the function int4(bigint): </p>
<pre>CREATE CAST (bigint AS int4) WITH FUNCTION int4(bigint) AS ASSIGNMENT;</pre>
<p>(This cast is already predefined in the system.)</p>
<h2>Compatibility</h2>
<p>The <code>CREATE CAST</code> command conforms to the SQL standard, except that SQL does not make provisions for binary-coercible types or extra arguments to implementation functions. AS IMPLICIT is a PostgreSQL extension, too.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], CREATE TYPE [<code><a href="/docs/linux/man/7-create_type/">create_type</a></code>(7)], DROP CAST [<code><a href="/docs/linux/man/7-drop_cast/">drop_cast</a></code>(7)] </p>
