---
title: "mongoc_cursor_next(3)"
name: "mongoc_cursor_next"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_next/"
description: "mongoc_cursor_next() – This function shall iterate the underlying cursor, setting bson to the next document."
---

<p>mongoc_cursor_next() &#8211; This function shall iterate the underlying cursor, setting bson to the next document.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_cursor_next (mongoc_cursor_t *cursor,
 const bson_t **bson);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>bson</code></p>
<dd>A location for a <code>const bson_t *</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall iterate the underlying cursor, setting <code>bson</code> to the next document. </p>
<p> This function is a blocking function. </p>
<h2>Returns</h2>
<p>This function returns true if a valid bson document was read from the cursor. Otherwise, false if there was an error or the cursor was exhausted. </p>
<p> Errors can be determined with the <code><a href="/docs/linux/man/3-mongoc_cursor_error/">mongoc_cursor_error</a>(3)</code> function. </p>
<h2>Lifecycle</h2>
<p>The bson objects set in this function are ephemeral and good until the next call. This means that you must copy the returned bson if you wish to retain it beyond the lifetime of a single call to <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
