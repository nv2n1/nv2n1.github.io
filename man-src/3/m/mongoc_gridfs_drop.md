---
title: "mongoc_gridfs_drop(3)"
name: "mongoc_gridfs_drop"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_drop/"
description: "mongoc_gridfs_drop() – Requests that an entire GridFS be dropped, including all files associated with it."
---

<p>mongoc_gridfs_drop() &#8211; Requests that an entire GridFS be dropped, including all files associated with it.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_gridfs_drop (mongoc_gridfs_t *gridfs,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>Requests that an entire GridFS be dropped, including all files associated with it. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
