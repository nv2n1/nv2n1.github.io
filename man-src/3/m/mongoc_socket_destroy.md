---
title: "mongoc_socket_destroy(3)"
name: "mongoc_socket_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_destroy/"
description: "mongoc_socket_destroy() – This function releases all resources associated with a mongoc_socket_t. This should be called when you are no longer using the socket."
---

<p>mongoc_socket_destroy() &#8211; This function releases all resources associated with a mongoc_socket_t. This should be called when you are no longer using the socket.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_socket_destroy (mongoc_socket_t *sock);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function releases all resources associated with a <code>mongoc_socket_t</code> \&amp;. This should be called when you are no longer using the socket. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
