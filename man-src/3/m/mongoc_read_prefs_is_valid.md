---
title: "mongoc_read_prefs_is_valid(3)"
name: "mongoc_read_prefs_is_valid"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_is_valid/"
description: "mongoc_read_prefs_is_valid() – Performs a consistency check of read_prefs to ensure it makes sense and can be satisfied."
---

<p>mongoc_read_prefs_is_valid() &#8211; Performs a consistency check of read_prefs to ensure it makes sense and can be satisfied.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_read_prefs_is_valid (const mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Performs a consistency check of <code>read_prefs</code> to ensure it makes sense and can be satisfied. </p>
<p> This only performs local consistency checks. </p>
<h2>Returns</h2>
<p>Returns true if the read pref is valid. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
