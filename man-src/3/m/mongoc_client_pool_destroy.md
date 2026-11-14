---
title: "mongoc_client_pool_destroy(3)"
name: "mongoc_client_pool_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_destroy/"
description: "mongoc_client_pool_destroy() – None"
---

<p>mongoc_client_pool_destroy() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_pool_destroy (mongoc_client_pool_t *pool);</pre>
<p>Release all resources associated with <code>pool</code> , including freeing the structure. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
