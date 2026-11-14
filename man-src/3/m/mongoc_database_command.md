---
title: "mongoc_database_command(3)"
name: "mongoc_database_command"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_command/"
description: "mongoc_database_command() – The mongoc_database_command() function shall execute a command on a database. This is performed lazily after calling mongoc_cursor_next() on the resulting cursor structure."
---

<p>mongoc_database_command() &#8211; The mongoc_database_command() function shall execute a command on a database. This is performed lazily after calling mongoc_cursor_next() on the resulting cursor structure.</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_database_command (mongoc_database_t *database,
 mongoc_query_flags_t flags,
 uint32_t skip,
 uint32_t limit,
 uint32_t batch_size,
 const bson_t *command,
 const bson_t *fields,
 const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A <code>mongoc_query_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>skip</code></p>
<dd>The number of documents to skip on the server.</dl>
<dl COMPACT>
<dt><code>limit</code></p>
<dd>The maximum number of documents to return from the cursor.</dl>
<dl COMPACT>
<dt><code>batch_size</code></p>
<dd>Attempt to batch results from the server in groups of <code>batch_size</code> documents.</dl>
<dl COMPACT>
<dt><code>command</code></p>
<dd>A <code>bson_t</code> containing the command.</dl>
<dl COMPACT>
<dt><code>fields</code></p>
<dd>An optional <code>bson_t</code> containing the fields to return. <code>NULL</code> for all fields.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>An optional <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<p> The <code><a href="/docs/linux/man/3-mongoc_database_command/">mongoc_database_command</a>(3)</code> function shall execute a command on a database. This is performed lazily after calling <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> on the resulting cursor structure. </p>
<h2>Returns</h2>
<p>This command returns a <code>mongoc_cursor_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> when no longer in use. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
