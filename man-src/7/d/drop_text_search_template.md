---
title: "drop_text_search_template(7)"
name: "drop_text_search_template"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_text_search_template/"
description: "DROP TEXT SEARCH TEMPLATE – remove a text search template"
---

<p>DROP TEXT SEARCH TEMPLATE &#8211; remove a text search template </p>
<h2>Synopsis</h2>
<pre>DROP TEXT SEARCH TEMPLATE [ IF EXISTS ] <i>name</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TEXT SEARCH TEMPLATE</code> drops an existing text search template. You must be a superuser to use this command.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the text search template does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search template.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the text search template.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the text search template if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Remove the text search template thesaurus: </p>
<pre>DROP TEXT SEARCH TEMPLATE thesaurus;</pre>
<p>This command will not succeed if there are any existing text search dictionaries that use the template. Add CASCADE to drop such dictionaries along with the template.</p>
<h2>Compatibility</h2>
<p>There is no <code>DROP TEXT SEARCH TEMPLATE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-alter_text_search_template/">alter_text_search_template</a></code>(7)], CREATE TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-create_text_search_template/">create_text_search_template</a></code>(7)] </p>
