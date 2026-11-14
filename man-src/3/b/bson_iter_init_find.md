---
title: "bson_iter_init_find(3)"
name: "bson_iter_init_find"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_init_find/"
description: "bson_iter_init_find() – This function is identical to (bson_iter_init() && bson_iter_find())."
---

<h2>NAME</h2>
<p> bson_iter_init_find() &#8211; This function is identical to (bson_iter_init() &amp;&amp; bson_iter_find()).</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_iter_init_find(bson_iter_t *iter,
                         const bson_t *bson,
                         const char *key);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>key</code></p>
<dd> A key to locate after initializing the iter.</dl>
<h2>DESCRIPTION</h2>
<p> This function is identical to <code>(<a href="/docs/linux/man/3-bson_iter_init/">bson_iter_init</a>(3) &amp;&amp; <a href="/docs/linux/man/3-bson_iter_find/">bson_iter_find</a>(3))</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
