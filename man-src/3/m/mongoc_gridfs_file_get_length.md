---
title: "mongoc_gridfs_file_get_length(3)"
name: "mongoc_gridfs_file_get_length"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_get_length/"
description: "mongoc_gridfs_file_get_length() – Fetches the length of the gridfs file in bytes."
---

<p>mongoc_gridfs_file_get_length() &#8211; Fetches the length of the gridfs file in bytes.</p>
<h2>Synopsis</h2>
<pre>int64_t
mongoc_gridfs_file_get_length (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the length of the gridfs file in bytes. </p>
<h2>Returns</h2>
<p>A 64-bit signed integer. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
