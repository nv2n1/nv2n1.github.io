---
title: "drop_text_search_configuration(7)"
name: "drop_text_search_configuration"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_text_search_configuration/"
description: "DROP TEXT SEARCH CONFIGURATION – remove a text search configuration"
---

<p>DROP TEXT SEARCH CONFIGURATION &#8211; remove a text search configuration </p>
<h2>Synopsis</h2>
<pre>DROP TEXT SEARCH CONFIGURATION [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TEXT SEARCH CONFIGURATION</code> drops an existing text search configuration. To execute this command you must be the owner of the configuration.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the text search configuration does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search configuration.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the text search configuration.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the text search configuration if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the text search configuration my_english: </p>
<pre>DROP TEXT SEARCH CONFIGURATION my_english;</pre>
<p>This command will not succeed if there are any existing indexes that reference the configuration in <code>to_tsvector</code> calls. Add CASCADE to drop such indexes along with the text search configuration.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP TEXT SEARCH CONFIGURATION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-alter_text_search_configuration/">alter_text_search_configuration</a></code>(7)], CREATE TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-create_text_search_configuration/">create_text_search_configuration</a></code>(7)] </p>
