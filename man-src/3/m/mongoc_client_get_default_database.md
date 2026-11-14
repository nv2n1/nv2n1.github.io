---
title: "mongoc_client_get_default_database(3)"
name: "mongoc_client_get_default_database"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_get_default_database/"
description: "mongoc_client_get_default_database() – None"
---

<p>mongoc_client_get_default_database() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_database_t *
mongoc_client_get_default_database (mongoc_client_t *client);</pre>
<p>Get the database named in the MongoDB connection URI, or <code>NULL</code> if the URI specifies none. </p>
<p> Useful when you want to choose which database to use based only on the URI in a configuration file. </p>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>client</code></p>
<dd>A <code>mongoc_client_t</code> \&amp;.</dl>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_database_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_database_destroy/">mongoc_database_destroy</a>(3)</code> \&amp;. </p>
<h2>Example</h2>
<pre>/* default database is &quot;db_name&quot; */
mongoc_client_t *client = mongoc_client_new (&quot;mongodb://host/db_name&quot;);
mongoc_database_t *db = mongoc_client_get_default_database (client);
assert (!strcmp (&quot;db_name&quot;, mongoc_database_get_name (db)));
mongoc_database_destroy (db);
mongoc_client_destroy (client);
/* no default database */
client = mongoc_client_new (&quot;mongodb://host/&quot;);
db = mongoc_client_get_default_database (client);
assert (!db);
mongoc_client_destroy (client);</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
