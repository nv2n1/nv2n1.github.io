---
title: "mongoc_collection_delete(3)"
name: "mongoc_collection_delete"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_delete/"
description: "mongoc_collection_delete() – This function shall delete documents in the given collection that match selector. The bson selector is not validated, simply passed along as appropriate to the server. ..."
---

<p>mongoc_collection_delete() &#8211; This function shall delete documents in the given collection that match selector. The bson selector is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_delete (mongoc_collection_t *collection,
 mongoc_delete_flags_t flags,
 const bson_t *selector,
 const mongoc_write_concern_t *write_concern,
 bson_error_t *error);</pre>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>This function is deprecated and should not be used in new code.</dl>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_collection_remove/">mongoc_collection_remove</a>(3)</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>A <code>mongoc_delete_flags_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>selector</code></p>
<dd>A <code>bson_t</code> containing the query to match documents.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall delete documents in the given <code>collection</code> that match <code>selector</code> \&amp;. The bson <code>selector</code> is not validated, simply passed along as appropriate to the server. As such, compatibility and errors should be validated in the appropriate server documentation. </p>
<p> If you want to limit deletes to a single document, provide <code>MONGOC_DELETE_SINGLE_REMOVE</code> in <code>flags</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
