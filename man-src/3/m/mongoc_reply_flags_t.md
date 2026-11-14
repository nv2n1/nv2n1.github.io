---
title: "mongoc_reply_flags_t(3)"
name: "mongoc_reply_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_reply_flags_t/"
description: "mongoc_reply_flags_t – Flags for deletion operations"
---

<p>mongoc_reply_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_REPLY_NONE = 0,
 MONGOC_REPLY_CURSOR_NOT_FOUND = 1 &lt;&lt; 0,
 MONGOC_REPLY_QUERY_FAILURE = 1 &lt;&lt; 1,
 MONGOC_REPLY_SHARD_CONFIG_STALE = 1 &lt;&lt; 2,
 MONGOC_REPLY_AWAIT_CAPABLE = 1 &lt;&lt; 3,
} mongoc_reply_flags_t;</pre>
<h2>Description</h2>
<p>These flags correspond to the wire protocol. They may be bitwise or&#8217;d together. </p>
<h2>Flag Values</h2>
<dl COMPACT>
<dt><code>MONGOC_REPLY_NONE</code></p>
<dd>No flags set.</dl>
<dl COMPACT>
<dt><code>MONGOC_REPLY_CURSOR_NOT_FOUND</code></p>
<dd>No matching cursor was found on the server.</dl>
<dl COMPACT>
<dt><code>MONGOC_REPLY_QUERY_FAILURE</code></p>
<dd>The query failed or was invalid. Error document has been provided.</dl>
<dl COMPACT>
<dt><code>MONGOC_REPLY_SHARD_CONFIG_STALE</code></p>
<dd>Shard config is stale.</dl>
<dl COMPACT>
<dt><code>MONGOC_REPLY_AWAIT_CAPABLE</code></p>
<dd>If the returned cursor is capable of MONGOC_QUERY_AWAIT_DATA.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
