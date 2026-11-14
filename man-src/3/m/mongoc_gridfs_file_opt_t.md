---
title: "mongoc_gridfs_file_opt_t(3)"
name: "mongoc_gridfs_file_opt_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_opt_t/"
description: "mongoc_gridfs_file_opt_t – This structure contains options that can be set on a mongoc_gridfs_file_t. It can be used by various functions when creating a new gridfs file."
---

<p>mongoc_gridfs_file_opt_t &#8211; This structure contains options that can be set on a mongoc_gridfs_file_t. It can be used by various functions when creating a new gridfs file.</p>
<h2>Synopsis</h2>
<pre>typedef struct
{
 const char *md5;
 const char *filename;
 const char *content_type;
 const bson_t *aliases;
 const bson_t *metadata;
 uint32_t chunk_size;
} mongoc_gridfs_file_opt_t;</pre>
<h2>Description</h2>
<p>This structure contains options that can be set on a <code>mongoc_gridfs_file_t</code> \&amp;. It can be used by various functions when creating a new gridfs file. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
