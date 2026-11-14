---
title: "mongoc_read_concern_set_level(3)"
name: "mongoc_read_concern_set_level"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_concern_set_level/"
description: "mongoc_read_concern_set_level() – The readConcern option allows clients to choose a level of isolation for their reads."
---

<p>mongoc_read_concern_set_level() &#8211; The readConcern option allows clients to choose a level of isolation for their reads.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_concern_set_level (mongoc_read_concern_t *read_concern,
 const char *level);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_concern</code></p>
<dd>A <code>mongoc_read_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>level</code></p>
<dd>The readConcern level to use. Should be either MONGOC_READ_CONCERN_LEVEL_LOCAL or MONGOC_READ_CONCERN_LEVEL_MAJORITY.</dl>
<h2>Description</h2>
<p>The readConcern option allows clients to choose a level of isolation for their reads. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
