---
title: "mongoc_client_get_server_status(3)"
name: "mongoc_client_get_server_status"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_server_status/"
description: "mongoc_client_get_server_status() – None"
---

<p>mongoc_client_get_server_status() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_client_get_server_status (mongoc_client_t *client,
 mongoc_read_prefs_t *read_prefs,
 bson_t *reply,
 bson_error_t *error);</pre>
<p>Queries the server for the current server status. The result is stored in <code>reply</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd><code>reply</code> is always initialized, even in the case of failure. Always call <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> to release it.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>A location for the result <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p><code>true</code> on success, otherwise <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
