---
title: "bson_oid_init_sequence(3)"
name: "bson_oid_init_sequence"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_init_sequence/"
description: "bson_oid_init_sequence() – Generates a new ObjectID using the 64-bit sequence."
---

<h2>NAME</h2>
<p> bson_oid_init_sequence() &#8211; Generates a new ObjectID using the 64-bit sequence.</p>
<h2>SYNOPSIS</h2>
<pre>
void
bson_oid_init_sequence (bson_oid_t     *oid,
                        bson_context_t *context);
</pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<dl>
<dt><code>context</code></p>
<dd> An optional <code>bson_context_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Generates a new ObjectID using the 64-bit sequence. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> This form of ObjectID is generally used by MongoDB replica peers only.</dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
