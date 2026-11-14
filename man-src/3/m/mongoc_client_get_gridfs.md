---
title: "mongoc_client_get_gridfs(3)"
name: "mongoc_client_get_gridfs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_gridfs/"
description: "mongoc_client_get_gridfs() – None"
---

<p>mongoc_client_get_gridfs() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_gridfs_t *
mongoc_client_get_gridfs (mongoc_client_t *client,
 const char *db,
 const char *prefix,
 bson_error_t *error);</pre>
<p>The <code><a href="/docs/linux/man/3-mongoc_client_get_gridfs/">mongoc_client_get_gridfs</a>(3)</code> function shall create a new <code>mongoc_gridfs_t</code> \&amp;. The <code>db</code> parameter is the name of the database which the gridfs instance should exist in. The <code>prefix</code> parameter corresponds to the gridfs collection namespacing; its default is &quot;fs&quot;, thus the default GridFS collection names are &quot;fs.files&quot; and &quot;fs.chunks&quot;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>db</code></p>
<dd>The database name.</dl>
<dl COMPACT>
<dt><code>prefix</code></p>
<dd>Optional prefix for gridfs collection names or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A <code>mongoc_gridfs_t</code> on success, <code>NULL</code> upon failure and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
