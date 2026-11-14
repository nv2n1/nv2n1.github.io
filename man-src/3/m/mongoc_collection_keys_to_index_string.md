---
title: "mongoc_collection_keys_to_index_string(3)"
name: "mongoc_collection_keys_to_index_string"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_keys_to_index_string/"
description: "mongoc_collection_keys_to_index_string() – This function shall returns the canonical stringification, as used in mongoc_collection_create_index() without an explicit name, of a given key specificat..."
---

<p>mongoc_collection_keys_to_index_string() &#8211; This function shall returns the canonical stringification, as used in mongoc_collection_create_index() without an explicit name, of a given key specification.</p>
<h2>Synopsis</h2>
<pre>
char *
mongoc_collection_keys_to_index_string (const bson_t *keys);
</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>keys</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>Description</h2>
<p> This function shall returns the canonical stringification, as used in <code><a href="/docs/linux/man/3-mongoc_collection_create_index/">mongoc_collection_create_index</a>(3)</code> without an explicit name, of a given key specification. </p>
<p> It is a programming error to call this function on a non-standard index, such one other than a straight index with ascending and descending. </p>
<h2>Returns</h2>
<p> A string that should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
