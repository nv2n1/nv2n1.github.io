---
title: "alter_text_search_template(7)"
name: "alter_text_search_template"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_text_search_template/"
description: "ALTER TEXT SEARCH TEMPLATE – change the definition of a text search template"
---

<p>ALTER TEXT SEARCH TEMPLATE &#8211; change the definition of a text search template </p>
<h2>Synopsis</h2>
<pre>ALTER TEXT SEARCH TEMPLATE <i>name</i> RENAME TO <i>newname</i></pre>
<h2>Description</h2>
<p><code>ALTER TEXT SEARCH TEMPLATE</code> changes the definition of a text search template. Currently, the only supported functionality is to change the template&#8217;s name. </p>
<p> You must be a superuser to use <code>ALTER TEXT SEARCH TEMPLATE</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search template.</p>
<dt><i>newname</i></p>
<dd>The new name of the text search template.</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER TEXT SEARCH TEMPLATE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-create_text_search_template/">create_text_search_template</a></code>(7)], DROP TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-drop_text_search_template/">drop_text_search_template</a></code>(7)] </p>
