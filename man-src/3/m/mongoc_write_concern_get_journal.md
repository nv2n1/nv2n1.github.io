---
title: "mongoc_write_concern_get_journal(3)"
name: "mongoc_write_concern_get_journal"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_get_journal/"
description: "mongoc_write_concern_get_journal() – Fetches if the write should be journaled before indicating success."
---

<p>mongoc_write_concern_get_journal() &#8211; Fetches if the write should be journaled before indicating success.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_write_concern_get_journal (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches if the write should be journaled before indicating success. </p>
<h2>Returns</h2>
<p>Returns true if the write should be journaled. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
