---
title: "mongoc_collection_find_and_modify_with_opts(3)"
name: "mongoc_collection_find_and_modify_with_opts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_find_and_modify_with_opts/"
description: "mongoc_collection_find_and_modify_with_opts() – Update and return an object."
---

<p>mongoc_collection_find_and_modify_with_opts() &#8211; Update and return an object.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_find_and_modify_with_opts (mongoc_collection_t *collection,
 const bson_t *query,
 const mongoc_find_and_modify_opts_t *opts,
 bson_t *reply,
 bson_error_t *error);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> containing the query to locate target document(s).</dl>
<dl COMPACT>
<dt><code>opts</code></p>
<dd><code>find and modify options</code></dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>An optional location for a <code>bson_t</code> that will be initialized with the result or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>Update and return an object. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns true on success; false on failure. </p>
<h2>Example</h2>
<p>See <code>mongoc_find_and_modify_opts_t</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
