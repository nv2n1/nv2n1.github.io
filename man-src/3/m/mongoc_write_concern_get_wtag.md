---
title: "mongoc_write_concern_get_wtag(3)"
name: "mongoc_write_concern_get_wtag"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_get_wtag/"
description: "mongoc_write_concern_get_wtag() – A string containing the wtag setting if it has been set. Otherwise returns NULL."
---

<p>mongoc_write_concern_get_wtag() &#8211; A string containing the wtag setting if it has been set. Otherwise returns NULL.</p>
<h2>Synopsis</h2>
<pre>const char *
mongoc_write_concern_get_wtag (const mongoc_write_concern_t *write_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>A string containing the wtag setting if it has been set. Otherwise returns <code>NULL</code> \&amp;. </p>
<h2>Returns</h2>
<p>Returns a string which should not be modified or freed, or <code>NULL</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
