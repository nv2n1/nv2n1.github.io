---
title: "mongoc_find_and_modify_opts_t(3)"
name: "mongoc_find_and_modify_opts_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_t/"
description: "mongoc_find_and_modify_opts_t – find_and_modify abstraction"
---

<p>mongoc_find_and_modify_opts_t &#8211; find_and_modify abstraction</p>
<h2>Synopsis</h2>
<p><code>mongoc_find_and_modify_opts_t</code> is a builder interface to construct a <code>find_and_modify</code> command. </p>
<p> It was created to be able to accommodate new arguments to the MongoDB find_and_modify command. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>New in mongoc 1.3.0</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>As of MongoDB 3.2, the <code>mongoc_write_concern_t</code> specified on the <code>mongoc_collection_t</code> will be used, if any.</dl>
<h2>Example</h2>
<pre>void fam_flags(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bson_t *update;
 bool success;
 /* Find Zlatan Ibrahimovic, the striker */
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;profession&quot;, &quot;Football player&quot;);
 BSON_APPEND_INT32 (&amp;query, &quot;age&quot;, 34);
 BSON_APPEND_INT32 (&amp;query, &quot;goals&quot;, (16+35+23+57+16+14+28+84)+(1+6+62));
 /* Add his football position */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;,
 &quot;position&quot;, BCON_UTF8 (&quot;striker&quot;),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 /* Create the document if it didn't exist, and return the updated document */
 mongoc_find_and_modify_opts_set_flags (opts, MONGOC_FIND_AND_MODIFY_UPSERT|MONGOC_FIND_AND_MODIFY_RETURN_NEW);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<pre>void fam_bypass(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t reply;
 bson_t *update;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find Zlatan Ibrahimovic, the striker */
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;profession&quot;, &quot;Football player&quot;);
 /* Bump his age */
 update = BCON_NEW (&quot;$inc&quot;, &quot;{&quot;,
 &quot;age&quot;, BCON_INT32 (1),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 /* He can still play, even though he is pretty old. */
 mongoc_find_and_modify_opts_set_bypass_document_validation (opts, true);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<pre>void fam_update(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t *update;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find Zlatan Ibrahimovic */
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 /* Make him a book author */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;,
 &quot;author&quot;, BCON_BOOL (true),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 /* Note that the document returned is the _previous_ version of the document
 * To fetch the modified new version, use
 * mongoc_find_and_modify_opts_set_flags (opts, MONGOC_FIND_AND_MODIFY_RETURN_NEW);
 */
 mongoc_find_and_modify_opts_set_update (opts, update);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<pre>void fam_fields(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t fields = BSON_INITIALIZER;
 bson_t *update;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find Zlatan Ibrahimovic */
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 BSON_APPEND_UTF8 (&amp;query, &quot;firstname&quot;, &quot;Zlatan&quot;);
 /* Return his goal tally */
 BSON_APPEND_INT32 (&amp;fields, &quot;goals&quot;, 1);
 /* Bump his goal tally */
 update = BCON_NEW (&quot;$inc&quot;, &quot;{&quot;,
 &quot;goals&quot;, BCON_INT32 (1),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 mongoc_find_and_modify_opts_set_fields (opts, &amp;fields);
 /* Return the new tally */
 mongoc_find_and_modify_opts_set_flags (opts, MONGOC_FIND_AND_MODIFY_RETURN_NEW);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;fields);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<pre>void fam_sort(mongoc_collection_t *collection)
{
 mongoc_find_and_modify_opts_t *opts;
 bson_t *update;
 bson_t sort = BSON_INITIALIZER;
 bson_t reply;
 bson_error_t error;
 bson_t query = BSON_INITIALIZER;
 bool success;
 /* Find all users with the lastname Ibrahimovic */
 BSON_APPEND_UTF8 (&amp;query, &quot;lastname&quot;, &quot;Ibrahimovic&quot;);
 /* Sort by age (descending) */
 BSON_APPEND_INT32 (&amp;sort, &quot;age&quot;, -1);
 /* Bump his goal tally */
 update = BCON_NEW (&quot;$set&quot;, &quot;{&quot;,
 &quot;oldest&quot;, BCON_BOOL (true),
 &quot;}&quot;);
 opts = mongoc_find_and_modify_opts_new ();
 mongoc_find_and_modify_opts_set_update (opts, update);
 mongoc_find_and_modify_opts_set_sort (opts, &amp;sort);
 success = mongoc_collection_find_and_modify_with_opts (collection, &amp;query, opts, &amp;reply, &amp;error);
 if (success) {
 char *str;
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 }
 bson_destroy (&amp;reply);
 bson_destroy (update);
 bson_destroy (&amp;sort);
 bson_destroy (&amp;query);
 mongoc_find_and_modify_opts_destroy (opts);
}</pre>
<pre>#include &lt;bcon.h&gt;
#include &lt;mongoc.h&gt;
#include &quot;flags.c&quot;
#include &quot;bypass.c&quot;
#include &quot;update.c&quot;
#include &quot;fields.c&quot;
#include &quot;sort.c&quot;
int main(void)
{
 mongoc_collection_t *collection;
 mongoc_database_t *database;
 mongoc_client_t *client;
 bson_error_t error;
 bson_t *options;
 client = mongoc_client_new (&quot;mongodb://localhost:27017/admin&quot;);
 database = mongoc_client_get_database (client, &quot;databaseName&quot;);
 options = BCON_NEW ( &quot;validator&quot;, &quot;{&quot;, &quot;age&quot;, &quot;{&quot;, &quot;$lte&quot;, BCON_INT32 (34), &quot;}&quot;, &quot;}&quot;, &quot;validationAction&quot;, BCON_UTF8 (&quot;error&quot;), &quot;validationLevel&quot;, BCON_UTF8 (&quot;moderate&quot;));
 collection = mongoc_database_create_collection (database, &quot;collectionName&quot;, options, &amp;error);
 if (!collection) {
 fprintf(stderr, &quot;Got error: \&quot;%s\&quot; on line %d
&quot;, error.message, __LINE__);
 return 1;
 }
 fam_flags (collection);
 fam_bypass (collection);
 fam_update (collection);
 fam_fields (collection);
 fam_sort (collection);
 mongoc_collection_drop (collection, NULL);
 bson_destroy (options);
 mongoc_database_destroy (database);
 mongoc_collection_destroy (collection);
 mongoc_client_destroy (client);
 return 0;
}</pre>
<p>Outputs: </p>
<pre>{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: false,
 &quot;n&quot;: 1,
 &quot;upserted&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 }
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 34,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 342,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;
 },
 &quot;ok&quot;: 1
}
{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: true,
 &quot;n&quot;: 1
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 34,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 342,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;
 },
 &quot;ok&quot;: 1
}
{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: true,
 &quot;n&quot;: 1
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 35,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 342,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;
 },
 &quot;ok&quot;: 1
}
{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: true,
 &quot;n&quot;: 1
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;goals&quot;: 343
 },
 &quot;ok&quot;: 1
}
{
 &quot;lastErrorObject&quot;: {
 &quot;updatedExisting&quot;: true,
 &quot;n&quot;: 1
 },
 &quot;value&quot;: {
 &quot;_id&quot;: {
 &quot;$oid&quot;: &quot;56562a99d13e6d86239c7b00&quot;
 },
 &quot;age&quot;: 35,
 &quot;firstname&quot;: &quot;Zlatan&quot;,
 &quot;goals&quot;: 343,
 &quot;lastname&quot;: &quot;Ibrahimovic&quot;,
 &quot;profession&quot;: &quot;Football player&quot;,
 &quot;position&quot;: &quot;striker&quot;,
 &quot;author&quot;: true
 },
 &quot;ok&quot;: 1
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
