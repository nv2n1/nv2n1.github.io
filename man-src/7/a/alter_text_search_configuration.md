---
title: "alter_text_search_configuration(7)"
name: "alter_text_search_configuration"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_text_search_configuration/"
description: "ALTER TEXT SEARCH CONFIGURATION – change the definition of a text search configuration"
---

<p>ALTER TEXT SEARCH CONFIGURATION &#8211; change the definition of a text search configuration </p>
<h2>Synopsis</h2>
<pre>ALTER TEXT SEARCH CONFIGURATION <i>name</i>
 ADD MAPPING FOR <i>token_type</i> [, ... ] WITH <i>dictionary_name</i> [, ... ]
ALTER TEXT SEARCH CONFIGURATION <i>name</i>
 ALTER MAPPING FOR <i>token_type</i> [, ... ] WITH <i>dictionary_name</i> [, ... ]
ALTER TEXT SEARCH CONFIGURATION <i>name</i>
 ALTER MAPPING REPLACE <i>old_dictionary</i> WITH <i>new_dictionary</i>
ALTER TEXT SEARCH CONFIGURATION <i>name</i>
 ALTER MAPPING FOR <i>token_type</i> [, ... ] REPLACE <i>old_dictionary</i> WITH <i>new_dictionary</i>
ALTER TEXT SEARCH CONFIGURATION <i>name</i>
 DROP MAPPING [ IF EXISTS ] FOR <i>token_type</i> [, ... ]
ALTER TEXT SEARCH CONFIGURATION <i>name</i> RENAME TO <i>newname</i>
ALTER TEXT SEARCH CONFIGURATION <i>name</i> OWNER TO <i>newowner</i></pre>
<h2>Description</h2>
<p><code>ALTER TEXT SEARCH CONFIGURATION</code> changes the definition of a text search configuration. You can modify its mappings from token types to dictionaries, or change the configuration&#8217;s name or owner. </p>
<p> You must be the owner of the configuration to use <code>ALTER TEXT SEARCH CONFIGURATION</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing text search configuration.</p>
<dt><i>token_type</i></p>
<dd>The name of a token type that is emitted by the configuration&#8217;s parser.</p>
<dt><i>dictionary_name</i></p>
<dd>The name of a text search dictionary to be consulted for the specified token type(s). If multiple dictionaries are listed, they are consulted in the specified order.</p>
<dt><i>old_dictionary</i></p>
<dd>The name of a text search dictionary to be replaced in the mapping.</p>
<dt><i>new_dictionary</i></p>
<dd>The name of a text search dictionary to be substituted for <i>old_dictionary</i>.</p>
<dt><i>newname</i></p>
<dd>The new name of the text search configuration.</p>
<dt><i>newowner</i></p>
<dd>The new owner of the text search configuration.</dl>
<p> The ADD MAPPING FOR form installs a list of dictionaries to be consulted for the specified token type(s); it is an error if there is already a mapping for any of the token types. The ALTER MAPPING FOR form does the same, but first removing any existing mapping for those token types. The ALTER MAPPING REPLACE forms substitute <i>new_dictionary</i> for <i>old_dictionary</i> anywhere the latter appears. This is done for only the specified token types when FOR appears, or for all mappings of the configuration when it doesn&#8217;t. The DROP MAPPING form removes all dictionaries for the specified token type(s), causing tokens of those types to be ignored by the text search configuration. It is an error if there is no mapping for the token types, unless IF EXISTS appears.</p>
<h2>Examples</h2>
<p>The following example replaces the english dictionary with the swedish dictionary anywhere that english is used within my_config. </p>
<pre>ALTER TEXT SEARCH CONFIGURATION my_config
 ALTER MAPPING REPLACE english WITH swedish;</pre>
<h2>Compatibility</h2>
<p>There is no <code>ALTER TEXT SEARCH CONFIGURATION</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-create_text_search_configuration/">create_text_search_configuration</a></code>(7)], DROP TEXT SEARCH CONFIGURATION [<code><a href="/docs/linux/man/7-drop_text_search_configuration/">drop_text_search_configuration</a></code>(7)] </p>
