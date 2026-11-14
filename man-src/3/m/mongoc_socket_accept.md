---
title: "mongoc_socket_accept(3)"
name: "mongoc_socket_accept"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_accept/"
description: "mongoc_socket_accept() – This function is a wrapper around the BSD socket accept() interface. It allows for more portability between UNIX-like and Microsoft Windows platforms."
---

<p>mongoc_socket_accept() &#8211; This function is a wrapper around the BSD socket accept() interface. It allows for more portability between UNIX-like and Microsoft Windows platforms.</p>
<h2>Synopsis</h2>
<pre>mongoc_socket_t *
mongoc_socket_accept (mongoc_socket_t *sock,
 int64_t expire_at);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>expire_at</code></p>
<dd>An int64_t containing a timeout in milliseconds.</dl>
<h2>Description</h2>
<p>This function is a wrapper around the BSD socket <code><a href="/docs/linux/man/3-accept/">accept</a>(3)</code> interface. It allows for more portability between UNIX-like and Microsoft Windows platforms. </p>
<h2>Returns</h2>
<p>NULL upon failure to accept or timeout. A newly allocated <code>mongoc_socket_t</code> that should be released with <code><a href="/docs/linux/man/3-mongoc_socket_destroy/">mongoc_socket_destroy</a>(3)</code> on success. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
