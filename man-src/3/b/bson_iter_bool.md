---
title: "bson_iter_bool(3)"
name: "bson_iter_bool"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_bool/"
description: "bson_iter_bool() – The bson_iter_bool()function shall return the boolean value of a BSON_TYPE_BOOL element. It is a programming error to call this function on an element other than BSON_TYPE_BOOL. ..."
---

<h2>NAME</h2>
<p> bson_iter_bool() &#8211; The bson_iter_bool()function shall return the boolean value of a BSON_TYPE_BOOL element. It is a programming error to call this function on an element other than BSON_TYPE_BOOL. You can check this with bson_iter_type() or BSON_ITER_HOLDS_BOOL().</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_BOOL(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_BOOL)
bool bson_iter_bool(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_bool/">bson_iter_bool</a>(3)</code> function shall return the boolean value of a BSON_TYPE_BOOL element. It is a programming error to call this function on an element other than BSON_TYPE_BOOL. You can check this with <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> or <code><a href="/docs/linux/man/3-bson_iter_holds_bool/">BSON_ITER_HOLDS_BOOL</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> Either <code>true</code> or <code>false</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
