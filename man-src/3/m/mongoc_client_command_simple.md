---
title: "mongoc_client_command_simple(3)"
name: "mongoc_client_command_simple"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_command_simple/"
description: "mongoc_client_command_simple() – None"
---

<p>mongoc_client_command_simple() &#8211; None</p>
<h2>Synopsis</h2>
<pre>
bool
mongoc_client_command_simple (mongoc_client_t           *client,
                              const char                *db_name,
                              const bson_t              *command,
                              const mongoc_read_prefs_t *read_prefs,
                              bson_t                    *reply,
                              bson_error_t              *error);
</pre>
<p> This is a simplified interface to <code><a href="/docs/linux/man/3-mongoc_client_command/">mongoc_client_command</a>(3)</code> \&amp;. It returns the first document from the result cursor into <code>reply</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dt>
<dd> <code>reply</code> is always set, and should be released with <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> \&amp;.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd> A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>db_name</code></p>
<dd> The name of the database to run the command on.</dl>
<dl COMPACT>
<dt><code>command</code></p>
<dd> A <code>bson_t</code> containing the command specification.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd> A <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd> A location for the resulting document.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd> An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p> Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p> <code>true</code> if successful; otherwise <code>false</code> and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p> This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
