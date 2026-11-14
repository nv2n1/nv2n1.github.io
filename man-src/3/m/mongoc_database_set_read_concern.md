---
title: "mongoc_database_set_read_concern(3)"
name: "mongoc_database_set_read_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_set_read_concern/"
description: "mongoc_database_set_read_concern() – None"
---

<p>mongoc_database_set_read_concern() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_database_set_read_concern (mongoc_database_t *database,
 const mongoc_read_concern_t *read_concern);</pre>
<p>This function sets the read concern to use on operations performed with <code>database</code> \&amp;. Collections created with <code><a href="/docs/linux/man/3-mongoc_database_get_collection/">mongoc_database_get_collection</a>(3)</code> after this call will inherit this read concern. </p>
<p> The default read concern is empty: No readConcern is sent to the server unless explicitly configured. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_concern</code></p>
<dd>A <code>mongoc_read_concern_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
