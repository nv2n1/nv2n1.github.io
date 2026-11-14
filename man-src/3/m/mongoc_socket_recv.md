---
title: "mongoc_socket_recv(3)"
name: "mongoc_socket_recv"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_recv/"
description: "mongoc_socket_recv() – This function performs a recv() on the underlying socket."
---

<p>mongoc_socket_recv() &#8211; This function performs a recv() on the underlying socket.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_socket_recv (mongoc_socket_t *sock,
 void *buf,
 size_t buflen,
 int flags,
 int64_t expire_at);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>buf</code></p>
<dd>A buffer to read into.</dl>
<dl COMPACT>
<dt><code>buflen</code></p>
<dd>A size_t with the number of bytes to receive.</dl>
<dl COMPACT>
<dt><code>flags</code></p>
<dd>flags for <code><a href="/docs/linux/man/3-recv/">recv</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>expire_at</code></p>
<dd>A int64_t with the time to expire in monotonic time using <code><a href="/docs/linux/man/3-bson_get_monotonic_time/">bson_get_monotonic_time</a>(3)</code> , which is in microseconds.</dl>
<h2>Description</h2>
<p>This function performs a <code><a href="/docs/linux/man/3-recv/">recv</a>(3)</code> on the underlying socket. </p>
<h2>Returns</h2>
<p>The number of bytes received on success, 0 on stream closed, and -1 if there was a failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
