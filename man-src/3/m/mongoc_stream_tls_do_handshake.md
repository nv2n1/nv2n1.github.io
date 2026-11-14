---
title: "mongoc_stream_tls_do_handshake(3)"
name: "mongoc_stream_tls_do_handshake"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_tls_do_handshake/"
description: "mongoc_stream_tls_do_handshake() – This function shall perform an SSL handshake on the underlying stream."
---

<p>mongoc_stream_tls_do_handshake() &#8211; This function shall perform an SSL handshake on the underlying stream.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_stream_tls_do_handshake (mongoc_stream_t *stream,
 int32_t timeout_msec);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_tls_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>timeout_msec</code></p>
<dd>A timeout, in milliseconds, for the handshake.</dl>
<p> This function shall perform an SSL handshake on the underlying stream. </p>
<h2>Returns</h2>
<p>The <code><a href="/docs/linux/man/3-mongoc_stream_tls_do_handshake/">mongoc_stream_tls_do_handshake</a>(3)</code> function returns true if the handshake was successful. If false, errno or openssl errors may be set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
