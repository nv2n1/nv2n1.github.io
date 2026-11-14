---
title: "mongoc_client_pool_min_size(3)"
name: "mongoc_client_pool_min_size"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_min_size/"
description: "mongoc_client_pool_min_size() – None"
---

<p>mongoc_client_pool_min_size() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_pool_min_size(mongoc_client_pool_t *pool,
 uint32_t min_pool_size);</pre>
<p>This function sets the minimum number of pooled connections kept in <code>mongoc_client_pool_t</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>min_pool_size</code></p>
<dd>The minimum number of connections which shall be kept in the pool.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
