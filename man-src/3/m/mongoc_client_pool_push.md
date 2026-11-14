---
title: "mongoc_client_pool_push(3)"
name: "mongoc_client_pool_push"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_push/"
description: "mongoc_client_pool_push() – None"
---

<p>mongoc_client_pool_push() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_pool_push (mongoc_client_pool_t *pool,
 mongoc_client_t *client);</pre>
<p>This function returns a <code>mongoc_client_t</code> back to the client pool. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
