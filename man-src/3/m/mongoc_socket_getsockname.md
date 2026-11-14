---
title: "mongoc_socket_getsockname(3)"
name: "mongoc_socket_getsockname"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_getsockname/"
description: "mongoc_socket_getsockname() – Retrieves the socket name for sock. The result is stored in addr. addrlen should be the size of the addr when calling this."
---

<p>mongoc_socket_getsockname() &#8211; Retrieves the socket name for sock. The result is stored in addr. addrlen should be the size of the addr when calling this.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_getsockname (mongoc_socket_t *sock,
 struct sockaddr *addr,
 socklen_t *addrlen);</pre>
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
<h2>Description</h2>
<p>Retrieves the socket name for <code>sock</code> \&amp;. The result is stored in <code>addr</code> \&amp;. <code>addrlen</code> should be the size of the <code>addr</code> when calling this. </p>
<h2>Returns</h2>
<p>0 if successful, otherwise -1 and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
