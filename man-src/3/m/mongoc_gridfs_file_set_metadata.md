---
title: "mongoc_gridfs_file_set_metadata(3)"
name: "mongoc_gridfs_file_set_metadata"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_set_metadata/"
description: "mongoc_gridfs_file_set_metadata() – Sets the metadata associated with file."
---

<p>mongoc_gridfs_file_set_metadata() &#8211; Sets the metadata associated with file.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_gridfs_file_set_metadata (mongoc_gridfs_file_t *file,
 const bson_t *metadata);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>bson</code></p>
<dd>A <code>bson_t</code> containing metadata for <code>file</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the metadata associated with <code>file</code> \&amp;. </p>
<p> You need to call <code><a href="/docs/linux/man/3-mongoc_gridfs_file_save/">mongoc_gridfs_file_save</a>(3)</code> to persist this change. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
