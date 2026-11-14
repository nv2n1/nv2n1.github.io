---
title: "bson_iter_oid(3)"
name: "bson_iter_oid"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_iter_oid/"
description: "bson_iter_oid() – Fetches the bson_oid_t for a BSON_TYPE_OID element. You should verify it is an element of type BSON_TYPE_OID before calling this function."
---

<h2>NAME</h2>
<p> bson_iter_oid() &#8211; Fetches the bson_oid_t for a BSON_TYPE_OID element. You should verify it is an element of type BSON_TYPE_OID before calling this function.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#define BSON_ITER_HOLDS_OID(iter) \
    (bson_iter_type((iter)) == BSON_TYPE_OID)
const bson_oid_t *
bson_iter_oid(const bson_iter_t *iter);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>iter</code></p>
<dd> A <code>bson_iter_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Fetches the <code>bson_oid_t</code> for a BSON_TYPE_OID element. You should verify it is an element of type BSON_TYPE_OID before calling this function. </p>
<h2>RETURNS</h2>
<p> A <code>bson_oid_t</code> that should not be modified or freed. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
