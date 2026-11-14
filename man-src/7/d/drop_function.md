---
title: "drop_function(7)"
name: "drop_function"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_function/"
description: "DROP FUNCTION – remove a function"
---

<p>DROP FUNCTION &#8211; remove a function </p>
<h2>Synopsis</h2>
<pre>DROP FUNCTION [ IF EXISTS ] <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] )
 [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP FUNCTION</code> removes the definition of an existing function. To execute this command the user must be the owner of the function. The argument types to the function must be specified, since several different functions can exist with the same name and different argument lists.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the function does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing function.</p>
<dt><i>argmode</i></p>
<dd>The mode of an argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Note that <code>DROP FUNCTION</code> does not actually pay any attention to OUT arguments, since only the input arguments are needed to determine the function&#8217;s identity. So it is sufficient to list the IN, INOUT, and VARIADIC arguments.</p>
<dt><i>argname</i></p>
<dd>The name of an argument. Note that <code>DROP FUNCTION</code> does not actually pay any attention to argument names, since only the argument data types are needed to determine the function&#8217;s identity.</p>
<dt><i>argtype</i></p>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the function (such as operators or triggers).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the function if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>This command removes the square root function: </p>
<pre>DROP FUNCTION sqrt(integer);</pre>
<h2>Compatibility</h2>
<p>A <code>DROP FUNCTION</code> statement is defined in the SQL standard, but it is not compatible with this command.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], ALTER FUNCTION [<code><a href="/docs/linux/man/7-alter_function/">alter_function</a></code>(7)] </p>
