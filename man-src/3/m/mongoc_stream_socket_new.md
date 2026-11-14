---
title: "mongoc_stream_socket_new(3)"
name: "mongoc_stream_socket_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_socket_new/"
description: "mongoc_stream_socket_new() – Creates a new mongoc_stream_socket_t using the mongoc_socket_t provided."
---

<p>mongoc_stream_socket_new() &#8211; Creates a new mongoc_stream_socket_t using the mongoc_socket_t provided.</p>
<h2>Synopsis</h2>
<pre>mongoc_stream_t *
mongoc_stream_socket_new (mongoc_socket_t *socket);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>socket</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<p> Creates a new <code>mongoc_stream_socket_t</code> using the <code>mongoc_socket_t</code> provided. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>This function transfers ownership of <code>socket</code> to the newly allocated stream.</dl>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_stream_socket_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_stream_destroy/">mongoc_stream_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
