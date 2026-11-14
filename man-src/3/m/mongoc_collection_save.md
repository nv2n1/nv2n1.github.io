---
title: "mongoc_collection_save(3)"
name: "mongoc_collection_save"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_save/"
description: "mongoc_collection_save() – This function shall save a document into collection. If the document has an _id field it will be updated. Otherwise it will be inserted."
---

<p>mongoc_collection_save() &#8211; This function shall save a document into collection. If the document has an _id field it will be updated. Otherwise it will be inserted.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_save (mongoc_collection_t *collection,
 const bson_t *document,
 const mongoc_write_concern_t *write_concern,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>document</code></p>
<dd>A <code>bson_t</code> containing the document.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> or <code>NULL</code> for default write concern.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall save a document into <code>collection</code> \&amp;. If the document has an <code>_id</code> field it will be updated. Otherwise it will be inserted. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
