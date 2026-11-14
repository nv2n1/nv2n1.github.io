---
title: "mongoc_client_set_write_concern(3)"
name: "mongoc_client_set_write_concern"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_set_write_concern/"
description: "mongoc_client_set_write_concern() – None"
---

<p>mongoc_client_set_write_concern() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_client_set_write_concern (mongoc_client_t *client,
 const mongoc_write_concern_t *write_concern);</pre>
<p>Sets the write concern for the client. This only affects future operations, collections, and databases inheriting from <code>client</code> \&amp;. </p>
<p> The default write concern is MONGOC_WRITE_CONCERN_W_DEFAULT: the driver blocks awaiting basic acknowledgment of write operations from MongoDB. This is the correct write concern for the great majority of applications. </p>
<p> It is a programming error to call this function on a client from a <code>mongoc_client_pool_t</code> \&amp;. For pooled clients, set the write concern with the <code>MongoDB URI</code> instead. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>write_concern</code></p>
<dd>A <code>mongoc_write_concern_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
