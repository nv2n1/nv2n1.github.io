---
title: "mongoc_matcher_new(3)"
name: "mongoc_matcher_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_matcher_new/"
description: "mongoc_matcher_new() – None"
---

<p>mongoc_matcher_new() &#8211; None</p>
<h2>Synopsis</h2>
<pre>mongoc_matcher_t *
mongoc_matcher_new (const bson_t *query,
 bson_error_t *error);</pre>
<p>Create a new <code>mongoc_matcher_t</code> using the query specification provided. </p>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_matcher_t</code> is deprecated and will be removed in version 2.0.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>error</code></p>
<dd>An optional location for a <code>bson_error_t</code> or <code>NULL</code> \&amp;.</dl>
<h2>Errors</h2>
<p>Errors are propagated via the <code>error</code> parameter. </p>
<h2>Returns</h2>
<p>A newly allocated <code>mongoc_matcher_t</code> that should be freed with <code><a href="/docs/linux/man/3-mongoc_matcher_destroy/">mongoc_matcher_destroy</a>(3)</code> when no longer in use. Upon failure, <code>NULL</code> is returned and <code>error</code> is set. This could happen if <code>query</code> contains an invalid query specification. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
