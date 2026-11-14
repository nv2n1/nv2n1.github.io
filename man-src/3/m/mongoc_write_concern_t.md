---
title: "mongoc_write_concern_t(3)"
name: "mongoc_write_concern_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_write_concern_t/"
description: "mongoc_write_concern_t – Write Concern abstraction"
---

<p>mongoc_write_concern_t &#8211; Write Concern abstraction</p>
<h2>Synopsis</h2>
<p><code>mongoc_write_concern_t</code> tells the driver what level of acknowledgment to await from the server. The default, MONGOC_WRITE_CONCERN_W_DEFAULT, is right for the great majority of applications. </p>
<p> You can specify a write concern on connection objects, database objects, collection objects, or per-operation. </p>
<p> See <code>Write Concern</code> on the MongoDB website for more information. </p>
<h2>Write Concern Levels</h2>
<dl COMPACT>
<dt><code>MONGOC_WRITE_CONCERN_W_DEFAULT (1)</code></p>
<dd>By default, writes block awaiting acknowledgment from MongoDB. Acknowledged write concern allows clients to catch network, duplicate key, and other errors.</dl>
<dl COMPACT>
<dt><code>MONGOC_WRITE_CONCERN_W_UNACKNOWLEDGED (0)</code></p>
<dd>With this write concern, MongoDB does not acknowledge the receipt of write operation. Unacknowledged is similar to errors ignored; however, mongoc attempts to receive and handle network errors when possible.</dl>
<dl COMPACT>
<dt><code>MONGOC_WRITE_CONCERN_W_MAJORITY (majority)</code></p>
<dd>Block until a write has been propagated to a majority of the nodes in the replica set.</dl>
<dl COMPACT>
<dt><code>n</code></p>
<dd>Block until a write has been propagated to at least <code>n</code> nodes in the replica set.</dl>
<dl COMPACT>
<dt><code>journal</code></p>
<dd>Block until the node receiving the write has committed the journal.</dl>
<h2>Deprecation</h2>
<p>The write concern <code>MONGOC_WRITE_CONCERN_W_ERRORS_IGNORED</code> (value -1) is a deprecated synonym for <code>MONGOC_WRITE_CONCERN_W_UNACKNOWLEDGED</code> (value 0), and will be removed in the next major release. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
