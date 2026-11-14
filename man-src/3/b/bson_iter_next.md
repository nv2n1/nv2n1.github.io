---
title: "bson_iter_next(3)"
name: "bson_iter_next"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_next/"
description: "bson_iter_next() – Advances iter to the next element in the document if one exists."
---

<h2>NAME</h2>
<p> bson_iter_next() &#8211; Advances iter to the next element in the document if one exists.</p>
<h2>SYNOPSIS</h2>
<pre>
bool
bson_iter_next (bson_iter_t *iter);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Advances <code>iter</code> to the next element in the document if one exists. </p>
<h2>RETURNS</h2>
<p> true if <code>iter</code> was advanced, otherwise false and <code>iter</code> should be considered invalid. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
