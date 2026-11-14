---
title: "mongoc_read_prefs_new(3)"
name: "mongoc_read_prefs_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_new/"
description: "mongoc_read_prefs_new() – Creates a new mongoc_read_prefs_t using the mode specified."
---

<p>mongoc_read_prefs_new() &#8211; Creates a new mongoc_read_prefs_t using the mode specified.</p>
<h2>Synopsis</h2>
<pre>mongoc_read_prefs_t *
mongoc_read_prefs_new (mongoc_read_mode_t read_mode);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_mode</code></p>
<dd>A <code>mongoc_read_mode_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Creates a new <code>mongoc_read_prefs_t</code> using the mode specified. </p>
<h2>Returns</h2>
<p>Returns a newly allocated <code>mongoc_read_prefs_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_read_prefs_destroy/">mongoc_read_prefs_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
