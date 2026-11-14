---
title: "mongoc_stream_file_get_fd(3)"
name: "mongoc_stream_file_get_fd"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_file_get_fd/"
description: "mongoc_stream_file_get_fd() – This function shall return the underlying file-descriptor of a mongoc_stream_file_t."
---

<p>mongoc_stream_file_get_fd() &#8211; This function shall return the underlying file-descriptor of a mongoc_stream_file_t.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_stream_file_get_fd (mongoc_stream_file_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_file_t</code> \&amp;.</dl>
<p> This function shall return the underlying file-descriptor of a <code>mongoc_stream_file_t</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Performing operations on the underlying file-descriptor may not be safe if used in conjunction with buffering. Avoid reading or writing from this file-descriptor.</dl>
<h2>Returns</h2>
<p>A file-descriptor that should not be modified by the caller. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
