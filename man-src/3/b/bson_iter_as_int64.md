---
title: "bson_iter_as_int64(3)"
name: "bson_iter_as_int64"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_as_int64/"
description: "bson_iter_as_int64() – The bson_iter_as_int64() function shall return the contents of the current element as if it were a BSON_TYPE_INT64 element. The currently supported casts include:"
---

<h2>NAME</h2>
<p> bson_iter_as_int64() &#8211; The bson_iter_as_int64() function shall return the contents of the current element as if it were a BSON_TYPE_INT64 element. The currently supported casts include:</p>
<h2>SYNOPSIS</h2>
<pre><code>
int64_t
bson_iter_as_int64(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_as_int64/">bson_iter_as_int64</a>(3)</code> function shall return the contents of the current element as if it were a BSON_TYPE_INT64 element. The currently supported casts include: </p>
<dl>
<dt>\[bu]</p>
<dd> BSON_TYPE_BOOL</p>
<dt>\[bu]</p>
<dd> BSON_TYPE_DOUBLE</p>
<dt>\[bu]</p>
<dd> BSON_TYPE_INT32</p>
<dt>\[bu]</p>
<dd> BSON_TYPE_INT64 </p>
</dl>
<h2>RETURNS</h2>
<p> A 64-bit signed integer. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
