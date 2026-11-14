---
title: "bson_iter_dbpointer(3)"
name: "bson_iter_dbpointer"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_dbpointer/"
description: "bson_iter_dbpointer() – Fetches the contents of a BSON_TYPE_DBPOINTER element."
---

<h2>NAME</h2>
<p> bson_iter_dbpointer() &#8211; Fetches the contents of a BSON_TYPE_DBPOINTER element.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_iter_dbpointer(const bson_iter_t *iter,
                         uint32_t *collection_len,
                         const char **collection,
                         const bson_oid_t **oid);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>collection_len</code></p>
<dd> A location for the length of the collection name.</dl>
<dl>
<dt><code>collection</code></p>
<dd> A location for the collection name..</dl>
<dl>
<dt><code>oid</code></p>
<dd> A location for a <code>bson_oid_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the contents of a BSON_TYPE_DBPOINTER element. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> The BSON_TYPE_DBPOINTER field type is deprecated by the BSON spec and should not be used in new code.</dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
