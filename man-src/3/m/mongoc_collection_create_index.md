---
title: "mongoc_collection_create_index(3)"
name: "mongoc_collection_create_index"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_create_index/"
description: "mongoc_collection_create_index() – This function will request the creation of a new index."
---

<p>mongoc_collection_create_index() &#8211; This function will request the creation of a new index.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_create_index (mongoc_collection_t *collection,
 const bson_t *keys,
 const mongoc_index_opt_t *opt,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>keys</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opt</code></p>
<dd>A mongoc_index_opt_t.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function will request the creation of a new index. </p>
<p> This function will use the <code>createIndexes</code> command if available on the MongoDB server. If not, it will fallback to inserting into system.indexes for compatibility with MongoDB &lt;= 2.4. </p>
<p> See <code>mongoc_index_opt_t</code> for options on creating indexes. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true on success, false on failure and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
