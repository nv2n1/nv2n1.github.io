---
title: "bson_iter_overwrite_double(3)"
name: "bson_iter_overwrite_double"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_overwrite_double/"
description: "bson_iter_overwrite_double() – The bson_iter_overwrite_double() function shall overwrite the contents of a BSON_TYPE_DOUBLE element in place."
---

<h2>NAME</h2>
<p> bson_iter_overwrite_double() &#8211; The bson_iter_overwrite_double() function shall overwrite the contents of a BSON_TYPE_DOUBLE element in place.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_iter_overwrite_double(bson_iter_t *iter,
                                double value);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>value</code></p>
<dd> The new double value.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_overwrite_double/">bson_iter_overwrite_double</a>(3)</code> function shall overwrite the contents of a BSON_TYPE_DOUBLE element in place. </p>
<p> This may only be done when the underlying bson document allows mutation. </p>
<p> It is a programming error to call this function when <code>iter</code> is not obvserving an element of type BSON_TYPE_DOUBLE. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
