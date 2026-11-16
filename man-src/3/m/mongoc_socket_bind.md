---
title: "mongoc_socket_bind(3)"
name: "mongoc_socket_bind"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_bind/"
description: "mongoc_socket_bind() – This function is a wrapper around the BSD socket bind() interface. It provides better portability between UNIX-like and Microsoft Windows platforms."
---

<p>mongoc_socket_bind() &#8211; This function is a wrapper around the BSD socket bind() interface. It provides better portability between UNIX-like and Microsoft Windows platforms.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_bind (mongoc_socket_t *sock,
 const struct sockaddr *addr,
 socklen_t addrlen);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></dt>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>addr</code></dt>
<dd>A struct sockaddr.</dd></dl>
<dl COMPACT>
<dt><code>addrlen</code></dt>
<dd>A socklen_t.</dd></dl>
<h2>Description</h2>
<p>This function is a wrapper around the BSD socket <code>bind(3)</code> interface. It provides better portability between UNIX-like and Microsoft Windows platforms. </p>
<h2>Returns</h2>
<p>0 on success, -1 on failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
