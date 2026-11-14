---
title: "mongoc_database_get_collection_names(3)"
name: "mongoc_database_get_collection_names"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_get_collection_names/"
description: "mongoc_database_get_collection_names() – None"
---

<p>mongoc_database_get_collection_names() &#8211; None</p>
<h2>Synopsis</h2>
<pre>char **
mongoc_database_get_collection_names (mongoc_database_t *database,
 bson_error_t *error);</pre>
<p>Fetches a <code>NULL</code> terminated array of <code>NULL-byte</code> terminated <code>char*</code> strings containing the names of all of the collections in <code>database</code> \&amp;. </p>
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
<p>A <code>NULL</code> terminated array of <code>NULL</code> terminated <code>char*</code> strings that should be freed with <code><a href="/docs/linux/man/3-bson_strfreev/">bson_strfreev</a>(3)</code> \&amp;. Upon failure, <code>NULL</code> is returned and <code>error</code> is set. </p>
<h2>Examples</h2>
<pre>{
 bson_error_t error;
 char **strv;
 unsigned i;
 if ((strv = mongoc_database_get_collection_names (database, &amp;error))) {
 for (i = 0; strv [i]; i++)
 printf (&quot;%s
&quot;, strv [i]);
 bson_strfreev (strv);
 } else {
 fprintf (stderr, &quot;Command failed: %s
&quot;, error.message);
 }
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
