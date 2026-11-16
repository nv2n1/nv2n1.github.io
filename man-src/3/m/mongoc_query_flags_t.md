---
title: "mongoc_query_flags_t(3)"
name: "mongoc_query_flags_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_query_flags_t/"
description: "mongoc_query_flags_t – Flags for deletion operations"
---

<p>mongoc_query_flags_t &#8211; Flags for deletion operations</p>
<h2>Synopsis</h2>
<pre>typedef enum
{
 MONGOC_QUERY_NONE = 0,
 MONGOC_QUERY_TAILABLE_CURSOR = 1 &lt;&lt; 1,
 MONGOC_QUERY_SLAVE_OK = 1 &lt;&lt; 2,
 MONGOC_QUERY_OPLOG_REPLAY = 1 &lt;&lt; 3,
 MONGOC_QUERY_NO_CURSOR_TIMEOUT = 1 &lt;&lt; 4,
 MONGOC_QUERY_AWAIT_DATA = 1 &lt;&lt; 5,
 MONGOC_QUERY_EXHAUST = 1 &lt;&lt; 6,
 MONGOC_QUERY_PARTIAL = 1 &lt;&lt; 7,
} mongoc_query_flags_t;</pre>
<h2>Description</h2>
<p>These flags correspond to the MongoDB wire protocol. They may be bitwise or&#8217;d together. They may modify how a query is performed in the MongoDB server. </p>
<h2>Flag Values</h2>
<dl COMPACT>
<dt><code>MONGOC_QUERY_NONE</code></dt>
<dd>Specify no query flags.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_TAILABLE_CURSOR</code></dt>
<dd>Cursor will not be closed when the last data is retrieved. You can resume this cursor later.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_SLAVE_OK</code></dt>
<dd>Allow query of replica set secondaries.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_OPLOG_REPLAY</code></dt>
<dd>Used internally by MongoDB.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_NO_CURSOR_TIMEOUT</code></dt>
<dd>The server normally times out an idle cursor after an inactivity period (10 minutes). This prevents that.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_AWAIT_DATA</code></dt>
<dd>Use with MONGOC_QUERY_TAILABLE_CURSOR. Block rather than returning no data. After a period, time out.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_EXHAUST</code></dt>
<dd>Stream the data down full blast in multiple &quot;reply&quot; packets. Faster when you are pulling down a lot of data and you know you want to retrieve it all.</dd></dl>
<dl COMPACT>
<dt><code>MONGOC_QUERY_PARTIAL</code></dt>
<dd>Get partial results from mongos if some shards are down (instead of throwing an error).</dd></dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
