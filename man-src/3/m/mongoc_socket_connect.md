---
title: "mongoc_socket_connect(3)"
name: "mongoc_socket_connect"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_connect/"
description: "mongoc_socket_connect() – This function is a wrapper around the BSD socket connect() interface. It provides better portability between UNIX-like and Microsoft Windows platforms."
---

<p>mongoc_socket_connect() &#8211; This function is a wrapper around the BSD socket connect() interface. It provides better portability between UNIX-like and Microsoft Windows platforms.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_connect (mongoc_socket_t *sock,
 const struct sockaddr *addr,
 socklen_t addrlen,
 int64_t expire_at);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>addr</code></p>
<dd>A struct sockaddr.</dl>
<dl COMPACT>
<dt><code>addrlen</code></p>
<dd>A socklen_t.</dl>
<dl COMPACT>
<dt><code>expire_at</code></p>
<dd>A int64_t containing the absolute timeout using the monotonic clock.</dl>
<h2>Description</h2>
<p>This function is a wrapper around the BSD socket <code><a href="/docs/linux/man/3-connect/">connect</a>(3)</code> interface. It provides better portability between UNIX-like and Microsoft Windows platforms. </p>
<p> This function performs a socket connection but will fail if @expire_at has been reached by the monotonic clock. Keep in mind that this is an absolute timeout in milliseconds. You should add your desired timeout to <code><a href="/docs/linux/man/3-bson_get_monotonic_time/">bson_get_monotonic_time</a>(3)</code> \&amp;. </p>
<h2>Returns</h2>
<p>0 if successful, -1 on failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
