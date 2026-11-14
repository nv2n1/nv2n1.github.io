---
title: "mongoc_gridfs_create_file(3)"
name: "mongoc_gridfs_create_file"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_create_file/"
description: "mongoc_gridfs_create_file() – This function shall create a new mongoc_gridfs_file_t."
---

<p>mongoc_gridfs_create_file() &#8211; This function shall create a new mongoc_gridfs_file_t.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_t *
mongoc_gridfs_create_file (mongoc_gridfs_t *gridfs,
 mongoc_gridfs_file_opt_t *opt);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opt</code></p>
<dd>A <code>mongoc_gridfs_file_opt_t</code> to specify file options.</dl>
<h2>Description</h2>
<p>This function shall create a new <code>mongoc_gridfs_file_t</code> \&amp;. </p>
<p> Use <code><a href="/docs/linux/man/3-mongoc_gridfs_file_writev/">mongoc_gridfs_file_writev</a>(3)</code> to write to the file. </p>
<h2>Returns</h2>
<p>Returns a newly allocated <code>mongoc_gridfs_file_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_destroy/">mongoc_gridfs_file_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
