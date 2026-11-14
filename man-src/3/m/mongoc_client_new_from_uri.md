---
title: "mongoc_client_new_from_uri(3)"
name: "mongoc_client_new_from_uri"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_new_from_uri/"
description: "mongoc_client_new_from_uri() – None"
---

<p>mongoc_client_new_from_uri() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_client_t *
mongoc_client_new_from_uri (const mongoc_uri_t *uri);</pre>
<p>Creates a new <code>mongoc_client_t</code> using the <code>mongoc_uri_t</code> provided. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_client_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_client_destroy/">mongoc_client_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
