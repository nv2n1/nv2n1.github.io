---
title: "mongoc_client_pool_t(3)"
name: "mongoc_client_pool_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_client_pool_t/"
description: "mongoc_client_pool_t – Connection pooling abstraction"
---

<p>mongoc_client_pool_t &#8211; Connection pooling abstraction</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_client_pool_t mongoc_client_pool_t</pre>
<p><code>mongoc_client_pool_t</code> is the basis for multi-threading in the MongoDB C driver. Since <code>mongoc_client_t</code> structures are not thread-safe, this structure is used to retrieve a new <code>mongoc_client_t</code> for a given thread. This structure <code>is thread-safe</code> \&amp;. </p>
<h2>Example</h2>
<pre>#include &lt;mongoc.h&gt;
static void *
worker (void *data)
{
 mongoc_client_pool_t *pool = data;
 mongoc_client_t *client;
 do {
 client = mongoc_client_pool_pop (pool);
 /*
 * Do something with client. If you are writing an HTTP server, you
 * probably only want to hold onto the client for the portion of the
 * request performing database queries.
 */
 mongoc_client_pool_push (pool, client);
 } while (!inShutdown);
 return NULL;
}
int main (int argc, char *argv[])
{
 mongoc_client_pool_t *pool;
 mongoc_uri_t *uri;
 pthread_t thread[10];
 unsigned i;
 void *ret;
 mongoc_init ();
 uri = mongoc_uri_new (&quot;mongodb://mdb1.example.com/?minPoolSize=16&quot;);
 pool = mongoc_client_pool_new (uri);
 for (i = 0; i &lt; 10; i++) {
 pthread_create (&amp;thread, NULL, worker, pool);
 }
 mongoc_uri_destroy (uri);
 for (i = 0; i &lt; 10; i++) {
 pthread_join (threads [i], &amp;ret);
 }
 mongoc_cleanup ();
 return 0;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
