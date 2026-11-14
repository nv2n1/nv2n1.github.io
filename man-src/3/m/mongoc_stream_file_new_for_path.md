---
title: "mongoc_stream_file_new_for_path(3)"
name: "mongoc_stream_file_new_for_path"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_file_new_for_path/"
description: "mongoc_stream_file_new_for_path() – This function shall create a new mongoc_stream_file_t after opening the underlying file with open() or the platform equivalent."
---

<p>mongoc_stream_file_new_for_path() &#8211; This function shall create a new mongoc_stream_file_t after opening the underlying file with open() or the platform equivalent.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_file_new_for_path (const char *path,
 int flags,
 int mode);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>path</code></p>
<dd>The path of the target file.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>Flags to be passed to <code><a href="/docs/linux/man/3-open/">open</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>mode</code></p>
<dd>An optional mode to be passed to <code><a href="/docs/linux/man/3-open/">open</a>(3)</code> when creating a file.</dl>
<p> This function shall create a new <code>mongoc_stream_file_t</code> after opening the underlying file with <code><a href="/docs/linux/man/3-open/">open</a>(3)</code> or the platform equivalent. </p>
<h2>Returns</h2>
<p><code>NULL</code> on failure, otherwise a newly allocated <code>mongoc_stream_file_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_stream_destroy/">mongoc_stream_destroy</a>(3)</code> when no longer in use. </p>
<p> <code>errno</code> is set upon failure. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
