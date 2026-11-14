---
title: "mongoc_stream_setsockopt(3)"
name: "mongoc_stream_setsockopt"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_setsockopt/"
description: "mongoc_stream_setsockopt() – This function is a wrapper around setsockopt() for streams that wrap sockets."
---

<p>mongoc_stream_setsockopt() &#8211; This function is a wrapper around setsockopt() for streams that wrap sockets.</p>
<h2>Synopsis</h2>
<pre>int
mongoc_stream_setsockopt (mongoc_stream_t *stream,
 int level,
 int optname,
 void *optval,
 socklen_t optlen);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>level</code></p>
<dd>The level to pass to <code><a href="/docs/linux/man/3-setsockopt/">setsockopt</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>optname</code></p>
<dd>The optname to pass to <code><a href="/docs/linux/man/3-setsockopt/">setsockopt</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>optval</code></p>
<dd>The optval to pass to <code><a href="/docs/linux/man/3-setsockopt/">setsockopt</a>(3)</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>optlen</code></p>
<dd>The optlen to pass to <code><a href="/docs/linux/man/3-setsockopt/">setsockopt</a>(3)</code> \&amp;.</dl>
<p> This function is a wrapper around <code><a href="/docs/linux/man/3-setsockopt/">setsockopt</a>(3)</code> for streams that wrap sockets. </p>
<h2>Returns</h2>
<p><code>0</code> on success, otherwise <code>-1</code> and <code>errno</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
