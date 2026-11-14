---
title: "mongoc_collection_get_read_concern(3)"
name: "mongoc_collection_get_read_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_get_read_concern/"
description: "mongoc_collection_get_read_concern() – Fetches the default read concern to be used on read operations originating from collection."
---

<p>mongoc_collection_get_read_concern() &#8211; Fetches the default read concern to be used on read operations originating from collection.</p>
<h2>Synopsis</h2>
<pre>const mongoc_read_concern_t *
mongoc_collection_get_read_concern (const mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the default read concern to be used on read operations originating from <code>collection</code> \&amp;. </p>
<h2>Returns</h2>
<p>A <code>mongoc_read_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
