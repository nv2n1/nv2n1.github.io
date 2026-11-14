---
title: "mongoc_cursor_get_max_await_time_ms(3)"
name: "mongoc_cursor_get_max_await_time_ms"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_get_max_await_time_ms/"
description: "mongoc_cursor_get_max_await_time_ms() – Retrieve the value set with mongoc_cursor_set_max_await_time_ms."
---

<p>mongoc_cursor_get_max_await_time_ms() &#8211; Retrieve the value set with mongoc_cursor_set_max_await_time_ms.</p>
<h2>Synopsis</h2>
<pre>uint32_t
mongoc_cursor_get_max_await_time_ms (mongoc_cursor_t *cursor);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<h2>Description</h2>
<p>Retrieve the value set with <code>mongoc_cursor_set_max_await_time_ms</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
