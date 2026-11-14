---
title: "mongoc_uri_copy(3)"
name: "mongoc_uri_copy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_copy/"
description: "mongoc_uri_copy() – Copies the entire contents of a URI."
---

<p>mongoc_uri_copy() &#8211; Copies the entire contents of a URI.</p>
<h2>Synopsis</h2>
<pre>mongoc_uri_t *
mongoc_uri_copy (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Copies the entire contents of a URI. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_uri_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_uri_destroy/">mongoc_uri_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
