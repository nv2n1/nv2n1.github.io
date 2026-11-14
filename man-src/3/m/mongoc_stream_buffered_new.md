---
title: "mongoc_stream_buffered_new(3)"
name: "mongoc_stream_buffered_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_buffered_new/"
description: "mongoc_stream_buffered_new() – This function shall create a new mongoc_stream_t that buffers bytes to and from the underlying base_stream."
---

<p>mongoc_stream_buffered_new() &#8211; This function shall create a new mongoc_stream_t that buffers bytes to and from the underlying base_stream.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_buffered_new (mongoc_stream_t *base_stream,
 size_t buffer_size);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>base_stream</code></p>
<dd>A <code>mongoc_stream_t</code> to buffer.</dl>
<dl COMPACT>
<dt><code>buffer_size</code></p>
<dd>A size_t containing the desired buffer size.</dl>
<p> This function shall create a new <code>mongoc_stream_t</code> that buffers bytes to and from the underlying <code>base_stream</code> \&amp;. </p>
<p> <code>buffer_size</code> will be used as the initial buffer size. It may grow past this size. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_stream_buffered_t</code> on success, otherwise <code>NULL</code> \&amp;. This should be freed with <code><a href="/docs/linux/man/3-mongoc_stream_destroy/">mongoc_stream_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
