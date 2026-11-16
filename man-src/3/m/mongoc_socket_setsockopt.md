---
title: "mongoc_socket_setsockopt(3)"
name: "mongoc_socket_setsockopt"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_setsockopt/"
description: "mongoc_socket_setsockopt() – This is a helper function for setsockopt()."
---

<p>mongoc_socket_setsockopt() &#8211; This is a helper function for setsockopt().</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_setsockopt (mongoc_socket_t *sock,
 int level,
 int optname,
 const void *optval,
 socklen_t optlen);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></dt>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>level</code></dt>
<dd>A sockopt level.</dd></dl>
<dl COMPACT>
<dt><code>optname</code></dt>
<dd>A sockopt name.</dd></dl>
<dl COMPACT>
<dt><code>optval</code></dt>
<dd>A the value for the sockopt.</dd></dl>
<dl COMPACT>
<dt><code>optlen</code></dt>
<dd>A socklen_t that contains the length of optval.</dd></dl>
<h2>Description</h2>
<p>This is a helper function for <code>setsockopt(3)</code> \&amp;. </p>
<h2>Returns</h2>
<p>0 on success, -1 on failure and errno is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
