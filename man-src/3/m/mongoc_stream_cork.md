---
title: "mongoc_stream_cork(3)"
name: "mongoc_stream_cork"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_cork/"
description: "mongoc_stream_cork() – This function shall prevent the writing of bytes to the underlying socket."
---

<p>mongoc_stream_cork() &#8211; This function shall prevent the writing of bytes to the underlying socket.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_stream_cork (mongoc_stream_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<p> This function shall prevent the writing of bytes to the underlying socket. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Not all streams implement this function. Buffering generally works better.</dl>
<h2>Returns</h2>
<p><code>0</code> on success, <code>-1</code> on failure and <code>errno</code> is set. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mongoc_stream_buffered_new/">mongoc_stream_buffered_new</a>(3)</code> \&amp;. </p>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_uncork/">mongoc_stream_uncork</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
