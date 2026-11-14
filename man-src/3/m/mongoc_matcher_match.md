---
title: "mongoc_matcher_match(3)"
name: "mongoc_matcher_match"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_matcher_match/"
description: "mongoc_matcher_match() – None"
---

<p>mongoc_matcher_match() &#8211; None</p>
<h2>Synopsis</h2>
<pre>bool
mongoc_matcher_match (const mongoc_matcher_t *matcher,
 const bson_t *document);</pre>
<p>This function will check to see if the query compiled in <code>matcher</code> matches <code>document</code> \&amp;. </p>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_matcher_t</code> is deprecated and will be removed in version 2.0.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>matcher</code></p>
<dd>A <code>mongoc_matcher_t</code> \&amp;.</dl>
<dl COMPACT>
<dt><code>query</code></p>
<dd>A <code>bson_t</code> that contains the query.</dl>
<h2>Returns</h2>
<p><code>true</code> if <code>document</code> matches the query specification provided to <code><a href="/docs/linux/man/3-mongoc_matcher_new/">mongoc_matcher_new</a>(3)</code> \&amp;. Otherwise, <code>false</code> \&amp;. </p>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
