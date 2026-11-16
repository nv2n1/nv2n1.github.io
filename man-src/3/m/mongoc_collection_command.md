---
title: "mongoc_collection_command(3)"
name: "mongoc_collection_command"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_command/"
description: "mongoc_collection_command() – This function shall execute a command on a collection. This is performed lazily and therefore requires calling mongoc_cursor_next() on the resulting cursor structure. ..."
---

<p>mongoc_collection_command() &#8211; This function shall execute a command on a collection. This is performed lazily and therefore requires calling mongoc_cursor_next() on the resulting cursor structure. The cursor should be freed with mongoc_cursor_destroy() when no longer in use.</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_collection_command (mongoc_collection_t *collection,
 mongoc_query_flags_t flags,
 uint32_t skip,
 uint32_t limit,
 uint32_t batch_size,
 const bson_t *command,
 const bson_t *fields,
 const mongoc_read_prefs_t *read_prefs)
BSON_GNUC_WARN_UNUSED_RESULT;</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></dt>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>flags</code></dt>
<dd>A <code>mongoc_query_flags_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>skip</code></dt>
<dd>A uint32_t with the number of documents to skip or zero.</dd></dl>
<dl COMPACT>
<dt><code>limit</code></dt>
<dd>A uint32_t with the max number of documents to return or zero.</dd></dl>
<dl COMPACT>
<dt><code>batch_size</code></dt>
<dd>A uint32_t with the number of documents in each batch or zero. Default is 100.</dd></dl>
<dl COMPACT>
<dt><code>command</code></dt>
<dd>A <code>bson_t</code> containing the command to execute.</dd></dl>
<dl COMPACT>
<dt><code>fields</code></dt>
<dd>A <code>bson_t</code> containing the fields to return or <code>NULL</code> \&amp;. Not all commands support this option.</dd></dl>
<dl COMPACT>
<dt><code>read_prefs</code></dt>
<dd>A <code>mongoc_read_prefs_t</code> or <code>NULL</code> \&amp;.</dd></dl>
<h2>Description</h2>
<p>This function shall execute a command on a collection. This is performed lazily and therefore requires calling <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> on the resulting cursor structure. The cursor should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> when no longer in use. </p>
<h2>Returns</h2>
<p>A lazy <code>mongoc_cursor_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dd></dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
