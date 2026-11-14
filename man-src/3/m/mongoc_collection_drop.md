---
title: "mongoc_collection_drop(3)"
name: "mongoc_collection_drop"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_drop/"
description: "mongoc_collection_drop() – This function requests that a collection be dropped, including all indexes associated with the collection."
---

<p>mongoc_collection_drop() &#8211; This function requests that a collection be dropped, including all indexes associated with the collection.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_drop (mongoc_collection_t *collection,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function requests that a <code>collection</code> be dropped, including all indexes associated with the <code>collection</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>Returns true if the collection was successfully dropped. Otherwise false and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
