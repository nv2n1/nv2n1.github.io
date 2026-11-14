---
title: "mongoc_client_command(3)"
name: "mongoc_client_command"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_command/"
description: "mongoc_client_command() – None"
---

<p>mongoc_client_command() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
mongoc_cursor_t *
mongoc_client_command (mongoc_client_t           *client,
                       const char                *db_name,
                       mongoc_query_flags_t       flags,
                       uint32_t                   skip,
                       uint32_t                   limit,
                       uint32_t                   batch_size,
                       const bson_t              *query,
                       const bson_t              *fields,
                       const mongoc_read_prefs_t *read_prefs);
</pre>
<p> This function executes a command on the server using the database and command specification provided. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd> A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>db_name</code></p>
<dd> The name of the database to run the command on.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd> A <code>mongoc_query_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>skip</code></p>
<dd> The number of result documents to skip.</dl>
<dl COMPACT>
<dt><code>limit</code></p>
<dd> The maximum number of documents to return.</dl>
<dl COMPACT>
<dt><code>batch_size</code></p>
<dd> The batch size of documents to return from the MongoDB server.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd> A <code>bson_t</code> containing the command specification.</dl>
<dl COMPACT>
<dt><code>fields</code></p>
<dd> An optional <code>bson_t</code> containing the fields to return in result documents.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd> An optional <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p> This function will always return a <code>mongoc_cursor_t</code> if valid parameters are passed. </p>
<p> The cursor should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
