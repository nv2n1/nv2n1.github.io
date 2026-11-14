---
title: "alter_text_search_parser(7)"
name: "alter_text_search_parser"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_text_search_parser/"
description: "ALTER TEXT SEARCH PARSER – change the definition of a text search parser"
---

<p>ALTER TEXT SEARCH PARSER &#8211; change the definition of a text search parser </p>
<h2>Synopsis</h2>
<pre>ALTER TEXT SEARCH PARSER <i>name</i> RENAME TO <i>newname</i></pre>
<h2>Description</h2>
<p><code>ALTER TEXT SEARCH PARSER</code> changes the definition of a text search parser. Currently, the only supported functionality is to change the parser&#8217;s name. </p>
<p> You must be a superuser to use <code>ALTER TEXT SEARCH PARSER</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search parser.</p>
<dt><i>newname</i></p>
<dd>The new name of the text search parser.</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER TEXT SEARCH PARSER</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-create_text_search_parser/">create_text_search_parser</a></code>(7)], DROP TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-drop_text_search_parser/">drop_text_search_parser</a></code>(7)] </p>
