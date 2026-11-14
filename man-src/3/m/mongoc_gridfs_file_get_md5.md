---
title: "mongoc_gridfs_file_get_md5(3)"
name: "mongoc_gridfs_file_get_md5"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_get_md5/"
description: "mongoc_gridfs_file_get_md5() – Fetches the pre-computed MD5 for the underlying gridfs file."
---

<p>mongoc_gridfs_file_get_md5() &#8211; Fetches the pre-computed MD5 for the underlying gridfs file.</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_gridfs_file_get_md5 (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the pre-computed MD5 for the underlying gridfs file. </p>
<h2>Returns</h2>
<p>Returns a string that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
