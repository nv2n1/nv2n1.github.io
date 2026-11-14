---
title: "mongoc_read_prefs_set_tags(3)"
name: "mongoc_read_prefs_set_tags"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_set_tags/"
description: "mongoc_read_prefs_set_tags() – Sets the tags to be used for the read preference. Only mongod instances matching these tags will be suitable for handling the request."
---

<p>mongoc_read_prefs_set_tags() &#8211; Sets the tags to be used for the read preference. Only mongod instances matching these tags will be suitable for handling the request.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_prefs_set_tags (mongoc_read_prefs_t *read_prefs,
 const bson_t *tags);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>tags</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the tags to be used for the read preference. Only mongod instances matching these tags will be suitable for handling the request. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
