---
title: "mongoc_database_get_collection(3)"
name: "mongoc_database_get_collection"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_get_collection/"
description: "mongoc_database_get_collection() – None"
---

<p>mongoc_database_get_collection() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_collection_t *
mongoc_database_get_collection (mongoc_database_t *database,
 const char *name);</pre>
<p>Allocates a new <code>mongoc_collection_t</code> structure for the collection named <code>name</code> in <code>database</code> \&amp;. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_collection_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_collection_destroy/">mongoc_collection_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
