---
title: "mongoc_collection_drop_index(3)"
name: "mongoc_collection_drop_index"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_drop_index/"
description: "mongoc_collection_drop_index() – This function requests than an index on collection be dropped. In the event of an error it returns false and error is set."
---

<p>mongoc_collection_drop_index() &#8211; This function requests than an index on collection be dropped. In the event of an error it returns false and error is set.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_drop_index (mongoc_collection_t *collection,
 const char *index_name,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>index_name</code></p>
<dd>A string containing the name of the index.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function requests than an index on <code>collection</code> be dropped. In the event of an error it returns false and error is set. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>true if successful, otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
