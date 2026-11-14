---
title: "mongoc_read_prefs_destroy(3)"
name: "mongoc_read_prefs_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_destroy/"
description: "mongoc_read_prefs_destroy() – Frees a read preference and all associated resources."
---

<p>mongoc_read_prefs_destroy() &#8211; Frees a read preference and all associated resources.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_read_prefs_destroy (mongoc_read_prefs_t *read_prefs);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Frees a read preference and all associated resources. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
