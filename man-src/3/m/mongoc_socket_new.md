---
title: "mongoc_socket_new(3)"
name: "mongoc_socket_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_new/"
description: "mongoc_socket_new() – Creates a new mongoc_socket_t structure. This calls socket() underneath to create a network socket."
---

<p>mongoc_socket_new() &#8211; Creates a new mongoc_socket_t structure. This calls socket() underneath to create a network socket.</p>
<h2>Synopsis</h2>
<pre>mongoc_socket_t *
mongoc_socket_new (int domain,
 int type,
 int protocol);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>domain</code></p>
<dd>An int containing the address family such as AF_INET.</dl>
<dl COMPACT>
<dt><code>type</code></p>
<dd>An int containing the socket type such as SOCK_STREAM.</dl>
<dl COMPACT>
<dt><code>protocol</code></p>
<dd>A protocol subset, typically 0.</dl>
<h2>Description</h2>
<p>Creates a new <code>mongoc_socket_t</code> structure. This calls <code><a href="/docs/linux/man/3-socket/">socket</a>(3)</code> underneath to create a network socket. </p>
<h2>Returns</h2>
<p>A new socket if successful, otherwise <code>NULL</code> and errno is set. The result should be freed with <code><a href="/docs/linux/man/3-mongoc_socket_destroy/">mongoc_socket_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
