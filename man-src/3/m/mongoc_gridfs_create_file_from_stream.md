---
title: "mongoc_gridfs_create_file_from_stream(3)"
name: "mongoc_gridfs_create_file_from_stream"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_create_file_from_stream/"
description: "mongoc_gridfs_create_file_from_stream() – This function shall create a new mongoc_gridfs_file_t and fill it with the contents of stream. Note that this function will read from stream until End of F..."
---

<p>mongoc_gridfs_create_file_from_stream() &#8211; This function shall create a new mongoc_gridfs_file_t and fill it with the contents of stream. Note that this function will read from stream until End of File, making it bet suited for file-backed streams.</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_file_t *
mongoc_gridfs_create_file_from_stream (mongoc_gridfs_t *gridfs,
 mongoc_stream_t *stream,
 mongoc_gridfs_file_opt_t *opt);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code><a href="/docs/linux/man/3-mongoc_gridfs_t/">mongoc_gridfs_t</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opt</code></p>
<dd>A <code>mongoc_gridfs_file_opt_t</code> to specify file options.</dl>
<h2>Description</h2>
<p>This function shall create a new <code>mongoc_gridfs_file_t</code> and fill it with the contents of <code>stream</code> \&amp;. Note that this function will read from <code>stream</code> until End of File, making it bet suited for file-backed streams. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_gridfs_file_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_gridfs_file_destroy/">mongoc_gridfs_file_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
