---
title: "mongoc_socket_close(3)"
name: "mongoc_socket_close"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_close/"
description: "mongoc_socket_close() – This function is a wrapper around the BSD socket shutdown() interface. It provides better portability between UNIX-like and Microsoft Windows platforms."
---

<p>mongoc_socket_close() &#8211; This function is a wrapper around the BSD socket shutdown() interface. It provides better portability between UNIX-like and Microsoft Windows platforms.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_close (mongoc_socket_t *socket);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>socket</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function is a wrapper around the BSD socket <code><a href="/docs/linux/man/3-shutdown/">shutdown</a>(3)</code> interface. It provides better portability between UNIX-like and Microsoft Windows platforms. </p>
<h2>Returns</h2>
<p>0 on success, -1 on failure to close the socket. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
