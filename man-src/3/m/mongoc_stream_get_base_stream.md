---
title: "mongoc_stream_get_base_stream(3)"
name: "mongoc_stream_get_base_stream"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_get_base_stream/"
description: "mongoc_stream_get_base_stream() – This function shall fetch the underlying stream for streams that wrap a base stream. Such implementations include mongoc_stream_buffered_t and mongoc_stream_tls_t."
---

<p>mongoc_stream_get_base_stream() &#8211; This function shall fetch the underlying stream for streams that wrap a base stream. Such implementations include mongoc_stream_buffered_t and mongoc_stream_tls_t.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_get_base_stream (mongoc_stream_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<p> This function shall fetch the underlying stream for streams that wrap a base stream. Such implementations include <code>mongoc_stream_buffered_t</code> and <code>mongoc_stream_tls_t</code> \&amp;. </p>
<h2>Returns</h2>
<p>A <code>mongoc_stream_t</code> or <code>NULL</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
