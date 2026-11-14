---
title: "mongoc_collection_insert_bulk(3)"
name: "mongoc_collection_insert_bulk"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_insert_bulk/"
description: "mongoc_collection_insert_bulk() – This function performs a bulk insert of all of the documents in documents. This function is deprecated as it cannot accurately return which documents may have fail..."
---

<p>mongoc_collection_insert_bulk() &#8211; This function performs a bulk insert of all of the documents in documents. This function is deprecated as it cannot accurately return which documents may have failed during the bulk insert.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_insert_bulk (mongoc_collection_t *collection,
 mongoc_insert_flags_t flags,
 const bson_t **documents,
 uint32_t n_documents,
 const mongoc_write_concern_t *write_concern,
 bson_error_t *error)
 BSON_GNUC_DEPRECATED_FOR (mongoc_collection_create_bulk_operation);</pre>
<h2>Deprecated</h2>
<p>This function is deprecated and should not be used in new code. </p>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_collection_create_bulk_operation/">mongoc_collection_create_bulk_operation</a>(3)</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A bitwise or of <code>mongoc_insert_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>documents</code></p>
<dd>An array of <code>const bson_t *</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>n_documents</code></p>
<dd>The number of documents in <code>documents</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function performs a bulk insert of all of the documents in <code>documents</code> \&amp;. This function is deprecated as it cannot accurately return which documents may have failed during the bulk insert. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
