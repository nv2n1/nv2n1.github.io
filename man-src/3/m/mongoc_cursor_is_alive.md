---
title: "mongoc_cursor_is_alive(3)"
name: "mongoc_cursor_is_alive"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_is_alive/"
description: "mongoc_cursor_is_alive() – Checks to see if a cursor is in a state that allows for more documents to be queried."
---

<p>mongoc_cursor_is_alive() &#8211; Checks to see if a cursor is in a state that allows for more documents to be queried.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_cursor_is_alive (const mongoc_cursor_t *cursor);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Checks to see if a cursor is in a state that allows for more documents to be queried. </p>
<p> This is primarily useful with tailable cursors. </p>
<h2>Returns</h2>
<p>true if there may be more content to retrieve from the cursor. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
