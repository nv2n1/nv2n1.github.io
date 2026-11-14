---
title: "mongoc_collection_command_simple(3)"
name: "mongoc_collection_command_simple"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_collection_command_simple/"
description: "mongoc_collection_command_simple() – This is a simplified version of mongoc_collection_command() that returns the first result document in reply. The parameter reply is initialized even upon failur..."
---

<p>mongoc_collection_command_simple() &#8211; This is a simplified version of mongoc_collection_command() that returns the first result document in reply. The parameter reply is initialized even upon failure to simplify memory management.</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_collection_command_simple (mongoc_collection_t *collection,
 const bson_t *command,
 const mongoc_read_prefs_t *read_prefs,
 bson_t *reply,
 bson_error_t *error);</pre>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>collection</code></p>
<dd>A <code>mongoc_collection_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>command</code></p>
<dd>A <code>bson_t</code> containing the command to execute.</dl>
<dl COMPACT>
<dt><code>read_prefs</code></p>
<dd>A <code>mongoc_read_prefs_t</code> or <code>NULL</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>reply</code></p>
<dd>A location to initialize a <code>bson_t</code> \&amp;. This should be on the stack.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Description</h2>
<p>This is a simplified version of <code><a href="/docs/linux/man/3-mongoc_collection_command/">mongoc_collection_command</a>(3)</code> that returns the first result document in <code>reply</code> \&amp;. The parameter <code>reply</code> is initialized even upon failure to simplify memory management. </p>
<p> This function tries to unwrap an embedded error in the command when possible. The unwrapped error will be propagated via the <code>error</code> parameter. Additionally, the result document is set in <code>reply</code> \&amp;. </p>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p><code>true</code> if successful, otherwise <code>false</code> \&amp;. </p>
<p> Not all commands have truly succeeded when <code>{ok:1.0}</code> is returned. This could simply mean the RPC successfully was executed. </p>
<h2>Example</h2>
<p>The following is an example of executing the collection stats command. </p>
<pre>#include &lt;mongoc.h&gt;
#include &lt;bcon.h&gt;
#include &lt;stdio.h&gt;
static void
print_collection_stats (mongoc_collection_t *collection)
{
 bson_error_t error;
 const char *name;
 bson_t *cmd;
 bson_t reply;
 name = mongoc_collection_get_name (collection);
 cmd = BCON_NEW (&quot;collStats&quot;, BCON_UTF8 (name));
 if (mongoc_collection_command_simple (collection, cmd, NULL, &amp;reply, &amp;error)) {
 str = bson_as_json (&amp;reply, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 } else {
 fprintf (stderr, &quot;%s
&quot;, error.message);
 }
 bson_destroy (&amp;reply);
 bson_destroy (cmd);
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
