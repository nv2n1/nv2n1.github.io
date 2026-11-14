---
title: "mongoc_database_set_read_prefs(3)"
name: "mongoc_database_set_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_set_read_prefs/"
description: "mongoc_database_set_read_prefs() – None"
---

<p>mongoc_database_set_read_prefs() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_database_set_read_prefs (mongoc_database_t *database,
 const mongoc_read_prefs_t *read_prefs);</pre>
<p>This function sets the default read preferences to use on operations performed with <code>database</code> \&amp;. Collections created with <code><a href="/docs/linux/man/3-mongoc_database_get_collection/">mongoc_database_get_collection</a>(3)</code> after this call will inherit these read preferences. </p>
<p> The global default is MONGOC_READ_PRIMARY: if the client is connected to a replica set it reads from the primary, otherwise it reads from the current MongoDB server. </p>
<p> Please see the MongoDB website for a description of <code>Read Preferences</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
