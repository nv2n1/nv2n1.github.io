---
title: "mongoc_collection_find_indexes(3)"
name: "mongoc_collection_find_indexes"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_find_indexes/"
description: "mongoc_collection_find_indexes() – None"
---

<p>mongoc_collection_find_indexes() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_collection_find_indexes (mongoc_collection_t *collection,
 bson_error_t *error);</pre>
<p>Fetches a cursor containing documents, each corresponding to an index on this collection. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A cursor where each result corresponds to the server&#8217;s representation of<br />
&nbsp;<wbr>an index on this collection. If the collection does not exist on the<br />
&nbsp;<wbr>server, the cursor will be empty. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
