---
title: "mongoc_gridfs_get_files(3)"
name: "mongoc_gridfs_get_files"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_get_files/"
description: "mongoc_gridfs_get_files() – Retrieves the mongoc_collection_t containing the file metadata for GridFS. This instance is owned by the mongoc_gridfs_t and should not be modified or freed."
---

<p>mongoc_gridfs_get_files() &#8211; Retrieves the mongoc_collection_t containing the file metadata for GridFS. This instance is owned by the mongoc_gridfs_t and should not be modified or freed.</p>
<h2>Synopsis</h2>
<pre>mongoc_collection_t *
mongoc_gridfs_get_files (mongoc_gridfs_t *gridfs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Retrieves the <code>mongoc_collection_t</code> containing the file metadata for GridFS. This instance is owned by the <code>mongoc_gridfs_t</code> and should not be modified or freed. </p>
<h2>Returns</h2>
<p>Returns a <code>mongoc_collection_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
