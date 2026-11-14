---
title: "mongoc_cursor_current(3)"
name: "mongoc_cursor_current"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_current/"
description: "mongoc_cursor_current() – Fetches the cursors current document or NULL if there has been an error."
---

<p>mongoc_cursor_current() &#8211; Fetches the cursors current document or NULL if there has been an error.</p>
<h2>Synopsis</h2>
<pre>const bson_t *
mongoc_cursor_current (const mongoc_cursor_t *cursor);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the cursors current document or <code>NULL</code> if there has been an error. </p>
<h2>Returns</h2>
<p>A <code>bson_t</code> that should not be modified or freed or <code>NULL</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
