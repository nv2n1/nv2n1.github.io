---
title: "mongoc_database_get_write_concern(3)"
name: "mongoc_database_get_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_get_write_concern/"
description: "mongoc_database_get_write_concern() – None"
---

<p>mongoc_database_get_write_concern() &#8211; None</p>
<h2>Synopsis</h2>
<pre>const mongoc_write_concern_t *
mongoc_database_get_write_concern (const mongoc_database_t *database);</pre>
<p>This function retrieves the default <code>mongoc_write_concern_t</code> to use with <code>database</code> as configured by the client. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A <code>mongoc_write_concern_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
