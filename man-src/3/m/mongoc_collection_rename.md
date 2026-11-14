---
title: "mongoc_collection_rename(3)"
name: "mongoc_collection_rename"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_rename/"
description: "mongoc_collection_rename() – This function is a helper to rename an existing collection on a MongoDB server. The name of the collection will also be updated internally so it is safe to continue usi..."
---

<p>mongoc_collection_rename() &#8211; This function is a helper to rename an existing collection on a MongoDB server. The name of the collection will also be updated internally so it is safe to continue using this collection after the rename. Additional operations will occur on renamed collection.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_rename (mongoc_collection_t *collection,
 const char *new_db,
 const char *new_name,
 bool drop_target_before_rename,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>new_db</code></p>
<dd>The name of the new database.</dl>
<dl COMPACT>
<dt><code>new_name</code></p>
<dd>The new name for the collection.</dl>
<dl COMPACT>
<dt><code>drop_target_before_rename</code></p>
<dd>If an existing collection matches the new name, drop it before the rename.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function is a helper to rename an existing collection on a MongoDB server. The name of the collection will also be updated internally so it is safe to continue using this collection after the rename. Additional operations will occur on renamed collection. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if the command executed successfully, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
