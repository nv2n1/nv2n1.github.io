---
title: "mongoc_collection_get_last_error(3)"
name: "mongoc_collection_get_last_error"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_get_last_error/"
description: "mongoc_collection_get_last_error() – The mongoc_collection_get_last_error() function shall return getLastError document, according to write_concern on last executed command for current collection i..."
---

<p>mongoc_collection_get_last_error() &#8211; The mongoc_collection_get_last_error() function shall return getLastError document, according to write_concern on last executed command for current collection instance.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_collection_get_last_error (const mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>The mongoc_collection_get_last_error() function shall return getLastError document, according to write_concern on last executed command for current collection instance. </p>
<p> A write_concern must be at least <code>MONGOC_WRITE_CONCERN_W_DEFAULT</code> in last command execution for this to be available. </p>
<h2>Returns</h2>
<p>A <code>bson_t</code> that should not be modified or <code>NULL</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
