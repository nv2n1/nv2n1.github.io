---
title: "mongoc_gridfs_file_writev(3)"
name: "mongoc_gridfs_file_writev"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_writev/"
description: "mongoc_gridfs_file_writev() – Performs a gathered write to the underlying gridfs file."
---

<p>mongoc_gridfs_file_writev() &#8211; Performs a gathered write to the underlying gridfs file.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_gridfs_file_writev (mongoc_gridfs_file_t *file,
 mongoc_iovec_t *iov,
 size_t iovcnt,
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
<dt><code>timeout_msec</code></p>
<dd>A uint32_t with the timeout in milliseconds.</dl>
<h2>Description</h2>
<p>Performs a gathered write to the underlying gridfs file. </p>
<p> If timeout is reached, then -1 is returned and errno is set to ETIMEDOUT. </p>
<h2>Returns</h2>
<p>Returns the number of bytes written or -1 upon error and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
