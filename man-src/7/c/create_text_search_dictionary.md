---
title: "create_text_search_dictionary(7)"
name: "create_text_search_dictionary"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_text_search_dictionary/"
description: "CREATE TEXT SEARCH DICTIONARY – define a new text search dictionary"
---

<p>CREATE TEXT SEARCH DICTIONARY &#8211; define a new text search dictionary </p>
<h2>Synopsis</h2>
<pre>CREATE TEXT SEARCH DICTIONARY <i>name</i> (
 TEMPLATE = <i>template</i>
 [, <i>option</i> = <i>value</i> [, ... ]]
)</pre>
<h2>Description</h2>
<p><code>CREATE TEXT SEARCH DICTIONARY</code> creates a new text search dictionary. A text search dictionary specifies a way of recognizing interesting or uninteresting words for searching. A dictionary depends on a text search template, which specifies the functions that actually perform the work. Typically the dictionary provides some options that control the detailed behavior of the template&#8217;s functions. </p>
<p> If a schema name is given then the text search dictionary is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> The user who defines a text search dictionary becomes its owner. </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the text search dictionary to be created. The name can be schema-qualified.</p>
<dt><i>template</i></p>
<dd>The name of the text search template that will define the basic behavior of this dictionary.</p>
<dt><i>option</i></p>
<dd>The name of a template-specific option to be set for this dictionary.</p>
<dt><i>value</i></p>
<dd>The value to use for a template-specific option. If the value is not a simple identifier or number, it must be quoted (but you can always quote it, if you wish).</dl>
<p> The options can appear in any order.</p>
<h2>Examples</h2>
<p>The following example command creates a Snowball-based dictionary with a nonstandard list of stop words. </p>
<pre><code>CREATE TEXT SEARCH DICTIONARY my_russian (
template = snowball,
language = russian,
stopwords = myrussian
);</code></pre>
<h2>Compatibility</h2>
<p>There is no <code>CREATE TEXT SEARCH DICTIONARY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-alter_text_search_dictionary/">alter_text_search_dictionary</a></code>(7)], DROP TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-drop_text_search_dictionary/">drop_text_search_dictionary</a></code>(7)] </p>
