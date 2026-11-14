---
title: "alter_user_mapping(7)"
name: "alter_user_mapping"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_user_mapping/"
description: "ALTER USER MAPPING – change the definition of a user mapping"
---

<p>ALTER USER MAPPING &#8211; change the definition of a user mapping </p>
<h2>Synopsis</h2>
<pre>ALTER USER MAPPING FOR { <i>username</i> | USER | CURRENT_USER | PUBLIC }
 SERVER <i>servername</i>
 OPTIONS ( [ ADD | SET | DROP ] <i>option</i> ['<i>value</i>'] [, ... ] )</pre>
<h2>Description</h2>
<p><code>ALTER USER MAPPING</code> changes the definition of a user mapping. </p>
<p> The owner of a foreign server can alter user mappings for that server for any user. Also, a user can alter a user mapping for his own user name if USAGE privilege on the server has been granted to the user.</p>
<h2>Parameters</h2>
<dl>
<dt><i>username</i></p>
<dd>User name of the mapping. CURRENT_USER and USER match the name of the current user. PUBLIC is used to match all present and future user names in the system.</p>
<dt><i>servername</i></p>
<dd>Server name of the user mapping.</p>
<dt><code>OPTIONS ( [ ADD | SET | DROP ] </code><i>option</i><code> [&#8216;</code><i>value</i><code>&#8216;] [, &#8230; ] )</code></p>
<dd>Change options for the user mapping. The new options override any previously specified options. ADD, SET, and DROP specify the action to be performed. ADD is assumed if no operation is explicitly specified. Option names must be unique; options are also validated by the server&#8217;s foreign-data wrapper.</dl>
<h2>Examples</h2>
<p>Change the password for user mapping bob, server foo: </p>
<pre>ALTER USER MAPPING FOR bob SERVER foo OPTIONS (user 'bob', password 'public');</pre>
<h2>Compatibility</h2>
<p><code>ALTER USER MAPPING</code> conforms to ISO/IEC 9075-9 (SQL/MED). There is a subtle syntax issue: The standard omits the FOR key word. Since both CREATE USER MAPPING and DROP USER MAPPING use FOR in analogous positions, and IBM DB2 (being the other major SQL/MED implementation) also requires it for ALTER USER MAPPING, PostgreSQL diverges from the standard here in the interest of consistency and interoperability.</p>
<h2>See Also</h2>
<p>CREATE USER MAPPING [<code><a href="/docs/linux/man/7-create_user_mapping/">create_user_mapping</a></code>(7)], DROP USER MAPPING [<code><a href="/docs/linux/man/7-drop_user_mapping/">drop_user_mapping</a></code>(7)] </p>
