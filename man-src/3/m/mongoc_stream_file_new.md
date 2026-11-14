---
title: "mongoc_stream_file_new(3)"
name: "mongoc_stream_file_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_file_new/"
description: "mongoc_stream_file_new() – Creates a new mongoc_stream_file_t using the file-descriptor provided."
---

<p>mongoc_stream_file_new() &#8211; Creates a new mongoc_stream_file_t using the file-descriptor provided.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_file_new (int fd);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>fd</code></p>
<dd>A UNIX style file-descriptor.</dl>
<p> Creates a new <code>mongoc_stream_file_t</code> using the file-descriptor provided. </p>
<h2>Returns</h2>
<p><code>NULL</code> upon failure, otherwise a newly allocated <code>mongoc_stream_file_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_stream_destroy/">mongoc_stream_destroy</a>(3)</code> when no longer in use. </p>
<p> <code>errno</code> is set upon failure. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
