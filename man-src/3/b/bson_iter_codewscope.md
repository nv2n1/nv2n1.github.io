---
title: "bson_iter_codewscope(3)"
name: "bson_iter_codewscope"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_codewscope/"
description: "bson_iter_codewscope() – The bson_iter_codewscope() function acts similar to bson_iter_code() except for BSON_TYPE_CODEWSCOPE elements. It also will provide a pointer to the buffer for scope, which..."
---

<h2>NAME</h2>
<p> bson_iter_codewscope() &#8211; The bson_iter_codewscope() function acts similar to bson_iter_code() except for BSON_TYPE_CODEWSCOPE elements. It also will provide a pointer to the buffer for scope, which can be loaded into a bson_t using bson_init_static().</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_CODEWSCOPE(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_CODEWSCOPE)
const char *
bson_iter_codewscope(const bson_iter_t *iter,
                     uint32_t *length,
                     uint32_t *scope_len,
                     const uint8_t **scope);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<dl>
<dt><code>length</code></p>
<dd> An optional location for the length of the resulting UTF-8 encoded string.</dl>
<dl>
<dt><code>scope_len</code></p>
<dd> A optional location for the length of <code>scope</code> \&amp;.</dl>
<dl>
<dt><code>scope</code></p>
<dd> An optional location to store the immutable raw scope BSON document.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_iter_codewscope/">bson_iter_codewscope</a>(3)</code> function acts similar to <code><a href="/docs/linux/man/3-bson_iter_code/">bson_iter_code</a>(3)</code> except for BSON_TYPE_CODEWSCOPE elements. It also will provide a pointer to the buffer for scope, which can be loaded into a <code>bson_t</code> using <code><a href="/docs/linux/man/3-bson_init_static/">bson_init_static</a>(3)</code> \&amp;. </p>
<h2>RETURNS</h2>
<p> An UTF-8 encoded string containing the JavaScript code which should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
