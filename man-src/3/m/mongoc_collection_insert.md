---
title: "mongoc_collection_insert(3)"
name: "mongoc_collection_insert"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_insert/"
description: "mongoc_collection_insert() – This function shall insert document into collection."
---

<p>mongoc_collection_insert() &#8211; This function shall insert document into collection.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_insert (mongoc_collection_t *collection,
 mongoc_insert_flags_t flags,
 const bson_t *document,
 const mongoc_write_concern_t *write_concern,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A <code>mongoc_insert_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>document</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall insert <code>document</code> into <code>collection</code> \&amp;. </p>
<p> If no <code>_id</code> element is found in <code>document</code> , then a <code>bson_oid_t</code> will be generated locally and added to the document. </p>
<p> You can retrieve a generated <code>_id</code> from <code><a href="/docs/linux/man/3-mongoc_collection_get_last_error/">mongoc_collection_get_last_error</a>(3)</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if the document was successfully inserted, otherwise false and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
