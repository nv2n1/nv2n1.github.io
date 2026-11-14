---
title: "mongoc_socket_listen(3)"
name: "mongoc_socket_listen"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_listen/"
description: "mongoc_socket_listen() – This function is similar to the BSD sockets listen() function. It is meant for socket servers."
---

<p>mongoc_socket_listen() &#8211; This function is similar to the BSD sockets listen() function. It is meant for socket servers.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_listen (mongoc_socket_t *sock,
 unsigned int backlog);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>backlog</code></p>
<dd>An int containing max backlog size.</dl>
<h2>Description</h2>
<p>This function is similar to the BSD sockets <code><a href="/docs/linux/man/3-listen/">listen</a>(3)</code> function. It is meant for socket servers. </p>
<h2>Returns</h2>
<p>0 on success, -1 on failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
