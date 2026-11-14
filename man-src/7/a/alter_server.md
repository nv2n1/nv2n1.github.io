---
title: "alter_server(7)"
name: "alter_server"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_server/"
description: "ALTER SERVER – change the definition of a foreign server"
---

<p>ALTER SERVER &#8211; change the definition of a foreign server </p>
<h2>Synopsis</h2>
<pre>ALTER SERVER <i>servername</i> [ VERSION 'newversion' ]
 [ OPTIONS ( [ ADD | SET | DROP ] <i>option</i> ['<i>value</i>'] [, ... ] ) ]
ALTER SERVER <i>servername</i> OWNER TO <i>new_owner</i></pre>
<h2>Description</h2>
<p><code>ALTER SERVER</code> changes the definition of a foreign server. The first form changes the server version string or the generic options of the server (at least one clause is required). The second form changes the owner of the server. </p>
<p> To alter the server you must be the owner of the server. Additionally to alter the owner, you must own the server and also be a direct or indirect member of the new owning role, and you must have USAGE privilege on the server&#8217;s foreign-data wrapper. (Note that superusers satisfy all these criteria automatically.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>servername</i></p>
<dd>The name of an existing server.</p>
<dt><i>serverversion</i></p>
<dd>New server version.</p>
<dt><code>OPTIONS ( [ ADD | SET | DROP ] </code><i>option</i><code> [&#8216;</code><i>value</i><code>&#8216;] [, &#8230; ] )</code></p>
<dd>Change options for the server. ADD, SET, and DROP specify the action to be performed. ADD is assumed if no operation is explicitly specified. Option names must be unique; names and values are also validated using the server&#8217;s foreign-data wrapper library.</dl>
<h2>Examples</h2>
<p>Alter server foo, add connection options: </p>
<pre>ALTER SERVER foo OPTIONS (host 'foo', dbname 'foodb');</pre>
<p>Alter server foo, change version, change host option: </p>
<pre>ALTER SERVER foo VERSION '8.4' OPTIONS (SET host 'baz');</pre>
<h2>Compatibility</h2>
<p><code>ALTER SERVER</code> conforms to ISO/IEC 9075-9 (SQL/MED).</p>
<h2>See Also</h2>
<p>CREATE SERVER [<code><a href="/docs/linux/man/7-create_server/">create_server</a></code>(7)], DROP SERVER [<code><a href="/docs/linux/man/7-drop_server/">drop_server</a></code>(7)] </p>
