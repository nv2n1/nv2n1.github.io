---
title: "mongoc_socket_errno(3)"
name: "mongoc_socket_errno"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_errno/"
description: "mongoc_socket_errno() – This function returns the currently captured errno for a socket. This may be useful to check was the last errno was after another function call has been made that clears the..."
---

<p>mongoc_socket_errno() &#8211; This function returns the currently captured errno for a socket. This may be useful to check was the last errno was after another function call has been made that clears the threads errno variable.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_socket_errno (mongoc_socket_t *sock);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>sock</code></p>
<dd>A <code>mongoc_socket_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function returns the currently captured <code>errno</code> for a socket. This may be useful to check was the last errno was after another function call has been made that clears the threads errno variable. </p>
<h2>Returns</h2>
<p>0 if there is no error, otherwise a specific errno. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
