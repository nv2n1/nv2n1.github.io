---
title: "mongoc_gridfs_file_get_id(3)"
name: "mongoc_gridfs_file_get_id"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_get_id/"
description: "mongoc_gridfs_file_get_id() – Fetches the id of a gridfs file."
---

<p>mongoc_gridfs_file_get_id() &#8211; Fetches the id of a gridfs file.</p>
<h2>Synopsis</h2>
<pre>const bson_value_t *
mongoc_gridfs_file_get_id (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the id of a gridfs file. </p>
<p> The C Driver always uses an ObjectId for <code>_id</code> , but files created by other drivers may have any type of <code>_id</code> \&amp;. </p>
<h2>Returns</h2>
<p>Returns a <code>const bson_value_t *</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
