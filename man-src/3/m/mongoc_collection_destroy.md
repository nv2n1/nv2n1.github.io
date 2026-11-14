---
title: "mongoc_collection_destroy(3)"
name: "mongoc_collection_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_destroy/"
description: "mongoc_collection_destroy() – This function shall destroy a mongoc_collection_t and its associated resources."
---

<p>mongoc_collection_destroy() &#8211; This function shall destroy a mongoc_collection_t and its associated resources.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_collection_destroy (mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall destroy a <code>mongoc_collection_t</code> and its associated resources. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Always destroy a <code>mongoc_cursor_t</code> created from a collection before destroying the collection.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
