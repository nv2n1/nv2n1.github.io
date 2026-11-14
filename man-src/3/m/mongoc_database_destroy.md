---
title: "mongoc_database_destroy(3)"
name: "mongoc_database_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_destroy/"
description: "mongoc_database_destroy() – void mongoc_database_destroy (mongoc_database_t *database);"
---

<p>mongoc_database_destroy() &#8211; void mongoc_database_destroy (mongoc_database_t *database);</p>
<h2>Synopsis</h2>
<pre>void
mongoc_database_destroy (mongoc_database_t *database);</pre>
<p>Releases all resources associated with <code>database</code> , including freeing the structure. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
