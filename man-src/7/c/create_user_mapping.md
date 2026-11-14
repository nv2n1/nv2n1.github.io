---
title: "create_user_mapping(7)"
name: "create_user_mapping"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_user_mapping/"
description: "CREATE USER MAPPING – define a new mapping of a user to a foreign server"
---

<p>CREATE USER MAPPING &#8211; define a new mapping of a user to a foreign server </p>
<h2>Synopsis</h2>
<pre>CREATE USER MAPPING FOR { <i>username</i> | USER | CURRENT_USER | PUBLIC }
 SERVER <i>servername</i>
 [ OPTIONS ( <i>option</i> '<i>value</i>' [ , ... ] ) ]</pre>
<h2>Description</h2>
<p><code>CREATE USER MAPPING</code> defines a mapping of a user to a foreign server. A user mapping typically encapsulates connection information that a foreign-data wrapper uses together with the information encapsulated be a foreign server to access an external data resource. </p>
<p> The owner of a foreign server can create user mappings for that server for any user. Also, a user can create a user mapping for his own user name if USAGE privilege on the server has been granted to the user.</p>
<h2>Parameters</h2>
<dl>
<dt><i>username</i></p>
<dd>The name of an existing user that is mapped to foreign server. CURRENT_USER and USER match the name of the current user. When PUBLIC is specified, a so-called public mapping is created that is used when no user-specific mapping is applicable.</p>
<dt><i>servername</i></p>
<dd>The name of an existing server for which the user mapping is to be created.</p>
<dt><code>OPTIONS ( </code><i>option</i><code> &#8216;</code><i>value</i><code>&#8216; [, &#8230; ] )</code></p>
<dd>This clause specifies the options of the user mapping. The options typically define the actual user name and password of the mapping. Option names must be unique. The allowed option names and values are specific to the server&#8217;s foreign-data wrapper.</dl>
<h2>Examples</h2>
<p>Create a user mapping for user bob, server foo: </p>
<pre>CREATE USER MAPPING FOR bob SERVER foo OPTIONS (user 'bob', password 'secret');</pre>
<h2>Compatibility</h2>
<p><code>CREATE USER MAPPING</code> conforms to ISO/IEC 9075-9 (SQL/MED).</p>
<h2>See Also</h2>
<p>ALTER USER MAPPING [<code><a href="/docs/linux/man/7-alter_user_mapping/">alter_user_mapping</a></code>(7)], DROP USER MAPPING [<code><a href="/docs/linux/man/7-drop_user_mapping/">drop_user_mapping</a></code>(7)], CREATE FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-create_foreign_data_wrapper/">create_foreign_data_wrapper</a></code>(7)], CREATE SERVER [<code><a href="/docs/linux/man/7-create_server/">create_server</a></code>(7)] </p>
