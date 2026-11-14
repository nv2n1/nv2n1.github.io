---
title: "mongoc_uri_get_ssl(3)"
name: "mongoc_uri_get_ssl"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_ssl/"
description: "mongoc_uri_get_ssl() – Fetches a boolean indicating if SSL was specified for use in the URI."
---

<p>mongoc_uri_get_ssl() &#8211; Fetches a boolean indicating if SSL was specified for use in the URI.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_uri_get_ssl (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a boolean indicating if SSL was specified for use in the URI. </p>
<h2>Returns</h2>
<p>Returns a boolean, true indicating that SSL should be used. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
