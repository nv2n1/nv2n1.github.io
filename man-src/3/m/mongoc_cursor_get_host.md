---
title: "mongoc_cursor_get_host(3)"
name: "mongoc_cursor_get_host"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_get_host/"
description: "mongoc_cursor_get_host() – Fetches the MongoDB host that the cursor is communicating with in the host out parameter."
---

<p>mongoc_cursor_get_host() &#8211; Fetches the MongoDB host that the cursor is communicating with in the host out parameter.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_cursor_get_host (mongoc_cursor_t *cursor,
 mongoc_host_list_t *host);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>host</code></p>
<dd>A <code>mongoc_host_list_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Fetches the MongoDB host that the cursor is communicating with in the <code>host</code> out parameter. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
