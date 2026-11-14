---
title: "mongoc_gridfs_file_list_t(3)"
name: "mongoc_gridfs_file_list_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_file_list_t/"
description: "mongoc_gridfs_file_list_t – mongoc_gridfs_file_list_t provides a gridfs file list abstraction. It provides iteration and basic marshalling on top of a regular mongoc_collection_find() style query. ..."
---

<p>mongoc_gridfs_file_list_t &#8211; mongoc_gridfs_file_list_t provides a gridfs file list abstraction. It provides iteration and basic marshalling on top of a regular mongoc_collection_find() style query. In interface, it&#8217;s styled after mongoc_cursor_t.</p>
<h2>Synopsis</h2>
<pre>#include &lt;mongoc.h&gt;
typedef struct _mongoc_gridfs_file_list_t mongoc_gridfs_file_list_t;</pre>
<h2>Description</h2>
<p><code>mongoc_gridfs_file_list_t</code> provides a gridfs file list abstraction. It provides iteration and basic marshalling on top of a regular <code><a href="/docs/linux/man/3-mongoc_collection_find/">mongoc_collection_find</a>(3)</code> style query. In interface, it&#8217;s styled after <code>mongoc_cursor_t</code> \&amp;. </p>
<h2>Example</h2>
<pre>mongoc_gridfs_file_list_t *list;
mongoc_gridfs_file_t *file;
list = mongoc_gridfs_find (gridfs, query);
while ((file = mongoc_gridfs_file_list_next (list))) {
 do_something(file);
 mongoc_gridfs_file_destroy (file);
}
mongoc_gridfs_file_list_destroy (list);</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
