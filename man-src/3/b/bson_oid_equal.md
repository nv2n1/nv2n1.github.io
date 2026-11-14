---
title: "bson_oid_equal(3)"
name: "bson_oid_equal"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_equal/"
description: "bson_oid_equal() – Checks if two bson_oid_t contain the same bytes."
---

<h2>NAME</h2>
<p> bson_oid_equal() &#8211; Checks if two bson_oid_t contain the same bytes.</p>
<h2>SYNOPSIS</h2>
<pre><code>
bool bson_oid_equal(const bson_oid_t *oid1,
                    const bson_oid_t *oid2);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>oid1</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<dl>
<dt><code>oid2</code></p>
<dd> A <code>bson_oid_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> Checks if two bson_oid_t contain the same bytes. </p>
<h2>RETURNS</h2>
<p> true if they are equal, otherwise false. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
