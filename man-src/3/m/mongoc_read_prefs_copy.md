---
title: "mongoc_read_prefs_copy(3)"
name: "mongoc_read_prefs_copy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_copy/"
description: "mongoc_read_prefs_copy() – This function shall deep copy a read preference."
---

<p>mongoc_read_prefs_copy() &#8211; This function shall deep copy a read preference.</p>
<h2>Synopsis</h2>
<pre>mongoc_read_prefs_t *
mongoc_read_prefs_copy (const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall deep copy a read preference. </p>
<h2>Returns</h2>
<p>Returns a newly allocated read preference that should be freed with <code><a href="/docs/linux/man/3-mongoc_read_prefs_destroy/">mongoc_read_prefs_destroy</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
