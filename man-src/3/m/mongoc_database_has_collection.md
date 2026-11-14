---
title: "mongoc_database_has_collection(3)"
name: "mongoc_database_has_collection"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_has_collection/"
description: "mongoc_database_has_collection() – None"
---

<p>mongoc_database_has_collection() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_has_collection (mongoc_database_t *database,
 const char *name,
 bson_error_t *error);</pre>
<p>This function checks to see if a collection exists on the MongoDB server within <code>database</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>name</code></p>
<dd>A string containing the name of the collection.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p><code>true</code> is returned if the collection exists. <code>false</code> is returned if the collection does not exist or an error occurred. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
