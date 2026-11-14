---
title: "mongoc_stream_gridfs_new(3)"
name: "mongoc_stream_gridfs_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_gridfs_new/"
description: "mongoc_stream_gridfs_new() – This function shall create a new mongoc_gridfs_file_t. This function does not transfer ownership of file. Therefore, file must remain valid for the lifetime of this str..."
---

<p>mongoc_stream_gridfs_new() &#8211; This function shall create a new mongoc_gridfs_file_t. This function does not transfer ownership of file. Therefore, file must remain valid for the lifetime of this stream.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_gridfs_new (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<p> This function shall create a new <code>mongoc_gridfs_file_t</code> \&amp;. This function does not transfer ownership of <code>file</code> \&amp;. Therefore, <code>file</code> must remain valid for the lifetime of this stream. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_stream_gridfs_t</code> if successful, otherwise <code>NULL</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
