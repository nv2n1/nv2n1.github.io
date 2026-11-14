---
title: "bson_compare(3)"
name: "bson_compare"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_compare/"
description: "bson_compare() – The bson_compare() function shall compare two bson documents for equality."
---

<h2>NAME</h2>
<p> bson_compare() &#8211; The bson_compare() function shall compare two bson documents for equality.</p>
<h2>SYNOPSIS</h2>
<pre><code>
int bson_compare(const bson_t *bson,
                 const bson_t *other);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>bson</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<dl>
<dt><code>other</code></p>
<dd> A <code>bson_t</code> \&amp;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/3-bson_compare/">bson_compare</a>(3)</code> function shall compare two bson documents for equality. </p>
<p> This can be useful in conjunction with _qsort()_. </p>
<p> If equal, 0 is returned. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> This function uses _memcmp()_ internally, so the semantics are the same.</dl>
<h2>RETURNS</h2>
<p> less than zero, zero, or greater than zero in <code><a href="/docs/linux/man/3-qsort/">qsort</a>(3)</code> style. </p>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
