---
title: "mongoc_read_prefs_t(3)"
name: "mongoc_read_prefs_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_read_prefs_t/"
description: "mongoc_read_prefs_t – A read preference abstraction"
---

<p>mongoc_read_prefs_t &#8211; A read preference abstraction</p>
<h2>Synopsis</h2>
<p><code>mongoc_read_prefs_t</code> provides an abstraction on top of the MongoDB connection read prefences. It allows for hinting to the driver which nodes in a replica set should be accessed first. </p>
<p> You can specify a read preference mode on connection objects, database objects, collection objects, or per-operation. Generally, it makes the most sense to stick with the global default, <code>MONGOC_READ_PRIMARY</code> \&amp;. All of the other modes come with caveats that won&#8217;t be covered in great detail here. </p>
<h2>Read Modes</h2>
<dl COMPACT>
<dt><code>MONGOC_READ_PRIMARY</code></p>
<dd>Default mode. All operations read from the current replica set primary.</dl>
<dl COMPACT>
<dt><code>MONGOC_READ_SECONDARY</code></p>
<dd>All operations read from among the nearest secondary members of the replica set.</dl>
<dl COMPACT>
<dt><code>MONGOC_READ_PRIMARY_PREFERRED</code></p>
<dd>In most situations, operations read from the primary but if it is unavailable, operations read from secondary members.</dl>
<dl COMPACT>
<dt><code>MONGOC_READ_SECONDARY_PREFERRED</code></p>
<dd>In most situations, operations read from among the nearest secondary members, but if no secondaries are available, operations read from the primary.</dl>
<dl COMPACT>
<dt><code>MONGOC_READ_NEAREST</code></p>
<dd>Operations read from among the nearest members of the replica set, irrespective of the member’s type.</dl>
<h2>Tag Sets</h2>
<p>Tag sets allow you to specify custom read preferences and write concerns so that your application can target operations to specific members. </p>
<p> Custom read preferences and write concerns evaluate tags sets in different ways: read preferences consider the value of a tag when selecting a member to read from. while write concerns ignore the value of a tag to when selecting a member except to consider whether or not the value is unique. </p>
<p> You can specify tag sets with the following read preference modes: </p>
<dl COMPACT>
<dt>\[bu]</p>
<dd>primaryPreferred</p>
<dt>\[bu]</p>
<dd>secondary</p>
<dt>\[bu]</p>
<dd>secondaryPreferred</p>
<dt>\[bu]</p>
<dd>nearest </p>
<p> Tags are not compatible with <code>MONGOC_READ_PRIMARY</code> and, in general, only apply when selecting a secondary member of a set for a read operation. However, the nearest read mode, when combined with a tag set will select the nearest member that matches the specified tag set, which may be a primary or secondary. </p>
<p> All interfaces use the same member selection logic to choose the member to which to direct read operations, basing the choice on read preference mode and tag sets. </p>
<p> <code></dl>
<p> </code></p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
