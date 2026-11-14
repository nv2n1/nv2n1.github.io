---
title: "mongoc_stream_write(3)"
name: "mongoc_stream_write"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_write/"
description: "mongoc_stream_write() – The mongoc_stream_write() function shall perform a write to a mongoc_stream_t. It’s modeled on the API and semantics of write(), though the parameters map only loosely."
---

<p>mongoc_stream_write() &#8211; The mongoc_stream_write() function shall perform a write to a mongoc_stream_t. It&#8217;s modeled on the API and semantics of write(), though the parameters map only loosely.</p>
<h2>Synopsis</h2>
<pre>
ssize_t
mongoc_stream_write (mongoc_stream_t *stream,
                    void            *buf,
                    size_t           count,
                    int32_t          timeout_msec);
</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd> A <code>mongoc_stream_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>buf</code></p>
<dd> The buffer to write.</dl>
<dl COMPACT>
<dt><code>count</code></p>
<dd> The number of bytes to write.</dl>
<dl COMPACT>
<dt><code>timeout_msec</code></p>
<dd> The number of milliseconds to wait before failure, a timeout of 0 will not block. If negative, use the default timeout.</dl>
<p> The <code><a href="/docs/linux/man/3-mongoc_stream_write/">mongoc_stream_write</a>(3)</code> function shall perform a write to a <code>mongoc_stream_t</code> \&amp;. It&#8217;s modeled on the API and semantics of <code><a href="/docs/linux/man/3-write/">write</a>(3)</code> , though the parameters map only loosely. </p>
<h2>Returns</h2>
<p> The <code>mongoc_stream_write</code> function returns the number of bytes write on success. It returns <code>&gt;= 0</code> and <code>&lt; min_bytes</code> when end-of-file is encountered and <code>-1</code> on failure. <code>errno</code> is set upon failure. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_read/">mongoc_stream_read</a>(3)</code> </p>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_readv/">mongoc_stream_readv</a>(3)</code> </p>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_writev/">mongoc_stream_writev</a>(3)</code> </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
