---
title: "mongoc_gridfs_file_tell(3)"
name: "mongoc_gridfs_file_tell"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_tell/"
description: "mongoc_gridfs_file_tell() – This function returns the current position indicator within file."
---

<p>mongoc_gridfs_file_tell() &#8211; This function returns the current position indicator within file.</p>
<h2>Synopsis</h2>
<pre>uint64_t
mongoc_gridfs_file_tell (mongoc_gridfs_file_t *file);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function returns the current position indicator within <code>file</code> \&amp;. </p>
<h2>Returns</h2>
<p>Returns a file position as an unsigned 64-bit integer. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
