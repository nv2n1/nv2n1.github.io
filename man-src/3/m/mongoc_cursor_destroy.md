---
title: "mongoc_cursor_destroy(3)"
name: "mongoc_cursor_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_destroy/"
description: "mongoc_cursor_destroy() – Frees a mongoc_cursor_t and releases all associated resources. If a server-side cursor has been allocated, it will be released as well."
---

<p>mongoc_cursor_destroy() &#8211; Frees a mongoc_cursor_t and releases all associated resources. If a server-side cursor has been allocated, it will be released as well.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_cursor_destroy (mongoc_cursor_t *cursor);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Frees a <code>mongoc_cursor_t</code> and releases all associated resources. If a server-side cursor has been allocated, it will be released as well. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
