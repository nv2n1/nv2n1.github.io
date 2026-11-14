---
title: "bson_iter_double(3)"
name: "bson_iter_double"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_double/"
description: "bson_iter_double() – Fetches the contents of a BSON_TYPE_DOUBLE field."
---

<h2>NAME</h2>
<p> bson_iter_double() &#8211; Fetches the contents of a BSON_TYPE_DOUBLE field.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_DOUBLE(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_DOUBLE)
double
bson_iter_double(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the contents of a BSON_TYPE_DOUBLE field. </p>
<h2>RETURNS</h2>
<p> A double. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
