---
title: "mongoc_collection_set_read_concern(3)"
name: "mongoc_collection_set_read_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_set_read_concern/"
description: "mongoc_collection_set_read_concern() – Sets the read concern to use for operations on collection."
---

<p>mongoc_collection_set_read_concern() &#8211; Sets the read concern to use for operations on collection.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_collection_set_read_concern (mongoc_collection_t *collection,
 const mongoc_read_concern_t *read_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_concern</code></p>
<dd>A <code>mongoc_read_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the read concern to use for operations on <code>collection</code> \&amp;. </p>
<p> The default read concern is empty: No readConcern is sent to the server unless explicitly configured. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
