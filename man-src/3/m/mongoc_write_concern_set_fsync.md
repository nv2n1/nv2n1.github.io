---
title: "mongoc_write_concern_set_fsync(3)"
name: "mongoc_write_concern_set_fsync"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_set_fsync/"
description: "mongoc_write_concern_set_fsync() – Sets if a fsync must be performed before indicating write success."
---

<p>mongoc_write_concern_set_fsync() &#8211; Sets if a fsync must be performed before indicating write success.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_write_concern_set_fsync (mongoc_write_concern_t *write_concern,
 bool fsync_);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>fsync_</code></p>
<dd>A boolean.</dl>
<h2>Description</h2>
<p>Sets if a fsync must be performed before indicating write success. </p>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>The <code>fsync</code> write concern is deprecated.</dl>
<p> Please use <code><a href="/docs/linux/man/3-mongoc_write_concern_set_journal/">mongoc_write_concern_set_journal</a>(3)</code> instead. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
