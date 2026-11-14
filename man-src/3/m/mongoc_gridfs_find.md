---
title: "mongoc_gridfs_find(3)"
name: "mongoc_gridfs_find"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_find/"
description: "mongoc_gridfs_find() – Finds all gridfs files matching query. You can iterate the matched gridfs files with the resulting file list."
---

<p>mongoc_gridfs_find() &#8211; Finds all gridfs files matching query. You can iterate the matched gridfs files with the resulting file list.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_list_t *
mongoc_gridfs_find (mongoc_gridfs_t *gridfs,
 const bson_t *query);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Finds all gridfs files matching <code>query</code> \&amp;. You can iterate the matched gridfs files with the resulting file list. </p>
<h2>Returns</h2>
<p>A newly allcoated <code>mongoc_gridfs_file_list_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_list_destroy/">mongoc_gridfs_file_list_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
