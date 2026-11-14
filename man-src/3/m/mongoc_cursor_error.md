---
title: "mongoc_cursor_error(3)"
name: "mongoc_cursor_error"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_error/"
description: "mongoc_cursor_error() – This function checks to see if an error has occurred while iterating the cursor."
---

<p>mongoc_cursor_error() &#8211; This function checks to see if an error has occurred while iterating the cursor.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_cursor_error (mongoc_cursor_t *cursor,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This function checks to see if an error has occurred while iterating the cursor. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>false if no error has occurred, otherwise true and error is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
