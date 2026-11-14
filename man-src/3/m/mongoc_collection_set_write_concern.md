---
title: "mongoc_collection_set_write_concern(3)"
name: "mongoc_collection_set_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_set_write_concern/"
description: "mongoc_collection_set_write_concern() – Sets the write concern to use for operations on collection."
---

<p>mongoc_collection_set_write_concern() &#8211; Sets the write concern to use for operations on collection.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_collection_set_write_concern (mongoc_collection_t *collection,
 const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the write concern to use for operations on <code>collection</code> \&amp;. </p>
<p> The default write concern is MONGOC_WRITE_CONCERN_W_DEFAULT: the driver blocks awaiting basic acknowledgment of write operations from MongoDB. This is the correct write concern for the great majority of applications. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
