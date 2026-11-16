---
title: "mongoc_collection_ensure_index(3)"
name: "mongoc_collection_ensure_index"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_ensure_index/"
description: "mongoc_collection_ensure_index() – None"
---

<p>mongoc_collection_ensure_index() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_ensure_index (mongoc_collection_t *collection,
 const bson_t *keys,
 const mongoc_index_opt_t *opt,
 bson_error_t *error)
 BSON_GNUC_DEPRECATED_FOR (mongoc_collection_create_index);</pre>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>This function is deprecated and should not be used in new code.</dd></dl>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_collection_create_index/">mongoc_collection_create_index</a>(3)</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></dt>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>keys</code></dt>
<dd>A <code>bson_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>opt</code></dt>
<dd>A mongoc_index_opt_t.</dd></dl>
<dl COMPACT>
<dt><code>error</code></dt>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dd></dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
