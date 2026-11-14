---
title: "mongoc_read_concern_get_level(3)"
name: "mongoc_read_concern_get_level"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_concern_get_level/"
description: "mongoc_read_concern_get_level() – Returns the currently set read concern."
---

<p>mongoc_read_concern_get_level() &#8211; Returns the currently set read concern.</p>
<h2>Synopsis</h2>
<pre>const char*
mongoc_read_concern_get_level (const mongoc_read_concern_t *read_concern);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>read_concern</code></p>
<dd>A <code>mongoc_read_concern_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Returns the currently set read concern. </p>
<h2>Returns</h2>
<p>Returns the current readConcern. If none is set, returns empty string. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
