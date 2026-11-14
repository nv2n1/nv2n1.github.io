---
title: "mongoc_gridfs_file_list_error(3)"
name: "mongoc_gridfs_file_list_error"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_list_error/"
description: "mongoc_gridfs_file_list_error() – Fetches any error that has occurred while trying to retrieve the file list."
---

<p>mongoc_gridfs_file_list_error() &#8211; Fetches any error that has occurred while trying to retrieve the file list.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_gridfs_file_list_error (mongoc_gridfs_file_list_t *list,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>list</code></p>
<dd>A <code>mongoc_gridfs_file_list_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches any error that has occurred while trying to retrieve the file list. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>false if no error has been registered, otherwise true and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
