---
title: "mongoc_find_and_modify_opts_set_bypass_document_validation(3)"
name: "mongoc_find_and_modify_opts_set_bypass_document_validation"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_find_and_modify_opts_set_bypass_document_validation/"
description: "mongoc_find_and_modify_opts_set_bypass_document_validation() – Adds bypassDocumentValidation argument to the builder."
---

<p>mongoc_find_and_modify_opts_set_bypass_document_validation() &#8211; Adds bypassDocumentValidation argument to the builder.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_find_and_modify_opts_set_bypass_document_validation (mongoc_find_and_modify_opts_t *opts,
 bool bypass);</pre>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>New in MongoDB 3.2 and mongoc 1.3.0</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>This option is only available when talking to MongoDB 3.2 and later.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>opts</code></p>
<dd>A <code>mongoc_find_and_modify_opts_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>bypass</code></p>
<dd>If the schema validation rules should be ignored.</dl>
<h2>Description</h2>
<p>Adds bypassDocumentValidation argument to the builder. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>When authentication is enabled, the authenticated user must have either the &quot;dbadmin&quot; or &quot;restore&quot; roles to bypass document validation.</dl>
<h2>Returns</h2>
<p>Returns true if it successfully added the option to the builder. </p>
<h2>Setting Bypassdocumentvalidation</h2>
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
<p>Outputs: </p>
<pre>{
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
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
