---
title: "mongoc_gridfs_find_one(3)"
name: "mongoc_gridfs_find_one"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_find_one/"
description: "mongoc_gridfs_find_one() – This function shall execute a query on the underlying gridfs implementation. The first file matching query will be returned."
---

<p>mongoc_gridfs_find_one() &#8211; This function shall execute a query on the underlying gridfs implementation. The first file matching query will be returned.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_t *
mongoc_gridfs_find_one (mongoc_gridfs_t *gridfs,
 const bson_t *query,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall execute a query on the underlying gridfs implementation. The first file matching <code>query</code> will be returned. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A newly allcoated <code>mongoc_gridfs_file_t</code> or <code>NULL</code> if no file could be found. You must free the resulting file with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_destroy/">mongoc_gridfs_file_destroy</a>(3)</code> if non-NULL. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
