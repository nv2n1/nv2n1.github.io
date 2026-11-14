---
title: "mongoc_gridfs_file_seek(3)"
name: "mongoc_gridfs_file_seek"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_seek/"
description: "mongoc_gridfs_file_seek() – Adjust the file position pointer in the given file by delta, starting from the position whence. The whence argument is interpreted as in fseek(2):"
---

<p>mongoc_gridfs_file_seek() &#8211; Adjust the file position pointer in the given file by delta, starting from the position whence. The whence argument is interpreted as in <a href="/docs/linux/man/2-fseek/">fseek</a>(2):</p>
<h2>Synopsis</h2>
<pre>int
mongoc_gridfs_file_seek (mongoc_gridfs_file_t *file,
 int64_t delta,
 int whence);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>delta</code></p>
<dd>The amount to move the file position. May be positive or negative.</dl>
<dl COMPACT>
<dt><code>whence</code></p>
<dd>One of SEEK_SET, SEEK_CUR or SEEK_END.</dl>
<h2>Description</h2>
<p>Adjust the file position pointer in the given file by <code>delta</code> , starting from the position <code>whence</code> \&amp;. The <code>whence</code> argument is interpreted as in <code><a href="/docs/linux/man/2-fseek/">fseek</a>(2)</code> : </p>
<dl COMPACT>
<dt><code>SEEK_SET</code></p>
<dd>Set the position relative to the start of the file.</dl>
<dl COMPACT>
<dt><code>SEEK_CUR</code></p>
<dd>Move <code>delta</code> relative to the current file position.</dl>
<dl COMPACT>
<dt><code>SEEK_END</code></p>
<dd>Move <code>delta</code> relative to the end of the file.</dl>
<p> On success, the file&#8217;s underlying position pointer is set appropriately. On failure, the file position is NOT changed and errno is set to indicate the error. </p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EINVAL</code></p>
<dd><code>whence</code> is not one of SEEK_SET, SEEK_CUR or SEEK_END.</dl>
<dl COMPACT>
<dt><code>EINVAL</code></p>
<dd>The resulting file position would be negative.</dl>
<h2>Returns</h2>
<p>Returns 0 if successful; otherwise -1 and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
