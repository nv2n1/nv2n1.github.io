---
title: "mongoc_gridfs_file_get_metadata(3)"
name: "mongoc_gridfs_file_get_metadata"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_get_metadata/"
description: "mongoc_gridfs_file_get_metadata() – Fetches a bson document containing the metadata for the gridfs file."
---

<p>mongoc_gridfs_file_get_metadata() &#8211; Fetches a bson document containing the metadata for the gridfs file.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_gridfs_file_get_metadata (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a bson document containing the metadata for the gridfs file. </p>
<h2>Returns</h2>
<p>Returns a <code>const bson_t *</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
