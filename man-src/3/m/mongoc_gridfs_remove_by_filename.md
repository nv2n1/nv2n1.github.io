---
title: "mongoc_gridfs_remove_by_filename(3)"
name: "mongoc_gridfs_remove_by_filename"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_remove_by_filename/"
description: "mongoc_gridfs_remove_by_filename() – Removes all files matching filename and their data chunks from the MongoDB server."
---

<p>mongoc_gridfs_remove_by_filename() &#8211; Removes all files matching filename and their data chunks from the MongoDB server.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_gridfs_remove_by_filename (mongoc_gridfs_t *gridfs,
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
<p>Removes all files matching <code>filename</code> and their data chunks from the MongoDB server. </p>
<h2>Returns</h2>
<p>Returns true if successful (including when no files match), otherwise false and <code>error</code> is set. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
