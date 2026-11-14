---
title: "mongoc_client_get_database_names(3)"
name: "mongoc_client_get_database_names"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_database_names/"
description: "mongoc_client_get_database_names() – None"
---

<p>mongoc_client_get_database_names() &#8211; None</p>
<h2>Synopsis</h2>
<pre>char **
mongoc_client_get_database_names (mongoc_client_t *client,
 bson_error_t *error);</pre>
<p>This function queries the MongoDB server for a list of known databases. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A <code>NULL</code> terminated vector of <code>NULL-byte</code> terminated strings. The result should be freed with <code><a href="/docs/linux/man/3-bson_strfreev/">bson_strfreev</a>(3)</code> \&amp;. </p>
<p> <code>NULL</code> is returned upon failure and <code>error</code> is set. </p>
<h2>Examples</h2>
<pre>{
 bson_error_t error;
 char **strv;
 unsigned i;
 if ((strv = mongoc_client_get_collection_names (client, &amp;error))) {
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
