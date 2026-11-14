---
title: "mongoc_database_remove_all_users(3)"
name: "mongoc_database_remove_all_users"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_remove_all_users/"
description: "mongoc_database_remove_all_users() – None"
---

<p>mongoc_database_remove_all_users() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_remove_all_users (mongoc_database_t *database,
 bson_error_t *error);</pre>
<p>This function will remove all users configured to access <code>database</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. This may fail if there are socket errors or the current user is not authorized to perform the given command. </p>
<h2>Returns</h2>
<p><code>true</code> if successful, otherise <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
