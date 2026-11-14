---
title: "mongoc_gridfs_file_get_aliases(3)"
name: "mongoc_gridfs_file_get_aliases"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_get_aliases/"
description: "mongoc_gridfs_file_get_aliases() – Fetches the aliases associated with a gridfs file."
---

<p>mongoc_gridfs_file_get_aliases() &#8211; Fetches the aliases associated with a gridfs file.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_gridfs_file_get_aliases (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the aliases associated with a gridfs file. </p>
<h2>Returns</h2>
<p>Returns a <code>const bson_t *</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
