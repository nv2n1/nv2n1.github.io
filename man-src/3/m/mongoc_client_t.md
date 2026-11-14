---
title: "mongoc_client_t(3)"
name: "mongoc_client_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_t/"
description: "mongoc_client_t – MongoDB Connection Abstraction"
---

<p>mongoc_client_t &#8211; MongoDB Connection Abstraction</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_client_t mongoc_client_t;
 
typedef mongoc_stream_t *
(*mongoc_stream_initiator_t) (const mongoc_uri_t *uri,
 const mongoc_host_list_t *host,
 void *user_data,
 bson_error_t *error);</pre>
<p><code>mongoc_client_t</code> is an opaque type that provides access to a MongoDB node, replica-set, or sharded-cluster. It maintains management of underlying sockets and routing to individual nodes based on <code>mongoc_read_prefs_t</code> or <code>mongoc_write_concern_t</code> \&amp;. </p>
<h2>Streams</h2>
<p>The underlying transport for a given client can be customized, wrapped or replaced by any implementation that fulfills <code>mongoc_stream_t</code> \&amp;. A custom transport can be set with <code><a href="/docs/linux/man/3-mongoc_client_set_stream_initiator/">mongoc_client_set_stream_initiator</a>(3)</code> \&amp;. </p>
<h2>Thread Safety</h2>
<p><code>mongoc_client_t</code> is <code>NOT</code> thread-safe and should only be used from one thread at a time. When used in multi-threaded scenarios, it is recommended that you use the thread-safe <code>mongoc_client_pool_t</code> to retrieve a <code>mongoc_client_t</code> for your thread. </p>
<h2>Lifecycle</h2>
<p>It is an error to call <code>mongoc_client_destroy</code> on a client that has operations pending. It is required that you release <code>mongoc_collection_t</code> and <code>mongoc_database_t</code> structures before calling <code>mongoc_client_destroy</code> \&amp;. </p>
<h2>Example</h2>
<pre>/* gcc example.c -o example $(pkg-config --cflags --libs libmongoc-1.0) */
/* ./example-client [CONNECTION_STRING [COLLECTION_NAME]] */
#include &lt;mongoc.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int
main (int argc,
 char *argv[])
{
 mongoc_client_t *client;
 mongoc_collection_t *collection;
 mongoc_cursor_t *cursor;
 bson_error_t error;
 const bson_t *doc;
 const char *uristr = &quot;mongodb://127.0.0.1/&quot;;
 const char *collection_name = &quot;test&quot;;
 bson_t query;
 char *str;
 mongoc_init ();
 if (argc &gt; 1) {
 uristr = argv [1];
 }
 if (argc &gt; 2) {
 collection_name = argv [2];
 }
 client = mongoc_client_new (uristr);
 if (!client) {
 fprintf (stderr, &quot;Failed to parse URI.
&quot;);
 return EXIT_FAILURE;
 }
 bson_init (&amp;query);
#if 0
 bson_append_utf8 (&amp;query, &quot;hello&quot;, -1, &quot;world&quot;, -1);
#endif
 collection = mongoc_client_get_collection (client, &quot;test&quot;, collection_name);
 cursor = mongoc_collection_find (collection,
 MONGOC_QUERY_NONE,
 0,
 0,
 0,
 &amp;query,
 NULL, /* Fields, NULL for all. */
 NULL); /* Read Prefs, NULL for default */
 while (mongoc_cursor_next (cursor, &amp;doc)) {
 str = bson_as_json (doc, NULL);
 fprintf (stdout, &quot;%s
&quot;, str);
 bson_free (str);
 }
 if (mongoc_cursor_error (cursor, &amp;error)) {
 fprintf (stderr, &quot;Cursor Failure: %s
&quot;, error.message);
 return EXIT_FAILURE;
 }
 bson_destroy (&amp;query);
 mongoc_cursor_destroy (cursor);
 mongoc_collection_destroy (collection);
 mongoc_client_destroy (client);
 mongoc_cleanup ();
 return EXIT_SUCCESS;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
