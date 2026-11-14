---
title: "mongoc_client_get_collection(3)"
name: "mongoc_client_get_collection"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_collection/"
description: "mongoc_client_get_collection() – None"
---

<p>mongoc_client_get_collection() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
mongoc_collection_t *
mongoc_client_get_collection (mongoc_client_t *client,
                              const char      *db,
                              const char      *collection);
</pre>
<p> Get a newly allocated <code>mongoc_collection_t</code> for the collection named <code>collection</code> in the database named <code>db</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> Collections are automatically created on the MongoDB server upon insertion of the first document. There is no need to create a collection manually.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd> A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>db</code></p>
<dd> The name of the database containing the collection.</dl>
<dl COMPACT>
<dt><code>collection</code></p>
<dd> The name of the collection.</dl>
<h2>Returns</h2>
<p> A newly allocated <code>mongoc_collection_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_collection_destroy/">mongoc_collection_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
