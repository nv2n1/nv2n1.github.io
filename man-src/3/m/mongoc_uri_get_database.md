---
title: "mongoc_uri_get_database(3)"
name: "mongoc_uri_get_database"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_database/"
description: "mongoc_uri_get_database() – Fetches the database portion of an URI if provided. This is the portion after the / but before the ?."
---

<p>mongoc_uri_get_database() &#8211; Fetches the database portion of an URI if provided. This is the portion after the / but before the ?.</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_uri_get_database (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the database portion of an URI if provided. This is the portion after the <code>/</code> but before the <code>?</code> \&amp;. </p>
<h2>Returns</h2>
<p>A string which should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
