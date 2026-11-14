---
title: "mongoc_write_concern_copy(3)"
name: "mongoc_write_concern_copy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_copy/"
description: "mongoc_write_concern_copy() – Performs a deep copy of write_concern."
---

<p>mongoc_write_concern_copy() &#8211; Performs a deep copy of write_concern.</p>
<h2>Synopsis</h2>
<pre>mongoc_write_concern_t *
mongoc_write_concern_copy (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Performs a deep copy of <code>write_concern</code> \&amp;. </p>
<h2>Returns</h2>
<p>Returns a newly allocated copy of <code>write_concern</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_write_concern_destroy/">mongoc_write_concern_destroy</a>(3)</code> when no longer in use. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
