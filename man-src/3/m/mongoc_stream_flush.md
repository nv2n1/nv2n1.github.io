---
title: "mongoc_stream_flush(3)"
name: "mongoc_stream_flush"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_flush/"
description: "mongoc_stream_flush() – This function shall flush any buffered bytes in the underlying stream to the physical transport. It mimics the API and semantics of fflush(), forcing a write of user space b..."
---

<p>mongoc_stream_flush() &#8211; This function shall flush any buffered bytes in the underlying stream to the physical transport. It mimics the API and semantics of fflush(), forcing a write of user space buffered data.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_stream_flush (mongoc_stream_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<p> This function shall flush any buffered bytes in the underlying stream to the physical transport. It mimics the API and semantics of <code><a href="/docs/linux/man/3-fflush/">fflush</a>(3)</code> , forcing a write of user space buffered data. </p>
<p> Not all stream implementations may implement this feature. </p>
<h2>Returns</h2>
<p>0 is returned on success, otherwise <code>-1</code> and <code>errno</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
