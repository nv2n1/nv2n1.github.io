---
title: "mongoc_collection_copy(3)"
name: "mongoc_collection_copy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_copy/"
description: "mongoc_collection_copy() – Performs a deep copy of the collection struct and its configuration. Useful if you intend to call mongoc_collection_set_write_concern, mongoc_collection_set_read_prefs, o..."
---

<p>mongoc_collection_copy() &#8211; Performs a deep copy of the collection struct and its configuration. Useful if you intend to call mongoc_collection_set_write_concern, mongoc_collection_set_read_prefs, or mongoc_collection_set_read_concern, and want to preserve an unaltered copy of the struct.</p>
<h2>Synopsis</h2>
<pre>mongoc_collection_t *
mongoc_collection_copy (mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Performs a deep copy of the <code>collection</code> struct and its configuration. Useful if you intend to call <code>mongoc_collection_set_write_concern</code> , <code>mongoc_collection_set_read_prefs</code> , or <code>mongoc_collection_set_read_concern</code> , and want to preserve an unaltered copy of the struct. </p>
<p> This function does <code>not</code> copy the contents of the collection on the MongoDB server; use the for that purpose. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_collection_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_collection_destroy/">mongoc_collection_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
