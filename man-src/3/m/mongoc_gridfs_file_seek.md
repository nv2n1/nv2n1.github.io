---
title: "mongoc_gridfs_file_seek(3)"
name: "mongoc_gridfs_file_seek"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_seek/"
description: "mongoc_gridfs_file_seek() – Adjust the file position pointer in the given file by delta, starting from the position whence. The whence argument is interpreted as in fseek(2):"
---

<p>mongoc_gridfs_file_seek() &#8211; Adjust the file position pointer in the given file by delta, starting from the position whence. The whence argument is interpreted as in fseek(2):</p>
<h2>Synopsis</h2>
<pre>int
mongoc_gridfs_file_seek (mongoc_gridfs_file_t *file,
 int64_t delta,
 int whence);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></dt>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>delta</code></dt>
<dd>The amount to move the file position. May be positive or negative.</dd></dl>
<dl COMPACT>
<dt><code>whence</code></dt>
<dd>One of SEEK_SET, SEEK_CUR or SEEK_END.</dd></dl>
<h2>Description</h2>
<p>Adjust the file position pointer in the given file by <code>delta</code> , starting from the position <code>whence</code> \&amp;. The <code>whence</code> argument is interpreted as in <code>fseek(2)</code> : </p>
<dl COMPACT>
<dt><code>SEEK_SET</code></dt>
<dd>Set the position relative to the start of the file.</dd></dl>
<dl COMPACT>
<dt><code>SEEK_CUR</code></dt>
<dd>Move <code>delta</code> relative to the current file position.</dd></dl>
<dl COMPACT>
<dt><code>SEEK_END</code></dt>
<dd>Move <code>delta</code> relative to the end of the file.</dd></dl>
<p> On success, the file&#8217;s underlying position pointer is set appropriately. On failure, the file position is NOT changed and errno is set to indicate the error. </p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EINVAL</code></dt>
<dd><code>whence</code> is not one of SEEK_SET, SEEK_CUR or SEEK_END.</dd></dl>
<dl COMPACT>
<dt><code>EINVAL</code></dt>
<dd>The resulting file position would be negative.</dd></dl>
<h2>Returns</h2>
<p>Returns 0 if successful; otherwise -1 and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
