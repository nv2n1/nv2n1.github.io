---
title: "mongoc_gridfs_file_readv(3)"
name: "mongoc_gridfs_file_readv"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_readv/"
description: "mongoc_gridfs_file_readv() – This function performs a scattered read from file, potentially blocking to read from the MongoDB server."
---

<p>mongoc_gridfs_file_readv() &#8211; This function performs a scattered read from file, potentially blocking to read from the MongoDB server.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_gridfs_file_readv (mongoc_gridfs_file_t *file,
 mongoc_iovec_t *iov,
 size_t iovcnt,
 size_t min_bytes,
 uint32_t timeout_msec);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>iov</code></p>
<dd>An array of <code>mongoc_iovec_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>iovcnt</code></p>
<dd>The number of elements in <code>iov</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>min_bytes</code></p>
<dd>The minimum number of bytes that must be read or an error will be synthesized.</dl>
<dl COMPACT>
<dt><code>timeout_msec</code></p>
<dd>A uint32_t with the timeout in milliseconds.</dl>
<h2>Description</h2>
<p>This function performs a scattered read from <code>file</code> , potentially blocking to read from the MongoDB server. </p>
<p> Timeout should be the number of milliseconds to allow blocking, or 0 to disallow blocking. </p>
<h2>Returns</h2>
<p>Returns the number of bytes read, or -1 on failure. Use <code>mongoc_gridfs_file_error</code> to retrieve error details. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
