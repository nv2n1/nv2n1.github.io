---
title: "mongoc_socket_getnameinfo(3)"
name: "mongoc_socket_getnameinfo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_getnameinfo/"
description: "mongoc_socket_getnameinfo() – This is a helper around getting the local name of a socket. It is a wrapper around getpeername() and getnameinfo()."
---

<p>mongoc_socket_getnameinfo() &#8211; This is a helper around getting the local name of a socket. It is a wrapper around getpeername() and getnameinfo().</p>
<h2>Synopsis</h2>
<pre>char *
mongoc_socket_getnameinfo (mongoc_socket_t *sock);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This is a helper around getting the local name of a socket. It is a wrapper around <code><a href="/docs/linux/man/3-getpeername/">getpeername</a>(3)</code> and <code><a href="/docs/linux/man/3-getnameinfo/">getnameinfo</a>(3)</code> \&amp;. </p>
<h2>Returns</h2>
<p>A newly allocated string that should be freed with <code><a href="/docs/linux/man/3-bson_free/">bson_free</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
