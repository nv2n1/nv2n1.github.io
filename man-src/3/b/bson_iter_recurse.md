---
title: "bson_iter_recurse(3)"
name: "bson_iter_recurse"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_recurse/"
description: "bson_iter_recurse() – The bson_iter_recurse() function shall initialize child using the embedded document or array currently observed by iter."
---

<h2>NAME</h2>
<p> bson_iter_recurse() &#8211; The bson_iter_recurse() function shall initialize child using the embedded document or array currently observed by iter.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_iter_recurse (const bson_iter_t *iter,
                   bson_iter_t       *child);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>child</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_recurse/">bson_iter_recurse</a>(3)</code> function shall initialize <code>child</code> using the embedded document or array currently observed by <code>iter</code> \&amp;. </p>
<p> If there was a failure to initialize the <code>iter</code> , false is returned and both <code>iter</code> and <code>child</code> should be considered invalid. </p>
<p> This should only be called when observing an element of type BSON_TYPE_ARRAY or BSON_TYPE_DOCUMENT. </p>
<h2>RETURNS</h2>
<p> true if <code>child</code> has been intialized. Otherwise, both <code>child</code> and <code>iter</code> should be considered invalid. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
