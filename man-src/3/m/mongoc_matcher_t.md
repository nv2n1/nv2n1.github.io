---
title: "mongoc_matcher_t(3)"
name: "mongoc_matcher_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_matcher_t/"
description: "mongoc_matcher_t – Client-side document matching abstraction"
---

<p>mongoc_matcher_t &#8211; Client-side document matching abstraction</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_matcher_t mongoc_matcher_t;</pre>
<p><code>mongoc_matcher_t</code> provides a reduced-interface for client-side matching of BSON documents. </p>
<p> It can perform the basics such as $in, $nin, $eq, $neq, $gt, $gte, $lt, and $lte. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_matcher_t</code> does not currently support the full spectrum of query operations that the MongoDB server supports.</dl>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_matcher_t</code> is deprecated and will be removed in version 2.0.</dl>
<h2>Example</h2>
<pre>#include &lt;bcon.h&gt;
#include &lt;bson.h&gt;
#include &lt;mongoc.h&gt;
#include &lt;stdio.h&gt;
int
main (int argc,
 char *argv[])
{
 mongoc_matcher_t *matcher;
 bson_reader_t *reader;
 const bson_t *bson;
 bson_t *spec;
 char *str;
 int fd;
 mongoc_init ();
#ifdef _WIN32
 fd = fileno (stdin);
#else
 fd = STDIN_FILENO;
#endif
 reader = bson_reader_new_from_fd (fd, false);
 spec = BCON_NEW (&quot;hello&quot;, &quot;world&quot;);
 matcher = mongoc_matcher_new (spec, NULL);
 while ((bson = bson_reader_read (reader, NULL))) {
 if (mongoc_matcher_match (matcher, bson)) {
 str = bson_as_json (bson, NULL);
 printf (&quot;%s
&quot;, str);
 bson_free (str);
 }
 }
 bson_reader_destroy (reader);
 bson_destroy (spec);
 mongoc_cleanup ();
 return 0;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
