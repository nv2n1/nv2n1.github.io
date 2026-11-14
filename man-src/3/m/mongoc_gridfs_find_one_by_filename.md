---
title: "mongoc_gridfs_find_one_by_filename(3)"
name: "mongoc_gridfs_find_one_by_filename"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_find_one_by_filename/"
description: "mongoc_gridfs_find_one_by_filename() – Finds the first file matching the filename specified. If no file could be found, NULL is returned and error is set."
---

<p>mongoc_gridfs_find_one_by_filename() &#8211; Finds the first file matching the filename specified. If no file could be found, NULL is returned and error is set.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_t *
mongoc_gridfs_find_one_by_filename (mongoc_gridfs_t *gridfs,
 const char *filename,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>filename</code></p>
<dd>A UTF-8 encoded string containing the filename.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>Finds the first file matching the filename specified. If no file could be found, <code>NULL</code> is returned and error is set. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns a newly allocated <code>mongoc_gridfs_file_t</code> if successful, otherwise <code>NULL</code> and error is set. You must free the resulting file with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_destroy/">mongoc_gridfs_file_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
