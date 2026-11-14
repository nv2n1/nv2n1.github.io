---
title: "mongoc_client_get_database(3)"
name: "mongoc_client_get_database"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_database/"
description: "mongoc_client_get_database() – None"
---

<p>mongoc_client_get_database() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
mongoc_database_t *
mongoc_client_get_database (mongoc_client_t *client,
                            const char      *name);
</pre>
<p> Get a newly allocated <code>mongoc_database_t</code> for the database named <code>name</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> Databases are automatically created on the MongoDB server upon insertion of the first document into a collection. There is no need to create a database manually.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd> A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>name</code></p>
<dd> The name of the database.</dl>
<h2>Returns</h2>
<p> A newly allocated <code>mongoc_database_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_database_destroy/">mongoc_database_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
