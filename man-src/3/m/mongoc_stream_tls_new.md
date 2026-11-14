---
title: "mongoc_stream_tls_new(3)"
name: "mongoc_stream_tls_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_tls_new/"
description: "mongoc_stream_tls_new() – Creates a new mongoc_stream_tls_t using the parameters supplied."
---

<p>mongoc_stream_tls_new() &#8211; Creates a new mongoc_stream_tls_t using the parameters supplied.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_tls_new (mongoc_stream_t *base_stream,
 mongoc_ssl_opt_t *opt,
 int client);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>base_stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>opt</code></p>
<dd>A <code>mongoc_ssl_opt_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>client</code></p>
<dd>1 for client, 0 for server TLS.</dl>
<p> Creates a new <code>mongoc_stream_tls_t</code> using the parameters supplied. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_stream_tls_t</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
