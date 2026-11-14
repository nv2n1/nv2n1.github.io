---
title: "mongoc_collection_get_read_prefs(3)"
name: "mongoc_collection_get_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_get_read_prefs/"
description: "mongoc_collection_get_read_prefs() – Fetches the default read preferences to use for collection. Operations without specified read-preferences will default to this."
---

<p>mongoc_collection_get_read_prefs() &#8211; Fetches the default read preferences to use for collection. Operations without specified read-preferences will default to this.</p>
<h2>Synopsis</h2>
<pre>const mongoc_read_prefs_t *
mongoc_collection_get_read_prefs (const mongoc_collection_t *collection);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the default read preferences to use for <code>collection</code> \&amp;. Operations without specified read-preferences will default to this. </p>
<h2>Returns</h2>
<p>A <code>mongoc_read_prefs_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
