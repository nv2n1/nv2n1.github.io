---
title: "mongoc_cursor_more(3)"
name: "mongoc_cursor_more"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_more/"
description: "mongoc_cursor_more() – This function shall indicate if there is more data to be read from the cursor."
---

<p>mongoc_cursor_more() &#8211; This function shall indicate if there is more data to be read from the cursor.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_cursor_more (mongoc_cursor_t *cursor);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall indicate if there is more data to be read from the cursor. </p>
<h2>Returns</h2>
<p>true if there is more data to be read from the cursor, otherwise false. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
