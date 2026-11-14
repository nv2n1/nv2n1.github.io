---
title: "mongoc_client_pool_set_ssl_opts(3)"
name: "mongoc_client_pool_set_ssl_opts"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_set_ssl_opts/"
description: "mongoc_client_pool_set_ssl_opts() – None"
---

<p>mongoc_client_pool_set_ssl_opts() &#8211; None</p>
<h2>Synopsis</h2>
<pre>#ifdef MONGOC_ENABLE_SSL
void
mongoc_client_pool_set_ssl_opts (mongoc_client_pool_t *pool,
 const mongoc_ssl_opt_t *opts);
#endif</pre>
<p>This function is identical to <code><a href="/docs/linux/man/3-mongoc_client_set_ssl_opts/">mongoc_client_set_ssl_opts</a>(3)</code> except for client pools. It ensures that all clients retrieved from <code><a href="/docs/linux/man/3-mongoc_client_pool_pop/">mongoc_client_pool_pop</a>(3)</code> or <code><a href="/docs/linux/man/3-mongoc_client_pool_try_pop/">mongoc_client_pool_try_pop</a>(3)</code> are configured with the same SSL settings. </p>
<p> It is a programming error to call this function after retrieving a client from the client pool. </p>
<p> Beginning in version 1.2.0, once a pool has any SSL options set, all connections use SSL, even if &quot;ssl=true&quot; is omitted from the MongoDB URI. Before, SSL options were ignored unless &quot;ssl=true&quot; was included in the URI. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>pool</code></p>
<dd>A <code>mongoc_client_pool_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_ssl_opt_t</code> that will not be modified.</dl>
<h2>Availability</h2>
<p>This feature requires that the MongoDB C driver was compiled with <code>&#8211;enable-ssl</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
