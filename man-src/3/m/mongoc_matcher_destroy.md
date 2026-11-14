---
title: "mongoc_matcher_destroy(3)"
name: "mongoc_matcher_destroy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_matcher_destroy/"
description: "mongoc_matcher_destroy() – None"
---

<p>mongoc_matcher_destroy() &#8211; None</p>
<h2>Synopsis</h2>
<pre>void
mongoc_matcher_destroy (mongoc_matcher_t *matcher);</pre>
<p>Release all resources associated with <code>matcher</code> including freeing the structure. </p>
<h2>Deprecated</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_matcher_t</code> is deprecated and will be removed in version 2.0.</dl>
<h2>Parameters</h2>
<dl COMPACT>
<dt><code>matcher</code></p>
<dd>A <code>mongoc_matcher_t</code> \&amp;.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
