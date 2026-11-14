---
title: "bson_iter_array(3)"
name: "bson_iter_array"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_array/"
description: "bson_iter_array() – The bson_iter_array() function shall retrieve the raw buffer of a sub-array from iter. iter MUST be on an element that is of type BSON_TYPE_ARRAY. This can be verified with bson..."
---

<h2>NAME</h2>
<p> bson_iter_array() &#8211; The bson_iter_array() function shall retrieve the raw buffer of a sub-array from iter. iter MUST be on an element that is of type BSON_TYPE_ARRAY. This can be verified with bson_iter_type() or the BSON_ITER_HOLDS_ARRAY() macro.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_iter_array(const bson_iter_t *iter,
                     uint32_t *array_len,
                     const uint8_t **array);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>array_len</code></p>
<dd> A location for the buffer length.</dl>
<dl>
<dt><code>array</code></p>
<dd> A location for the immutable buffer.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_array/">bson_iter_array</a>(3)</code> function shall retrieve the raw buffer of a sub-array from <code>iter</code> \&amp;. <code>iter</code> </p>
<p> <code>MUST</code> be on an element that is of type BSON_TYPE_ARRAY. This can be verified with <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> or the <code><a href="/docs/linux/man/3-bson_iter_holds_array/">BSON_ITER_HOLDS_ARRAY</a>(3)</code> macro. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
