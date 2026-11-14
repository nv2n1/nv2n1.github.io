---
title: "bson_iter_find_descendant(3)"
name: "bson_iter_find_descendant"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_find_descendant/"
description: "bson_iter_find_descendant() – The bson_iter_find_descendant() function shall follow standard MongoDB dot notation to recurse into subdocuments. descendant will be initialized and advanced to the de..."
---

<h2>NAME</h2>
<p> bson_iter_find_descendant() &#8211; The bson_iter_find_descendant() function shall follow standard MongoDB dot notation to recurse into subdocuments. descendant will be initialized and advanced to the descendant. If false is returned, both iter and descendant should be considered invalid.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_iter_find_descendant(bson_iter_t *iter,
                               const char *dotkey,
                               bson_iter_t *descendant);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>dotkey</code></p>
<dd> A dot-notation key like <code>a.b.c.d</code> \&amp;.</dl>
<dl>
<dt><code>descendant</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_find_descendant/">bson_iter_find_descendant</a>(3)</code> function shall follow standard MongoDB dot notation to recurse into subdocuments. <code>descendant</code> will be initialized and advanced to the descendant. If false is returned, both <code>iter</code> and <code>descendant</code> should be considered invalid. </p>
<h2>RETURNS</h2>
<p> true is returned if the requested key was found. If not, false is returned and <code>iter</code> was exhausted and should now be considered invalid. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
