---
title: "mongoc_stream_readv(3)"
name: "mongoc_stream_readv"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_readv/"
description: "mongoc_stream_readv() – This function is identical to mongoc_stream_read() except that it takes a mongoc_iovec_t to perform gathered I/O."
---

<p>mongoc_stream_readv() &#8211; This function is identical to mongoc_stream_read() except that it takes a mongoc_iovec_t to perform gathered I/O.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_stream_readv (mongoc_stream_t *stream,
 mongoc_iovec_t *iov,
 size_t iovcnt,
 size_t min_bytes,
 int32_t timeout_msec);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>iov</code></p>
<dd>A vector of <code>mongoc_iovec_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>iovcnt</code></p>
<dd>The number of items in <code>iov</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>min_bytes</code></p>
<dd>The minimum number of bytes to read or failure will be indicated.</dl>
<dl COMPACT>
<dt><code>timeout_msec</code></p>
<dd>A timeout in milliseconds, or 0 to indicate non-blocking. A negative value with use the default timeout.</dl>
<p> This function is identical to <code><a href="/docs/linux/man/3-mongoc_stream_read/">mongoc_stream_read</a>(3)</code> except that it takes a <code>mongoc_iovec_t</code> to perform gathered I/O. </p>
<h2>Returns</h2>
<p><code>&gt;= 0</code> on success, <code>-1</code> on failure and <code>errno</code> is set. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mongoc_stream_read/">mongoc_stream_read</a>(3)</code> </p>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_write/">mongoc_stream_write</a>(3)</code> </p>
<p> <code><a href="/docs/linux/man/3-mongoc_stream_writev/">mongoc_stream_writev</a>(3)</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
