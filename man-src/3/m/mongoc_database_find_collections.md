---
title: "mongoc_database_find_collections(3)"
name: "mongoc_database_find_collections"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_find_collections/"
description: "mongoc_database_find_collections() – None"
---

<p>mongoc_database_find_collections() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_cursor_t *
mongoc_database_find_collections (mongoc_database_t * database,
 const bson_t * filter,
 bson_error_t * error);</pre>
<p>Fetches a cursor containing documents, each corresponding to a collection on this database. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>filter</code></p>
<dd>A matcher used by the server to filter the returned collections. May be <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A cursor where each result corresponds to the server&#8217;s representation of<br />
&nbsp;<wbr>a collection in this database. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
