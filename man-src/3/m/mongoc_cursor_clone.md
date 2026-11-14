---
title: "mongoc_cursor_clone(3)"
name: "mongoc_cursor_clone"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_clone/"
description: "mongoc_cursor_clone() – This function shall create a copy of a mongoc_cursor_t. The cloned cursor will be reset to the beginning of the query, and therefore the query will be re-executed on the Mon..."
---

<p>mongoc_cursor_clone() &#8211; This function shall create a copy of a mongoc_cursor_t. The cloned cursor will be reset to the beginning of the query, and therefore the query will be re-executed on the MongoDB server when mongoc_cursor_next() is called.</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_cursor_clone (const mongoc_cursor_t *cursor)
 BSON_GNUC_WARN_UNUSED_RESULT;</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function shall create a copy of a <code>mongoc_cursor_t</code> \&amp;. The cloned cursor will be reset to the beginning of the query, and therefore the query will be re-executed on the MongoDB server when <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> is called. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_cursor_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_cursor_destroy/">mongoc_cursor_destroy</a>(3)</code> when no longer in use. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Failure to handle the result of this function is a programming error.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
