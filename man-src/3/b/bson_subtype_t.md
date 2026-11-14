---
title: "bson_subtype_t(3)"
name: "bson_subtype_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_subtype_t/"
description: "bson_subtype_t – Binary Field Subtype"
---

<h2>NAME</h2>
<p> bson_subtype_t &#8211; Binary Field Subtype</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef enum {
    BSON_SUBTYPE_BINARY = 0x00,
    BSON_SUBTYPE_FUNCTION = 0x01,
    BSON_SUBTYPE_BINARY_DEPRECATED = 0x02,
    BSON_SUBTYPE_UUID_DEPRECATED = 0x03,
    BSON_SUBTYPE_UUID = 0x04,
    BSON_SUBTYPE_MD5 = 0x05,
    BSON_SUBTYPE_USER = 0x80,
} bson_subtype_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> This enumeration contains the various subtypes that may be used in a binary field. See <code><a rel="nofollow" href="http://bsonspec.org">http://bsonspec.org</a></code> for more information. </p>
<h2>EXAMPLE</h2>
<pre><code>
bson_t doc = BSON_INITIALIZER;
BSON_APPEND_BINARY(&amp;doc, "binary", BSON_SUBTYPE_BINARY, data, data_len);
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
