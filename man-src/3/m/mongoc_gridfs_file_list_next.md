---
title: "mongoc_gridfs_file_list_next(3)"
name: "mongoc_gridfs_file_list_next"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_list_next/"
description: "mongoc_gridfs_file_list_next() – This function shall iterate the underlying gridfs file list, returning the next file each iteration. This is a blocking function."
---

<p>mongoc_gridfs_file_list_next() &#8211; This function shall iterate the underlying gridfs file list, returning the next file each iteration. This is a blocking function.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_t *
mongoc_gridfs_file_list_next (mongoc_gridfs_file_list_t *list);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>list</code></p>
<dd>A <code>mongoc_gridfs_file_list_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall iterate the underlying gridfs file list, returning the next file each iteration. This is a blocking function. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_gridfs_file_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_destroy/">mongoc_gridfs_file_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
