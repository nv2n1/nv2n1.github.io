---
title: "bson_string_t(3)"
name: "bson_string_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_string_t/"
description: "bson_string_t – String Building Abstraction"
---

<h2>NAME</h2>
<p> bson_string_t &#8211; String Building Abstraction</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct
{
    char *str;
    uint32_t len;
    uint32_t alloc;
} bson_string_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>bson_string_t</code> is an abstraction for building strings. As chunks are added to the string, allocations are performed in powers of two. </p>
<p> This API is useful if you need to build UTF-8 encoded strings. </p>
<h2>EXAMPLE</h2>
<pre><code>
bson_string_t *str;
str = bson_string_new(NULL);
bson_string_append_printf(str, "%d %s %f
", 0, "some string", 0.123);
printf("%s
", str-&gt;str);
bson_string_free(str, true);
</code></pre>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> You can call <code><a href="/docs/linux/man/3-bson_string_free/">bson_string_free</a>(3)</code> with <code>false</code> if you would like to take ownership of <code>str-&gt;str</code> \&amp;. Some APIs that do this might call <code>return bson_string_free (str, false);</code> after building the string.</dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
