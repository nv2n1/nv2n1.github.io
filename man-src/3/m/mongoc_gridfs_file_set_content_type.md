---
title: "mongoc_gridfs_file_set_content_type(3)"
name: "mongoc_gridfs_file_set_content_type"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_set_content_type/"
description: "mongoc_gridfs_file_set_content_type() – Sets the content type for the gridfs file. This should be something like \"text/plain\"."
---

<p>mongoc_gridfs_file_set_content_type() &#8211; Sets the content type for the gridfs file. This should be something like &quot;text/plain&quot;.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_gridfs_file_set_content_type (mongoc_gridfs_file_t *file,
 const char *content_type);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>str</code></p>
<dd>A string containing the content type.</dl>
<h2>Description</h2>
<p>Sets the content type for the gridfs file. This should be something like <code>text/plain</code> \&amp;. </p>
<p> You need to call <code><a href="/docs/linux/man/3-mongoc_gridfs_file_save/">mongoc_gridfs_file_save</a>(3)</code> to persist this change. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
