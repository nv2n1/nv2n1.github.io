---
title: "mongoc_client_get_uri(3)"
name: "mongoc_client_get_uri"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_uri/"
description: "mongoc_client_get_uri() – None"
---

<p>mongoc_client_get_uri() &#8211; None</p>
<h2>Synopsis</h2>
<pre>const mongoc_uri_t *
mongoc_client_get_uri (const mongoc_client_t *client);</pre>
<p>Fetches the <code>mongoc_uri_t</code> used to create the client. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A <code>mongoc_uri_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
