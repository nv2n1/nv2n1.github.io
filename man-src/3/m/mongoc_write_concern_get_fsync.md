---
title: "mongoc_write_concern_get_fsync(3)"
name: "mongoc_write_concern_get_fsync"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_get_fsync/"
description: "mongoc_write_concern_get_fsync() – Fetches if an fsync should be performed before returning success on a write operation."
---

<p>mongoc_write_concern_get_fsync() &#8211; Fetches if an fsync should be performed before returning success on a write operation.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_write_concern_get_fsync (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches if an fsync should be performed before returning success on a write operation. </p>
<h2>Returns</h2>
<p>Returns true if <code>fsync</code> is set as part of the write concern. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
