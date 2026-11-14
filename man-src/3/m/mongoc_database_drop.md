---
title: "mongoc_database_drop(3)"
name: "mongoc_database_drop"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_drop/"
description: "mongoc_database_drop() – bool mongoc_database_drop (mongoc_database_t *database, bson_error_t *error);"
---

<p>mongoc_database_drop() &#8211; bool mongoc_database_drop (mongoc_database_t *database,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bson_error_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*error);</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_drop (mongoc_database_t *database,
 bson_error_t *error);</pre>
<p>This function attempts to drop a database on the MongoDB server. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p><code>true</code> if successful, otherwise <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
