---
title: "mongoc_write_concern_set_w(3)"
name: "mongoc_write_concern_set_w"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_set_w/"
description: "mongoc_write_concern_set_w() – Sets the w value for the write concern. See mongoc_write_concern_t for more information on this setting."
---

<p>mongoc_write_concern_set_w() &#8211; Sets the w value for the write concern. See mongoc_write_concern_t for more information on this setting.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_write_concern_set_w (mongoc_write_concern_t *write_concern,
 int32_t w);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>w</code></p>
<dd>A positive <code>int32_t</code> or zero.</dl>
<h2>Description</h2>
<p>Sets the <code>w</code> value for the write concern. See <code>mongoc_write_concern_t</code> for more information on this setting. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
