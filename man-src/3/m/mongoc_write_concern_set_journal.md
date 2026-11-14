---
title: "mongoc_write_concern_set_journal(3)"
name: "mongoc_write_concern_set_journal"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_set_journal/"
description: "mongoc_write_concern_set_journal() – Sets if the write must have been journaled before indicating success."
---

<p>mongoc_write_concern_set_journal() &#8211; Sets if the write must have been journaled before indicating success.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_write_concern_set_journal (mongoc_write_concern_t *write_concern,
 bool journal);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>journal</code></p>
<dd>A boolean.</dl>
<h2>Description</h2>
<p>Sets if the write must have been journaled before indicating success. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
