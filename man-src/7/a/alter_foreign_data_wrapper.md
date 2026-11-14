---
title: "alter_foreign_data_wrapper(7)"
name: "alter_foreign_data_wrapper"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_foreign_data_wrapper/"
description: "ALTER FOREIGN DATA WRAPPER – change the definition of a foreign-data wrapper"
---

<p>ALTER FOREIGN DATA WRAPPER &#8211; change the definition of a foreign-data wrapper </p>
<h2>Synopsis</h2>
<pre>ALTER FOREIGN DATA WRAPPER <i>name</i>
 [ VALIDATOR <i>valfunction</i> | NO VALIDATOR ]
 [ OPTIONS ( [ ADD | SET | DROP ] <i>option</i> ['<i>value</i>'] [, ... ]) ]
ALTER FOREIGN DATA WRAPPER <i>name</i> OWNER TO <i>new_owner</i></pre>
<h2>Description</h2>
<p><code>ALTER FOREIGN DATA WRAPPER</code> changes the definition of a foreign-data wrapper. The first form of the command changes the library or the generic options of the foreign-data wrapper (at least one clause is required). The second form changes the owner of the foreign-data wrapper. </p>
<p> Only superusers can alter foreign-data wrappers. Additionally, only superusers can own foreign-data wrappers.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of an existing foreign-data wrapper.</p>
<dt><code>VALIDATOR </code><i>valfunction</i></p>
<dd>Specifies a new foreign-data wrapper validator function. </p>
<p> Note that it is possible that after changing the validator the options to the foreign-data wrapper, servers, and user mappings have become invalid. It is up to the user to make sure that these options are correct before using the foreign-data wrapper.</p>
<dt><code>NO VALIDATOR</code></p>
<dd>This is used to specify that the foreign-data wrapper should no longer have a validator function.</p>
<dt><code>OPTIONS ( [ ADD | SET | DROP ] </code><i>option</i><code> [&#8216;</code><i>value</i><code>&#8216;] [, &#8230; ] )</code></p>
<dd>Change options for the foreign-data wrapper. ADD, SET, and DROP specify the action to be performed. ADD is assumed if no operation is explicitly specified. Option names must be unique; names and values are also validated using the foreign data wrapper library.</dl>
<h2>Examples</h2>
<p>Change a foreign-data wrapper dbi, add option foo, drop bar: </p>
<pre>ALTER FOREIGN DATA WRAPPER dbi OPTIONS (ADD foo '1', DROP 'bar');</pre>
<p>Change the foreign-data wrapper dbi validator to bob.myvalidator: </p>
<pre>ALTER FOREIGN DATA WRAPPER dbi VALIDATOR bob.myvalidator;</pre>
<h2>Compatibility</h2>
<p><code>ALTER FOREIGN DATA WRAPPER</code> conforms to ISO/IEC 9075-9 (SQL/MED). The standard does not specify the VALIDATOR and OWNER TO variants of the command.</p>
<h2>See Also</h2>
<p>CREATE FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-create_foreign_data_wrapper/">create_foreign_data_wrapper</a></code>(7)], DROP FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-drop_foreign_data_wrapper/">drop_foreign_data_wrapper</a></code>(7)] </p>
