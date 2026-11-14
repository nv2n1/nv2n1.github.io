---
title: "mongoc_uri_get_read_prefs(3)"
name: "mongoc_uri_get_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_read_prefs/"
description: "mongoc_uri_get_read_prefs() – Fetches a bson document containing read preference tag information from a URI. Note that this does not include the read preference mode."
---

<p>mongoc_uri_get_read_prefs() &#8211; Fetches a bson document containing read preference tag information from a URI. Note that this does not include the read preference mode.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_uri_get_read_prefs (const mongoc_uri_t *uri);</pre>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>This function is deprecated and should not be used in new code.</dl>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_uri_get_read_prefs_t/">mongoc_uri_get_read_prefs_t</a>(3)</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a bson document containing read preference tag information from a URI. Note that this does not include the read preference mode. </p>
<h2>Returns</h2>
<p>Returns a bson document that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
