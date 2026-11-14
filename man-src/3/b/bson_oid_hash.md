---
title: "bson_oid_hash(3)"
name: "bson_oid_hash"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_hash/"
description: "bson_oid_hash() – Generates a hash code for oid suitable for a hashtable."
---

<h2>NAME</h2>
<p> bson_oid_hash() &#8211; Generates a hash code for oid suitable for a hashtable.</p>
<h2>SYNOPSIS</h2>
<pre><code>
uint32_t
bson_oid_hash(const bson_oid_t *oid);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Generates a hash code for <code>oid</code> suitable for a hashtable. </p>
<h2>RETURNS</h2>
<p> A 32-bit hash code. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
