---
title: "mongoc_client_get_max_bson_size(3)"
name: "mongoc_client_get_max_bson_size"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_max_bson_size/"
description: "mongoc_client_get_max_bson_size() – None"
---

<p>mongoc_client_get_max_bson_size() &#8211; None</p>
<h2>Synopsis</h2>
<pre>int32_t
mongoc_client_get_max_bson_size (mongoc_client_t *client);</pre>
<p>The <code><a href="/docs/linux/man/3-mongoc_client_get_max_bson_size/">mongoc_client_get_max_bson_size</a>(3)</code> returns the maximum bson document size allowed by the cluster. Until a connection has been made, this will be the default of 16Mb. </p>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>This function is deprecated and should not be used in new code.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>The server provided max bson size, or 16Mb if no connection has been established. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
