---
title: "bson_oid_init_from_data(3)"
name: "bson_oid_init_from_data"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_init_from_data/"
description: "bson_oid_init_from_data() – Initializes a bson_oid_t using the raw buffer provided."
---

<h2>NAME</h2>
<p> bson_oid_init_from_data() &#8211; Initializes a bson_oid_t using the raw buffer provided.</p>
<h2>SYNOPSIS</h2>
<pre><code>
void bson_oid_init_from_data(bson_oid_t *oid,
                             const uint8_t *data);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<dl>
<dt><code>data</code></p>
<dd> A buffer containing 12 bytes for the oid.</dl>
<h2>DESCRIPTION</h2>
<p> Initializes a <code>bson_oid_t</code> using the raw buffer provided. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
