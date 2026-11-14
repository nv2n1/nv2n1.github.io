---
title: "mongoc_database_command_simple(3)"
name: "mongoc_database_command_simple"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_command_simple/"
description: "mongoc_database_command_simple() – This is a simplified interface to mongoc_database_command() that returns the first result document."
---

<p>mongoc_database_command_simple() &#8211; This is a simplified interface to mongoc_database_command() that returns the first result document.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_database_command_simple (mongoc_database_t *database,
 const bson_t *command,
 const mongoc_read_prefs_t *read_prefs,
 bson_t *reply,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>database</code></p>
<dd>A <code>mongoc_database_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>command</code></p>
<dd>A <code>bson_t</code> containing the command.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>An optional <code>mongoc_read_prefs_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>A location to store the commands first result document.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<p> This is a simplified interface to <code><a href="/docs/linux/man/3-mongoc_database_command/">mongoc_database_command</a>(3)</code> that returns the first result document. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>This function will <code>always</code> initialize <code>reply</code> \&amp;. The caller should always call <code><a href="/docs/linux/man/3-bson_destroy/">bson_destroy</a>(3)</code> with <code>reply</code> as an argument.</dl>
<h2>Errors</h2>
<p>Errors are propagated through the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p><code>true</code> on success, <code>false</code> on failure and <code>error</code> is set. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
