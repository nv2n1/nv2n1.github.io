---
title: "create_conversion(7)"
name: "create_conversion"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_conversion/"
description: "CREATE CONVERSION – define a new encoding conversion"
---

<p>CREATE CONVERSION &#8211; define a new encoding conversion </p>
<h2>Synopsis</h2>
<pre>CREATE [ DEFAULT ] CONVERSION <i>name</i>
 FOR <i>source_encoding</i> TO <i>dest_encoding</i> FROM <i>funcname</i></pre>
<h2>Description</h2>
<p><code>CREATE CONVERSION</code> defines a new conversion between character set encodings. Also, conversions that are marked DEFAULT can be used for automatic encoding conversion between client and server. For this purpose, two conversions, from encoding A to B <code>and</code> from encoding B to A, must be defined. </p>
<p> To be able to create a conversion, you must have EXECUTE privilege on the function and CREATE privilege on the destination schema.</p>
<h2>Parameters</h2>
<dl>
<dt><code>DEFAULT</code></p>
<dd>The DEFAULT clause indicates that this conversion is the default for this particular source to destination encoding. There should be only one default encoding in a schema for the encoding pair.</p>
<dt><i>name</i></p>
<dd>The name of the conversion. The conversion name can be schema-qualified. If it is not, the conversion is defined in the current schema. The conversion name must be unique within a schema.</p>
<dt><i>source_encoding</i></p>
<dd>The source encoding name.</p>
<dt><i>dest_encoding</i></p>
<dd>The destination encoding name.</p>
<dt><i>funcname</i></p>
<dd>The function used to perform the conversion. The function name can be schema-qualified. If it is not, the function will be looked up in the path. </p>
<p> The function must have the following signature: </p>
<pre>conv_proc(
 integer, -- source encoding ID
 integer, -- destination encoding ID
 cstring, -- source string (null terminated C string)
 internal, -- destination (fill with a null terminated C string)
 integer -- source string length
) RETURNS void;</pre>
</dl>
<h2>Notes</h2>
<p>Use <code>DROP CONVERSION</code> to remove user-defined conversions. </p>
<p> The privileges required to create a conversion might be changed in a future release.</p>
<h2>Examples</h2>
<p>To create a conversion from encoding UTF8 to LATIN1 using <code>myfunc</code>: </p>
<pre>CREATE CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc;</pre>
<h2>Compatibility</h2>
<p><code>CREATE CONVERSION</code> is a PostgreSQL extension. There is no <code>CREATE CONVERSION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER CONVERSION [<code><a href="/docs/linux/man/7-alter_conversion/">alter_conversion</a></code>(7)], CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], DROP CONVERSION [<code><a href="/docs/linux/man/7-drop_conversion/">drop_conversion</a></code>(7)] </p>
