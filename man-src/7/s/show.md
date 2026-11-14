---
title: "show(7)"
name: "show"
section: "7"
letter: "s"
url: "/docs/linux/man/7-show/"
description: "SHOW – show the value of a run-time parameter"
---

<p>SHOW &#8211; show the value of a run-time parameter </p>
<h2>Synopsis</h2>
<pre>SHOW <i>name</i>
SHOW ALL</pre>
<h2>Description</h2>
<p><code>SHOW</code> will display the current setting of run-time parameters. These variables can be set using the <code>SET</code> statement, by editing the <i>postgresql.conf</i> configuration file, through the <code>PGOPTIONS</code> environmental variable (when using <code>libpq</code> or a <code>libpq</code>-based application), or through command-line flags when starting the <code>postgres</code> server. See in the documentation for details.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of a run-time parameter. Available parameters are documented in in the documentation and on the SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)] reference page. In addition, there are a few parameters that can be shown but not set:</p>
<dl>
<dd>
<dl>
<dt><code>SERVER_VERSION</code></p>
<dd>Shows the server&#8217;s version number.</p>
<dt><code>SERVER_ENCODING</code></p>
<dd>Shows the server-side character set encoding. At present, this parameter can be shown but not set, because the encoding is determined at database creation time.</p>
<dt><code>LC_COLLATE</code></p>
<dd>Shows the database&#8217;s locale setting for collation (text ordering). At present, this parameter can be shown but not set, because the setting is determined at database creation time.</p>
<dt><code>LC_CTYPE</code></p>
<dd>Shows the database&#8217;s locale setting for character classification. At present, this parameter can be shown but not set, because the setting is determined at database creation time.</p>
<dt><code>IS_SUPERUSER</code></p>
<dd>True if the current role has superuser privileges.</dl>
</dl>
</dl>
<dl>
<dt><code>ALL</code></p>
<dd>Show the values of all configuration parameters, with descriptions.</dl>
<h2>Notes</h2>
<p>The function <code>current_setting</code> produces equivalent output; see in the documentation. Also, the <code>pg_settings</code> system view produces the same information.</p>
<h2>Examples</h2>
<p>Show the current setting of the parameter DateStyle: </p>
<pre>SHOW DateStyle;
 DateStyle
-----------
 ISO, MDY
(1 row)</pre>
<p>Show the current setting of the parameter geqo: </p>
<pre>SHOW geqo;
 geqo
------
 on
(1 row)</pre>
<p>Show all settings: </p>
<pre>SHOW ALL;
 name | setting | description 
--------------------------------+--------------------------------+----------------------------------------------------------------------------------------------
 add_missing_from | off | Automatically adds missing table references to FROM clauses.
 allow_system_table_mods | off | Allows modifications of the structure of system tables.
 .
 .
 .
 work_mem | 1024 | Sets the maximum memory to be used for query workspaces.
 zero_damaged_pages | off | Continues processing past damaged page headers.
(146 rows)</pre>
<h2>Compatibility</h2>
<p>The <code>SHOW</code> command is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>SET [<code><a href="/docs/linux/man/7-set/">set</a></code>(7)], RESET [<code><a href="/docs/linux/man/7-reset/">reset</a></code>(7)] </p>
