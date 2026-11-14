---
title: "drop_text_search_dictionary(7)"
name: "drop_text_search_dictionary"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_text_search_dictionary/"
description: "DROP TEXT SEARCH DICTIONARY – remove a text search dictionary"
---

<p>DROP TEXT SEARCH DICTIONARY &#8211; remove a text search dictionary </p>
<h2>Synopsis</h2>
<pre>DROP TEXT SEARCH DICTIONARY [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TEXT SEARCH DICTIONARY</code> drops an existing text search dictionary. To execute this command you must be the owner of the dictionary.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the text search dictionary does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search dictionary.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the text search dictionary.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the text search dictionary if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the text search dictionary english: </p>
<pre>DROP TEXT SEARCH DICTIONARY english;</pre>
<p>This command will not succeed if there are any existing text search configurations that use the dictionary. Add CASCADE to drop such configurations along with the dictionary.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP TEXT SEARCH DICTIONARY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-alter_text_search_dictionary/">alter_text_search_dictionary</a></code>(7)], CREATE TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-create_text_search_dictionary/">create_text_search_dictionary</a></code>(7)] </p>
