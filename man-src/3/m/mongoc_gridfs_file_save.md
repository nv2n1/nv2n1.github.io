---
title: "mongoc_gridfs_file_save(3)"
name: "mongoc_gridfs_file_save"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_save/"
description: "mongoc_gridfs_file_save() – Saves modifications to file to the MongoDB server."
---

<p>mongoc_gridfs_file_save() &#8211; Saves modifications to file to the MongoDB server.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_gridfs_file_save (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Saves modifications to <code>file</code> to the MongoDB server. </p>
<p> If an error occurred, false is returned and the error can be retrieved with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_error/">mongoc_gridfs_file_error</a>(3)</code> \&amp;. </p>
<h2>Returns</h2>
<p>Returns true if successful, otherwise false. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
