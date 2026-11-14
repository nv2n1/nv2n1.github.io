---
title: "mongoc_read_prefs_set_mode(3)"
name: "mongoc_read_prefs_set_mode"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_set_mode/"
description: "mongoc_read_prefs_set_mode() – Sets the read preference mode. See the MongoDB website for more information on Read Preferences."
---

<p>mongoc_read_prefs_set_mode() &#8211; Sets the read preference mode. See the MongoDB website for more information on Read Preferences.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_prefs_set_mode (mongoc_read_prefs_t *read_prefs,
 mongoc_read_mode_t mode);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>mode</code></p>
<dd>A <code>mongoc_read_mode_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Sets the read preference mode. See the MongoDB website for more information on <code>Read Preferences</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
