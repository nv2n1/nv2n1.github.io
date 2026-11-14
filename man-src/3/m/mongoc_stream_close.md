---
title: "mongoc_stream_close(3)"
name: "mongoc_stream_close"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_close/"
description: "mongoc_stream_close() – This function shall close underlying file-descriptors of stream."
---

<p>mongoc_stream_close() &#8211; This function shall close underlying file-descriptors of stream.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_stream_close (mongoc_stream_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<p> This function shall close underlying file-descriptors of <code>stream</code> \&amp;. </p>
<h2>Returns</h2>
<p><code>0</code> on success, otherwise <code>-1</code> and <code>errno</code> is set. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mongoc_stream_destroy/">mongoc_stream_destroy</a>(3)</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
