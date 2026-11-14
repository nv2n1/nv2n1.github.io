---
title: "mongoc_gridfs_file_t(3)"
name: "mongoc_gridfs_file_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_t/"
description: "mongoc_gridfs_file_t – This structure provides a MongoDB GridFS file abstraction. It provides several APIs."
---

<p>mongoc_gridfs_file_t &#8211; This structure provides a MongoDB GridFS file abstraction. It provides several APIs.</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_gridfs_file_t mongoc_gridfs_file_t;</pre>
<h2>Description</h2>
<p>This structure provides a MongoDB GridFS file abstraction. It provides several APIs. </p>
<dl COMPACT>
<dt>\[bu]</p>
<dd>readv, writev, seek, and tell.</p>
<dt>\[bu]</p>
<dd>General file metadata such as filename and length.</p>
<dt>\[bu]</p>
<dd>GridFS metadata such as md5, filename, content_type, aliases, metadata, chunk_size, and upload_date. </p>
</dl>
<h2>Thread Safety</h2>
<p>This structure is NOT thread-safe and should only be used from one thread at a time. </p>
<h2>Related</h2>
<dl COMPACT>
<dt>\[bu]</p>
<dd><code>mongoc_client_t</code></p>
<dt>\[bu]</p>
<dd><code>mongoc_gridfs_t</code></p>
<dt>\[bu]</p>
<dd><code>mongoc_gridfs_file_list_t</code></p>
<dt>\[bu]</p>
<dd><code>mongoc_gridfs_file_opt_t</code> </p>
<p> <code></dl>
<p> </code></p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
