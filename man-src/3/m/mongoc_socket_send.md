---
title: "mongoc_socket_send(3)"
name: "mongoc_socket_send"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_send/"
description: "mongoc_socket_send() – Sends buflen bytes in buf to the destination. If a timeout expired, the number of bytes sent will be returned or -1 if no bytes were sent."
---

<p>mongoc_socket_send() &#8211; Sends buflen bytes in buf to the destination. If a timeout expired, the number of bytes sent will be returned or -1 if no bytes were sent.</p>
<h2>Synopsis</h2>
<pre>ssize_t
mongoc_socket_send (mongoc_socket_t *sock,
 const void *buf,
 size_t buflen,
 int64_t expire_at);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>buf</code></p>
<dd>A buffer to send.</dl>
<dl COMPACT>
<dt><code>buflen</code></p>
<dd>A size_t with the number of bytes in buf.</dl>
<dl COMPACT>
<dt><code>expire_at</code></p>
<dd>A int64_t with an absolute timeout for the operation or 0. The timeout is in monotonic time using microseconds. You can retrieve the current monotonic time with <code><a href="/docs/linux/man/3-bson_get_monotonic_time/">bson_get_monotonic_time</a>(3)</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sends buflen bytes in buf to the destination. If a timeout expired, the number of bytes sent will be returned or -1 if no bytes were sent. </p>
<h2>Returns</h2>
<p>-1 on failure and errno is set, or the number of bytes sent. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
