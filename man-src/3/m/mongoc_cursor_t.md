---
title: "mongoc_cursor_t(3)"
name: "mongoc_cursor_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cursor_t/"
description: "mongoc_cursor_t – Client-side cursor abtraction"
---

<p>mongoc_cursor_t &#8211; Client-side cursor abtraction</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_cursor_t mongoc_cursor_t;</pre>
<p><code>mongoc_cursor_t</code> provides access to a MongoDB query cursor. It wraps up the wire protocol negotiation required to initiate a query and retrieve an unknown number of documents. </p>
<p> Cursors are lazy, meaning that no network traffic occurs until the first call to <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> \&amp;. </p>
<p> At that point we can: </p>
<dl COMPACT>
<dt>\[bu]</p>
<dd>Determine which host we&#8217;ve connected to with <code><a href="/docs/linux/man/3-mongoc_cursor_get_host/">mongoc_cursor_get_host</a>(3)</code> \&amp;.</p>
<dt>\[bu]</p>
<dd>Retrieve more records with repeated calls to <code><a href="/docs/linux/man/3-mongoc_cursor_next/">mongoc_cursor_next</a>(3)</code> \&amp;.</p>
<dt>\[bu]</p>
<dd>Test for more records with <code><a href="/docs/linux/man/3-mongoc_cursor_more/">mongoc_cursor_more</a>(3)</code></p>
<dt>\[bu]</p>
<dd>Clone a query to repeat execution at a later point with <code><a href="/docs/linux/man/3-mongoc_cursor_clone/">mongoc_cursor_clone</a>(3)</code> \&amp;.</p>
<dt>\[bu]</p>
<dd>Test for errors with <code><a href="/docs/linux/man/3-mongoc_cursor_error/">mongoc_cursor_error</a>(3)</code> \&amp;. </p>
</dl>
<h2>Thread Safety</h2>
<p><code>mongoc_cursor_t</code> is <code>NOT</code> thread safe. It may only be used from the thread it was created from. </p>
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
