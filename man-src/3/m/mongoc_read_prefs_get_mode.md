---
title: "mongoc_read_prefs_get_mode(3)"
name: "mongoc_read_prefs_get_mode"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_get_mode/"
description: "mongoc_read_prefs_get_mode() – Fetches the mongoc_read_mode_t for the read preference."
---

<p>mongoc_read_prefs_get_mode() &#8211; Fetches the mongoc_read_mode_t for the read preference.</p>
<h2>Synopsis</h2>
<pre>mongoc_read_mode_t
mongoc_read_prefs_get_mode (const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the <code>mongoc_read_mode_t</code> for the read preference. </p>
<h2>Returns</h2>
<p>Returns the read preference mode. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
