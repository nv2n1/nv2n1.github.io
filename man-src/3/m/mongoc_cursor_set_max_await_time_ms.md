---
title: "mongoc_cursor_set_max_await_time_ms(3)"
name: "mongoc_cursor_set_max_await_time_ms"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_set_max_await_time_ms/"
description: "mongoc_cursor_set_max_await_time_ms() – The maximum amount of time for the server to wait on new documents to satisfy a tailable cursor query. Only applies if the cursor is created from mongoc_coll..."
---

<p>mongoc_cursor_set_max_await_time_ms() &#8211; The maximum amount of time for the server to wait on new documents to satisfy a tailable cursor query. Only applies if the cursor is created from mongoc_collection_find with the query flags MONGOC_QUERY_TAILABLE_CURSOR and MONGOC_QUERY_AWAIT_DATA, and the server is MongoDB 3.2 or later. See the documentation for maxTimeMS and the &quot;getMore&quot; command.</p>
<h2>Synopsis</h2>
<pre>void
mongoc_cursor_set_max_await_time_ms (mongoc_cursor_t *cursor,
 uint32_t max_await_time_ms);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>cursor</code></p>
<dd>A <code>mongoc_cursor_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>max_await_time_ms</code></p>
<dd>A timeout in milliseconds.</dl>
<h2>Description</h2>
<p>The maximum amount of time for the server to wait on new documents to satisfy a tailable cursor query. Only applies if the cursor is created from <code>mongoc_collection_find</code> with the <code>query flags</code> MONGOC_QUERY_TAILABLE_CURSOR and MONGOC_QUERY_AWAIT_DATA, and the server is MongoDB 3.2 or later. See <code>the documentation for maxTimeMS and the getMore command</code> \&amp;. </p>
<p> The <code>max_await_time_ms</code> cannot be changed after the first call to <code>mongoc_cursor_next</code> \&amp;. </p>
<h2>See Also</h2>
<p><code>Tailable Cursors.</code> </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
