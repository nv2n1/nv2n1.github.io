---
title: "drop_user_mapping(7)"
name: "drop_user_mapping"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_user_mapping/"
description: "DROP USER MAPPING – remove a user mapping for a foreign server"
---

<p>DROP USER MAPPING &#8211; remove a user mapping for a foreign server </p>
<h2>Synopsis</h2>
<pre>DROP USER MAPPING [ IF EXISTS ] FOR { <i>username</i> | USER | CURRENT_USER | PUBLIC } SERVER <i>servername</i></pre>
<h2>Description</h2>
<p><code>DROP USER MAPPING</code> removes an existing user mapping from foreign server. </p>
<p> The owner of a foreign server can drop user mappings for that server for any user. Also, a user can drop a user mapping for his own user name if USAGE privilege on the server has been granted to the user.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the user mapping does not exist. A notice is issued in this case.</p>
<dt><i>username</i></p>
<dd>User name of the mapping. CURRENT_USER and USER match the name of the current user. PUBLIC is used to match all present and future user names in the system.</p>
<dt><i>servername</i></p>
<dd>Server name of the user mapping.</dl>
<h2>Examples</h2>
<p>Drop a user mapping bob, server foo if it exists: </p>
<pre>DROP USER MAPPING IF EXISTS FOR bob SERVER foo;</pre>
<h2>Compatibility</h2>
<p><code>DROP USER MAPPING</code> conforms to ISO/IEC 9075-9 (SQL/MED). The IF EXISTS clause is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE USER MAPPING [<code><a href="/docs/linux/man/7-create_user_mapping/">create_user_mapping</a></code>(7)], ALTER USER MAPPING [<code><a href="/docs/linux/man/7-alter_user_mapping/">alter_user_mapping</a></code>(7)] </p>
