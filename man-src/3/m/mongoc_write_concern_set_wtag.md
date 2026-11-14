---
title: "mongoc_write_concern_set_wtag(3)"
name: "mongoc_write_concern_set_wtag"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_set_wtag/"
description: "mongoc_write_concern_set_wtag() – Sets the write tag that must be satistified for the write to indicate success. Write tags are preset write concerns configured on your MongoDB server. See mongoc_w..."
---

<p>mongoc_write_concern_set_wtag() &#8211; Sets the write tag that must be satistified for the write to indicate success. Write tags are preset write concerns configured on your MongoDB server. See mongoc_write_concern_t for more information on this setting.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_write_concern_set_wtag (mongoc_write_concern_t *write_concern,
 const char *tag);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>tag</code></p>
<dd>A string containing the write tag.</dl>
<h2>Description</h2>
<p>Sets the write tag that must be satistified for the write to indicate success. Write tags are preset write concerns configured on your MongoDB server. See <code>mongoc_write_concern_t</code> for more information on this setting. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
