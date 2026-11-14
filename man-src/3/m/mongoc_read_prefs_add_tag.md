---
title: "mongoc_read_prefs_add_tag(3)"
name: "mongoc_read_prefs_add_tag"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_add_tag/"
description: "mongoc_read_prefs_add_tag() – This function shall add a tag to a read preference."
---

<p>mongoc_read_prefs_add_tag() &#8211; This function shall add a tag to a read preference.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_prefs_add_tag (mongoc_read_prefs_t *read_prefs,
 const bson_t *tag);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>tag</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall add a tag to a read preference. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
