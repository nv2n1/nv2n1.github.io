---
title: "mongoc_read_prefs_get_tags(3)"
name: "mongoc_read_prefs_get_tags"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_get_tags/"
description: "mongoc_read_prefs_get_tags() – Fetches any read preference tags that have been registered."
---

<p>mongoc_read_prefs_get_tags() &#8211; Fetches any read preference tags that have been registered.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_read_prefs_get_tags (const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches any read preference tags that have been registered. </p>
<h2>Returns</h2>
<p>Returns a <code>bson_t</code> that should not be modified or freed. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
