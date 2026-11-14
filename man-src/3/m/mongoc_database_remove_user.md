---
title: "mongoc_database_remove_user(3)"
name: "mongoc_database_remove_user"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_remove_user/"
description: "mongoc_database_remove_user() – None"
---

<p>mongoc_database_remove_user() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_remove_user (mongoc_database_t *database,
 const char *username,
 bson_error_t *error);</pre>
<p>This function removes the user named <code>username</code> from <code>database</code> \&amp;. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>username</code></p>
<dd>A string containing the username of the user to remove.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. This could include socket errors or others if the current user is not authorized to perform the command. </p>
<h2>Returns</h2>
<p><code>true</code> on success, otherwise <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
