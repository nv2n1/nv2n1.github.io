---
title: "alter_function(7)"
name: "alter_function"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_function/"
description: "ALTER FUNCTION – change the definition of a function"
---

<p>ALTER FUNCTION &#8211; change the definition of a function </p>
<h2>Synopsis</h2>
<pre>ALTER FUNCTION <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] )
 <i>action</i> [ ... ] [ RESTRICT ]
ALTER FUNCTION <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] )
 RENAME TO <i>new_name</i>
ALTER FUNCTION <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] )
 OWNER TO <i>new_owner</i>
ALTER FUNCTION <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [, ...] ] )
 SET SCHEMA <i>new_schema</i>
where <i>action</i> is one of:
 CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
 IMMUTABLE | STABLE | VOLATILE
 [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
 COST <i>execution_cost</i>
 ROWS <i>result_rows</i>
 SET <i>configuration_parameter</i> { TO | = } { <i>value</i> | DEFAULT }
 SET <i>configuration_parameter</i> FROM CURRENT
 RESET <i>configuration_parameter</i>
 RESET ALL</pre>
<h2>Description</h2>
<p><code>ALTER FUNCTION</code> changes the definition of a function. </p>
<p> You must own the function to use <code>ALTER FUNCTION</code>. To change a function&#8217;s schema, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the function&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the function. However, a superuser can alter ownership of any function anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing function.</p>
<dt><i>argmode</i></p>
<dd>The mode of an argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Note that <code>ALTER FUNCTION</code> does not actually pay any attention to OUT arguments, since only the input arguments are needed to determine the function&#8217;s identity. So it is sufficient to list the IN, INOUT, and VARIADIC arguments.</p>
<dt><i>argname</i></p>
<dd>The name of an argument. Note that <code>ALTER FUNCTION</code> does not actually pay any attention to argument names, since only the argument data types are needed to determine the function&#8217;s identity.</p>
<dt><i>argtype</i></p>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any.</p>
<dt><i>new_name</i></p>
<dd>The new name of the function.</p>
<dt><i>new_owner</i></p>
<dd>The new owner of the function. Note that if the function is marked SECURITY DEFINER, it will subsequently execute as the new owner.</p>
<dt><i>new_schema</i></p>
<dd>The new schema for the function.</p>
<dt><code>CALLED ON NULL INPUT</code></p>
<dd>
<dt><code>RETURNS NULL ON NULL INPUT</code></p>
<dd>
<dt><code>STRICT</code></p>
<dd>CALLED ON NULL INPUT changes the function so that it will be invoked when some or all of its arguments are null. RETURNS NULL ON NULL INPUT or STRICT changes the function so that it is not invoked if any of its arguments are null; instead, a null result is assumed automatically. See CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] for more information.</p>
<dt><code>IMMUTABLE</code></p>
<dd>
<dt><code>STABLE</code></p>
<dd>
<dt><code>VOLATILE</code></p>
<dd>Change the volatility of the function to the specified setting. See CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] for details.</p>
<dt><code>[ EXTERNAL ] SECURITY INVOKER</code></p>
<dd>
<dt><code>[ EXTERNAL ] SECURITY DEFINER</code></p>
<dd>Change whether the function is a security definer or not. The key word EXTERNAL is ignored for SQL conformance. See CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] for more information about this capability.</p>
<dt><code>COST </code><i>execution_cost</i></p>
<dd>Change the estimated execution cost of the function. See CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] for more information.</p>
<dt><code>ROWS </code><i>result_rows</i></p>
<dd>Change the estimated number of rows returned by a set-returning function. See CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] for more information.</p>
<dt><i>configuration_parameter</i></p>
<dd>
<dt><i>value</i></p>
<dd>Add or change the assignment to be made to a configuration parameter when the function is called. If <i>value</i> is DEFAULT or, equivalently, RESET is used, the function-local setting is removed, so that the function executes with the value present in its environment. Use RESET ALL to clear all function-local settings. SET FROM CURRENT saves the session&#8217;s current value of the parameter as the value to be applied when the function is entered. </p>
<p> See SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] and in the documentation for more information about allowed parameter names and values.</p>
<dt><code>RESTRICT</code></p>
<dd>Ignored for conformance with the SQL standard.</dl>
<h2>Examples</h2>
<p>To rename the function sqrt for type <code>integer</code> to square_root: </p>
<pre>ALTER FUNCTION sqrt(integer) RENAME TO square_root;</pre>
<p>To change the owner of the function sqrt for type <code>integer</code> to joe: </p>
<pre>ALTER FUNCTION sqrt(integer) OWNER TO joe;</pre>
<p>To change the schema of the function sqrt for type <code>integer</code> to maths: </p>
<pre>ALTER FUNCTION sqrt(integer) SET SCHEMA maths;</pre>
<p>To adjust the search path that is automatically set for a function: </p>
<pre><code>ALTER FUNCTION check_password(text) SET search_path = admin, pg_temp;</code></pre>
<p> To disable automatic setting of search_path for a function: </p>
<pre>ALTER FUNCTION check_password(text) RESET search_path;</pre>
<p>The function will now execute with whatever search path is used by its caller.</p>
<h2>Compatibility</h2>
<p>This statement is partially compatible with the <code>ALTER FUNCTION</code> statement in the SQL standard. The standard allows more properties of a function to be modified, but does not provide the ability to rename a function, make a function a security definer, attach configuration parameter values to a function, or change the owner, schema, or volatility of a function. The standard also requires the RESTRICT key word, which is optional in PostgreSQL.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], DROP FUNCTION [<code><a href="/docs/linux/man/7-drop_function/">drop_function</a></code>(7)] </p>
