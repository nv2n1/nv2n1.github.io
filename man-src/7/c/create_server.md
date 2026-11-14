---
title: "create_server(7)"
name: "create_server"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_server/"
description: "CREATE SERVER – define a new foreign server"
---

<p>CREATE SERVER &#8211; define a new foreign server </p>
<h2>Synopsis</h2>
<pre>CREATE SERVER <i>servername</i> [ TYPE 'servertype' ] [ VERSION 'serverversion' ]
 FOREIGN DATA WRAPPER <i>fdwname</i>
 [ OPTIONS ( <i>option</i> '<i>value</i>' [, ... ] ) ]</pre>
<h2>Description</h2>
<p><code>CREATE SERVER</code> defines a new foreign server. The user who defines the server becomes its owner. </p>
<p> A foreign server typically encapsulates connection information that a foreign-data wrapper uses to access an external data resource. Additional user-specific connection information may be specified by means of user mappings. </p>
<p> The server name must be unique within the database. </p>
<p> Creating a server requires USAGE privilege on the foreign-data wrapper being used.</p>
<h2>Parameters</h2>
<dl>
<dt><i>servername</i></p>
<dd>The name of the foreign server to be created.</p>
<dt><i>servertype</i></p>
<dd>Optional server type.</p>
<dt><i>serverversion</i></p>
<dd>Optional server version.</p>
<dt><i>fdwname</i></p>
<dd>The name of the foreign-data wrapper that manages the server.</p>
<dt><code>OPTIONS ( </code><i>option</i><code> &#8216;</code><i>value</i><code>&#8216; [, &#8230; ] )</code></p>
<dd>This clause specifies the options for the server. The options typically define the connection details of the server, but the actual names and values are dependent on the server&#8217;s foreign-data wrapper.</dl>
<h2>Notes</h2>
<p>When using the <code>dblink</code> module (see in the documentation), the foreign server name can be used as an argument of the <code><a href="/docs/linux/man/l-dblink_connect/">dblink_connect</a></code>(l) function to indicate the connection parameters. See also there for more examples. It is necessary to have the USAGE privilege on the foreign server to be able to use it in this way.</p>
<h2>Examples</h2>
<p>Create a server foo that uses the built-in foreign-data wrapper default: </p>
<pre>CREATE SERVER foo FOREIGN DATA WRAPPER &quot;default&quot;;</pre>
<p>Create a server myserver that uses the foreign-data wrapper pgsql: </p>
<pre>CREATE SERVER myserver FOREIGN DATA WRAPPER pgsql OPTIONS (host 'foo', dbname 'foodb', port '5432');</pre>
<h2>Compatibility</h2>
<p><code>CREATE SERVER</code> conforms to ISO/IEC 9075-9 (SQL/MED).</p>
<h2>See Also</h2>
<p>ALTER SERVER [<code><a href="/docs/linux/man/7-alter_server/">alter_server</a></code>(7)], DROP SERVER [<code><a href="/docs/linux/man/7-drop_server/">drop_server</a></code>(7)], CREATE FOREIGN DATA WRAPPER [<code><a href="/docs/linux/man/7-create_foreign_data_wrapper/">create_foreign_data_wrapper</a></code>(7)], CREATE USER MAPPING [<code><a href="/docs/linux/man/7-create_user_mapping/">create_user_mapping</a></code>(7)] </p>
