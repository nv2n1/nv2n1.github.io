---
title: "mongoc_collection_set_read_prefs(3)"
name: "mongoc_collection_set_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_set_read_prefs/"
description: "mongoc_collection_set_read_prefs() – Sets the default read preferences to use for operations on collection not specifying a read preference."
---

<p>mongoc_collection_set_read_prefs() &#8211; Sets the default read preferences to use for operations on collection not specifying a read preference.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_collection_set_read_prefs (mongoc_collection_t *collection,
 const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the default read preferences to use for operations on <code>collection</code> not specifying a read preference. </p>
<p> The global default is MONGOC_READ_PRIMARY: if the client is connected to a replica set it reads from the primary, otherwise it reads from the current MongoDB server. </p>
<p> Please see the MongoDB website for a description of <code>Read Preferences</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
