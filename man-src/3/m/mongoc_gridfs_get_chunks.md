---
title: "mongoc_gridfs_get_chunks(3)"
name: "mongoc_gridfs_get_chunks"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_get_chunks/"
description: "mongoc_gridfs_get_chunks() – Returns a mongoc_collection_t that contains the chunks for files. This instance is owned by the mongoc_gridfs_t instance and should not be modified or freed."
---

<p>mongoc_gridfs_get_chunks() &#8211; Returns a mongoc_collection_t that contains the chunks for files. This instance is owned by the mongoc_gridfs_t instance and should not be modified or freed.</p>
<h2>Synopsis</h2>
<pre>mongoc_collection_t *
mongoc_gridfs_get_chunks (mongoc_gridfs_t *gridfs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>gridfs</code></p>
<dd>A <code>mongoc_gridfs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Returns a <code>mongoc_collection_t</code> that contains the chunks for files. This instance is owned by the <code>mongoc_gridfs_t</code> instance and should not be modified or freed. </p>
<h2>Returns</h2>
<p>Returns a <code>mongoc_collection_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
