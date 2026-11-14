---
title: "mongoc_write_concern_get_w(3)"
name: "mongoc_write_concern_get_w"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_get_w/"
description: "mongoc_write_concern_get_w() – Fetches the w parameter of the write concern."
---

<p>mongoc_write_concern_get_w() &#8211; Fetches the w parameter of the write concern.</p>
<h2>Synopsis</h2>
<pre>int32_t
mongoc_write_concern_get_w (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the <code>w</code> parameter of the write concern. </p>
<h2>Returns</h2>
<p>Returns an integer containing the w value. If wmajority is set, this would be MONGOC_WRITE_CONCERN_W_MAJORITY. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
