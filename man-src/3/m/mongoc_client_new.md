---
title: "mongoc_client_new(3)"
name: "mongoc_client_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_new/"
description: "mongoc_client_new() – None"
---

<p>mongoc_client_new() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_client_t *
mongoc_client_new (const char *uri_string);</pre>
<p>Creates a new <code>mongoc_client_t</code> using the URI string provided. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri_string</code></p>
<dd>A string containing the MongoDB connection URI.</dl>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_client_t</code> if the URI parsed successfully, otherwise <code>NULL</code> \&amp;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mongoc_client_new_from_uri/">mongoc_client_new_from_uri</a>(3)</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
