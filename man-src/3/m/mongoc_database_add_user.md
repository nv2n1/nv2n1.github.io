---
title: "mongoc_database_add_user(3)"
name: "mongoc_database_add_user"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_add_user/"
description: "mongoc_database_add_user() – This function shall create a new user with access to database."
---

<p>mongoc_database_add_user() &#8211; This function shall create a new user with access to database.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_add_user (mongoc_database_t *database,
 const char *username,
 const char *password,
 const bson_t *roles,
 const bson_t *custom_data,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></dt>
<dd>A <code>mongoc_database_t</code> \&amp;.</dd></dl>
<dl COMPACT>
<dt><code>username</code></dt>
<dd>The name of the user.</dd></dl>
<dl COMPACT>
<dt><code>password</code></dt>
<dd>The cleartext password for the user.</dd></dl>
<dl COMPACT>
<dt><code>roles</code></dt>
<dd>An optional <code>bson_t</code> for roles.</dd></dl>
<dl COMPACT>
<dt><code>custom_data</code></dt>
<dd>A optional <code>bson_t</code> for extra data.</dd></dl>
<dl COMPACT>
<dt><code>error</code></dt>
<dd>A location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dd></dl>
<p> This function shall create a new user with access to <code>database</code> \&amp;. </p>
<p> This function handles the difference between MongoDB <code>2.4</code> and <code>2.6</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are returned through the <code>error</code> parameter and can include socket or other server side failures. </p>
<h2>Returns</h2>
<p>This function shall return <code>true</code> if the user was successfully added. In the event of an error, it returns <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
