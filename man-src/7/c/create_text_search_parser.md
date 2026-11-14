---
title: "create_text_search_parser(7)"
name: "create_text_search_parser"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_text_search_parser/"
description: "CREATE TEXT SEARCH PARSER – define a new text search parser"
---

<p>CREATE TEXT SEARCH PARSER &#8211; define a new text search parser </p>
<h2>Synopsis</h2>
<pre>CREATE TEXT SEARCH PARSER <i>name</i> (
 START = <i>start_function</i> ,
 GETTOKEN = <i>gettoken_function</i> ,
 END = <i>end_function</i> ,
 LEXTYPES = <i>lextypes_function</i>
 [, HEADLINE = <i>headline_function</i> ]
)</pre>
<h2>Description</h2>
<p><code>CREATE TEXT SEARCH PARSER</code> creates a new text search parser. A text search parser defines a method for splitting a text string into tokens and assigning types (categories) to the tokens. A parser is not particularly useful by itself, but must be bound into a text search configuration along with some text search dictionaries to be used for searching. </p>
<p> If a schema name is given then the text search parser is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> You must be a superuser to use <code>CREATE TEXT SEARCH PARSER</code>. (This restriction is made because an erroneous text search parser definition could confuse or even crash the server.) </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the text search parser to be created. The name can be schema-qualified.</p>
<dt><i>start_function</i></p>
<dd>The name of the start function for the parser.</p>
<dt><i>gettoken_function</i></p>
<dd>The name of the get-next-token function for the parser.</p>
<dt><i>end_function</i></p>
<dd>The name of the end function for the parser.</p>
<dt><i>lextypes_function</i></p>
<dd>The name of the lextypes function for the parser (a function that returns information about the set of token types it produces).</p>
<dt><i>headline_function</i></p>
<dd>The name of the headline function for the parser (a function that summarizes a set of tokens).</dl>
<p> The function names can be schema-qualified if necessary. Argument types are not given, since the argument list for each type of function is predetermined. All except the headline function are required. </p>
<p> The arguments can appear in any order, not only the one shown above.</p>
<h2>Compatibility</h2>
<p>There is no <code>CREATE TEXT SEARCH PARSER</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-alter_text_search_parser/">alter_text_search_parser</a></code>(7)], DROP TEXT SEARCH PARSER [<code><a href="/docs/linux/man/7-drop_text_search_parser/">drop_text_search_parser</a></code>(7)] </p>
