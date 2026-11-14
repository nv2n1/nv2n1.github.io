---
title: "mongoc_client_pool_pop(3)"
name: "mongoc_client_pool_pop"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_pop/"
description: "mongoc_client_pool_pop() – None"
---

<p>mongoc_client_pool_pop() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_client_t *
mongoc_client_pool_pop (mongoc_client_pool_t *pool);</pre>
<p>Retrieve a <code>mongoc_client_t</code> from the client pool, possibly blocking until one is available. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A <code>mongoc_client_t</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
