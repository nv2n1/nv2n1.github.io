---
title: "mongoc_stream_socket_get_socket(3)"
name: "mongoc_stream_socket_get_socket"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_socket_get_socket/"
description: "mongoc_stream_socket_get_socket() – Retrieves the underlying mongoc_socket_t for a mongoc_stream_socket_t."
---

<p>mongoc_stream_socket_get_socket() &#8211; Retrieves the underlying mongoc_socket_t for a mongoc_stream_socket_t.</p>
<h2>Synopsis</h2>
<pre>mongoc_socket_t *
mongoc_stream_socket_get_socket (mongoc_stream_socket_t *stream);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_socket_t</code> \&amp;.</dl>
<p> Retrieves the underlying <code>mongoc_socket_t</code> for a <code>mongoc_stream_socket_t</code> \&amp;. </p>
<h2>Returns</h2>
<p>A <code>mongoc_stream_socket_t</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
