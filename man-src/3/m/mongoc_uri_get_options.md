---
title: "mongoc_uri_get_options(3)"
name: "mongoc_uri_get_options"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_get_options/"
description: "mongoc_uri_get_options() – Fetches a bson document containing all of the options provided after the ? of a URI."
---

<p>mongoc_uri_get_options() &#8211; Fetches a bson document containing all of the options provided after the ? of a URI.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_uri_get_options (const mongoc_uri_t *uri);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>uri</code></p>
<dd>A <code>mongoc_uri_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches a bson document containing all of the options provided after the <code>?</code> of a URI. </p>
<h2>Returns</h2>
<p>A <code>bson_t</code> which should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
