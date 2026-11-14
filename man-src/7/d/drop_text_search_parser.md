---
title: "drop_text_search_parser(7)"
name: "drop_text_search_parser"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_text_search_parser/"
description: "DROP TEXT SEARCH PARSER – remove a text search parser"
---

<p>DROP TEXT SEARCH PARSER &#8211; remove a text search parser </p>
<h2>Synopsis</h2>
<pre>DROP TEXT SEARCH PARSER [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TEXT SEARCH PARSER</code> drops an existing text search parser. You must be a superuser to use this command.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the text search parser does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search parser.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the text search parser.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the text search parser if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the text search parser my_parser: </p>
<pre>DROP TEXT SEARCH PARSER my_parser;</pre>
<p>This command will not succeed if there are any existing text search configurations that use the parser. Add CASCADE to drop such configurations along with the parser.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP TEXT SEARCH PARSER</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-alter_text_search_parser/">alter_text_search_parser</a></code>(7)], CREATE TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-create_text_search_parser/">create_text_search_parser</a></code>(7)] </p>
