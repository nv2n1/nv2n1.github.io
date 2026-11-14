---
title: "create_foreign_data_wrapper(7)"
name: "create_foreign_data_wrapper"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_foreign_data_wrapper/"
description: "CREATE FOREIGN DATA WRAPPER – define a new foreign-data wrapper"
---

<p>CREATE FOREIGN DATA WRAPPER &#8211; define a new foreign-data wrapper </p>
<h2>Synopsis</h2>
<pre>CREATE FOREIGN DATA WRAPPER <i>name</i>
 [ VALIDATOR <i>valfunction</i> | NO VALIDATOR ]
 [ OPTIONS ( <i>option</i> '<i>value</i>' [, ... ] ) ]</pre>
<h2>Description</h2>
<p><code>CREATE FOREIGN DATA WRAPPER</code> creates a new foreign-data wrapper. The user who defines a foreign-data wrapper becomes its owner. </p>
<p> The foreign-data wrapper name must be unique within the database. </p>
<p> Only superusers can create foreign-data wrappers.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the foreign-data wrapper to be created.</p>
<dt><code>VALIDATOR </code><i>valfunction</i></p>
<dd><i>valfunction</i> is the name of a previously registered function that will be called to check the generic options given to the foreign-data wrapper, as well as to foreign servers and user mappings using the foreign-data wrapper. If no validator function or NO VALIDATOR is specified, then options will not be checked at creation time. (Foreign-data wrappers will possibly ignore or reject invalid option specifications at run time, depending on the implementation.) The validator function must take two arguments: one of type <code>text[]</code>, which will contain the array of options as stored in the system catalogs, and one of type <code>oid</code>, which will be the OID of the system catalog containing the options. The return type is ignored; the function should indicate invalid options using the <code>ereport()</code> function.</p>
<dt><code>OPTIONS ( </code><i>option</i><code> &#8216;</code><i>value</i><code>&#8216; [, &#8230; ] )</code></p>
<dd>This clause specifies options for the new foreign-data wrapper. The allowed option names and values are specific to each foreign data wrapper and are validated using the foreign-data wrapper library. Option names must be unique.</dl>
<h2>Notes</h2>
<p>At the moment, the foreign-data wrapper functionality is very rudimentary. The purpose of foreign-data wrappers, foreign servers, and user mappings is to store this information in a standard way so that it can be queried by interested applications. One such application is <code>dblink</code>; see in the documentation. The functionality to actually query external data through a foreign-data wrapper library does not exist yet. </p>
<p> There is currently one foreign-data wrapper validator function provided: <i>postgresql_fdw_validator</i>, which accepts options corresponding to <code>libpq</code> connection parameters.</p>
<h2>Examples</h2>
<p>Create a foreign-data wrapper dummy: </p>
<pre>CREATE FOREIGN DATA WRAPPER dummy;</pre>
<p>Create a foreign-data wrapper postgresql with validator function postgresql_fdw_validator: </p>
<pre>CREATE FOREIGN DATA WRAPPER postgresql VALIDATOR postgresql_fdw_validator;</pre>
<p>Create a foreign-data wrapper mywrapper with some options: </p>
<pre>CREATE FOREIGN DATA WRAPPER mywrapper
 OPTIONS (debug 'true');</pre>
<h2>Compatibility</h2>
<p><code>CREATE FOREIGN DATA WRAPPER</code> conforms to ISO/IEC 9075-9 (SQL/MED), with the exception that the VALIDATOR clause is an extension and the clauses LIBRARY and LANGUAGE are not yet implemented in PostgreSQL. </p>
<p> Note, however, that the SQL/MED functionality as a whole is not yet conforming.</p>
<h2>See Also</h2>
<p>ALTER FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-alter_foreign_data_wrapper/">alter_foreign_data_wrapper</a></code>(7)], DROP FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-drop_foreign_data_wrapper/">drop_foreign_data_wrapper</a></code>(7)], CREATE SERVER [<code><a href="/docs/linux/man/7-create_server/">create_server</a></code>(7)], CREATE USER MAPPING [<code><a href="/docs/linux/man/7-create_user_mapping/">create_user_mapping</a></code>(7)] </p>
