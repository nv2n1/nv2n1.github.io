---
title: "mongoc_uri_get_write_concern(3)"
name: "mongoc_uri_get_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_write_concern/"
description: "mongoc_uri_get_write_concern() – Fetches a write concern that is owned by the URI instance. This write concern is configured based on URI parameters."
---

<p>mongoc_uri_get_write_concern() &#8211; Fetches a write concern that is owned by the URI instance. This write concern is configured based on URI parameters.</p>
<h2>Synopsis</h2>
<pre>const mongoc_write_concern_t *
mongoc_uri_get_write_concern (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a write concern that is owned by the URI instance. This write concern is configured based on URI parameters. </p>
<h2>Returns</h2>
<p>Returns a <code>mongoc_write_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
