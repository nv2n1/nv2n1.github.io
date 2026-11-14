---
title: "mongoc_collection_update(3)"
name: "mongoc_collection_update"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_update/"
description: "mongoc_collection_update() – This function shall update documents in collection that match selector."
---

<p>mongoc_collection_update() &#8211; This function shall update documents in collection that match selector.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_update (mongoc_collection_t *collection,
 mongoc_update_flags_t flags,
 const bson_t *selector,
 const bson_t *update,
 const mongoc_write_concern_t *write_concern,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A bitwise or of <code>mongoc_update_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>selector</code></p>
<dd>A <code>bson_t</code> containing the query to match documents for updating.</dl>
<dl COMPACT>
<dt><code>update</code></p>
<dd>A <code>bson_t</code> containing the update to perform.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall update documents in <code>collection</code> that match <code>selector</code> \&amp;. </p>
<p> By default, updates only a single document. Set flags to <code>MONGOC_UPDATE_MULTI_UPDATE</code> to update multiple documents. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
