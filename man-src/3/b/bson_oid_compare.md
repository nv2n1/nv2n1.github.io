---
title: "bson_oid_compare(3)"
name: "bson_oid_compare"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_oid_compare/"
description: "bson_oid_compare() – The bson_oid_compare() function shall return a qsort() style value of a lexicographical sort of _oid1_ and _oid2_."
---

<h2>NAME</h2>
<p> bson_oid_compare() &#8211; The bson_oid_compare() function shall return a qsort() style value of a lexicographical sort of _oid1_ and _oid2_.</p>
<h2>SYNOPSIS</h2>
<pre><code>
int bson_oid_compare(const bson_oid_t *oid1,
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
<p> The <code><a href="/docs/linux/man/3-bson_oid_compare/">bson_oid_compare</a>(3)</code> function shall return a qsort() style value of a lexicographical sort of _oid1_ and _oid2_. </p>
<h2>RETURNS</h2>
<p> less than 0, 0, or greater than 0 based on the comparison. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
