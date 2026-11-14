---
title: "mongoc_gridfs_file_error(3)"
name: "mongoc_gridfs_file_error"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_error/"
description: "mongoc_gridfs_file_error() – This function checks to see if there has been an error associated with the last operation upon file."
---

<p>mongoc_gridfs_file_error() &#8211; This function checks to see if there has been an error associated with the last operation upon file.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_gridfs_file_error (mongoc_gridfs_file_t *file,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>file</code></p>
<dd>A <code>mongoc_gridfs_file_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function checks to see if there has been an error associated with the last operation upon <code>file</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns false if there has been no registered error, otherwise true and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
