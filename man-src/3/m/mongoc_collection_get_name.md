---
title: "mongoc_collection_get_name(3)"
name: "mongoc_collection_get_name"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_get_name/"
description: "mongoc_collection_get_name() – Fetches the name of collection."
---

<p>mongoc_collection_get_name() &#8211; Fetches the name of collection.</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_collection_get_name (mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the name of <code>collection</code> \&amp;. </p>
<h2>Returns</h2>
<p>A string which should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
