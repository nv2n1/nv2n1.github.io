---
title: "mongoc_stream_tls_check_cert(3)"
name: "mongoc_stream_tls_check_cert"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_stream_tls_check_cert/"
description: "mongoc_stream_tls_check_cert() – The mongoc_stream_tls_check_cert() function shall perform a RFC-6125 certificate verification."
---

<p>mongoc_stream_tls_check_cert() &#8211; The mongoc_stream_tls_check_cert() function shall perform a RFC-6125 certificate verification.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_stream_tls_check_cert (mongoc_stream_t *stream,
 const char *host);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>stream</code></p>
<dd>A <code>mongoc_stream_tls_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>host</code></p>
<dd>A UTF-8 string holding the hostname used in socket creation. This value is what will be matched against the server provided certificate.</dl>
<p> The <code><a href="/docs/linux/man/3-mongoc_stream_tls_check_cert/">mongoc_stream_tls_check_cert</a>(3)</code> function shall perform a RFC-6125 certificate verification. </p>
<h2>Returns</h2>
<p>The <code><a href="/docs/linux/man/3-mongoc_stream_tls_check_cert/">mongoc_stream_tls_check_cert</a>(3)</code> function returns true if the certificate is valid was successful. If false, openssl errors may be set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
