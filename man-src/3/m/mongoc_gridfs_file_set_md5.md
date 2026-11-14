---
title: "mongoc_gridfs_file_set_md5(3)"
name: "mongoc_gridfs_file_set_md5"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_set_md5/"
description: "mongoc_gridfs_file_set_md5() – Sets the MD5 checksum for file."
---

<p>mongoc_gridfs_file_set_md5() &#8211; Sets the MD5 checksum for file.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_gridfs_file_set_md5 (mongoc_gridfs_file_t *file,
 const char *md5);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>str</code></p>
<dd>A string containing the MD5 of the file.</dl>
<h2>Description</h2>
<p>Sets the MD5 checksum for <code>file</code> \&amp;. </p>
<p> You need to call <code><a href="/docs/linux/man/3-mongoc_gridfs_file_save/">mongoc_gridfs_file_save</a>(3)</code> to persist this change. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
