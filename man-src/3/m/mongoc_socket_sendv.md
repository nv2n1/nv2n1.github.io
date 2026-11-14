---
title: "mongoc_socket_sendv(3)"
name: "mongoc_socket_sendv"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_sendv/"
description: "mongoc_socket_sendv() – Sends a vector of buffers to the destination. This uses sendmsg() when available to perform a gathered write. If IOV_MAX is reached, a fallback will be used."
---

<p>mongoc_socket_sendv() &#8211; Sends a vector of buffers to the destination. This uses sendmsg() when available to perform a gathered write. If IOV_MAX is reached, a fallback will be used.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_socket_sendv (mongoc_socket_t *sock,
 mongoc_iovec_t *iov,
 size_t iovcnt,
 int64_t expire_at);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>iov</code></p>
<dd>A mongoc_iovec_t.</dl>
<dl COMPACT>
<dt><code>iovcnt</code></p>
<dd>A size_t containing the number of elements in iov.</dl>
<dl COMPACT>
<dt><code>expire_at</code></p>
<dd>A int64_t with absolute timeout in monotonic time. The monotonic clock is in microseconds and can be fetched using <code><a href="/docs/linux/man/3-bson_get_monotonic_time/">bson_get_monotonic_time</a>(3)</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sends a vector of buffers to the destination. This uses <code><a href="/docs/linux/man/3-sendmsg/">sendmsg</a>(3)</code> when available to perform a gathered write. If IOV_MAX is reached, a fallback will be used. </p>
<h2>Returns</h2>
<p>the number of bytes sent on success, or -1 on failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
