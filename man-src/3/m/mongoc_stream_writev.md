---
title: "mongoc_stream_writev(3)"
name: "mongoc_stream_writev"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_writev/"
description: "mongoc_stream_writev() – The mongoc_stream_writev() function shall perform a write to a mongoc_stream_t. It’s modeled on the API and semantics of writev(), though the parameters map only loosely."
---

<p>mongoc_stream_writev() &#8211; The mongoc_stream_writev() function shall perform a write to a mongoc_stream_t. It&#8217;s modeled on the API and semantics of writev(), though the parameters map only loosely.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_stream_writev (mongoc_stream_t *stream,
 mongoc_iovec_t *iov,
 size_t iovcnt,
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
<dt><code>timeout_msec</code></p>
<dd>The number of milliseconds to block before indicating failure, or 0 for non-blocking. Negative values indicate the default timeout.</dl>
<p> The <code><a href="/docs/linux/man/3-mongoc_stream_writev/">mongoc_stream_writev</a>(3)</code> function shall perform a write to a <code>mongoc_stream_t</code> \&amp;. It&#8217;s modeled on the API and semantics of <code><a href="/docs/linux/man/3-writev/">writev</a>(3)</code> , though the parameters map only loosely. </p>
<h2>Returns</h2>
<p>The number of bytes written on success, or <code>-1</code> upon failure and <code>errno</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
