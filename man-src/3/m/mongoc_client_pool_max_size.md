---
title: "mongoc_client_pool_max_size(3)"
name: "mongoc_client_pool_max_size"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_max_size/"
description: "mongoc_client_pool_max_size() – None"
---

<p>mongoc_client_pool_max_size() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_pool_min_size(mongoc_client_pool_t *pool,
 uint32_t max_pool_size);</pre>
<p>This function sets the maximum number of pooled connections available from a <code>mongoc_client_pool_t</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>max_pool_size</code></p>
<dd>The maximum number of connections which shall be available from the pool.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
