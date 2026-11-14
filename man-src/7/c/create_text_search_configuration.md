---
title: "create_text_search_configuration(7)"
name: "create_text_search_configuration"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_text_search_configuration/"
description: "CREATE TEXT SEARCH CONFIGURATION – define a new text search configuration"
---

<p>CREATE TEXT SEARCH CONFIGURATION &#8211; define a new text search configuration </p>
<h2>Synopsis</h2>
<pre>CREATE TEXT SEARCH CONFIGURATION <i>name</i> (
 PARSER = <i>parser_name</i> |
 COPY = <i>source_config</i>
)</pre>
<h2>Description</h2>
<p><code>CREATE TEXT SEARCH CONFIGURATION</code> creates a new text search configuration. A text search configuration specifies a text search parser that can divide a string into tokens, plus dictionaries that can be used to determine which tokens are of interest for searching. </p>
<p> If only the parser is specified, then the new text search configuration initially has no mappings from token types to dictionaries, and therefore will ignore all words. Subsequent <code>ALTER TEXT SEARCH CONFIGURATION</code> commands must be used to create mappings to make the configuration useful. Alternatively, an existing text search configuration can be copied. </p>
<p> If a schema name is given then the text search configuration is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> The user who defines a text search configuration becomes its owner. </p>
<p> Refer to in the documentation for further information.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the text search configuration to be created. The name can be schema-qualified.</p>
<dt><i>parser_name</i></p>
<dd>The name of the text search parser to use for this configuration.</p>
<dt><i>source_config</i></p>
<dd>The name of an existing text search configuration to copy.</dl>
<h2>Notes</h2>
<p>The PARSER and COPY options are mutually exclusive, because when an existing configuration is copied, its parser selection is copied too.</p>
<h2>Compatibility</h2>
<p>There is no <code>CREATE TEXT SEARCH CONFIGURATION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-alter_text_search_configuration/">alter_text_search_configuration</a></code>(7)], DROP TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-drop_text_search_configuration/">drop_text_search_configuration</a></code>(7)] </p>
