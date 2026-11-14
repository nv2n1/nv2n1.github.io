---
title: "mongoc_database_get_name(3)"
name: "mongoc_database_get_name"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_get_name/"
description: "mongoc_database_get_name() – None"
---

<p>mongoc_database_get_name() &#8211; None</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_database_get_name (mongoc_database_t *database);</pre>
<p>Fetches the name of the database. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A string which should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
