---
title: "bson_iter_int64(3)"
name: "bson_iter_int64"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_int64/"
description: "bson_iter_int64() – Fetches the value from a BSON_TYPE_INT64 field. You should verify that this is a BSON_TYPE_INT64 field before calling this function."
---

<h2>NAME</h2>
<p> bson_iter_int64() &#8211; Fetches the value from a BSON_TYPE_INT64 field. You should verify that this is a BSON_TYPE_INT64 field before calling this function.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_INT64(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_INT64)
int64_t
bson_iter_int64(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the value from a BSON_TYPE_INT64 field. You should verify that this is a BSON_TYPE_INT64 field before calling this function. </p>
<h2>RETURNS</h2>
<p> A 64-bit integer. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
