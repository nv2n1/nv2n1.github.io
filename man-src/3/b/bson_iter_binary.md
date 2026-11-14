---
title: "bson_iter_binary(3)"
name: "bson_iter_binary"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_binary/"
description: "bson_iter_binary() – This function shall return the binary data of a BSON_TYPE_BINARY element. It is a programming error to call this function on a field that is not of type BSON_TYPE_BINARY. You c..."
---

<h2>NAME</h2>
<p> bson_iter_binary() &#8211; This function shall return the binary data of a BSON_TYPE_BINARY element. It is a programming error to call this function on a field that is not of type BSON_TYPE_BINARY. You can check this with the BSON_ITER_HOLDS_BINARY() macro or bson_iter_type().</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_BINARY(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_BINARY)
void bson_iter_binary(const bson_iter_t *iter,
                      bson_subtype_t *subtype,
                      uint32_t *binary_len,
                      const uint8_t **binary);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>subtype</code></p>
<dd> A location for a <code>bson_subtype_t</code> or NULL.</dl>
<dl>
<dt><code>binary_len</code></p>
<dd> A location for the length of <code>binary</code> \&amp;.</dl>
<dl>
<dt><code>binary</code></p>
<dd> A location for a pointer to the immutable buffer.</dl>
<h2>DESCRIPTION</h2>
<p> This function shall return the binary data of a BSON_TYPE_BINARY element. It is a programming error to call this function on a field that is not of type BSON_TYPE_BINARY. You can check this with the BSON_ITER_HOLDS_BINARY() macro or <code><a href="/docs/linux/man/3-bson_iter_type/">bson_iter_type</a>(3)</code> \&amp;. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
