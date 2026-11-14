---
title: "mongoc_database_t(3)"
name: "mongoc_database_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_database_t/"
description: "mongoc_database_t – MongoDB Database Abstraction"
---

<p>mongoc_database_t &#8211; MongoDB Database Abstraction</p>
<h2>Synopsis</h2>
<p><code>typedef struct _mongoc_database_t mongoc_database_t;</code> </p>
<p> <code>mongoc_database_t</code> provides access to a MongoDB database. This handle is useful for actions a particular database object. It <code>is not</code> a container for <code>mongoc_collection_t</code> structures. </p>
<p> Read preferences and write concerns are inherited from the parent client. They can be overridden with <code><a href="/docs/linux/man/3-mongoc_database_set_read_prefs/">mongoc_database_set_read_prefs</a>(3)</code> and <code><a href="/docs/linux/man/3-mongoc_database_set_write_concern/">mongoc_database_set_write_concern</a>(3)</code> \&amp;. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>It is an error to call <code><a href="/docs/linux/man/3-mongoc_database_destroy/">mongoc_database_destroy</a>(3)</code> on a<br />
&nbsp;<wbr>database that has operations pending. It is required that you release <code>mongoc_cursor_t</code> structures before calling <code>mongoc_database_destroy</code> \&amp;.</dl>
<h2>Examples</h2>
<pre>#include &lt;mongoc.h&gt;
int
main (int argc,
 char *argv[])
{
 mongoc_database_t *database;
 mongoc_client_t *client;
 mongoc_init ();
 client = mongoc_client_new (&quot;mongodb://localhost/&quot;);
 database = mongoc_client_get_database (client, &quot;test&quot;);
 mongoc_database_destroy (database);
 mongoc_client_destroy (client);
 mongoc_cleanup ();
 return 0;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
