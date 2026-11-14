---
title: "mongoc_collection_get_write_concern(3)"
name: "mongoc_collection_get_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_get_write_concern/"
description: "mongoc_collection_get_write_concern() – Fetches the default write concern to be used on write operations originating from collection and not specifying a write concern."
---

<p>mongoc_collection_get_write_concern() &#8211; Fetches the default write concern to be used on write operations originating from collection and not specifying a write concern.</p>
<h2>Synopsis</h2>
<pre>const mongoc_write_concern_t *
mongoc_collection_get_write_concern (const mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the default write concern to be used on write operations originating from <code>collection</code> and not specifying a write concern. </p>
<h2>Returns</h2>
<p>A <code>mongoc_write_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
