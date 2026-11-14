---
title: "mongoc_database_create_collection(3)"
name: "mongoc_database_create_collection"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_create_collection/"
description: "mongoc_database_create_collection() – None"
---

<p>mongoc_database_create_collection() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_collection_t *
mongoc_database_create_collection (mongoc_database_t *database,
 const char *name,
 const bson_t *options,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>name</code></p>
<dd>The name of the new collection.</dl>
<dl COMPACT>
<dt><code>options</code></p>
<dd>An optional <code>bson_t</code> for options to the <code>createDatabase</code> command.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>A location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>This function returns a newly allocated <code>mongoc_collection_t</code> upon success, <code>NULL</code> upon failure and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
