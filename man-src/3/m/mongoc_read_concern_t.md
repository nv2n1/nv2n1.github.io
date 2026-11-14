---
title: "mongoc_read_concern_t(3)"
name: "mongoc_read_concern_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_concern_t/"
description: "mongoc_read_concern_t – Read Concern abstraction"
---

<p>mongoc_read_concern_t &#8211; Read Concern abstraction</p>
<h2>Synopsis</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in MongoDB 3.2 and mongoc 1.3.0</dl>
<p> The <code>mongoc_read_concern_t</code> allows clients to choose a level of isolation for their reads. The default, MONGOC_READ_CONCERN_LEVEL_LOCAL, is right for the great majority of applications. </p>
<p> You can specify a read concern on connection objects, database objects, or collection objects. </p>
<p> See <code>readConcern</code> on the MongoDB website for more information. </p>
<p> Read Concern is only sent to MongoDB when it has explicitly been set by <code>mongoc_read_concern_set_level</code> to anything other then empty string. </p>
<h2>Read Concern Levels</h2>
<dl COMPACT>
<dt><code>MONGOC_READ_CONCERN_LEVEL_LOCAL (&quot;local&quot;)</code></p>
<dd>Default. The query will return the node’s most recent copy of data. Provides no guarantee that the data has been written to a majority of the nodes.</dl>
<dl COMPACT>
<dt><code>MONGOC_READ_CONCERN_LEVEL_MAJORITY (&quot;majority&quot;)</code></p>
<dd>The query will return the node’s most recent copy of the data confirmed as having been written to a majority of the nodes.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
