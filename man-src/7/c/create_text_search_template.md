---
title: "create_text_search_template(7)"
name: "create_text_search_template"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_text_search_template/"
description: "CREATE TEXT SEARCH TEMPLATE – define a new text search template"
---

<p>CREATE TEXT SEARCH TEMPLATE &#8211; define a new text search template </p>
<h2>Synopsis</h2>
<pre>CREATE TEXT SEARCH TEMPLATE <i>name</i> (
 [ INIT = <i>init_function</i> , ]
 LEXIZE = <i>lexize_function</i>
)</pre>
<h2>Description</h2>
<p><code>CREATE TEXT SEARCH TEMPLATE</code> creates a new text search template. Text search templates define the functions that implement text search dictionaries. A template is not useful by itself, but must be instantiated as a dictionary to be used. The dictionary typically specifies parameters to be given to the template functions. </p>
<p> If a schema name is given then the text search template is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> You must be a superuser to use <code>CREATE TEXT SEARCH TEMPLATE</code>. This restriction is made because an erroneous text search template definition could confuse or even crash the server. The reason for separating templates from dictionaries is that a template encapsulates the &#8220;unsafe&#8221; aspects of defining a dictionary. The parameters that can be set when defining a dictionary are safe for unprivileged users to set, and so creating a dictionary need not be a privileged operation. </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the text search template to be created. The name can be schema-qualified.</p>
<dt><i>init_function</i></p>
<dd>The name of the init function for the template.</p>
<dt><i>lexize_function</i></p>
<dd>The name of the lexize function for the template.</dl>
<p> The function names can be schema-qualified if necessary. Argument types are not given, since the argument list for each type of function is predetermined. The lexize function is required, but the init function is optional. </p>
<p> The arguments can appear in any order, not only the one shown above.</p>
<h2>Compatibility</h2>
<p>There is no <code>CREATE TEXT SEARCH TEMPLATE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-alter_text_search_template/">alter_text_search_template</a></code>(7)], DROP TEXT SEARCH TEMPLATE [<code><a href="/docs/linux/man/7-drop_text_search_template/">drop_text_search_template</a></code>(7)] </p>
