---
title: "mongoc_uri_new_for_host_port(3)"
name: "mongoc_uri_new_for_host_port"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_new_for_host_port/"
description: "mongoc_uri_new_for_host_port() – Creates a new mongoc_uri_t based on the hostname and port provided."
---

<p>mongoc_uri_new_for_host_port() &#8211; Creates a new mongoc_uri_t based on the hostname and port provided.</p>
<h2>Synopsis</h2>
<pre>mongoc_uri_t *
mongoc_uri_new_for_host_port (const char *hostname,
 uint16_t port);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>hostname</code></p>
<dd>A string containing the hostname.</dl>
<dl COMPACT>
<dt><code>port</code></p>
<dd>A uint16_t.</dl>
<h2>Description</h2>
<p>Creates a new <code>mongoc_uri_t</code> based on the hostname and port provided. </p>
<h2>Returns</h2>
<p>Returns a newly allocated <code>mongoc_uri_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_uri_destroy/">mongoc_uri_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
