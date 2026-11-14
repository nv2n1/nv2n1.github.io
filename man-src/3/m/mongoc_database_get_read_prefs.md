---
title: "mongoc_database_get_read_prefs(3)"
name: "mongoc_database_get_read_prefs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_get_read_prefs/"
description: "mongoc_database_get_read_prefs() – None"
---

<p>mongoc_database_get_read_prefs() &#8211; None</p>
<h2>Synopsis</h2>
<pre>const mongoc_read_prefs_t *
mongoc_database_get_read_prefs (const mongoc_database_t *database);</pre>
<p>Fetches the default read preferences to use with <code>database</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A <code>mongoc_write_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
