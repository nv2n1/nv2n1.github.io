---
title: "mongoc_write_concern_get_wtimeout(3)"
name: "mongoc_write_concern_get_wtimeout"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_get_wtimeout/"
description: "mongoc_write_concern_get_wtimeout() – Fetches the write timeout to use as part of the write concern. If the write has not completed before this timeout, an error will be returned."
---

<p>mongoc_write_concern_get_wtimeout() &#8211; Fetches the write timeout to use as part of the write concern. If the write has not completed before this timeout, an error will be returned.</p>
<h2>Synopsis</h2>
<pre>int32_t
mongoc_write_concern_get_wtimeout (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the write timeout to use as part of the write concern. If the write has not completed before this timeout, an error will be returned. </p>
<p> A value of 0 indicates no write timeout. </p>
<h2>Returns</h2>
<p>Returns an 32-bit signed integer containing the timeout. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
