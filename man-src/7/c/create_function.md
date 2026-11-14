---
title: "create_function(7)"
name: "create_function"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_function/"
description: "CREATE FUNCTION – define a new function"
---

<p>CREATE FUNCTION &#8211; define a new function </p>
<h2>Synopsis</h2>
<pre>CREATE [ OR REPLACE ] FUNCTION
 <i>name</i> ( [ [ <i>argmode</i> ] [ <i>argname</i> ] <i>argtype</i> [ { DEFAULT | = } <i>defexpr</i> ] [, ...] ] )
 [ RETURNS <i>rettype</i>
 | RETURNS TABLE ( <i>colname</i> <i>coltype</i> [, ...] ) ]
 { LANGUAGE <i>langname</i>
 | WINDOW
 | IMMUTABLE | STABLE | VOLATILE
 | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
 | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
 | COST <i>execution_cost</i>
 | ROWS <i>result_rows</i>
 | SET <i>configuration_parameter</i> { TO <i>value</i> | = <i>value</i> | FROM CURRENT }
 | AS '<i>definition</i>'
 | AS '<i>obj_file</i>', '<i>link_symbol</i>'
 } ...
 [ WITH ( <i>attribute</i> [, ...] ) ]</pre>
<h2>Description</h2>
<p><code>CREATE FUNCTION</code> defines a new function. <code>CREATE OR REPLACE FUNCTION</code> will either create a new function, or replace an existing definition. </p>
<p> If a schema name is included, then the function is created in the specified schema. Otherwise it is created in the current schema. The name of the new function must not match any existing function with the same input argument types in the same schema. However, functions of different argument types can share a name (this is called <i>overloading</i>). </p>
<p> To replace the current definition of an existing function, use <code>CREATE OR REPLACE FUNCTION</code>. It is not possible to change the name or argument types of a function this way (if you tried, you would actually be creating a new, distinct function). Also, <code>CREATE OR REPLACE FUNCTION</code> will not let you change the return type of an existing function. To do that, you must drop and recreate the function. (When using OUT parameters, that means you cannot change the names or types of any OUT parameters except by dropping the function.) </p>
<p> If you drop and then recreate a function, the new function is not the same entity as the old; you will have to drop existing rules, views, triggers, etc. that refer to the old function. Use <code>CREATE OR REPLACE FUNCTION</code> to change a function definition without breaking objects that refer to the function. Also, <code>ALTER FUNCTION</code> can be used to change most of the auxiliary properties of an existing function. </p>
<p> The user that creates the function becomes the owner of the function.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the function to create.</p>
<dt><i>argmode</i></p>
<dd>The mode of an argument: IN, OUT, INOUT, or VARIADIC. If omitted, the default is IN. Only OUT arguments can follow a VARIADIC one. Also, OUT and INOUT arguments cannot be used together with the RETURNS TABLE notation.</p>
<dt><i>argname</i></p>
<dd>The name of an argument. Some languages (currently only PL/pgSQL) let you use the name in the function body. For other languages the name of an input argument is just extra documentation. But the name of an output argument is significant, since it defines the column name in the result row type. (If you omit the name for an output argument, the system will choose a default column name.)</p>
<dt><i>argtype</i></p>
<dd>The data type(s) of the function&#8217;s arguments (optionally schema-qualified), if any. The argument types can be base, composite, or domain types, or can reference the type of a table column. </p>
<p> Depending on the implementation language it might also be allowed to specify &#8220;pseudotypes&#8221; such as <code>cstring</code>. Pseudotypes indicate that the actual argument type is either incompletely specified, or outside the set of ordinary SQL data types. </p>
<p> The type of a column is referenced by writing <i>tablename</i>.<i>columnname</i>%TYPE. Using this feature can sometimes help make a function independent of changes to the definition of a table.</p>
<dt><i>defexpr</i></p>
<dd>An expression to be used as default value if the parameter is not specified. The expression has to be coercible to the argument type of the parameter. Only input (including INOUT) parameters can have a default value. All input parameters following a parameter with a default value must have default values as well.</p>
<dt><i>rettype</i></p>
<dd>The return data type (optionally schema-qualified). The return type can be a base, composite, or domain type, or can reference the type of a table column. Depending on the implementation language it might also be allowed to specify &#8220;pseudotypes&#8221; such as <code>cstring</code>. If the function is not supposed to return a value, specify <code>void</code> as the return type. </p>
<p> When there are OUT or INOUT parameters, the RETURNS clause can be omitted. If present, it must agree with the result type implied by the output parameters: RECORD if there are multiple output parameters, or the same type as the single output parameter. </p>
<p> The SETOF modifier indicates that the function will return a set of items, rather than a single item. </p>
<p> The type of a column is referenced by writing <i>tablename</i>.<i>columnname</i>%TYPE.</p>
<dt><i>colname</i></p>
<dd>The name of an output column in the RETURNS TABLE syntax. This is effectively another way of declaring a named OUT parameter, except that RETURNS TABLE also implies RETURNS SETOF.</p>
<dt><i>coltype</i></p>
<dd>The data type of an output column in the RETURNS TABLE syntax.</p>
<dt><i>langname</i></p>
<dd>The name of the language that the function is implemented in. Can be SQL, C, internal, or the name of a user-defined procedural language. For backward compatibility, the name can be enclosed by single quotes.</p>
<dt><code>WINDOW</code></p>
<dd>WINDOW indicates that the function is a <i>window function</i> rather than a plain function. This is currently only useful for functions written in C. The WINDOW attribute cannot be changed when replacing an existing function definition.</p>
<dt><code>IMMUTABLE</code></p>
<dd>
<dt><code>STABLE</code></p>
<dd>
<dt><code>VOLATILE</code></p>
<dd>These attributes inform the query optimizer about the behavior of the function. At most one choice can be specified. If none of these appear, VOLATILE is the default assumption. </p>
<p> IMMUTABLE indicates that the function cannot modify the database and always returns the same result when given the same argument values; that is, it does not do database lookups or otherwise use information not directly present in its argument list. If this option is given, any call of the function with all-constant arguments can be immediately replaced with the function value. </p>
<p> STABLE indicates that the function cannot modify the database, and that within a single table scan it will consistently return the same result for the same argument values, but that its result could change across SQL statements. This is the appropriate selection for functions whose results depend on database lookups, parameter variables (such as the current time zone), etc. Also note that the <code>current_timestamp</code> family of functions qualify as stable, since their values do not change within a transaction. </p>
<p> VOLATILE indicates that the function value can change even within a single table scan, so no optimizations can be made. Relatively few database functions are volatile in this sense; some examples are random(), currval(), timeofday(). But note that any function that has side-effects must be classified volatile, even if its result is quite predictable, to prevent calls from being optimized away; an example is setval(). </p>
<p> For additional details see in the documentation.</p>
<dt><code>CALLED ON NULL INPUT</code></p>
<dd>
<dt><code>RETURNS NULL ON NULL INPUT</code></p>
<dd>
<dt><code>STRICT</code></p>
<dd>CALLED ON NULL INPUT (the default) indicates that the function will be called normally when some of its arguments are null. It is then the function author&#8217;s responsibility to check for null values if necessary and respond appropriately. </p>
<p> RETURNS NULL ON NULL INPUT or STRICT indicates that the function always returns null whenever any of its arguments are null. If this parameter is specified, the function is not executed when there are null arguments; instead a null result is assumed automatically.</p>
<dt><code>[EXTERNAL] SECURITY INVOKER</code></p>
<dd>
<dt><code>[EXTERNAL] SECURITY DEFINER</code></p>
<dd>SECURITY INVOKER indicates that the function is to be executed with the privileges of the user that calls it. That is the default. SECURITY DEFINER specifies that the function is to be executed with the privileges of the user that created it. </p>
<p> The key word EXTERNAL is allowed for SQL conformance, but it is optional since, unlike in SQL, this feature applies to all functions not only external ones.</p>
<dt><i>execution_cost</i></p>
<dd>A positive number giving the estimated execution cost for the function, in units of cpu_operator_cost. If the function returns a set, this is the cost per returned row. If the cost is not specified, 1 unit is assumed for C-language and internal functions, and 100 units for functions in all other languages. Larger values cause the planner to try to avoid evaluating the function more often than necessary.</p>
<dt><i>result_rows</i></p>
<dd>A positive number giving the estimated number of rows that the planner should expect the function to return. This is only allowed when the function is declared to return a set. The default assumption is 1000 rows.</p>
<dt><i>configuration_parameter</i></p>
<dd>
<dt><i>value</i></p>
<dd>The SET clause causes the specified configuration parameter to be set to the specified value when the function is entered, and then restored to its prior value when the function exits. SET FROM CURRENT saves the session&#8217;s current value of the parameter as the value to be applied when the function is entered. </p>
<p> See SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] and in the documentation for more information about allowed parameter names and values.</p>
<dt><i>definition</i></p>
<dd>A string constant defining the function; the meaning depends on the language. It can be an internal function name, the path to an object file, an SQL command, or text in a procedural language.</p>
<dt><i>obj_file</i><code>, </code><i>link_symbol</i></p>
<dd>This form of the AS clause is used for dynamically loadable C language functions when the function name in the C language source code is not the same as the name of the SQL function. The string <i>obj_file</i> is the name of the file containing the dynamically loadable object, and <i>link_symbol</i> is the function&#8217;s link symbol, that is, the name of the function in the C language source code. If the link symbol is omitted, it is assumed to be the same as the name of the SQL function being defined.</p>
<dt><i>attribute</i></p>
<dd>The historical way to specify optional pieces of information about the function. The following attributes can appear here:</p>
<dl>
<dd>
<dl>
<dt><code>isStrict</code></p>
<dd>Equivalent to STRICT or RETURNS NULL ON NULL INPUT.</p>
<dt><code>isCachable</code></p>
<dd>isCachable is an obsolete equivalent of IMMUTABLE; it&#8217;s still accepted for backwards-compatibility reasons.</dl>
</dl>
</dl>
<p> Attribute names are not case-sensitive.</p>
<h2>Notes</h2>
<p>Refer to in the documentation for further information on writing functions. </p>
<p> The full SQL type syntax is allowed for input arguments and return value. However, some details of the type specification (e.g., the precision field for type <code>numeric</code>) are the responsibility of the underlying function implementation and are silently swallowed (i.e., not recognized or enforced) by the <code>CREATE FUNCTION</code> command. </p>
<p> PostgreSQL allows function <i>overloading</i>; that is, the same name can be used for several different functions so long as they have distinct input argument types. However, the C names of all functions must be different, so you must give overloaded C functions different C names (for example, use the argument types as part of the C names). </p>
<p> Two functions are considered the same if they have the same names and <code>input</code> argument types, ignoring any OUT parameters. Thus for example these declarations conflict: </p>
<pre>CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, out text) ...</pre>
<p>Functions that have different argument type lists will not be considered to conflict at creation time, but if defaults are provided they might conflict in use. For example, consider </p>
<pre>CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, int default 42) ...</pre>
<p>A call foo(10) will fail due to the ambiguity about which function should be called. </p>
<p> When repeated <code>CREATE FUNCTION</code> calls refer to the same object file, the file is only loaded once per session. To unload and reload the file (perhaps during development), start a new session. </p>
<p> Use DROP FUNCTION [<code><a href="/docs/linux/man/7-drop_function/">drop_function</a></code>(7)] to remove user-defined functions. </p>
<p> It is often helpful to use dollar quoting (see in the documentation) to write the function definition string, rather than the normal single quote syntax. Without dollar quoting, any single quotes or backslashes in the function definition must be escaped by doubling them. </p>
<p> If a SET clause is attached to a function, then the effects of a <code>SET LOCAL</code> command executed inside the function for the same variable are restricted to the function: the configuration parameter&#8217;s prior value is still restored at function exit. However, an ordinary <code>SET</code> command (without LOCAL) overrides the SET clause, much as it would do for a previous <code>SET LOCAL</code> command: the effects of such a command will persist after function exit, unless the current transaction is rolled back. </p>
<p> To be able to define a function, the user must have the USAGE privilege on the language. </p>
<p> When <code>CREATE OR REPLACE FUNCTION</code> is used to replace an existing function, the ownership and permissions of the function do not change. All other function properties are assigned the values specified or implied in the command. You must own the function to replace it (this includes being a member of the owning role). </p>
<p> If a function is declared STRICT with a VARIADIC argument, the strictness check tests that the variadic array <code>as a whole</code> is non-null. The function will still be called if the array has null elements.</p>
<h2>Examples</h2>
<p>Here are some trivial examples to help you get started. For more information and examples, see in the documentation. </p>
<pre>CREATE FUNCTION add(integer, integer) RETURNS integer
 AS 'select $1 + $2;'
 LANGUAGE SQL
 IMMUTABLE
 RETURNS NULL ON NULL INPUT;</pre>
<p>Increment an integer, making use of an argument name, in <code>PL/pgSQL</code>: </p>
<pre>CREATE OR REPLACE FUNCTION increment(i integer) RETURNS integer AS $$
 BEGIN
 RETURN i + 1;
 END;
$$ LANGUAGE plpgsql;</pre>
<p>Return a record containing multiple output parameters: </p>
<pre>CREATE FUNCTION dup(in int, out f1 int, out f2 text)
 AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
 LANGUAGE SQL;
SELECT * FROM dup(42);</pre>
<p>You can do the same thing more verbosely with an explicitly named composite type: </p>
<pre>CREATE TYPE dup_result AS (f1 int, f2 text);
CREATE FUNCTION dup(int) RETURNS dup_result
 AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
 LANGUAGE SQL;
SELECT * FROM dup(42);</pre>
<p>Another way to return multiple columns is to use a TABLE function: </p>
<pre>CREATE FUNCTION dup(int) RETURNS TABLE(f1 int, f2 text)
 AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
 LANGUAGE SQL;
SELECT * FROM dup(42);</pre>
<p>However, a TABLE function is different from the preceding examples, because it actually returns a <code>set</code> of records, not just one record.</p>
<h2>Writing Security Definer Functions Safely</h2>
<p>Because a SECURITY DEFINER function is executed with the privileges of the user that created it, care is needed to ensure that the function cannot be misused. For security, search_path should be set to exclude any schemas writable by untrusted users. This prevents malicious users from creating objects that mask objects used by the function. Particularly important in this regard is the temporary-table schema, which is searched first by default, and is normally writable by anyone. A secure arrangement can be had by forcing the temporary schema to be searched last. To do this, write pg_temp as the last entry in search_path. This function illustrates safe usage: </p>
<pre>CREATE FUNCTION check_password(uname TEXT, pass TEXT)
RETURNS BOOLEAN AS $$
DECLARE passed BOOLEAN;
BEGIN
 SELECT (pwd = $2) INTO passed
 FROM pwds
 WHERE username = $1;
 RETURN passed;
END;
$$ LANGUAGE plpgsql
 SECURITY DEFINER
 -- Set a secure search_path: trusted schema(s), then 'pg_temp'.
 SET search_path = admin, pg_temp;</pre>
<p>Before PostgreSQL version 8.3, the SET option was not available, and so older functions may contain rather complicated logic to save, set, and restore search_path. The SET option is far easier to use for this purpose. </p>
<p> Another point to keep in mind is that by default, execute privilege is granted to PUBLIC for newly created functions (see GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)] for more information). Frequently you will wish to restrict use of a security definer function to only some users. To do that, you must revoke the default PUBLIC privileges and then grant execute privilege selectively. To avoid having a window where the new function is accessible to all, create it and set the privileges within a single transaction. For example: </p>
<pre>BEGIN;
CREATE FUNCTION check_password(uname TEXT, pass TEXT) ... SECURITY DEFINER;
REVOKE ALL ON FUNCTION check_password(uname TEXT, pass TEXT) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION check_password(uname TEXT, pass TEXT) TO admins;
COMMIT;</pre>
<h2>Compatibility</h2>
<p>A <code>CREATE FUNCTION</code> command is defined in SQL:1999 and later. The PostgreSQL version is similar but not fully compatible. The attributes are not portable, neither are the different available languages. </p>
<p> For compatibility with some other database systems, <i>argmode</i> can be written either before or after <i>argname</i>. But only the first way is standard-compliant. </p>
<p> The SQL standard does not specify parameter defaults. The syntax with the DEFAULT key word is from Oracle, and it is somewhat in the spirit of the standard: SQL/PSM uses it for variable default values. The syntax with = is used in T-SQL and Firebird.</p>
<h2>See Also</h2>
<p>ALTER FUNCTION [<code><a href="/docs/linux/man/7-alter_function/">alter_function</a></code>(7)], DROP FUNCTION [<code><a href="/docs/linux/man/7-drop_function/">drop_function</a></code>(7)], GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)], LOAD [<code><a href="/docs/linux/man/7-load/">load</a></code>(7)], REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)], createlang [<code><a href="/docs/linux/man/1-createlang/">createlang</a></code>(1)] </p>
